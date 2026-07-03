root@ubuntu:/userdata/dev_ws# ros2 launch origincar_bringup stage3_bringup.launch.py
[INFO] [launch]: All log files can be found below /root/.ros/log/2026-07-03-13-42-10-871938-ubuntu-22505
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [origincar_base_node-1]: process started with pid [22519]
[INFO] [lslidar_driver_node-2]: process started with pid [22521]
[INFO] [robot_state_publisher-3]: process started with pid [22523]
[INFO] [imu_madgwick_filter.py-4]: process started with pid [22525]
[INFO] [bmi088_iio_bridge.py-5]: process started with pid [22527]
[INFO] [imu_madgwick_filter.py-6]: process started with pid [22529]
[INFO] [ekf_node-7]: process started with pid [22531]
[INFO] [static_transform_publisher-8]: process started with pid [22571]
[INFO] [aurora930_node-9]: process started with pid [22573]
[INFO] [qr_decoder-10]: process started with pid [22575]
[INFO] [qr_decision-11]: process started with pid [22577]
[INFO] [vision_ai_node-12]: process started with pid [22579]
[INFO] [hobot_codec_republish-13]: process started with pid [22581]
[origincar_base_node-1] [INFO] [1783057331.579236484] [origincar_base]: origincar_base serial port opened
[lslidar_driver_node-2] [INFO] [1783057331.585689318] [lslidar_driver_node]: Lidar is N10
[lslidar_driver_node-2] [INFO] [1783057331.603160404] [lslidar_driver_node]: Initialised lslidar without error
[lslidar_driver_node-2] [INFO] [1783057331.603342321] [lslidar_driver_node]: Successfully initialize driver...
[robot_state_publisher-3] [INFO] [1783057331.599228403] [robot_state_publisher]: got segment base_footprint
[robot_state_publisher-3] [INFO] [1783057331.599605029] [robot_state_publisher]: got segment base_link
[robot_state_publisher-3] [INFO] [1783057331.599697945] [robot_state_publisher]: got segment gyro_link
[robot_state_publisher-3] [INFO] [1783057331.599747737] [robot_state_publisher]: got segment laser_link
[ekf_node-7] Both imu1_differential and imu1_relative were set to true. Using differential mode.
[hobot_codec_republish-13] [WARN] [1783057331.863969109] [vlm_jpeg_encoder]: Parameters:
[hobot_codec_republish-13]              sub_topic: /aurora/rgb/image_raw
[hobot_codec_republish-13]              pub_topic: /aurora/rgb/image_jpeg
[hobot_codec_republish-13]                channel: 0
[hobot_codec_republish-13]                in_mode: ros
[hobot_codec_republish-13]               out_mode: ros
[hobot_codec_republish-13]              in_format: bgr8
[hobot_codec_republish-13]             out_format: jpeg
[hobot_codec_republish-13]            jpg_quality: 85.00
[hobot_codec_republish-13]        input_framerate: 30
[hobot_codec_republish-13]       output_framerate: -1
[hobot_codec_republish-13]            dump_output: false
[hobot_codec_republish-13]       dump_file_prefix: ./dump_codec_output
[hobot_codec_republish-13]       dump_frame_count: -1 (unlimited)
[static_transform_publisher-8] [INFO] [1783057331.878385986] [depth_camera_tf]: Spinning until stopped - publishing transform
[static_transform_publisher-8] translation: ('0.140000', '0.000000', '0.050000')
[static_transform_publisher-8] rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
[static_transform_publisher-8] from 'base_link' to 'depth_camera_link'
[hobot_codec_republish-13] [WARN] [1783057331.902245823] [HobotCodecImpl]: platform x5
[qr_decoder-10] [INFO] [1783057332.350793556] [qr_decoder_zbar]: QR decoder (ZBar) started: rgb=/aurora/rgb/image_raw, depth=/aurora/depth/image_raw, filter=on, range=[50, 4000]mm, min_qr_len=1, intrinsics: fx=421.3 fy=422.3 cx=320.3 cy=197.0
[aurora930_node-9] W0703 13:42:12.407672 22573 ros2_node.cc:35] hello aurora 900/930
[aurora930_node-9] 2026-07-03 13:42:12.485 (   0.209s) [        90794020] device_manager_impl.cc:89    INFO| hotplug has registed by user
[aurora930_node-9] device_count==========1
[aurora930_node-9] I0703 13:42:12.516427 22573 aurora900_ros2_device.cc:153] BOOT_ORDER_1::Found 1 deptrum device
[aurora930_node-9] I0703 13:42:12.516943 22573 aurora900_ros2_device.cc:162] BOOT_ORDER_1::No serial number provided: picking first device
[aurora930_node-9] 2026-07-03 13:42:12.517 (   0.241s) [        90794020] device_manager_impl.cc:318   INFO| Device information:
[aurora930_node-9]      ir_pid:0x1930, rgb_pid:0x0
[aurora930_node-9]      serial number:HY400529001015314G00248
[aurora930_node-9] I0703 13:42:12.517127 22573 aurora900_ros2_device.cc:206] BOOT_ORDER_1::0:device start opening
[aurora930_node-9] 2026-07-03 13:42:12.519 (   0.243s) [        90794020]   custom_usb_device.cc:101   INFO| bulk in endpoint addr:129
[aurora930_node-9] 2026-07-03 13:42:12.519 (   0.243s) [        90794020]   custom_usb_device.cc:98    INFO| bulk out endpoint addr:2
[aurora930_node-9] 2026-07-03 13:42:12.533 (   0.258s) [        90794020]deptrum_camera_aurora93:53    INFO| doe_broken:0 ito_support:1 crash_count:0 wdt_count:0 hard_reset_count:2 heart_boot_count:0 boot_total:127 last_crash_time:N
[aurora930_node-9] I0703 13:42:12.534076 22573 aurora900_ros2_device.cc:247] device supported frame_mode:
[aurora930_node-9] I0703 13:42:12.534175 22573 aurora900_ros2_device.cc:252] [0]:ir_mode:=13 kRes320x200Ir8Bit rgb_mode:=31 kRes320x200RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0703 13:42:12.534219 22573 aurora900_ros2_device.cc:252] [1]:ir_mode:=17 kRes480x300Depth16Bit rgb_mode:=32 kRes480x300RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0703 13:42:12.534252 22573 aurora900_ros2_device.cc:252] [2]:ir_mode:=20 kRes640x400Ir8Bit rgb_mode:=33 kRes640x400RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0703 13:42:12.534284 22573 aurora900_ros2_device.cc:266] current set mode ir_mode:20:kRes640x400Ir8Bit,rgb_mode:33:kRes640x400RgbYuv
[INFO] [map_server-14]: process started with pid [22678]
[INFO] [costmap_filter_info_server-15]: process started with pid [22680]
[INFO] [lifecycle_manager-16]: process started with pid [22687]
[costmap_filter_info_server-15] [INFO] [1783057332.894134887] [costmap_filter_info_server]: This is costmap filter info publisher
[lifecycle_manager-16] [INFO] [1783057332.909267181] [lifecycle_manager_keepout]: Creating
[lifecycle_manager-16] [INFO] [1783057332.965198064] [lifecycle_manager_keepout]: Creating and initializing lifecycle service clients
[map_server-14] [INFO] [1783057332.980556483] [keepout_mask_server]:
[map_server-14]         keepout_mask_server lifecycle node launched.
[map_server-14]         Waiting on external lifecycle transitions to activate
[map_server-14]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[map_server-14] [INFO] [1783057332.981241316] [keepout_mask_server]: Creating
[costmap_filter_info_server-15] [INFO] [1783057333.056713202] [keepout_filter_info_server]:
[costmap_filter_info_server-15]         keepout_filter_info_server lifecycle node launched.
[costmap_filter_info_server-15]         Waiting on external lifecycle transitions to activate
[costmap_filter_info_server-15]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[aurora930_node-9] I0703 13:42:13.072992 22573 aurora900_ros2_device.cc:387] Switch Auto Exposure
[aurora930_node-9] 2026-07-03 13:42:13.132 (   0.856s) [        90794020]      aurora900_impl.cc:1106  INFO| SetHeartbeat user set heartbeat enable: 0
[lifecycle_manager-16] [INFO] [1783057333.169135469] [lifecycle_manager_keepout]: Starting managed nodes bringup...
[lifecycle_manager-16] [INFO] [1783057333.191482139] [lifecycle_manager_keepout]: Configuring keepout_mask_server
[map_server-14] [INFO] [1783057333.195783348] [keepout_mask_server]: Configuring
[map_server-14] [INFO] [1783057333.196067431] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.yaml
[map_server-14] [INFO] [1783057333.197146640] [map_io]: resolution: 0.05
[map_server-14] [INFO] [1783057333.197213057] [map_io]: origin[0]: -2.65
[map_server-14] [INFO] [1783057333.197243682] [map_io]: origin[1]: -4.5
[map_server-14] [INFO] [1783057333.197270890] [map_io]: origin[2]: 0
[map_server-14] [INFO] [1783057333.197298515] [map_io]: free_thresh: 0.5
[map_server-14] [INFO] [1783057333.197326515] [map_io]: occupied_thresh: 0.5
[map_server-14] [INFO] [1783057333.197359473] [map_io]: mode: scale
[map_server-14] [INFO] [1783057333.197388265] [map_io]: negate: 0
[map_server-14] [INFO] [1783057333.198032932] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm
[map_server-14] [INFO] [1783057333.225274686] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm: 163 X 141 map @ 0.05 m/cell
[lifecycle_manager-16] [INFO] [1783057333.259397316] [lifecycle_manager_keepout]: Configuring keepout_filter_info_server
[costmap_filter_info_server-15] [INFO] [1783057333.260438274] [keepout_filter_info_server]: Configuring
[lifecycle_manager-16] [INFO] [1783057333.284464236] [lifecycle_manager_keepout]: Activating keepout_mask_server
[map_server-14] [INFO] [1783057333.285371653] [keepout_mask_server]: Activating
[map_server-14] [INFO] [1783057333.285767070] [keepout_mask_server]: Creating bond (keepout_mask_server) to lifecycle manager.
[bmi088_iio_bridge.py-5] [INFO] [1783057333.298518613] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1783057333.303625781] [bmi088_iio_bridge]:   DIAGNOSTIC: Scanning IIO devices under /sys/bus/iio/devices/
[bmi088_iio_bridge.py-5] [INFO] [1783057333.307493115] [bmi088_iio_bridge]:   Equivalent to: ls /sys/bus/iio/devices/*/name
[bmi088_iio_bridge.py-5] [INFO] [1783057333.310502782] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1783057333.313610532] [bmi088_iio_bridge]:   iio:device0/name = "34190000.adc"
[bmi088_iio_bridge.py-5] [INFO] [1783057333.316836949] [bmi088_iio_bridge]:   iio:device1/name = "bmi08x"
[bmi088_iio_bridge.py-5] [INFO] [1783057333.319600117] [bmi088_iio_bridge]:   trigger0/name = "34190000.adc-dev0"
[bmi088_iio_bridge.py-5] [INFO] [1783057333.322958617] [bmi088_iio_bridge]:   Total IIO devices found: 3
[bmi088_iio_bridge.py-5] [INFO] [1783057333.325865201] [bmi088_iio_bridge]:   BMI088 kernel module APPEARS LOADED: 1 BMI device(s) detected
[bmi088_iio_bridge.py-5] [INFO] [1783057333.329260368] [bmi088_iio_bridge]:   BMI device names: ['bmi08x']
[bmi088_iio_bridge.py-5] [INFO] [1783057333.333016619] [bmi088_iio_bridge]:   gyro:  /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_anglvel is_si=False scale_override=0.00053
[bmi088_iio_bridge.py-5] [INFO] [1783057333.337074286] [bmi088_iio_bridge]:   accel: /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_accel is_si=False scale_override=0.00341
[lifecycle_manager-16] [INFO] [1783057333.398232295] [lifecycle_manager_keepout]: Server keepout_mask_server connected with bond.
[lifecycle_manager-16] [INFO] [1783057333.398483670] [lifecycle_manager_keepout]: Activating keepout_filter_info_server
[costmap_filter_info_server-15] [INFO] [1783057333.400368504] [keepout_filter_info_server]: Activating
[costmap_filter_info_server-15] [INFO] [1783057333.400623045] [keepout_filter_info_server]: Creating bond (keepout_filter_info_server) to lifecycle manager.
[bmi088_iio_bridge.py-5] [INFO] [1783057333.463994013] [bmi088_iio_bridge]: BMI088 IIO Bridge 启动 @ 100Hz -> /imu_data  [OK]
[lifecycle_manager-16] [INFO] [1783057333.518752271] [lifecycle_manager_keepout]: Server keepout_filter_info_server connected with bond.
[lifecycle_manager-16] [INFO] [1783057333.518923146] [lifecycle_manager_keepout]: Managed nodes are active
[lifecycle_manager-16] [INFO] [1783057333.518992604] [lifecycle_manager_keepout]: Creating bond timer...
[aurora930_node-9] I0703 13:42:13.542342 22573 aurora900_ros2_device.cc:304] BOOT_ORDER_1::Device information:
[aurora930_node-9] I0703 13:42:13.542492 22573 aurora900_ros2_device.cc:305]     sdk version: 1.1.22
[aurora930_node-9] I0703 13:42:13.542531 22573 aurora900_ros2_device.cc:306]     device name: Aurora 930
[aurora930_node-9] I0703 13:42:13.542559 22573 aurora900_ros2_device.cc:307]     serial number: HY400529001015314G00248
[aurora930_node-9] I0703 13:42:13.542585 22573 aurora900_ros2_device.cc:308]     firmware version: 1.7.2
[aurora930_node-9] I0703 13:42:13.542635 22573 camera_parameters.cc:134] BOOT_ORDER_1::Camera Parameters:
[aurora930_node-9] I0703 13:42:13.542665 22573 camera_parameters.cc:135] BOOT_ORDER_1::  Ir Intrinsics:
[aurora930_node-9] I0703 13:42:13.542691 22573 camera_parameters.cc:146]                 Resolution:
[aurora930_node-9] I0703 13:42:13.542716 22573 camera_parameters.cc:147]                         Rows:400
[aurora930_node-9] I0703 13:42:13.542742 22573 camera_parameters.cc:148]                         Cols:640
[aurora930_node-9] I0703 13:42:13.542766 22573 camera_parameters.cc:149]                 Intrinsics:
[aurora930_node-9] I0703 13:42:13.542791 22573 camera_parameters.cc:150]                         fx: 421.307
[aurora930_node-9] I0703 13:42:13.542887 22573 camera_parameters.cc:151]                         fy: 422.254
[aurora930_node-9] I0703 13:42:13.542920 22573 camera_parameters.cc:152]                         cx: 320.27
[aurora930_node-9] I0703 13:42:13.542953 22573 camera_parameters.cc:153]                         cy: 197.01
[aurora930_node-9] I0703 13:42:13.542985 22573 camera_parameters.cc:154]                         k1: 0.0606853
[aurora930_node-9] I0703 13:42:13.543016 22573 camera_parameters.cc:155]                         k2: -0.10961
[aurora930_node-9] I0703 13:42:13.543047 22573 camera_parameters.cc:156]                         p1: 0.00126689
[aurora930_node-9] I0703 13:42:13.543079 22573 camera_parameters.cc:157]                         p2: -0.00120539
[aurora930_node-9] I0703 13:42:13.543110 22573 camera_parameters.cc:158]                         k3: 0.0522281
[aurora930_node-9] I0703 13:42:13.543156 22573 camera_parameters.cc:138] BOOT_ORDER_1::  Rgb Intrinsics:
[aurora930_node-9] I0703 13:42:13.543183 22573 camera_parameters.cc:146]                 Resolution:
[aurora930_node-9] I0703 13:42:13.543208 22573 camera_parameters.cc:147]                         Rows:400
[aurora930_node-9] I0703 13:42:13.543233 22573 camera_parameters.cc:148]                         Cols:640
[aurora930_node-9] I0703 13:42:13.543258 22573 camera_parameters.cc:149]                 Intrinsics:
[aurora930_node-9] I0703 13:42:13.543283 22573 camera_parameters.cc:150]                         fx: 416.49
[aurora930_node-9] I0703 13:42:13.543314 22573 camera_parameters.cc:151]                         fy: 417.383
[aurora930_node-9] I0703 13:42:13.543345 22573 camera_parameters.cc:152]                         cx: 316.832
[aurora930_node-9] I0703 13:42:13.543377 22573 camera_parameters.cc:153]                         cy: 188.753
[aurora930_node-9] I0703 13:42:13.543408 22573 camera_parameters.cc:154]                         k1: 0.00611878
[aurora930_node-9] I0703 13:42:13.543439 22573 camera_parameters.cc:155]                         k2: -0.0490436
[aurora930_node-9] I0703 13:42:13.543470 22573 camera_parameters.cc:156]                         p1: 0.000399548
[aurora930_node-9] I0703 13:42:13.543501 22573 camera_parameters.cc:157]                         p2: 0.000563892
[aurora930_node-9] I0703 13:42:13.543532 22573 camera_parameters.cc:158]                         k3: 0.0308458
[aurora930_node-9] I0703 13:42:13.543563 22573 camera_parameters.cc:141] BOOT_ORDER_1::  Ir to Rgb Extrinsic:
[aurora930_node-9] I0703 13:42:13.543589 22573 camera_parameters.cc:162]                 Extrinsics:
[aurora930_node-9] I0703 13:42:13.543614 22573 camera_parameters.cc:163]                         Rotation[0]: 0.999973, 0.00724076, -0.00112023
[aurora930_node-9] I0703 13:42:13.543651 22573 camera_parameters.cc:165]                         Rotation[1]: -0.00724006, 0.999973, 0.000633162
[aurora930_node-9] I0703 13:42:13.543687 22573 camera_parameters.cc:167]                         Rotation[2]: 0.00112478, -0.000625033, 0.999999
[aurora930_node-9] I0703 13:42:13.543767 22573 camera_parameters.cc:169]                         Translation: -9.88662, 0.117748, 0.603513
[aurora930_node-9] 2026-07-03 13:42:13.544 (   1.268s) [        90794020]      aurora900_impl.cc:578   INFO| stream_mask_:0, rgb_stream_count_:1
[imu_madgwick_filter.py-6] [INFO] [1783057333.565425695] [imu_madgwick_bmi088]: [imu_madgwick] init: beta=0.0030, gyro_noise=0.0002, accel_noise=0.010
[imu_madgwick_filter.py-4] [INFO] [1783057333.566055195] [imu_madgwick_filter]: [imu_madgwick] init: beta=0.0330, gyro_noise=0.0010, accel_noise=0.050
[imu_madgwick_filter.py-4] [INFO] [1783057333.571588071] [imu_madgwick_filter]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-6] [INFO] [1783057333.572570029] [imu_madgwick_bmi088]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-4] [INFO] [1783057333.574262321] [imu_madgwick_filter]: [imu_madgwick] accel init: roll=-0.7deg, pitch=-0.6deg
[imu_madgwick_filter.py-6] [INFO] [1783057333.575887863] [imu_madgwick_bmi088]: [imu_madgwick] accel init: roll=-2.1deg, pitch=-3.6deg
[qr_decision-11] [INFO] [1783057333.723144343] [qr_decision]: qr_decision started: cooldown=3.0s, awaiting /sign from qr_decoder
[hobot_codec_republish-13] [WARN] [1783057333.837907277] [HobotVenc]: init_pic_w_: 640, init_pic_h_: 400, alined_pic_w_: 640, alined_pic_h_: 400, aline_w_: 16, aline_h_: 16
[hobot_codec_republish-13] [WARN] [1783057336.963681870] [vlm_jpeg_encoder]: Sub imgRaw fps [8.71]
[hobot_codec_republish-13] [WARN] [1783057336.965870495] [vlm_jpeg_encoder]: Pub img fps [8.70]
[aurora930_node-9] 2026-07-03 13:42:13.866 (   1.590s) [        611D37E0]deptrum_camera_aurora93:407    ERR| recv first frame time is 1783057333866
[lslidar_driver_node-2] port = /dev/ttyACM1, baud_rate = 230400
[lslidar_driver_node-2] open_port /dev/ttyACM1 OK !
[INFO] [component_container_isolated-17]: process started with pid [22846]
[vision_ai_node-12] [INFO] [1783057336.937866158] [vision_ai_node]: Loaded config: /userdata/dev_ws/install/racing_vision_ai/share/racing_vision_ai/config/vision_ai_config.yaml
[vision_ai_node-12] [INFO] [1783057337.314035006] [vision_ai_node]: Volcengine Ark client initialized
[vision_ai_node-12] [INFO] [1783057337.328818842] [vision_ai_node]: Vision AI Node initialized (JPU JPEG mode)
[vision_ai_node-12] [INFO] [1783057337.331290550] [vision_ai_node]: Waiting for sign4return=9
[vision_ai_node-12] [INFO] [1783057337.333706842] [vision_ai_node]: Image topic: /aurora/rgb/image_jpeg
[bmi088_iio_bridge.py-5] [INFO] [1783057338.891853370] [bmi088_iio_bridge]:   gyro bias calibrated: (0.002589, 0.001577, -0.002785) rad/s
[INFO] [competition_master_stage3.py-21]: process started with pid [22863]
[INFO] [depth_detector-18]: process started with pid [22850]
[INFO] [tracker_node-19]: process started with pid [22852]
[INFO] [costmap_publisher-20]: process started with pid [22856]
[INFO] [path_optimizer_node.py-22]: process started with pid [22868]
[INFO] [speed_profile_node.py-23]: process started with pid [22873]
[INFO] [rviz2-24]: process started with pid [22875]
[component_container_isolated-17] [INFO] [1783057340.002688913] [nav2_container]: Load Library: /opt/ros/humble/lib/libmap_server_core.so
[component_container_isolated-17] [INFO] [1783057340.092800594] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::CostmapFilterInfoServer>
[component_container_isolated-17] [INFO] [1783057340.092994677] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapSaver>
[component_container_isolated-17] [INFO] [1783057340.093079177] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-17] [INFO] [1783057340.093143969] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-17] [INFO] [1783057340.357707718] [map_server]:
[component_container_isolated-17]       map_server lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783057340.358709093] [map_server]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/map_server' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783057340.373387012] [nav2_container]: Load Library: /opt/ros/humble/lib/libcontroller_server_core.so
[component_container_isolated-17] [INFO] [1783057340.421334894] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-17] [INFO] [1783057340.421589102] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-17] [INFO] [1783057340.612654298] [controller_server]:
[component_container_isolated-17]       controller_server lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783057340.647801345] [controller_server]: Creating controller server
[component_container_isolated-17] [INFO] [1783057340.823534872] [local_costmap.local_costmap]:
[component_container_isolated-17]       local_costmap lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783057340.826619164] [local_costmap.local_costmap]: Creating Costmap
[component_container_isolated-17] [INFO] [1783057340.872228713] [nav2_container]: Load Library: /opt/ros/humble/lib/libamcl_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/controller_server' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783057340.900362050] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-17] [INFO] [1783057340.900558592] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-17] [INFO] [1783057341.047698073] [amcl]:
[component_container_isolated-17]       amcl lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783057341.050511657] [amcl]: Creating
[component_container_isolated-17] [INFO] [1783057341.236543810] [nav2_container]: Load Library: /opt/ros/humble/lib/libsmoother_server_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/amcl' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783057341.242817978] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-17] [INFO] [1783057341.242994145] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-17] [INFO] [1783057341.369877539] [smoother_server]:
[component_container_isolated-17]       smoother_server lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783057341.380920582] [smoother_server]: Creating smoother server
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/smoother_server' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783057341.395750001] [nav2_container]: Load Library: /opt/ros/humble/lib/libnav2_lifecycle_manager_core.so
[component_container_isolated-17] [INFO] [1783057341.399126835] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-17] [INFO] [1783057341.399305002] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-17] [INFO] [1783057341.500481934] [lifecycle_manager_localization]: Creating
[component_container_isolated-17] [INFO] [1783057341.542717190] [nav2_container]: Load Library: /opt/ros/humble/lib/libplanner_server_core.so
[component_container_isolated-17] [INFO] [1783057341.546170316] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-17] [INFO] [1783057341.546323983] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_localization' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783057341.571677362] [lifecycle_manager_localization]: Creating and initializing lifecycle service clients
[component_container_isolated-17] [INFO] [1783057341.652750499] [lifecycle_manager_localization]: Starting managed nodes bringup...
[component_container_isolated-17] [INFO] [1783057341.653588666] [lifecycle_manager_localization]: Configuring map_server
[component_container_isolated-17] [INFO] [1783057341.655875083] [map_server]: Configuring
[component_container_isolated-17] [INFO] [1783057341.656191458] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.yaml
[component_container_isolated-17] [INFO] [1783057341.657334708] [map_io]: resolution: 0.05
[component_container_isolated-17] [INFO] [1783057341.657432291] [map_io]: origin[0]: -2.65
[component_container_isolated-17] [INFO] [1783057341.657466708] [map_io]: origin[1]: -4.5
[component_container_isolated-17] [INFO] [1783057341.657494208] [map_io]: origin[2]: 0
[component_container_isolated-17] [INFO] [1783057341.657522375] [map_io]: free_thresh: 0.25
[component_container_isolated-17] [INFO] [1783057341.657550958] [map_io]: occupied_thresh: 0.65
[component_container_isolated-17] [INFO] [1783057341.657597375] [map_io]: mode: trinary
[component_container_isolated-17] [INFO] [1783057341.657629166] [map_io]: negate: 0
[component_container_isolated-17] [INFO] [1783057341.658305500] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm
[component_container_isolated-17] [INFO] [1783057341.706891466] [planner_server]:
[component_container_isolated-17]       planner_server lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783057341.709917008] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm: 163 X 141 map @ 0.05 m/cell
[component_container_isolated-17] [INFO] [1783057341.732926720] [planner_server]: Creating
[component_container_isolated-17] [INFO] [1783057341.766588766] [lifecycle_manager_localization]: Configuring amcl
[component_container_isolated-17] [INFO] [1783057341.767437558] [amcl]: Configuring
[component_container_isolated-17] [INFO] [1783057341.768985392] [amcl]: initTransforms
[component_container_isolated-17] [INFO] [1783057341.873578574] [amcl]: initPubSub
[component_container_isolated-17] [INFO] [1783057341.935869834] [amcl]: Subscribed to map topic.
[component_container_isolated-17] [INFO] [1783057341.947168752] [global_costmap.global_costmap]:
[component_container_isolated-17]       global_costmap lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783057341.957541171] [global_costmap.global_costmap]: Creating Costmap
[component_container_isolated-17] [INFO] [1783057341.987562759] [lifecycle_manager_localization]: Activating map_server
[component_container_isolated-17] [INFO] [1783057341.988674175] [map_server]: Activating
[component_container_isolated-17] [INFO] [1783057341.989161801] [map_server]: Creating bond (map_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057342.015155638] [amcl]: Received a 163 X 141 map @ 0.050 m/pix
[hobot_codec_republish-13] [WARN] [1783057342.039350725] [vlm_jpeg_encoder]: Sub imgRaw fps [12.41]
[hobot_codec_republish-13] [WARN] [1783057342.042005850] [vlm_jpeg_encoder]: Pub img fps [12.41]
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/planner_server' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783057342.066837187] [nav2_container]: Load Library: /opt/ros/humble/lib/libbehavior_server_core.so
[component_container_isolated-17] [INFO] [1783057342.085313857] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-17] [INFO] [1783057342.085519774] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-17] [INFO] [1783057342.106137402] [lifecycle_manager_localization]: Server map_server connected with bond.
[component_container_isolated-17] [INFO] [1783057342.106303485] [lifecycle_manager_localization]: Activating amcl
[component_container_isolated-17] [INFO] [1783057342.107164902] [amcl]: Activating
[component_container_isolated-17] [INFO] [1783057342.107414527] [amcl]: initialPoseReceived
[component_container_isolated-17] [INFO] [1783057342.107897860] [amcl]: Setting pose (1783057342.107893): -1.985 -0.014 0.262
[component_container_isolated-17] [INFO] [1783057342.109748236] [amcl]: Creating bond (amcl) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057342.139734032] [amcl]: createLaserObject
[component_container_isolated-17] [INFO] [1783057342.232843588] [lifecycle_manager_localization]: Server amcl connected with bond.
[component_container_isolated-17] [INFO] [1783057342.233032171] [lifecycle_manager_localization]: Managed nodes are active
[component_container_isolated-17] [INFO] [1783057342.233153546] [lifecycle_manager_localization]: Creating bond timer...
[component_container_isolated-17] [INFO] [1783057342.241040964] [behavior_server]:
[component_container_isolated-17]       behavior_server lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/behavior_server' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783057342.287373221] [nav2_container]: Load Library: /opt/ros/humble/lib/libbt_navigator_core.so
[component_container_isolated-17] [INFO] [1783057342.297485098] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-17] [INFO] [1783057342.297810890] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-17] [INFO] [1783057342.442985745] [bt_navigator]:
[component_container_isolated-17]       bt_navigator lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783057342.443516870] [bt_navigator]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/bt_navigator' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783057342.464261665] [nav2_container]: Load Library: /opt/ros/humble/lib/libwaypoint_follower_core.so
[component_container_isolated-17] [INFO] [1783057342.467459499] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-17] [INFO] [1783057342.467637124] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-17] [INFO] [1783057342.557161888] [waypoint_follower]:
[component_container_isolated-17]       waypoint_follower lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783057342.573297724] [waypoint_follower]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/waypoint_follower' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783057342.617428230] [nav2_container]: Load Library: /opt/ros/humble/lib/libvelocity_smoother_core.so
[component_container_isolated-17] [INFO] [1783057342.626883565] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-17] [INFO] [1783057342.631256066] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-17] [INFO] [1783057342.746842167] [velocity_smoother]:
[component_container_isolated-17]       velocity_smoother lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/velocity_smoother' in container '/nav2_container'
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783057342.767734670] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-17] [INFO] [1783057342.767902087] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-17] [INFO] [1783057342.917933693] [lifecycle_manager_navigation]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_navigation' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783057342.994361580] [lifecycle_manager_navigation]: Creating and initializing lifecycle service clients
[component_container_isolated-17] [INFO] [1783057343.245070744] [lifecycle_manager_navigation]: Starting managed nodes bringup...
[component_container_isolated-17] [INFO] [1783057343.245313285] [lifecycle_manager_navigation]: Configuring controller_server
[component_container_isolated-17] [INFO] [1783057343.247816827] [controller_server]: Configuring controller interface
[component_container_isolated-17] [INFO] [1783057343.248807703] [controller_server]: getting goal checker plugins..
[component_container_isolated-17] [INFO] [1783057343.250498620] [controller_server]: Controller frequency set to 10.0000Hz
[component_container_isolated-17] [INFO] [1783057343.250826370] [local_costmap.local_costmap]: Configuring
[component_container_isolated-17] [INFO] [1783057343.309403212] [local_costmap.local_costmap]: Using plugin "obstacle_layer"
[imu_madgwick_filter.py-6] [INFO] [1783057343.422879979] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=439 q_w=0.9993 angle=4.3deg beta=0.0030
[component_container_isolated-17] [INFO] [1783057343.432867939] [local_costmap.local_costmap]: Subscribed to Topics: scan aurora_points tracked_obstacles
[imu_madgwick_filter.py-4] [INFO] [1783057343.440174149] [imu_madgwick_filter]: [imu_madgwick ->] msgs=197 q_w=0.9993 angle=4.4deg beta=0.0330
[component_container_isolated-17] [INFO] [1783057343.693942771] [local_costmap.local_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-17] [INFO] [1783057343.705142231] [local_costmap.local_costmap]: Using plugin "keepout_filter"
[component_container_isolated-17] [INFO] [1783057343.858822005] [local_costmap.local_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-17] [INFO] [1783057343.867171965] [local_costmap.local_costmap]: Using plugin "inflation_layer"
[component_container_isolated-17] [INFO] [1783057343.947781602] [local_costmap.local_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-17] [INFO] [1783057344.137221465] [controller_server]: Created progress_checker : progress_checker of type nav2_controller::SimpleProgressChecker
[component_container_isolated-17] [INFO] [1783057344.173856387] [controller_server]: Created goal checker : goal_checker of type nav2_controller::SimpleGoalChecker
[component_container_isolated-17] [INFO] [1783057344.227318979] [controller_server]: Controller Server has goal_checker  goal checkers available.
[component_container_isolated-17] [INFO] [1783057344.232440438] [controller_server]: Created controller : FollowPath of type nav2_regulated_pure_pursuit_controller::RegulatedPurePursuitController
[depth_detector-18] [INFO] [1783057344.312502159] [depth_detector]: DepthDetector v2 ready: CCL + ground removal + median, 320×200 @ DS=2
[speed_profile_node.py-23] [INFO] [1783057344.390322087] [speed_profile_node]: speed_profile_node started — v_max=0.50 v_min=0.15 beta=0.47 lambda=1.32 max_accel=1.01 max_decel=-1.57
[component_container_isolated-17] [INFO] [1783057344.572192449] [controller_server]: Controller Server has FollowPath  controllers available.
[component_container_isolated-17] [INFO] [1783057344.696870843] [lifecycle_manager_navigation]: Configuring smoother_server
[component_container_isolated-17] [INFO] [1783057344.699200718] [smoother_server]: Configuring smoother server
[component_container_isolated-17] [INFO] [1783057344.867933536] [smoother_server]: Created smoother : SmoothPath of type nav2_constrained_smoother/ConstrainedSmoother
[costmap_publisher-20] [INFO] [1783057344.877351871] [costmap_publisher]: CostmapPublisher ready (tracked_object → PointCloud2)
[component_container_isolated-17] [INFO] [1783057345.022561143] [smoother_server]: Smoother Server has SmoothPath  smoothers available.
[path_optimizer_node.py-22] [INFO] [1783057345.072352443] [path_optimizer_node]: PathOptimizerNode started
[path_optimizer_node.py-22] [INFO] [1783057345.080610944] [path_optimizer_node]: Parameters: lambda=0.100, alpha=0.120, max_shift=0.080 m, scipy=True, iters=50, lr=0.100
[component_container_isolated-17] [INFO] [1783057345.095469946] [lifecycle_manager_navigation]: Configuring planner_server
[component_container_isolated-17] [INFO] [1783057345.097123363] [planner_server]: Configuring
[component_container_isolated-17] [INFO] [1783057345.097511447] [global_costmap.global_costmap]: Configuring
[component_container_isolated-17] [INFO] [1783057345.172734209] [global_costmap.global_costmap]: Using plugin "static_layer"
[component_container_isolated-17] [INFO] [1783057345.188050336] [global_costmap.global_costmap]: Subscribing to the map topic (/map) with transient local durability
[component_container_isolated-17] [INFO] [1783057345.198767004] [global_costmap.global_costmap]: Initialized plugin "static_layer"
[component_container_isolated-17] [INFO] [1783057345.198940921] [global_costmap.global_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-17] [INFO] [1783057345.219843674] [global_costmap.global_costmap]: Subscribed to Topics: scan aurora_points tracked_obstacles
[component_container_isolated-17] [INFO] [1783057345.386369867] [global_costmap.global_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-17] [INFO] [1783057345.387472575] [global_costmap.global_costmap]: Using plugin "keepout_filter"
[component_container_isolated-17] [INFO] [1783057345.409593037] [global_costmap.global_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-17] [INFO] [1783057345.409791537] [global_costmap.global_costmap]: Using plugin "inflation_layer"
[component_container_isolated-17] [INFO] [1783057345.428196498] [global_costmap.global_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-17] [INFO] [1783057345.503605885] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 163 X 141 at 0.050000 m/pix
[component_container_isolated-17] [INFO] [1783057345.541788683] [planner_server]: Created global planner plugin GridBased of type nav2_smac_planner/SmacPlannerHybrid
[component_container_isolated-17] [INFO] [1783057345.542006558] [planner_server]: Configuring GridBased of type SmacPlannerHybrid
[component_container_isolated-17] [INFO] [1783057345.615140694] [planner_server]: Even sized heuristic lookup table size set 200.000000, increasing size by 1 to make odd
[competition_master_stage3.py-21] [INFO] [1783057345.988187960] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-21] [INFO] [1783057345.992793711] [competition_master_stage3]: === [Stage 3] 总控节点初始化 ===
[competition_master_stage3.py-21] [INFO] [1783057345.995708753] [competition_master_stage3]:   QR点:    (0.41, -3.17, yaw=0.00)
[competition_master_stage3.py-21] [INFO] [1783057345.998623879] [competition_master_stage3]:   通道入口: (0.38, -1.10, yaw=0.00)
[competition_master_stage3.py-21] [INFO] [1783057346.003214254] [competition_master_stage3]:   P点:     (-1.99, -0.01, yaw=0.26)
[competition_master_stage3.py-21] [INFO] [1783057346.006830463] [competition_master_stage3]:   cruise_cw: 3 路点 → VLM=(3.01, -1.16)
[competition_master_stage3.py-21] [INFO] [1783057346.011946339] [competition_master_stage3]:   cruise_ccw: 4 路点 → VLM=(2.17, 0.69)
[competition_master_stage3.py-21] [INFO] [1783057346.014927673] [competition_master_stage3]:   超时: total=180.0s QR=90.0s entry=60.0s cruise=180.0s vlm=30.0s return=120.0s
[competition_master_stage3.py-21] [INFO] [1783057346.017982673] [competition_master_stage3]:   回退QR方向: 逆时针
[competition_master_stage3.py-21] [INFO] [1783057346.022108715] [competition_master_stage3]:   VLM结果话题: vlm_result
[competition_master_stage3.py-21] [INFO] [1783057346.025018091] [competition_master_stage3]: ============================================================
[tracker_node-19] [INFO] [1783057346.941189942] [tracker_node]: TrackerNode ready (N=50, 5.0Hz, cost_gate=3.0m)
[hobot_codec_republish-13] [WARN] [1783057347.098407842] [vlm_jpeg_encoder]: Sub imgRaw fps [10.28]
[hobot_codec_republish-13] [WARN] [1783057347.101324467] [vlm_jpeg_encoder]: Pub img fps [10.28]
[tracker_node-19] [INFO] [1783057348.457920055] [tracker_node]: Tracker initialized at (0.02, 0.00)
[rviz2-24] [INFO] [1783057348.723806472] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-24] [INFO] [1783057348.724565805] [rviz2]: OpenGl version: 4.5 (GLSL 4.5)
[rviz2-24] [INFO] [1783057349.866835443] [rviz2]: Stereo is NOT SUPPORTED
[qr_decoder-10] [INFO] [1783057350.697058741] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=200 last_qr_frame=-1 gap=-1 frames rejects=0
[tracker_node-19] [WARN] [1783057351.456872861] [tracker_node]: Measurement timeout (3.1s), pausing tracking
[tracker_node-19] [INFO] [1783057351.657600352] [tracker_node]: Tracker initialized at (0.11, 0.00)
[hobot_codec_republish-13] [WARN] [1783057352.123359509] [vlm_jpeg_encoder]: Sub imgRaw fps [12.94]
[hobot_codec_republish-13] [WARN] [1783057352.125855718] [vlm_jpeg_encoder]: Pub img fps [12.94]
[imu_madgwick_filter.py-6] [INFO] [1783057353.417254590] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=911 q_w=0.9993 angle=4.3deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057353.439225927] [imu_madgwick_filter]: [imu_madgwick ->] msgs=397 q_w=0.9973 angle=8.5deg beta=0.0330
[rviz2-24] [INFO] [1783057354.551999855] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[rviz2-24] [ERROR] [1783057355.516409385] [rviz2]: Vertex Program:rviz/glsl120/indexed_8bit_image.vert Fragment Program:rviz/glsl120/indexed_8bit_image.frag GLSL link result :
[rviz2-24] active samplers with a different type refer to the same texture image unit
[tracker_node-19] [WARN] [1783057356.660370236] [tracker_node]: Reinitializing (divergence=2.37m > 1.5m)
[hobot_codec_republish-13] [WARN] [1783057357.166192943] [vlm_jpeg_encoder]: Sub imgRaw fps [13.49]
[hobot_codec_republish-13] [WARN] [1783057357.172754319] [vlm_jpeg_encoder]: Pub img fps [13.48]
[component_container_isolated-17] [INFO] [1783057361.740073147] [planner_server]: Configured plugin GridBased of type SmacPlannerHybrid with maximum iterations 2027, max on approach iterations 300, and not allowing unknown traversal. Tolerance 0.50.Using motion model: Reeds-Shepp.
[component_container_isolated-17] [INFO] [1783057361.740344064] [planner_server]: Planner Server has GridBased  planners available.
[component_container_isolated-17] [INFO] [1783057361.802203074] [lifecycle_manager_navigation]: Configuring behavior_server
[component_container_isolated-17] [INFO] [1783057361.803160574] [behavior_server]: Configuring
[component_container_isolated-17] [INFO] [1783057361.853409999] [behavior_server]: Creating behavior plugin spin of type nav2_behaviors/Spin
[component_container_isolated-17] [INFO] [1783057361.857601541] [behavior_server]: Configuring spin
[component_container_isolated-17] [INFO] [1783057361.931097678] [behavior_server]: Creating behavior plugin backup of type nav2_behaviors/BackUp
[component_container_isolated-17] [INFO] [1783057361.935519346] [behavior_server]: Configuring backup
[component_container_isolated-17] [INFO] [1783057361.970895685] [behavior_server]: Creating behavior plugin drive_on_heading of type nav2_behaviors/DriveOnHeading
[component_container_isolated-17] [INFO] [1783057361.975237394] [behavior_server]: Configuring drive_on_heading
[component_container_isolated-17] [INFO] [1783057362.035455362] [behavior_server]: Creating behavior plugin wait of type nav2_behaviors/Wait
[component_container_isolated-17] [INFO] [1783057362.039038946] [behavior_server]: Configuring wait
[component_container_isolated-17] [INFO] [1783057362.079966703] [lifecycle_manager_navigation]: Configuring bt_navigator
[component_container_isolated-17] [INFO] [1783057362.080780203] [bt_navigator]: Configuring
[hobot_codec_republish-13] [WARN] [1783057362.233245395] [vlm_jpeg_encoder]: Sub imgRaw fps [13.23]
[hobot_codec_republish-13] [WARN] [1783057362.239868438] [vlm_jpeg_encoder]: Pub img fps [13.23]
[competition_master_stage3.py-21] [INFO] [1783057362.506297940] [competition_master_stage3]: [LAUNCH] 发车阶段: 17.5s
[competition_master_stage3.py-21] [INFO] [1783057362.521460026] [competition_master_stage3]: >>> 系统就绪, 开始 Stage 3 导航
[competition_master_stage3.py-21] [INFO] [1783057362.556654198] [competition_master_stage3]: [BAG] 录制开始: stage3_20260703_134242
[competition_master_stage3.py-21] [INFO] [1783057362.565538908] [competition_master_stage3]: [状态机] INIT → NAV_TO_QR
[component_container_isolated-17] [INFO] [1783057362.586519453] [lifecycle_manager_navigation]: Configuring waypoint_follower
[competition_master_stage3.py-21] [INFO] [1783057362.587747412] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-17] [INFO] [1783057362.587842787] [waypoint_follower]: Configuring
[competition_master_stage3.py-21] [WARN] [1783057362.658074673] [competition_master_stage3]: 导航目标被拒绝, 3s 后重试...
[component_container_isolated-17] [INFO] [1783057362.741123187] [waypoint_follower]: Created waypoint_task_executor : wait_at_waypoint of type nav2_waypoint_follower::WaitAtWaypoint
[component_container_isolated-17] [INFO] [1783057362.751392855] [lifecycle_manager_navigation]: Configuring velocity_smoother
[component_container_isolated-17] [INFO] [1783057362.753032980] [velocity_smoother]: Configuring velocity smoother
[component_container_isolated-17] [INFO] [1783057362.781759777] [lifecycle_manager_navigation]: Activating controller_server
[component_container_isolated-17] [INFO] [1783057362.782661860] [controller_server]: Activating
[component_container_isolated-17] [INFO] [1783057362.782932277] [local_costmap.local_costmap]: Activating
[component_container_isolated-17] [INFO] [1783057362.783048902] [local_costmap.local_costmap]: Checking transform
[component_container_isolated-17] [INFO] [1783057362.783435860] [local_costmap.local_costmap]: start
[component_container_isolated-17] [INFO] [1783057362.802829947] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057362.819996200] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057362.820185700] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [INFO] [1783057362.829394410] [local_costmap.local_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[competition_master_stage3.py-21] [INFO] [1783057363.071658741] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.01,-0.02) yaw=14deg cmd=(vx=0.00 wz=0.00) elapsed=0.5s cpuFreq=1500MHz cpuT=74C cpu=88% mem=20%
[component_container_isolated-17] [INFO] [1783057363.119901874] [controller_server]: Activating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-17] [INFO] [1783057363.120199416] [controller_server]: Creating bond (controller_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057363.239007727] [lifecycle_manager_navigation]: Server controller_server connected with bond.
[component_container_isolated-17] [INFO] [1783057363.239209019] [lifecycle_manager_navigation]: Activating smoother_server
[component_container_isolated-17] [INFO] [1783057363.242394853] [smoother_server]: Activating
[component_container_isolated-17] [INFO] [1783057363.242726145] [smoother_server]: Activating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-17] [INFO] [1783057363.242886770] [smoother_server]: Creating bond (smoother_server) to lifecycle manager.
[tracker_node-19] [WARN] [1783057363.257670730] [tracker_node]: Measurement timeout (3.1s), pausing tracking
[component_container_isolated-17] [INFO] [1783057363.371610416] [lifecycle_manager_navigation]: Server smoother_server connected with bond.
[component_container_isolated-17] [INFO] [1783057363.371787374] [lifecycle_manager_navigation]: Activating planner_server
[component_container_isolated-17] [INFO] [1783057363.372880583] [planner_server]: Activating
[component_container_isolated-17] [INFO] [1783057363.373156749] [global_costmap.global_costmap]: Activating
[component_container_isolated-17] [INFO] [1783057363.373232333] [global_costmap.global_costmap]: Checking transform
[component_container_isolated-17] [INFO] [1783057363.373490958] [global_costmap.global_costmap]: start
[component_container_isolated-17] [INFO] [1783057363.399306504] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[imu_madgwick_filter.py-6] [INFO] [1783057363.414205840] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1424 q_w=0.9993 angle=4.2deg beta=0.0030
[component_container_isolated-17] [INFO] [1783057363.429954634] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057363.430131092] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [INFO] [1783057363.441303094] [global_costmap.global_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[imu_madgwick_filter.py-4] [INFO] [1783057363.442424969] [imu_madgwick_filter]: [imu_madgwick ->] msgs=593 q_w=0.9938 angle=12.8deg beta=0.0330
[tracker_node-19] [INFO] [1783057363.456346221] [tracker_node]: Tracker initialized at (0.02, 0.00)
[tracker_node-19] [WARN] [1783057363.657114296] [tracker_node]: Measurement timeout (3.5s), pausing tracking
[tracker_node-19] [INFO] [1783057363.856446746] [tracker_node]: Tracker initialized at (0.02, 0.00)
[rviz2-24] [INFO] [1783057363.971862015] [rviz2]: Trying to create a map of size 60 x 60 using 1 swatches
[component_container_isolated-17] [INFO] [1783057364.629871791] [planner_server]: Activating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-17] [INFO] [1783057364.639092501] [planner_server]: Creating bond (planner_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057364.778646649] [lifecycle_manager_navigation]: Server planner_server connected with bond.
[component_container_isolated-17] [INFO] [1783057364.778845357] [lifecycle_manager_navigation]: Activating behavior_server
[component_container_isolated-17] [INFO] [1783057364.780293691] [behavior_server]: Activating
[component_container_isolated-17] [INFO] [1783057364.780529441] [behavior_server]: Activating spin
[component_container_isolated-17] [INFO] [1783057364.780709524] [behavior_server]: Activating backup
[component_container_isolated-17] [INFO] [1783057364.780819191] [behavior_server]: Activating drive_on_heading
[component_container_isolated-17] [INFO] [1783057364.780896566] [behavior_server]: Activating wait
[component_container_isolated-17] [INFO] [1783057364.780979482] [behavior_server]: Creating bond (behavior_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057364.910595837] [lifecycle_manager_navigation]: Server behavior_server connected with bond.
[component_container_isolated-17] [INFO] [1783057364.911180046] [lifecycle_manager_navigation]: Activating bt_navigator
[component_container_isolated-17] [INFO] [1783057364.914601338] [bt_navigator]: Activating
[competition_master_stage3.py-21] [INFO] [1783057365.090238659] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.01,-0.02) yaw=14deg cmd=(vx=0.00 wz=0.00) elapsed=2.5s cpuFreq=1500MHz cpuT=75C cpu=100% mem=21%
[component_container_isolated-17] [WARN] [1783057365.153781044] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-17] [WARN] [1783057365.335357366] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-17] [WARN] [1783057365.489771725] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[rviz2-24] [INFO] [1783057365.651648585] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[competition_master_stage3.py-21] [INFO] [1783057365.688834175] [competition_master_stage3]: 重试发送导航目标 (QR点)...
[component_container_isolated-17] [WARN] [1783057365.737174725] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[competition_master_stage3.py-21] [INFO] [1783057365.757565228] [competition_master_stage3]: [DIAG] nav目标距离: 3.97m, robot=(-2.01,-0.02) → target=(0.41,-3.17)
[competition_master_stage3.py-21] [INFO] [1783057365.782772357] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-17] [WARN] [1783057366.007175895] [bt_navigator_navigate_to_pose_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-17] [INFO] [1783057366.270733980] [bt_navigator]: Creating bond (bt_navigator) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057366.301346902] [bt_navigator]: Begin navigating from current location (-2.01, -0.02) to (0.41, -3.17)
[component_container_isolated-17] [INFO] [1783057366.302629402] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[competition_master_stage3.py-21] [INFO] [1783057366.316467571] [competition_master_stage3]: 导航目标已接受，车辆出发...
[component_container_isolated-17] [INFO] [1783057366.326645156] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057366.341479992] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057366.341639117] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057366.357294161] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [INFO] [1783057366.389692583] [lifecycle_manager_navigation]: Server bt_navigator connected with bond.
[component_container_isolated-17] [INFO] [1783057366.391119834] [lifecycle_manager_navigation]: Activating waypoint_follower
[component_container_isolated-17] [INFO] [1783057366.394824668] [waypoint_follower]: Activating
[component_container_isolated-17] [INFO] [1783057366.395104584] [waypoint_follower]: Creating bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057366.522947397] [lifecycle_manager_navigation]: Server waypoint_follower connected with bond.
[component_container_isolated-17] [INFO] [1783057366.523122856] [lifecycle_manager_navigation]: Activating velocity_smoother
[component_container_isolated-17] [INFO] [1783057366.525783398] [velocity_smoother]: Activating
[component_container_isolated-17] [INFO] [1783057366.526206814] [velocity_smoother]: Creating bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-17] [WARN] [1783057366.563462071] [planner_server]: GridBased: failed to create plan, no valid path found.
[component_container_isolated-17] [WARN] [1783057366.563720696] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.41, -3.17)
[component_container_isolated-17] [WARN] [1783057366.563833821] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[imu_madgwick_filter.py-4] [WARN] [1783057366.668431213] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1500s > 0.15s, capping
[component_container_isolated-17] [INFO] [1783057366.675226089] [lifecycle_manager_navigation]: Server velocity_smoother connected with bond.
[component_container_isolated-17] [INFO] [1783057366.675407173] [lifecycle_manager_navigation]: Managed nodes are active
[component_container_isolated-17] [INFO] [1783057366.675477589] [lifecycle_manager_navigation]: Creating bond timer...
[component_container_isolated-17] [INFO] [1783057366.721198764] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057366.751582394] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057366.766409646] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057366.766583813] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [INFO] [1783057366.777274023] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057366.812658404] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [WARN] [1783057366.816868405] [BehaviorTreeEngine]: Behavior Tree tick rate 10.00 was exceeded!
[component_container_isolated-17] [INFO] [1783057366.834317824] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057366.834484283] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057366.852539577] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [WARN] [1783057367.056466361] [tracker_node]: Measurement timeout (3.2s), pausing tracking
[competition_master_stage3.py-21] [INFO] [1783057367.079625782] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.01,-0.02) yaw=14deg cmd=(vx=0.00 wz=0.00) elapsed=4.5s cpuFreq=1500MHz cpuT=76C cpu=83% mem=21%
[tracker_node-19] [INFO] [1783057367.256332603] [tracker_node]: Tracker initialized at (-0.11, 0.00)
[qr_decoder-10] [INFO] [1783057367.263657813] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=400 last_qr_frame=-1 gap=-1 frames rejects=0
[hobot_codec_republish-13] [WARN] [1783057367.281837399] [vlm_jpeg_encoder]: Sub imgRaw fps [10.30]
[hobot_codec_republish-13] [WARN] [1783057367.284299983] [vlm_jpeg_encoder]: Pub img fps [10.31]
[component_container_isolated-17] [WARN] [1783057367.398072960] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.7768 Hz
[path_optimizer_node.py-22] [INFO] [1783057367.430296049] [path_optimizer_node]: Path optimised (34 pts, 8.4 ms): mean |kappa| 0.7657 -> 0.8242 (-7.6%), max |kappa| 3.3333 -> 4.6943 (-40.8%), max shift 0.080 m
[tracker_node-19] [WARN] [1783057367.455765136] [tracker_node]: Measurement timeout (3.6s), pausing tracking
[speed_profile_node.py-23] [INFO] [1783057367.464518138] [speed_profile_node]: Plan received: 34 poses, mean|κ|=0.8349 m⁻¹, max|κ|=3.3066 m⁻¹, mean_v=0.385 m/s, min_v=0.153 m/s, max_v=0.498 m/s
[component_container_isolated-17] [INFO] [1783057367.505449478] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-17] [WARN] [1783057367.505785228] [controller_server]: No goal checker was specified in parameter 'current_goal_checker'. Server will use only plugin loaded goal_checker . This warning will appear once.
[tracker_node-19] [INFO] [1783057367.656326462] [tracker_node]: Tracker initialized at (-0.11, 0.00)
[tracker_node-19] [WARN] [1783057367.857337037] [tracker_node]: Measurement timeout (4.0s), pausing tracking
[tracker_node-19] [INFO] [1783057368.056924529] [tracker_node]: Tracker initialized at (-0.11, 0.00)
[tracker_node-19] [WARN] [1783057368.256539354] [tracker_node]: Measurement timeout (4.4s), pausing tracking
[tracker_node-19] [INFO] [1783057368.460259180] [tracker_node]: Tracker initialized at (-0.11, 0.00)
[component_container_isolated-17] [INFO] [1783057368.602723870] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057368.618964206] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057368.630567000] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057368.630721542] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057368.843084036] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057369.078299200] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.80,-0.00) yaw=-0deg cmd=(vx=0.40 wz=0.09) elapsed=6.5s plan[34pts 4.7m] (-2.00,-0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=76C cpu=85% mem=22%
[component_container_isolated-17] Reallocing temp weights 301 - 60
[component_container_isolated-17] [WARN] [1783057369.394908837] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3002 Hz
[path_optimizer_node.py-22] [INFO] [1783057369.437098802] [path_optimizer_node]: Path optimised (32 pts, 4.8 ms): mean |kappa| 0.8101 -> 0.8801 (-8.6%), max |kappa| 3.3333 -> 4.8618 (-45.9%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057369.492546978] [speed_profile_node]: Plan received: 32 poses, mean|κ|=0.8957 m⁻¹, max|κ|=3.4718 m⁻¹, mean_v=0.379 m/s, min_v=0.150 m/s, max_v=0.499 m/s
[component_container_isolated-17] [INFO] [1783057369.506068481] [controller_server]: Passing new path to controller.
[component_container_isolated-17] [INFO] [1783057370.602553249] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057370.625273294] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057370.636616213] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057370.636746713] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057370.647489590] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057371.080043871] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.08,0.01) yaw=-2deg cmd=(vx=-0.13 wz=0.05) elapsed=8.5s plan[32pts 4.3m] (-1.60,0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=76C cpu=93% mem=21%
[component_container_isolated-17] [WARN] [1783057371.394296841] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3379 Hz
[path_optimizer_node.py-22] [INFO] [1783057371.417129303] [path_optimizer_node]: Path optimised (25 pts, 9.0 ms): mean |kappa| 0.8044 -> 0.6406 (20.4%), max |kappa| 3.3333 -> 4.4021 (-32.1%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057371.439855432] [speed_profile_node]: Plan received: 25 poses, mean|κ|=0.6657 m⁻¹, max|κ|=2.9709 m⁻¹, mean_v=0.414 m/s, min_v=0.168 m/s, max_v=0.495 m/s
[component_container_isolated-17] [INFO] [1783057371.506068694] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057371.656705552] [tracker_node]: Measurement timeout (3.0s), pausing tracking
[tracker_node-19] [INFO] [1783057371.857178545] [tracker_node]: Tracker initialized at (0.02, 0.00)
[hobot_codec_republish-13] [WARN] [1783057372.294449702] [vlm_jpeg_encoder]: Sub imgRaw fps [13.37]
[hobot_codec_republish-13] [WARN] [1783057372.301454870] [vlm_jpeg_encoder]: Pub img fps [13.36]
[component_container_isolated-17] [INFO] [1783057372.602695338] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057372.616481424] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057372.625070634] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057372.625225467] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057372.637159177] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057373.077524127] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.87,-0.01) yaw=-10deg cmd=(vx=0.19 wz=-0.97) elapsed=10.5s plan[25pts 3.5m] (-0.90,-0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=76C cpu=88% mem=22%
[component_container_isolated-17] [WARN] [1783057373.389582555] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3099 Hz
[imu_madgwick_filter.py-6] [INFO] [1783057373.414124768] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1798 q_w=0.9108 angle=48.8deg beta=0.0030
[path_optimizer_node.py-22] [INFO] [1783057373.418305810] [path_optimizer_node]: Path optimised (24 pts, 10.6 ms): mean |kappa| 0.4741 -> 0.5263 (-11.0%), max |kappa| 3.3333 -> 3.4345 (-3.0%), max shift 0.080 m
[imu_madgwick_filter.py-4] [INFO] [1783057373.440140731] [imu_madgwick_filter]: [imu_madgwick ->] msgs=788 q_w=0.9661 angle=29.9deg beta=0.0330
[speed_profile_node.py-23] [INFO] [1783057373.457068775] [speed_profile_node]: Plan received: 24 poses, mean|κ|=0.5403 m⁻¹, max|κ|=2.3853 m⁻¹, mean_v=0.426 m/s, min_v=0.202 m/s, max_v=0.497 m/s
[component_container_isolated-17] [INFO] [1783057373.506526367] [controller_server]: Passing new path to controller.
[component_container_isolated-17] Reallocing temp weights 1500 - 60
[component_container_isolated-17] [INFO] [1783057374.503601537] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057374.534680209] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057374.548669753] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057374.548824587] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057374.578727217] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057375.077319802] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.59,-0.26) yaw=-76deg cmd=(vx=0.40 wz=0.28) elapsed=12.5s plan[24pts 3.4m] (-0.80,-0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=76C cpu=100% mem=22%
[component_container_isolated-17] [WARN] [1783057375.390194022] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2009 Hz
[path_optimizer_node.py-22] [INFO] [1783057375.405354817] [path_optimizer_node]: Path optimised (21 pts, 3.8 ms): mean |kappa| 0.4004 -> 0.5983 (-49.4%), max |kappa| 3.3333 -> 3.6478 (-9.4%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057375.441980448] [speed_profile_node]: Plan received: 21 poses, mean|κ|=0.6108 m⁻¹, max|κ|=2.6087 m⁻¹, mean_v=0.417 m/s, min_v=0.188 m/s, max_v=0.500 m/s
[component_container_isolated-17] [INFO] [1783057375.506126542] [controller_server]: Passing new path to controller.
[component_container_isolated-17] [INFO] [1783057376.603126106] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057376.624233610] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057376.639595196] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057376.639798321] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057376.655131698] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-4] [WARN] [1783057376.813731267] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.2000s > 0.15s, capping
[tracker_node-19] [WARN] [1783057376.866824693] [tracker_node]: Reinitializing (divergence=2.15m > 1.5m)
[competition_master_stage3.py-21] [INFO] [1783057377.081485105] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.39,-0.93) yaw=-77deg cmd=(vx=0.40 wz=-0.06) elapsed=14.5s plan[21pts 2.8m] (-0.50,-0.55)→(0.40,-3.15) cpuFreq=1500MHz cpuT=76C cpu=88% mem=22%
[hobot_codec_republish-13] [WARN] [1783057377.340365816] [vlm_jpeg_encoder]: Sub imgRaw fps [13.28]
[hobot_codec_republish-13] [WARN] [1783057377.345648817] [vlm_jpeg_encoder]: Pub img fps [13.28]
[component_container_isolated-17] [WARN] [1783057377.400549743] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-17] [WARN] [1783057377.400825618] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.41, -3.17)
[component_container_isolated-17] [WARN] [1783057377.400937243] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-17] [INFO] [1783057377.502838136] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057377.516504597] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057377.522205431] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057377.532228891] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057377.545686602] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057377.545845435] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057377.556912562] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057378.384701747] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2008 Hz
[path_optimizer_node.py-22] [INFO] [1783057378.405707250] [path_optimizer_node]: Path optimised (17 pts, 3.5 ms): mean |kappa| 1.1344 -> 1.3614 (-20.0%), max |kappa| 3.3333 -> 3.8336 (-15.0%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057378.437768089] [speed_profile_node]: Plan received: 17 poses, mean|κ|=1.2721 m⁻¹, max|κ|=2.7033 m⁻¹, mean_v=0.323 m/s, min_v=0.182 m/s, max_v=0.419 m/s
[component_container_isolated-17] [INFO] [1783057378.506053393] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057379.076323033] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.31,-1.16) yaw=-81deg cmd=(vx=0.40 wz=-0.73) elapsed=16.5s plan[17pts 2.4m] (-0.30,-1.15)→(0.40,-3.15) cpuFreq=1500MHz cpuT=76C cpu=93% mem=22%
[component_container_isolated-17] [INFO] [1783057379.602676041] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057379.625884170] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057379.641343923] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057379.641534215] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057379.656705759] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057380.387542053] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3989 Hz
[path_optimizer_node.py-22] [INFO] [1783057380.403841139] [path_optimizer_node]: Path optimised (15 pts, 3.3 ms): mean |kappa| 0.7534 -> 0.7313 (2.9%), max |kappa| 3.3333 -> 3.0810 (7.6%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057380.443306771] [speed_profile_node]: Plan received: 15 poses, mean|κ|=0.7266 m⁻¹, max|κ|=1.9911 m⁻¹, mean_v=0.395 m/s, min_v=0.231 m/s, max_v=0.479 m/s
[component_container_isolated-17] [INFO] [1783057380.506064823] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057381.077755048] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.35,-1.37) yaw=-115deg cmd=(vx=0.26 wz=0.97) elapsed=18.5s plan[15pts 2.0m] (-0.30,-1.35)→(0.40,-3.15) cpuFreq=1500MHz cpuT=77C cpu=71% mem=22%
[component_container_isolated-17] [INFO] [1783057381.602552973] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057381.619837726] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057381.636859771] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057381.637051771] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057381.647650523] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[hobot_codec_republish-13] [WARN] [1783057382.370594358] [vlm_jpeg_encoder]: Sub imgRaw fps [12.73]
[hobot_codec_republish-13] [WARN] [1783057382.375869067] [vlm_jpeg_encoder]: Pub img fps [12.73]
[component_container_isolated-17] [WARN] [1783057382.388837652] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3295 Hz
[path_optimizer_node.py-22] [INFO] [1783057382.400269863] [path_optimizer_node]: Path optimised (13 pts, 2.9 ms): mean |kappa| 0.6912 -> 0.4560 (34.0%), max |kappa| 3.3333 -> 1.2873 (61.4%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057382.431273535] [speed_profile_node]: Plan received: 13 poses, mean|κ|=0.4340 m⁻¹, max|κ|=0.9247 m⁻¹, mean_v=0.433 m/s, min_v=0.351 m/s, max_v=0.486 m/s
[component_container_isolated-17] [INFO] [1783057382.506074840] [controller_server]: Passing new path to controller.
[qr_decoder-10] [INFO] [1783057382.905526993] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=600 last_qr_frame=-1 gap=-1 frames rejects=0
[competition_master_stage3.py-21] [INFO] [1783057383.087310566] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.49,-1.71) yaw=-104deg cmd=(vx=0.31 wz=0.59) elapsed=20.5s plan[13pts 1.7m] (-0.50,-1.75)→(0.40,-3.15) cpuFreq=1500MHz cpuT=76C cpu=100% mem=22%
[imu_madgwick_filter.py-6] [INFO] [1783057383.416914583] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2213 q_w=0.5067 angle=119.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057383.439705670] [imu_madgwick_filter]: [imu_madgwick ->] msgs=975 q_w=0.6969 angle=91.6deg beta=0.0330
[component_container_isolated-17] [INFO] [1783057383.512574141] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057383.540770438] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057383.553676315] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057383.553869523] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057383.569884568] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057384.404457381] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.1733 Hz
[path_optimizer_node.py-22] [INFO] [1783057384.434361512] [path_optimizer_node]: Path optimised (11 pts, 7.3 ms): mean |kappa| 0.6204 -> 0.2193 (64.6%), max |kappa| 3.3306 -> 0.4681 (85.9%), max shift 0.077 m
[speed_profile_node.py-23] [INFO] [1783057384.455608182] [speed_profile_node]: Plan received: 11 poses, mean|κ|=0.1956 m⁻¹, max|κ|=0.3176 m⁻¹, mean_v=0.473 m/s, min_v=0.453 m/s, max_v=0.498 m/s
[component_container_isolated-17] [INFO] [1783057384.606255834] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057385.056741955] [tracker_node]: Measurement timeout (3.0s), pausing tracking
[competition_master_stage3.py-21] [INFO] [1783057385.078824459] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.39,-2.09) yaw=-61deg cmd=(vx=0.40 wz=0.06) elapsed=22.5s plan[11pts 1.5m] (-0.50,-1.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=76C cpu=90% mem=22%
[tracker_node-19] [INFO] [1783057385.256774865] [tracker_node]: Tracker initialized at (-0.06, 0.00)
[qr_decoder-10] [INFO] [1783057385.453074900] [qr_decoder_zbar]: [qr_decoder] QR DETECTED frame=631 symbols=1 (gap=-1 frames)
[tracker_node-19] [WARN] [1783057385.456749234] [tracker_node]: Measurement timeout (3.4s), pausing tracking
[qr_decoder-10] [INFO] [1783057385.457484359] [qr_decoder_zbar]: [QR] 1584 | depth=0mm (advisory, publishing anyway)
[qr_decoder-10] [INFO] [1783057385.463755318] [qr_decoder_zbar]: [QR] 1584 | robot_pos: (0.44, -2.48, yaw=-1.69)
[competition_master_stage3.py-21] [INFO] [1783057385.470837486] [competition_master_stage3]: [QR检测] 内容: 1584
[competition_master_stage3.py-21] [INFO] [1783057385.478721571] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decoder_zbar
[qr_decision-11] [INFO] [1783057385.478659238] [qr_decision]: [QR] 1584 CCW @ (x=0.43, y=-2.53, yaw=-1.69) → /qr_event
[competition_master_stage3.py-21] [INFO] [1783057385.485015239] [competition_master_stage3]: >>> QR 解码已关闭, 等待方向判断 (/qr_event)...
[qr_decision-11] [INFO] [1783057385.485409739] [qr_decision]: [检查点] qr_decision 发布 /qr_event (由 task_manager 决定停车)
[competition_master_stage3.py-21] [INFO] [1783057385.488593989] [competition_master_stage3]: [QR检测] 取消当前导航目标, 等待BT完成 cancel/halt 清理...
[competition_master_stage3.py-21] [INFO] [1783057385.502471200] [competition_master_stage3]: [QR事件] 方向: 逆时针 (通道巡航阶段使用)
[component_container_isolated-17] [INFO] [1783057385.506788576] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-17] [INFO] [1783057385.507037368] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-17] [INFO] [1783057385.511463119] [bt_navigator]: [navigate_to_pose] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-17] [INFO] [1783057385.512210910] [bt_navigator]: Goal canceled
[competition_master_stage3.py-21] [INFO] [1783057385.524704788] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decision
[qr_decoder-10] [INFO] [1783057385.548523542] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[competition_master_stage3.py-21] [INFO] [1783057385.554247209] [competition_master_stage3]: [结果回调] BT取消确认完成 (STATUS_CANCELED), 准备发送通道入口目标...
[competition_master_stage3.py-21] [INFO] [1783057385.560677919] [competition_master_stage3]: [状态机] NAV_TO_QR → BACKING_UP
[competition_master_stage3.py-21] [INFO] [1783057385.570298337] [competition_master_stage3]: >>> BT取消完成, 右后退摆正车头→前进进通道...
[competition_master_stage3.py-21] [INFO] [1783057385.576188338] [competition_master_stage3]: [BACKUP] 右后退中: vx=-0.15 wz=0.80, 持续 6.0s...
[tracker_node-19] [INFO] [1783057385.662392604] [tracker_node]: Tracker initialized at (-0.06, 0.00)
[tracker_node-19] [WARN] [1783057385.856256804] [tracker_node]: Measurement timeout (3.8s), pausing tracking
[qr_decision-11] Traceback (most recent call last):
[qr_decision-11]   File "/userdata/dev_ws/install/origincar_qr/lib/origincar_qr/qr_decision", line 33, in <module>
[qr_decision-11]     sys.exit(load_entry_point('origincar-qr==0.0.0', 'console_scripts', 'qr_decision')())
[qr_decision-11]   File "/userdata/dev_ws/install/origincar_qr/lib/python3.10/site-packages/origincar_qr/qr_decision.py", line 97, in main
[qr_decision-11]     rclpy.spin(node)
[qr_decision-11]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 229, in spin
[qr_decision-11]     executor.spin_once()
[qr_decision-11]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 808, in spin_once
[qr_decision-11]     self._spin_once_impl(timeout_sec)
[qr_decision-11]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 797, in _spin_once_impl
[qr_decision-11]     handler, entity, node = self.wait_for_ready_callbacks(timeout_sec=timeout_sec)
[qr_decision-11]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 780, in wait_for_ready_callbacks
[qr_decision-11]     return next(self._cb_iter)
[qr_decision-11]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 681, in _wait_for_ready_callbacks
[qr_decision-11]     raise ExternalShutdownException()
[qr_decision-11] rclpy.executors.ExternalShutdownException
[INFO] [qr_decoder-10]: process has finished cleanly [pid 22575]
[tracker_node-19] [INFO] [1783057386.056951882] [tracker_node]: Tracker initialized at (-0.06, 0.00)
[tracker_node-19] [WARN] [1783057386.257094292] [tracker_node]: Measurement timeout (4.2s), pausing tracking
[tracker_node-19] [INFO] [1783057386.456506202] [tracker_node]: Tracker initialized at (-0.06, 0.00)
[tracker_node-19] [WARN] [1783057386.657206321] [tracker_node]: Measurement timeout (4.6s), pausing tracking
[ERROR] [qr_decision-11]: process has died [pid 22577, exit code 1, cmd '/userdata/dev_ws/install/origincar_qr/lib/origincar_qr/qr_decision --ros-args -r __node:=qr_decision --params-file /tmp/launch_params_u5b8gw2c'].
[tracker_node-19] [INFO] [1783057386.856346482] [tracker_node]: Tracker initialized at (-0.06, 0.00)
[tracker_node-19] [WARN] [1783057387.056925392] [tracker_node]: Measurement timeout (5.0s), pausing tracking
[competition_master_stage3.py-21] [INFO] [1783057387.070384228] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.25,-2.28) yaw=-54deg cmd=(vx=-0.15 wz=0.80) elapsed=24.5s plan[11pts 1.5m] (-0.50,-1.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=76C cpu=88% mem=21%
[tracker_node-19] [INFO] [1783057387.257729761] [tracker_node]: Tracker initialized at (-0.06, 0.00)
[hobot_codec_republish-13] [WARN] [1783057387.425622333] [vlm_jpeg_encoder]: Sub imgRaw fps [12.66]
[hobot_codec_republish-13] [WARN] [1783057387.428010250] [vlm_jpeg_encoder]: Pub img fps [12.67]
[tracker_node-19] [WARN] [1783057387.456782838] [tracker_node]: Measurement timeout (5.4s), pausing tracking
[tracker_node-19] [INFO] [1783057387.656474666] [tracker_node]: Tracker initialized at (-0.06, 0.00)
[tracker_node-19] [WARN] [1783057387.862476161] [tracker_node]: Measurement timeout (5.8s), pausing tracking
[tracker_node-19] [INFO] [1783057388.056816570] [tracker_node]: Tracker initialized at (-0.06, 0.00)
[competition_master_stage3.py-21] [INFO] [1783057389.072410168] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.13,-2.42) yaw=-35deg cmd=(vx=-0.15 wz=0.80) elapsed=26.5s plan[11pts 1.5m] (-0.50,-1.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=76C cpu=80% mem=21%
[competition_master_stage3.py-21] [INFO] [1783057391.075601235] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.42,-2.36) yaw=24deg cmd=(vx=-0.15 wz=0.80) elapsed=28.5s plan[11pts 1.5m] (-0.50,-1.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=76C cpu=90% mem=21%
[tracker_node-19] [WARN] [1783057391.257134976] [tracker_node]: Measurement timeout (3.1s), pausing tracking
[tracker_node-19] [INFO] [1783057391.457829262] [tracker_node]: Tracker initialized at (0.03, 0.00)
[competition_master_stage3.py-21] [INFO] [1783057391.583417243] [competition_master_stage3]: [状态机] BACKING_UP → CRUISE_CHANNEL
[competition_master_stage3.py-21] [INFO] [1783057391.587943827] [competition_master_stage3]: [CRUISE] 方向: CCW (逆时针, even QR), 路点: (0.25,-1.17), (1.66,-1.50), (2.90,-0.90), (2.17,0.69)
[competition_master_stage3.py-21] [INFO] [1783057391.611541040] [competition_master_stage3]: [CRUISE] NavigateThroughPoses: (0.38,-1.10), (0.25,-1.17), (1.66,-1.50), (2.90,-0.90), (2.17,0.69)
[component_container_isolated-17] [INFO] [1783057391.617981958] [bt_navigator]: Begin navigating from current location through 5 poses to (2.17, 0.69)
[component_container_isolated-17] [INFO] [1783057391.619144291] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057391.635078127] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[competition_master_stage3.py-21] [INFO] [1783057391.642334795] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[component_container_isolated-17] [INFO] [1783057391.647732546] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057391.647902880] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[tracker_node-19] [WARN] [1783057391.656890131] [tracker_node]: Measurement timeout (3.5s), pausing tracking
[component_container_isolated-17] [WARN] [1783057391.677511468] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [INFO] [1783057391.857675626] [tracker_node]: Tracker initialized at (0.03, 0.00)
[tracker_node-19] [WARN] [1783057392.056249495] [tracker_node]: Measurement timeout (3.9s), pausing tracking
[tracker_node-19] [INFO] [1783057392.256849448] [tracker_node]: Tracker initialized at (0.03, 0.00)
[component_container_isolated-17] [WARN] [1783057392.413849309] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3163 Hz
[hobot_codec_republish-13] [WARN] [1783057392.432363396] [vlm_jpeg_encoder]: Sub imgRaw fps [13.58]
[hobot_codec_republish-13] [WARN] [1783057392.435303021] [vlm_jpeg_encoder]: Pub img fps [13.58]
[path_optimizer_node.py-22] [INFO] [1783057392.455287192] [path_optimizer_node]: Path optimised (67 pts, 9.8 ms): mean |kappa| 2.0306 -> 3.5071 (-72.7%), max |kappa| 13.2078 -> 17.6561 (-33.7%), max shift 0.080 m
[tracker_node-19] [WARN] [1783057392.456003025] [tracker_node]: Measurement timeout (4.3s), pausing tracking
[speed_profile_node.py-23] [INFO] [1783057392.514619077] [speed_profile_node]: Plan received: 67 poses, mean|κ|=3.4977 m⁻¹, max|κ|=11.3340 m⁻¹, mean_v=0.244 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[component_container_isolated-17] [INFO] [1783057392.523496787] [controller_server]: Received a goal, begin computing control effort.
[tracker_node-19] [INFO] [1783057392.656335811] [tracker_node]: Tracker initialized at (0.03, 0.00)
[tracker_node-19] [WARN] [1783057392.857263889] [tracker_node]: Measurement timeout (4.7s), pausing tracking
[tracker_node-19] [INFO] [1783057393.057355925] [tracker_node]: Tracker initialized at (0.03, 0.00)
[competition_master_stage3.py-21] [INFO] [1783057393.077675512] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.54,-2.45) yaw=52deg cmd=(vx=-0.30 wz=-0.34) elapsed=30.5s plan[67pts 9.2m] (-0.60,-2.45)→(2.20,0.65) cpuFreq=1500MHz cpuT=76C cpu=88% mem=21%
[tracker_node-19] [WARN] [1783057393.257508170] [tracker_node]: Measurement timeout (5.1s), pausing tracking
[imu_madgwick_filter.py-6] [INFO] [1783057393.438115661] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2690 q_w=0.9530 angle=35.3deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057393.440859161] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1167 q_w=0.8402 angle=65.7deg beta=0.0330
[tracker_node-19] [INFO] [1783057393.456808164] [tracker_node]: Tracker initialized at (0.03, 0.00)
[component_container_isolated-17] [INFO] [1783057393.619079319] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057393.629398820] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057393.636975738] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057393.637134155] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057393.643767906] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057394.413108337] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2894 Hz
[path_optimizer_node.py-22] [INFO] [1783057394.444880260] [path_optimizer_node]: Path optimised (71 pts, 6.5 ms): mean |kappa| 2.0849 -> 3.2394 (-55.4%), max |kappa| 13.2078 -> 17.1029 (-29.5%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057394.518732607] [speed_profile_node]: Plan received: 71 poses, mean|κ|=3.2480 m⁻¹, max|κ|=11.3340 m⁻¹, mean_v=0.243 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[component_container_isolated-17] [INFO] [1783057394.526060066] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057395.074067832] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.72,-2.66) yaw=53deg cmd=(vx=-0.30 wz=-0.50) elapsed=32.5s plan[71pts 9.6m] (-0.70,-2.65)→(2.20,0.65) cpuFreq=1500MHz cpuT=76C cpu=90% mem=21%
[component_container_isolated-17] [INFO] [1783057395.619997682] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057395.633244142] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057395.644938769] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057395.645106144] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057395.656837355] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057396.403071658] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3246 Hz
[path_optimizer_node.py-22] [INFO] [1783057396.461490793] [path_optimizer_node]: Path optimised (66 pts, 6.4 ms): mean |kappa| 1.8118 -> 3.1246 (-72.5%), max |kappa| 13.2078 -> 13.3284 (-0.9%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057396.508700343] [speed_profile_node]: Plan received: 66 poses, mean|κ|=3.0338 m⁻¹, max|κ|=11.3340 m⁻¹, mean_v=0.269 m/s, min_v=0.150 m/s, max_v=0.500 m/s
[component_container_isolated-17] [INFO] [1783057396.523969180] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057397.080124864] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.68,-2.58) yaw=54deg cmd=(vx=0.40 wz=0.24) elapsed=34.5s plan[66pts 9.0m] (-0.70,-2.65)→(2.20,0.65) cpuFreq=1500MHz cpuT=76C cpu=80% mem=21%
[hobot_codec_republish-13] [WARN] [1783057397.436059971] [vlm_jpeg_encoder]: Sub imgRaw fps [12.99]
[hobot_codec_republish-13] [WARN] [1783057397.438927013] [vlm_jpeg_encoder]: Pub img fps [12.99]
[component_container_isolated-17] [INFO] [1783057397.619004505] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057397.627747881] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057397.638995342] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057397.639168842] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057397.651695094] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057398.413376817] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2922 Hz
[path_optimizer_node.py-22] [INFO] [1783057398.451938199] [path_optimizer_node]: Path optimised (64 pts, 5.5 ms): mean |kappa| 2.1202 -> 3.5695 (-68.4%), max |kappa| 13.2078 -> 18.9465 (-43.4%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057398.521819503] [speed_profile_node]: Plan received: 64 poses, mean|κ|=3.4620 m⁻¹, max|κ|=11.3339 m⁻¹, mean_v=0.264 m/s, min_v=0.150 m/s, max_v=0.499 m/s
[component_container_isolated-17] [INFO] [1783057398.523960004] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057399.076797147] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.66,-2.51) yaw=50deg cmd=(vx=0.40 wz=-0.10) elapsed=36.5s plan[64pts 9.0m] (-0.60,-2.55)→(2.20,0.65) cpuFreq=1500MHz cpuT=76C cpu=87% mem=21%
[component_container_isolated-17] [INFO] [1783057399.619001038] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057399.635355624] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057399.649269710] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057399.649436002] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057399.661868213] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057400.413895934] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3044 Hz
[path_optimizer_node.py-22] [INFO] [1783057400.451079025] [path_optimizer_node]: Path optimised (60 pts, 5.7 ms): mean |kappa| 1.9900 -> 3.6407 (-82.9%), max |kappa| 13.2078 -> 18.9310 (-43.3%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057400.507894952] [speed_profile_node]: Plan received: 60 poses, mean|κ|=3.5237 m⁻¹, max|κ|=11.3340 m⁻¹, mean_v=0.247 m/s, min_v=0.150 m/s, max_v=0.498 m/s
[component_container_isolated-17] [INFO] [1783057400.523980038] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057401.078050349] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.27,-1.87) yaw=61deg cmd=(vx=0.40 wz=0.09) elapsed=38.5s plan[60pts 8.2m] (-0.30,-1.85)→(2.20,0.65) cpuFreq=1500MHz cpuT=76C cpu=60% mem=21%
[component_container_isolated-17] [INFO] [1783057401.619200115] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057401.630368826] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057401.639560327] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057401.639755119] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057401.649244663] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057402.403598261] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3105 Hz
[path_optimizer_node.py-22] [INFO] [1783057402.430919224] [path_optimizer_node]: Path optimised (58 pts, 5.6 ms): mean |kappa| 2.0390 -> 3.4151 (-67.5%), max |kappa| 13.2078 -> 14.4026 (-9.0%), max shift 0.080 m
[hobot_codec_republish-13] [WARN] [1783057402.452628311] [vlm_jpeg_encoder]: Sub imgRaw fps [13.36]
[speed_profile_node.py-23] [INFO] [1783057402.486770276] [speed_profile_node]: Plan received: 58 poses, mean|κ|=3.3017 m⁻¹, max|κ|=11.3340 m⁻¹, mean_v=0.242 m/s, min_v=0.150 m/s, max_v=0.496 m/s
[component_container_isolated-17] [INFO] [1783057402.523967866] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057403.074080135] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.12,-1.61) yaw=53deg cmd=(vx=0.40 wz=-0.26) elapsed=40.5s plan[58pts 7.9m] (-0.20,-1.65)→(2.20,0.65) cpuFreq=1500MHz cpuT=76C cpu=100% mem=21%
[hobot_codec_republish-13] [WARN] [1783057403.177498237] [vlm_jpeg_encoder]: Pub img fps [11.68]
[imu_madgwick_filter.py-6] [INFO] [1783057403.417633699] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3185 q_w=0.9693 angle=28.5deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057403.439692244] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1360 q_w=0.8473 angle=64.2deg beta=0.0330
[component_container_isolated-17] [INFO] [1783057403.619261570] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057403.633160072] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057403.643408032] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057403.643575657] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057403.655519160] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057404.398040881] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3421 Hz
[path_optimizer_node.py-22] [INFO] [1783057404.422298677] [path_optimizer_node]: Path optimised (48 pts, 4.9 ms): mean |kappa| 2.2456 -> 2.9408 (-31.0%), max |kappa| 13.2078 -> 13.3289 (-0.9%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057404.475013395] [speed_profile_node]: Plan received: 48 poses, mean|κ|=2.8251 m⁻¹, max|κ|=11.3339 m⁻¹, mean_v=0.268 m/s, min_v=0.150 m/s, max_v=0.485 m/s
[component_container_isolated-17] [INFO] [1783057404.523974196] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057405.073590799] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.21,-1.25) yaw=37deg cmd=(vx=0.40 wz=-0.90) elapsed=42.5s plan[48pts 6.7m] (0.30,-1.15)→(2.20,0.65) cpuFreq=1500MHz cpuT=76C cpu=87% mem=21%
[component_container_isolated-17] [INFO] [1783057405.619699317] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057405.636011987] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057405.645832697] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057405.645985489] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057405.655604949] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057406.389307545] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3531 Hz
[path_optimizer_node.py-22] [INFO] [1783057406.417305092] [path_optimizer_node]: Path optimised (46 pts, 5.2 ms): mean |kappa| 2.8849 -> 3.6811 (-27.6%), max |kappa| 13.2078 -> 13.3289 (-0.9%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057406.460227100] [speed_profile_node]: Plan received: 46 poses, mean|κ|=3.5533 m⁻¹, max|κ|=11.3342 m⁻¹, mean_v=0.234 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[component_container_isolated-17] [INFO] [1783057406.523975778] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057407.070276672] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.68,-1.09) yaw=-7deg cmd=(vx=0.20 wz=0.97) elapsed=44.5s plan[46pts 6.7m] (0.60,-1.05)→(2.20,0.65) cpuFreq=1500MHz cpuT=76C cpu=85% mem=21%
[component_container_isolated-17] [INFO] [1783057407.618953109] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057407.629091236] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057407.639635654] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057407.639768571] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057407.647573197] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[hobot_codec_republish-13] [WARN] [1783057408.184275340] [vlm_jpeg_encoder]: Sub imgRaw fps [14.93]
[component_container_isolated-17] [WARN] [1783057408.395410671] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3238 Hz
[path_optimizer_node.py-22] [INFO] [1783057408.430306511] [path_optimizer_node]: Path optimised (45 pts, 4.8 ms): mean |kappa| 2.5837 -> 3.7276 (-44.3%), max |kappa| 13.2078 -> 13.3286 (-0.9%), max shift 0.080 m
[component_container_isolated-17] [INFO] [1783057408.523963029] [controller_server]: Passing new path to controller.
[hobot_codec_republish-13] [WARN] [1783057408.678013766] [vlm_jpeg_encoder]: Pub img fps [13.64]
[speed_profile_node.py-23] [INFO] [1783057408.745084404] [speed_profile_node]: Plan received: 45 poses, mean|κ|=3.5915 m⁻¹, max|κ|=11.3344 m⁻¹, mean_v=0.231 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[competition_master_stage3.py-21] [INFO] [1783057409.086729218] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.77,-1.08) yaw=-16deg cmd=(vx=0.40 wz=0.39) elapsed=46.5s plan[45pts 6.4m] (0.90,-1.15)→(2.20,0.65) cpuFreq=1500MHz cpuT=76C cpu=100% mem=21%
[component_container_isolated-17] [INFO] [1783057409.619031111] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057409.632209030] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057409.644436240] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057409.644599365] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057409.652961159] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057410.395737007] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3322 Hz
[path_optimizer_node.py-22] [INFO] [1783057410.423862763] [path_optimizer_node]: Path optimised (45 pts, 7.3 ms): mean |kappa| 2.9610 -> 3.7298 (-26.0%), max |kappa| 13.2078 -> 13.3288 (-0.9%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057410.476289564] [speed_profile_node]: Plan received: 45 poses, mean|κ|=3.6500 m⁻¹, max|κ|=11.3341 m⁻¹, mean_v=0.238 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[component_container_isolated-17] [INFO] [1783057410.523967032] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057411.075096136] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.10,-1.09) yaw=8deg cmd=(vx=-0.24 wz=0.33) elapsed=48.5s plan[45pts 6.5m] (1.00,-1.15)→(2.20,0.65) cpuFreq=1500MHz cpuT=76C cpu=88% mem=21%
[component_container_isolated-17] [INFO] [1783057411.619085073] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057411.636904909] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057411.743992971] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057411.744255971] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057411.753791682] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057412.411625265] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3158 Hz
[path_optimizer_node.py-22] [INFO] [1783057412.415059891] [path_optimizer_node]: Path optimised (42 pts, 4.6 ms): mean |kappa| 2.5646 -> 3.1319 (-22.1%), max |kappa| 13.2078 -> 13.3289 (-0.9%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057412.455351273] [speed_profile_node]: Plan received: 42 poses, mean|κ|=2.9944 m⁻¹, max|κ|=11.3341 m⁻¹, mean_v=0.261 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[component_container_isolated-17] [INFO] [1783057412.523978203] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057413.074778891] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.06,-1.13) yaw=26deg cmd=(vx=0.30 wz=-0.87) elapsed=50.5s plan[42pts 6.0m] (1.10,-1.05)→(2.20,0.65) cpuFreq=1500MHz cpuT=76C cpu=100% mem=21%
[imu_madgwick_filter.py-6] [INFO] [1783057413.415790498] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3686 q_w=0.9944 angle=12.2deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057413.440156586] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1555 q_w=0.9007 angle=51.5deg beta=0.0330
[component_container_isolated-17] [INFO] [1783057413.618983953] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057413.629291622] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057413.638838499] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057413.638990207] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057413.654561377] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[hobot_codec_republish-13] [WARN] [1783057413.732899308] [vlm_jpeg_encoder]: Sub imgRaw fps [14.81]
[hobot_codec_republish-13] [WARN] [1783057413.736522601] [vlm_jpeg_encoder]: Pub img fps [14.83]
[component_container_isolated-17] [WARN] [1783057414.402033270] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3182 Hz
[path_optimizer_node.py-22] [INFO] [1783057414.434675692] [path_optimizer_node]: Path optimised (41 pts, 6.5 ms): mean |kappa| 2.5245 -> 3.1776 (-25.9%), max |kappa| 13.2078 -> 13.3287 (-0.9%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057414.468232199] [speed_profile_node]: Plan received: 41 poses, mean|κ|=3.0403 m⁻¹, max|κ|=11.3342 m⁻¹, mean_v=0.257 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[component_container_isolated-17] [INFO] [1783057414.523965335] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057414.856369940] [tracker_node]: Measurement timeout (3.0s), pausing tracking
[tracker_node-19] [INFO] [1783057415.057006728] [tracker_node]: Tracker initialized at (0.10, 0.00)
[competition_master_stage3.py-21] [INFO] [1783057415.075249982] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.35,-1.09) yaw=-17deg cmd=(vx=0.21 wz=-0.97) elapsed=52.5s plan[41pts 5.8m] (1.30,-1.05)→(2.20,0.65) cpuFreq=1500MHz cpuT=76C cpu=94% mem=21%
[tracker_node-19] [WARN] [1783057415.255853350] [tracker_node]: Measurement timeout (3.4s), pausing tracking
[tracker_node-19] [INFO] [1783057415.456432471] [tracker_node]: Tracker initialized at (0.10, 0.00)
[component_container_isolated-17] [INFO] [1783057415.619178836] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057415.637526423] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057415.647642550] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057415.647793550] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[tracker_node-19] [WARN] [1783057415.657143177] [tracker_node]: Measurement timeout (3.8s), pausing tracking
[component_container_isolated-17] [WARN] [1783057415.670184096] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [INFO] [1783057415.857064382] [tracker_node]: Tracker initialized at (0.10, 0.00)
[tracker_node-19] [WARN] [1783057416.056496128] [tracker_node]: Measurement timeout (4.2s), pausing tracking
[tracker_node-19] [INFO] [1783057416.256100000] [tracker_node]: Tracker initialized at (-0.01, 0.00)
[component_container_isolated-17] [WARN] [1783057416.394091068] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3555 Hz
[path_optimizer_node.py-22] [INFO] [1783057416.429450658] [path_optimizer_node]: Path optimised (42 pts, 5.8 ms): mean |kappa| 2.4060 -> 3.2319 (-34.3%), max |kappa| 12.7282 -> 18.2927 (-43.7%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057416.473768542] [speed_profile_node]: Plan received: 42 poses, mean|κ|=3.1603 m⁻¹, max|κ|=11.5263 m⁻¹, mean_v=0.265 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[component_container_isolated-17] [INFO] [1783057416.523974676] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057417.075262324] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.56,-1.27) yaw=-60deg cmd=(vx=-0.30 wz=-0.47) elapsed=54.5s plan[42pts 6.3m] (1.60,-1.25)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=87% mem=21%
[component_container_isolated-17] [INFO] [1783057417.619523179] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057417.639152808] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057417.648623935] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057417.648764476] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057417.666788396] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057418.389750078] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3514 Hz
[path_optimizer_node.py-22] [INFO] [1783057418.432237461] [path_optimizer_node]: Path optimised (39 pts, 6.6 ms): mean |kappa| 1.9612 -> 3.0769 (-56.9%), max |kappa| 12.0193 -> 22.7565 (-89.3%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057418.476988803] [speed_profile_node]: Plan received: 39 poses, mean|κ|=2.9293 m⁻¹, max|κ|=14.4415 m⁻¹, mean_v=0.306 m/s, min_v=0.150 m/s, max_v=0.495 m/s
[component_container_isolated-17] [INFO] [1783057418.525534520] [controller_server]: Passing new path to controller.
[hobot_codec_republish-13] [WARN] [1783057418.785981946] [vlm_jpeg_encoder]: Sub imgRaw fps [13.46]
[hobot_codec_republish-13] [WARN] [1783057418.788446738] [vlm_jpeg_encoder]: Pub img fps [13.46]
[competition_master_stage3.py-21] [INFO] [1783057419.078379544] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.48,-1.08) yaw=-79deg cmd=(vx=-0.30 wz=-0.16) elapsed=56.5s plan[39pts 5.8m] (1.50,-0.95)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=87% mem=21%
[tracker_node-19] [WARN] [1783057419.255997662] [tracker_node]: Measurement timeout (3.2s), pausing tracking
[tracker_node-19] [INFO] [1783057419.457626784] [tracker_node]: Tracker initialized at (-0.01, 0.00)
[component_container_isolated-17] [INFO] [1783057419.531645173] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057419.541553092] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057419.552717386] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057419.552860636] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057419.573152348] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [WARN] [1783057419.656689031] [tracker_node]: Measurement timeout (3.6s), pausing tracking
[tracker_node-19] [INFO] [1783057419.858924279] [tracker_node]: Tracker initialized at (-0.01, 0.00)
[component_container_isolated-17] [WARN] [1783057420.397002633] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2020 Hz
[path_optimizer_node.py-22] [INFO] [1783057420.444474517] [path_optimizer_node]: Path optimised (43 pts, 9.7 ms): mean |kappa| 2.4675 -> 3.7502 (-52.0%), max |kappa| 14.0941 -> 29.6818 (-110.6%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057420.486418692] [speed_profile_node]: Plan received: 43 poses, mean|κ|=3.7615 m⁻¹, max|κ|=16.2035 m⁻¹, mean_v=0.265 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[component_container_isolated-17] [INFO] [1783057420.523978658] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057421.078226849] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.43,-0.78) yaw=-84deg cmd=(vx=0.01 wz=0.14) elapsed=58.5s plan[43pts 6.2m] (1.50,-0.85)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=100% mem=21%
[component_container_isolated-17] [INFO] [1783057421.619023037] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057421.631537165] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057421.644650834] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057421.644838709] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057421.657512086] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057422.385912395] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-17] [WARN] [1783057422.386181103] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.90, -0.90)
[component_container_isolated-17] [WARN] [1783057422.386307978] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-17] [INFO] [1783057422.519054754] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057422.531147757] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057422.544238426] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057422.544413176] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [INFO] [1783057422.552805886] [behavior_server]: Running wait
[component_container_isolated-17] [WARN] [1783057422.556262678] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [INFO] [1783057422.556308845] [behavior_server]: wait completed successfully
[component_container_isolated-17] [INFO] [1783057422.819158313] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057422.825922439] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057422.840307317] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057422.840484900] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057422.852101694] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [WARN] [1783057423.056533776] [tracker_node]: Measurement timeout (3.1s), pausing tracking
[competition_master_stage3.py-21] [INFO] [1783057423.074978279] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.44,-0.77) yaw=-57deg cmd=(vx=-0.17 wz=-0.97) elapsed=60.5s plan[43pts 6.2m] (1.50,-0.85)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=85% mem=21%
[tracker_node-19] [INFO] [1783057423.256620565] [tracker_node]: Tracker initialized at (0.13, 0.00)
[component_container_isolated-17] [WARN] [1783057423.382808715] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-17] [WARN] [1783057423.383105506] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.90, -0.90)
[component_container_isolated-17] [WARN] [1783057423.383239340] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[imu_madgwick_filter.py-6] [INFO] [1783057423.415877763] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4166 q_w=0.8520 angle=63.2deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057423.439769559] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1752 q_w=0.9875 angle=18.1deg beta=0.0330
[tracker_node-19] [WARN] [1783057423.456983271] [tracker_node]: Measurement timeout (3.5s), pausing tracking
[component_container_isolated-17] [INFO] [1783057423.523985284] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-17] [INFO] [1783057423.524174784] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-17] [INFO] [1783057423.524941201] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-17] [INFO] [1783057423.545006121] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057423.563042667] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057423.564772750] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [INFO] [1783057423.566624542] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [WARN] [1783057423.579873128] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [INFO] [1783057423.590074630] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057423.595148131] [behavior_server]: Running wait
[component_container_isolated-17] [INFO] [1783057423.595427173] [behavior_server]: wait completed successfully
[component_container_isolated-17] [INFO] [1783057423.604694175] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057423.604862008] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057423.617743136] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [INFO] [1783057423.658016477] [tracker_node]: Tracker initialized at (0.13, 0.00)
[component_container_isolated-17] [INFO] [1783057423.820087092] [behavior_server]: Running backup
[component_container_isolated-17] [INFO] [1783057423.821063217] [behavior_server]: DriveOnHeading: no acceleration or deceleration limits set
[tracker_node-19] [WARN] [1783057423.862874142] [tracker_node]: Measurement timeout (3.9s), pausing tracking
[hobot_codec_republish-13] [WARN] [1783057423.931576405] [vlm_jpeg_encoder]: Sub imgRaw fps [12.44]
[hobot_codec_republish-13] [WARN] [1783057423.934577448] [vlm_jpeg_encoder]: Pub img fps [12.44]
[tracker_node-19] [INFO] [1783057424.062590056] [tracker_node]: Tracker initialized at (-0.05, 0.00)
[imu_madgwick_filter.py-4] [WARN] [1783057424.366450699] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1501s > 0.15s, capping
[competition_master_stage3.py-21] [INFO] [1783057425.069063837] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.44,-0.77) yaw=-57deg cmd=(vx=-0.12 wz=0.00) elapsed=62.5s plan[43pts 6.2m] (1.50,-0.85)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=75% mem=21%
[tracker_node-19] [WARN] [1783057427.058665812] [tracker_node]: Measurement timeout (3.1s), pausing tracking
[competition_master_stage3.py-21] [INFO] [1783057427.073539773] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.44,-0.77) yaw=-54deg cmd=(vx=-0.12 wz=0.00) elapsed=64.5s plan[43pts 6.2m] (1.50,-0.85)→(2.20,0.65) cpuFreq=1500MHz cpuT=76C cpu=87% mem=21%
[tracker_node-19] [INFO] [1783057427.260829185] [tracker_node]: Tracker initialized at (-0.05, 0.00)
[hobot_codec_republish-13] [WARN] [1783057428.970240565] [vlm_jpeg_encoder]: Sub imgRaw fps [13.70]
[hobot_codec_republish-13] [WARN] [1783057428.976737566] [vlm_jpeg_encoder]: Pub img fps [13.69]
[competition_master_stage3.py-21] [INFO] [1783057429.070574668] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.33,-0.61) yaw=-57deg cmd=(vx=-0.12 wz=0.00) elapsed=66.5s plan[43pts 6.2m] (1.50,-0.85)→(2.20,0.65) cpuFreq=1500MHz cpuT=76C cpu=88% mem=21%
[component_container_isolated-17] [WARN] [1783057430.821409266] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-17] [WARN] [1783057430.821581057] [behavior_server]: backup failed
[component_container_isolated-17] [WARN] [1783057430.821687724] [behavior_server]: [backup] [ActionServer] Aborting handle.
[competition_master_stage3.py-21] [INFO] [1783057431.070463190] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.21,-0.43) yaw=-59deg cmd=(vx=0.00 wz=0.00) elapsed=68.5s plan[43pts 6.2m] (1.50,-0.85)→(2.20,0.65) cpuFreq=1500MHz cpuT=76C cpu=90% mem=21%
[component_container_isolated-17] [INFO] [1783057431.121661909] [behavior_server]: Running wait
[imu_madgwick_filter.py-4] [WARN] [1783057431.565247830] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1501s > 0.15s, capping
[competition_master_stage3.py-21] [INFO] [1783057433.074363715] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.08,-0.24) yaw=-62deg cmd=(vx=0.00 wz=0.00) elapsed=70.5s plan[43pts 6.2m] (1.50,-0.85)→(2.20,0.65) cpuFreq=1500MHz cpuT=76C cpu=85% mem=21%
[imu_madgwick_filter.py-6] [INFO] [1783057433.416627242] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4670 q_w=0.7834 angle=76.9deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057433.439470955] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1945 q_w=0.9722 angle=27.1deg beta=0.0330
[hobot_codec_republish-13] [WARN] [1783057434.014661779] [vlm_jpeg_encoder]: Sub imgRaw fps [13.88]
[hobot_codec_republish-13] [WARN] [1783057434.021982572] [vlm_jpeg_encoder]: Pub img fps [13.88]
[component_container_isolated-17] [INFO] [1783057434.122569134] [behavior_server]: wait completed successfully
[component_container_isolated-17] [INFO] [1783057434.419224443] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057434.430068445] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057434.442494364] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057434.442628073] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057434.455977701] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057435.073078783] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.08,-0.24) yaw=-62deg cmd=(vx=0.00 wz=0.00) elapsed=72.5s plan[43pts 6.2m] (1.50,-0.85)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=87% mem=21%
[component_container_isolated-17] [WARN] [1783057435.413458685] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.0347 Hz
[path_optimizer_node.py-22] [INFO] [1783057435.475628280] [path_optimizer_node]: Path optimised (44 pts, 16.4 ms): mean |kappa| 1.6597 -> 2.3996 (-44.6%), max |kappa| 13.1477 -> 12.2759 (6.6%), max shift 0.080 m
[component_container_isolated-17] [INFO] [1783057435.520547581] [controller_server]: Received a goal, begin computing control effort.
[speed_profile_node.py-23] [INFO] [1783057435.520578206] [speed_profile_node]: Plan received: 44 poses, mean|κ|=2.2937 m⁻¹, max|κ|=11.1233 m⁻¹, mean_v=0.327 m/s, min_v=0.150 m/s, max_v=0.496 m/s
[component_container_isolated-17] [INFO] [1783057436.618988178] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057436.633327264] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057436.646931142] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057436.647275725] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057436.656404810] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057437.079701104] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.08,-0.24) yaw=-62deg cmd=(vx=0.40 wz=0.12) elapsed=74.5s plan[44pts 6.4m] (1.10,-0.25)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=100% mem=21%
[component_container_isolated-17] [WARN] [1783057437.425580757] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3042 Hz
[path_optimizer_node.py-22] [INFO] [1783057437.455700263] [path_optimizer_node]: Path optimised (42 pts, 7.0 ms): mean |kappa| 1.7186 -> 2.8262 (-64.4%), max |kappa| 13.7223 -> 13.8513 (-0.9%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057437.494787146] [speed_profile_node]: Plan received: 42 poses, mean|κ|=2.6936 m⁻¹, max|κ|=11.7092 m⁻¹, mean_v=0.302 m/s, min_v=0.150 m/s, max_v=0.496 m/s
[component_container_isolated-17] [INFO] [1783057437.629073548] [controller_server]: Passing new path to controller.
[component_container_isolated-17] [INFO] [1783057438.719063811] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057438.730882396] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057438.749674900] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057438.750039734] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057438.766918362] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[hobot_codec_republish-13] [WARN] [1783057439.055132087] [vlm_jpeg_encoder]: Sub imgRaw fps [12.70]
[hobot_codec_republish-13] [WARN] [1783057439.057933171] [vlm_jpeg_encoder]: Pub img fps [12.71]
[competition_master_stage3.py-21] [INFO] [1783057439.074489674] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.45,-1.11) yaw=-50deg cmd=(vx=0.13 wz=-0.18) elapsed=76.5s plan[42pts 5.8m] (1.20,-0.65)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=88% mem=21%
[component_container_isolated-17] [WARN] [1783057439.399366782] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.5383 Hz
[path_optimizer_node.py-22] [INFO] [1783057439.427499788] [path_optimizer_node]: Path optimised (37 pts, 5.3 ms): mean |kappa| 2.2662 -> 2.9687 (-31.0%), max |kappa| 13.1709 -> 13.8029 (-4.8%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057439.463908337] [speed_profile_node]: Plan received: 37 poses, mean|κ|=2.8181 m⁻¹, max|κ|=11.5242 m⁻¹, mean_v=0.294 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[component_container_isolated-17] [INFO] [1783057439.529089767] [controller_server]: Passing new path to controller.
[component_container_isolated-17] [INFO] [1783057440.619133988] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057440.634985575] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057440.641910785] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057440.642078201] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057440.651773203] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057441.075051540] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.65,-1.30) yaw=-55deg cmd=(vx=0.40 wz=0.16) elapsed=78.5s plan[37pts 5.5m] (1.50,-1.25)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=77% mem=21%
[component_container_isolated-17] [WARN] [1783057441.389742895] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3383 Hz
[imu_madgwick_filter.py-4] [WARN] [1783057441.413769442] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1501s > 0.15s, capping
[path_optimizer_node.py-22] [INFO] [1783057441.417638859] [path_optimizer_node]: Path optimised (33 pts, 6.1 ms): mean |kappa| 2.2766 -> 2.7220 (-19.6%), max |kappa| 12.7282 -> 12.2114 (4.1%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057441.462701202] [speed_profile_node]: Plan received: 33 poses, mean|κ|=2.5675 m⁻¹, max|κ|=10.9598 m⁻¹, mean_v=0.306 m/s, min_v=0.150 m/s, max_v=0.479 m/s
[component_container_isolated-17] [INFO] [1783057441.529083299] [controller_server]: Passing new path to controller.
[component_container_isolated-17] [INFO] [1783057442.619137938] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057442.633314149] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057442.645834944] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057442.646009235] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057442.666877490] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057443.070410822] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.97,-1.88) yaw=-47deg cmd=(vx=0.13 wz=-0.10) elapsed=80.5s plan[33pts 4.9m] (1.70,-1.55)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=88% mem=21%
[component_container_isolated-17] [WARN] [1783057443.385636220] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-17] [WARN] [1783057443.385862637] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.90, -0.90)
[component_container_isolated-17] [WARN] [1783057443.385989095] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[imu_madgwick_filter.py-6] [INFO] [1783057443.416699851] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5163 q_w=0.9180 angle=46.7deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057443.440046815] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2138 q_w=0.9981 angle=7.0deg beta=0.0330
[tracker_node-19] [WARN] [1783057443.456704735] [tracker_node]: Measurement timeout (3.1s), pausing tracking
[component_container_isolated-17] [INFO] [1783057443.519268123] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057443.533878376] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057443.547957253] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057443.548274587] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [INFO] [1783057443.560552381] [behavior_server]: Running wait
[component_container_isolated-17] [INFO] [1783057443.560998089] [behavior_server]: wait completed successfully
[component_container_isolated-17] [WARN] [1783057443.561571340] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [INFO] [1783057443.656166026] [tracker_node]: Tracker initialized at (0.01, 0.00)
[component_container_isolated-17] [INFO] [1783057443.819134517] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057443.832315645] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057443.851060441] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057443.851257774] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057443.864807985] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [WARN] [1783057443.865560027] [tracker_node]: Measurement timeout (3.5s), pausing tracking
[tracker_node-19] [INFO] [1783057444.058640358] [tracker_node]: Tracker initialized at (0.01, 0.00)
[hobot_codec_republish-13] [WARN] [1783057444.099148533] [vlm_jpeg_encoder]: Sub imgRaw fps [13.29]
[hobot_codec_republish-13] [WARN] [1783057444.105045784] [vlm_jpeg_encoder]: Pub img fps [13.28]
[tracker_node-19] [WARN] [1783057444.256374399] [tracker_node]: Measurement timeout (3.9s), pausing tracking
[component_container_isolated-17] [WARN] [1783057444.393471385] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.8500 Hz
[path_optimizer_node.py-22] [INFO] [1783057444.425359433] [path_optimizer_node]: Path optimised (34 pts, 9.1 ms): mean |kappa| 3.3220 -> 4.0578 (-22.1%), max |kappa| 15.1323 -> 16.0294 (-5.9%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057444.455660648] [speed_profile_node]: Plan received: 34 poses, mean|κ|=3.8375 m⁻¹, max|κ|=13.8852 m⁻¹, mean_v=0.269 m/s, min_v=0.150 m/s, max_v=0.479 m/s
[tracker_node-19] [INFO] [1783057444.457004732] [tracker_node]: Tracker initialized at (0.01, 0.00)
[component_container_isolated-17] [INFO] [1783057444.529080330] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057444.658444565] [tracker_node]: Measurement timeout (4.3s), pausing tracking
[tracker_node-19] [INFO] [1783057444.862375232] [tracker_node]: Tracker initialized at (0.06, 0.00)
[competition_master_stage3.py-21] [INFO] [1783057445.070241941] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.21,-1.97) yaw=-37deg cmd=(vx=0.40 wz=-0.70) elapsed=82.5s plan[34pts 5.0m] (2.20,-2.05)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=87% mem=21%
[component_container_isolated-17] [INFO] [1783057445.619067304] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057445.630605015] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057445.645209893] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057445.645376726] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057445.664525230] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057446.381694086] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-17] [WARN] [1783057446.381962503] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.90, -0.90)
[component_container_isolated-17] [WARN] [1783057446.382111419] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-17] [INFO] [1783057446.519114114] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057446.532103825] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057446.540765327] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057446.540915744] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [INFO] [1783057446.541499952] [behavior_server]: Running wait
[component_container_isolated-17] [INFO] [1783057446.541798244] [behavior_server]: wait completed successfully
[component_container_isolated-17] [WARN] [1783057446.550505954] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [INFO] [1783057446.819407510] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057446.844397807] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057446.853333725] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057446.853500433] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057446.863357894] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057447.071223312] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.38,-2.30) yaw=-65deg cmd=(vx=0.31 wz=0.41) elapsed=84.5s plan[34pts 5.0m] (2.20,-2.05)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=87% mem=21%
[component_container_isolated-17] [WARN] [1783057447.396673171] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.8816 Hz
[path_optimizer_node.py-22] [INFO] [1783057447.431505595] [path_optimizer_node]: Path optimised (32 pts, 4.5 ms): mean |kappa| 2.7636 -> 3.3139 (-19.9%), max |kappa| 15.0174 -> 22.6157 (-50.6%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057447.471736478] [speed_profile_node]: Plan received: 32 poses, mean|κ|=3.2150 m⁻¹, max|κ|=12.6043 m⁻¹, mean_v=0.292 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[component_container_isolated-17] [INFO] [1783057447.529085240] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057447.858017933] [tracker_node]: Measurement timeout (3.1s), pausing tracking
[tracker_node-19] [INFO] [1783057448.057283266] [tracker_node]: Tracker initialized at (0.06, 0.00)
[tracker_node-19] [WARN] [1783057448.256833682] [tracker_node]: Measurement timeout (3.5s), pausing tracking
[tracker_node-19] [INFO] [1783057448.458114224] [tracker_node]: Tracker initialized at (0.06, 0.00)
[component_container_isolated-17] [INFO] [1783057448.620137841] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057448.645200762] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[tracker_node-19] [WARN] [1783057448.666119517] [tracker_node]: Measurement timeout (3.9s), pausing tracking
[component_container_isolated-17] [INFO] [1783057448.666593100] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057448.666735767] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057448.688706688] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [INFO] [1783057448.860463390] [tracker_node]: Tracker initialized at (0.06, 0.00)
[tracker_node-19] [WARN] [1783057449.057345765] [tracker_node]: Measurement timeout (4.3s), pausing tracking
[competition_master_stage3.py-21] [INFO] [1783057449.082187436] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.46,-2.44) yaw=-55deg cmd=(vx=-0.03 wz=-0.30) elapsed=86.5s plan[32pts 4.3m] (2.50,-2.35)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=77% mem=21%
[hobot_codec_republish-13] [WARN] [1783057449.119216027] [vlm_jpeg_encoder]: Sub imgRaw fps [11.95]
[hobot_codec_republish-13] [WARN] [1783057449.123890028] [vlm_jpeg_encoder]: Pub img fps [11.96]
[tracker_node-19] [INFO] [1783057449.257972556] [tracker_node]: Tracker initialized at (0.06, 0.00)
[component_container_isolated-17] [WARN] [1783057449.390911292] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3931 Hz
[path_optimizer_node.py-22] [INFO] [1783057449.438626260] [path_optimizer_node]: Path optimised (32 pts, 15.7 ms): mean |kappa| 2.7279 -> 3.5778 (-31.2%), max |kappa| 14.0358 -> 22.3983 (-59.6%), max shift 0.080 m
[tracker_node-19] [WARN] [1783057449.457708473] [tracker_node]: Measurement timeout (4.7s), pausing tracking
[speed_profile_node.py-23] [INFO] [1783057449.502422274] [speed_profile_node]: Plan received: 32 poses, mean|κ|=3.4524 m⁻¹, max|κ|=12.2840 m⁻¹, mean_v=0.269 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[component_container_isolated-17] [INFO] [1783057449.529180654] [controller_server]: Passing new path to controller.
[tracker_node-19] [INFO] [1783057449.656947556] [tracker_node]: Tracker initialized at (0.06, 0.00)
[component_container_isolated-17] [INFO] [1783057450.619025631] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057450.633547509] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057450.645249595] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057450.645538595] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057450.658350014] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057451.074370559] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.34,-2.16) yaw=-72deg cmd=(vx=-0.30 wz=0.97) elapsed=88.5s plan[32pts 4.3m] (2.30,-2.15)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=100% mem=21%
[component_container_isolated-17] [WARN] [1783057451.398605877] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3284 Hz
[path_optimizer_node.py-22] [INFO] [1783057451.431928134] [path_optimizer_node]: Path optimised (37 pts, 5.3 ms): mean |kappa| 2.8143 -> 3.7234 (-32.3%), max |kappa| 12.7282 -> 13.8778 (-9.0%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057451.463188973] [speed_profile_node]: Plan received: 37 poses, mean|κ|=3.6356 m⁻¹, max|κ|=11.4381 m⁻¹, mean_v=0.250 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[component_container_isolated-17] [INFO] [1783057451.529083487] [controller_server]: Passing new path to controller.
[component_container_isolated-17] [INFO] [1783057452.619060465] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057452.638616677] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057452.650350971] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057452.650507471] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057452.686329896] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [WARN] [1783057452.855667639] [tracker_node]: Measurement timeout (3.1s), pausing tracking
[tracker_node-19] [INFO] [1783057453.056085015] [tracker_node]: Tracker initialized at (-0.09, 0.00)
[competition_master_stage3.py-21] [INFO] [1783057453.076347894] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.06,-1.88) yaw=-12deg cmd=(vx=0.22 wz=0.34) elapsed=90.5s plan[37pts 5.4m] (2.20,-2.05)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=100% mem=21%
[tracker_node-19] [WARN] [1783057453.255587806] [tracker_node]: Measurement timeout (3.5s), pausing tracking
[imu_madgwick_filter.py-4] [INFO] [1783057453.439785887] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2331 q_w=0.9088 angle=49.3deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1783057453.439995928] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5636 q_w=0.9928 angle=13.7deg beta=0.0030
[component_container_isolated-17] [WARN] [1783057453.444282929] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2614 Hz
[path_optimizer_node.py-22] [INFO] [1783057453.454550223] [path_optimizer_node]: Path optimised (33 pts, 5.2 ms): mean |kappa| 2.7434 -> 3.6543 (-33.2%), max |kappa| 12.7282 -> 20.2172 (-58.8%), max shift 0.080 m
[tracker_node-19] [INFO] [1783057453.457204724] [tracker_node]: Tracker initialized at (-0.09, 0.00)
[speed_profile_node.py-23] [INFO] [1783057453.503147442] [speed_profile_node]: Plan received: 33 poses, mean|κ|=3.6164 m⁻¹, max|κ|=11.9505 m⁻¹, mean_v=0.270 m/s, min_v=0.150 m/s, max_v=0.479 m/s
[component_container_isolated-17] [INFO] [1783057453.629080760] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057453.656250724] [tracker_node]: Measurement timeout (3.9s), pausing tracking
[tracker_node-19] [INFO] [1783057453.856819516] [tracker_node]: Tracker initialized at (-0.09, 0.00)
[tracker_node-19] [WARN] [1783057454.057691891] [tracker_node]: Measurement timeout (4.3s), pausing tracking
[hobot_codec_republish-13] [WARN] [1783057454.128189656] [vlm_jpeg_encoder]: Sub imgRaw fps [12.78]
[hobot_codec_republish-13] [WARN] [1783057454.131718657] [vlm_jpeg_encoder]: Pub img fps [12.78]
[tracker_node-19] [INFO] [1783057454.257465100] [tracker_node]: Tracker initialized at (-0.09, 0.00)
[tracker_node-19] [WARN] [1783057454.459095850] [tracker_node]: Measurement timeout (4.7s), pausing tracking
[tracker_node-19] [INFO] [1783057454.656117142] [tracker_node]: Tracker initialized at (-0.09, 0.00)
[component_container_isolated-17] [INFO] [1783057454.719007738] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057454.727048698] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057454.746815077] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057454.746986244] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057454.760077414] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [WARN] [1783057454.856506350] [tracker_node]: Measurement timeout (5.1s), pausing tracking
[tracker_node-19] [INFO] [1783057455.056871809] [tracker_node]: Tracker initialized at (-0.09, 0.00)
[competition_master_stage3.py-21] [INFO] [1783057455.076949022] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.00,-1.87) yaw=-9deg cmd=(vx=-0.30 wz=-0.96) elapsed=92.5s plan[33pts 4.8m] (2.00,-1.85)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=90% mem=21%
[tracker_node-19] [WARN] [1783057455.256568851] [tracker_node]: Measurement timeout (5.5s), pausing tracking
[component_container_isolated-17] [WARN] [1783057455.395918464] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.5724 Hz
[path_optimizer_node.py-22] [INFO] [1783057455.409837467] [path_optimizer_node]: Path optimised (32 pts, 5.4 ms): mean |kappa| 2.4984 -> 3.4913 (-39.7%), max |kappa| 12.9250 -> 25.9032 (-100.4%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057455.448263058] [speed_profile_node]: Plan received: 32 poses, mean|κ|=3.2886 m⁻¹, max|κ|=15.4062 m⁻¹, mean_v=0.306 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[tracker_node-19] [INFO] [1783057455.457701394] [tracker_node]: Tracker initialized at (-0.09, 0.00)
[component_container_isolated-17] [INFO] [1783057455.529104617] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057455.656478519] [tracker_node]: Measurement timeout (5.9s), pausing tracking
[tracker_node-19] [INFO] [1783057455.856112477] [tracker_node]: Tracker initialized at (-0.09, 0.00)
[tracker_node-19] [WARN] [1783057456.056998978] [tracker_node]: Measurement timeout (6.3s), pausing tracking
[tracker_node-19] [INFO] [1783057456.257483270] [tracker_node]: Tracker initialized at (-0.09, 0.00)
[tracker_node-19] [WARN] [1783057456.456269312] [tracker_node]: Measurement timeout (6.7s), pausing tracking
[component_container_isolated-17] [INFO] [1783057456.618995138] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057456.632662058] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057456.640843809] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057456.641066476] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[tracker_node-19] [INFO] [1783057456.657186188] [tracker_node]: Tracker initialized at (-0.09, 0.00)
[component_container_isolated-17] [WARN] [1783057456.657392063] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [WARN] [1783057456.865588565] [tracker_node]: Measurement timeout (7.1s), pausing tracking
[tracker_node-19] [INFO] [1783057457.056292605] [tracker_node]: Tracker initialized at (-0.09, 0.00)
[competition_master_stage3.py-21] [INFO] [1783057457.075845276] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.80,-1.82) yaw=-34deg cmd=(vx=0.40 wz=0.16) elapsed=94.5s plan[32pts 4.6m] (1.90,-1.85)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=93% mem=21%
[tracker_node-19] [WARN] [1783057457.261581940] [tracker_node]: Measurement timeout (7.5s), pausing tracking
[component_container_isolated-17] [WARN] [1783057457.388860051] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-17] [WARN] [1783057457.389109217] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.90, -0.90)
[component_container_isolated-17] [WARN] [1783057457.389212967] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[tracker_node-19] [INFO] [1783057457.457450273] [tracker_node]: Tracker initialized at (-0.09, 0.00)
[component_container_isolated-17] [INFO] [1783057457.527210288] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057457.536363207] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057457.551207418] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057457.551383252] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [INFO] [1783057457.551393127] [behavior_server]: Running wait
[component_container_isolated-17] [INFO] [1783057457.551838043] [behavior_server]: wait completed successfully
[component_container_isolated-17] [WARN] [1783057457.565458005] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [WARN] [1783057457.657339066] [tracker_node]: Measurement timeout (7.9s), pausing tracking
[component_container_isolated-17] [INFO] [1783057457.819317517] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057457.832296311] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057457.845266689] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057457.845411897] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[tracker_node-19] [INFO] [1783057457.857020316] [tracker_node]: Tracker initialized at (-0.09, 0.00)
[component_container_isolated-17] [WARN] [1783057457.857957983] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057458.392782680] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.8281 Hz
[path_optimizer_node.py-22] [INFO] [1783057458.413977517] [path_optimizer_node]: Path optimised (27 pts, 6.2 ms): mean |kappa| 2.8450 -> 3.2877 (-15.6%), max |kappa| 12.7282 -> 13.1772 (-3.5%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057458.449127691] [speed_profile_node]: Plan received: 27 poses, mean|κ|=3.0723 m⁻¹, max|κ|=11.2715 m⁻¹, mean_v=0.296 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[component_container_isolated-17] [INFO] [1783057458.529072917] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057459.072513782] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.46,-2.04) yaw=-12deg cmd=(vx=0.28 wz=0.90) elapsed=96.5s plan[27pts 3.9m] (2.50,-2.05)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=87% mem=21%
[hobot_codec_republish-13] [WARN] [1783057459.176670762] [vlm_jpeg_encoder]: Sub imgRaw fps [13.27]
[hobot_codec_republish-13] [WARN] [1783057459.181355805] [vlm_jpeg_encoder]: Pub img fps [13.27]
[component_container_isolated-17] [INFO] [1783057459.619137856] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057459.635576401] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057459.643313236] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057459.643679736] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057459.650942655] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057460.394401688] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3409 Hz
[path_optimizer_node.py-22] [INFO] [1783057460.430843904] [path_optimizer_node]: Path optimised (27 pts, 4.0 ms): mean |kappa| 3.0246 -> 4.1097 (-35.9%), max |kappa| 12.9667 -> 18.5036 (-42.7%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057460.464046702] [speed_profile_node]: Plan received: 27 poses, mean|κ|=3.8357 m⁻¹, max|κ|=11.6761 m⁻¹, mean_v=0.296 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[component_container_isolated-17] [INFO] [1783057460.529124091] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057461.056664453] [tracker_node]: Measurement timeout (3.0s), pausing tracking
[competition_master_stage3.py-21] [INFO] [1783057461.072805207] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.77,-2.05) yaw=12deg cmd=(vx=0.40 wz=0.57) elapsed=98.5s plan[27pts 3.8m] (2.90,-2.05)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=75% mem=21%
[tracker_node-19] [INFO] [1783057461.255940537] [tracker_node]: Tracker initialized at (-0.22, 0.00)
[tracker_node-19] [WARN] [1783057461.456658914] [tracker_node]: Measurement timeout (3.4s), pausing tracking
[component_container_isolated-17] [INFO] [1783057461.619173907] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057461.640872744] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[tracker_node-19] [INFO] [1783057461.657405540] [tracker_node]: Tracker initialized at (-0.22, 0.00)
[component_container_isolated-17] [INFO] [1783057461.657872248] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057461.658019498] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057461.675453835] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [WARN] [1783057461.856183874] [tracker_node]: Measurement timeout (3.8s), pausing tracking
[tracker_node-19] [INFO] [1783057462.055866708] [tracker_node]: Tracker initialized at (-0.22, 0.00)
[tracker_node-19] [WARN] [1783057462.256273417] [tracker_node]: Measurement timeout (4.2s), pausing tracking
[component_container_isolated-17] [WARN] [1783057462.397175156] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3799 Hz
[path_optimizer_node.py-22] [INFO] [1783057462.430419871] [path_optimizer_node]: Path optimised (25 pts, 17.3 ms): mean |kappa| 2.9494 -> 4.0619 (-37.7%), max |kappa| 12.7663 -> 15.5980 (-22.2%), max shift 0.080 m
[tracker_node-19] [INFO] [1783057462.456585377] [tracker_node]: Tracker initialized at (-0.22, 0.00)
[speed_profile_node.py-23] [INFO] [1783057462.468164171] [speed_profile_node]: Plan received: 25 poses, mean|κ|=3.7934 m⁻¹, max|κ|=12.1373 m⁻¹, mean_v=0.281 m/s, min_v=0.150 m/s, max_v=0.478 m/s
[component_container_isolated-17] [INFO] [1783057462.529257309] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057462.657326961] [tracker_node]: Measurement timeout (4.6s), pausing tracking
[tracker_node-19] [INFO] [1783057462.858595629] [tracker_node]: Tracker initialized at (-0.05, 0.00)
[competition_master_stage3.py-21] [INFO] [1783057463.075326009] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.14,-1.78) yaw=55deg cmd=(vx=0.28 wz=0.97) elapsed=100.5s plan[25pts 3.3m] (3.10,-1.85)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=71% mem=21%
[imu_madgwick_filter.py-6] [INFO] [1783057463.416286749] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=6118 q_w=0.8004 angle=73.7deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057463.439402795] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2525 q_w=0.3438 angle=139.8deg beta=0.0330
[component_container_isolated-17] [INFO] [1783057463.619153625] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057463.630397086] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057463.646843798] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057463.647054590] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057463.667840136] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[hobot_codec_republish-13] [WARN] [1783057464.242666425] [vlm_jpeg_encoder]: Sub imgRaw fps [13.03]
[hobot_codec_republish-13] [WARN] [1783057464.246141010] [vlm_jpeg_encoder]: Pub img fps [13.03]
[component_container_isolated-17] [WARN] [1783057464.387414373] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3394 Hz
[path_optimizer_node.py-22] [INFO] [1783057464.411999837] [path_optimizer_node]: Path optimised (22 pts, 6.7 ms): mean |kappa| 2.8970 -> 4.5793 (-58.1%), max |kappa| 13.9459 -> 19.5910 (-40.5%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057464.450574553] [speed_profile_node]: Plan received: 22 poses, mean|κ|=4.3215 m⁻¹, max|κ|=11.5821 m⁻¹, mean_v=0.243 m/s, min_v=0.150 m/s, max_v=0.473 m/s
[component_container_isolated-17] [INFO] [1783057464.529186154] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057465.071627312] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.21,-1.34) yaw=99deg cmd=(vx=0.40 wz=0.39) elapsed=102.5s plan[22pts 3.0m] (3.20,-1.35)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=88% mem=21%
[component_container_isolated-17] [INFO] [1783057465.631177348] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057465.663385314] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057465.693040778] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057465.693227987] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057465.707913907] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [WARN] [1783057465.856082355] [tracker_node]: Measurement timeout (3.2s), pausing tracking
[tracker_node-19] [INFO] [1783057466.056274565] [tracker_node]: Tracker initialized at (-0.05, 0.00)
[tracker_node-19] [WARN] [1783057466.256915316] [tracker_node]: Measurement timeout (3.6s), pausing tracking
[component_container_isolated-17] [WARN] [1783057466.386788469] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.5017 Hz
[path_optimizer_node.py-22] [INFO] [1783057466.403037014] [path_optimizer_node]: Path optimised (21 pts, 3.6 ms): mean |kappa| 3.6285 -> 5.2584 (-44.9%), max |kappa| 13.3223 -> 12.7495 (4.3%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057466.425604811] [speed_profile_node]: Plan received: 21 poses, mean|κ|=4.9918 m⁻¹, max|κ|=10.8523 m⁻¹, mean_v=0.189 m/s, min_v=0.150 m/s, max_v=0.400 m/s
[tracker_node-19] [INFO] [1783057466.456371693] [tracker_node]: Tracker initialized at (-0.05, 0.00)
[component_container_isolated-17] [INFO] [1783057466.529089083] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057466.661779028] [tracker_node]: Measurement timeout (4.0s), pausing tracking
[tracker_node-19] [INFO] [1783057466.856476445] [tracker_node]: Tracker initialized at (-0.05, 0.00)
[tracker_node-19] [WARN] [1783057467.055715863] [tracker_node]: Measurement timeout (4.4s), pausing tracking
[competition_master_stage3.py-21] [INFO] [1783057467.082229911] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.06,-1.01) yaw=123deg cmd=(vx=0.17 wz=-1.69) elapsed=104.5s plan[21pts 2.7m] (3.10,-1.05)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=83% mem=21%
[tracker_node-19] [INFO] [1783057467.256396323] [tracker_node]: Tracker initialized at (-0.05, 0.00)
[tracker_node-19] [WARN] [1783057467.456263283] [tracker_node]: Measurement timeout (4.8s), pausing tracking
[component_container_isolated-17] [INFO] [1783057467.619096235] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057467.632264071] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057467.641812865] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057467.641973365] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057467.654193326] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [INFO] [1783057467.656714451] [tracker_node]: Tracker initialized at (-0.05, 0.00)
[tracker_node-19] [WARN] [1783057467.857816620] [tracker_node]: Measurement timeout (5.2s), pausing tracking
[tracker_node-19] [INFO] [1783057468.056570204] [tracker_node]: Tracker initialized at (-0.05, 0.00)
[tracker_node-19] [WARN] [1783057468.257060289] [tracker_node]: Measurement timeout (5.6s), pausing tracking
[component_container_isolated-17] [WARN] [1783057468.384322317] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3647 Hz
[path_optimizer_node.py-22] [INFO] [1783057468.397911111] [path_optimizer_node]: Path optimised (13 pts, 2.8 ms): mean |kappa| 1.6561 -> 0.2919 (82.4%), max |kappa| 12.0427 -> 0.9965 (91.7%), max shift 0.074 m
[speed_profile_node.py-23] [INFO] [1783057468.425974159] [speed_profile_node]: Plan received: 13 poses, mean|κ|=0.2788 m⁻¹, max|κ|=0.6247 m⁻¹, mean_v=0.459 m/s, min_v=0.399 m/s, max_v=0.492 m/s
[tracker_node-19] [INFO] [1783057468.457037166] [tracker_node]: Tracker initialized at (-0.05, 0.00)
[component_container_isolated-17] [INFO] [1783057468.529121265] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057468.656221417] [tracker_node]: Measurement timeout (6.0s), pausing tracking
[tracker_node-19] [INFO] [1783057468.856747044] [tracker_node]: Tracker initialized at (-0.05, 0.00)
[tracker_node-19] [WARN] [1783057469.056997670] [tracker_node]: Measurement timeout (6.4s), pausing tracking
[competition_master_stage3.py-21] [INFO] [1783057469.075905591] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.01,-1.00) yaw=117deg cmd=(vx=0.40 wz=0.12) elapsed=106.5s plan[13pts 1.9m] (3.00,-0.95)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=100% mem=21%
[hobot_codec_republish-13] [WARN] [1783057469.247837128] [vlm_jpeg_encoder]: Sub imgRaw fps [13.39]
[hobot_codec_republish-13] [WARN] [1783057469.251455463] [vlm_jpeg_encoder]: Pub img fps [13.39]
[tracker_node-19] [INFO] [1783057469.260500340] [tracker_node]: Tracker initialized at (-0.05, 0.00)
[tracker_node-19] [WARN] [1783057469.455831549] [tracker_node]: Measurement timeout (6.8s), pausing tracking
[component_container_isolated-17] [INFO] [1783057469.620420084] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057469.632325378] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[tracker_node-19] [INFO] [1783057469.656744925] [tracker_node]: Tracker initialized at (-0.05, 0.00)
[component_container_isolated-17] [INFO] [1783057469.658735592] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057469.658881259] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057469.667162178] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057470.385977417] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4036 Hz
[path_optimizer_node.py-22] [INFO] [1783057470.404858004] [path_optimizer_node]: Path optimised (14 pts, 4.0 ms): mean |kappa| 3.0330 -> 2.4772 (18.3%), max |kappa| 11.9226 -> 15.9710 (-34.0%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057470.433304385] [speed_profile_node]: Plan received: 14 poses, mean|κ|=2.6034 m⁻¹, max|κ|=7.7121 m⁻¹, mean_v=0.299 m/s, min_v=0.150 m/s, max_v=0.438 m/s
[component_container_isolated-17] [INFO] [1783057470.529076906] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057471.070528857] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.77,-0.59) yaw=109deg cmd=(vx=-0.30 wz=0.58) elapsed=108.5s plan[14pts 2.1m] (2.90,-0.75)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=88% mem=21%
[component_container_isolated-17] [INFO] [1783057471.619476101] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057471.639782981] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057471.652562734] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057471.652719900] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057471.667852737] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057472.385880102] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3838 Hz
[path_optimizer_node.py-22] [INFO] [1783057472.403002272] [path_optimizer_node]: Path optimised (11 pts, 3.9 ms): mean |kappa| 1.5155 -> 0.9135 (39.7%), max |kappa| 3.3333 -> 1.6511 (50.5%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057472.438240405] [speed_profile_node]: Plan received: 11 poses, mean|κ|=0.8301 m⁻¹, max|κ|=1.0695 m⁻¹, mean_v=0.366 m/s, min_v=0.330 m/s, max_v=0.425 m/s
[component_container_isolated-17] [INFO] [1783057472.529082508] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057473.073685251] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.76,-0.60) yaw=125deg cmd=(vx=0.40 wz=-0.69) elapsed=110.5s plan[11pts 1.5m] (2.80,-0.65)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=77% mem=21%
[imu_madgwick_filter.py-6] [INFO] [1783057473.416344785] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=6597 q_w=0.4738 angle=123.4deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057473.439695998] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2717 q_w=-0.1179 angle=193.5deg beta=0.0330
[component_container_isolated-17] [INFO] [1783057473.619236162] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057473.634120791] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057473.643672001] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057473.644287126] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057473.655419504] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[hobot_codec_republish-13] [WARN] [1783057474.275012722] [vlm_jpeg_encoder]: Sub imgRaw fps [11.94]
[hobot_codec_republish-13] [WARN] [1783057474.280651848] [vlm_jpeg_encoder]: Pub img fps [11.93]
[component_container_isolated-17] [WARN] [1783057474.387849705] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3457 Hz
[path_optimizer_node.py-22] [INFO] [1783057474.400304500] [path_optimizer_node]: Path optimised (13 pts, 2.7 ms): mean |kappa| 0.4770 -> 0.4349 (8.8%), max |kappa| 1.2464 -> 0.9378 (24.8%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057474.436172299] [speed_profile_node]: Plan received: 13 poses, mean|κ|=0.4056 m⁻¹, max|κ|=0.5996 m⁻¹, mean_v=0.438 m/s, min_v=0.403 m/s, max_v=0.471 m/s
[component_container_isolated-17] [INFO] [1783057474.529094319] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057475.077474523] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.74,-0.49) yaw=101deg cmd=(vx=0.40 wz=0.51) elapsed=112.5s plan[13pts 1.3m] (2.70,-0.55)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=81% mem=21%
[component_container_isolated-17] [INFO] [1783057475.619052350] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057475.634927478] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057475.648873731] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057475.649074106] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057475.661754151] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057476.390445102] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3477 Hz
[path_optimizer_node.py-22] [INFO] [1783057476.400653105] [path_optimizer_node]: Path optimised (6 pts, 2.5 ms): mean |kappa| 3.7716 -> 0.2876 (92.4%), max |kappa| 8.5847 -> 0.5848 (93.2%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057476.416892942] [speed_profile_node]: Plan received: 6 poses, mean|κ|=0.2540 m⁻¹, max|κ|=0.3471 m⁻¹, mean_v=0.464 m/s, min_v=0.448 m/s, max_v=0.479 m/s
[component_container_isolated-17] [INFO] [1783057476.529350758] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057477.071078752] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.63,-0.06) yaw=112deg cmd=(vx=0.40 wz=0.37) elapsed=114.5s plan[6pts 0.7m] (2.60,0.15)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=87% mem=21%
[component_container_isolated-17] [INFO] [1783057477.519760726] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057477.531946728] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057477.541363147] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057477.541987981] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057477.550860857] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057478.390555167] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.1737 Hz
[path_optimizer_node.py-22] [INFO] [1783057478.409635797] [path_optimizer_node]: Path optimised (5 pts, 4.4 ms): mean |kappa| 4.0840 -> 1.3018 (68.1%), max |kappa| 6.3043 -> 1.8344 (70.9%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057478.425160883] [speed_profile_node]: Plan received: 5 poses, mean|κ|=0.9468 m⁻¹, max|κ|=1.1953 m⁻¹, mean_v=0.349 m/s, min_v=0.314 m/s, max_v=0.385 m/s
[component_container_isolated-17] [INFO] [1783057478.429812509] [controller_server]: Reached the goal!
[component_container_isolated-17] [INFO] [1783057478.521104738] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-17] [INFO] [1783057478.522706697] [controller_server]: Reached the goal!
[tracker_node-19] [WARN] [1783057478.656344851] [tracker_node]: Measurement timeout (3.1s), pausing tracking
[tracker_node-19] [INFO] [1783057478.856539145] [tracker_node]: Tracker initialized at (0.07, 0.00)
[component_container_isolated-17] [INFO] [1783057478.919299576] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-21] [INFO] [1783057478.925069244] [competition_master_stage3]: [结果回调] 巡航完成, 触发VLM推理...
[competition_master_stage3.py-21] [INFO] [1783057478.927794869] [competition_master_stage3]: [VLM] 发布 sign4return=100, 拍照推理中...
[competition_master_stage3.py-21] [INFO] [1783057478.931690203] [competition_master_stage3]: [状态机] CRUISE_CHANNEL → RETURN_P
[vision_ai_node-12] [INFO] [1783057478.932012370] [vision_ai_node]: Received sign4return: 100
[competition_master_stage3.py-21] [INFO] [1783057478.938079038] [competition_master_stage3]: [RETURN] NavigateThroughPoses: 通道入口→P点 (0.38,-1.10)→(-1.99,-0.01)
[component_container_isolated-17] [INFO] [1783057478.940264164] [bt_navigator]: Begin navigating from current location through 2 poses to (-1.99, -0.01)
[component_container_isolated-17] [INFO] [1783057478.941851247] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057478.955272292] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057478.966954545] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057478.967122003] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057478.978451589] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057478.979487089] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[tracker_node-19] [WARN] [1783057479.057031648] [tracker_node]: Measurement timeout (3.5s), pausing tracking
[competition_master_stage3.py-21] [INFO] [1783057479.075946069] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.33,0.32) yaw=136deg cmd=(vx=0.00 wz=0.00) elapsed=116.5s plan[5pts 0.5m] (2.40,0.25)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=87% mem=21%
[tracker_node-19] [INFO] [1783057479.256489483] [tracker_node]: Tracker initialized at (0.07, 0.00)
[hobot_codec_republish-13] [WARN] [1783057479.289627324] [vlm_jpeg_encoder]: Sub imgRaw fps [11.57]
[hobot_codec_republish-13] [WARN] [1783057479.292117325] [vlm_jpeg_encoder]: Pub img fps [11.57]
[component_container_isolated-17] [WARN] [1783057479.403878308] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 2.2623 Hz
[path_optimizer_node.py-22] [INFO] [1783057479.445194733] [path_optimizer_node]: Path optimised (49 pts, 6.2 ms): mean |kappa| 1.2660 -> 2.0036 (-58.3%), max |kappa| 12.3729 -> 18.2211 (-47.3%), max shift 0.080 m
[tracker_node-19] [WARN] [1783057479.458170403] [tracker_node]: Measurement timeout (3.9s), pausing tracking
[speed_profile_node.py-23] [INFO] [1783057479.504229663] [speed_profile_node]: Plan received: 49 poses, mean|κ|=2.0731 m⁻¹, max|κ|=8.4460 m⁻¹, mean_v=0.333 m/s, min_v=0.150 m/s, max_v=0.497 m/s
[component_container_isolated-17] [INFO] [1783057479.542993005] [controller_server]: Received a goal, begin computing control effort.
[tracker_node-19] [INFO] [1783057479.660481364] [tracker_node]: Tracker initialized at (0.07, 0.00)
[tracker_node-19] [WARN] [1783057479.856376658] [tracker_node]: Measurement timeout (4.3s), pausing tracking
[tracker_node-19] [INFO] [1783057480.056102285] [tracker_node]: Tracker initialized at (0.07, 0.00)
[tracker_node-19] [WARN] [1783057480.255951329] [tracker_node]: Measurement timeout (4.7s), pausing tracking
[tracker_node-19] [INFO] [1783057480.458006082] [tracker_node]: Tracker initialized at (0.07, 0.00)
[component_container_isolated-17] [INFO] [1783057480.641940331] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057480.663090503] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057480.684048632] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057480.684265424] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057480.695542510] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057481.079274887] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.18,0.48) yaw=126deg cmd=(vx=0.14 wz=-0.17) elapsed=118.5s plan[49pts 7.1m] (2.20,0.55)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=100% mem=21%
[component_container_isolated-17] [WARN] [1783057481.397378874] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4120 Hz
[path_optimizer_node.py-22] [INFO] [1783057481.446081135] [path_optimizer_node]: Path optimised (51 pts, 5.2 ms): mean |kappa| 1.2545 -> 1.4890 (-18.7%), max |kappa| 11.5702 -> 12.9458 (-11.9%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057481.502647147] [speed_profile_node]: Plan received: 51 poses, mean|κ|=1.5346 m⁻¹, max|κ|=6.4554 m⁻¹, mean_v=0.335 m/s, min_v=0.150 m/s, max_v=0.497 m/s
[component_container_isolated-17] [INFO] [1783057481.549399699] [controller_server]: Passing new path to controller.
[component_container_isolated-17] [INFO] [1783057482.642118817] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057482.668651906] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057482.684046201] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057482.684205951] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057482.694854995] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057483.082833373] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.29,0.36) yaw=142deg cmd=(vx=-0.17 wz=-1.03) elapsed=120.5s plan[51pts 7.7m] (2.30,0.35)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=100% mem=21%
[component_container_isolated-17] [WARN] [1783057483.397654943] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3939 Hz
[imu_madgwick_filter.py-6] [INFO] [1783057483.420553782] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=7066 q_w=0.5868 angle=108.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057483.439311202] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2913 q_w=-0.0262 angle=183.0deg beta=0.0330
[path_optimizer_node.py-22] [INFO] [1783057483.439810953] [path_optimizer_node]: Path optimised (48 pts, 5.8 ms): mean |kappa| 1.1462 -> 1.8888 (-64.8%), max |kappa| 12.4764 -> 19.5879 (-57.0%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057483.472729335] [speed_profile_node]: Plan received: 48 poses, mean|κ|=1.8146 m⁻¹, max|κ|=9.4556 m⁻¹, mean_v=0.340 m/s, min_v=0.150 m/s, max_v=0.497 m/s
[component_container_isolated-17] [INFO] [1783057483.549403935] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057483.656230876] [tracker_node]: Measurement timeout (3.0s), pausing tracking
[tracker_node-19] [INFO] [1783057483.856544670] [tracker_node]: Tracker initialized at (0.05, 0.00)
[tracker_node-19] [WARN] [1783057484.056276256] [tracker_node]: Measurement timeout (3.4s), pausing tracking
[tracker_node-19] [INFO] [1783057484.256132718] [tracker_node]: Tracker initialized at (0.05, 0.00)
[hobot_codec_republish-13] [WARN] [1783057484.315333148] [vlm_jpeg_encoder]: Sub imgRaw fps [12.94]
[tracker_node-19] [WARN] [1783057484.456698721] [tracker_node]: Measurement timeout (3.8s), pausing tracking
[component_container_isolated-17] [INFO] [1783057484.641834387] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057484.656571515] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[tracker_node-19] [INFO] [1783057484.675309270] [tracker_node]: Tracker initialized at (0.05, 0.00)
[component_container_isolated-17] [INFO] [1783057484.675665145] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057484.675793020] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057484.702835567] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [WARN] [1783057484.857199518] [tracker_node]: Measurement timeout (4.2s), pausing tracking
[tracker_node-19] [INFO] [1783057485.056856188] [tracker_node]: Tracker initialized at (0.05, 0.00)
[competition_master_stage3.py-21] [INFO] [1783057485.073004400] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.39,0.29) yaw=121deg cmd=(vx=0.40 wz=-0.05) elapsed=122.5s plan[48pts 7.1m] (2.40,0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=87% mem=22%
[tracker_node-19] [WARN] [1783057485.257719441] [tracker_node]: Measurement timeout (4.6s), pausing tracking
[component_container_isolated-17] [WARN] [1783057485.395506305] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3896 Hz
[path_optimizer_node.py-22] [INFO] [1783057485.444019483] [path_optimizer_node]: Path optimised (47 pts, 9.3 ms): mean |kappa| 1.3316 -> 2.0222 (-51.9%), max |kappa| 13.8164 -> 14.3337 (-3.7%), max shift 0.080 m
[tracker_node-19] [INFO] [1783057485.462467279] [tracker_node]: Tracker initialized at (0.05, 0.00)
[speed_profile_node.py-23] [INFO] [1783057485.489865160] [speed_profile_node]: Plan received: 47 poses, mean|κ|=1.9452 m⁻¹, max|κ|=8.3113 m⁻¹, mean_v=0.323 m/s, min_v=0.150 m/s, max_v=0.497 m/s
[tracker_node-19] [WARN] [1783057485.659393364] [tracker_node]: Measurement timeout (5.0s), pausing tracking
[tracker_node-19] [INFO] [1783057485.860306784] [tracker_node]: Tracker initialized at (0.05, 0.00)
[competition_master_stage3.py-21] [INFO] [1783057487.073848639] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.98,0.84) yaw=120deg cmd=(vx=-0.30 wz=0.07) elapsed=124.5s plan[47pts 6.9m] (2.20,0.55)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=75% mem=22%
[component_container_isolated-17] [INFO] [1783057487.649397727] [controller_server]: Passing new path to controller.
[hobot_codec_republish-13] [WARN] [1783057488.617809236] [vlm_jpeg_encoder]: Pub img fps [6.97]
[component_container_isolated-17] [INFO] [1783057488.741794972] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057488.756812934] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057488.765046977] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057488.765232685] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057488.777619563] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [WARN] [1783057489.056723293] [tracker_node]: Measurement timeout (3.1s), pausing tracking
[competition_master_stage3.py-21] [INFO] [1783057489.069870587] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.07,0.66) yaw=121deg cmd=(vx=0.40 wz=-0.11) elapsed=126.5s plan[47pts 6.9m] (2.20,0.55)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=85% mem=21%
[tracker_node-19] [INFO] [1783057489.265909923] [tracker_node]: Tracker initialized at (0.20, 0.00)
[component_container_isolated-17] [WARN] [1783057489.397650328] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.5839 Hz
[path_optimizer_node.py-22] [INFO] [1783057489.432957002] [path_optimizer_node]: Path optimised (44 pts, 5.3 ms): mean |kappa| 1.1192 -> 1.7861 (-59.6%), max |kappa| 13.3224 -> 19.6233 (-47.3%), max shift 0.080 m
[tracker_node-19] [WARN] [1783057489.455947591] [tracker_node]: Measurement timeout (3.5s), pausing tracking
[speed_profile_node.py-23] [INFO] [1783057489.489921849] [speed_profile_node]: Plan received: 44 poses, mean|κ|=1.7104 m⁻¹, max|κ|=9.2561 m⁻¹, mean_v=0.354 m/s, min_v=0.150 m/s, max_v=0.497 m/s
[component_container_isolated-17] [INFO] [1783057489.549397779] [controller_server]: Passing new path to controller.
[tracker_node-19] [INFO] [1783057489.656112636] [tracker_node]: Tracker initialized at (0.20, 0.00)
[tracker_node-19] [WARN] [1783057489.856507681] [tracker_node]: Measurement timeout (3.9s), pausing tracking
[tracker_node-19] [INFO] [1783057490.059520685] [tracker_node]: Tracker initialized at (0.20, 0.00)
[tracker_node-19] [WARN] [1783057490.255717771] [tracker_node]: Measurement timeout (4.3s), pausing tracking
[tracker_node-19] [INFO] [1783057490.456902525] [tracker_node]: Tracker initialized at (0.20, 0.00)
[component_container_isolated-17] [INFO] [1783057490.641693483] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057490.665475447] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057490.682742576] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057490.683010326] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057490.694447620] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057491.075514998] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.69,1.11) yaw=156deg cmd=(vx=-0.30 wz=-0.16) elapsed=128.5s plan[44pts 6.2m] (2.00,0.75)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=77% mem=21%
[component_container_isolated-17] [WARN] [1783057491.387194568] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-17] [WARN] [1783057491.387440401] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-17] [WARN] [1783057491.387537610] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-17] [INFO] [1783057491.541945103] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057491.552870314] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057491.562797941] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057491.562970691] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [INFO] [1783057491.563055275] [behavior_server]: Running wait
[component_container_isolated-17] [INFO] [1783057491.563268233] [behavior_server]: wait completed successfully
[component_container_isolated-17] [WARN] [1783057491.580088112] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [INFO] [1783057491.742026315] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057491.766169029] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057491.776912573] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057491.777069948] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057491.788951159] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057492.416430968] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.5784 Hz
[path_optimizer_node.py-22] [INFO] [1783057492.457491143] [path_optimizer_node]: Path optimised (66 pts, 6.9 ms): mean |kappa| 1.1910 -> 1.9313 (-62.2%), max |kappa| 12.9226 -> 12.9473 (-0.2%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057492.516623365] [speed_profile_node]: Plan received: 66 poses, mean|κ|=1.9026 m⁻¹, max|κ|=8.3648 m⁻¹, mean_v=0.333 m/s, min_v=0.150 m/s, max_v=0.496 m/s
[component_container_isolated-17] [INFO] [1783057492.549398081] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057493.076049367] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.81,1.03) yaw=131deg cmd=(vx=0.26 wz=0.75) elapsed=130.5s plan[66pts 9.7m] (1.80,1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=71% mem=22%
[imu_madgwick_filter.py-6] [INFO] [1783057493.421995737] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=7557 q_w=0.5700 angle=110.5deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057493.439382824] [imu_madgwick_filter]: [imu_madgwick ->] msgs=3109 q_w=-0.0846 angle=189.7deg beta=0.0330
[tracker_node-19] [WARN] [1783057493.656938582] [tracker_node]: Measurement timeout (3.1s), pausing tracking
[hobot_codec_republish-13] [WARN] [1783057493.676520378] [vlm_jpeg_encoder]: Sub imgRaw fps [13.43]
[tracker_node-19] [INFO] [1783057493.856077544] [tracker_node]: Tracker initialized at (0.08, 0.00)
[tracker_node-19] [WARN] [1783057494.058802215] [tracker_node]: Measurement timeout (3.5s), pausing tracking
[tracker_node-19] [INFO] [1783057494.256418926] [tracker_node]: Tracker initialized at (0.08, 0.00)
[tracker_node-19] [WARN] [1783057494.455728222] [tracker_node]: Measurement timeout (3.9s), pausing tracking
[component_container_isolated-17] [WARN] [1783057494.515419860] [controller_server]: Control loop missed its desired rate of 10.0000Hz
[component_container_isolated-17] [INFO] [1783057493.641875662] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [WARN] [1783057494.142785484] [bt_navigator_navigate_through_poses_rclcpp_node]: Node timed out while executing service call to global_costmap/clear_entirely_global_costmap.
[hobot_codec_republish-13] [WARN] [1783057494.518650403] [vlm_jpeg_encoder]: Pub img fps [11.53]
[component_container_isolated-17] [INFO] [1783057494.530486780] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057494.540647824] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057494.553174202] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [WARN] [1783057494.568118622] [BehaviorTreeEngine]: Behavior Tree tick rate 10.00 was exceeded!
[component_container_isolated-17] [INFO] [1783057494.573208873] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057494.573379040] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [INFO] [1783057494.587597585] [behavior_server]: Running wait
[component_container_isolated-17] [INFO] [1783057494.589366960] [behavior_server]: wait completed successfully
[component_container_isolated-17] [WARN] [1783057494.602676755] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [INFO] [1783057494.658028601] [tracker_node]: Tracker initialized at (0.08, 0.00)
[tracker_node-19] [WARN] [1783057494.855716813] [tracker_node]: Measurement timeout (4.3s), pausing tracking
[component_container_isolated-17] [INFO] [1783057494.871491733] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057494.884270569] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057494.897560030] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057494.897816030] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057494.914977368] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [INFO] [1783057495.056248900] [tracker_node]: Tracker initialized at (0.08, 0.00)
[competition_master_stage3.py-21] [INFO] [1783057495.077082196] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.81,1.03) yaw=131deg cmd=(vx=-0.20 wz=0.97) elapsed=132.5s plan[66pts 9.7m] (1.80,1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=77% mem=21%
[tracker_node-19] [WARN] [1783057495.256193654] [tracker_node]: Measurement timeout (4.7s), pausing tracking
[component_container_isolated-17] [WARN] [1783057495.395153144] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 2.0050 Hz
[path_optimizer_node.py-22] [INFO] [1783057495.442384613] [path_optimizer_node]: Path optimised (47 pts, 5.9 ms): mean |kappa| 1.9123 -> 3.1804 (-66.3%), max |kappa| 11.9226 -> 55.6702 (-366.9%), max shift 0.080 m
[tracker_node-19] [INFO] [1783057495.456687949] [tracker_node]: Tracker initialized at (0.08, 0.00)
[speed_profile_node.py-23] [INFO] [1783057495.482304330] [speed_profile_node]: Plan received: 47 poses, mean|κ|=3.0678 m⁻¹, max|κ|=16.8670 m⁻¹, mean_v=0.310 m/s, min_v=0.150 m/s, max_v=0.497 m/s
[component_container_isolated-17] [INFO] [1783057495.527804174] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057495.655797161] [tracker_node]: Measurement timeout (5.1s), pausing tracking
[tracker_node-19] [INFO] [1783057495.857470457] [tracker_node]: Tracker initialized at (0.08, 0.00)
[tracker_node-19] [WARN] [1783057496.056803378] [tracker_node]: Measurement timeout (5.5s), pausing tracking
[tracker_node-19] [INFO] [1783057496.256809507] [tracker_node]: Tracker initialized at (0.08, 0.00)
[tracker_node-19] [WARN] [1783057496.456561052] [tracker_node]: Measurement timeout (5.9s), pausing tracking
[component_container_isolated-17] [INFO] [1783057496.520675608] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057496.532030028] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057496.540978321] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057496.541179946] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057496.559811284] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [INFO] [1783057496.662762724] [tracker_node]: Tracker initialized at (0.08, 0.00)
[competition_master_stage3.py-21] [INFO] [1783057497.072332776] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.88,0.95) yaw=143deg cmd=(vx=0.27 wz=-0.97) elapsed=134.5s plan[47pts 6.9m] (1.80,1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=88% mem=21%
[component_container_isolated-17] [WARN] [1783057497.389297557] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.1931 Hz
[path_optimizer_node.py-22] [INFO] [1783057497.442724402] [path_optimizer_node]: Path optimised (48 pts, 8.6 ms): mean |kappa| 1.4875 -> 2.0352 (-36.8%), max |kappa| 13.8959 -> 24.1824 (-74.0%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057497.481229036] [speed_profile_node]: Plan received: 48 poses, mean|κ|=2.1545 m⁻¹, max|κ|=11.1668 m⁻¹, mean_v=0.328 m/s, min_v=0.150 m/s, max_v=0.497 m/s
[component_container_isolated-17] [INFO] [1783057497.568968764] [controller_server]: Passing new path to controller.
[component_container_isolated-17] [INFO] [1783057498.561247700] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057498.573966411] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057498.586682039] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057498.586947622] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057498.598565291] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057499.082630652] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.79,1.05) yaw=128deg cmd=(vx=-0.30 wz=-0.28) elapsed=136.5s plan[48pts 6.6m] (1.90,0.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=100% mem=21%
[component_container_isolated-17] [WARN] [1783057499.396514724] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2388 Hz
[path_optimizer_node.py-22] [INFO] [1783057499.441721693] [path_optimizer_node]: Path optimised (43 pts, 7.9 ms): mean |kappa| 1.0904 -> 1.5890 (-45.7%), max |kappa| 12.3078 -> 12.5397 (-1.9%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057499.489253621] [speed_profile_node]: Plan received: 43 poses, mean|κ|=1.5211 m⁻¹, max|κ|=7.6106 m⁻¹, mean_v=0.358 m/s, min_v=0.150 m/s, max_v=0.497 m/s
[hobot_codec_republish-13] [WARN] [1783057499.511857167] [vlm_jpeg_encoder]: Sub imgRaw fps [13.99]
[hobot_codec_republish-13] [WARN] [1783057499.587540476] [vlm_jpeg_encoder]: Pub img fps [14.01]
[component_container_isolated-17] [INFO] [1783057499.605319397] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057499.859009330] [tracker_node]: Measurement timeout (3.2s), pausing tracking
[tracker_node-19] [INFO] [1783057500.058608459] [tracker_node]: Tracker initialized at (0.20, 0.00)
[tracker_node-19] [WARN] [1783057500.256473880] [tracker_node]: Measurement timeout (3.5s), pausing tracking
[tracker_node-19] [INFO] [1783057500.458144926] [tracker_node]: Tracker initialized at (0.20, 0.00)
[tracker_node-19] [WARN] [1783057500.656535847] [tracker_node]: Measurement timeout (3.9s), pausing tracking
[component_container_isolated-17] [INFO] [1783057500.678471518] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057500.695681647] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057500.709721109] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057500.710250734] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057500.727590488] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [INFO] [1783057500.856139184] [tracker_node]: Tracker initialized at (0.20, 0.00)
[tracker_node-19] [WARN] [1783057501.056683939] [tracker_node]: Measurement timeout (4.3s), pausing tracking
[competition_master_stage3.py-21] [INFO] [1783057501.075683651] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.04,0.79) yaw=121deg cmd=(vx=0.40 wz=0.96) elapsed=138.5s plan[43pts 6.1m] (1.90,0.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=93% mem=21%
[tracker_node-19] [INFO] [1783057501.258978110] [tracker_node]: Tracker initialized at (0.20, 0.00)
[component_container_isolated-17] [WARN] [1783057501.388178432] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-17] [WARN] [1783057501.388467182] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-17] [WARN] [1783057501.388595932] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[tracker_node-19] [WARN] [1783057501.456584822] [tracker_node]: Measurement timeout (4.7s), pausing tracking
[component_container_isolated-17] [INFO] [1783057501.568802973] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057501.581302601] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057501.593946312] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057501.594212521] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [INFO] [1783057501.600368480] [behavior_server]: Running wait
[component_container_isolated-17] [INFO] [1783057501.600845439] [behavior_server]: wait completed successfully
[component_container_isolated-17] [WARN] [1783057501.604926148] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [INFO] [1783057501.656461785] [tracker_node]: Tracker initialized at (0.20, 0.00)
[tracker_node-19] [WARN] [1783057501.855706623] [tracker_node]: Measurement timeout (5.1s), pausing tracking
[component_container_isolated-17] [INFO] [1783057501.869084042] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057501.888761755] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057501.903614384] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057501.904621051] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057501.930449348] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [INFO] [1783057502.064283504] [tracker_node]: Tracker initialized at (0.20, 0.00)
[tracker_node-19] [WARN] [1783057502.258534299] [tracker_node]: Measurement timeout (5.6s), pausing tracking
[component_container_isolated-17] [WARN] [1783057502.387839912] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 2.1345 Hz
[path_optimizer_node.py-22] [INFO] [1783057502.420376003] [path_optimizer_node]: Path optimised (39 pts, 6.1 ms): mean |kappa| 0.8990 -> 1.6567 (-84.3%), max |kappa| 13.0307 -> 14.9516 (-14.7%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057502.454400261] [speed_profile_node]: Plan received: 39 poses, mean|κ|=1.5795 m⁻¹, max|κ|=8.4490 m⁻¹, mean_v=0.371 m/s, min_v=0.150 m/s, max_v=0.497 m/s
[tracker_node-19] [INFO] [1783057502.456533053] [tracker_node]: Tracker initialized at (0.20, 0.00)
[component_container_isolated-17] [INFO] [1783057502.615538089] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057502.657115724] [tracker_node]: Measurement timeout (5.9s), pausing tracking
[tracker_node-19] [INFO] [1783057502.856472437] [tracker_node]: Tracker initialized at (0.23, 0.00)
[competition_master_stage3.py-21] [INFO] [1783057503.078843863] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.35,1.04) yaw=-167deg cmd=(vx=0.40 wz=0.94) elapsed=140.5s plan[39pts 5.6m] (1.50,1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=100% mem=21%
[imu_madgwick_filter.py-6] [INFO] [1783057503.417171233] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=8043 q_w=-0.2668 angle=211.0deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057503.440637196] [imu_madgwick_filter]: [imu_madgwick ->] msgs=3303 q_w=-0.8523 angle=296.9deg beta=0.0330
[component_container_isolated-17] [INFO] [1783057503.668672291] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057503.680451543] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057503.689164670] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057503.689329546] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057503.700106465] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057504.417252547] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3732 Hz
[path_optimizer_node.py-22] [INFO] [1783057504.470368476] [path_optimizer_node]: Path optimised (80 pts, 8.7 ms): mean |kappa| 1.6235 -> 2.4329 (-49.9%), max |kappa| 12.4916 -> 15.9514 (-27.7%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057504.523055863] [speed_profile_node]: Plan received: 80 poses, mean|κ|=2.4988 m⁻¹, max|κ|=10.2437 m⁻¹, mean_v=0.297 m/s, min_v=0.150 m/s, max_v=0.492 m/s
[hobot_codec_republish-13] [WARN] [1783057504.556848954] [vlm_jpeg_encoder]: Sub imgRaw fps [13.08]
[component_container_isolated-17] [INFO] [1783057504.615533968] [controller_server]: Passing new path to controller.
[hobot_codec_republish-13] [WARN] [1783057504.621240386] [vlm_jpeg_encoder]: Pub img fps [13.11]
[competition_master_stage3.py-21] [INFO] [1783057505.086785619] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.97,0.74) yaw=-121deg cmd=(vx=-0.20 wz=0.36) elapsed=142.5s plan[80pts 11.9m] (0.90,0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=72% mem=21%
[component_container_isolated-17] [INFO] [1783057505.669546920] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057505.683879924] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057505.704747054] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057505.704902554] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[tracker_node-19] [WARN] [1783057505.856918380] [tracker_node]: Measurement timeout (3.0s), pausing tracking
[component_container_isolated-17] [WARN] [1783057505.920447520] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[tracker_node-19] [INFO] [1783057506.056719218] [tracker_node]: Tracker initialized at (0.23, 0.00)
[tracker_node-19] [WARN] [1783057506.256088556] [tracker_node]: Measurement timeout (3.4s), pausing tracking
[component_container_isolated-17] [WARN] [1783057506.397141506] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4638 Hz
[path_optimizer_node.py-22] [INFO] [1783057506.426036971] [path_optimizer_node]: Path optimised (39 pts, 7.0 ms): mean |kappa| 1.4540 -> 3.6405 (-150.4%), max |kappa| 12.8431 -> 60.9339 (-374.4%), max shift 0.080 m
[tracker_node-19] [INFO] [1783057506.456109353] [tracker_node]: Tracker initialized at (0.23, 0.00)
[speed_profile_node.py-23] [INFO] [1783057506.463674563] [speed_profile_node]: Plan received: 39 poses, mean|κ|=3.6479 m⁻¹, max|κ|=16.9351 m⁻¹, mean_v=0.323 m/s, min_v=0.150 m/s, max_v=0.497 m/s
[component_container_isolated-17] [INFO] [1783057506.615534307] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057506.656119858] [tracker_node]: Measurement timeout (3.8s), pausing tracking
[tracker_node-19] [INFO] [1783057506.857182779] [tracker_node]: Tracker initialized at (0.23, 0.00)
[tracker_node-19] [WARN] [1783057507.056524284] [tracker_node]: Measurement timeout (4.2s), pausing tracking
[competition_master_stage3.py-21] [INFO] [1783057507.075879122] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.98,0.78) yaw=-95deg cmd=(vx=-0.30 wz=-0.61) elapsed=144.5s plan[39pts 5.5m] (1.00,0.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=85% mem=21%
[tracker_node-19] [INFO] [1783057507.256854081] [tracker_node]: Tracker initialized at (0.23, 0.00)
[component_container_isolated-17] [INFO] [1783057507.668723968] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057507.689091056] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057507.702993434] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057507.703156726] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057507.716363354] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057508.392315386] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4512 Hz
[path_optimizer_node.py-22] [INFO] [1783057508.423408644] [path_optimizer_node]: Path optimised (40 pts, 4.8 ms): mean |kappa| 1.1963 -> 1.5826 (-32.3%), max |kappa| 12.7833 -> 16.7908 (-31.3%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057508.454739734] [speed_profile_node]: Plan received: 40 poses, mean|κ|=1.6745 m⁻¹, max|κ|=8.6147 m⁻¹, mean_v=0.347 m/s, min_v=0.150 m/s, max_v=0.497 m/s
[component_container_isolated-17] [INFO] [1783057508.615544605] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057509.075764879] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.03,1.06) yaw=-103deg cmd=(vx=0.36 wz=0.03) elapsed=146.5s plan[40pts 5.8m] (1.00,0.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=100% mem=21%
[hobot_codec_republish-13] [WARN] [1783057509.589128957] [vlm_jpeg_encoder]: Sub imgRaw fps [13.71]
[component_container_isolated-17] [INFO] [1783057509.668828476] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057509.684374021] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057509.694994523] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057509.695160982] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057509.705799276] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[hobot_codec_republish-13] [WARN] [1783057509.761411039] [vlm_jpeg_encoder]: Pub img fps [13.43]
[component_container_isolated-17] [WARN] [1783057510.402458105] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4147 Hz
[path_optimizer_node.py-22] [INFO] [1783057510.436942030] [path_optimizer_node]: Path optimised (36 pts, 6.5 ms): mean |kappa| 1.0879 -> 2.3551 (-116.5%), max |kappa| 14.1016 -> 37.0005 (-162.4%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057510.473756497] [speed_profile_node]: Plan received: 36 poses, mean|κ|=2.2303 m⁻¹, max|κ|=13.2740 m⁻¹, mean_v=0.383 m/s, min_v=0.150 m/s, max_v=0.497 m/s
[component_container_isolated-17] [INFO] [1783057510.615558322] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057511.087594974] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.99,0.94) yaw=-118deg cmd=(vx=0.33 wz=0.97) elapsed=148.5s plan[36pts 4.9m] (1.00,0.85)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=88% mem=21%
[component_container_isolated-17] [INFO] [1783057511.668642485] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057511.677683279] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057511.686835031] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057511.686985239] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057511.696718325] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057512.395559572] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4437 Hz
[path_optimizer_node.py-22] [INFO] [1783057512.429412955] [path_optimizer_node]: Path optimised (41 pts, 6.8 ms): mean |kappa| 1.5005 -> 3.4897 (-132.6%), max |kappa| 11.9872 -> 53.0595 (-342.6%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057512.488619719] [speed_profile_node]: Plan received: 41 poses, mean|κ|=3.3205 m⁻¹, max|κ|=20.7151 m⁻¹, mean_v=0.359 m/s, min_v=0.150 m/s, max_v=0.497 m/s
[component_container_isolated-17] [INFO] [1783057512.615526165] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-4] [WARN] [1783057513.061826978] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1500s > 0.15s, capping
[competition_master_stage3.py-21] [INFO] [1783057513.074808773] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.91,0.64) yaw=-93deg cmd=(vx=0.40 wz=-0.03) elapsed=150.5s plan[41pts 5.6m] (0.90,0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=93% mem=22%
[imu_madgwick_filter.py-6] [INFO] [1783057513.414723353] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=8548 q_w=-0.7223 angle=272.5deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057513.439220859] [imu_madgwick_filter]: [imu_madgwick ->] msgs=3491 q_w=-0.9998 angle=357.7deg beta=0.0330
[component_container_isolated-17] [INFO] [1783057513.668636079] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057513.685355000] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057513.703179379] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057513.703356087] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057513.724860217] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057514.392350833] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4759 Hz
[path_optimizer_node.py-22] [INFO] [1783057514.436944843] [path_optimizer_node]: Path optimised (37 pts, 11.2 ms): mean |kappa| 2.1932 -> 4.4892 (-104.7%), max |kappa| 12.6388 -> 31.3456 (-148.0%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057514.483218938] [speed_profile_node]: Plan received: 37 poses, mean|κ|=4.4444 m⁻¹, max|κ|=17.0263 m⁻¹, mean_v=0.267 m/s, min_v=0.150 m/s, max_v=0.443 m/s
[component_container_isolated-17] [INFO] [1783057514.615523802] [controller_server]: Passing new path to controller.
[hobot_codec_republish-13] [WARN] [1783057514.649961435] [vlm_jpeg_encoder]: Sub imgRaw fps [12.85]
[hobot_codec_republish-13] [WARN] [1783057514.797446636] [vlm_jpeg_encoder]: Pub img fps [13.11]
[competition_master_stage3.py-21] [INFO] [1783057515.074678827] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.07,0.05) yaw=-72deg cmd=(vx=0.25 wz=-0.97) elapsed=152.5s plan[37pts 5.1m] (1.10,-0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=71% mem=22%
[component_container_isolated-17] [INFO] [1783057515.669312175] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057515.686906554] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057515.698538974] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057515.698703807] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057515.922132402] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057516.392889763] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4467 Hz
[path_optimizer_node.py-22] [INFO] [1783057516.430959230] [path_optimizer_node]: Path optimised (37 pts, 5.5 ms): mean |kappa| 2.1784 -> 4.5364 (-108.2%), max |kappa| 13.2419 -> 41.9012 (-216.4%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057516.472199115] [speed_profile_node]: Plan received: 37 poses, mean|κ|=4.4686 m⁻¹, max|κ|=18.1226 m⁻¹, mean_v=0.277 m/s, min_v=0.150 m/s, max_v=0.467 m/s
[component_container_isolated-17] [INFO] [1783057516.615535940] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057517.082866509] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.13,-0.32) yaw=-110deg cmd=(vx=0.25 wz=0.86) elapsed=154.5s plan[37pts 5.0m] (1.10,-0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=88% mem=22%
[component_container_isolated-17] [INFO] [1783057517.668921481] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057517.689174777] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057517.703701573] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057517.703846281] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057517.722220577] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057518.397765612] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4439 Hz
[path_optimizer_node.py-22] [INFO] [1783057518.418469617] [path_optimizer_node]: Path optimised (29 pts, 7.0 ms): mean |kappa| 1.2339 -> 1.5830 (-28.3%), max |kappa| 12.1872 -> 13.3286 (-9.4%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057518.446630665] [speed_profile_node]: Plan received: 29 poses, mean|κ|=1.4894 m⁻¹, max|κ|=6.3527 m⁻¹, mean_v=0.367 m/s, min_v=0.150 m/s, max_v=0.477 m/s
[component_container_isolated-17] [INFO] [1783057518.615541580] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057519.076724939] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.08,-0.48) yaw=-98deg cmd=(vx=0.36 wz=-0.48) elapsed=156.5s plan[29pts 4.3m] (1.10,-0.55)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=85% mem=22%
[component_container_isolated-17] [INFO] [1783057519.668667663] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057519.692706002] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057519.704840130] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057519.705099755] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[hobot_codec_republish-13] [WARN] [1783057519.712429715] [vlm_jpeg_encoder]: Sub imgRaw fps [13.83]
[component_container_isolated-17] [WARN] [1783057519.724705552] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[hobot_codec_republish-13] [WARN] [1783057519.835541161] [vlm_jpeg_encoder]: Pub img fps [13.90]
[component_container_isolated-17] [WARN] [1783057520.391762002] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4434 Hz
[path_optimizer_node.py-22] [INFO] [1783057520.412270965] [path_optimizer_node]: Path optimised (25 pts, 3.8 ms): mean |kappa| 1.1504 -> 1.6108 (-40.0%), max |kappa| 11.9423 -> 12.3753 (-3.6%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057520.483914482] [speed_profile_node]: Plan received: 25 poses, mean|κ|=1.5003 m⁻¹, max|κ|=6.1583 m⁻¹, mean_v=0.374 m/s, min_v=0.150 m/s, max_v=0.496 m/s
[component_container_isolated-17] [INFO] [1783057520.615532388] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-4] [WARN] [1783057520.862215947] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.2497s > 0.15s, capping
[competition_master_stage3.py-21] [INFO] [1783057521.085713333] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.00,-0.78) yaw=-127deg cmd=(vx=0.40 wz=-0.18) elapsed=158.5s plan[25pts 3.6m] (1.00,-0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=83% mem=22%
[component_container_isolated-17] [INFO] [1783057521.668842222] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057521.686415393] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057521.695276229] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057521.697471437] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057521.712369358] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057522.391991811] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4422 Hz
[path_optimizer_node.py-22] [INFO] [1783057522.412001524] [path_optimizer_node]: Path optimised (27 pts, 4.3 ms): mean |kappa| 2.1241 -> 2.5863 (-21.8%), max |kappa| 12.7804 -> 9.2431 (27.7%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057522.441622615] [speed_profile_node]: Plan received: 27 poses, mean|κ|=2.4227 m⁻¹, max|κ|=6.9872 m⁻¹, mean_v=0.290 m/s, min_v=0.150 m/s, max_v=0.490 m/s
[component_container_isolated-17] [INFO] [1783057522.615531906] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057523.071568223] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.61,-1.04) yaw=-149deg cmd=(vx=0.30 wz=0.97) elapsed=160.5s plan[27pts 3.9m] (0.60,-1.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=88% mem=21%
[imu_madgwick_filter.py-6] [INFO] [1783057523.414549555] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=9030 q_w=-0.2190 angle=205.3deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057523.439565561] [imu_madgwick_filter]: [imu_madgwick ->] msgs=3681 q_w=-0.9029 angle=309.1deg beta=0.0330
[component_container_isolated-17] [INFO] [1783057523.668649824] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057523.689467079] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057523.709422834] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057523.709595751] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057523.726891380] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057524.390597830] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4871 Hz
[path_optimizer_node.py-22] [INFO] [1783057524.413086377] [path_optimizer_node]: Path optimised (21 pts, 3.4 ms): mean |kappa| 0.6061 -> 0.7521 (-24.1%), max |kappa| 3.3333 -> 4.8120 (-44.4%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057524.435887841] [speed_profile_node]: Plan received: 21 poses, mean|κ|=0.7782 m⁻¹, max|κ|=3.0565 m⁻¹, mean_v=0.401 m/s, min_v=0.164 m/s, max_v=0.496 m/s
[component_container_isolated-17] [INFO] [1783057524.615566843] [controller_server]: Passing new path to controller.
[hobot_codec_republish-13] [WARN] [1783057524.754862168] [vlm_jpeg_encoder]: Sub imgRaw fps [12.69]
[hobot_codec_republish-13] [WARN] [1783057524.927154251] [vlm_jpeg_encoder]: Pub img fps [12.57]
[competition_master_stage3.py-21] [INFO] [1783057525.077117328] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.47,-1.31) yaw=-109deg cmd=(vx=-0.28 wz=0.31) elapsed=162.5s plan[21pts 2.9m] (0.50,-1.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=77% mem=22%
[component_container_isolated-17] [INFO] [1783057525.668940178] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057525.681099056] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057525.693632101] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057525.693783101] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057525.723526316] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057526.389276393] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.5009 Hz
[path_optimizer_node.py-22] [INFO] [1783057526.407534231] [path_optimizer_node]: Path optimised (27 pts, 3.5 ms): mean |kappa| 1.7439 -> 2.7264 (-56.3%), max |kappa| 11.9622 -> 12.2692 (-2.6%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057526.440817614] [speed_profile_node]: Plan received: 27 poses, mean|κ|=2.7000 m⁻¹, max|κ|=7.5520 m⁻¹, mean_v=0.290 m/s, min_v=0.150 m/s, max_v=0.451 m/s
[component_container_isolated-17] [INFO] [1783057526.615583989] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057526.656614332] [tracker_node]: Measurement timeout (3.1s), pausing tracking
[tracker_node-19] [INFO] [1783057526.857939505] [tracker_node]: Tracker initialized at (-0.05, 0.00)
[tracker_node-19] [WARN] [1783057527.057661637] [tracker_node]: Measurement timeout (3.5s), pausing tracking
[competition_master_stage3.py-21] [INFO] [1783057527.070727431] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.45,-1.31) yaw=-103deg cmd=(vx=-0.17 wz=-0.50) elapsed=164.5s plan[27pts 4.0m] (0.50,-1.35)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=88% mem=22%
[tracker_node-19] [INFO] [1783057527.257307810] [tracker_node]: Tracker initialized at (-0.05, 0.00)
[tracker_node-19] [WARN] [1783057527.458408900] [tracker_node]: Measurement timeout (3.9s), pausing tracking
[tracker_node-19] [INFO] [1783057527.656577739] [tracker_node]: Tracker initialized at (-0.05, 0.00)
[component_container_isolated-17] [INFO] [1783057527.669130700] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057527.688069580] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057527.703619042] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057527.703786542] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057527.719940088] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057528.384022372] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4861 Hz
[path_optimizer_node.py-22] [INFO] [1783057528.439016844] [path_optimizer_node]: Path optimised (21 pts, 26.0 ms): mean |kappa| 0.4859 -> 0.4112 (15.4%), max |kappa| 3.3333 -> 2.2613 (32.2%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057528.475256894] [speed_profile_node]: Plan received: 21 poses, mean|κ|=0.4230 m⁻¹, max|κ|=1.5453 m⁻¹, mean_v=0.438 m/s, min_v=0.273 m/s, max_v=0.496 m/s
[component_container_isolated-17] [INFO] [1783057528.615527137] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057529.078282540] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.47,-1.21) yaw=-87deg cmd=(vx=-0.30 wz=-0.32) elapsed=166.5s plan[21pts 2.9m] (0.50,-1.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=100% mem=22%
[component_container_isolated-17] [INFO] [1783057529.668924141] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057529.679996435] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057529.698153731] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057529.698320273] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057529.721157445] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[hobot_codec_republish-13] [WARN] [1783057529.757322079] [vlm_jpeg_encoder]: Sub imgRaw fps [12.40]
[hobot_codec_republish-13] [WARN] [1783057529.954615626] [vlm_jpeg_encoder]: Pub img fps [12.53]
[component_container_isolated-17] [WARN] [1783057530.411938612] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4000 Hz
[path_optimizer_node.py-22] [INFO] [1783057530.433350742] [path_optimizer_node]: Path optimised (30 pts, 4.3 ms): mean |kappa| 1.6732 -> 2.1274 (-27.1%), max |kappa| 11.9226 -> 11.9088 (0.1%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057530.458104498] [speed_profile_node]: Plan received: 30 poses, mean|κ|=2.1726 m⁻¹, max|κ|=6.1633 m⁻¹, mean_v=0.303 m/s, min_v=0.150 m/s, max_v=0.494 m/s
[component_container_isolated-17] [INFO] [1783057530.615525828] [controller_server]: Passing new path to controller.
[tracker_node-19] [WARN] [1783057530.856907844] [tracker_node]: Measurement timeout (3.1s), pausing tracking
[tracker_node-19] [INFO] [1783057531.057423768] [tracker_node]: Tracker initialized at (0.02, 0.00)
[competition_master_stage3.py-21] [INFO] [1783057531.075960439] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.40,-1.03) yaw=-50deg cmd=(vx=-0.17 wz=-0.03) elapsed=168.5s plan[30pts 4.4m] (0.40,-1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=88% mem=22%
[component_container_isolated-17] [INFO] [1783057531.668869541] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057531.681803085] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057531.695861631] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057531.696021006] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057531.714159010] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057532.401698802] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4191 Hz
[path_optimizer_node.py-22] [INFO] [1783057532.426147182] [path_optimizer_node]: Path optimised (27 pts, 7.4 ms): mean |kappa| 1.9327 -> 2.1999 (-13.8%), max |kappa| 11.9857 -> 14.9875 (-25.0%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057532.447434604] [speed_profile_node]: Plan received: 27 poses, mean|κ|=2.1913 m⁻¹, max|κ|=5.7822 m⁻¹, mean_v=0.284 m/s, min_v=0.150 m/s, max_v=0.487 m/s
[component_container_isolated-17] [INFO] [1783057532.615608437] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057533.075221756] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.40,-1.02) yaw=-50deg cmd=(vx=-0.30 wz=-0.47) elapsed=170.5s plan[27pts 3.9m] (0.40,-0.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=75% mem=22%
[imu_madgwick_filter.py-6] [INFO] [1783057533.416431214] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=9525 q_w=-0.7962 angle=285.5deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057533.441050012] [imu_madgwick_filter]: [imu_madgwick ->] msgs=3878 q_w=-0.9585 angle=326.9deg beta=0.0330
[component_container_isolated-17] [INFO] [1783057533.670175193] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057533.721762788] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057533.837747317] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057533.838004525] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057533.846246110] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057534.393000035] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.6175 Hz
[path_optimizer_node.py-22] [INFO] [1783057534.419186916] [path_optimizer_node]: Path optimised (18 pts, 3.5 ms): mean |kappa| 0.4171 -> 0.1656 (60.3%), max |kappa| 3.3219 -> 0.5311 (84.0%), max shift 0.070 m
[speed_profile_node.py-23] [INFO] [1783057534.437262879] [speed_profile_node]: Plan received: 18 poses, mean|κ|=0.1644 m⁻¹, max|κ|=0.3409 m⁻¹, mean_v=0.478 m/s, min_v=0.449 m/s, max_v=0.495 m/s
[tracker_node-19] [WARN] [1783057534.460681718] [tracker_node]: Reinitializing (divergence=1.95m > 1.5m)
[component_container_isolated-17] [INFO] [1783057534.615517756] [controller_server]: Passing new path to controller.
[hobot_codec_republish-13] [WARN] [1783057534.787944631] [vlm_jpeg_encoder]: Sub imgRaw fps [12.92]
[competition_master_stage3.py-21] [INFO] [1783057535.075546826] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.33,-0.86) yaw=-69deg cmd=(vx=0.40 wz=0.59) elapsed=172.5s plan[18pts 2.5m] (0.30,-0.85)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=100% mem=22%
[competition_master_stage3.py-21] [INFO] [1783057537.072559063] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.46,-0.98) yaw=-47deg cmd=(vx=0.00 wz=0.00) elapsed=174.5s plan[18pts 2.5m] (0.30,-0.85)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=88% mem=22%
[component_container_isolated-17] [INFO] [1783057535.568932738] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [WARN] [1783057536.068889068] [bt_navigator_navigate_through_poses_rclcpp_node]: Node timed out while executing service call to global_costmap/clear_entirely_global_costmap.
[component_container_isolated-17] [WARN] [1783057537.781538444] [controller_server]: Control loop missed its desired rate of 10.0000Hz
[hobot_codec_republish-13] [WARN] [1783057537.784469987] [vlm_jpeg_encoder]: Pub img fps [7.92]
[component_container_isolated-17] [INFO] [1783057537.808555618] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057537.813141910] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057537.821170246] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [WARN] [1783057537.833046832] [BehaviorTreeEngine]: Behavior Tree tick rate 10.00 was exceeded!
[component_container_isolated-17] [INFO] [1783057537.834159457] [behavior_server]: Running wait
[component_container_isolated-17] [INFO] [1783057537.834532374] [behavior_server]: wait completed successfully
[component_container_isolated-17] [INFO] [1783057537.835754499] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057537.835906958] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057537.845703502] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [INFO] [1783057538.136423240] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057538.150710993] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057538.158714537] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057538.158879828] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057538.165486538] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057538.390043760] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 4.3049 Hz
[path_optimizer_node.py-22] [INFO] [1783057538.407273639] [path_optimizer_node]: Path optimised (19 pts, 3.9 ms): mean |kappa| 0.2062 -> 0.0699 (66.1%), max |kappa| 2.1832 -> 0.3190 (85.4%), max shift 0.028 m
[speed_profile_node.py-23] [INFO] [1783057538.432443479] [speed_profile_node]: Plan received: 19 poses, mean|κ|=0.0731 m⁻¹, max|κ|=0.1696 m⁻¹, mean_v=0.492 m/s, min_v=0.478 m/s, max_v=0.498 m/s
[component_container_isolated-17] [INFO] [1783057538.590108642] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057539.084651763] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.46,-0.98) yaw=-47deg cmd=(vx=-0.30 wz=0.74) elapsed=176.5s plan[19pts 2.7m] (0.50,-0.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=100% mem=22%
[component_container_isolated-17] [INFO] [1783057539.570336132] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057539.582868510] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057539.603948141] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057539.604135557] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057539.619068228] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057540.385766749] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2786 Hz
[path_optimizer_node.py-22] [INFO] [1783057540.401100753] [path_optimizer_node]: Path optimised (16 pts, 3.2 ms): mean |kappa| 0.1756 -> 0.0674 (61.6%), max |kappa| 2.3615 -> 0.3852 (83.7%), max shift 0.029 m
[speed_profile_node.py-23] [INFO] [1783057540.440940554] [speed_profile_node]: Plan received: 16 poses, mean|κ|=0.0687 m⁻¹, max|κ|=0.2053 m⁻¹, mean_v=0.492 m/s, min_v=0.473 m/s, max_v=0.500 m/s
[component_container_isolated-17] [INFO] [1783057540.514901656] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783057541.084672796] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.04,-0.73) yaw=-23deg cmd=(vx=-0.30 wz=0.31) elapsed=178.5s plan[16pts 2.1m] (-0.00,-0.75)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=77% mem=22%
[component_container_isolated-17] [INFO] [1783057541.528525780] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057541.541241075] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057541.550009368] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057541.550191202] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057541.564061830] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783057542.386678241] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2017 Hz
[path_optimizer_node.py-22] [INFO] [1783057542.415031206] [path_optimizer_node]: Path optimised (14 pts, 2.9 ms): mean |kappa| 0.1956 -> 0.0666 (66.0%), max |kappa| 2.1912 -> 0.3294 (85.0%), max shift 0.028 m
[speed_profile_node.py-23] [INFO] [1783057542.444032088] [speed_profile_node]: Plan received: 14 poses, mean|κ|=0.0668 m⁻¹, max|κ|=0.1749 m⁻¹, mean_v=0.493 m/s, min_v=0.478 m/s, max_v=0.500 m/s
[component_container_isolated-17] [INFO] [1783057542.543715321] [controller_server]: Passing new path to controller.
[hobot_codec_republish-13] [WARN] [1783057542.838242227] [vlm_jpeg_encoder]: Sub imgRaw fps [14.83]
[hobot_codec_republish-13] [WARN] [1783057542.853428647] [vlm_jpeg_encoder]: Pub img fps [14.80]
[competition_master_stage3.py-21] [ERROR] [1783057543.022272397] [competition_master_stage3]: >>> [TIMEOUT] 全局超时! 已运行 180.5s > 180.0s, 当前状态=RETURN_P
[imu_madgwick_filter.py-6] [INFO] [1783057543.420372912] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=10019 q_w=-0.9495 angle=323.4deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057543.439138292] [imu_madgwick_filter]: [imu_madgwick ->] msgs=4077 q_w=-0.7958 angle=285.5deg beta=0.0330
[component_container_isolated-17] [INFO] [1783057543.651271469] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057543.667667640] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057543.683283060] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057543.683436394] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057543.698109064] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057543.901184906] [competition_master_stage3]: [BAG] 录制已停止
[competition_master_stage3.py-21] [INFO] [1783057543.905770032] [competition_master_stage3]: [状态机] RETURN_P → TIMEOUT
[competition_master_stage3.py-21] [INFO] [1783057543.914391076] [competition_master_stage3]:
[competition_master_stage3.py-21] [INFO] [1783057543.916937868] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-21] [INFO] [1783057543.919284285] [competition_master_stage3]: >>> [Stage 3] 任务结束 <<<
[competition_master_stage3.py-21] [INFO] [1783057543.923849411] [competition_master_stage3]:   最终状态: TIMEOUT
[competition_master_stage3.py-21] [INFO] [1783057543.926916871] [competition_master_stage3]:   总耗时:   181.4s
[competition_master_stage3.py-21] [INFO] [1783057543.930513996] [competition_master_stage3]:   --- 各阶段耗时 ---
[competition_master_stage3.py-21] [INFO] [1783057543.935510248] [competition_master_stage3]:   LAUNCH................ 17.5s
[competition_master_stage3.py-21] [INFO] [1783057543.940888999] [competition_master_stage3]:   NAV_TO_QR............. 23.0s
[competition_master_stage3.py-21] [INFO] [1783057543.945067625] [competition_master_stage3]:   BACKING_UP............ 6.0s
[competition_master_stage3.py-21] [INFO] [1783057543.948993084] [competition_master_stage3]:   CRUISE_CHANNEL........ 87.4s
[competition_master_stage3.py-21] [INFO] [1783057543.956707878] [competition_master_stage3]:   RETURN_P.............. 65.0s
[competition_master_stage3.py-21] [INFO] [1783057543.962601504] [competition_master_stage3]:   (transition/overhead). -17.5s
[competition_master_stage3.py-21] [INFO] [1783057543.968135131] [competition_master_stage3]:   --- ---
[competition_master_stage3.py-21] [INFO] [1783057543.974768341] [competition_master_stage3]:   QR 原始数据: 1584
[competition_master_stage3.py-21] [INFO] [1783057543.978487925] [competition_master_stage3]:   QR 方向:   逆时针 (CW=顺时针/odd, CCW=逆时针/even)
[competition_master_stage3.py-21] [WARN] [1783057543.981676051] [competition_master_stage3]:   VLM 结果:  未收到
[competition_master_stage3.py-21] [INFO] [1783057543.984237843] [competition_master_stage3]:   超时限制:  180.0s (全局)
[competition_master_stage3.py-21] [INFO] [1783057543.986475344] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-21] [INFO] [1783057543.993829720] [competition_master_stage3]: [TRAJ] CSV已保存: /userdata/dev_ws/trajectory_20260703_134543.csv (186 点)
[competition_master_stage3.py-21] [INFO] [1783057544.448434666] [competition_master_stage3]: [TRAJ] Nav2 params snapshot: 31 keys
[competition_master_stage3.py-21] [INFO] [1783057544.454331959] [competition_master_stage3]: [TRAJ] 摘要JSON已保存: /userdata/dev_ws/trajectory_20260703_134543_summary.json
[competition_master_stage3.py-21] [INFO] [1783057544.458772794] [competition_master_stage3]: [TRAJ] 规划历史已保存: /userdata/dev_ws/trajectory_20260703_134543_plans.csv (74 次规划)
[competition_master_stage3.py-21] [INFO] [1783057544.479570632] [competition_master_stage3]: [TRAJ] costmap PGM已保存: /userdata/dev_ws/trajectory_20260703_134543_costmap.pgm
[component_container_isolated-17] [WARN] [1783057544.512156307] [planner_server]: GridBased: failed to create plan, exceeded maximum iterations.
[component_container_isolated-17] [WARN] [1783057544.512395515] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (-1.99, -0.01)
[component_container_isolated-17] [WARN] [1783057544.512531890] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[competition_master_stage3.py-21] [INFO] [1783057544.537092480] [competition_master_stage3]: [DIAG] state=TIMEOUT pos=(-0.19,-0.66) yaw=-10deg cmd=(vx=-0.30 wz=-0.24) elapsed=181.9s plan[14pts 1.9m] (-0.20,-0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=42% mem=21%
[component_container_isolated-17] [INFO] [1783057544.633824462] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057544.642860339] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057544.652321008] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057544.652501883] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [INFO] [1783057544.661699260] [behavior_server]: Running wait
[component_container_isolated-17] [INFO] [1783057544.662814927] [behavior_server]: wait completed successfully
[component_container_isolated-17] [WARN] [1783057544.665584428] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [INFO] [1783057544.933886994] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057544.947417539] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057544.958361125] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057544.958529792] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057544.971189462] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057545.077771405] [competition_master_stage3]: [DIAG] state=TIMEOUT pos=(-0.58,-0.50) yaw=-25deg cmd=(vx=0.00 wz=0.00) elapsed=182.5s plan[14pts 1.9m] (-0.20,-0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=84% mem=21%
[component_container_isolated-17] [WARN] [1783057545.481062005] [planner_server]: GridBased: failed to create plan, exceeded maximum iterations.
[component_container_isolated-17] [WARN] [1783057545.481299755] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (-1.99, -0.01)
[component_container_isolated-17] [WARN] [1783057545.481405546] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-17] [INFO] [1783057545.679486137] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-17] [INFO] [1783057545.679667637] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-17] [INFO] [1783057545.680219804] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-17] [INFO] [1783057545.688854723] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057545.699173350] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057545.701445934] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057545.701695851] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057545.716980688] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [INFO] [1783057545.726753774] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057545.735492776] [behavior_server]: Running wait
[component_container_isolated-17] [INFO] [1783057545.735971109] [behavior_server]: wait completed successfully
[component_container_isolated-17] [WARN] [1783057545.736167484] [BehaviorTreeEngine]: Behavior Tree tick rate 10.00 was exceeded!
[component_container_isolated-17] [INFO] [1783057545.738952652] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057545.739092485] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057545.751324196] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [INFO] [1783057545.934737950] [behavior_server]: Running backup
[competition_master_stage3.py-21] [INFO] [1783057547.079226942] [competition_master_stage3]: [DIAG] state=TIMEOUT pos=(-0.45,-0.54) yaw=-17deg cmd=(vx=0.00 wz=0.00) elapsed=184.5s plan[14pts 1.9m] (-0.20,-0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=75% mem=21%
[hobot_codec_republish-13] [WARN] [1783057547.848064508] [vlm_jpeg_encoder]: Sub imgRaw fps [12.38]
[hobot_codec_republish-13] [WARN] [1783057547.918757484] [vlm_jpeg_encoder]: Pub img fps [12.44]
[competition_master_stage3.py-21] [INFO] [1783057549.075450271] [competition_master_stage3]: [DIAG] state=TIMEOUT pos=(-0.45,-0.54) yaw=-17deg cmd=(vx=0.00 wz=0.00) elapsed=186.5s plan[14pts 1.9m] (-0.20,-0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=77% mem=21%
[competition_master_stage3.py-21] [INFO] [1783057551.072489852] [competition_master_stage3]: [DIAG] state=TIMEOUT pos=(-0.61,-0.49) yaw=-17deg cmd=(vx=0.00 wz=0.00) elapsed=188.5s plan[14pts 1.9m] (-0.20,-0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=66% mem=21%
[hobot_codec_republish-13] [WARN] [1783057552.871159801] [vlm_jpeg_encoder]: Sub imgRaw fps [13.54]
[hobot_codec_republish-13] [WARN] [1783057552.930790733] [vlm_jpeg_encoder]: Pub img fps [13.57]
[competition_master_stage3.py-21] [INFO] [1783057553.076533436] [competition_master_stage3]: [DIAG] state=TIMEOUT pos=(-0.77,-0.49) yaw=-17deg cmd=(vx=0.00 wz=0.00) elapsed=190.5s plan[14pts 1.9m] (-0.20,-0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=87% mem=21%
[imu_madgwick_filter.py-6] [INFO] [1783057553.414774396] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=10545 q_w=-0.9754 angle=334.5deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783057553.440321235] [imu_madgwick_filter]: [imu_madgwick ->] msgs=4276 q_w=-0.7118 angle=270.8deg beta=0.0330
[component_container_isolated-17] [WARN] [1783057554.835839877] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-17] [WARN] [1783057554.836010502] [behavior_server]: backup failed
[component_container_isolated-17] [WARN] [1783057554.836082335] [behavior_server]: [backup] [ActionServer] Aborting handle.
[imu_madgwick_filter.py-4] [WARN] [1783057554.959744866] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1501s > 0.15s, capping
[competition_master_stage3.py-21] [INFO] [1783057555.077484479] [competition_master_stage3]: [DIAG] state=TIMEOUT pos=(-0.77,-0.49) yaw=-17deg cmd=(vx=0.00 wz=0.00) elapsed=192.5s plan[14pts 1.9m] (-0.20,-0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=50% mem=21%
[component_container_isolated-17] [INFO] [1783057555.139489370] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-17] [INFO] [1783057555.154616498] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057555.163405292] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057555.163649209] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [INFO] [1783057555.163443876] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [WARN] [1783057555.178563921] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [INFO] [1783057555.179865880] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057555.185220631] [behavior_server]: Running wait
[component_container_isolated-17] [INFO] [1783057555.185619798] [behavior_server]: wait completed successfully
[component_container_isolated-17] [INFO] [1783057555.191723216] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057555.191873758] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057555.203714969] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [INFO] [1783057555.434420527] [behavior_server]: Running backup
[component_container_isolated-17] [WARN] [1783057555.435779361] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-17] [WARN] [1783057555.435917444] [behavior_server]: backup failed
[component_container_isolated-17] [WARN] [1783057555.436067902] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-17] [INFO] [1783057555.734567602] [behavior_server]: Running wait
[competition_master_stage3.py-21] [INFO] [1783057557.076059398] [competition_master_stage3]: [DIAG] state=TIMEOUT pos=(-0.96,-0.43) yaw=-16deg cmd=(vx=0.00 wz=0.00) elapsed=194.5s plan[14pts 1.9m] (-0.20,-0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=75% mem=21%
[hobot_codec_republish-13] [WARN] [1783057557.946676867] [vlm_jpeg_encoder]: Sub imgRaw fps [13.00]
[hobot_codec_republish-13] [WARN] [1783057557.948986576] [vlm_jpeg_encoder]: Pub img fps [12.95]
[component_container_isolated-17] [INFO] [1783057558.739810734] [behavior_server]: wait completed successfully
[component_container_isolated-17] [INFO] [1783057559.033828016] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783057559.047143311] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783057559.057720147] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783057559.057929606] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783057559.069964442] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783057559.076241944] [competition_master_stage3]: [DIAG] state=TIMEOUT pos=(-0.96,-0.43) yaw=-16deg cmd=(vx=0.00 wz=0.00) elapsed=196.5s plan[14pts 1.9m] (-0.20,-0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=100% mem=21%
[component_container_isolated-17] [WARN] [1783057559.387947772] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 3.0729 Hz
[path_optimizer_node.py-22] [INFO] [1783057559.400725484] [path_optimizer_node]: Path optimised (17 pts, 2.7 ms): mean |kappa| 1.1346 -> 1.8691 (-64.7%), max |kappa| 3.3334 -> 9.7675 (-193.0%), max shift 0.080 m
[speed_profile_node.py-23] [INFO] [1783057559.428053491] [speed_profile_node]: Plan received: 17 poses, mean|κ|=1.7086 m⁻¹, max|κ|=4.7777 m⁻¹, mean_v=0.334 m/s, min_v=0.150 m/s, max_v=0.492 m/s
^C[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[lifecycle_manager-16] [INFO] [1783057559.473786919] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-16] [INFO] [1783057559.474046502] [lifecycle_manager_keepout]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_keepout)
[lifecycle_manager-16] [INFO] [1783057559.474215628] [lifecycle_manager_keepout]: Terminating bond timer...
[ERROR] [origincar_base_node-1]: process has died [pid 22519, exit code -6, cmd '/userdata/dev_ws/install/origincar_base/lib/origincar_base/origincar_base_node --ros-args --params-file /tmp/launch_params_t778pi1n --params-file /tmp/launch_params_yrhto_vn'].
[ERROR] [lslidar_driver_node-2]: process has died [pid 22521, exit code -6, cmd '/userdata/dev_ws/install/lslidar_driver/lib/lslidar_driver/lslidar_driver_node --ros-args -r __node:=lslidar_driver_node --params-file /userdata/dev_ws/install/lslidar_driver/share/lslidar_driver/params/lsx10.yaml'].
[INFO] [ekf_node-7]: process has finished cleanly [pid 22531]
[INFO] [robot_state_publisher-3]: process has finished cleanly [pid 22523]
[ERROR] [rviz2-24]: process has died [pid 22875, exit code -11, cmd '/opt/ros/humble/lib/rviz2/rviz2 -d /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/rviz/nav.rviz --ros-args -r __node:=rviz2'].
[INFO] [hobot_codec_republish-13]: process has finished cleanly [pid 22581]
[INFO] [static_transform_publisher-8]: process has finished cleanly [pid 22571]
[INFO] [lifecycle_manager-16]: process has finished cleanly [pid 22687]
[INFO] [costmap_filter_info_server-15]: process has finished cleanly [pid 22680]
[INFO] [map_server-14]: process has finished cleanly [pid 22678]
[INFO] [bmi088_iio_bridge.py-5]: process has finished cleanly [pid 22527]
[INFO] [imu_madgwick_filter.py-4]: process has finished cleanly [pid 22525]
[map_server-14] [INFO] [1783057559.473823377] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-14] [INFO] [1783057559.474046377] [keepout_mask_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_mask_server)
[map_server-14] [INFO] [1783057559.474353086] [keepout_mask_server]: Deactivating
[map_server-14] [INFO] [1783057559.474444336] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[INFO] [imu_madgwick_filter.py-6]: process has finished cleanly [pid 22529]
[rviz2-24] [INFO] [1783057559.473839544] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[static_transform_publisher-8] [INFO] [1783057559.473910502] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-17] [INFO] [1783057559.474095544] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-17] [INFO] [1783057559.474212836] [lifecycle_manager_navigation]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_navigation)
[component_container_isolated-17] [INFO] [1783057559.474451253] [lifecycle_manager_navigation]: Terminating bond timer...
[origincar_base_node-1] [INFO] [1783057559.475213294] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1783057559.475668128] [origincar_base]: Stop command sent to STM32 on shutdown.
[origincar_base_node-1] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[origincar_base_node-1] terminate called after throwing an instance of 'rclcpp::exceptions::RCLError'
[origincar_base_node-1]   what():  failed to create guard condition: the given context is not valid, either rcl_init() was not called or rcl_shutdown() was called., at ./src/rcl/guard_condition.c:67
[costmap_filter_info_server-15] [INFO] [1783057559.476366961] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-15] [INFO] [1783057559.476672836] [keepout_filter_info_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_filter_info_server)
[costmap_filter_info_server-15] [INFO] [1783057559.476947753] [keepout_filter_info_server]: Deactivating
[costmap_filter_info_server-15] [INFO] [1783057559.477050128] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-15] [INFO] [1783057559.488469589] [keepout_filter_info_server]: Cleaning up
[costmap_filter_info_server-15] [INFO] [1783057559.488702340] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-15] [INFO] [1783057559.842626596] [keepout_filter_info_server]: Destroying
[robot_state_publisher-3] [INFO] [1783057559.476962462] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[aurora930_node-9] [INFO] [1783057559.485269005] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[aurora930_node-9] I0703 13:45:59.535164 22573 ros2_node.cc:90] process quit succeed
[aurora930_node-9] I0703 13:45:59.535362 22573 aurora900_ros2_device.cc:83] begin stop()
[aurora930_node-9] I0703 13:45:59.625053 22573 aurora900_ros2_device.cc:103] stop stream
[aurora930_node-9] 2026-07-03 13:45:59.696 ( 227.420s) [        90794020]      aurora900_impl.cc:648   INFO| ir_stream_count_=0, rgb_stream_count_=0, depth_stream_count_=0
[aurora930_node-9] 2026-07-03 13:45:59.696 ( 227.420s) [        90794020]      aurora900_impl.cc:649   INFO| mask=7
[aurora930_node-9] I0703 13:46:00.044888 22573 aurora900_ros2_device.cc:105] destroy stream
[aurora930_node-9] I0703 13:46:00.045117 22573 aurora900_ros2_device.cc:110] close glog
[aurora930_node-9] WARNING: Logging before InitGoogleLogging() is written to STDERR
[aurora930_node-9] I0703 13:46:00.045253 22573 ros2_device.cc:113] close device...
[aurora930_node-9] 2026-07-03 13:46:00.545 ( 228.269s) [        611D37E0]         cmd_backend.cc:40    INFO| RunBlocking is end!!!
[aurora930_node-9] 2026-07-03 13:46:00.746 ( 228.470s) [        90794020]deptrum_camera_vendor.c:121   INFO| device is close.
[aurora930_node-9] I0703 13:46:00.749464 22573 ros2_device.cc:116] quit succeed
[ekf_node-7] [INFO] [1783057559.485410130] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[competition_master_stage3.py-21] [INFO] [1783057559.518397139] [competition_master_stage3]: [MAIN] 收到 Ctrl+C, 停止录制 + 保存轨迹...
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.522332181] [competition_master_stage3]:
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.525881682] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.529310808] [competition_master_stage3]: >>> [Stage 3] 任务结束 <<<
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.532950851] [competition_master_stage3]:   最终状态: TIMEOUT
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.536692560] [competition_master_stage3]:   总耗时:   197.0s
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.539745686] [competition_master_stage3]:   --- 各阶段耗时 ---
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.542848645] [competition_master_stage3]:   LAUNCH................ 17.5s
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.546048729] [competition_master_stage3]:   NAV_TO_QR............. 23.0s
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.549283980] [competition_master_stage3]:   BACKING_UP............ 6.0s
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.552957064] [competition_master_stage3]:   CRUISE_CHANNEL........ 87.4s
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.556274732] [competition_master_stage3]:   RETURN_P.............. 65.0s
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.559474357] [competition_master_stage3]:   (transition/overhead). -1.9s
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.562734525] [competition_master_stage3]:   --- ---
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.565876901] [competition_master_stage3]:   QR 原始数据: 1584
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.569234360] [competition_master_stage3]:   QR 方向:   逆时针 (CW=顺时针/odd, CCW=逆时针/even)
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [WARN] [1783057559.573336611] [competition_master_stage3]:   VLM 结果:  未收到
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.576711695] [competition_master_stage3]:   超时限制:  180.0s (全局)
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.627492083] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057559.637198585] [competition_master_stage3]: [TRAJ] CSV已保存: /userdata/dev_ws/trajectory_20260703_134559.csv (192 点)
[speed_profile_node.py-23] Traceback (most recent call last):
[speed_profile_node.py-23]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/speed_profile_node.py", line 395, in <module>
[speed_profile_node.py-23]     main()
[speed_profile_node.py-23]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/speed_profile_node.py", line 391, in main
[speed_profile_node.py-23]     rclpy.shutdown()
[speed_profile_node.py-23]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 130, in shutdown
[speed_profile_node.py-23]     _shutdown(context=context)
[speed_profile_node.py-23]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/utilities.py", line 58, in shutdown
[speed_profile_node.py-23]     return context.shutdown()
[speed_profile_node.py-23]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/context.py", line 102, in shutdown
[speed_profile_node.py-23]     self.__context.shutdown()
[speed_profile_node.py-23] rclpy._rclpy_pybind11.RCLError: failed to shutdown: rcl_shutdown already called on the given context, at ./src/rcl/init.c:241
[path_optimizer_node.py-22] Traceback (most recent call last):
[path_optimizer_node.py-22]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/path_optimizer_node.py", line 620, in <module>
[path_optimizer_node.py-22]     main()
[path_optimizer_node.py-22]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/path_optimizer_node.py", line 616, in main
[path_optimizer_node.py-22]     rclpy.shutdown()
[path_optimizer_node.py-22]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 130, in shutdown
[path_optimizer_node.py-22]     _shutdown(context=context)
[path_optimizer_node.py-22]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/utilities.py", line 58, in shutdown
[path_optimizer_node.py-22]     return context.shutdown()
[path_optimizer_node.py-22]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/context.py", line 102, in shutdown
[path_optimizer_node.py-22]     self.__context.shutdown()
[path_optimizer_node.py-22] rclpy._rclpy_pybind11.RCLError: failed to shutdown: rcl_shutdown already called on the given context, at ./src/rcl/init.c:241
[map_server-14] [INFO] [1783057559.505218344] [keepout_mask_server]: Cleaning up
[map_server-14] [INFO] [1783057559.505506052] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[map_server-14] [INFO] [1783057559.788981624] [keepout_mask_server]: Destroying
[component_container_isolated-17] [INFO] [1783057559.539121102] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-17] [INFO] [1783057559.726250733] [local_costmap.local_costmap]: Message Filter dropping message: frame 'laser_link' at time 1783057559.425 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-17] [INFO] [1783057560.138858129] [velocity_smoother]: Running Nav2 LifecycleNode rcl preshutdown (velocity_smoother)
[component_container_isolated-17] [INFO] [1783057560.139236754] [velocity_smoother]: Deactivating
[component_container_isolated-17] [INFO] [1783057560.139376087] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057560.149870632] [velocity_smoother]: Cleaning up
[component_container_isolated-17] [INFO] [1783057560.150120423] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057560.150188882] [waypoint_follower]: Running Nav2 LifecycleNode rcl preshutdown (waypoint_follower)
[component_container_isolated-17] [INFO] [1783057560.150293298] [waypoint_follower]: Deactivating
[component_container_isolated-17] [INFO] [1783057560.150369548] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057560.160630884] [waypoint_follower]: Cleaning up
[component_container_isolated-17] [INFO] [1783057560.176916888] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057560.177082972] [planner_server]: Running Nav2 LifecycleNode rcl preshutdown (planner_server)
[component_container_isolated-17] [INFO] [1783057560.177249847] [planner_server]: Deactivating
[component_container_isolated-17] [INFO] [1783057560.177865430] [global_costmap.global_costmap]: Deactivating
[component_container_isolated-17] [INFO] [1783057560.373875522] [planner_server]: Deactivating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-17] [INFO] [1783057560.374231188] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057560.384680274] [planner_server]: Cleaning up
[component_container_isolated-17] [INFO] [1783057560.445487790] [global_costmap.global_costmap]: Cleaning up
[component_container_isolated-17] [INFO] [1783057560.470527046] [planner_server]: Cleaning up plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-17] [INFO] [1783057560.471787380] [planner_server]: Destroying plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-17] [INFO] [1783057560.518131600] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057560.518276016] [behavior_server]: Running Nav2 LifecycleNode rcl preshutdown (behavior_server)
[component_container_isolated-17] [INFO] [1783057560.518395975] [behavior_server]: Deactivating
[component_container_isolated-17] [INFO] [1783057560.518591433] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057560.529301394] [behavior_server]: Cleaning up
[component_container_isolated-17] [INFO] [1783057560.567000195] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057560.567177737] [lifecycle_manager_localization]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_localization)
[component_container_isolated-17] [INFO] [1783057560.567270945] [lifecycle_manager_localization]: Terminating bond timer...
[component_container_isolated-17] [INFO] [1783057560.631524003] [smoother_server]: Running Nav2 LifecycleNode rcl preshutdown (smoother_server)
[component_container_isolated-17] [INFO] [1783057560.631876045] [smoother_server]: Deactivating
[component_container_isolated-17] [INFO] [1783057560.631958795] [smoother_server]: Deactivating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-17] [INFO] [1783057560.632105295] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057560.642600923] [smoother_server]: Cleaning up
[component_container_isolated-17] [INFO] [1783057560.642740090] [smoother_server]: Cleaning up smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-17] [INFO] [1783057560.802294630] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057560.802443672] [amcl]: Running Nav2 LifecycleNode rcl preshutdown (amcl)
[component_container_isolated-17] [INFO] [1783057560.802565088] [amcl]: Deactivating
[component_container_isolated-17] [INFO] [1783057560.802718130] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057560.813346841] [amcl]: Cleaning up
[component_container_isolated-17] [INFO] [1783057560.869207272] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057560.872831356] [bt_navigator]: Running Nav2 LifecycleNode rcl preshutdown (bt_navigator)
[component_container_isolated-17] [INFO] [1783057560.874226773] [bt_navigator]: Deactivating
[component_container_isolated-17] [WARN] [1783057560.874400148] [bt_navigator]: [navigate_through_poses] [ActionServer] Requested to deactivate server but goal is still executing. Should check if action server is running before deactivating.
[component_container_isolated-17] [INFO] [1783057560.939554248] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-17] [INFO] [1783057560.939778748] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-17] [WARN] [1783057560.940417707] [bt_navigator]: [navigate_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-17] [INFO] [1783057560.940949457] [bt_navigator]: Goal canceled
[component_container_isolated-17] [WARN] [1783057560.941544290] [bt_navigator]: [navigate_through_poses] [ActionServer] Stopping the thread per request.
[component_container_isolated-17] [INFO] [1783057560.942153165] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057560.952637751] [bt_navigator]: Cleaning up
[component_container_isolated-17] [INFO] [1783057561.371151024] [bt_navigator]: Completed Cleaning up
[component_container_isolated-17] [INFO] [1783057561.371556649] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057561.371680399] [controller_server]: Running Nav2 LifecycleNode rcl preshutdown (controller_server)
[component_container_isolated-17] [INFO] [1783057561.371819566] [controller_server]: Deactivating
[component_container_isolated-17] [INFO] [1783057561.371885357] [controller_server]: Deactivating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-17] [INFO] [1783057561.372121066] [local_costmap.local_costmap]: Deactivating
[component_container_isolated-17] [INFO] [1783057561.387150861] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057561.397778364] [controller_server]: Cleaning up
[component_container_isolated-17] [INFO] [1783057561.397952031] [controller_server]: Cleaning up controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-17] [INFO] [1783057561.398271239] [local_costmap.local_costmap]: Cleaning up
[lifecycle_manager-16] [INFO] [1783057560.022215599] [lifecycle_manager_keepout]: Destroying lifecycle_manager_keepout
[ERROR] [costmap_publisher-20]: process has died [pid 22856, exit code 1, cmd '/userdata/dev_ws/install/object_tracker/lib/object_tracker/costmap_publisher --ros-args -r __node:=costmap_publisher'].
[ERROR] [speed_profile_node.py-23]: process has died [pid 22873, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/speed_profile_node.py --ros-args -r __node:=speed_profile_node --params-file /tmp/launch_params_xb99u3m_'].
[vision_ai_node-12] Traceback (most recent call last):
[vision_ai_node-12]   File "/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node", line 33, in <module>
[vision_ai_node-12]     sys.exit(load_entry_point('racing-vision-ai==0.0.1', 'console_scripts', 'vision_ai_node')())
[vision_ai_node-12]   File "/userdata/dev_ws/install/racing_vision_ai/lib/python3.10/site-packages/racing_vision_ai/vision_ai_node.py", line 226, in main
[vision_ai_node-12]     rclpy.shutdown()
[vision_ai_node-12]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 130, in shutdown
[vision_ai_node-12]     _shutdown(context=context)
[vision_ai_node-12]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/utilities.py", line 58, in shutdown
[vision_ai_node-12]     return context.shutdown()
[vision_ai_node-12]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/context.py", line 102, in shutdown
[vision_ai_node-12]     self.__context.shutdown()
[vision_ai_node-12] rclpy._rclpy_pybind11.RCLError: failed to shutdown: rcl_shutdown already called on the given context, at ./src/rcl/init.c:241
[costmap_publisher-20] Traceback (most recent call last):
[costmap_publisher-20]   File "/userdata/dev_ws/install/object_tracker/lib/object_tracker/costmap_publisher", line 33, in <module>
[costmap_publisher-20]     sys.exit(load_entry_point('object-tracker==0.0.1', 'console_scripts', 'costmap_publisher')())
[costmap_publisher-20]   File "/userdata/dev_ws/install/object_tracker/lib/python3.10/site-packages/object_tracker/costmap_publisher.py", line 76, in main
[costmap_publisher-20]     rclpy.shutdown()
[costmap_publisher-20]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 130, in shutdown
[costmap_publisher-20]     _shutdown(context=context)
[costmap_publisher-20]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/utilities.py", line 58, in shutdown
[costmap_publisher-20]     return context.shutdown()
[costmap_publisher-20]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/context.py", line 102, in shutdown
[costmap_publisher-20]     self.__context.shutdown()
[costmap_publisher-20] rclpy._rclpy_pybind11.RCLError: failed to shutdown: rcl_shutdown already called on the given context, at ./src/rcl/init.c:241
[tracker_node-19] Traceback (most recent call last):
[tracker_node-19]   File "/userdata/dev_ws/install/object_tracker/lib/object_tracker/tracker_node", line 33, in <module>
[tracker_node-19]     sys.exit(load_entry_point('object-tracker==0.0.1', 'console_scripts', 'tracker_node')())
[tracker_node-19]   File "/userdata/dev_ws/install/object_tracker/lib/python3.10/site-packages/object_tracker/tracker_node.py", line 313, in main
[tracker_node-19]     rclpy.shutdown()
[tracker_node-19]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 130, in shutdown
[tracker_node-19]     _shutdown(context=context)
[tracker_node-19]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/utilities.py", line 58, in shutdown
[tracker_node-19]     return context.shutdown()
[tracker_node-19]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/context.py", line 102, in shutdown
[tracker_node-19]     self.__context.shutdown()
[tracker_node-19] rclpy._rclpy_pybind11.RCLError: failed to shutdown: rcl_shutdown already called on the given context, at ./src/rcl/init.c:241
[depth_detector-18] Traceback (most recent call last):
[depth_detector-18]   File "/userdata/dev_ws/install/object_tracker/lib/object_tracker/depth_detector", line 33, in <module>
[depth_detector-18]     sys.exit(load_entry_point('object-tracker==0.0.1', 'console_scripts', 'depth_detector')())
[depth_detector-18]   File "/userdata/dev_ws/install/object_tracker/lib/python3.10/site-packages/object_tracker/depth_detector.py", line 382, in main
[depth_detector-18]     rclpy.shutdown()
[depth_detector-18]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 130, in shutdown
[depth_detector-18]     _shutdown(context=context)
[depth_detector-18]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/utilities.py", line 58, in shutdown
[depth_detector-18]     return context.shutdown()
[depth_detector-18]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/context.py", line 102, in shutdown
[depth_detector-18]     self.__context.shutdown()
[depth_detector-18] rclpy._rclpy_pybind11.RCLError: failed to shutdown: rcl_shutdown already called on the given context, at ./src/rcl/init.c:241
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057560.225660567] [competition_master_stage3]: [TRAJ] Nav2 params snapshot: 31 keys
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057560.231413069] [competition_master_stage3]: [TRAJ] 摘要JSON已保存: /userdata/dev_ws/trajectory_20260703_134559_summary.json
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057560.239199487] [competition_master_stage3]: [TRAJ] 规划历史已保存: /userdata/dev_ws/trajectory_20260703_134559_plans.csv (75 次规划)
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783057560.260379826] [competition_master_stage3]: [TRAJ] costmap PGM已保存: /userdata/dev_ws/trajectory_20260703_134559_costmap.pgm
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[ERROR] [path_optimizer_node.py-22]: process has died [pid 22868, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/path_optimizer_node.py --ros-args -r __node:=path_optimizer_node --params-file /tmp/launch_params_duy1jdaj'].
[INFO] [competition_master_stage3.py-21]: process has finished cleanly [pid 22863]
[ERROR] [depth_detector-18]: process has died [pid 22850, exit code 1, cmd '/userdata/dev_ws/install/object_tracker/lib/object_tracker/depth_detector --ros-args -r __node:=depth_detector'].
[INFO] [aurora930_node-9]: process has finished cleanly [pid 22573]
[ERROR] [vision_ai_node-12]: process has died [pid 22579, exit code 1, cmd '/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node --ros-args -r __node:=vision_ai_node'].
[ERROR] [tracker_node-19]: process has died [pid 22852, exit code 1, cmd '/userdata/dev_ws/install/object_tracker/lib/object_tracker/tracker_node --ros-args -r __node:=tracker_node --params-file /tmp/launch_params_decrwi6d'].
[component_container_isolated-17] [INFO] [1783057562.466214926] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057562.466371218] [map_server]: Running Nav2 LifecycleNode rcl preshutdown (map_server)
[component_container_isolated-17] [INFO] [1783057562.466485218] [map_server]: Deactivating
[component_container_isolated-17] [INFO] [1783057562.466629968] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783057562.477216054] [map_server]: Cleaning up
[component_container_isolated-17] [INFO] [1783057562.477665929] [map_server]: Destroying bond (map_server) to lifecycle manager.
[ERROR] [component_container_isolated-17]: process[component_container_isolated-17] failed to terminate '5' seconds after receiving 'SIGINT', escalating to 'SIGTERM'
[INFO] [component_container_isolated-17]: sending signal 'SIGTERM' to process[component_container_isolated-17]
[component_container_isolated-17] [INFO] [1783057566.468483486] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [component_container_isolated-17]: process[component_container_isolated-17] failed to terminate '10.0' seconds after receiving 'SIGTERM', escalating to 'SIGKILL'
[INFO] [component_container_isolated-17]: sending signal 'SIGKILL' to process[component_container_isolated-17]
[ERROR] [component_container_isolated-17]: process has died [pid 22846, exit code -9, cmd '/opt/ros/humble/lib/rclcpp_components/component_container_isolated --ros-args --log-level info --ros-args -r __node:=nav2_container --params-file /tmp/launch_params_7mmwss9h --params-file /tmp/launch_params_ktg316pq -r /tf:=tf -r /tf_static:=tf_static'].
root@ubuntu:/userdata/dev_ws#
