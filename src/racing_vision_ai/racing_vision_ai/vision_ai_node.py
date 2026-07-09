#!/usr/bin/env python3
import base64
import os
import numpy as np

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import Int32, String
from sensor_msgs.msg import CompressedImage
import yaml

# 导入火山引擎SDK
try:
    from volcenginesdkarkruntime import Ark
except ImportError:
    print("Warning: volcengine-python-sdk[ark] not installed. Please install with: pip install volcengine-python-sdk[ark]")
    Ark = None


class VisionAINode(Node):
    """
    Racing Vision AI Node
    Subscribes to sign4return; when value==9, receives one JPEG frame
    (pre-encoded by hobot_codec JPU hardware) and sends to Volcengine Ark VLM.

    JPU integration: hobot_codec node encodes /aurora/rgb/image_raw → JPEG via
    hardware JPU. This node receives CompressedImage directly — no CPU encoding.
    """

    def __init__(self):
        super().__init__('vision_ai_node')

        # 声明参数，允许用户指定配置文件路径
        self.declare_parameter('config_path', '')

        # 加载配置文件
        self.config = self.load_config()

        # 初始化火山引擎客户端
        self.ark_client = None
        if Ark is not None:
            api_key = self.config.get('volcengine', {}).get('api_key')
            if api_key:
                self.ark_client = Ark(api_key=api_key)
                self.get_logger().info("Volcengine Ark client initialized")
            else:
                api_key = os.environ.get('ARK_API_KEY')
                if api_key:
                    self.ark_client = Ark(api_key=api_key)
                    self.get_logger().info("Volcengine Ark client using env var")
                else:
                    self.get_logger().error("ARK_API_KEY not set")
        else:
            self.get_logger().warn("Volcengine SDK not available")

        # 从配置文件获取模型ID
        self.model_id = self.config.get('volcengine', {}).get('model_id')
        if not self.model_id:
            self.model_id = os.environ.get('ARK_MODEL_ID', 'your-model-id')

        # 目标sign值
        self.target_sign = self.config.get('detection', {}).get('target_sign', 9)

        # 状态变量
        self.waiting_for_image = False

        # QoS配置
        qos_profile = QoSProfile(depth=10)

        # 订阅sign4return话题
        self.sign_subscriber = self.create_subscription(
            Int32,
            self.config.get('detection', {}).get('sign_topic', 'sign4return'),
            self.sign_callback,
            qos_profile
        )

        # 图像话题名称 (default: JPU-encoded JPEG from hobot_codec)
        self.image_topic = self.config.get('detection', {}).get(
            'image_topic', '/aurora/rgb/image_jpeg')

        # 订阅图像话题（仅在需要时订阅）
        self.image_sub = None

        # 发布 VLM 分析结果
        self.result_topic = self.config.get('detection', {}).get(
            'result_topic', 'vlm_result')
        self.result_pub = self.create_publisher(String, self.result_topic, 10)

        self.get_logger().info("Vision AI Node initialized (JPU JPEG mode)")
        self.get_logger().info(f"Waiting for sign4return={self.target_sign}")
        self.get_logger().info(f"Image topic: {self.image_topic}")

    def load_config(self):
        """加载配置文件"""
        try:
            from ament_index_python.packages import get_package_share_directory
            package_share_dir = get_package_share_directory('racing_vision_ai')
            installed_config_path = os.path.join(
                package_share_dir, 'config', 'vision_ai_config.yaml')
        except Exception:
            installed_config_path = None

        possible_paths = [
            os.path.join(os.getcwd(), 'vision_ai_config.yaml'),
            os.path.join(os.path.dirname(os.path.dirname(__file__)),
                        'config', 'vision_ai_config.yaml'),
        ]
        if installed_config_path:
            possible_paths.append(installed_config_path)

        param_config_path = self.get_parameter(
            'config_path').get_parameter_value().string_value
        if param_config_path:
            possible_paths.insert(0, param_config_path)

        for config_path in possible_paths:
            try:
                with open(config_path, 'r', encoding='utf-8') as file:
                    config = yaml.safe_load(file)
                    self.get_logger().info(f"Loaded config: {config_path}")
                    return config
            except Exception:
                continue

        self.get_logger().warn("No config file found, using defaults")
        return {}

    def sign_callback(self, msg):
        """处理sign4return信号"""
        self.get_logger().info(f"Received sign4return: {msg.data}")

        if msg.data == self.target_sign:
            self.get_logger().info(
                f"Trigger received (sign4return={self.target_sign}), "
                f"subscribing to {self.image_topic}...")
            self.waiting_for_image = True

            if self.image_sub is None:
                qos_profile = QoSProfile(depth=10)
                self.image_sub = self.create_subscription(
                    CompressedImage,
                    self.image_topic,
                    self.image_callback,
                    qos_profile
                )
                self.get_logger().info(f"Subscribed to {self.image_topic}")

    def image_callback(self, msg):
        """处理JPU预编码的JPEG帧 — 直接使用，无需CPU编码"""
        if not self.waiting_for_image:
            return

        self.get_logger().info(
            f"Received JPU-encoded JPEG frame "
            f"({len(msg.data)} bytes), sending to VLM...")

        try:
            # JPEG bytes 直接来自 hobot_codec JPU 硬件编码
            jpeg_bytes = np.frombuffer(msg.data, dtype=np.uint8)
            base64_image = base64.b64encode(jpeg_bytes.tobytes()).decode('utf-8')

            # 调用火山引擎 VLM API
            result = self._call_vlm(base64_image)

            if result:
                self.get_logger().info(f"VLM Result: {result}")
                self.result_pub.publish(String(data=result))
            else:
                self.get_logger().warn("VLM returned no result")

        except Exception as e:
            self.get_logger().error(f"Error processing VLM frame: {str(e)}")

        finally:
            self.waiting_for_image = False
            if self.image_sub is not None:
                self.destroy_subscription(self.image_sub)
                self.image_sub = None
                self.get_logger().info("Unsubscribed from image topic")

    def _call_vlm(self, base64_image):
        """Call Volcengine Ark VLM API with base64-encoded JPEG."""
        if self.ark_client is None:
            self.get_logger().warn("Ark client not available")
            return "AI client not available"

        try:
            prompt = self.config.get('volcengine', {}).get(
                'prompt', "请详细描述这张图片中的内容。")

            response = self.ark_client.chat.completions.create(
                model=self.model_id,
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "image_url",
                         "image_url": {
                             "url": f"data:image/jpeg;base64,{base64_image}"
                         }},
                        {"type": "text", "text": prompt},
                    ],
                }],
                timeout=10.0,
            )

            if response.choices and len(response.choices) > 0:
                return response.choices[0].message.content
            return None

        except Exception as e:
            self.get_logger().error(f"VLM API error: {str(e)}")
            return None


def main(args=None):
    rclpy.init(args=args)
    node = VisionAINode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
