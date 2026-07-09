#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/image.hpp"
#include "nav_msgs/msg/odometry.hpp"
#include "geometry_msgs/msg/pose_stamped.hpp"
#include <cv_bridge/cv_bridge.h>
#include "opencv2/opencv.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "zbar.h"
#include <std_msgs/msg/string.hpp>

class QrCodeDetection : public rclcpp::Node
{
public:
  QrCodeDetection() : Node("qr_decoder_zbar")
  {
    this->declare_parameter<std::string>("rgb_topic", "/aurora/rgb/image_raw");
    this->declare_parameter<std::string>("depth_topic", "/aurora/depth/image_raw");
    this->declare_parameter<bool>("enable_depth_filter", true);
    this->declare_parameter<int>("depth_min_mm", 50);
    this->declare_parameter<int>("depth_max_mm", 4000);
    this->declare_parameter<int>("min_qr_length", 1);
    this->declare_parameter<double>("fx", 421.307);
    this->declare_parameter<double>("fy", 422.254);
    this->declare_parameter<double>("cx", 320.27);
    this->declare_parameter<double>("cy", 197.01);

    rgb_topic_ = this->get_parameter("rgb_topic").as_string();
    depth_topic_ = this->get_parameter("depth_topic").as_string();
    enable_depth_filter_ = this->get_parameter("enable_depth_filter").as_bool();
    depth_min_mm_ = this->get_parameter("depth_min_mm").as_int();
    depth_max_mm_ = this->get_parameter("depth_max_mm").as_int();
    min_qr_length_ = this->get_parameter("min_qr_length").as_int();
    fx_ = this->get_parameter("fx").as_double();
    fy_ = this->get_parameter("fy").as_double();
    cx_ = this->get_parameter("cx").as_double();
    cy_ = this->get_parameter("cy").as_double();

    rgb_sub_ = this->create_subscription<sensor_msgs::msg::Image>(
      rgb_topic_, 10,
      std::bind(&QrCodeDetection::rgbCallback, this, std::placeholders::_1));

    depth_sub_ = this->create_subscription<sensor_msgs::msg::Image>(
      depth_topic_, 10,
      std::bind(&QrCodeDetection::depthCallback, this, std::placeholders::_1));

    sign_com_pub = this->create_publisher<std_msgs::msg::String>("/sign", 10);
    sign_pose_pub_ = this->create_publisher<geometry_msgs::msg::PoseStamped>("/sign_pose", 10);

    odom_sub_ = this->create_subscription<nav_msgs::msg::Odometry>(
      "/odom", 10,
      std::bind(&QrCodeDetection::odomCallback, this, std::placeholders::_1));

    scanner_.set_config(zbar::ZBAR_NONE, zbar::ZBAR_CFG_ENABLE, 0);  // disable all
    scanner_.set_config(zbar::ZBAR_QRCODE, zbar::ZBAR_CFG_ENABLE, 1); // QR only
    scanner_.enable_cache(true);

    frame_count_ = 0;
    last_qr_frame_ = -1;
    consecutive_rejects_ = 0;

    RCLCPP_INFO(this->get_logger(),
      "QR decoder (ZBar) started: rgb=%s, depth=%s, filter=%s, range=[%d, %d]mm, "
      "min_qr_len=%d, intrinsics: fx=%.1f fy=%.1f cx=%.1f cy=%.1f",
      rgb_topic_.c_str(), depth_topic_.c_str(),
      enable_depth_filter_ ? "on" : "off",
      depth_min_mm_, depth_max_mm_, min_qr_length_,
      fx_, fy_, cx_, cy_);
  }

private:
  void odomCallback(const nav_msgs::msg::Odometry::SharedPtr msg)
  {
    odom_x_ = msg->pose.pose.position.x;
    odom_y_ = msg->pose.pose.position.y;
    double qw = msg->pose.pose.orientation.w;
    double qz = msg->pose.pose.orientation.z;
    odom_yaw_ = std::atan2(2.0 * qw * qz, 1.0 - 2.0 * qz * qz);
  }

  void depthCallback(const sensor_msgs::msg::Image::SharedPtr msg)
  {
    try {
      latest_depth_ = cv_bridge::toCvCopy(msg, "mono16")->image;
    } catch (const cv_bridge::Exception &e) {
      RCLCPP_ERROR(this->get_logger(), "cv_bridge depth error: %s", e.what());
    }
  }

  void rgbCallback(const sensor_msgs::msg::Image::SharedPtr msg)
  {
    cv::Mat frame;
    try {
      frame = cv_bridge::toCvCopy(msg, "bgr8")->image;
    } catch (const cv_bridge::Exception &e) {
      RCLCPP_ERROR(this->get_logger(), "cv_bridge RGB error: %s", e.what());
      return;
    }

    if (frame.empty()) {
      RCLCPP_ERROR(this->get_logger(), "Empty RGB frame.");
      return;
    }

    cv::Mat gray;
    cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY);

    // Multi-scale ZBar: original + 0.5x downscale
    frame_count_++;
    zbar::Image zbar_orig(gray.cols, gray.rows, "Y800", (uchar*)gray.data, gray.cols*gray.rows);
    int n = scanner_.scan(zbar_orig);
    cv::Mat half;
    zbar::Image* zbar_result = &zbar_orig;
    double half_scale = 1.0;

    if (n == 0) {
      cv::resize(gray, half, cv::Size(), 0.5, 0.5, cv::INTER_AREA);
      // zbar_result stays valid because half (cv::Mat) is in outer scope
      zbar_result = new zbar::Image(half.cols, half.rows, "Y800", (uchar*)half.data, half.cols*half.rows);
      n = scanner_.scan(*zbar_result);
      half_scale = 0.5;
    }

    if (n > 0) {
      if (last_qr_frame_ < 0 || (frame_count_ - last_qr_frame_) > 5) {
        RCLCPP_INFO(this->get_logger(),
          "[qr_decoder] QR DETECTED frame=%d symbols=%d (gap=%d frames)",
          frame_count_, n, last_qr_frame_ < 0 ? -1 : frame_count_ - last_qr_frame_ - 1);
      }
      last_qr_frame_ = frame_count_;
      for (zbar::Image::SymbolIterator symbol = zbar_result->symbol_begin();
           symbol != zbar_result->symbol_end(); ++symbol) {

        std::string qr_data = symbol->get_data();

        // Layer 1: Content validation — reject short/noise detections
        if (static_cast<int>(qr_data.length()) < min_qr_length_) {
          consecutive_rejects_++;
          RCLCPP_WARN(this->get_logger(),
            "[qr_decoder] REJECT(length): '%s' len=%zu < min=%d (rejects=%d)",
            qr_data.c_str(), qr_data.length(), min_qr_length_, consecutive_rejects_);
          continue;
        }

        // Layer 2: Depth check — advisory only (depth cam often lags RGB)
        int loc_size = symbol->get_location_size();
        int cx = 0, cy = 0;
        for (int i = 0; i < loc_size; i++) {
          cx += symbol->get_location_x(i);
          cy += symbol->get_location_y(i);
        }
        cx /= loc_size;
        cy /= loc_size;

        // Scale back coordinates for half-scale detections
        if (half_scale != 1.0) {
          cx = static_cast<int>(cx / half_scale);
          cy = static_cast<int>(cy / half_scale);
        }

        int depth_mm = 0;
        bool depth_valid = false;
        if (enable_depth_filter_ && !latest_depth_.empty()) {
          if (cx >= 0 && cx < latest_depth_.cols && cy >= 0 && cy < latest_depth_.rows) {
            depth_mm = latest_depth_.at<uint16_t>(cy, cx);
            depth_valid = (depth_mm >= static_cast<uint16_t>(depth_min_mm_) &&
                           depth_mm <= static_cast<uint16_t>(depth_max_mm_));
          }
        }

        // --- Passed content filter: publish (depth is advisory) ---
        consecutive_rejects_ = 0;
        if (depth_valid) {
          double Z = depth_mm / 1000.0;
          double X = (cx - cx_) * Z / fx_;
          double Y = (cy - cy_) * Z / fy_;
          RCLCPP_INFO(this->get_logger(),
            "[QR] %s | 3D:(%+.3f, %+.3f, %.3f)m | px(%d,%d) D:%dmm",
            qr_data.c_str(), X, Y, Z, cx, cy, depth_mm);
        } else if (enable_depth_filter_) {
          RCLCPP_INFO(this->get_logger(),
            "[QR] %s | depth=%dmm (advisory, publishing anyway)",
            qr_data.c_str(), depth_mm);
        } else {
          RCLCPP_INFO(this->get_logger(),
            "[QR] %s | depth filter off",
            qr_data.c_str());
        }

        auto sign_com_msg = std_msgs::msg::String();
        sign_com_msg.data = qr_data;
        sign_com_pub->publish(std::move(sign_com_msg));

        geometry_msgs::msg::PoseStamped pose_msg;
        pose_msg.header.stamp = this->now();
        pose_msg.header.frame_id = "odom";
        pose_msg.pose.position.x = odom_x_;
        pose_msg.pose.position.y = odom_y_;
        pose_msg.pose.orientation.z = std::sin(odom_yaw_ / 2.0);
        pose_msg.pose.orientation.w = std::cos(odom_yaw_ / 2.0);
        sign_pose_pub_->publish(pose_msg);

        RCLCPP_INFO(this->get_logger(),
          "[QR] %s | robot_pos: (%.2f, %.2f, yaw=%.2f)",
          qr_data.c_str(), odom_x_, odom_y_, odom_yaw_);
      }
      // Clean up half-scale image if created
      if (zbar_result != &zbar_orig) {
        delete zbar_result;
      }
    }

    // Periodic scanning status (every 200 frames)
    if (frame_count_ % 200 == 0) {
      int gap = last_qr_frame_ < 0 ? -1 : frame_count_ - last_qr_frame_;
      RCLCPP_INFO(this->get_logger(),
        "[qr_decoder] SCAN_STATUS frame=%d last_qr_frame=%d gap=%d frames rejects=%d",
        frame_count_, last_qr_frame_, gap, consecutive_rejects_);
    }
  }

  std::string rgb_topic_;
  std::string depth_topic_;
  bool enable_depth_filter_;
  int depth_min_mm_;
  int depth_max_mm_;
  int min_qr_length_;
  double fx_, fy_, cx_, cy_;
  cv::Mat latest_depth_;

  rclcpp::Subscription<sensor_msgs::msg::Image>::SharedPtr rgb_sub_;
  rclcpp::Subscription<sensor_msgs::msg::Image>::SharedPtr depth_sub_;
  rclcpp::Subscription<nav_msgs::msg::Odometry>::SharedPtr odom_sub_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr sign_com_pub;
  rclcpp::Publisher<geometry_msgs::msg::PoseStamped>::SharedPtr sign_pose_pub_;
  double odom_x_ = 0.0, odom_y_ = 0.0, odom_yaw_ = 0.0;
  zbar::ImageScanner scanner_;
  int frame_count_ = 0;
  int last_qr_frame_ = -1;
  int consecutive_rejects_ = 0;
};

int main(int argc, char *argv[])
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<QrCodeDetection>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
