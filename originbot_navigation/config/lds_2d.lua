-- Copyright 2016 The Cartographer Authors
--
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
--
--      http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.

-- /* N10 激光雷达 Cartographer 2D SLAM 配置文件 */
--
-- N10 雷达规格: 2000点/圈, 0.18°角分辨率, 5Hz扫描频率, 360°全方位
-- 适用场景: 21届智能汽车竞赛地瓜机器人赛项 5m×5m 场地建图

include "map_builder.lua"
include "trajectory_builder.lua"

options = {
  map_builder = MAP_BUILDER,                    -- map_builder.lua的配置信息
  trajectory_builder = TRAJECTORY_BUILDER,      -- trajectory_builder.lua的配置信息
  map_frame = "map",                            -- 地图坐标系的名称
  tracking_frame = "base_footprint",            -- 跟踪坐标系，一般是机器人基坐标系的名称
  published_frame = "odom",                     -- 发布定位信息所使用的里程计坐标系名称，算法将发布map和published_frame之间的tf
  odom_frame = "odom",                          -- 机器人现有里程计坐标系的名称
  provide_odom_frame = false,                   -- 是否需要算法发布里程计信息
  publish_frame_projected_to_2d = true,         -- 2D SLAM: 投影到二维, 消除Z/roll/pitch噪声
  use_odometry = true,                          -- 是否使用机器人里程计，如果是，机器人必须要发布odom的tf
  use_nav_sat = false,                          -- 是否使用GPS
  use_landmarks = false,                        -- 是否使用路标
  num_laser_scans = 1,                          -- 订阅激光雷达LaserScan话题的数量
  num_multi_echo_laser_scans = 0,               -- 订阅多回波技术激光雷达话题的数量
  num_subdivisions_per_laser_scan = 1,          -- 将一帧激光雷达数据分割为几次处理
  num_point_clouds = 0,                         -- 是否使用点云数据
  lookup_transform_timeout_sec = 0.5,           -- 查找tf坐标变换数据的超时时间
  submap_publish_period_sec = 0.3,              -- 发布submap子图的周期，单位秒
  pose_publish_period_sec = 5e-3,               -- 发布姿态的周期，单位秒
  trajectory_publish_period_sec = 30e-3,        -- 发布轨迹的周期，单位秒
  rangefinder_sampling_ratio = 1.,              -- 测距仪采样率(N10: 2000点/圈, 1.0=全采样)
  odometry_sampling_ratio = 1.,                 -- 里程计数据采样率
  fixed_frame_pose_sampling_ratio = 1.,         -- 固定坐标系位姿采样率
  imu_sampling_ratio = 1.,                      -- IMU数据采样率(N10内置IMU或被外部IMU替代)
  landmarks_sampling_ratio = 1.,                -- 路标数据采样率
}

MAP_BUILDER.use_trajectory_builder_2d = true          -- 是否使用2D建图                

TRAJECTORY_BUILDER_2D.min_range = 0.3                 -- 最小测距(m)，N10驱动默认0.3m，过滤传感器机身噪声
TRAJECTORY_BUILDER_2D.max_range = 8.0                 -- 最大测距(m)，5m×5m竞赛场地内8m足够覆盖
TRAJECTORY_BUILDER_2D.missing_data_ray_length = 3.0   -- 射线清理距离(m)，消除动态障碍物残影。5m×5m场地设为3.0确保充分清理
TRAJECTORY_BUILDER_2D.use_imu_data = false            -- Route B架构: IMU由EKF融合进odometry，Cartographer不独立处理IMU，消除双重计算
TRAJECTORY_BUILDER_2D.use_online_correlative_scan_matching = true      -- 启用在线CSM扫描匹配，在里程计推算位姿附近搜索最佳匹配，修复漂移导致的叠图
TRAJECTORY_BUILDER_2D.ceres_scan_matcher.translation_weight = 12.0     -- 平移匹配权重(默认10)。Route B下EKF提供平滑里程计，略提升以增强激光匹配修正能力
TRAJECTORY_BUILDER_2D.ceres_scan_matcher.rotation_weight = 45.0        -- 旋转匹配权重(默认40)。同上，略提升以对抗N10 5Hz低频可能带来的角度累积误差
TRAJECTORY_BUILDER_2D.voxel_filter_size = 0.025                         -- 体素滤波尺寸(m)，降采样以去除噪点。N10稠密点云(2000点)保持默认2.5cm平衡细节与性能
TRAJECTORY_BUILDER_2D.motion_filter.max_angle_radians = 0.052                -- 运动滤波角度阈值(0.052rad≈3°)，N10分辨率0.18°可支持更精细过滤
TRAJECTORY_BUILDER_2D.motion_filter.max_distance_meters = 0.05          -- 运动滤波距离阈值(5cm)，N10有2000点/圈可处理更密帧

POSE_GRAPH.constraint_builder.min_score = 0.60                         -- 全局约束当前最小得分(当前node与当前submap的匹配得分)
POSE_GRAPH.constraint_builder.global_localization_min_score = 0.60     -- 全局约束全局最小得分(当前node与全局submap的匹配得分)

POSE_GRAPH.optimize_every_n_nodes = 15                                -- 全局优化间隔(5m×5m小场地，更频繁优化及时纠正累积漂移)

return options
