root@ubuntu:/userdata/dev_ws# ros2 launch origincar_bringup stage3_bringup.launch.py
[INFO] [launch]: All log files can be found below /root/.ros/log/2026-06-28-17-44-01-483178-ubuntu-37133
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [origincar_base_node-1]: process started with pid [37147]
[INFO] [lslidar_driver_node-2]: process started with pid [37149]
[INFO] [robot_state_publisher-3]: process started with pid [37151]
[INFO] [imu_madgwick_filter.py-4]: process started with pid [37153]
[INFO] [bmi088_iio_bridge.py-5]: process started with pid [37155]
[INFO] [imu_madgwick_filter.py-6]: process started with pid [37157]
[INFO] [ekf_node-7]: process started with pid [37159]
[INFO] [static_transform_publisher-8]: process started with pid [37205]
[INFO] [aurora930_node-9]: process started with pid [37207]
[INFO] [qr_decoder-10]: process started with pid [37209]
[INFO] [qr_decision-11]: process started with pid [37211]
[INFO] [vision_ai_node-12]: process started with pid [37213]
[origincar_base_node-1] [INFO] [1782639842.143417245] [origincar_base]: origincar_base serial port opened
[lslidar_driver_node-2] [INFO] [1782639842.198004861] [lslidar_driver_node]: Lidar is N10
[lslidar_driver_node-2] [INFO] [1782639842.209849418] [lslidar_driver_node]: Initialised lslidar without error
[lslidar_driver_node-2] [INFO] [1782639842.210022127] [lslidar_driver_node]: Successfully initialize driver...
[robot_state_publisher-3] [INFO] [1782639842.185048135] [robot_state_publisher]: got segment base_footprint
[robot_state_publisher-3] [INFO] [1782639842.185426885] [robot_state_publisher]: got segment base_link
[robot_state_publisher-3] [INFO] [1782639842.185545302] [robot_state_publisher]: got segment gyro_link
[robot_state_publisher-3] [INFO] [1782639842.185613219] [robot_state_publisher]: got segment laser_link
[ekf_node-7] Both imu1_differential and imu1_relative were set to true. Using differential mode.
[static_transform_publisher-8] [INFO] [1782639842.400728218] [depth_camera_tf]: Spinning until stopped - publishing transform
[static_transform_publisher-8] translation: ('0.140000', '0.000000', '0.050000')
[static_transform_publisher-8] rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
[static_transform_publisher-8] from 'base_link' to 'depth_camera_link'
[aurora930_node-9] W0628 17:44:02.784319 37207 ros2_node.cc:35] hello aurora 900/930
[qr_decoder-10] [INFO] [1782639842.892020758] [qr_decoder_zbar]: QR decoder (ZBar) started: rgb=/aurora/rgb/image_raw, depth=/aurora/depth/image_raw, filter=on, range=[50, 4000]mm, min_qr_len=1, intrinsics: fx=421.3 fy=422.3 cx=320.3 cy=197.0
[aurora930_node-9] 2026-06-28 17:44:02.918 (   0.269s) [        992C4020] device_manager_impl.cc:89    INFO| hotplug has registed by user
[aurora930_node-9] device_count==========1
[aurora930_node-9] I0628 17:44:02.977300 37207 aurora900_ros2_device.cc:153] BOOT_ORDER_1::Found 1 deptrum device
[aurora930_node-9] I0628 17:44:02.977804 37207 aurora900_ros2_device.cc:162] BOOT_ORDER_1::No serial number provided: picking first device
[aurora930_node-9] 2026-06-28 17:44:02.977 (   0.328s) [        992C4020] device_manager_impl.cc:318   INFO| Device information:
[aurora930_node-9]      ir_pid:0x1930, rgb_pid:0x0
[aurora930_node-9]      serial number:HY400529001015314G00248
[aurora930_node-9] I0628 17:44:02.977970 37207 aurora900_ros2_device.cc:206] BOOT_ORDER_1::0:device start opening
[aurora930_node-9] 2026-06-28 17:44:02.980 (   0.330s) [        992C4020]   custom_usb_device.cc:101   INFO| bulk in endpoint addr:129
[aurora930_node-9] 2026-06-28 17:44:02.980 (   0.330s) [        992C4020]   custom_usb_device.cc:98    INFO| bulk out endpoint addr:2
[aurora930_node-9] 2026-06-28 17:44:03.012 (   0.362s) [        992C4020]deptrum_camera_aurora93:53    INFO| doe_broken:0 ito_support:1 crash_count:0 wdt_count:0 hard_reset_count:2 heart_boot_count:0 boot_total:121 last_crash_time:N
[aurora930_node-9] I0628 17:44:03.012571 37207 aurora900_ros2_device.cc:247] device supported frame_mode:
[aurora930_node-9] I0628 17:44:03.012676 37207 aurora900_ros2_device.cc:252] [0]:ir_mode:=13 kRes320x200Ir8Bit rgb_mode:=31 kRes320x200RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0628 17:44:03.012723 37207 aurora900_ros2_device.cc:252] [1]:ir_mode:=17 kRes480x300Depth16Bit rgb_mode:=32 kRes480x300RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0628 17:44:03.012758 37207 aurora900_ros2_device.cc:252] [2]:ir_mode:=20 kRes640x400Ir8Bit rgb_mode:=33 kRes640x400RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0628 17:44:03.012790 37207 aurora900_ros2_device.cc:266] current set mode ir_mode:20:kRes640x400Ir8Bit,rgb_mode:33:kRes640x400RgbYuv
[INFO] [map_server-13]: process started with pid [37308]
[INFO] [costmap_filter_info_server-14]: process started with pid [37310]
[INFO] [lifecycle_manager-15]: process started with pid [37319]
[aurora930_node-9] I0628 17:44:03.527514 37207 aurora900_ros2_device.cc:387] Switch Auto Exposure
[costmap_filter_info_server-14] [INFO] [1782639843.587572908] [costmap_filter_info_server]: This is costmap filter info publisher
[aurora930_node-9] 2026-06-28 17:44:03.588 (   0.938s) [        992C4020]      aurora900_impl.cc:1106  INFO| SetHeartbeat user set heartbeat enable: 0
[lifecycle_manager-15] [INFO] [1782639843.653001705] [lifecycle_manager_keepout]: Creating
[lifecycle_manager-15] [INFO] [1782639843.708700655] [lifecycle_manager_keepout]: Creating and initializing lifecycle service clients
[map_server-13] [INFO] [1782639843.722353882] [keepout_mask_server]:
[map_server-13]         keepout_mask_server lifecycle node launched.
[map_server-13]         Waiting on external lifecycle transitions to activate
[map_server-13]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[map_server-13] [INFO] [1782639843.722920633] [keepout_mask_server]: Creating
[costmap_filter_info_server-14] [INFO] [1782639843.729215808] [keepout_filter_info_server]:
[costmap_filter_info_server-14]         keepout_filter_info_server lifecycle node launched.
[costmap_filter_info_server-14]         Waiting on external lifecycle transitions to activate
[costmap_filter_info_server-14]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[lifecycle_manager-15] [INFO] [1782639843.767020109] [lifecycle_manager_keepout]: Starting managed nodes bringup...
[lifecycle_manager-15] [INFO] [1782639843.767952235] [lifecycle_manager_keepout]: Configuring keepout_mask_server
[map_server-13] [INFO] [1782639843.785337175] [keepout_mask_server]: Configuring
[map_server-13] [INFO] [1782639843.785622926] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.yaml
[map_server-13] [INFO] [1782639843.786664552] [map_io]: resolution: 0.05
[map_server-13] [INFO] [1782639843.787979887] [map_io]: origin[0]: -2.65
[map_server-13] [INFO] [1782639843.788041721] [map_io]: origin[1]: -4.5
[map_server-13] [INFO] [1782639843.788071637] [map_io]: origin[2]: 0
[map_server-13] [INFO] [1782639843.788102637] [map_io]: free_thresh: 0.5
[map_server-13] [INFO] [1782639843.788131596] [map_io]: occupied_thresh: 0.5
[map_server-13] [INFO] [1782639843.788197596] [map_io]: mode: scale
[map_server-13] [INFO] [1782639843.788233221] [map_io]: negate: 0
[map_server-13] [INFO] [1782639843.790195432] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm
[map_server-13] [INFO] [1782639843.813958464] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm: 163 X 141 map @ 0.05 m/cell
[lifecycle_manager-15] [INFO] [1782639843.841380751] [lifecycle_manager_keepout]: Configuring keepout_filter_info_server
[costmap_filter_info_server-14] [INFO] [1782639843.842624128] [keepout_filter_info_server]: Configuring
[lifecycle_manager-15] [INFO] [1782639843.864356324] [lifecycle_manager_keepout]: Activating keepout_mask_server
[map_server-13] [INFO] [1782639843.865184408] [keepout_mask_server]: Activating
[map_server-13] [INFO] [1782639843.865558826] [keepout_mask_server]: Creating bond (keepout_mask_server) to lifecycle manager.
[lifecycle_manager-15] [INFO] [1782639843.973554347] [lifecycle_manager_keepout]: Server keepout_mask_server connected with bond.
[lifecycle_manager-15] [INFO] [1782639843.973726889] [lifecycle_manager_keepout]: Activating keepout_filter_info_server
[costmap_filter_info_server-14] [INFO] [1782639843.974656306] [keepout_filter_info_server]: Activating
[costmap_filter_info_server-14] [INFO] [1782639843.974868807] [keepout_filter_info_server]: Creating bond (keepout_filter_info_server) to lifecycle manager.
[bmi088_iio_bridge.py-5] [INFO] [1782639843.981367857] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1782639843.984355695] [bmi088_iio_bridge]:   DIAGNOSTIC: Scanning IIO devices under /sys/bus/iio/devices/
[bmi088_iio_bridge.py-5] [INFO] [1782639843.987395407] [bmi088_iio_bridge]:   Equivalent to: ls /sys/bus/iio/devices/*/name
[bmi088_iio_bridge.py-5] [INFO] [1782639843.990283661] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1782639843.992926456] [bmi088_iio_bridge]:   iio:device0/name = "34190000.adc"
[bmi088_iio_bridge.py-5] [INFO] [1782639843.995300793] [bmi088_iio_bridge]:   iio:device1/name = "bmi08x"
[bmi088_iio_bridge.py-5] [INFO] [1782639843.997658171] [bmi088_iio_bridge]:   trigger0/name = "34190000.adc-dev0"
[bmi088_iio_bridge.py-5] [INFO] [1782639844.000061216] [bmi088_iio_bridge]:   Total IIO devices found: 3
[bmi088_iio_bridge.py-5] [INFO] [1782639844.002650969] [bmi088_iio_bridge]:   BMI088 kernel module APPEARS LOADED: 1 BMI device(s) detected
[bmi088_iio_bridge.py-5] [INFO] [1782639844.005208723] [bmi088_iio_bridge]:   BMI device names: ['bmi08x']
[imu_madgwick_filter.py-6] [INFO] [1782639844.006003974] [imu_madgwick_bmi088]: [imu_madgwick] init: beta=0.0030, gyro_noise=0.0002, accel_noise=0.010
[bmi088_iio_bridge.py-5] [INFO] [1782639844.008307435] [bmi088_iio_bridge]:   gyro:  /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_anglvel is_si=False scale_override=0.00053
[aurora930_node-9] I0628 17:44:04.008658 37207 aurora900_ros2_device.cc:304] BOOT_ORDER_1::Device information:
[aurora930_node-9] I0628 17:44:04.008821 37207 aurora900_ros2_device.cc:305]     sdk version: 1.1.22
[aurora930_node-9] I0628 17:44:04.008862 37207 aurora900_ros2_device.cc:306]     device name: Aurora 930
[aurora930_node-9] I0628 17:44:04.008889 37207 aurora900_ros2_device.cc:307]     serial number: HY400529001015314G00248
[aurora930_node-9] I0628 17:44:04.008914 37207 aurora900_ros2_device.cc:308]     firmware version: 1.7.2
[aurora930_node-9] I0628 17:44:04.008966 37207 camera_parameters.cc:134] BOOT_ORDER_1::Camera Parameters:
[aurora930_node-9] I0628 17:44:04.008996 37207 camera_parameters.cc:135] BOOT_ORDER_1::  Ir Intrinsics:
[aurora930_node-9] I0628 17:44:04.009022 37207 camera_parameters.cc:146]                 Resolution:
[aurora930_node-9] I0628 17:44:04.009047 37207 camera_parameters.cc:147]                         Rows:400
[aurora930_node-9] I0628 17:44:04.009073 37207 camera_parameters.cc:148]                         Cols:640
[aurora930_node-9] I0628 17:44:04.009099 37207 camera_parameters.cc:149]                 Intrinsics:
[aurora930_node-9] I0628 17:44:04.009122 37207 camera_parameters.cc:150]                         fx: 421.307
[aurora930_node-9] I0628 17:44:04.009219 37207 camera_parameters.cc:151]                         fy: 422.254
[aurora930_node-9] I0628 17:44:04.009253 37207 camera_parameters.cc:152]                         cx: 320.27
[aurora930_node-9] I0628 17:44:04.009286 37207 camera_parameters.cc:153]                         cy: 197.01
[aurora930_node-9] I0628 17:44:04.009318 37207 camera_parameters.cc:154]                         k1: 0.0606853
[aurora930_node-9] I0628 17:44:04.009351 37207 camera_parameters.cc:155]                         k2: -0.10961
[aurora930_node-9] I0628 17:44:04.009382 37207 camera_parameters.cc:156]                         p1: 0.00126689
[aurora930_node-9] I0628 17:44:04.009413 37207 camera_parameters.cc:157]                         p2: -0.00120539
[aurora930_node-9] I0628 17:44:04.009445 37207 camera_parameters.cc:158]                         k3: 0.0522281
[aurora930_node-9] I0628 17:44:04.009476 37207 camera_parameters.cc:138] BOOT_ORDER_1::  Rgb Intrinsics:
[aurora930_node-9] I0628 17:44:04.009502 37207 camera_parameters.cc:146]                 Resolution:
[aurora930_node-9] I0628 17:44:04.009527 37207 camera_parameters.cc:147]                         Rows:400
[aurora930_node-9] I0628 17:44:04.009552 37207 camera_parameters.cc:148]                         Cols:640
[aurora930_node-9] I0628 17:44:04.009577 37207 camera_parameters.cc:149]                 Intrinsics:
[aurora930_node-9] I0628 17:44:04.009629 37207 camera_parameters.cc:150]                         fx: 416.49
[aurora930_node-9] I0628 17:44:04.009672 37207 camera_parameters.cc:151]                         fy: 417.383
[aurora930_node-9] I0628 17:44:04.009706 37207 camera_parameters.cc:152]                         cx: 316.832
[aurora930_node-9] I0628 17:44:04.009737 37207 camera_parameters.cc:153]                         cy: 188.753
[aurora930_node-9] I0628 17:44:04.009768 37207 camera_parameters.cc:154]                         k1: 0.00611878
[aurora930_node-9] I0628 17:44:04.009799 37207 camera_parameters.cc:155]                         k2: -0.0490436
[aurora930_node-9] I0628 17:44:04.009891 37207 camera_parameters.cc:156]                         p1: 0.000399548
[aurora930_node-9] I0628 17:44:04.009925 37207 camera_parameters.cc:157]                         p2: 0.000563892
[aurora930_node-9] I0628 17:44:04.009958 37207 camera_parameters.cc:158]                         k3: 0.0308458
[aurora930_node-9] I0628 17:44:04.009989 37207 camera_parameters.cc:141] BOOT_ORDER_1::  Ir to Rgb Extrinsic:
[aurora930_node-9] I0628 17:44:04.010022 37207 camera_parameters.cc:162]                 Extrinsics:
[aurora930_node-9] I0628 17:44:04.010048 37207 camera_parameters.cc:163]                         Rotation[0]: 0.999973, 0.00724076, -0.00112023
[aurora930_node-9] I0628 17:44:04.010085 37207 camera_parameters.cc:165]                         Rotation[1]: -0.00724006, 0.999973, 0.000633162
[aurora930_node-9] I0628 17:44:04.010129 37207 camera_parameters.cc:167]                         Rotation[2]: 0.00112478, -0.000625033, 0.999999
[aurora930_node-9] I0628 17:44:04.010223 37207 camera_parameters.cc:169]                         Translation: -9.88662, 0.117748, 0.603513
[aurora930_node-9] 2026-06-28 17:44:04.010 (   1.361s) [        992C4020]      aurora900_impl.cc:578   INFO| stream_mask_:0, rgb_stream_count_:1
[bmi088_iio_bridge.py-5] [INFO] [1782639844.011361939] [bmi088_iio_bridge]:   accel: /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_accel is_si=False scale_override=0.00341
[imu_madgwick_filter.py-4] [INFO] [1782639844.069267268] [imu_madgwick_filter]: [imu_madgwick] init: beta=0.0330, gyro_noise=0.0010, accel_noise=0.050
[imu_madgwick_filter.py-4] [INFO] [1782639844.075082734] [imu_madgwick_filter]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-4] [INFO] [1782639844.077704654] [imu_madgwick_filter]: [imu_madgwick] accel init: roll=-1.5deg, pitch=0.2deg
[lifecycle_manager-15] [INFO] [1782639844.086775083] [lifecycle_manager_keepout]: Server keepout_filter_info_server connected with bond.
[lifecycle_manager-15] [INFO] [1782639844.086971125] [lifecycle_manager_keepout]: Managed nodes are active
[lifecycle_manager-15] [INFO] [1782639844.087048083] [lifecycle_manager_keepout]: Creating bond timer...
[bmi088_iio_bridge.py-5] [INFO] [1782639844.120388337] [bmi088_iio_bridge]: BMI088 IIO Bridge 启动 @ 100Hz -> /imu_data  [OK]
[imu_madgwick_filter.py-6] [INFO] [1782639844.148925792] [imu_madgwick_bmi088]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-6] [INFO] [1782639844.151613254] [imu_madgwick_bmi088]: [imu_madgwick] accel init: roll=-2.3deg, pitch=-3.4deg
[qr_decision-11] [INFO] [1782639844.275164296] [qr_decision]: qr_decision started: cooldown=3.0s, awaiting /sign from qr_decoder
[aurora930_node-9] 2026-06-28 17:44:04.336 (   1.686s) [        699E37E0]deptrum_camera_aurora93:407    ERR| recv first frame time is 1782639844336
[lslidar_driver_node-2] port = /dev/ttyACM1, baud_rate = 230400
[lslidar_driver_node-2] open_port /dev/ttyACM1 OK !
[vision_ai_node-12] [INFO] [1782639848.013708013] [vision_ai_node]: 成功加载配置文件: /userdata/dev_ws/install/racing_vision_ai/share/racing_vision_ai/config/vision_ai_config.yaml
[vision_ai_node-12] [INFO] [1782639848.375461626] [vision_ai_node]: Volcengine Ark client initialized successfully
[vision_ai_node-12] [INFO] [1782639848.395270944] [vision_ai_node]: Vision AI Node initialized
[vision_ai_node-12] [INFO] [1782639848.397468447] [vision_ai_node]: Waiting for sign4return=100 signal...
[vision_ai_node-12] [INFO] [1782639848.399639450] [vision_ai_node]: Results will be published to vlm_result
[bmi088_iio_bridge.py-5] [INFO] [1782639849.581184586] [bmi088_iio_bridge]:   gyro bias calibrated: (0.002480, 0.001431, -0.002671) rad/s
[INFO] [component_container_isolated-16]: process started with pid [37466]
[INFO] [competition_master_stage3.py-17]: process started with pid [37468]
[INFO] [rviz2-18]: process started with pid [37470]
[component_container_isolated-16] [INFO] [1782639850.441578204] [nav2_container]: Load Library: /opt/ros/humble/lib/libcontroller_server_core.so
[component_container_isolated-16] [INFO] [1782639850.470832576] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-16] [INFO] [1782639850.471061868] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-16] [INFO] [1782639850.541721255] [controller_server]:
[component_container_isolated-16]       controller_server lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782639850.567430123] [controller_server]: Creating controller server
[component_container_isolated-16] [INFO] [1782639850.649398859] [local_costmap.local_costmap]:
[component_container_isolated-16]       local_costmap lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782639850.652601030] [local_costmap.local_costmap]: Creating Costmap
[component_container_isolated-16] [INFO] [1782639850.670042636] [nav2_container]: Load Library: /opt/ros/humble/lib/libmap_server_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/controller_server' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782639850.730648676] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::CostmapFilterInfoServer>
[component_container_isolated-16] [INFO] [1782639850.730815052] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapSaver>
[component_container_isolated-16] [INFO] [1782639850.730905760] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-16] [INFO] [1782639850.731048469] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-16] [INFO] [1782639850.798643101] [map_server]:
[component_container_isolated-16]       map_server lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/map_server' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782639850.798947185] [map_server]: Creating
[component_container_isolated-16] [INFO] [1782639850.805987445] [nav2_container]: Load Library: /opt/ros/humble/lib/libsmoother_server_core.so
[component_container_isolated-16] [INFO] [1782639850.812329037] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-16] [INFO] [1782639850.812502328] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-16] [INFO] [1782639850.896036608] [smoother_server]:
[component_container_isolated-16]       smoother_server lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782639850.905690662] [smoother_server]: Creating smoother server
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/smoother_server' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782639850.911995296] [nav2_container]: Load Library: /opt/ros/humble/lib/libamcl_core.so
[component_container_isolated-16] [INFO] [1782639850.920784849] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-16] [INFO] [1782639850.920980475] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-16] [INFO] [1782639851.001383250] [amcl]:
[component_container_isolated-16]       amcl lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782639851.003482127] [amcl]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/amcl' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782639851.122683330] [nav2_container]: Load Library: /opt/ros/humble/lib/libplanner_server_core.so
[component_container_isolated-16] [INFO] [1782639851.126360751] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-16] [INFO] [1782639851.126523877] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-16] [INFO] [1782639851.183976787] [planner_server]:
[component_container_isolated-16]       planner_server lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782639851.193235050] [planner_server]: Creating
[component_container_isolated-16] [INFO] [1782639851.286318050] [global_costmap.global_costmap]:
[component_container_isolated-16]       global_costmap lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782639851.289837763] [global_costmap.global_costmap]: Creating Costmap
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/planner_server' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782639851.307495412] [nav2_container]: Load Library: /opt/ros/humble/lib/libnav2_lifecycle_manager_core.so
[component_container_isolated-16] [INFO] [1782639851.310892625] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-16] [INFO] [1782639851.311134625] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-16] [INFO] [1782639851.384586432] [lifecycle_manager_localization]: Creating
[component_container_isolated-16] [INFO] [1782639851.412855762] [nav2_container]: Load Library: /opt/ros/humble/lib/libbehavior_server_core.so
[component_container_isolated-16] [INFO] [1782639851.418445020] [lifecycle_manager_localization]: Creating and initializing lifecycle service clients
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_localization' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782639851.445281681] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-16] [INFO] [1782639851.449370270] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-16] [INFO] [1782639851.485342068] [lifecycle_manager_localization]: Starting managed nodes bringup...
[component_container_isolated-16] [INFO] [1782639851.492370161] [lifecycle_manager_localization]: Configuring map_server
[component_container_isolated-16] [INFO] [1782639851.494100205] [map_server]: Configuring
[component_container_isolated-16] [INFO] [1782639851.494425247] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.yaml
[component_container_isolated-16] [INFO] [1782639851.497998294] [map_io]: resolution: 0.05
[component_container_isolated-16] [INFO] [1782639851.498123544] [map_io]: origin[0]: -2.65
[component_container_isolated-16] [INFO] [1782639851.498156794] [map_io]: origin[1]: -4.5
[component_container_isolated-16] [INFO] [1782639851.498185085] [map_io]: origin[2]: 0
[component_container_isolated-16] [INFO] [1782639851.498214377] [map_io]: free_thresh: 0.25
[component_container_isolated-16] [INFO] [1782639851.498243002] [map_io]: occupied_thresh: 0.65
[component_container_isolated-16] [INFO] [1782639851.498288294] [map_io]: mode: trinary
[component_container_isolated-16] [INFO] [1782639851.498319377] [map_io]: negate: 0
[component_container_isolated-16] [INFO] [1782639851.499077878] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm
[component_container_isolated-16] [INFO] [1782639851.529244586] [behavior_server]:
[component_container_isolated-16]       behavior_server lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782639851.540196392] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm: 163 X 141 map @ 0.05 m/cell
[component_container_isolated-16] [INFO] [1782639851.566517552] [lifecycle_manager_localization]: Configuring amcl
[component_container_isolated-16] [INFO] [1782639851.567520762] [amcl]: Configuring
[component_container_isolated-16] [INFO] [1782639851.568006013] [amcl]: initTransforms
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/behavior_server' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782639851.592410379] [nav2_container]: Load Library: /opt/ros/humble/lib/libbt_navigator_core.so
[component_container_isolated-16] [INFO] [1782639851.602400601] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-16] [INFO] [1782639851.602587018] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-16] [INFO] [1782639851.659344094] [amcl]: initPubSub
[component_container_isolated-16] [INFO] [1782639851.692322930] [amcl]: Subscribed to map topic.
[component_container_isolated-16] [INFO] [1782639851.729256772] [lifecycle_manager_localization]: Activating map_server
[component_container_isolated-16] [INFO] [1782639851.730111106] [map_server]: Activating
[component_container_isolated-16] [INFO] [1782639851.730526315] [map_server]: Creating bond (map_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639851.730705440] [amcl]: Received a 163 X 141 map @ 0.050 m/pix
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/bt_navigator' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782639851.738035617] [bt_navigator]:
[component_container_isolated-16]       bt_navigator lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782639851.738341617] [bt_navigator]: Creating
[component_container_isolated-16] [INFO] [1782639851.763700401] [nav2_container]: Load Library: /opt/ros/humble/lib/libwaypoint_follower_core.so
[component_container_isolated-16] [INFO] [1782639851.768043199] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-16] [INFO] [1782639851.768224741] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-16] [INFO] [1782639851.841267672] [lifecycle_manager_localization]: Server map_server connected with bond.
[component_container_isolated-16] [INFO] [1782639851.841455756] [lifecycle_manager_localization]: Activating amcl
[component_container_isolated-16] [INFO] [1782639851.842476924] [amcl]: Activating
[component_container_isolated-16] [INFO] [1782639851.842731966] [amcl]: initialPoseReceived
[component_container_isolated-16] [INFO] [1782639851.843624842] [amcl]: Setting pose (1782639851.843615): -1.985 -0.014 0.262
[component_container_isolated-16] [INFO] [1782639851.845597428] [amcl]: Creating bond (amcl) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639851.877746763] [waypoint_follower]:
[component_container_isolated-16]       waypoint_follower lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782639851.882581936] [waypoint_follower]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/waypoint_follower' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782639851.904716133] [nav2_container]: Load Library: /opt/ros/humble/lib/libvelocity_smoother_core.so
[component_container_isolated-16] [INFO] [1782639851.908241971] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-16] [INFO] [1782639851.908610597] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-16] [INFO] [1782639851.911188433] [amcl]: createLaserObject
[component_container_isolated-16] [INFO] [1782639851.966840425] [lifecycle_manager_localization]: Server amcl connected with bond.
[component_container_isolated-16] [INFO] [1782639851.967027009] [lifecycle_manager_localization]: Managed nodes are active
[component_container_isolated-16] [INFO] [1782639851.967146134] [lifecycle_manager_localization]: Creating bond timer...
[component_container_isolated-16] [INFO] [1782639852.011727235] [velocity_smoother]:
[component_container_isolated-16]       velocity_smoother lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/velocity_smoother' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782639852.029595009] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-16] [INFO] [1782639852.029818593] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-16] [INFO] [1782639852.116204126] [lifecycle_manager_navigation]: Creating
[component_container_isolated-16] [INFO] [1782639852.138261072] [lifecycle_manager_navigation]: Creating and initializing lifecycle service clients
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_navigation' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782639852.211999922] [lifecycle_manager_navigation]: Starting managed nodes bringup...
[component_container_isolated-16] [INFO] [1782639852.212749964] [lifecycle_manager_navigation]: Configuring controller_server
[component_container_isolated-16] [INFO] [1782639852.213672466] [controller_server]: Configuring controller interface
[component_container_isolated-16] [INFO] [1782639852.214676175] [controller_server]: getting goal checker plugins..
[component_container_isolated-16] [INFO] [1782639852.215899177] [controller_server]: Controller frequency set to 10.0000Hz
[component_container_isolated-16] [INFO] [1782639852.216204636] [local_costmap.local_costmap]: Configuring
[component_container_isolated-16] [INFO] [1782639852.249578889] [local_costmap.local_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-16] [INFO] [1782639852.289761985] [local_costmap.local_costmap]: Subscribed to Topics: scan aurora_points
[component_container_isolated-16] [INFO] [1782639852.405589349] [local_costmap.local_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-16] [INFO] [1782639852.409836605] [local_costmap.local_costmap]: Using plugin "keepout_filter"
[component_container_isolated-16] [INFO] [1782639852.437319225] [local_costmap.local_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-16] [INFO] [1782639852.437513100] [local_costmap.local_costmap]: Using plugin "inflation_layer"
[component_container_isolated-16] [INFO] [1782639852.454985957] [local_costmap.local_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-16] [INFO] [1782639852.508436071] [controller_server]: Created progress_checker : progress_checker of type nav2_controller::SimpleProgressChecker
[component_container_isolated-16] [INFO] [1782639852.515143246] [controller_server]: Created goal checker : goal_checker of type nav2_controller::SimpleGoalChecker
[component_container_isolated-16] [INFO] [1782639852.526680345] [controller_server]: Controller Server has goal_checker  goal checkers available.
[component_container_isolated-16] [INFO] [1782639852.532142936] [controller_server]: Created controller : FollowPath of type nav2_regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-16] [INFO] [1782639852.614011004] [controller_server]: Controller Server has FollowPath  controllers available.
[component_container_isolated-16] [INFO] [1782639852.671158748] [lifecycle_manager_navigation]: Configuring smoother_server
[component_container_isolated-16] [INFO] [1782639852.672203208] [smoother_server]: Configuring smoother server
[component_container_isolated-16] [INFO] [1782639852.741947218] [smoother_server]: Created smoother : SmoothPath of type nav2_constrained_smoother/ConstrainedSmoother
[component_container_isolated-16] [INFO] [1782639852.808615058] [smoother_server]: Smoother Server has SmoothPath  smoothers available.
[component_container_isolated-16] [INFO] [1782639852.851911741] [lifecycle_manager_navigation]: Configuring planner_server
[component_container_isolated-16] [INFO] [1782639852.854248286] [planner_server]: Configuring
[component_container_isolated-16] [INFO] [1782639852.854924745] [global_costmap.global_costmap]: Configuring
[component_container_isolated-16] [INFO] [1782639852.888312415] [global_costmap.global_costmap]: Using plugin "static_layer"
[component_container_isolated-16] [INFO] [1782639852.900754890] [global_costmap.global_costmap]: Subscribing to the map topic (/map) with transient local durability
[component_container_isolated-16] [INFO] [1782639852.905397063] [global_costmap.global_costmap]: Initialized plugin "static_layer"
[component_container_isolated-16] [INFO] [1782639852.905567772] [global_costmap.global_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-16] [INFO] [1782639852.927832010] [global_costmap.global_costmap]: Subscribed to Topics: scan aurora_points
[component_container_isolated-16] [INFO] [1782639853.017562089] [global_costmap.global_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-16] [INFO] [1782639853.017751590] [global_costmap.global_costmap]: Using plugin "keepout_filter"
[component_container_isolated-16] [INFO] [1782639853.030796524] [global_costmap.global_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-16] [INFO] [1782639853.031008566] [global_costmap.global_costmap]: Using plugin "inflation_layer"
[component_container_isolated-16] [INFO] [1782639853.041819914] [global_costmap.global_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-16] [INFO] [1782639853.086535224] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 163 X 141 at 0.050000 m/pix
[competition_master_stage3.py-17] [INFO] [1782639853.093060899] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-17] [INFO] [1782639853.096396820] [competition_master_stage3]: === [Stage 3] 总控节点初始化 ===
[competition_master_stage3.py-17] [INFO] [1782639853.099584575] [competition_master_stage3]:   QR点:    (0.41, -3.17, yaw=0.00)
[competition_master_stage3.py-17] [INFO] [1782639853.102462829] [competition_master_stage3]:   通道入口: (0.38, -1.10, yaw=0.00)
[competition_master_stage3.py-17] [INFO] [1782639853.105219291] [competition_master_stage3]:   P点:     (-1.99, -0.01, yaw=0.26)
[competition_master_stage3.py-17] [INFO] [1782639853.108202003] [competition_master_stage3]:   cruise_cw: 3 路点 → VLM=(3.01, -1.16)
[competition_master_stage3.py-17] [INFO] [1782639853.111315799] [competition_master_stage3]:   cruise_ccw: 4 路点 → VLM=(2.17, 0.69)
[component_container_isolated-16] [INFO] [1782639853.114059011] [planner_server]: Created global planner plugin GridBased of type nav2_smac_planner/SmacPlannerHybrid
[competition_master_stage3.py-17] [INFO] [1782639853.114322886] [competition_master_stage3]:   超时: total=180.0s QR=90.0s entry=60.0s cruise=180.0s vlm=30.0s return=120.0s
[component_container_isolated-16] [INFO] [1782639853.114237928] [planner_server]: Configuring GridBased of type SmacPlannerHybrid
[competition_master_stage3.py-17] [INFO] [1782639853.117141598] [competition_master_stage3]:   回退QR方向: 逆时针
[competition_master_stage3.py-17] [INFO] [1782639853.120330353] [competition_master_stage3]:   VLM结果话题: vlm_result
[competition_master_stage3.py-17] [INFO] [1782639853.123407190] [competition_master_stage3]: ============================================================
[component_container_isolated-16] [INFO] [1782639853.149037808] [planner_server]: Even sized heuristic lookup table size set 200.000000, increasing size by 1 to make odd
[rviz2-18] [INFO] [1782639853.383988582] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-18] [INFO] [1782639853.384762625] [rviz2]: OpenGl version: 4.5 (GLSL 4.5)
[rviz2-18] [INFO] [1782639853.688576575] [rviz2]: Stereo is NOT SUPPORTED
[imu_madgwick_filter.py-6] [INFO] [1782639853.864445145] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=462 q_w=0.9993 angle=4.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782639853.938587578] [imu_madgwick_filter]: [imu_madgwick ->] msgs=200 q_w=0.9965 angle=9.6deg beta=0.0330
[rviz2-18] [INFO] [1782639855.985561122] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[rviz2-18] [ERROR] [1782639856.352127739] [rviz2]: Vertex Program:rviz/glsl120/indexed_8bit_image.vert Fragment Program:rviz/glsl120/indexed_8bit_image.frag GLSL link result :
[rviz2-18] active samplers with a different type refer to the same texture image unit
[qr_decoder-10] [INFO] [1782639860.568114854] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=200 last_qr_frame=-1 gap=-1 frames rejects=0
[imu_madgwick_filter.py-6] [INFO] [1782639863.864509059] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1021 q_w=0.9993 angle=4.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782639863.938320824] [imu_madgwick_filter]: [imu_madgwick ->] msgs=399 q_w=0.9861 angle=19.1deg beta=0.0330
[component_container_isolated-16] Reallocing temp weights 301 - 60
[component_container_isolated-16] [INFO] [1782639869.028138872] [planner_server]: Configured plugin GridBased of type SmacPlannerHybrid with maximum iterations 2027, max on approach iterations 300, and not allowing unknown traversal. Tolerance 0.50.Using motion model: Reeds-Shepp.
[component_container_isolated-16] [INFO] [1782639869.028377498] [planner_server]: Planner Server has GridBased  planners available.
[component_container_isolated-16] [INFO] [1782639869.084641531] [lifecycle_manager_navigation]: Configuring behavior_server
[component_container_isolated-16] [INFO] [1782639869.085744991] [behavior_server]: Configuring
[component_container_isolated-16] [INFO] [1782639869.125368919] [behavior_server]: Creating behavior plugin spin of type nav2_behaviors/Spin
[component_container_isolated-16] [INFO] [1782639869.129312507] [behavior_server]: Configuring spin
[component_container_isolated-16] [INFO] [1782639869.173092982] [behavior_server]: Creating behavior plugin backup of type nav2_behaviors/BackUp
[component_container_isolated-16] [INFO] [1782639869.176872987] [behavior_server]: Configuring backup
[component_container_isolated-16] [INFO] [1782639869.225405677] [behavior_server]: Creating behavior plugin drive_on_heading of type nav2_behaviors/DriveOnHeading
[component_container_isolated-16] [INFO] [1782639869.229683849] [behavior_server]: Configuring drive_on_heading
[component_container_isolated-16] [INFO] [1782639869.269858736] [behavior_server]: Creating behavior plugin wait of type nav2_behaviors/Wait
[component_container_isolated-16] [INFO] [1782639869.274098492] [behavior_server]: Configuring wait
[component_container_isolated-16] [INFO] [1782639869.302114863] [lifecycle_manager_navigation]: Configuring bt_navigator
[component_container_isolated-16] [INFO] [1782639869.303122447] [bt_navigator]: Configuring
[competition_master_stage3.py-17] [INFO] [1782639869.396132821] [competition_master_stage3]: [DIAG] state=INIT pos=(-1.99,-0.02) yaw=20deg cmd=(vx=0.00 wz=0.00) elapsed=0.0s cpuFreq=1500MHz cpuT=77C cpu=88% mem=17%
[competition_master_stage3.py-17] [INFO] [1782639869.656597877] [competition_master_stage3]: [LAUNCH] 发车阶段: 16.8s
[competition_master_stage3.py-17] [INFO] [1782639869.676259653] [competition_master_stage3]: >>> 系统就绪, 开始 Stage 3 导航
[competition_master_stage3.py-17] [INFO] [1782639869.690491922] [competition_master_stage3]: [BAG] 录制开始: stage3_20260628_174429
[competition_master_stage3.py-17] [INFO] [1782639869.696001888] [competition_master_stage3]: [状态机] INIT → NAV_TO_QR
[competition_master_stage3.py-17] [INFO] [1782639869.705726109] [competition_master_stage3]: [DIAG] nav目标距离: 3.96m, robot=(-1.99,-0.02) → target=(0.41,-3.17)
[competition_master_stage3.py-17] [INFO] [1782639869.709540364] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-16] [INFO] [1782639869.748097207] [lifecycle_manager_navigation]: Configuring waypoint_follower
[component_container_isolated-16] [INFO] [1782639869.749299709] [waypoint_follower]: Configuring
[competition_master_stage3.py-17] [WARN] [1782639869.765517356] [competition_master_stage3]: 导航目标被拒绝, 3s 后重试...
[component_container_isolated-16] [INFO] [1782639869.844071919] [waypoint_follower]: Created waypoint_task_executor : wait_at_waypoint of type nav2_waypoint_follower::WaitAtWaypoint
[component_container_isolated-16] [INFO] [1782639869.852773055] [lifecycle_manager_navigation]: Configuring velocity_smoother
[component_container_isolated-16] [INFO] [1782639869.854293891] [velocity_smoother]: Configuring velocity smoother
[component_container_isolated-16] [INFO] [1782639869.883765680] [lifecycle_manager_navigation]: Activating controller_server
[component_container_isolated-16] [INFO] [1782639869.884657181] [controller_server]: Activating
[component_container_isolated-16] [INFO] [1782639869.884931765] [local_costmap.local_costmap]: Activating
[component_container_isolated-16] [INFO] [1782639869.885097348] [local_costmap.local_costmap]: Checking transform
[component_container_isolated-16] [INFO] [1782639869.885524516] [local_costmap.local_costmap]: start
[component_container_isolated-16] [INFO] [1782639869.905440334] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782639869.914062345] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782639869.914254804] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782639870.034428089] [local_costmap.local_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[component_container_isolated-16] [INFO] [1782639870.114015279] [controller_server]: Activating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-16] [INFO] [1782639870.114304196] [controller_server]: Creating bond (controller_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639870.241427865] [lifecycle_manager_navigation]: Server controller_server connected with bond.
[component_container_isolated-16] [INFO] [1782639870.241665824] [lifecycle_manager_navigation]: Activating smoother_server
[component_container_isolated-16] [INFO] [1782639870.242728283] [smoother_server]: Activating
[component_container_isolated-16] [INFO] [1782639870.242958742] [smoother_server]: Activating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-16] [INFO] [1782639870.243052617] [smoother_server]: Creating bond (smoother_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639870.365844697] [lifecycle_manager_navigation]: Server smoother_server connected with bond.
[component_container_isolated-16] [INFO] [1782639870.366004406] [lifecycle_manager_navigation]: Activating planner_server
[component_container_isolated-16] [INFO] [1782639870.367342408] [planner_server]: Activating
[component_container_isolated-16] [INFO] [1782639870.367657825] [global_costmap.global_costmap]: Activating
[component_container_isolated-16] [INFO] [1782639870.367747033] [global_costmap.global_costmap]: Checking transform
[component_container_isolated-16] [INFO] [1782639870.368033200] [global_costmap.global_costmap]: start
[component_container_isolated-16] [INFO] [1782639870.384338764] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782639870.392689275] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782639870.392866317] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782639870.398901908] [global_costmap.global_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[rviz2-18] [INFO] [1782639870.721762339] [rviz2]: Trying to create a map of size 60 x 60 using 1 swatches
[competition_master_stage3.py-17] [INFO] [1782639870.945940512] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.02,-0.03) yaw=21deg cmd=(vx=0.00 wz=0.00) elapsed=1.2s cpuFreq=1500MHz cpuT=78C cpu=75% mem=18%
[component_container_isolated-16] [INFO] [1782639871.391509147] [planner_server]: Activating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-16] [INFO] [1782639871.399946492] [planner_server]: Creating bond (planner_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639871.523568448] [lifecycle_manager_navigation]: Server planner_server connected with bond.
[component_container_isolated-16] [INFO] [1782639871.523732574] [lifecycle_manager_navigation]: Activating behavior_server
[component_container_isolated-16] [INFO] [1782639871.525129367] [behavior_server]: Activating
[component_container_isolated-16] [INFO] [1782639871.525263659] [behavior_server]: Activating spin
[component_container_isolated-16] [INFO] [1782639871.525428451] [behavior_server]: Activating backup
[component_container_isolated-16] [INFO] [1782639871.525528451] [behavior_server]: Activating drive_on_heading
[component_container_isolated-16] [INFO] [1782639871.525606826] [behavior_server]: Activating wait
[component_container_isolated-16] [INFO] [1782639871.525690493] [behavior_server]: Creating bond (behavior_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639871.639490394] [lifecycle_manager_navigation]: Server behavior_server connected with bond.
[component_container_isolated-16] [INFO] [1782639871.639665395] [lifecycle_manager_navigation]: Activating bt_navigator
[component_container_isolated-16] [INFO] [1782639871.640787646] [bt_navigator]: Activating
[component_container_isolated-16] [WARN] [1782639871.710920156] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[rviz2-18] [INFO] [1782639871.778115412] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[component_container_isolated-16] [WARN] [1782639871.833739070] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-16] [WARN] [1782639871.902549911] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-16] [WARN] [1782639872.026828827] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-16] [WARN] [1782639872.241717571] [bt_navigator_navigate_to_pose_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-16] [INFO] [1782639872.448277221] [bt_navigator]: Creating bond (bt_navigator) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639872.565828920] [lifecycle_manager_navigation]: Server bt_navigator connected with bond.
[component_container_isolated-16] [INFO] [1782639872.566015253] [lifecycle_manager_navigation]: Activating waypoint_follower
[component_container_isolated-16] [INFO] [1782639872.567450338] [waypoint_follower]: Activating
[component_container_isolated-16] [INFO] [1782639872.567705089] [waypoint_follower]: Creating bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639872.696417885] [lifecycle_manager_navigation]: Server waypoint_follower connected with bond.
[component_container_isolated-16] [INFO] [1782639872.696590219] [lifecycle_manager_navigation]: Activating velocity_smoother
[component_container_isolated-16] [INFO] [1782639872.698129262] [velocity_smoother]: Activating
[component_container_isolated-16] [INFO] [1782639872.698651596] [velocity_smoother]: Creating bond (velocity_smoother) to lifecycle manager.
[competition_master_stage3.py-17] [INFO] [1782639872.773867696] [competition_master_stage3]: 重试发送导航目标 (QR点)...
[competition_master_stage3.py-17] [INFO] [1782639872.782674208] [competition_master_stage3]: [DIAG] nav目标距离: 3.97m, robot=(-2.02,-0.03) → target=(0.41,-3.17)
[competition_master_stage3.py-17] [INFO] [1782639872.790749511] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-16] [INFO] [1782639872.795224475] [bt_navigator]: Begin navigating from current location (-2.02, -0.03) to (0.41, -3.17)
[competition_master_stage3.py-17] [INFO] [1782639872.809443161] [competition_master_stage3]: 导航目标已接受，车辆出发...
[component_container_isolated-16] [INFO] [1782639872.822961429] [lifecycle_manager_navigation]: Server velocity_smoother connected with bond.
[component_container_isolated-16] [INFO] [1782639872.823311471] [lifecycle_manager_navigation]: Managed nodes are active
[component_container_isolated-16] [INFO] [1782639872.823422137] [lifecycle_manager_navigation]: Creating bond timer...
[competition_master_stage3.py-17] [INFO] [1782639872.948049637] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.02,-0.03) yaw=21deg cmd=(vx=0.00 wz=0.00) elapsed=3.2s cpuFreq=1500MHz cpuT=78C cpu=88% mem=18%
[component_container_isolated-16] [WARN] [1782639873.394433772] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.7025 Hz
[component_container_isolated-16] [INFO] [1782639873.497386659] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-16] [WARN] [1782639873.497719660] [controller_server]: No goal checker was specified in parameter 'current_goal_checker'. Server will use only plugin loaded goal_checker . This warning will appear once.
[imu_madgwick_filter.py-6] [INFO] [1782639873.863813689] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1539 q_w=0.9993 angle=4.2deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782639873.939678164] [imu_madgwick_filter]: [imu_madgwick ->] msgs=598 q_w=0.9694 angle=28.4deg beta=0.0330
[competition_master_stage3.py-17] [INFO] [1782639874.947193296] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.87,0.01) yaw=5deg cmd=(vx=0.25 wz=-0.97) elapsed=5.2s plan[29pts 4.2m] (-2.00,-0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=78C cpu=66% mem=18%
[component_container_isolated-16] [WARN] [1782639875.378621578] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2846 Hz
[component_container_isolated-16] [INFO] [1782639875.497988236] [controller_server]: Passing new path to controller.
[qr_decoder-10] [INFO] [1782639875.937191570] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=400 last_qr_frame=-1 gap=-1 frames rejects=0
[imu_madgwick_filter.py-4] [WARN] [1782639876.672041213] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.2000s > 0.15s, capping
[competition_master_stage3.py-17] [INFO] [1782639876.949726748] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.46,-0.29) yaw=-55deg cmd=(vx=0.40 wz=0.29) elapsed=7.2s plan[26pts 3.9m] (-1.70,-0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=78C cpu=81% mem=18%
[component_container_isolated-16] [WARN] [1782639877.379800111] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2795 Hz
[component_container_isolated-16] [INFO] [1782639877.498011643] [controller_server]: Passing new path to controller.
[component_container_isolated-16] Reallocing temp weights 798 - 60
[competition_master_stage3.py-17] [INFO] [1782639878.949458194] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.11,-0.72) yaw=-60deg cmd=(vx=0.40 wz=0.10) elapsed=9.2s plan[23pts 3.2m] (-1.30,-0.45)→(0.40,-3.15) cpuFreq=1500MHz cpuT=78C cpu=63% mem=19%
[component_container_isolated-16] [WARN] [1782639879.376140927] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2847 Hz
[component_container_isolated-16] [INFO] [1782639879.498114672] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639880.946378800] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.80,-1.22) yaw=-58deg cmd=(vx=-0.05 wz=0.05) elapsed=11.2s plan[20pts 2.7m] (-1.00,-0.85)→(0.40,-3.15) cpuFreq=1500MHz cpuT=78C cpu=58% mem=19%
[component_container_isolated-16] [WARN] [1782639881.380608167] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2770 Hz
[component_container_isolated-16] [INFO] [1782639881.498004697] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639882.950670746] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.63,-1.49) yaw=-64deg cmd=(vx=0.40 wz=-0.06) elapsed=13.2s plan[14pts 1.9m] (-0.60,-1.55)→(0.40,-3.15) cpuFreq=1500MHz cpuT=78C cpu=69% mem=18%
[component_container_isolated-16] [WARN] [1782639883.379752647] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2782 Hz
[component_container_isolated-16] [INFO] [1782639883.497979679] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-6] [INFO] [1782639883.863228870] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2061 q_w=0.7091 angle=89.7deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782639883.937896552] [imu_madgwick_filter]: [imu_madgwick ->] msgs=785 q_w=0.9014 angle=51.3deg beta=0.0330
[qr_decoder-10] [INFO] [1782639884.623854960] [qr_decoder_zbar]: [qr_decoder] QR DETECTED frame=515 symbols=1 (gap=-1 frames)
[qr_decoder-10] [INFO] [1782639884.624097460] [qr_decoder_zbar]: [QR] 1585 | 3D:(-0.638, +0.157, 1.543)m | px(146,240) D:1543mm
[qr_decoder-10] [INFO] [1782639884.624598336] [qr_decoder_zbar]: [QR] 1585 | robot_pos: (0.35, -2.67, yaw=-1.84)
[qr_decision-11] [INFO] [1782639884.630133718] [qr_decision]: [QR] 1585 CW @ (x=0.35, y=-2.67, yaw=-1.84) → /qr_event
[qr_decision-11] [INFO] [1782639884.633617848] [qr_decision]: [检查点] qr_decision 发布 /qr_event (由 task_manager 决定停车)
[competition_master_stage3.py-17] [INFO] [1782639884.642825776] [competition_master_stage3]: [QR检测] 内容: 1585
[competition_master_stage3.py-17] [INFO] [1782639884.677930531] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decoder_zbar
[competition_master_stage3.py-17] [INFO] [1782639884.694481761] [competition_master_stage3]: >>> QR 解码已关闭, 等待方向判断 (/qr_event)...
[competition_master_stage3.py-17] [INFO] [1782639884.707765029] [competition_master_stage3]: [QR检测] 取消当前导航目标, 等待BT完成 cancel/halt 清理...
[competition_master_stage3.py-17] [INFO] [1782639884.723428883] [competition_master_stage3]: [QR事件] 方向: 顺时针 (通道巡航阶段使用)
[qr_decoder-10] [INFO] [1782639884.724819552] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[competition_master_stage3.py-17] [INFO] [1782639884.733098854] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decision
[competition_master_stage3.py-17] [INFO] [1782639884.949305682] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.38,-1.99) yaw=-67deg cmd=(vx=0.31 wz=0.02) elapsed=15.2s plan[13pts 1.7m] (-0.50,-1.75)→(0.40,-3.15) cpuFreq=1500MHz cpuT=79C cpu=100% mem=18%
[INFO] [qr_decoder-10]: process has finished cleanly [pid 37209]
[component_container_isolated-16] [ERROR] [1782639885.297827184] [bt_navigator_navigate_to_pose_rclcpp_node]: Failed to get result for compute_path_to_pose in node halt!
[component_container_isolated-16] Reallocing temp weights 1068 - 60
[component_container_isolated-16] [WARN] [1782639885.380048418] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2779 Hz
[component_container_isolated-16] [INFO] [1782639885.398010567] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-16] [INFO] [1782639885.398194275] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-16] [INFO] [1782639885.400118403] [bt_navigator]: [navigate_to_pose] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-16] [INFO] [1782639885.401028029] [bt_navigator]: Goal canceled
[competition_master_stage3.py-17] [INFO] [1782639885.414549172] [competition_master_stage3]: [结果回调] BT取消确认完成 (STATUS_CANCELED), 准备发送通道入口目标...
[competition_master_stage3.py-17] [INFO] [1782639885.419576637] [competition_master_stage3]: [状态机] NAV_TO_QR → BACKING_UP
[competition_master_stage3.py-17] [INFO] [1782639885.423615475] [competition_master_stage3]: >>> BT取消完成, 右后退摆正车头→前进进通道...
[competition_master_stage3.py-17] [INFO] [1782639885.432612987] [competition_master_stage3]: [BACKUP] 右后退中: vx=-0.15 wz=0.80, 持续 6.0s...
[INFO] [qr_decision-11]: process has finished cleanly [pid 37211]
[competition_master_stage3.py-17] [INFO] [1782639886.948428782] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.24,-2.25) yaw=-66deg cmd=(vx=-0.15 wz=0.80) elapsed=17.2s plan[7pts 1.0m] (-0.20,-2.45)→(0.40,-3.15) cpuFreq=1500MHz cpuT=78C cpu=63% mem=18%
[competition_master_stage3.py-17] [INFO] [1782639888.958001268] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.23,-2.30) yaw=-36deg cmd=(vx=-0.15 wz=0.80) elapsed=19.2s plan[7pts 1.0m] (-0.20,-2.45)→(0.40,-3.15) cpuFreq=1500MHz cpuT=78C cpu=78% mem=18%
[competition_master_stage3.py-17] [INFO] [1782639890.946021222] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.54,-2.22) yaw=20deg cmd=(vx=-0.15 wz=0.80) elapsed=21.2s plan[7pts 1.0m] (-0.20,-2.45)→(0.40,-3.15) cpuFreq=1200MHz cpuT=78C cpu=61% mem=18%
[competition_master_stage3.py-17] [INFO] [1782639891.435262742] [competition_master_stage3]: [状态机] BACKING_UP → CRUISE_CHANNEL
[competition_master_stage3.py-17] [INFO] [1782639891.437569787] [competition_master_stage3]: [CRUISE] 方向: CW (顺时针, odd QR), 路点: (0.93,0.11), (2.19,0.77), (3.01,-1.16)
[competition_master_stage3.py-17] [INFO] [1782639891.442909544] [competition_master_stage3]: [CRUISE] NavigateThroughPoses: (0.38,-1.10), (0.93,0.11), (2.19,0.77), (3.01,-1.16)
[component_container_isolated-16] [INFO] [1782639891.446171840] [bt_navigator]: Begin navigating from current location through 4 poses to (3.01, -1.16)
[competition_master_stage3.py-17] [INFO] [1782639891.456352811] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[component_container_isolated-16] [WARN] [1782639892.396391175] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.0552 Hz
[component_container_isolated-16] [INFO] [1782639892.548351875] [controller_server]: Received a goal, begin computing control effort.
[competition_master_stage3.py-17] [INFO] [1782639892.947016566] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.64,-2.27) yaw=33deg cmd=(vx=0.40 wz=0.02) elapsed=23.2s plan[61pts 8.7m] (-0.70,-2.35)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=58% mem=18%
[imu_madgwick_filter.py-6] [INFO] [1782639893.863148355] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2601 q_w=0.9767 angle=24.8deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782639893.937253911] [imu_madgwick_filter]: [imu_madgwick ->] msgs=983 q_w=0.8100 angle=71.8deg beta=0.0330
[component_container_isolated-16] [WARN] [1782639894.391118800] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3470 Hz
[component_container_isolated-16] [INFO] [1782639894.548717590] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639894.947138573] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.37,-1.96) yaw=48deg cmd=(vx=0.40 wz=0.13) elapsed=25.2s plan[59pts 8.3m] (-0.50,-2.05)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=69% mem=18%
[component_container_isolated-16] [WARN] [1782639896.388610092] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3507 Hz
[component_container_isolated-16] [INFO] [1782639896.548692261] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639896.947485577] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.08,-1.55) yaw=54deg cmd=(vx=0.21 wz=0.11) elapsed=27.2s plan[53pts 7.5m] (-0.00,-1.45)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=80% mem=18%
[component_container_isolated-16] [WARN] [1782639898.389781595] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3488 Hz
[component_container_isolated-16] [INFO] [1782639898.548675471] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639898.946892368] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.24,-1.19) yaw=34deg cmd=(vx=0.40 wz=-0.17) elapsed=29.2s plan[52pts 7.4m] (0.10,-1.35)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=72% mem=18%
[component_container_isolated-16] [WARN] [1782639900.385049921] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3584 Hz
[component_container_isolated-16] [INFO] [1782639900.548698594] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639900.946271282] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.64,-0.97) yaw=36deg cmd=(vx=0.21 wz=-0.96) elapsed=31.2s plan[50pts 7.0m] (0.70,-0.85)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=61% mem=18%
[component_container_isolated-16] Reallocing temp weights 1500 - 60
[component_container_isolated-16] [WARN] [1782639902.389207339] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3495 Hz
[component_container_isolated-16] [INFO] [1782639902.548677464] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639902.946103151] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.08,-0.71) yaw=1deg cmd=(vx=-0.00 wz=-0.69) elapsed=33.2s plan[45pts 6.5m] (0.90,-0.75)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=58% mem=18%
[imu_madgwick_filter.py-6] [INFO] [1782639903.862923643] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3142 q_w=0.9474 angle=37.3deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782639903.937556199] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1174 q_w=0.9842 angle=20.4deg beta=0.0330
[component_container_isolated-16] [WARN] [1782639904.391818585] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3503 Hz
[component_container_isolated-16] [INFO] [1782639904.548701124] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639904.946030018] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.00,-0.70) yaw=14deg cmd=(vx=0.35 wz=0.97) elapsed=35.2s plan[45pts 6.3m] (1.10,-0.65)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=45% mem=18%
[component_container_isolated-16] [WARN] [1782639906.390268823] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3478 Hz
[component_container_isolated-16] [INFO] [1782639906.548719780] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639906.945862174] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.23,-0.60) yaw=8deg cmd=(vx=-0.17 wz=0.04) elapsed=37.2s plan[45pts 6.3m] (1.20,-0.65)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=54% mem=18%
[component_container_isolated-16] [WARN] [1782639908.383496593] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3629 Hz
[component_container_isolated-16] [INFO] [1782639908.548699059] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639908.946415661] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.17,-0.62) yaw=18deg cmd=(vx=0.18 wz=-0.46) elapsed=39.2s plan[45pts 6.4m] (1.20,-0.65)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=61% mem=18%
[component_container_isolated-16] [WARN] [1782639910.389246377] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3495 Hz
[component_container_isolated-16] [INFO] [1782639910.548698334] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639910.946830270] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.30,-0.59) yaw=4deg cmd=(vx=-0.17 wz=-0.97) elapsed=41.2s plan[44pts 6.2m] (1.40,-0.55)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=61% mem=18%
[component_container_isolated-16] [WARN] [1782639912.384018018] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3611 Hz
[component_container_isolated-16] [INFO] [1782639912.548696566] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639912.948550753] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.18,-0.55) yaw=-24deg cmd=(vx=-0.19 wz=-0.97) elapsed=43.2s plan[43pts 6.1m] (1.20,-0.55)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=72% mem=18%
[imu_madgwick_filter.py-6] [INFO] [1782639913.863763403] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3692 q_w=0.7583 angle=81.4deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782639913.937445416] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1372 q_w=0.9891 angle=16.9deg beta=0.0330
[component_container_isolated-16] [WARN] [1782639914.388108294] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3522 Hz
[component_container_isolated-16] [INFO] [1782639914.548702711] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639914.950732317] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.00,-0.41) yaw=-53deg cmd=(vx=0.40 wz=0.06) elapsed=45.2s plan[43pts 6.2m] (1.00,-0.35)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=80% mem=18%
[component_container_isolated-16] [WARN] [1782639916.389545355] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3547 Hz
[component_container_isolated-16] [INFO] [1782639916.548697103] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639916.951012376] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.09,-0.58) yaw=-62deg cmd=(vx=-0.30 wz=-0.97) elapsed=47.2s plan[43pts 6.1m] (1.10,-0.55)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=63% mem=18%
[component_container_isolated-16] [WARN] [1782639918.388237909] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3511 Hz
[component_container_isolated-16] [INFO] [1782639918.548839618] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639918.946270384] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.00,-0.18) yaw=-95deg cmd=(vx=-0.13 wz=0.53) elapsed=49.2s plan[35pts 4.9m] (1.00,-0.15)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=58% mem=18%
[component_container_isolated-16] [WARN] [1782639920.382016371] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3847 Hz
[component_container_isolated-16] [INFO] [1782639920.548707296] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639920.950117233] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.00,-0.21) yaw=-84deg cmd=(vx=-0.30 wz=0.04) elapsed=51.2s plan[35pts 5.1m] (1.00,-0.05)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=69% mem=18%
[component_container_isolated-16] [WARN] [1782639922.377379750] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782639922.377628167] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.19, 0.77)
[component_container_isolated-16] [WARN] [1782639922.377730000] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782639922.547096469] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782639922.562426864] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782639922.572081335] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782639922.575082547] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782639922.573606254] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782639922.575929132] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782639922.587713939] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-17] [INFO] [1782639922.948065864] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.97,0.42) yaw=-90deg cmd=(vx=0.40 wz=0.10) elapsed=53.2s plan[35pts 5.1m] (1.00,-0.05)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=61% mem=18%
[component_container_isolated-16] [WARN] [1782639923.390384270] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.8472 Hz
[component_container_isolated-16] [INFO] [1782639923.548709392] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-6] [INFO] [1782639923.864092758] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4238 q_w=0.5192 angle=117.4deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782639923.937244895] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1570 q_w=0.9313 angle=42.7deg beta=0.0330
[competition_master_stage3.py-17] [INFO] [1782639924.955148170] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.96,0.19) yaw=-97deg cmd=(vx=-0.30 wz=0.27) elapsed=55.2s plan[32pts 4.6m] (1.00,0.25)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=70% mem=18%
[component_container_isolated-16] [WARN] [1782639925.376131423] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782639925.376346423] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.19, 0.77)
[component_container_isolated-16] [WARN] [1782639925.376472048] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782639925.547026936] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782639925.561493579] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782639925.577617475] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782639925.578862935] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782639925.578925685] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782639925.580923771] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782639925.594134205] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [WARN] [1782639926.387146980] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.8703 Hz
[component_container_isolated-16] [INFO] [1782639926.548695398] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639926.959232178] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.94,0.66) yaw=-91deg cmd=(vx=-0.13 wz=-0.43) elapsed=57.2s plan[29pts 4.4m] (1.00,0.75)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=81% mem=18%
[component_container_isolated-16] [WARN] [1782639928.383635018] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3645 Hz
[component_container_isolated-16] [INFO] [1782639928.548708523] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639928.954068546] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.95,0.83) yaw=-107deg cmd=(vx=-0.30 wz=-0.97) elapsed=59.2s plan[28pts 3.9m] (1.00,0.85)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=72% mem=18%
[component_container_isolated-16] [WARN] [1782639930.385684311] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3564 Hz
[component_container_isolated-16] [INFO] [1782639930.548689812] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639930.946821743] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.32,1.18) yaw=-172deg cmd=(vx=-0.28 wz=0.09) elapsed=61.2s plan[27pts 3.8m] (1.30,1.15)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=69% mem=18%
[component_container_isolated-16] [WARN] [1782639932.387263016] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3538 Hz
[component_container_isolated-16] [INFO] [1782639932.548697099] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639932.961762423] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.60,1.25) yaw=159deg cmd=(vx=0.24 wz=0.97) elapsed=63.2s plan[25pts 3.4m] (1.70,1.15)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=88% mem=18%
[imu_madgwick_filter.py-6] [INFO] [1782639933.863308709] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4766 q_w=-0.3916 angle=226.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782639933.937648763] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1769 q_w=0.3342 angle=141.0deg beta=0.0330
[component_container_isolated-16] [WARN] [1782639934.381369418] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3660 Hz
[component_container_isolated-16] [INFO] [1782639934.548697383] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639934.946956354] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.62,1.24) yaw=154deg cmd=(vx=-0.30 wz=0.01) elapsed=65.2s plan[25pts 3.4m] (1.50,1.25)→(3.00,-1.15) cpuFreq=1500MHz cpuT=78C cpu=87% mem=18%
[component_container_isolated-16] [WARN] [1782639936.381505241] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3638 Hz
[component_container_isolated-16] [INFO] [1782639936.548765039] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639936.948424386] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.99,1.10) yaw=140deg cmd=(vx=-0.13 wz=-0.21) elapsed=67.2s plan[22pts 2.9m] (2.00,1.05)→(3.00,-1.15) cpuFreq=1500MHz cpuT=79C cpu=61% mem=18%
[component_container_isolated-16] [WARN] [1782639938.376710096] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3729 Hz
[component_container_isolated-16] [INFO] [1782639938.648704196] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639938.947763163] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.12,0.98) yaw=117deg cmd=(vx=-0.30 wz=-0.47) elapsed=69.2s plan[19pts 2.6m] (2.10,0.95)→(3.00,-1.15) cpuFreq=1500MHz cpuT=79C cpu=75% mem=18%
[component_container_isolated-16] [WARN] [1782639940.376024496] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3774 Hz
[component_container_isolated-16] [INFO] [1782639940.548906552] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639940.947176646] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.33,0.58) yaw=122deg cmd=(vx=-0.28 wz=-0.25) elapsed=71.2s plan[15pts 2.1m] (2.30,0.55)→(3.00,-1.15) cpuFreq=1500MHz cpuT=79C cpu=88% mem=18%
[component_container_isolated-16] [WARN] [1782639942.376857354] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3729 Hz
[component_container_isolated-16] [INFO] [1782639942.548711491] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639942.950697131] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.51,0.21) yaw=109deg cmd=(vx=-0.28 wz=-0.03) elapsed=73.2s plan[12pts 1.6m] (2.50,0.15)→(3.00,-1.15) cpuFreq=1500MHz cpuT=79C cpu=80% mem=18%
[imu_madgwick_filter.py-6] [INFO] [1782639943.869279349] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5280 q_w=-0.7487 angle=276.9deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782639943.940581274] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1967 q_w=-0.0408 angle=184.7deg beta=0.0330
[component_container_isolated-16] [WARN] [1782639944.379144294] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3976 Hz
[component_container_isolated-16] [INFO] [1782639944.548797594] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639944.955332073] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.71,-0.25) yaw=106deg cmd=(vx=-0.16 wz=0.50) elapsed=75.2s plan[9pts 1.2m] (2.70,-0.25)→(3.00,-1.15) cpuFreq=1500MHz cpuT=79C cpu=87% mem=18%
[component_container_isolated-16] [WARN] [1782639946.375760932] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3767 Hz
[component_container_isolated-16] [INFO] [1782639946.548711445] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [INFO] [1782639946.849615580] [controller_server]: Reached the goal!
[competition_master_stage3.py-17] [INFO] [1782639946.947855289] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.92,-0.68) yaw=116deg cmd=(vx=-0.30 wz=-0.66) elapsed=77.2s plan[7pts 0.8m] (2.90,-0.55)→(3.00,-1.15) cpuFreq=1500MHz cpuT=79C cpu=63% mem=18%
[component_container_isolated-16] [INFO] [1782639947.347085091] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-17] [INFO] [1782639947.357244687] [competition_master_stage3]: [结果回调] 巡航完成, 触发VLM推理...
[competition_master_stage3.py-17] [INFO] [1782639947.363366737] [competition_master_stage3]: [VLM] 发布 sign4return=100, 拍照推理中...
[vision_ai_node-12] [INFO] [1782639947.378593881] [vision_ai_node]: Received sign4return: 100
[competition_master_stage3.py-17] [INFO] [1782639947.378965673] [competition_master_stage3]: [状态机] CRUISE_CHANNEL → RETURN_P
[vision_ai_node-12] [INFO] [1782639947.382571761] [vision_ai_node]: Received trigger signal (sign4return=100), subscribing to image topic...
[competition_master_stage3.py-17] [INFO] [1782639947.388006643] [competition_master_stage3]: [RETURN] NavigateThroughPoses: 通道入口→P点 (0.38,-1.10)→(-1.99,-0.01)
[component_container_isolated-16] [INFO] [1782639947.394171568] [bt_navigator]: Begin navigating from current location through 2 poses to (-1.99, -0.01)
[competition_master_stage3.py-17] [INFO] [1782639947.402195161] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[vision_ai_node-12] [INFO] [1782639947.407202126] [vision_ai_node]: Subscribed to /aurora/rgb/image_raw topic
[vision_ai_node-12] [INFO] [1782639947.469423789] [vision_ai_node]: Received compressed image, processing with AI model...
[component_container_isolated-16] [WARN] [1782639948.391281925] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.0085 Hz
[component_container_isolated-16] [INFO] [1782639948.497783561] [controller_server]: Received a goal, begin computing control effort.
[competition_master_stage3.py-17] [INFO] [1782639948.950037889] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(3.00,-0.88) yaw=101deg cmd=(vx=-0.30 wz=-0.45) elapsed=79.2s plan[50pts 6.8m] (3.00,-0.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=72% mem=18%
[component_container_isolated-16] [WARN] [1782639950.387150140] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2698 Hz
[component_container_isolated-16] [INFO] [1782639950.498113949] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639950.948223190] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(3.02,-1.19) yaw=82deg cmd=(vx=-0.30 wz=0.17) elapsed=81.2s plan[46pts 6.4m] (3.00,-1.35)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=63% mem=18%
[component_container_isolated-16] [WARN] [1782639952.382008018] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2784 Hz
[component_container_isolated-16] [INFO] [1782639952.498113291] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639952.955195665] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.97,-1.84) yaw=64deg cmd=(vx=-0.17 wz=-0.76) elapsed=83.2s plan[42pts 5.8m] (3.00,-1.75)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=87% mem=18%
[imu_madgwick_filter.py-6] [INFO] [1782639953.864344907] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5786 q_w=-0.9762 angle=334.9deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782639953.938128126] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2167 q_w=-0.4625 angle=235.1deg beta=0.0330
[component_container_isolated-16] [WARN] [1782639954.388282033] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2707 Hz
[component_container_isolated-16] [INFO] [1782639954.498095423] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639954.960380386] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.93,-1.98) yaw=53deg cmd=(vx=-0.20 wz=-0.42) elapsed=85.2s plan[41pts 5.7m] (2.80,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=71% mem=18%
[component_container_isolated-16] [WARN] [1782639956.384121948] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2777 Hz
[component_container_isolated-16] [INFO] [1782639956.498096677] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639956.948372041] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.72,-2.15) yaw=6deg cmd=(vx=-0.30 wz=-0.30) elapsed=87.2s plan[43pts 6.0m] (2.80,-2.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=66% mem=18%
[component_container_isolated-16] [WARN] [1782639958.381841988] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2794 Hz
[component_container_isolated-16] [INFO] [1782639958.498135636] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639958.952168213] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.38,-2.14) yaw=-5deg cmd=(vx=-0.20 wz=-0.67) elapsed=89.2s plan[38pts 5.2m] (2.40,-2.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=90% mem=18%
[component_container_isolated-16] [WARN] [1782639960.390110831] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2724 Hz
[component_container_isolated-16] [INFO] [1782639960.498104259] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639960.947266371] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.30,-2.10) yaw=-30deg cmd=(vx=-0.30 wz=-0.93) elapsed=91.2s plan[38pts 5.2m] (2.40,-2.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=72% mem=18%
[component_container_isolated-16] [WARN] [1782639962.376441768] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782639962.376731935] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782639962.381398232] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782639962.496606795] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782639962.513511858] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782639962.523239412] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782639962.523553621] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782639962.523985705] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782639962.524137663] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782639962.537210846] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-17] [INFO] [1782639962.947404825] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.06,-1.85) yaw=-63deg cmd=(vx=0.40 wz=0.42) elapsed=93.2s plan[38pts 5.2m] (2.40,-2.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=57% mem=18%
[component_container_isolated-16] [WARN] [1782639963.389763469] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.7329 Hz
[component_container_isolated-16] [INFO] [1782639963.498103356] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-6] [INFO] [1782639963.863361569] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=6298 q_w=-0.8024 angle=286.7deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782639963.937745663] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2362 q_w=-0.9435 angle=321.3deg beta=0.0330
[competition_master_stage3.py-17] [INFO] [1782639964.947640568] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.16,-2.01) yaw=-53deg cmd=(vx=-0.30 wz=-0.15) elapsed=95.2s plan[37pts 5.0m] (2.20,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=61% mem=18%
[component_container_isolated-16] [WARN] [1782639965.375622193] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782639965.375912693] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782639965.376031985] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782639965.496670888] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782639965.505042398] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782639965.511391656] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782639965.511553032] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782639965.512899450] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782639965.513160909] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782639965.521332502] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [WARN] [1782639966.386183472] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.7025 Hz
[vision_ai_node-12] [INFO] [1782639966.447083466] [vision_ai_node]: AI Analysis Result: 这张图片呈现了一个**临时布置的室内场景**，细节如下：
[vision_ai_node-12]
[vision_ai_node-12] ### 场景与地面
[vision_ai_node-12] 地面铺着**带有褶皱的浅色塑料布**（米黄与浅灰交织的色调），布料略显凌乱，似用于防护或临时施工/活动筹备。
[vision_ai_node-12]
[vision_ai_node-12]
[vision_ai_node-12] ### 主要物体与位置
[vision_ai_node-12] - **右侧遮挡物**：画面右侧是一块**深蓝色的厚实布料**（如帐篷布或大型遮挡布），布料垂落且带自然褶皱，占据右侧大部分区域，边缘隐约露出黑色支撑结构（可能是帐篷支架）。
[vision_ai_node-12] - **左侧纸箱**：左侧靠墙（墙面下半部米黄、上半部白色，中间有深色分隔线）放置一个**彩色纸箱**，箱身以蓝、红、白为主色调（疑似产品包装），顶部开口、边缘略微展开。 
[vision_ai_node-12] - **墙面设施**：
[vision_ai_node-12]   - 墙上方挂有一台**黑色的电视（或显示器）**；
[vision_ai_node-12]   - 电视下方有一个**白色小型装置**（如开关、插座）；
[vision_ai_node-12]   - 装置旁贴有一张**白色告示牌**，再右侧露出部分**红色消防标识牌**（带白色文字）。
[vision_ai_node-12]
[vision_ai_node-12]
[vision_ai_node-12] ### 色调与氛围
[vision_ai_node-12] 整体色调以**蓝（遮挡布）、白（墙面、告示）、米黄（墙面下半部、地面塑料布）**为主，氛围简洁却略带“临时感”（地面塑料布褶皱、遮挡布自然垂落），似为活动筹备、施工过渡或临时空间布置的场景。
[vision_ai_node-12]
[vision_ai_node-12]
[vision_ai_node-12] 物体分布清晰：深蓝色遮挡布（右）、彩色纸箱（左中）、墙面设施（上）与浅色塑料布地面（下），共同构成“临时布置”的视觉效果。
[competition_master_stage3.py-17] [INFO] [1782639966.471664538] [competition_master_stage3]: [VLM] 后台收到推理结果: 这张图片呈现了一个**临时布置的室内场景**，细节如下：
[competition_master_stage3.py-17]
[competition_master_stage3.py-17] ### 场景与地面
[competition_master_stage3.py-17] 地面铺着**带有褶皱的浅色塑料布**（米黄与浅灰交织的色调），布料略显凌乱，似用于防护或临时施工/活动筹备。
[competition_master_stage3.py-17]
[competition_master_stage3.py-17]
[competition_master_stage3.py-17] ### 主要物体与位置
[competition_master_stage3.py-17] - *...
[vision_ai_node-12] [INFO] [1782639966.471999039] [vision_ai_node]: Unsubscribed from image topic
[component_container_isolated-16] [INFO] [1782639966.498118114] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639966.946733598] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.90,-1.65) yaw=-57deg cmd=(vx=-0.20 wz=0.14) elapsed=97.2s plan[33pts 4.5m] (1.90,-1.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=66% mem=18%
[component_container_isolated-16] [WARN] [1782639968.381857954] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2775 Hz
[component_container_isolated-16] [INFO] [1782639968.498252351] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639968.966390735] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.70,-1.40) yaw=-56deg cmd=(vx=-0.30 wz=-0.07) elapsed=99.2s plan[32pts 4.3m] (1.80,-1.45)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=87% mem=18%
[component_container_isolated-16] [WARN] [1782639970.383433317] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.1621 Hz
[component_container_isolated-16] [INFO] [1782639970.498096295] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639970.953895495] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.54,-1.18) yaw=-59deg cmd=(vx=-0.20 wz=0.20) elapsed=101.2s plan[29pts 3.8m] (1.40,-1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=80% mem=18%
[component_container_isolated-16] [WARN] [1782639972.383564008] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2754 Hz
[component_container_isolated-16] [INFO] [1782639972.498108194] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639972.947639427] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.32,-0.90) yaw=-46deg cmd=(vx=-0.30 wz=0.97) elapsed=103.2s plan[28pts 3.8m] (1.40,-0.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=72% mem=18%
[imu_madgwick_filter.py-6] [INFO] [1782639973.864266333] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=6813 q_w=-0.9826 angle=338.6deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782639973.937550675] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2559 q_w=-0.6225 angle=257.0deg beta=0.0330
[component_container_isolated-16] [WARN] [1782639974.377969814] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2861 Hz
[component_container_isolated-16] [INFO] [1782639974.498109090] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639974.953978039] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.94,-0.79) yaw=5deg cmd=(vx=-0.20 wz=-0.89) elapsed=105.2s plan[22pts 3.0m] (0.90,-0.75)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=64% mem=18%
[component_container_isolated-16] [WARN] [1782639976.379264876] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2842 Hz
[component_container_isolated-16] [INFO] [1782639976.498103442] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639976.946430381] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.71,-0.82) yaw=-5deg cmd=(vx=-0.30 wz=-0.24) elapsed=107.2s plan[20pts 2.8m] (0.70,-0.85)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=61% mem=18%
[component_container_isolated-16] [WARN] [1782639978.380656727] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2776 Hz
[component_container_isolated-16] [INFO] [1782639978.498099791] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639978.946805897] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.20,-0.70) yaw=-22deg cmd=(vx=-0.20 wz=0.50) elapsed=109.2s plan[17pts 2.3m] (0.20,-0.75)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=63% mem=18%
[component_container_isolated-16] [WARN] [1782639980.377211445] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2844 Hz
[component_container_isolated-16] [INFO] [1782639980.498101596] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639980.952627084] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.13,-0.68) yaw=-13deg cmd=(vx=-0.30 wz=-0.51) elapsed=111.2s plan[16pts 2.2m] (0.10,-0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=63% mem=18%
[component_container_isolated-16] [WARN] [1782639982.376384705] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2858 Hz
[component_container_isolated-16] [INFO] [1782639982.498092857] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639982.949747716] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.39,-0.51) yaw=-20deg cmd=(vx=-0.20 wz=-0.21) elapsed=113.2s plan[12pts 1.6m] (-0.50,-0.45)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=66% mem=18%
[imu_madgwick_filter.py-6] [INFO] [1782639983.868911743] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=7340 q_w=-0.9202 angle=313.9deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782639983.937248912] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2759 q_w=-0.7396 angle=275.4deg beta=0.0330
[component_container_isolated-16] [WARN] [1782639984.376390713] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2884 Hz
[component_container_isolated-16] [INFO] [1782639984.498106324] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639984.949955682] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.60,-0.44) yaw=-20deg cmd=(vx=-0.30 wz=0.03) elapsed=115.2s plan[12pts 1.6m] (-0.50,-0.45)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=72% mem=18%
[component_container_isolated-16] [WARN] [1782639986.380178598] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2785 Hz
[component_container_isolated-16] [INFO] [1782639986.498100371] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639986.947445600] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.82,-0.38) yaw=-17deg cmd=(vx=-0.20 wz=-0.86) elapsed=117.2s plan[8pts 1.0m] (-1.00,-0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=58% mem=18%
[component_container_isolated-16] [WARN] [1782639988.376616763] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2873 Hz
[component_container_isolated-16] [INFO] [1782639988.498102249] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782639988.949400105] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.23,-0.21) yaw=-35deg cmd=(vx=-0.30 wz=0.51) elapsed=119.2s plan[7pts 0.9m] (-1.10,-0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=70% mem=18%
[component_container_isolated-16] [INFO] [1782639989.999066792] [controller_server]: Reached the goal!
[component_container_isolated-16] [WARN] [1782639990.376388889] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2874 Hz
[component_container_isolated-16] [INFO] [1782639990.496591330] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-17] [INFO] [1782639990.501566628] [competition_master_stage3]: [结果回调] 返航完成, 已回到P点!
[competition_master_stage3.py-17] [INFO] [1782639991.074985261] [competition_master_stage3]: [BAG] 录制已停止
[competition_master_stage3.py-17] [INFO] [1782639991.079782684] [competition_master_stage3]: [状态机] RETURN_P → DONE
[competition_master_stage3.py-17] [INFO] [1782639991.091630907] [competition_master_stage3]:
[competition_master_stage3.py-17] [INFO] [1782639991.095091287] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-17] [INFO] [1782639991.098488916] [competition_master_stage3]: >>> [Stage 3] 任务结束 <<<
[competition_master_stage3.py-17] [INFO] [1782639991.102027795] [competition_master_stage3]:   最终状态: DONE
[competition_master_stage3.py-17] [INFO] [1782639991.105184799] [competition_master_stage3]:   总耗时:   121.4s
[competition_master_stage3.py-17] [INFO] [1782639991.108201053] [competition_master_stage3]:   --- 各阶段耗时 ---
[competition_master_stage3.py-17] [INFO] [1782639991.111848641] [competition_master_stage3]:   LAUNCH................ 16.8s
[competition_master_stage3.py-17] [INFO] [1782639991.114645978] [competition_master_stage3]:   NAV_TO_QR............. 15.7s
[competition_master_stage3.py-17] [INFO] [1782639991.117695690] [competition_master_stage3]:   BACKING_UP............ 6.0s
[competition_master_stage3.py-17] [INFO] [1782639991.120714235] [competition_master_stage3]:   CRUISE_CHANNEL........ 55.9s
[competition_master_stage3.py-17] [INFO] [1782639991.123735906] [competition_master_stage3]:   RETURN_P.............. 43.7s
[competition_master_stage3.py-17] [INFO] [1782639991.126823909] [competition_master_stage3]:   (transition/overhead). -16.8s
[competition_master_stage3.py-17] [INFO] [1782639991.129586288] [competition_master_stage3]:   --- ---
[competition_master_stage3.py-17] [INFO] [1782639991.132890125] [competition_master_stage3]:   QR 原始数据: 1585
[competition_master_stage3.py-17] [INFO] [1782639991.135934338] [competition_master_stage3]:   QR 方向:   顺时针 (CW=顺时针/odd, CCW=逆时针/even)
[competition_master_stage3.py-17] [INFO] [1782639991.138490049] [competition_master_stage3]:   VLM 结果:  这张图片呈现了一个**临时布置的室内场景**，细节如下：
[competition_master_stage3.py-17]
[competition_master_stage3.py-17] ### 场景与地面
[competition_master_stage3.py-17] 地面铺着**带有褶皱的浅色塑料布**（米黄与浅灰交织的色调），布料略显凌乱，似用于防护或临时施工/活动筹备。
[competition_master_stage3.py-17]
[competition_master_stage3.py-17]
[competition_master_stage3.py-17] ### 主要物体与位置
[competition_master_stage3.py-17] - **右侧遮挡物**：画面右侧是一块**深蓝色的厚实布料**（如帐篷布或大型遮挡布），布料垂落且带自然褶皱，占据右侧大部分区域，边缘隐约露出黑色支撑结构（可能是帐篷
[competition_master_stage3.py-17] [INFO] [1782639991.141590970] [competition_master_stage3]:   超时限制:  180.0s (全局)
[competition_master_stage3.py-17] [INFO] [1782639991.144814224] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-17] [INFO] [1782639991.153196609] [competition_master_stage3]: [TRAJ] CSV已保存: /userdata/dev_ws/trajectory_20260628_174631.csv (121 点)
[competition_master_stage3.py-17] [INFO] [1782639991.567833710] [competition_master_stage3]: [TRAJ] Nav2 params snapshot: 31 keys
[competition_master_stage3.py-17] [INFO] [1782639991.572893217] [competition_master_stage3]: [TRAJ] 摘要JSON已保存: /userdata/dev_ws/trajectory_20260628_174631_summary.json
[competition_master_stage3.py-17] [INFO] [1782639991.577050972] [competition_master_stage3]: [TRAJ] 规划历史已保存: /userdata/dev_ws/trajectory_20260628_174631_plans.csv (55 次规划)
[competition_master_stage3.py-17] [INFO] [1782639991.595910537] [competition_master_stage3]: [TRAJ] costmap PGM已保存: /userdata/dev_ws/trajectory_20260628_174631_costmap.pgm
[competition_master_stage3.py-17] [INFO] [1782639991.657259322] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.43,-0.14) yaw=-8deg cmd=(vx=0.00 wz=0.00) elapsed=121.9s plan[4pts 0.4m] (-1.60,-0.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=50% mem=18%
[competition_master_stage3.py-17] [INFO] [1782639992.948157392] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.43,-0.14) yaw=-8deg cmd=(vx=0.00 wz=0.00) elapsed=123.2s plan[4pts 0.4m] (-1.60,-0.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=79C cpu=61% mem=18%
[imu_madgwick_filter.py-6] [INFO] [1782639993.868579540] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=7871 q_w=-0.9731 angle=333.4deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782639993.938732919] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2958 q_w=-0.5468 angle=246.3deg beta=0.0330
^C[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[component_container_isolated-16] [INFO] [1782639994.816475972] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-16] [INFO] [1782639994.816703181] [lifecycle_manager_navigation]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_navigation)
[component_container_isolated-16] [INFO] [1782639994.816989389] [lifecycle_manager_navigation]: Terminating bond timer...
[ERROR] [lslidar_driver_node-2]: process has died [pid 37149, exit code -6, cmd '/userdata/dev_ws/install/lslidar_driver/lib/lslidar_driver/lslidar_driver_node --ros-args -r __node:=lslidar_driver_node --params-file /userdata/dev_ws/install/lslidar_driver/share/lslidar_driver/params/lsx10.yaml'].
[ERROR] [origincar_base_node-1]: process has died [pid 37147, exit code -6, cmd '/userdata/dev_ws/install/origincar_base/lib/origincar_base/origincar_base_node --ros-args --params-file /tmp/launch_params_7z3tqrc_ --params-file /tmp/launch_params_ltqm86y4'].
[INFO] [costmap_filter_info_server-14]: process has finished cleanly [pid 37310]
[INFO] [imu_madgwick_filter.py-6]: process has finished cleanly [pid 37157]
[ERROR] [rviz2-18]: process has died [pid 37470, exit code -11, cmd '/opt/ros/humble/lib/rviz2/rviz2 -d /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/rviz/nav.rviz --ros-args -r __node:=rviz2'].
[INFO] [ekf_node-7]: process has finished cleanly [pid 37159]
[INFO] [lifecycle_manager-15]: process has finished cleanly [pid 37319]
[INFO] [map_server-13]: process has finished cleanly [pid 37308]
[INFO] [static_transform_publisher-8]: process has finished cleanly [pid 37205]
[INFO] [robot_state_publisher-3]: process has finished cleanly [pid 37151]
[map_server-13] [INFO] [1782639994.816547180] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-13] [INFO] [1782639994.816776889] [keepout_mask_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_mask_server)
[map_server-13] [INFO] [1782639994.817044598] [keepout_mask_server]: Deactivating
[map_server-13] [INFO] [1782639994.817138056] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[costmap_filter_info_server-14] [INFO] [1782639994.816793889] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-14] [INFO] [1782639994.816988723] [keepout_filter_info_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_filter_info_server)
[costmap_filter_info_server-14] [INFO] [1782639994.817224931] [keepout_filter_info_server]: Deactivating
[costmap_filter_info_server-14] [INFO] [1782639994.817309348] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[rviz2-18] [INFO] [1782639994.816802972] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[static_transform_publisher-8] [INFO] [1782639994.816800972] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1782639994.817252973] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1782639994.817580848] [origincar_base]: Stop command sent to STM32 on shutdown.
[origincar_base_node-1] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[origincar_base_node-1] terminate called after throwing an instance of 'rclcpp::exceptions::RCLError'
[origincar_base_node-1]   what():  failed to create guard condition: the given context is not valid, either rcl_init() was not called or rcl_shutdown() was called., at ./src/rcl/guard_condition.c:67
[aurora930_node-9] [INFO] [1782639994.817659473] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[aurora930_node-9] I0628 17:46:34.919703 37207 ros2_node.cc:90] process quit succeed
[aurora930_node-9] I0628 17:46:34.919872 37207 aurora900_ros2_device.cc:83] begin stop()
[aurora930_node-9] I0628 17:46:34.919920 37207 aurora900_ros2_device.cc:103] stop stream
[aurora930_node-9] 2026-06-28 17:46:34.965 ( 152.315s) [        992C4020]      aurora900_impl.cc:648   INFO| ir_stream_count_=0, rgb_stream_count_=0, depth_stream_count_=0
[aurora930_node-9] 2026-06-28 17:46:34.965 ( 152.315s) [        992C4020]      aurora900_impl.cc:649   INFO| mask=7
[aurora930_node-9] I0628 17:46:35.220434 37207 aurora900_ros2_device.cc:105] destroy stream
[aurora930_node-9] I0628 17:46:35.220715 37207 aurora900_ros2_device.cc:110] close glog
[aurora930_node-9] WARNING: Logging before InitGoogleLogging() is written to STDERR
[aurora930_node-9] I0628 17:46:35.221194 37207 ros2_device.cc:113] close device...
[aurora930_node-9] 2026-06-28 17:46:35.720 ( 153.070s) [        699E37E0]         cmd_backend.cc:40    INFO| RunBlocking is end!!!
[aurora930_node-9] 2026-06-28 17:46:35.921 ( 153.271s) [        992C4020]deptrum_camera_vendor.c:121   INFO| device is close.
[aurora930_node-9] I0628 17:46:35.923583 37207 ros2_device.cc:116] quit succeed
[robot_state_publisher-3] [INFO] [1782639994.818371224] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[competition_master_stage3.py-17] [INFO] [1782639994.833065368] [competition_master_stage3]: [MAIN] 收到 Ctrl+C, 停止录制 + 保存轨迹...
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.838841917] [competition_master_stage3]:
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.861710195] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.874593128] [competition_master_stage3]: >>> [Stage 3] 任务结束 <<<
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.877988715] [competition_master_stage3]:   最终状态: DONE
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.907835461] [competition_master_stage3]:   总耗时:   125.1s
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.913415301] [competition_master_stage3]:   --- 各阶段耗时 ---
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.921962520] [competition_master_stage3]:   LAUNCH................ 16.8s
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.931158532] [competition_master_stage3]:   NAV_TO_QR............. 15.7s
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.937170247] [competition_master_stage3]:   BACKING_UP............ 6.0s
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.941817670] [competition_master_stage3]:   CRUISE_CHANNEL........ 55.9s
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.947029968] [competition_master_stage3]:   RETURN_P.............. 43.7s
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.952697642] [competition_master_stage3]:   (transition/overhead). -13.0s
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.959415067] [competition_master_stage3]:   --- ---
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.964998907] [competition_master_stage3]:   QR 原始数据: 1585
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.969766830] [competition_master_stage3]:   QR 方向:   顺时针 (CW=顺时针/odd, CCW=逆时针/even)
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.974263585] [competition_master_stage3]:   VLM 结果:  这张图片呈现了一个**临时布置的室内场景**，细节如下：
[competition_master_stage3.py-17]
[competition_master_stage3.py-17] ### 场景与地面
[competition_master_stage3.py-17] 地面铺着**带有褶皱的浅色塑料布**（米黄与浅灰交织的色调），布料略显凌乱，似用于防护或临时施工/活动筹备。
[competition_master_stage3.py-17]
[competition_master_stage3.py-17]
[competition_master_stage3.py-17] ### 主要物体与位置
[competition_master_stage3.py-17] - **右侧遮挡物**：画面右侧是一块**深蓝色的厚实布料**（如帐篷布或大型遮挡布），布料垂落且带自然褶皱，占据右侧大部分区域，边缘隐约露出黑色支撑结构（可能是帐篷
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.977839673] [competition_master_stage3]:   超时限制:  180.0s (全局)
[ekf_node-7] [INFO] [1782639994.821884479] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-15] [INFO] [1782639994.822300438] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-15] [INFO] [1782639994.824368065] [lifecycle_manager_keepout]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_keepout)
[lifecycle_manager-15] [INFO] [1782639994.824590274] [lifecycle_manager_keepout]: Terminating bond timer...
[lifecycle_manager-15] [INFO] [1782639994.995621904] [lifecycle_manager_keepout]: Destroying lifecycle_manager_keepout
[map_server-13] [INFO] [1782639994.836524830] [keepout_mask_server]: Cleaning up
[map_server-13] [INFO] [1782639994.836760747] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[map_server-13] [INFO] [1782639995.052358308] [keepout_mask_server]: Destroying
[costmap_filter_info_server-14] [INFO] [1782639994.838948125] [keepout_filter_info_server]: Cleaning up
[costmap_filter_info_server-14] [INFO] [1782639994.839209875] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-14] [INFO] [1782639995.065972616] [keepout_filter_info_server]: Destroying
[component_container_isolated-16] [INFO] [1782639995.060330693] [local_costmap.local_costmap]: Message Filter dropping message: frame 'laser_link' at time 1782639994.759 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-16] [INFO] [1782639995.233983451] [velocity_smoother]: Running Nav2 LifecycleNode rcl preshutdown (velocity_smoother)
[component_container_isolated-16] [INFO] [1782639995.234432826] [velocity_smoother]: Deactivating
[component_container_isolated-16] [INFO] [1782639995.234605701] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639995.245775132] [velocity_smoother]: Cleaning up
[component_container_isolated-16] [INFO] [1782639995.246255716] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639995.246389091] [waypoint_follower]: Running Nav2 LifecycleNode rcl preshutdown (waypoint_follower)
[component_container_isolated-16] [INFO] [1782639995.246526550] [waypoint_follower]: Deactivating
[component_container_isolated-16] [INFO] [1782639995.246668050] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639995.257636980] [waypoint_follower]: Cleaning up
[component_container_isolated-16] [INFO] [1782639995.304360622] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639995.304518747] [behavior_server]: Running Nav2 LifecycleNode rcl preshutdown (behavior_server)
[component_container_isolated-16] [INFO] [1782639995.304653539] [behavior_server]: Deactivating
[component_container_isolated-16] [INFO] [1782639995.304966039] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639995.315387010] [behavior_server]: Cleaning up
[component_container_isolated-16] [INFO] [1782639995.363604237] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639995.363771612] [bt_navigator]: Running Nav2 LifecycleNode rcl preshutdown (bt_navigator)
[component_container_isolated-16] [INFO] [1782639995.363913988] [bt_navigator]: Deactivating
[component_container_isolated-16] [INFO] [1782639995.364081238] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639995.374451584] [bt_navigator]: Cleaning up
[component_container_isolated-16] [INFO] [1782639995.926435397] [bt_navigator]: Completed Cleaning up
[component_container_isolated-16] [INFO] [1782639995.927368523] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639995.927538232] [amcl]: Running Nav2 LifecycleNode rcl preshutdown (amcl)
[component_container_isolated-16] [INFO] [1782639995.928093399] [amcl]: Deactivating
[component_container_isolated-16] [INFO] [1782639995.928372608] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639995.944328919] [amcl]: Cleaning up
[component_container_isolated-16] [INFO] [1782639995.967574990] [lifecycle_manager_localization]: Have not received a heartbeat from amcl.
[component_container_isolated-16] [ERROR] [1782639995.967752157] [lifecycle_manager_localization]: CRITICAL FAILURE: SERVER amcl IS DOWN after not receiving a heartbeat for 4000 ms. Shutting down related nodes.
[component_container_isolated-16] [INFO] [1782639995.968102407] [lifecycle_manager_localization]: Terminating bond timer...
[component_container_isolated-16] [INFO] [1782639995.968188616] [lifecycle_manager_localization]: Resetting managed nodes...
[component_container_isolated-16] [INFO] [1782639995.968246991] [lifecycle_manager_localization]: Deactivating amcl
[component_container_isolated-16] [WARN] [1782639995.992584896] [rcl_lifecycle]: No transition matching 4 found for current state cleaningup
[component_container_isolated-16] [WARN] [1782639995.992677563] [rcl_lifecycle]: No transition matching 4 found for current state cleaningup
[component_container_isolated-16] [ERROR] [1782639995.992719355] [amcl]: Unable to start transition 4 from current state cleaningup: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-16] [ERROR] [1782639995.994599690] [lifecycle_manager_localization]: Failed to change state for node: amcl
[component_container_isolated-16] [INFO] [1782639995.994856107] [lifecycle_manager_localization]: Deactivating map_server
[component_container_isolated-16] [INFO] [1782639995.995816858] [map_server]: Deactivating
[component_container_isolated-16] [INFO] [1782639995.995992859] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639996.001600616] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639996.001774699] [planner_server]: Running Nav2 LifecycleNode rcl preshutdown (planner_server)
[component_container_isolated-16] [INFO] [1782639996.001906866] [planner_server]: Deactivating
[component_container_isolated-16] [INFO] [1782639996.002143116] [global_costmap.global_costmap]: Deactivating
[component_container_isolated-16] [INFO] [1782639996.110564751] [lifecycle_manager_localization]: Cleaning up amcl
[component_container_isolated-16] [WARN] [1782639996.111756836] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-16] [WARN] [1782639996.111839420] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-16] [ERROR] [1782639996.111867920] [amcl]: Unable to start transition 2 from current state unconfigured: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-16] [INFO] [1782639996.112814546] [lifecycle_manager_localization]: Cleaning up map_server
[component_container_isolated-16] [INFO] [1782639996.113394422] [map_server]: Cleaning up
[component_container_isolated-16] [INFO] [1782639996.122854892] [lifecycle_manager_localization]: Managed nodes have been reset
[component_container_isolated-16] [INFO] [1782639996.368486823] [planner_server]: Deactivating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-16] [INFO] [1782639996.368785740] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639996.379192628] [planner_server]: Cleaning up
[component_container_isolated-16] [INFO] [1782639996.402337240] [global_costmap.global_costmap]: Cleaning up
[component_container_isolated-16] [INFO] [1782639996.411842627] [planner_server]: Cleaning up plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-16] [INFO] [1782639996.412867336] [planner_server]: Destroying plugin GridBased of type SmacPlannerHybrid
[bmi088_iio_bridge.py-5] Traceback (most recent call last):
[bmi088_iio_bridge.py-5]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/bmi088_iio_bridge.py", line 493, in <module>
[bmi088_iio_bridge.py-5]     main()
[bmi088_iio_bridge.py-5]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/bmi088_iio_bridge.py", line 489, in main
[bmi088_iio_bridge.py-5]     rclpy.shutdown()
[bmi088_iio_bridge.py-5]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 130, in shutdown
[bmi088_iio_bridge.py-5]     _shutdown(context=context)
[bmi088_iio_bridge.py-5]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/utilities.py", line 58, in shutdown
[bmi088_iio_bridge.py-5]     return context.shutdown()
[bmi088_iio_bridge.py-5]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/context.py", line 102, in shutdown
[bmi088_iio_bridge.py-5]     self.__context.shutdown()
[bmi088_iio_bridge.py-5] rclpy._rclpy_pybind11.RCLError: failed to shutdown: rcl_shutdown already called on the given context, at ./src/rcl/init.c:241
[vision_ai_node-12] Traceback (most recent call last):
[vision_ai_node-12]   File "/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node", line 33, in <module>
[vision_ai_node-12]     sys.exit(load_entry_point('racing-vision-ai==0.0.1', 'console_scripts', 'vision_ai_node')())
[vision_ai_node-12]   File "/userdata/dev_ws/install/racing_vision_ai/lib/python3.10/site-packages/racing_vision_ai/vision_ai_node.py", line 283, in main
[vision_ai_node-12]     rclpy.shutdown()
[vision_ai_node-12]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 130, in shutdown
[vision_ai_node-12]     _shutdown(context=context)
[vision_ai_node-12]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/utilities.py", line 58, in shutdown
[vision_ai_node-12]     return context.shutdown()
[vision_ai_node-12]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/context.py", line 102, in shutdown
[vision_ai_node-12]     self.__context.shutdown()
[vision_ai_node-12] rclpy._rclpy_pybind11.RCLError: failed to shutdown: rcl_shutdown already called on the given context, at ./src/rcl/init.c:241
[imu_madgwick_filter.py-4] Traceback (most recent call last):
[imu_madgwick_filter.py-4]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/imu_madgwick_filter.py", line 301, in <module>
[imu_madgwick_filter.py-4]     main()
[imu_madgwick_filter.py-4]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/imu_madgwick_filter.py", line 286, in main
[imu_madgwick_filter.py-4]     rclpy.spin(node)
[imu_madgwick_filter.py-4]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 229, in spin
[imu_madgwick_filter.py-4]     executor.spin_once()
[imu_madgwick_filter.py-4]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 808, in spin_once
[imu_madgwick_filter.py-4]     self._spin_once_impl(timeout_sec)
[imu_madgwick_filter.py-4]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 805, in _spin_once_impl
[imu_madgwick_filter.py-4]     raise handler.exception()
[imu_madgwick_filter.py-4]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/task.py", line 272, in _execute_coroutine_step
[imu_madgwick_filter.py-4]     result = coro.send(None)
[imu_madgwick_filter.py-4]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 478, in handler
[imu_madgwick_filter.py-4]     arg = take_from_wait_list(entity)
[imu_madgwick_filter.py-4]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 400, in _take_subscription
[imu_madgwick_filter.py-4]     msg_info = sub.handle.take_message(sub.msg_type, sub.raw)
[imu_madgwick_filter.py-4] RuntimeError: Unable to convert call argument to Python object (compile in debug mode for details)
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.981473719] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639994.989638271] [competition_master_stage3]: [TRAJ] CSV已保存: /userdata/dev_ws/trajectory_20260628_174634.csv (122 点)
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639995.550722054] [competition_master_stage3]: [TRAJ] Nav2 params snapshot: 31 keys
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639995.561826693] [competition_master_stage3]: [TRAJ] 摘要JSON已保存: /userdata/dev_ws/trajectory_20260628_174634_summary.json
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639995.570648579] [competition_master_stage3]: [TRAJ] 规划历史已保存: /userdata/dev_ws/trajectory_20260628_174634_plans.csv (55 次规划)
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782639995.594242066] [competition_master_stage3]: [TRAJ] costmap PGM已保存: /userdata/dev_ws/trajectory_20260628_174634_costmap.pgm
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[component_container_isolated-16] [INFO] [1782639996.433294278] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639996.433453195] [smoother_server]: Running Nav2 LifecycleNode rcl preshutdown (smoother_server)
[component_container_isolated-16] [INFO] [1782639996.433567362] [smoother_server]: Deactivating
[component_container_isolated-16] [INFO] [1782639996.433622362] [smoother_server]: Deactivating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-16] [INFO] [1782639996.433760821] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639996.444122417] [smoother_server]: Cleaning up
[component_container_isolated-16] [INFO] [1782639996.444251334] [smoother_server]: Cleaning up smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-16] [INFO] [1782639996.460819646] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639996.460996480] [map_server]: Running Nav2 LifecycleNode rcl preshutdown (map_server)
[component_container_isolated-16] [INFO] [1782639996.461082771] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639996.461139146] [lifecycle_manager_localization]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_localization)
[component_container_isolated-16] [INFO] [1782639996.471692493] [controller_server]: Running Nav2 LifecycleNode rcl preshutdown (controller_server)
[component_container_isolated-16] [INFO] [1782639996.471935951] [controller_server]: Deactivating
[component_container_isolated-16] [INFO] [1782639996.472020785] [controller_server]: Deactivating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-16] [INFO] [1782639996.472247119] [local_costmap.local_costmap]: Deactivating
[component_container_isolated-16] [INFO] [1782639996.486023802] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782639996.496577149] [controller_server]: Cleaning up
[component_container_isolated-16] [INFO] [1782639996.496719107] [controller_server]: Cleaning up controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-16] [INFO] [1782639996.497010483] [local_costmap.local_costmap]: Cleaning up
[ERROR] [imu_madgwick_filter.py-4]: process has died [pid 37153, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/imu_madgwick_filter.py --ros-args -r __node:=imu_madgwick_filter --params-file /userdata/dev_ws/install/origincar_base/share/origincar_base/config/imu_madgwick.yaml'].
[ERROR] [bmi088_iio_bridge.py-5]: process has died [pid 37155, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/bmi088_iio_bridge.py --ros-args -r __node:=bmi088_iio_bridge --params-file /tmp/launch_params_kpsgggmf'].
[ERROR] [vision_ai_node-12]: process has died [pid 37213, exit code 1, cmd '/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node --ros-args -r __node:=vision_ai_node'].
[INFO] [aurora930_node-9]: process has finished cleanly [pid 37207]
[INFO] [competition_master_stage3.py-17]: process has finished cleanly [pid 37468]
[component_container_isolated-16] [INFO] [1782639997.540690991] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[ERROR] [component_container_isolated-16]: process[component_container_isolated-16] failed to terminate '5' seconds after receiving 'SIGINT', escalating to 'SIGTERM'
[INFO] [component_container_isolated-16]: sending signal 'SIGTERM' to process[component_container_isolated-16]
[component_container_isolated-16] [INFO] [1782640001.424262945] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [component_container_isolated-16]: process[component_container_isolated-16] failed to terminate '10.0' seconds after receiving 'SIGTERM', escalating to 'SIGKILL'
[INFO] [component_container_isolated-16]: sending signal 'SIGKILL' to process[component_container_isolated-16]
[ERROR] [component_container_isolated-16]: process has died [pid 37466, exit code -9, cmd '/opt/ros/humble/lib/rclcpp_components/component_container_isolated --ros-args --log-level info --ros-args -r __node:=nav2_container --params-file /tmp/launch_params_vyp6onng --params-file /tmp/launch_params_udihkic0 -r /tf:=tf -r /tf_static:=tf_static'].
root@ubuntu:/userdata/dev_ws# ros2 launch origincar_bringup stage3_bringup.launch.py
[INFO] [launch]: All log files can be found below /root/.ros/log/2026-06-28-17-46-49-881871-ubuntu-38837
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [origincar_base_node-1]: process started with pid [38859]
[INFO] [lslidar_driver_node-2]: process started with pid [38861]
[INFO] [robot_state_publisher-3]: process started with pid [38863]
[INFO] [imu_madgwick_filter.py-4]: process started with pid [38865]
[INFO] [bmi088_iio_bridge.py-5]: process started with pid [38867]
[INFO] [imu_madgwick_filter.py-6]: process started with pid [38869]
[INFO] [ekf_node-7]: process started with pid [38871]
[INFO] [static_transform_publisher-8]: process started with pid [38911]
[INFO] [aurora930_node-9]: process started with pid [38913]
[INFO] [qr_decoder-10]: process started with pid [38915]
[INFO] [qr_decision-11]: process started with pid [38917]
[INFO] [vision_ai_node-12]: process started with pid [38919]
[origincar_base_node-1] [INFO] [1782640010.589077013] [origincar_base]: origincar_base serial port opened
[lslidar_driver_node-2] [INFO] [1782640010.577110706] [lslidar_driver_node]: Lidar is N10
[lslidar_driver_node-2] [INFO] [1782640010.593767477] [lslidar_driver_node]: Initialised lslidar without error
[lslidar_driver_node-2] [INFO] [1782640010.593925060] [lslidar_driver_node]: Successfully initialize driver...
[robot_state_publisher-3] [INFO] [1782640010.582803380] [robot_state_publisher]: got segment base_footprint
[robot_state_publisher-3] [INFO] [1782640010.583172047] [robot_state_publisher]: got segment base_link
[robot_state_publisher-3] [INFO] [1782640010.583258755] [robot_state_publisher]: got segment gyro_link
[robot_state_publisher-3] [INFO] [1782640010.583312256] [robot_state_publisher]: got segment laser_link
[ekf_node-7] Both imu1_differential and imu1_relative were set to true. Using differential mode.
[static_transform_publisher-8] [INFO] [1782640010.757015887] [depth_camera_tf]: Spinning until stopped - publishing transform
[static_transform_publisher-8] translation: ('0.140000', '0.000000', '0.050000')
[static_transform_publisher-8] rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
[static_transform_publisher-8] from 'base_link' to 'depth_camera_link'
[aurora930_node-9] W0628 17:46:51.308854 38913 ros2_node.cc:35] hello aurora 900/930
[qr_decoder-10] [INFO] [1782640011.395941427] [qr_decoder_zbar]: QR decoder (ZBar) started: rgb=/aurora/rgb/image_raw, depth=/aurora/depth/image_raw, filter=on, range=[50, 4000]mm, min_qr_len=1, intrinsics: fx=421.3 fy=422.3 cx=320.3 cy=197.0
[aurora930_node-9] 2026-06-28 17:46:51.403 (   0.241s) [        8EE34020] device_manager_impl.cc:89    INFO| hotplug has registed by user
[aurora930_node-9] device_count==========1
[aurora930_node-9] I0628 17:46:51.432363 38913 aurora900_ros2_device.cc:153] BOOT_ORDER_1::Found 1 deptrum device
[aurora930_node-9] I0628 17:46:51.441107 38913 aurora900_ros2_device.cc:162] BOOT_ORDER_1::No serial number provided: picking first device
[aurora930_node-9] 2026-06-28 17:46:51.441 (   0.278s) [        8EE34020] device_manager_impl.cc:318   INFO| Device information:
[aurora930_node-9]      ir_pid:0x1930, rgb_pid:0x0
[aurora930_node-9]      serial number:HY400529001015314G00248
[aurora930_node-9] I0628 17:46:51.441418 38913 aurora900_ros2_device.cc:206] BOOT_ORDER_1::0:device start opening
[aurora930_node-9] 2026-06-28 17:46:51.443 (   0.281s) [        8EE34020]   custom_usb_device.cc:101   INFO| bulk in endpoint addr:129
[aurora930_node-9] 2026-06-28 17:46:51.444 (   0.281s) [        8EE34020]   custom_usb_device.cc:98    INFO| bulk out endpoint addr:2
[aurora930_node-9] 2026-06-28 17:46:51.449 (   0.286s) [        8EE34020]deptrum_camera_aurora93:53    INFO| doe_broken:0 ito_support:1 crash_count:0 wdt_count:0 hard_reset_count:2 heart_boot_count:0 boot_total:121 last_crash_time:N
[aurora930_node-9] I0628 17:46:51.449146 38913 aurora900_ros2_device.cc:247] device supported frame_mode:
[aurora930_node-9] I0628 17:46:51.449262 38913 aurora900_ros2_device.cc:252] [0]:ir_mode:=13 kRes320x200Ir8Bit rgb_mode:=31 kRes320x200RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0628 17:46:51.449358 38913 aurora900_ros2_device.cc:252] [1]:ir_mode:=17 kRes480x300Depth16Bit rgb_mode:=32 kRes480x300RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0628 17:46:51.449419 38913 aurora900_ros2_device.cc:252] [2]:ir_mode:=20 kRes640x400Ir8Bit rgb_mode:=33 kRes640x400RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0628 17:46:51.449461 38913 aurora900_ros2_device.cc:266] current set mode ir_mode:20:kRes640x400Ir8Bit,rgb_mode:33:kRes640x400RgbYuv
[INFO] [map_server-13]: process started with pid [38997]
[INFO] [costmap_filter_info_server-14]: process started with pid [38999]
[INFO] [lifecycle_manager-15]: process started with pid [39001]
[costmap_filter_info_server-14] [INFO] [1782640011.951054904] [costmap_filter_info_server]: This is costmap filter info publisher
[lifecycle_manager-15] [INFO] [1782640011.957884538] [lifecycle_manager_keepout]: Creating
[aurora930_node-9] I0628 17:46:51.986614 38913 aurora900_ros2_device.cc:387] Switch Auto Exposure
[aurora930_node-9] 2026-06-28 17:46:52.039 (   0.877s) [        8EE34020]      aurora900_impl.cc:1106  INFO| SetHeartbeat user set heartbeat enable: 0
[lifecycle_manager-15] [INFO] [1782640012.058604287] [lifecycle_manager_keepout]: Creating and initializing lifecycle service clients
[map_server-13] [INFO] [1782640012.103185092] [keepout_mask_server]:
[map_server-13]         keepout_mask_server lifecycle node launched.
[map_server-13]         Waiting on external lifecycle transitions to activate
[map_server-13]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[map_server-13] [INFO] [1782640012.104220260] [keepout_mask_server]: Creating
[lifecycle_manager-15] [INFO] [1782640012.120722114] [lifecycle_manager_keepout]: Starting managed nodes bringup...
[lifecycle_manager-15] [INFO] [1782640012.121139990] [lifecycle_manager_keepout]: Configuring keepout_mask_server
[map_server-13] [INFO] [1782640012.122199783] [keepout_mask_server]: Configuring
[map_server-13] [INFO] [1782640012.122470741] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.yaml
[map_server-13] [INFO] [1782640012.123754118] [map_io]: resolution: 0.05
[map_server-13] [INFO] [1782640012.123840326] [map_io]: origin[0]: -2.65
[map_server-13] [INFO] [1782640012.123872368] [map_io]: origin[1]: -4.5
[map_server-13] [INFO] [1782640012.123899993] [map_io]: origin[2]: 0
[map_server-13] [INFO] [1782640012.123928993] [map_io]: free_thresh: 0.5
[map_server-13] [INFO] [1782640012.123957326] [map_io]: occupied_thresh: 0.5
[map_server-13] [INFO] [1782640012.123996785] [map_io]: mode: scale
[map_server-13] [INFO] [1782640012.124026493] [map_io]: negate: 0
[map_server-13] [INFO] [1782640012.124826328] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm
[costmap_filter_info_server-14] [INFO] [1782640012.135415299] [keepout_filter_info_server]:
[costmap_filter_info_server-14]         keepout_filter_info_server lifecycle node launched.
[costmap_filter_info_server-14]         Waiting on external lifecycle transitions to activate
[costmap_filter_info_server-14]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[map_server-13] [INFO] [1782640012.146165479] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm: 163 X 141 map @ 0.05 m/cell
[lifecycle_manager-15] [INFO] [1782640012.188510323] [lifecycle_manager_keepout]: Configuring keepout_filter_info_server
[costmap_filter_info_server-14] [INFO] [1782640012.189431616] [keepout_filter_info_server]: Configuring
[lifecycle_manager-15] [INFO] [1782640012.210159225] [lifecycle_manager_keepout]: Activating keepout_mask_server
[map_server-13] [INFO] [1782640012.223184657] [keepout_mask_server]: Activating
[map_server-13] [INFO] [1782640012.223729908] [keepout_mask_server]: Creating bond (keepout_mask_server) to lifecycle manager.
[lifecycle_manager-15] [INFO] [1782640012.344915933] [lifecycle_manager_keepout]: Server keepout_mask_server connected with bond.
[lifecycle_manager-15] [INFO] [1782640012.345106433] [lifecycle_manager_keepout]: Activating keepout_filter_info_server
[costmap_filter_info_server-14] [INFO] [1782640012.346111268] [keepout_filter_info_server]: Activating
[costmap_filter_info_server-14] [INFO] [1782640012.346339226] [keepout_filter_info_server]: Creating bond (keepout_filter_info_server) to lifecycle manager.
[bmi088_iio_bridge.py-5] [INFO] [1782640012.399612959] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1782640012.402560296] [bmi088_iio_bridge]:   DIAGNOSTIC: Scanning IIO devices under /sys/bus/iio/devices/
[bmi088_iio_bridge.py-5] [INFO] [1782640012.405196424] [bmi088_iio_bridge]:   Equivalent to: ls /sys/bus/iio/devices/*/name
[bmi088_iio_bridge.py-5] [INFO] [1782640012.407733927] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1782640012.410283180] [bmi088_iio_bridge]:   iio:device0/name = "34190000.adc"
[bmi088_iio_bridge.py-5] [INFO] [1782640012.412900642] [bmi088_iio_bridge]:   iio:device1/name = "bmi08x"
[bmi088_iio_bridge.py-5] [INFO] [1782640012.415683020] [bmi088_iio_bridge]:   trigger0/name = "34190000.adc-dev0"
[bmi088_iio_bridge.py-5] [INFO] [1782640012.418548315] [bmi088_iio_bridge]:   Total IIO devices found: 3
[bmi088_iio_bridge.py-5] [INFO] [1782640012.421554902] [bmi088_iio_bridge]:   BMI088 kernel module APPEARS LOADED: 1 BMI device(s) detected
[bmi088_iio_bridge.py-5] [INFO] [1782640012.424284947] [bmi088_iio_bridge]:   BMI device names: ['bmi08x']
[bmi088_iio_bridge.py-5] [INFO] [1782640012.427480035] [bmi088_iio_bridge]:   gyro:  /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_anglvel is_si=False scale_override=0.00053
[bmi088_iio_bridge.py-5] [INFO] [1782640012.430620914] [bmi088_iio_bridge]:   accel: /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_accel is_si=False scale_override=0.00341
[imu_madgwick_filter.py-6] [INFO] [1782640012.443557596] [imu_madgwick_bmi088]: [imu_madgwick] init: beta=0.0030, gyro_noise=0.0002, accel_noise=0.010
[aurora930_node-9] I0628 17:46:52.450023 38913 aurora900_ros2_device.cc:304] BOOT_ORDER_1::Device information:
[aurora930_node-9] I0628 17:46:52.450183 38913 aurora900_ros2_device.cc:305]     sdk version: 1.1.22
[aurora930_node-9] I0628 17:46:52.450227 38913 aurora900_ros2_device.cc:306]     device name: Aurora 930
[aurora930_node-9] I0628 17:46:52.450254 38913 aurora900_ros2_device.cc:307]     serial number: HY400529001015314G00248
[aurora930_node-9] I0628 17:46:52.450280 38913 aurora900_ros2_device.cc:308]     firmware version: 1.7.2
[aurora930_node-9] I0628 17:46:52.450332 38913 camera_parameters.cc:134] BOOT_ORDER_1::Camera Parameters:
[aurora930_node-9] I0628 17:46:52.450361 38913 camera_parameters.cc:135] BOOT_ORDER_1::  Ir Intrinsics:
[aurora930_node-9] I0628 17:46:52.450397 38913 camera_parameters.cc:146]                 Resolution:
[aurora930_node-9] I0628 17:46:52.450423 38913 camera_parameters.cc:147]                         Rows:400
[aurora930_node-9] I0628 17:46:52.450448 38913 camera_parameters.cc:148]                         Cols:640
[aurora930_node-9] I0628 17:46:52.450479 38913 camera_parameters.cc:149]                 Intrinsics:
[aurora930_node-9] I0628 17:46:52.450505 38913 camera_parameters.cc:150]                         fx: 421.307
[aurora930_node-9] I0628 17:46:52.450613 38913 camera_parameters.cc:151]                         fy: 422.254
[aurora930_node-9] I0628 17:46:52.450654 38913 camera_parameters.cc:152]                         cx: 320.27
[aurora930_node-9] I0628 17:46:52.450687 38913 camera_parameters.cc:153]                         cy: 197.01
[aurora930_node-9] I0628 17:46:52.450723 38913 camera_parameters.cc:154]                         k1: 0.0606853
[aurora930_node-9] I0628 17:46:52.450757 38913 camera_parameters.cc:155]                         k2: -0.10961
[aurora930_node-9] I0628 17:46:52.450788 38913 camera_parameters.cc:156]                         p1: 0.00126689
[aurora930_node-9] I0628 17:46:52.450845 38913 camera_parameters.cc:157]                         p2: -0.00120539
[aurora930_node-9] I0628 17:46:52.450887 38913 camera_parameters.cc:158]                         k3: 0.0522281
[aurora930_node-9] I0628 17:46:52.450919 38913 camera_parameters.cc:138] BOOT_ORDER_1::  Rgb Intrinsics:
[aurora930_node-9] I0628 17:46:52.450975 38913 camera_parameters.cc:146]                 Resolution:
[aurora930_node-9] I0628 17:46:52.451006 38913 camera_parameters.cc:147]                         Rows:400
[aurora930_node-9] I0628 17:46:52.451032 38913 camera_parameters.cc:148]                         Cols:640
[aurora930_node-9] I0628 17:46:52.451058 38913 camera_parameters.cc:149]                 Intrinsics:
[aurora930_node-9] I0628 17:46:52.451083 38913 camera_parameters.cc:150]                         fx: 416.49
[aurora930_node-9] I0628 17:46:52.451116 38913 camera_parameters.cc:151]                         fy: 417.383
[aurora930_node-9] I0628 17:46:52.451148 38913 camera_parameters.cc:152]                         cx: 316.832
[aurora930_node-9] I0628 17:46:52.451179 38913 camera_parameters.cc:153]                         cy: 188.753
[aurora930_node-9] I0628 17:46:52.451210 38913 camera_parameters.cc:154]                         k1: 0.00611878
[aurora930_node-9] I0628 17:46:52.451248 38913 camera_parameters.cc:155]                         k2: -0.0490436
[aurora930_node-9] I0628 17:46:52.451279 38913 camera_parameters.cc:156]                         p1: 0.000399548
[aurora930_node-9] I0628 17:46:52.451311 38913 camera_parameters.cc:157]                         p2: 0.000563892
[aurora930_node-9] I0628 17:46:52.451349 38913 camera_parameters.cc:158]                         k3: 0.0308458
[aurora930_node-9] I0628 17:46:52.451380 38913 camera_parameters.cc:141] BOOT_ORDER_1::  Ir to Rgb Extrinsic:
[aurora930_node-9] I0628 17:46:52.451411 38913 camera_parameters.cc:162]                 Extrinsics:
[aurora930_node-9] I0628 17:46:52.451437 38913 camera_parameters.cc:163]                         Rotation[0]: 0.999973, 0.00724076, -0.00112023
[aurora930_node-9] I0628 17:46:52.451474 38913 camera_parameters.cc:165]                         Rotation[1]: -0.00724006, 0.999973, 0.000633162
[aurora930_node-9] I0628 17:46:52.451516 38913 camera_parameters.cc:167]                         Rotation[2]: 0.00112478, -0.000625033, 0.999999
[aurora930_node-9] I0628 17:46:52.451604 38913 camera_parameters.cc:169]                         Translation: -9.88662, 0.117748, 0.603513
[aurora930_node-9] 2026-06-28 17:46:52.452 (   1.289s) [        8EE34020]      aurora900_impl.cc:578   INFO| stream_mask_:0, rgb_stream_count_:1
[imu_madgwick_filter.py-4] [INFO] [1782640012.467702793] [imu_madgwick_filter]: [imu_madgwick] init: beta=0.0330, gyro_noise=0.0010, accel_noise=0.050
[lifecycle_manager-15] [INFO] [1782640012.468912711] [lifecycle_manager_keepout]: Server keepout_filter_info_server connected with bond.
[lifecycle_manager-15] [INFO] [1782640012.469088503] [lifecycle_manager_keepout]: Managed nodes are active
[lifecycle_manager-15] [INFO] [1782640012.469161003] [lifecycle_manager_keepout]: Creating bond timer...
[imu_madgwick_filter.py-4] [INFO] [1782640012.474020259] [imu_madgwick_filter]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-4] [INFO] [1782640012.476895929] [imu_madgwick_filter]: [imu_madgwick] accel init: roll=-1.6deg, pitch=0.3deg
[bmi088_iio_bridge.py-5] [INFO] [1782640012.548644018] [bmi088_iio_bridge]: BMI088 IIO Bridge 启动 @ 100Hz -> /imu_data  [OK]
[imu_madgwick_filter.py-6] [INFO] [1782640012.573825215] [imu_madgwick_bmi088]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-6] [INFO] [1782640012.576302635] [imu_madgwick_bmi088]: [imu_madgwick] accel init: roll=-2.3deg, pitch=-3.6deg
[qr_decision-11] [INFO] [1782640012.584468062] [qr_decision]: qr_decision started: cooldown=3.0s, awaiting /sign from qr_decoder
[aurora930_node-9] 2026-06-28 17:46:52.784 (   1.621s) [        53FF57E0]deptrum_camera_aurora93:407    ERR| recv first frame time is 1782640012784
[lslidar_driver_node-2] port = /dev/ttyACM1, baud_rate = 230400
[lslidar_driver_node-2] open_port /dev/ttyACM1 OK !
[vision_ai_node-12] [INFO] [1782640016.073662868] [vision_ai_node]: 成功加载配置文件: /userdata/dev_ws/install/racing_vision_ai/share/racing_vision_ai/config/vision_ai_config.yaml
[vision_ai_node-12] [INFO] [1782640016.438294526] [vision_ai_node]: Volcengine Ark client initialized successfully
[vision_ai_node-12] [INFO] [1782640016.453017502] [vision_ai_node]: Vision AI Node initialized
[vision_ai_node-12] [INFO] [1782640016.455457255] [vision_ai_node]: Waiting for sign4return=100 signal...
[vision_ai_node-12] [INFO] [1782640016.457733425] [vision_ai_node]: Results will be published to vlm_result
[INFO] [component_container_isolated-16]: process started with pid [39170]
[bmi088_iio_bridge.py-5] [INFO] [1782640017.811188218] [bmi088_iio_bridge]:   gyro bias calibrated: (0.003066, 0.000994, -0.003082) rad/s
[INFO] [competition_master_stage3.py-17]: process started with pid [39172]
[INFO] [rviz2-18]: process started with pid [39176]
[component_container_isolated-16] [INFO] [1782640018.795902555] [nav2_container]: Load Library: /opt/ros/humble/lib/libcontroller_server_core.so
[component_container_isolated-16] [INFO] [1782640018.824594007] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-16] [INFO] [1782640018.824770132] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-16] [INFO] [1782640018.897760056] [controller_server]:
[component_container_isolated-16]       controller_server lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782640018.922892670] [controller_server]: Creating controller server
[component_container_isolated-16] [INFO] [1782640019.000820433] [local_costmap.local_costmap]:
[component_container_isolated-16]       local_costmap lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782640019.003373519] [local_costmap.local_costmap]: Creating Costmap
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/controller_server' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782640019.024904587] [nav2_container]: Load Library: /opt/ros/humble/lib/libmap_server_core.so
[component_container_isolated-16] [INFO] [1782640019.077216943] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::CostmapFilterInfoServer>
[component_container_isolated-16] [INFO] [1782640019.077447027] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapSaver>
[component_container_isolated-16] [INFO] [1782640019.077552402] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-16] [INFO] [1782640019.077631819] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-16] [INFO] [1782640019.131945511] [map_server]:
[component_container_isolated-16]       map_server lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782640019.132386720] [map_server]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/map_server' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782640019.138504685] [nav2_container]: Load Library: /opt/ros/humble/lib/libsmoother_server_core.so
[component_container_isolated-16] [INFO] [1782640019.145837194] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-16] [INFO] [1782640019.146011486] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-16] [INFO] [1782640019.228161754] [smoother_server]:
[component_container_isolated-16]       smoother_server lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782640019.240173227] [smoother_server]: Creating smoother server
[component_container_isolated-16] [INFO] [1782640019.252187950] [nav2_container]: Load Library: /opt/ros/humble/lib/libamcl_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/smoother_server' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782640019.262722255] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-16] [INFO] [1782640019.262923589] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-16] [INFO] [1782640019.343406521] [amcl]:
[component_container_isolated-16]       amcl lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782640019.345661732] [amcl]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/amcl' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782640019.430317670] [nav2_container]: Load Library: /opt/ros/humble/lib/libplanner_server_core.so
[component_container_isolated-16] [INFO] [1782640019.435120759] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-16] [INFO] [1782640019.435285259] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-16] [INFO] [1782640019.522733908] [planner_server]:
[component_container_isolated-16]       planner_server lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782640019.532781296] [planner_server]: Creating
[component_container_isolated-16] [INFO] [1782640019.604592842] [global_costmap.global_costmap]:
[component_container_isolated-16]       global_costmap lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782640019.607481304] [global_costmap.global_costmap]: Creating Costmap
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/planner_server' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782640019.637332174] [nav2_container]: Load Library: /opt/ros/humble/lib/libnav2_lifecycle_manager_core.so
[component_container_isolated-16] [INFO] [1782640019.640899970] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-16] [INFO] [1782640019.641107679] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-16] [INFO] [1782640019.697931624] [lifecycle_manager_localization]: Creating
[component_container_isolated-16] [INFO] [1782640019.722083987] [lifecycle_manager_localization]: Creating and initializing lifecycle service clients
[component_container_isolated-16] [INFO] [1782640019.722747029] [nav2_container]: Load Library: /opt/ros/humble/lib/libbehavior_server_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_localization' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782640019.747807477] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-16] [INFO] [1782640019.747980144] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-16] [INFO] [1782640019.776242012] [lifecycle_manager_localization]: Starting managed nodes bringup...
[component_container_isolated-16] [INFO] [1782640019.779515183] [lifecycle_manager_localization]: Configuring map_server
[component_container_isolated-16] [INFO] [1782640019.782008936] [map_server]: Configuring
[component_container_isolated-16] [INFO] [1782640019.782625603] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.yaml
[component_container_isolated-16] [INFO] [1782640019.784149147] [map_io]: resolution: 0.05
[component_container_isolated-16] [INFO] [1782640019.784256522] [map_io]: origin[0]: -2.65
[component_container_isolated-16] [INFO] [1782640019.784289647] [map_io]: origin[1]: -4.5
[component_container_isolated-16] [INFO] [1782640019.784317439] [map_io]: origin[2]: 0
[component_container_isolated-16] [INFO] [1782640019.784347022] [map_io]: free_thresh: 0.25
[component_container_isolated-16] [INFO] [1782640019.784375480] [map_io]: occupied_thresh: 0.65
[component_container_isolated-16] [INFO] [1782640019.784419397] [map_io]: mode: trinary
[component_container_isolated-16] [INFO] [1782640019.784451355] [map_io]: negate: 0
[component_container_isolated-16] [INFO] [1782640019.785240148] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm
[component_container_isolated-16] [INFO] [1782640019.821099192] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm: 163 X 141 map @ 0.05 m/cell
[component_container_isolated-16] [INFO] [1782640019.840263966] [behavior_server]:
[component_container_isolated-16]       behavior_server lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782640019.848852060] [lifecycle_manager_localization]: Configuring amcl
[component_container_isolated-16] [INFO] [1782640019.849818519] [amcl]: Configuring
[component_container_isolated-16] [INFO] [1782640019.850258020] [amcl]: initTransforms
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/behavior_server' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782640019.892966781] [nav2_container]: Load Library: /opt/ros/humble/lib/libbt_navigator_core.so
[component_container_isolated-16] [INFO] [1782640019.904174461] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-16] [INFO] [1782640019.904349420] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-16] [INFO] [1782640019.920457731] [amcl]: initPubSub
[component_container_isolated-16] [INFO] [1782640019.961675407] [amcl]: Subscribed to map topic.
[component_container_isolated-16] [INFO] [1782640019.990759318] [lifecycle_manager_localization]: Activating map_server
[component_container_isolated-16] [INFO] [1782640019.991629610] [map_server]: Activating
[component_container_isolated-16] [INFO] [1782640019.992161944] [map_server]: Creating bond (map_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640019.994232780] [amcl]: Received a 163 X 141 map @ 0.050 m/pix
[component_container_isolated-16] [INFO] [1782640020.039475753] [bt_navigator]:
[component_container_isolated-16]       bt_navigator lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/bt_navigator' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782640020.039812628] [bt_navigator]: Creating
[component_container_isolated-16] [INFO] [1782640020.061029987] [nav2_container]: Load Library: /opt/ros/humble/lib/libwaypoint_follower_core.so
[component_container_isolated-16] [INFO] [1782640020.064073783] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-16] [INFO] [1782640020.064281991] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-16] [INFO] [1782640020.120304435] [lifecycle_manager_localization]: Server map_server connected with bond.
[component_container_isolated-16] [INFO] [1782640020.120469436] [lifecycle_manager_localization]: Activating amcl
[component_container_isolated-16] [INFO] [1782640020.121354062] [amcl]: Activating
[component_container_isolated-16] [INFO] [1782640020.121578020] [amcl]: initialPoseReceived
[component_container_isolated-16] [INFO] [1782640020.122052688] [amcl]: Setting pose (1782640020.122047): -1.985 -0.014 0.262
[component_container_isolated-16] [INFO] [1782640020.123918231] [amcl]: Creating bond (amcl) to lifecycle manager.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/waypoint_follower' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782640020.146131175] [waypoint_follower]:
[component_container_isolated-16]       waypoint_follower lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1782640020.149055304] [waypoint_follower]: Creating
[component_container_isolated-16] [INFO] [1782640020.152276516] [amcl]: createLaserObject
[component_container_isolated-16] [INFO] [1782640020.172752250] [nav2_container]: Load Library: /opt/ros/humble/lib/libvelocity_smoother_core.so
[component_container_isolated-16] [INFO] [1782640020.176309713] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-16] [INFO] [1782640020.176463963] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-16] [INFO] [1782640020.236386370] [lifecycle_manager_localization]: Server amcl connected with bond.
[component_container_isolated-16] [INFO] [1782640020.236568745] [lifecycle_manager_localization]: Managed nodes are active
[component_container_isolated-16] [INFO] [1782640020.236686704] [lifecycle_manager_localization]: Creating bond timer...
[component_container_isolated-16] [INFO] [1782640020.290885645] [velocity_smoother]:
[component_container_isolated-16]       velocity_smoother lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/velocity_smoother' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782640020.306241872] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-16] [INFO] [1782640020.306423289] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-16] [INFO] [1782640020.402642658] [lifecycle_manager_navigation]: Creating
[component_container_isolated-16] [INFO] [1782640020.447042546] [lifecycle_manager_navigation]: Creating and initializing lifecycle service clients
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_navigation' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1782640020.544412540] [lifecycle_manager_navigation]: Starting managed nodes bringup...
[component_container_isolated-16] [INFO] [1782640020.544922458] [lifecycle_manager_navigation]: Configuring controller_server
[component_container_isolated-16] [INFO] [1782640020.547649461] [controller_server]: Configuring controller interface
[component_container_isolated-16] [INFO] [1782640020.548701254] [controller_server]: getting goal checker plugins..
[component_container_isolated-16] [INFO] [1782640020.555775554] [controller_server]: Controller frequency set to 10.0000Hz
[component_container_isolated-16] [INFO] [1782640020.556152763] [local_costmap.local_costmap]: Configuring
[component_container_isolated-16] [INFO] [1782640020.596542271] [local_costmap.local_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-16] [INFO] [1782640020.631823690] [local_costmap.local_costmap]: Subscribed to Topics: scan aurora_points
[component_container_isolated-16] [INFO] [1782640020.742622993] [local_costmap.local_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-16] [INFO] [1782640020.742803534] [local_costmap.local_costmap]: Using plugin "keepout_filter"
[component_container_isolated-16] [INFO] [1782640020.768787066] [local_costmap.local_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-16] [INFO] [1782640020.770423735] [local_costmap.local_costmap]: Using plugin "inflation_layer"
[component_container_isolated-16] [INFO] [1782640020.791403053] [local_costmap.local_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-16] [INFO] [1782640020.852240086] [controller_server]: Created progress_checker : progress_checker of type nav2_controller::SimpleProgressChecker
[component_container_isolated-16] [INFO] [1782640020.859769220] [controller_server]: Created goal checker : goal_checker of type nav2_controller::SimpleGoalChecker
[component_container_isolated-16] [INFO] [1782640020.871954735] [controller_server]: Controller Server has goal_checker  goal checkers available.
[component_container_isolated-16] [INFO] [1782640020.877616742] [controller_server]: Created controller : FollowPath of type nav2_regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-16] [INFO] [1782640020.979094658] [controller_server]: Controller Server has FollowPath  controllers available.
[component_container_isolated-16] [INFO] [1782640021.030676222] [lifecycle_manager_navigation]: Configuring smoother_server
[component_container_isolated-16] [INFO] [1782640021.033007975] [smoother_server]: Configuring smoother server
[component_container_isolated-16] [INFO] [1782640021.109094193] [smoother_server]: Created smoother : SmoothPath of type nav2_constrained_smoother/ConstrainedSmoother
[component_container_isolated-16] [INFO] [1782640021.164242344] [smoother_server]: Smoother Server has SmoothPath  smoothers available.
[component_container_isolated-16] [INFO] [1782640021.204080643] [lifecycle_manager_navigation]: Configuring planner_server
[component_container_isolated-16] [INFO] [1782640021.204965270] [planner_server]: Configuring
[component_container_isolated-16] [INFO] [1782640021.205279353] [global_costmap.global_costmap]: Configuring
[component_container_isolated-16] [INFO] [1782640021.247895614] [global_costmap.global_costmap]: Using plugin "static_layer"
[component_container_isolated-16] [INFO] [1782640021.272622728] [global_costmap.global_costmap]: Subscribing to the map topic (/map) with transient local durability
[component_container_isolated-16] [INFO] [1782640021.277577817] [global_costmap.global_costmap]: Initialized plugin "static_layer"
[component_container_isolated-16] [INFO] [1782640021.277737609] [global_costmap.global_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-16] [INFO] [1782640021.288184330] [global_costmap.global_costmap]: Subscribed to Topics: scan aurora_points
[component_container_isolated-16] [INFO] [1782640021.366322135] [global_costmap.global_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-16] [INFO] [1782640021.366487218] [global_costmap.global_costmap]: Using plugin "keepout_filter"
[component_container_isolated-16] [INFO] [1782640021.384735991] [global_costmap.global_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-16] [INFO] [1782640021.384909699] [global_costmap.global_costmap]: Using plugin "inflation_layer"
[component_container_isolated-16] [INFO] [1782640021.400784635] [global_costmap.global_costmap]: Initialized plugin "inflation_layer"
[competition_master_stage3.py-17] [INFO] [1782640021.402419137] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-17] [INFO] [1782640021.407184935] [competition_master_stage3]: === [Stage 3] 总控节点初始化 ===
[competition_master_stage3.py-17] [INFO] [1782640021.412327316] [competition_master_stage3]:   QR点:    (0.41, -3.17, yaw=0.00)
[competition_master_stage3.py-17] [INFO] [1782640021.419199825] [competition_master_stage3]:   通道入口: (0.38, -1.10, yaw=0.00)
[competition_master_stage3.py-17] [INFO] [1782640021.423912789] [competition_master_stage3]:   P点:     (-1.99, -0.01, yaw=0.26)
[competition_master_stage3.py-17] [INFO] [1782640021.429232795] [competition_master_stage3]:   cruise_cw: 3 路点 → VLM=(3.01, -1.16)
[competition_master_stage3.py-17] [INFO] [1782640021.434413010] [competition_master_stage3]:   cruise_ccw: 4 路点 → VLM=(2.17, 0.69)
[competition_master_stage3.py-17] [INFO] [1782640021.445415065] [competition_master_stage3]:   超时: total=180.0s QR=90.0s entry=60.0s cruise=180.0s vlm=30.0s return=120.0s
[competition_master_stage3.py-17] [INFO] [1782640021.449340945] [competition_master_stage3]:   回退QR方向: 逆时针
[competition_master_stage3.py-17] [INFO] [1782640021.453997659] [competition_master_stage3]:   VLM结果话题: vlm_result
[competition_master_stage3.py-17] [INFO] [1782640021.458749123] [competition_master_stage3]: ============================================================
[component_container_isolated-16] [INFO] [1782640021.469101844] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 163 X 141 at 0.050000 m/pix
[component_container_isolated-16] [INFO] [1782640021.493349166] [planner_server]: Created global planner plugin GridBased of type nav2_smac_planner/SmacPlannerHybrid
[component_container_isolated-16] [INFO] [1782640021.494189625] [planner_server]: Configuring GridBased of type SmacPlannerHybrid
[component_container_isolated-16] [INFO] [1782640021.536715136] [planner_server]: Even sized heuristic lookup table size set 200.000000, increasing size by 1 to make odd
[imu_madgwick_filter.py-6] [INFO] [1782640022.309602794] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=462 q_w=0.9993 angle=4.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782640022.332512614] [imu_madgwick_filter]: [imu_madgwick ->] msgs=200 q_w=0.9966 angle=9.4deg beta=0.0330
[rviz2-18] [INFO] [1782640023.110000278] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-18] [INFO] [1782640023.110898154] [rviz2]: OpenGl version: 4.5 (GLSL 4.5)
[rviz2-18] [INFO] [1782640023.534927466] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-18] [INFO] [1782640026.076164085] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[rviz2-18] [ERROR] [1782640026.480546998] [rviz2]: Vertex Program:rviz/glsl120/indexed_8bit_image.vert Fragment Program:rviz/glsl120/indexed_8bit_image.frag GLSL link result :
[rviz2-18] active samplers with a different type refer to the same texture image unit
[qr_decoder-10] [INFO] [1782640027.989525681] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=200 last_qr_frame=-1 gap=-1 frames rejects=0
[imu_madgwick_filter.py-6] [INFO] [1782640032.309844011] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1052 q_w=0.9994 angle=4.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782640032.344978596] [imu_madgwick_filter]: [imu_madgwick ->] msgs=400 q_w=0.9866 angle=18.8deg beta=0.0330
[component_container_isolated-16] Reallocing temp weights 301 - 60
[competition_master_stage3.py-17] [INFO] [1782640037.727818001] [competition_master_stage3]: [DIAG] state=INIT pos=(-2.00,-0.02) yaw=19deg cmd=(vx=0.00 wz=0.00) elapsed=0.0s cpuFreq=1500MHz cpuT=78C cpu=62% mem=17%
[component_container_isolated-16] [INFO] [1782640037.860090954] [planner_server]: Configured plugin GridBased of type SmacPlannerHybrid with maximum iterations 2027, max on approach iterations 300, and not allowing unknown traversal. Tolerance 0.50.Using motion model: Reeds-Shepp.
[component_container_isolated-16] [INFO] [1782640037.861159164] [planner_server]: Planner Server has GridBased  planners available.
[component_container_isolated-16] [INFO] [1782640037.914419771] [lifecycle_manager_navigation]: Configuring behavior_server
[component_container_isolated-16] [INFO] [1782640037.919339068] [behavior_server]: Configuring
[component_container_isolated-16] [INFO] [1782640037.955761196] [behavior_server]: Creating behavior plugin spin of type nav2_behaviors/Spin
[component_container_isolated-16] [INFO] [1782640037.959456325] [behavior_server]: Configuring spin
[component_container_isolated-16] [INFO] [1782640038.007748884] [behavior_server]: Creating behavior plugin backup of type nav2_behaviors/BackUp
[component_container_isolated-16] [INFO] [1782640038.011478306] [behavior_server]: Configuring backup
[component_container_isolated-16] [INFO] [1782640038.057224153] [behavior_server]: Creating behavior plugin drive_on_heading of type nav2_behaviors/DriveOnHeading
[component_container_isolated-16] [INFO] [1782640038.061278491] [behavior_server]: Configuring drive_on_heading
[component_container_isolated-16] [INFO] [1782640038.100938873] [behavior_server]: Creating behavior plugin wait of type nav2_behaviors/Wait
[component_container_isolated-16] [INFO] [1782640038.106663505] [behavior_server]: Configuring wait
[component_container_isolated-16] [INFO] [1782640038.138365127] [lifecycle_manager_navigation]: Configuring bt_navigator
[component_container_isolated-16] [INFO] [1782640038.139455170] [bt_navigator]: Configuring
[competition_master_stage3.py-17] [INFO] [1782640038.490030806] [competition_master_stage3]: [LAUNCH] 发车阶段: 17.3s
[competition_master_stage3.py-17] [INFO] [1782640038.495345354] [competition_master_stage3]: >>> 系统就绪, 开始 Stage 3 导航
[competition_master_stage3.py-17] [INFO] [1782640038.508851912] [competition_master_stage3]: [BAG] 录制开始: stage3_20260628_174718
[competition_master_stage3.py-17] [INFO] [1782640038.516093712] [competition_master_stage3]: [状态机] INIT → NAV_TO_QR
[competition_master_stage3.py-17] [INFO] [1782640038.543078495] [competition_master_stage3]: [DIAG] nav目标距离: 3.97m, robot=(-2.00,-0.02) → target=(0.41,-3.17)
[competition_master_stage3.py-17] [INFO] [1782640038.547736959] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-16] [INFO] [1782640038.567893400] [lifecycle_manager_navigation]: Configuring waypoint_follower
[component_container_isolated-16] [INFO] [1782640038.569288694] [waypoint_follower]: Configuring
[competition_master_stage3.py-17] [WARN] [1782640038.579459290] [competition_master_stage3]: 导航目标被拒绝, 3s 后重试...
[component_container_isolated-16] [INFO] [1782640038.673765488] [waypoint_follower]: Created waypoint_task_executor : wait_at_waypoint of type nav2_waypoint_follower::WaitAtWaypoint
[component_container_isolated-16] [INFO] [1782640038.682809040] [lifecycle_manager_navigation]: Configuring velocity_smoother
[component_container_isolated-16] [INFO] [1782640038.684202417] [velocity_smoother]: Configuring velocity smoother
[component_container_isolated-16] [INFO] [1782640038.719591835] [lifecycle_manager_navigation]: Activating controller_server
[component_container_isolated-16] [INFO] [1782640038.720751753] [controller_server]: Activating
[component_container_isolated-16] [INFO] [1782640038.721083504] [local_costmap.local_costmap]: Activating
[component_container_isolated-16] [INFO] [1782640038.721274296] [local_costmap.local_costmap]: Checking transform
[component_container_isolated-16] [INFO] [1782640038.721848296] [local_costmap.local_costmap]: start
[component_container_isolated-16] [INFO] [1782640038.739128817] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640038.753910294] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640038.754236461] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640038.770297480] [local_costmap.local_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[component_container_isolated-16] [INFO] [1782640039.006220226] [controller_server]: Activating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-16] [INFO] [1782640039.006519185] [controller_server]: Creating bond (controller_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640039.125586288] [lifecycle_manager_navigation]: Server controller_server connected with bond.
[component_container_isolated-16] [INFO] [1782640039.125808622] [lifecycle_manager_navigation]: Activating smoother_server
[component_container_isolated-16] [INFO] [1782640039.129075293] [smoother_server]: Activating
[component_container_isolated-16] [INFO] [1782640039.129325001] [smoother_server]: Activating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-16] [INFO] [1782640039.129422043] [smoother_server]: Creating bond (smoother_server) to lifecycle manager.
[competition_master_stage3.py-17] [INFO] [1782640039.217737567] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.03,-0.03) yaw=19deg cmd=(vx=0.00 wz=0.00) elapsed=0.6s cpuFreq=1500MHz cpuT=79C cpu=66% mem=17%
[component_container_isolated-16] [INFO] [1782640039.258546534] [lifecycle_manager_navigation]: Server smoother_server connected with bond.
[component_container_isolated-16] [INFO] [1782640039.258900909] [lifecycle_manager_navigation]: Activating planner_server
[component_container_isolated-16] [INFO] [1782640039.263674373] [planner_server]: Activating
[component_container_isolated-16] [INFO] [1782640039.264014665] [global_costmap.global_costmap]: Activating
[component_container_isolated-16] [INFO] [1782640039.264107124] [global_costmap.global_costmap]: Checking transform
[component_container_isolated-16] [INFO] [1782640039.264436958] [global_costmap.global_costmap]: start
[component_container_isolated-16] [INFO] [1782640039.271652383] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640039.281383312] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640039.281565228] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640039.288643654] [global_costmap.global_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[rviz2-18] [INFO] [1782640039.590812147] [rviz2]: Trying to create a map of size 60 x 60 using 1 swatches
[component_container_isolated-16] [INFO] [1782640040.381282234] [planner_server]: Activating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-16] [INFO] [1782640040.386226949] [planner_server]: Creating bond (planner_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640040.502833716] [lifecycle_manager_navigation]: Server planner_server connected with bond.
[component_container_isolated-16] [INFO] [1782640040.502979966] [lifecycle_manager_navigation]: Activating behavior_server
[component_container_isolated-16] [INFO] [1782640040.504143634] [behavior_server]: Activating
[component_container_isolated-16] [INFO] [1782640040.504273843] [behavior_server]: Activating spin
[component_container_isolated-16] [INFO] [1782640040.504576260] [behavior_server]: Activating backup
[component_container_isolated-16] [INFO] [1782640040.504826885] [behavior_server]: Activating drive_on_heading
[component_container_isolated-16] [INFO] [1782640040.504915510] [behavior_server]: Activating wait
[component_container_isolated-16] [INFO] [1782640040.505036385] [behavior_server]: Creating bond (behavior_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640040.623189987] [lifecycle_manager_navigation]: Server behavior_server connected with bond.
[component_container_isolated-16] [INFO] [1782640040.623373279] [lifecycle_manager_navigation]: Activating bt_navigator
[component_container_isolated-16] [INFO] [1782640040.624699031] [bt_navigator]: Activating
[rviz2-18] [INFO] [1782640040.726229988] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[component_container_isolated-16] [WARN] [1782640040.776614799] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-16] [WARN] [1782640040.847786969] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-16] [WARN] [1782640040.910920004] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-16] [WARN] [1782640041.102460363] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[competition_master_stage3.py-17] [INFO] [1782640041.218996921] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.03,-0.03) yaw=19deg cmd=(vx=0.00 wz=0.00) elapsed=2.7s cpuFreq=1500MHz cpuT=80C cpu=100% mem=18%
[component_container_isolated-16] [WARN] [1782640041.328917555] [bt_navigator_navigate_to_pose_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-16] [INFO] [1782640041.477527444] [bt_navigator]: Creating bond (bt_navigator) to lifecycle manager.
[competition_master_stage3.py-17] [INFO] [1782640041.586444910] [competition_master_stage3]: 重试发送导航目标 (QR点)...
[competition_master_stage3.py-17] [INFO] [1782640041.593395502] [competition_master_stage3]: [DIAG] nav目标距离: 3.98m, robot=(-2.03,-0.03) → target=(0.41,-3.17)
[component_container_isolated-16] [INFO] [1782640041.595488088] [lifecycle_manager_navigation]: Server bt_navigator connected with bond.
[component_container_isolated-16] [INFO] [1782640041.595659838] [lifecycle_manager_navigation]: Activating waypoint_follower
[competition_master_stage3.py-17] [INFO] [1782640041.596632089] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-16] [INFO] [1782640041.598071924] [waypoint_follower]: Activating
[component_container_isolated-16] [INFO] [1782640041.598339258] [waypoint_follower]: Creating bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640041.601274970] [bt_navigator]: Begin navigating from current location (-2.03, -0.03) to (0.41, -3.17)
[competition_master_stage3.py-17] [INFO] [1782640041.629214420] [competition_master_stage3]: 导航目标已接受，车辆出发...
[component_container_isolated-16] [INFO] [1782640041.724090411] [lifecycle_manager_navigation]: Server waypoint_follower connected with bond.
[component_container_isolated-16] [INFO] [1782640041.724245578] [lifecycle_manager_navigation]: Activating velocity_smoother
[component_container_isolated-16] [INFO] [1782640041.726032871] [velocity_smoother]: Activating
[component_container_isolated-16] [INFO] [1782640041.726378247] [velocity_smoother]: Creating bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640041.843294306] [lifecycle_manager_navigation]: Server velocity_smoother connected with bond.
[component_container_isolated-16] [INFO] [1782640041.843460806] [lifecycle_manager_navigation]: Managed nodes are active
[component_container_isolated-16] [INFO] [1782640041.843525431] [lifecycle_manager_navigation]: Creating bond timer...
[component_container_isolated-16] [WARN] [1782640042.293536103] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4532 Hz
[imu_madgwick_filter.py-6] [INFO] [1782640042.309985290] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1565 q_w=0.9993 angle=4.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782640042.332994235] [imu_madgwick_filter]: [imu_madgwick ->] msgs=600 q_w=0.9699 angle=28.2deg beta=0.0330
[component_container_isolated-16] [INFO] [1782640042.403781863] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-16] [WARN] [1782640042.404248946] [controller_server]: No goal checker was specified in parameter 'current_goal_checker'. Server will use only plugin loaded goal_checker . This warning will appear once.
[competition_master_stage3.py-17] [INFO] [1782640043.204124794] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.03,-0.03) yaw=19deg cmd=(vx=0.27 wz=-0.97) elapsed=4.6s plan[28pts 4.1m] (-2.00,-0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=79C cpu=57% mem=18%
[qr_decoder-10] [INFO] [1782640043.778953410] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=400 last_qr_frame=-1 gap=-1 frames rejects=0
[component_container_isolated-16] [WARN] [1782640044.290667157] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2715 Hz
[component_container_isolated-16] [INFO] [1782640044.404583587] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640045.204038933] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.56,-0.19) yaw=-51deg cmd=(vx=0.40 wz=0.14) elapsed=6.6s plan[26pts 3.8m] (-1.70,-0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=80C cpu=25% mem=19%
[component_container_isolated-16] [WARN] [1782640046.286583539] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2903 Hz
[component_container_isolated-16] [INFO] [1782640046.404553849] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640047.204149820] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.30,-0.60) yaw=-53deg cmd=(vx=0.40 wz=-0.13) elapsed=8.6s plan[22pts 3.1m] (-1.30,-0.65)→(0.40,-3.15) cpuFreq=1500MHz cpuT=80C cpu=42% mem=19%
[component_container_isolated-16] Reallocing temp weights 642 - 60
[component_container_isolated-16] [WARN] [1782640048.287001091] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2768 Hz
[component_container_isolated-16] [INFO] [1782640048.404566067] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640049.207301749] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.93,-1.08) yaw=-55deg cmd=(vx=0.40 wz=-0.14) elapsed=10.6s plan[20pts 2.8m] (-1.10,-0.85)→(0.40,-3.15) cpuFreq=1500MHz cpuT=80C cpu=100% mem=19%
[component_container_isolated-16] Reallocing temp weights 1500 - 60
[component_container_isolated-16] [WARN] [1782640050.286852474] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2772 Hz
[component_container_isolated-16] [INFO] [1782640050.404674825] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640051.206495588] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.77,-1.36) yaw=-66deg cmd=(vx=0.40 wz=-0.13) elapsed=12.6s plan[15pts 2.0m] (-0.70,-1.55)→(0.40,-3.15) cpuFreq=1500MHz cpuT=80C cpu=92% mem=19%
[imu_madgwick_filter.py-4] [WARN] [1782640052.224930237] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.2013s > 0.15s, capping
[component_container_isolated-16] [WARN] [1782640052.286314728] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2785 Hz
[imu_madgwick_filter.py-6] [INFO] [1782640052.310238632] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2062 q_w=0.7252 angle=87.0deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782640052.332799909] [imu_madgwick_filter]: [imu_madgwick ->] msgs=791 q_w=0.9026 angle=51.0deg beta=0.0330
[component_container_isolated-16] [INFO] [1782640052.404574121] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640053.204015630] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.50,-1.88) yaw=-65deg cmd=(vx=0.40 wz=0.05) elapsed=14.6s plan[13pts 1.8m] (-0.60,-1.75)→(0.40,-3.15) cpuFreq=1500MHz cpuT=80C cpu=37% mem=19%
[qr_decoder-10] [INFO] [1782640053.262828868] [qr_decoder_zbar]: [qr_decoder] QR DETECTED frame=526 symbols=1 (gap=-1 frames)
[qr_decoder-10] [INFO] [1782640053.263079243] [qr_decoder_zbar]: [QR] 1585 | 3D:(-0.490, +0.183, 1.760)m | px(203,241) D:1760mm
[qr_decoder-10] [INFO] [1782640053.263604119] [qr_decoder_zbar]: [QR] 1585 | robot_pos: (0.24, -2.59, yaw=-1.79)
[qr_decision-11] [INFO] [1782640053.267397832] [qr_decision]: [QR] 1585 CW @ (x=0.24, y=-2.59, yaw=-1.79) → /qr_event
[competition_master_stage3.py-17] [INFO] [1782640053.270257377] [competition_master_stage3]: [QR检测] 内容: 1585
[qr_decision-11] [INFO] [1782640053.270544419] [qr_decision]: [检查点] qr_decision 发布 /qr_event (由 task_manager 决定停车)
[competition_master_stage3.py-17] [INFO] [1782640053.277128427] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decoder_zbar
[competition_master_stage3.py-17] [INFO] [1782640053.281215640] [competition_master_stage3]: >>> QR 解码已关闭, 等待方向判断 (/qr_event)...
[competition_master_stage3.py-17] [INFO] [1782640053.285202854] [competition_master_stage3]: [QR检测] 取消当前导航目标, 等待BT完成 cancel/halt 清理...
[competition_master_stage3.py-17] [INFO] [1782640053.298643620] [competition_master_stage3]: [QR事件] 方向: 顺时针 (通道巡航阶段使用)
[component_container_isolated-16] [INFO] [1782640053.304592669] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-16] [INFO] [1782640053.304997294] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-16] [INFO] [1782640053.306840921] [bt_navigator]: [navigate_to_pose] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-16] [INFO] [1782640053.307816006] [bt_navigator]: Goal canceled
[competition_master_stage3.py-17] [INFO] [1782640053.311149510] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decision
[competition_master_stage3.py-17] [INFO] [1782640053.337871626] [competition_master_stage3]: [结果回调] BT取消确认完成 (STATUS_CANCELED), 准备发送通道入口目标...
[qr_decoder-10] [INFO] [1782640053.338669627] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[competition_master_stage3.py-17] [INFO] [1782640053.344736301] [competition_master_stage3]: [状态机] NAV_TO_QR → BACKING_UP
[competition_master_stage3.py-17] [INFO] [1782640053.353055269] [competition_master_stage3]: >>> BT取消完成, 右后退摆正车头→前进进通道...
[competition_master_stage3.py-17] [INFO] [1782640053.367268911] [competition_master_stage3]: [BACKUP] 右后退中: vx=-0.15 wz=0.80, 持续 6.0s...
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
[INFO] [qr_decoder-10]: process has finished cleanly [pid 38915]
[ERROR] [qr_decision-11]: process has died [pid 38917, exit code 1, cmd '/userdata/dev_ws/install/origincar_qr/lib/origincar_qr/qr_decision --ros-args -r __node:=qr_decision --params-file /tmp/launch_params_14x73qgy'].
[competition_master_stage3.py-17] [INFO] [1782640055.203955048] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.34,-2.17) yaw=-59deg cmd=(vx=-0.15 wz=0.80) elapsed=16.6s plan[13pts 1.8m] (-0.60,-1.75)→(0.40,-3.15) cpuFreq=1500MHz cpuT=80C cpu=33% mem=18%
[competition_master_stage3.py-17] [INFO] [1782640057.202773338] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.38,-2.17) yaw=-27deg cmd=(vx=-0.15 wz=0.80) elapsed=18.6s plan[13pts 1.8m] (-0.60,-1.75)→(0.40,-3.15) cpuFreq=1500MHz cpuT=80C cpu=28% mem=18%
[competition_master_stage3.py-17] [INFO] [1782640059.204202169] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.66,-2.13) yaw=29deg cmd=(vx=-0.15 wz=0.80) elapsed=20.6s plan[13pts 1.8m] (-0.60,-1.75)→(0.40,-3.15) cpuFreq=1500MHz cpuT=79C cpu=28% mem=18%
[competition_master_stage3.py-17] [INFO] [1782640059.370628953] [competition_master_stage3]: [状态机] BACKING_UP → CRUISE_CHANNEL
[competition_master_stage3.py-17] [INFO] [1782640059.375015625] [competition_master_stage3]: [CRUISE] 方向: CW (顺时针, odd QR), 路点: (0.93,0.11), (2.19,0.77), (3.01,-1.16)
[competition_master_stage3.py-17] [INFO] [1782640059.386604306] [competition_master_stage3]: [CRUISE] NavigateThroughPoses: (0.38,-1.10), (0.93,0.11), (2.19,0.77), (3.01,-1.16)
[component_container_isolated-16] [INFO] [1782640059.389712976] [bt_navigator]: Begin navigating from current location through 4 poses to (3.01, -1.16)
[competition_master_stage3.py-17] [INFO] [1782640059.402779784] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[component_container_isolated-16] [WARN] [1782640060.310243628] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.0900 Hz
[component_container_isolated-16] [INFO] [1782640060.491581805] [controller_server]: Received a goal, begin computing control effort.
[competition_master_stage3.py-17] [INFO] [1782640061.210596463] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.74,-2.19) yaw=45deg cmd=(vx=0.40 wz=-0.27) elapsed=22.6s plan[61pts 8.7m] (-0.80,-2.25)→(3.00,-1.15) cpuFreq=1500MHz cpuT=80C cpu=57% mem=18%
[component_container_isolated-16] [WARN] [1782640062.298516232] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4175 Hz
[imu_madgwick_filter.py-6] [INFO] [1782640062.311813289] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2593 q_w=0.9857 angle=19.4deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782640062.335462943] [imu_madgwick_filter]: [imu_madgwick ->] msgs=991 q_w=0.8483 angle=63.9deg beta=0.0330
[component_container_isolated-16] [INFO] [1782640062.492528465] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640063.203110612] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.35,-1.80) yaw=39deg cmd=(vx=0.40 wz=0.25) elapsed=24.6s plan[58pts 8.2m] (-0.50,-1.95)→(3.00,-1.15) cpuFreq=1500MHz cpuT=79C cpu=16% mem=18%
[component_container_isolated-16] [WARN] [1782640064.296469553] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4193 Hz
[component_container_isolated-16] [INFO] [1782640064.493199914] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640065.215455700] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.04,-1.44) yaw=48deg cmd=(vx=0.40 wz=-0.25) elapsed=26.6s plan[53pts 7.5m] (-0.00,-1.45)→(3.00,-1.15) cpuFreq=1500MHz cpuT=80C cpu=93% mem=18%
[component_container_isolated-16] [WARN] [1782640066.295818915] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4212 Hz
[component_container_isolated-16] [INFO] [1782640066.492435026] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640067.203858506] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.32,-1.16) yaw=22deg cmd=(vx=0.40 wz=0.68) elapsed=28.6s plan[51pts 7.2m] (0.20,-1.25)→(3.00,-1.15) cpuFreq=1500MHz cpuT=79C cpu=62% mem=18%
[component_container_isolated-16] [WARN] [1782640068.293327398] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4255 Hz
[component_container_isolated-16] [INFO] [1782640068.592493132] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640069.203675657] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.77,-0.81) yaw=55deg cmd=(vx=0.40 wz=0.43) elapsed=30.6s plan[46pts 6.4m] (0.80,-0.85)→(3.00,-1.15) cpuFreq=1500MHz cpuT=80C cpu=55% mem=18%
[component_container_isolated-16] [WARN] [1782640070.295144466] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4228 Hz
[component_container_isolated-16] [INFO] [1782640070.492444078] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640071.203265347] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.95,-0.40) yaw=66deg cmd=(vx=0.40 wz=0.18) elapsed=32.6s plan[45pts 6.4m] (0.80,-0.65)→(3.00,-1.15) cpuFreq=1500MHz cpuT=79C cpu=62% mem=18%
[component_container_isolated-16] [WARN] [1782640072.289644274] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4350 Hz
[imu_madgwick_filter.py-6] [INFO] [1782640072.310757507] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3133 q_w=0.8824 angle=56.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782640072.333293493] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1188 q_w=0.5672 angle=110.9deg beta=0.0330
[component_container_isolated-16] [INFO] [1782640072.492474017] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640073.204121661] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.03,-0.15) yaw=75deg cmd=(vx=0.40 wz=0.33) elapsed=34.6s plan[35pts 5.1m] (1.10,-0.05)→(3.00,-1.15) cpuFreq=1500MHz cpuT=79C cpu=33% mem=18%
[component_container_isolated-16] [WARN] [1782640074.286263456] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640074.286518165] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.19, 0.77)
[component_container_isolated-16] [WARN] [1782640074.286608207] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640074.390502664] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640074.400887052] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640074.409821479] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640074.410031063] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640074.410309438] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640074.410750522] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640074.422780203] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-17] [INFO] [1782640075.204298971] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.03,0.32) yaw=97deg cmd=(vx=0.31 wz=-0.24) elapsed=36.6s plan[35pts 5.1m] (1.10,-0.05)→(3.00,-1.15) cpuFreq=1500MHz cpuT=80C cpu=37% mem=18%
[component_container_isolated-16] [WARN] [1782640075.285680777] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640075.285938402] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.19, 0.77)
[component_container_isolated-16] [WARN] [1782640075.286047277] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640075.392427571] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-16] [INFO] [1782640075.392619780] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-16] [INFO] [1782640075.393156281] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640075.401155123] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640075.406915339] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640075.407069797] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640075.407215089] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640075.422183982] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [WARN] [1782640075.429905991] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640075.436820666] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640075.437112292] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640075.437540167] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640075.437638834] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640075.449506723] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640075.690933845] [behavior_server]: Running backup
[component_container_isolated-16] [INFO] [1782640075.691467429] [behavior_server]: DriveOnHeading: no acceleration or deceleration limits set
[competition_master_stage3.py-17] [INFO] [1782640077.200807650] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.94,0.65) yaw=101deg cmd=(vx=-0.12 wz=0.00) elapsed=38.6s plan[35pts 5.1m] (1.10,-0.05)→(3.00,-1.15) cpuFreq=1500MHz cpuT=79C cpu=50% mem=18%
[component_container_isolated-16] [WARN] [1782640077.992024929] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640077.992198471] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640077.992297554] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640078.291191161] [behavior_server]: Running wait
[competition_master_stage3.py-17] [INFO] [1782640079.210893051] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.90,0.65) yaw=97deg cmd=(vx=0.00 wz=0.00) elapsed=40.6s plan[35pts 5.1m] (1.10,-0.05)→(3.00,-1.15) cpuFreq=1500MHz cpuT=80C cpu=92% mem=18%
[competition_master_stage3.py-17] [INFO] [1782640081.201200510] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.90,0.65) yaw=97deg cmd=(vx=0.00 wz=0.00) elapsed=42.6s plan[35pts 5.1m] (1.10,-0.05)→(3.00,-1.15) cpuFreq=1500MHz cpuT=80C cpu=50% mem=18%
[component_container_isolated-16] [INFO] [1782640081.291661951] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640082.291195559] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4346 Hz
[imu_madgwick_filter.py-6] [INFO] [1782640082.310823875] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3669 q_w=0.7674 angle=79.8deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782640082.332721067] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1384 q_w=0.3187 angle=142.8deg beta=0.0330
[component_container_isolated-16] [INFO] [1782640082.491459423] [controller_server]: Received a goal, begin computing control effort.
[competition_master_stage3.py-17] [INFO] [1782640083.204727357] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.90,0.65) yaw=97deg cmd=(vx=0.31 wz=-0.97) elapsed=44.6s plan[29pts 3.9m] (0.90,0.65)→(3.00,-1.15) cpuFreq=1500MHz cpuT=80C cpu=60% mem=18%
[component_container_isolated-16] [WARN] [1782640084.290735067] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4308 Hz
[component_container_isolated-16] [INFO] [1782640084.491880390] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640085.202533069] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.06,0.98) yaw=30deg cmd=(vx=0.40 wz=-0.34) elapsed=46.6s plan[31pts 4.3m] (0.90,0.85)→(3.00,-1.15) cpuFreq=1500MHz cpuT=80C cpu=28% mem=18%
[component_container_isolated-16] [WARN] [1782640086.288814528] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4368 Hz
[component_container_isolated-16] [INFO] [1782640086.492198187] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640087.200922697] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.42,1.11) yaw=15deg cmd=(vx=0.20 wz=-0.97) elapsed=48.6s plan[23pts 3.1m] (1.50,1.15)→(3.00,-1.15) cpuFreq=1500MHz cpuT=80C cpu=57% mem=18%
[component_container_isolated-16] [WARN] [1782640088.291675368] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4308 Hz
[component_container_isolated-16] [INFO] [1782640088.491869398] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640089.203758785] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.81,1.16) yaw=-26deg cmd=(vx=0.19 wz=-0.97) elapsed=50.6s plan[22pts 2.9m] (1.70,1.15)→(3.00,-1.15) cpuFreq=1500MHz cpuT=80C cpu=100% mem=18%
[component_container_isolated-16] [WARN] [1782640090.288424032] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4377 Hz
[component_container_isolated-16] [INFO] [1782640090.491868523] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640091.205350162] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.01,0.94) yaw=-70deg cmd=(vx=0.25 wz=0.97) elapsed=52.6s plan[19pts 2.5m] (2.00,0.95)→(3.00,-1.15) cpuFreq=1500MHz cpuT=80C cpu=86% mem=18%
[component_container_isolated-16] [WARN] [1782640092.287711780] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4418 Hz
[imu_madgwick_filter.py-6] [INFO] [1782640092.312574476] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4181 q_w=0.9246 angle=44.8deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782640092.333198542] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1583 q_w=0.9708 angle=27.8deg beta=0.0330
[component_container_isolated-16] [INFO] [1782640092.392080153] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640093.202052739] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.31,0.55) yaw=-35deg cmd=(vx=0.17 wz=-0.97) elapsed=54.6s plan[14pts 2.0m] (2.30,0.55)→(3.00,-1.15) cpuFreq=1500MHz cpuT=80C cpu=70% mem=18%
[component_container_isolated-16] [WARN] [1782640094.284455730] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2617 Hz
[component_container_isolated-16] [INFO] [1782640094.401091493] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640095.203998611] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.58,0.39) yaw=-64deg cmd=(vx=0.35 wz=-0.97) elapsed=56.6s plan[13pts 1.8m] (2.50,0.45)→(3.00,-1.15) cpuFreq=1500MHz cpuT=80C cpu=100% mem=18%
[component_container_isolated-16] [WARN] [1782640096.288525729] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2583 Hz
[component_container_isolated-16] [INFO] [1782640096.491927803] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640097.203073519] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.60,-0.16) yaw=-91deg cmd=(vx=0.40 wz=0.10) elapsed=58.6s plan[10pts 1.4m] (2.60,0.05)→(3.00,-1.15) cpuFreq=1500MHz cpuT=80C cpu=55% mem=18%
[component_container_isolated-16] [WARN] [1782640098.287974928] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4392 Hz
[component_container_isolated-16] [INFO] [1782640098.391921259] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640099.213825939] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.70,-0.68) yaw=-81deg cmd=(vx=0.32 wz=-0.08) elapsed=60.6s plan[5pts 0.7m] (2.70,-0.65)→(3.00,-1.15) cpuFreq=1500MHz cpuT=80C cpu=100% mem=18%
[component_container_isolated-16] [INFO] [1782640100.092664686] [controller_server]: Reached the goal!
[component_container_isolated-16] [WARN] [1782640100.286138331] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2608 Hz
[component_container_isolated-16] [INFO] [1782640100.590683691] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-17] [INFO] [1782640100.602783747] [competition_master_stage3]: [结果回调] 巡航完成, 触发VLM推理...
[competition_master_stage3.py-17] [INFO] [1782640100.605484625] [competition_master_stage3]: [VLM] 发布 sign4return=100, 拍照推理中...
[competition_master_stage3.py-17] [INFO] [1782640100.609372005] [competition_master_stage3]: [状态机] CRUISE_CHANNEL → RETURN_P
[vision_ai_node-12] [INFO] [1782640100.610557214] [vision_ai_node]: Received sign4return: 100
[competition_master_stage3.py-17] [INFO] [1782640100.620610060] [competition_master_stage3]: [RETURN] NavigateThroughPoses: 通道入口→P点 (0.38,-1.10)→(-1.99,-0.01)
[component_container_isolated-16] [INFO] [1782640100.624904981] [bt_navigator]: Begin navigating from current location through 2 poses to (-1.99, -0.01)
[vision_ai_node-12] [INFO] [1782640100.625461899] [vision_ai_node]: Received trigger signal (sign4return=100), subscribing to image topic...
[competition_master_stage3.py-17] [INFO] [1782640100.656259393] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[vision_ai_node-12] [INFO] [1782640100.667791574] [vision_ai_node]: Subscribed to /aurora/rgb/image_raw topic
[vision_ai_node-12] [INFO] [1782640100.714666879] [vision_ai_node]: Received compressed image, processing with AI model...
[competition_master_stage3.py-17] [INFO] [1782640101.205536000] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.74,-0.91) yaw=-83deg cmd=(vx=0.00 wz=0.00) elapsed=62.6s plan[3pts 0.4m] (2.70,-0.95)→(3.00,-1.15) cpuFreq=1500MHz cpuT=80C cpu=16% mem=18%
[component_container_isolated-16] [WARN] [1782640101.295941940] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.5041 Hz
[component_container_isolated-16] [INFO] [1782640101.428310180] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-16] [INFO] [1782640101.428593389] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-6] [INFO] [1782640102.310027471] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4693 q_w=0.7524 angle=82.4deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782640102.333189498] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1773 q_w=0.9998 angle=2.4deg beta=0.0330
[competition_master_stage3.py-17] [INFO] [1782640103.204956569] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.98,-1.38) yaw=-47deg cmd=(vx=0.40 wz=-0.07) elapsed=64.6s plan[50pts 7.1m] (2.80,-1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=33% mem=18%
[component_container_isolated-16] [WARN] [1782640103.293007172] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3094 Hz
[component_container_isolated-16] [INFO] [1782640103.428833374] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640105.202122548] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(3.25,-1.67) yaw=-77deg cmd=(vx=-0.29 wz=0.97) elapsed=66.6s plan[47pts 6.5m] (3.00,-1.45)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=81C cpu=33% mem=18%
[component_container_isolated-16] [WARN] [1782640105.284060228] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640105.284360479] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640105.284481270] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640105.425745645] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640105.435414865] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640105.448826422] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640105.449407048] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640105.449825299] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640105.449714299] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640105.462480439] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [WARN] [1782640106.297323672] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.7573 Hz
[component_container_isolated-16] [INFO] [1782640106.428695744] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640107.204784324] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(3.19,-1.50) yaw=-48deg cmd=(vx=-0.17 wz=-1.41) elapsed=68.6s plan[50pts 7.0m] (3.20,-1.55)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=55% mem=18%
[component_container_isolated-16] [WARN] [1782640108.293185980] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3109 Hz
[component_container_isolated-16] [INFO] [1782640108.428716723] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640109.204752886] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(3.18,-1.51) yaw=-65deg cmd=(vx=0.19 wz=-0.97) elapsed=70.6s plan[49pts 6.7m] (3.10,-1.45)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=81% mem=18%
[component_container_isolated-16] [WARN] [1782640110.290816705] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3104 Hz
[component_container_isolated-16] [INFO] [1782640110.428718283] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640111.205153613] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(3.20,-1.76) yaw=-106deg cmd=(vx=0.30 wz=-0.97) elapsed=72.6s plan[46pts 6.3m] (3.20,-1.75)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=81C cpu=50% mem=18%
[component_container_isolated-16] [WARN] [1782640112.295289185] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3025 Hz
[imu_madgwick_filter.py-6] [INFO] [1782640112.310584578] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5197 q_w=0.1940 angle=157.6deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782640112.334907981] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1973 q_w=0.8452 angle=64.6deg beta=0.0330
[component_container_isolated-16] [INFO] [1782640112.428694425] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-4] [WARN] [1782640112.669061374] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1500s > 0.15s, capping
[competition_master_stage3.py-17] [INFO] [1782640113.202880209] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.92,-2.02) yaw=-156deg cmd=(vx=0.40 wz=-0.48) elapsed=74.6s plan[45pts 6.2m] (3.10,-1.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=42% mem=18%
[component_container_isolated-16] [WARN] [1782640114.283792811] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640114.284101811] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640114.284225770] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640114.425804727] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640114.440019369] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640114.455671304] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640114.457011097] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640114.460654393] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640114.461793436] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640114.474358368] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-17] [INFO] [1782640115.203993015] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.35,-1.96) yaw=161deg cmd=(vx=-0.30 wz=0.34) elapsed=76.6s plan[45pts 6.2m] (3.10,-1.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=16% mem=18%
[component_container_isolated-16] [WARN] [1782640115.289636699] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640115.289894241] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640115.289985908] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640115.428736654] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-16] [INFO] [1782640115.429071946] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-16] [INFO] [1782640115.431183490] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640115.443744713] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640115.450250054] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640115.455309476] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640115.455483810] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640115.470136952] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [WARN] [1782640115.473643831] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640115.477414877] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640115.477793336] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640115.482090674] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640115.482246966] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640115.493856147] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640115.726144002] [behavior_server]: Running backup
[competition_master_stage3.py-17] [INFO] [1782640117.208770073] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.52,-2.00) yaw=174deg cmd=(vx=-0.12 wz=0.00) elapsed=78.6s plan[45pts 6.2m] (3.10,-1.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=100% mem=18%
[competition_master_stage3.py-17] [INFO] [1782640119.202393824] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.89,-2.03) yaw=174deg cmd=(vx=-0.12 wz=0.00) elapsed=80.6s plan[45pts 6.2m] (3.10,-1.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=44% mem=18%
[component_container_isolated-16] [WARN] [1782640119.228819355] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640119.229076772] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640119.229179064] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640119.525561994] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640119.551789150] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640119.555392029] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640119.568390294] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640119.568771503] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640119.574052009] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [WARN] [1782640119.582790228] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640119.585602356] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640119.585750023] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640119.587865942] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640119.588114776] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640119.597763037] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640119.833006771] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640119.836734608] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640119.836909275] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640119.837017942] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640120.128798325] [behavior_server]: Running wait
[competition_master_stage3.py-17] [INFO] [1782640121.202833498] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.89,-2.03) yaw=174deg cmd=(vx=0.00 wz=0.00) elapsed=82.6s plan[45pts 6.2m] (3.10,-1.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=50% mem=18%
[imu_madgwick_filter.py-6] [INFO] [1782640122.310457501] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5719 q_w=-0.1966 angle=202.7deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782640122.332684360] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2169 q_w=0.6690 angle=96.0deg beta=0.0330
[component_container_isolated-16] [INFO] [1782640123.129910042] [behavior_server]: wait completed successfully
[competition_master_stage3.py-17] [INFO] [1782640123.202492168] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.89,-2.03) yaw=174deg cmd=(vx=0.00 wz=0.00) elapsed=84.6s plan[45pts 6.2m] (3.10,-1.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=81C cpu=57% mem=18%
[component_container_isolated-16] [WARN] [1782640124.290878564] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.1582 Hz
[component_container_isolated-16] [INFO] [1782640124.430990644] [controller_server]: Received a goal, begin computing control effort.
[competition_master_stage3.py-17] [INFO] [1782640125.203270587] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.89,-2.03) yaw=174deg cmd=(vx=0.40 wz=0.34) elapsed=86.6s plan[44pts 5.9m] (3.00,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=66% mem=18%
[component_container_isolated-16] [WARN] [1782640126.290884190] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3111 Hz
[component_container_isolated-16] [INFO] [1782640126.431399103] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-17] [INFO] [1782640127.201882752] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.51,-2.00) yaw=168deg cmd=(vx=0.40 wz=-0.16) elapsed=88.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=57% mem=18%
[component_container_isolated-16] [WARN] [1782640128.283951430] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640128.284196555] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640128.284292930] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640128.425893970] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640128.434123896] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640128.454069836] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640128.454245295] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640128.457187507] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640128.457555799] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640128.472000149] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-17] [INFO] [1782640129.201550332] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.10,-1.79) yaw=147deg cmd=(vx=-0.30 wz=0.04) elapsed=90.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=81C cpu=50% mem=18%
[component_container_isolated-16] [WARN] [1782640129.290888853] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640129.291146561] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640129.291238145] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640129.431401141] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-16] [INFO] [1782640129.431727558] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-16] [INFO] [1782640129.432810810] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640129.448292411] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640129.453685334] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640129.453862126] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640129.453949293] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640129.472826315] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640129.474205941] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640129.479917489] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640129.480431907] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640129.487007414] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640129.487204790] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640129.499667096] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640129.726182193] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640129.726805027] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640129.726925610] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640129.726990485] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640130.025708625] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640130.035627137] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640130.047956276] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640130.048325443] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640130.048445485] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640130.060178707] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640130.068248091] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640130.075845267] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640130.076149934] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640130.079624688] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640130.079787563] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640130.091752452] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640130.326076266] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640130.327846935] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640130.328006352] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640130.328078185] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640130.626631741] [behavior_server]: Running wait
[competition_master_stage3.py-17] [INFO] [1782640131.204824372] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.24,-1.86) yaw=153deg cmd=(vx=0.00 wz=0.00) elapsed=92.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=81C cpu=50% mem=18%
[vision_ai_node-12] [INFO] [1782640131.974580351] [vision_ai_node]: AI Analysis Result: 这张图片展示了**室内电梯区域的临时布置场景**，疑似处于施工保护或场地筹备状态，细节如下：
[vision_ai_node-12]
[vision_ai_node-12]
[vision_ai_node-12] ### 场景与布局
[vision_ai_node-12] 画面聚焦建筑内部的电梯厅区域，地面铺有**浅色（浅黄/白色）反光塑料布**（施工用地面保护膜，表面带褶皱、反光明显），整体氛围偏向“临时布置”（如施工、活动筹备）。
[vision_ai_node-12]
[vision_ai_node-12]
[vision_ai_node-12] ### 核心物体与细节
[vision_ai_node-12] 1. **电梯与按钮**：
[vision_ai_node-12]    - 左侧是**银色电梯门**，两侧门框为**黑色大理石质感**（纹理清晰）。
[vision_ai_node-12]    - 电梯旁的墙面上，装有**银色电梯按钮面板**，嵌有黑色按钮（可见“上行/下行”标识），用于操控电梯。
[vision_ai_node-12]
[vision_ai_node-12] 2. **墙面海报**：
[vision_ai_node-12]    电梯上方的墙面上，张贴着一张**蓝白主色调的海报**，展示一栋现代建筑及周边环境（疑似宣传该建筑或场所）。
[vision_ai_node-12]
[vision_ai_node-12] 3. **黄色物体**：
[vision_ai_node-12]    前景中有至少3个**明亮的黄色物体**（塑料或木质质感）：
[vision_ai_node-12]    - 左侧：一个亮黄色长方体（受光面更亮，视觉上更醒目）。
[vision_ai_node-12]    - 中间：一个黄色正方体（或长方体），体积稍小。
[vision_ai_node-12]    - 后方（电梯墙前）：一个黄色物体（高度与中间物体相近，呈立放状态）。
[vision_ai_node-12]
[vision_ai_node-12] 4. **蓝色布帘**：
[vision_ai_node-12]    右侧是一块**深蓝色的大型布帘**，布料质感明显，覆盖在某个物体表面（遮挡作用），占据画面右侧大部分空间。
[vision_ai_node-12]
[vision_ai_node-12]
[vision_ai_node-12] ### 色彩与氛围
[vision_ai_node-12] 色彩对比强烈：**银色电梯门**、**黑色门框/按钮**、**蓝白海报**、**明黄色物体**、**深蓝色布帘**、**浅色反光塑料布**，共同营造出“临时布置”的视觉效果（如施工保护、活动道具筹备）。
[vision_ai_node-12]
[vision_ai_node-12]
[vision_ai_node-12] ### 整体感受
[vision_ai_node-12] 场景似在进行**施工保护**（地面铺保护膜）或**活动场地布置**（黄/蓝物体、布帘为临时道具/遮挡），色彩鲜明的物体与反光地面，传递出“临时、筹备中”的氛围。
[vision_ai_node-12]
[vision_ai_node-12]
[vision_ai_node-12] （注：黄色物体、蓝色布帘的具体用途暂不明确，推测为“临时遮挡/道具”；地面塑料布为施工常用的“地面保护膜”，防止作业弄脏地面。）
[competition_master_stage3.py-17] [INFO] [1782640131.990409495] [competition_master_stage3]: [VLM] 后台收到推理结果: 这张图片展示了**室内电梯区域的临时布置场景**，疑似处于施工保护或场地筹备状态，细节如下：
[competition_master_stage3.py-17]
[competition_master_stage3.py-17]
[competition_master_stage3.py-17] ### 场景与布局
[competition_master_stage3.py-17] 画面聚焦建筑内部的电梯厅区域，地面铺有**浅色（浅黄/白色）反光塑料布**（施工用地面保护膜，表面带褶皱、反光明显...
[vision_ai_node-12] [INFO] [1782640131.989420827] [vision_ai_node]: Unsubscribed from image topic
[imu_madgwick_filter.py-6] [INFO] [1782640132.313067286] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=6239 q_w=-0.3948 angle=226.5deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782640132.333081893] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2367 q_w=0.5674 angle=110.9deg beta=0.0330
[competition_master_stage3.py-17] [INFO] [1782640133.203271696] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.24,-1.86) yaw=153deg cmd=(vx=0.00 wz=0.00) elapsed=94.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=25% mem=18%
[component_container_isolated-16] [INFO] [1782640133.627176647] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640134.284053244] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640134.284309578] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640134.284464328] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640134.425582158] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640134.432179624] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640134.437773631] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640134.438181756] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640134.447779976] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640134.447940518] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640134.453350066] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-17] [INFO] [1782640135.201887893] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.24,-1.86) yaw=153deg cmd=(vx=0.00 wz=0.00) elapsed=96.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=50% mem=18%
[component_container_isolated-16] [WARN] [1782640135.289211536] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640135.289465287] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640135.289556454] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640135.425653487] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640135.431513952] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640135.437113583] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640135.437885126] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640135.438063751] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640135.448703763] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640135.453374227] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640135.462553904] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640135.462839238] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640135.465002657] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640135.465162824] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640135.477266171] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640135.726081294] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640135.728115921] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640135.728264755] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640135.728424463] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640136.025634725] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640136.033614567] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640136.039817741] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640136.042740328] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640136.042925120] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640136.053207882] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640136.058259679] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640136.067951816] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640136.068304191] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640136.071019527] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640136.071203069] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640136.083335958] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640136.326490407] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640136.328276993] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640136.328439951] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640136.328679535] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640136.626729631] [behavior_server]: Running wait
[competition_master_stage3.py-17] [INFO] [1782640137.210347808] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.24,-1.86) yaw=153deg cmd=(vx=0.00 wz=0.00) elapsed=98.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=50% mem=18%
[competition_master_stage3.py-17] [INFO] [1782640139.200446407] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.24,-1.86) yaw=153deg cmd=(vx=0.00 wz=0.00) elapsed=100.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=12% mem=18%
[component_container_isolated-16] [INFO] [1782640139.627279235] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640140.283745662] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640140.284077079] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640140.284300580] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640140.431769875] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640140.441777929] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640140.448132228] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640140.448269353] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640140.454609402] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640140.463633246] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640140.463943704] [behavior_server]: wait completed successfully
[competition_master_stage3.py-17] [INFO] [1782640141.202068393] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.24,-1.86) yaw=153deg cmd=(vx=0.00 wz=0.00) elapsed=102.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=16% mem=18%
[component_container_isolated-16] [WARN] [1782640141.289809536] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640141.290051494] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640141.290149619] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640141.425613276] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640141.431557908] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640141.439955793] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640141.441497003] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640141.443319422] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640141.446937551] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640141.462811403] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640141.462949445] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640141.467347200] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [WARN] [1782640141.467611658] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640141.469213535] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640141.469516785] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640141.726936875] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640141.731163255] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640141.731318297] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640141.731392922] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640142.025589429] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640142.035601607] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640142.040249696] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640142.047262996] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640142.047436080] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640142.064776183] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640142.071958608] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640142.077939823] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640142.078190990] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640142.083247579] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640142.083397913] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640142.095629635] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-6] [INFO] [1782640142.310511759] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=6780 q_w=-0.3934 angle=226.3deg beta=0.0030
[component_container_isolated-16] [INFO] [1782640142.326696278] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640142.328487780] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640142.328657988] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640142.328736780] [behavior_server]: [backup] [ActionServer] Aborting handle.
[imu_madgwick_filter.py-4] [INFO] [1782640142.333011827] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2567 q_w=0.6352 angle=101.1deg beta=0.0330
[component_container_isolated-16] [INFO] [1782640142.626655750] [behavior_server]: Running wait
[competition_master_stage3.py-17] [INFO] [1782640143.204377585] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.27,-1.89) yaw=154deg cmd=(vx=0.00 wz=0.00) elapsed=104.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=33% mem=18%
[competition_master_stage3.py-17] [INFO] [1782640145.201645102] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.27,-1.89) yaw=154deg cmd=(vx=0.00 wz=0.00) elapsed=106.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=0% mem=18%
[component_container_isolated-16] [INFO] [1782640145.627041844] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640146.283731561] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640146.284151520] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640146.284251270] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640146.425671808] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640146.439638366] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640146.445782748] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640146.446072415] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640146.450920254] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640146.451128962] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640146.461671808] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-17] [INFO] [1782640147.203600415] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.27,-1.89) yaw=154deg cmd=(vx=0.00 wz=0.00) elapsed=108.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=44% mem=18%
[component_container_isolated-16] [WARN] [1782640147.289224555] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640147.289486055] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640147.289707972] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640147.425604254] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640147.433664638] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640147.437358726] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640147.441702523] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640147.441916523] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640147.450181699] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640147.450933867] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640147.456264248] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640147.456531082] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640147.462082713] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640147.462234005] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640147.482695820] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640147.726286601] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640147.727095352] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640147.727264227] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640147.727333686] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640148.025555447] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640148.031938954] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640148.038738795] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640148.043629676] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640148.043791801] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640148.051787185] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640148.055038439] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640148.064549992] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640148.064810909] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640148.066178535] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640148.066309369] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640148.078064466] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640148.326111377] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640148.327034045] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640148.327158336] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640148.327222961] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640148.632507105] [behavior_server]: Running wait
[competition_master_stage3.py-17] [INFO] [1782640149.203253514] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.27,-1.89) yaw=154deg cmd=(vx=0.00 wz=0.00) elapsed=110.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=33% mem=18%
[competition_master_stage3.py-17] [INFO] [1782640151.205341155] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.27,-1.89) yaw=154deg cmd=(vx=0.00 wz=0.00) elapsed=112.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=33% mem=18%
[component_container_isolated-16] [INFO] [1782640151.632919231] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640152.283667189] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640152.283930856] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640152.284051273] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[imu_madgwick_filter.py-6] [INFO] [1782640152.309768677] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=7323 q_w=-0.3923 angle=226.2deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782640152.333241829] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2767 q_w=0.6989 angle=91.3deg beta=0.0330
[component_container_isolated-16] [INFO] [1782640152.425744852] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640152.432870277] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640152.438564284] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640152.438589076] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640152.438882034] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640152.438857576] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640152.445603334] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-17] [INFO] [1782640153.203942457] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.27,-1.89) yaw=154deg cmd=(vx=0.00 wz=0.00) elapsed=114.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=20% mem=18%
[component_container_isolated-16] [WARN] [1782640153.291626849] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640153.291877183] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640153.291969850] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640153.425719129] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640153.434372139] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640153.441701314] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640153.441872189] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640153.441966231] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640153.451357658] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640153.458724667] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640153.466578801] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640153.466841218] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640153.470023888] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640153.470156096] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640153.481949277] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640153.726206766] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640153.727599309] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640153.727721310] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640153.727786060] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640154.025675986] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640154.032443869] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640154.039327502] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640154.043892465] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640154.044058132] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640154.052146225] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [WARN] [1782640154.058532732] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640154.063269821] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640154.063406321] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640154.063742905] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640154.064017738] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640154.075396293] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640154.326992499] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640154.329291043] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640154.329470169] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640154.329553335] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640154.626523177] [behavior_server]: Running wait
[competition_master_stage3.py-17] [INFO] [1782640155.200570462] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.31,-1.90) yaw=154deg cmd=(vx=0.00 wz=0.00) elapsed=116.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=44% mem=18%
[competition_master_stage3.py-17] [INFO] [1782640157.204671891] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.31,-1.90) yaw=154deg cmd=(vx=0.00 wz=0.00) elapsed=118.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=71% mem=18%
[component_container_isolated-16] [INFO] [1782640157.631697840] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640158.285030007] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640158.285259090] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640158.285364424] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640158.425639710] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640158.434204845] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640158.446730026] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640158.446895818] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640158.453139825] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640158.453499117] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640158.558041195] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-17] [INFO] [1782640159.223930543] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.31,-1.90) yaw=154deg cmd=(vx=0.00 wz=0.00) elapsed=120.7s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=60% mem=18%
[component_container_isolated-16] [WARN] [1782640159.289580327] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640159.289818994] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640159.289943160] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640159.425630566] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640159.434025201] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640159.439413499] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640159.441988793] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640159.442164002] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640159.451917346] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640159.456350810] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640159.463948318] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640159.464931528] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640159.467710281] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640159.467868406] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640159.480825713] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640159.727052412] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640159.727907455] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640159.728275705] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640159.728371539] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640160.025587338] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640160.035443641] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640160.044219734] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640160.044407735] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640160.044447110] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [WARN] [1782640160.058447709] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640160.064603758] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640160.072420683] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640160.073607851] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640160.075756562] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640160.075969729] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640160.087905784] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640160.326315558] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640160.327789643] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640160.327944018] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640160.328042102] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640160.626212652] [behavior_server]: Running wait
[competition_master_stage3.py-17] [INFO] [1782640161.205125274] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.31,-1.90) yaw=154deg cmd=(vx=0.00 wz=0.00) elapsed=122.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=0% mem=18%
[imu_madgwick_filter.py-6] [INFO] [1782640162.310444875] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=7883 q_w=-0.3912 angle=226.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782640162.333042775] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2967 q_w=0.7580 angle=81.4deg beta=0.0330
[competition_master_stage3.py-17] [INFO] [1782640163.203062939] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.31,-1.90) yaw=154deg cmd=(vx=0.00 wz=0.00) elapsed=124.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=37% mem=18%
[component_container_isolated-16] [INFO] [1782640163.628588510] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640164.177578680] [local_costmap.local_costmap]: Message Filter dropping message: frame 'laser_link' at time 1782640163.875 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-16] [WARN] [1782640164.283710927] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640164.283925927] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640164.284025802] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640164.425673923] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640164.430266136] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640164.435598392] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640164.435666351] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640164.435894893] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640164.437029811] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640164.444525486] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-17] [INFO] [1782640165.204614606] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.31,-1.90) yaw=154deg cmd=(vx=0.00 wz=0.00) elapsed=126.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=33% mem=18%
[component_container_isolated-16] [WARN] [1782640165.289584578] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640165.289861745] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640165.289988745] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640165.425710317] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640165.436144537] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640165.451605472] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640165.451932681] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640165.452049389] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640165.459096897] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [WARN] [1782640165.469692743] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640165.474068081] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640165.474222373] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640165.474795457] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640165.475044582] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640165.486658095] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640165.737228632] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640165.738191591] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640165.738334425] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640165.738422675] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640166.025574545] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640166.032842262] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640166.038233060] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640166.039335978] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640166.039625603] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640166.049424406] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640166.050321324] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640166.057341457] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640166.057598374] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640166.062363879] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640166.062606546] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640166.075846478] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640166.331232603] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640166.332570313] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640166.332704438] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640166.332771313] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640166.626370816] [behavior_server]: Running wait
[competition_master_stage3.py-17] [INFO] [1782640167.201893141] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.26,-1.88) yaw=153deg cmd=(vx=0.00 wz=0.00) elapsed=128.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=28% mem=18%
[competition_master_stage3.py-17] [INFO] [1782640169.202178802] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.26,-1.88) yaw=153deg cmd=(vx=0.00 wz=0.00) elapsed=130.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=55% mem=18%
[component_container_isolated-16] [INFO] [1782640169.626750411] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640170.283409495] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640170.283665953] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640170.283774037] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640170.426075199] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640170.433922541] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640170.440016757] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640170.440182674] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640170.446801348] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640170.447341432] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640170.450393144] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-17] [INFO] [1782640171.203222794] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.26,-1.88) yaw=153deg cmd=(vx=0.00 wz=0.00) elapsed=132.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=50% mem=18%
[component_container_isolated-16] [WARN] [1782640171.290409561] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640171.290669769] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640171.290784186] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640171.425896340] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640171.438440146] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640171.448850533] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640171.451671911] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640171.451839120] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640171.458691503] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [WARN] [1782640171.471237600] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640171.474717271] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640171.474860021] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640171.475045938] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640171.475252938] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640171.487315910] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640171.639678751] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640171.640767835] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640171.640910752] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640171.641016336] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640171.925584202] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640171.932861960] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640171.941078095] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640171.941159970] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640171.941354428] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640171.950605397] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640171.956700988] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640171.965323247] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640171.965765706] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640171.968105209] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640171.968262876] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640171.980445140] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640172.226534295] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640172.230510133] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640172.233786262] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640172.233902679] [behavior_server]: [backup] [ActionServer] Aborting handle.
[imu_madgwick_filter.py-6] [INFO] [1782640172.310230932] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=8440 q_w=-0.3897 angle=225.9deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782640172.333587834] [imu_madgwick_filter]: [imu_madgwick ->] msgs=3167 q_w=0.8113 angle=71.6deg beta=0.0330
[component_container_isolated-16] [INFO] [1782640172.526984055] [behavior_server]: Running wait
[competition_master_stage3.py-17] [INFO] [1782640173.203939368] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.26,-1.88) yaw=153deg cmd=(vx=0.00 wz=0.00) elapsed=134.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=40% mem=18%
[competition_master_stage3.py-17] [INFO] [1782640175.204259564] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.26,-1.88) yaw=153deg cmd=(vx=0.00 wz=0.00) elapsed=136.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=64% mem=18%
[component_container_isolated-16] [INFO] [1782640175.527377599] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640176.284165919] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640176.284486586] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640176.284630794] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640176.425619580] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640176.431652545] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640176.438090136] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640176.438336969] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640176.438434761] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640176.438391094] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640176.447032563] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-17] [INFO] [1782640177.204411091] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.26,-1.88) yaw=153deg cmd=(vx=0.00 wz=0.00) elapsed=138.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=75% mem=18%
[component_container_isolated-16] [WARN] [1782640177.290525731] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640177.290751606] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640177.290839898] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640177.425689343] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640177.434514770] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640177.437655315] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640177.447993452] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640177.448063577] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640177.448377994] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1782640177.459636715] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640177.459959132] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640177.463034511] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640177.463186052] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640177.464028803] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [WARN] [1782640177.475632525] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640177.726315977] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640177.727390728] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640177.727543353] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640177.727929229] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640178.025619109] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640178.034837536] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640178.043493254] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640178.043513379] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640178.044607755] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640178.057912812] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640178.060212940] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640178.070133993] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640178.070444410] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640178.071459619] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640178.071674828] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640178.083806842] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640178.326582409] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640178.328170995] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640178.328337828] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640178.328817829] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640178.627218668] [behavior_server]: Running wait
[competition_master_stage3.py-17] [INFO] [1782640179.207968953] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.27,-1.89) yaw=154deg cmd=(vx=0.00 wz=0.00) elapsed=140.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=55% mem=18%
[competition_master_stage3.py-17] [INFO] [1782640181.204734264] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.27,-1.89) yaw=154deg cmd=(vx=0.00 wz=0.00) elapsed=142.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=61% mem=18%
[component_container_isolated-16] [INFO] [1782640181.627641869] [behavior_server]: wait completed successfully
[component_container_isolated-16] [WARN] [1782640182.299715590] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640182.300003049] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640182.300123716] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[imu_madgwick_filter.py-6] [INFO] [1782640182.317762028] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=8985 q_w=-0.3881 angle=225.7deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782640182.333216045] [imu_madgwick_filter]: [imu_madgwick ->] msgs=3367 q_w=0.8587 angle=61.7deg beta=0.0330
[component_container_isolated-16] [INFO] [1782640182.425633858] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640182.431618490] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640182.436342787] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640182.436622787] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640182.439109624] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640182.439294124] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640182.449967136] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-17] [INFO] [1782640183.204364617] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.27,-1.89) yaw=154deg cmd=(vx=0.00 wz=0.00) elapsed=144.6s plan[40pts 5.5m] (2.60,-2.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=80C cpu=63% mem=18%
[component_container_isolated-16] [WARN] [1782640183.288811588] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-16] [WARN] [1782640183.289026255] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.07, -0.73)
[component_container_isolated-16] [WARN] [1782640183.289136547] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640183.425769910] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640183.434176461] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640183.442373262] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640183.442740679] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640183.442919846] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640183.453962317] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640183.459363990] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640183.470148169] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640183.470436127] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640183.471845046] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640183.471981504] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640183.483674476] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640183.726477459] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640183.727775253] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640183.728047044] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640183.728141545] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640184.025570549] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-16] [INFO] [1782640184.037253479] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640184.043233944] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-16] [INFO] [1782640184.043362944] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640184.043492819] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640184.052186871] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640184.060208671] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1782640184.068723264] [behavior_server]: Running wait
[component_container_isolated-16] [INFO] [1782640184.070850975] [behavior_server]: wait completed successfully
[component_container_isolated-16] [INFO] [1782640184.071773059] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1782640184.071911893] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [WARN] [1782640184.083965782] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-16] [INFO] [1782640184.326069764] [behavior_server]: Running backup
[component_container_isolated-16] [WARN] [1782640184.328109933] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-16] [WARN] [1782640184.328262559] [behavior_server]: backup failed
[component_container_isolated-16] [WARN] [1782640184.328338767] [behavior_server]: [backup] [ActionServer] Aborting handle.
^C[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[rviz2-18] [INFO] [1782640184.467369550] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [origincar_base_node-1]: process has died [pid 38859, exit code -6, cmd '/userdata/dev_ws/install/origincar_base/lib/origincar_base/origincar_base_node --ros-args --params-file /tmp/launch_params_97fj30g8 --params-file /tmp/launch_params_pm9uwncr'].
[ERROR] [lslidar_driver_node-2]: process has died [pid 38861, exit code -6, cmd '/userdata/dev_ws/install/lslidar_driver/lib/lslidar_driver/lslidar_driver_node --ros-args -r __node:=lslidar_driver_node --params-file /userdata/dev_ws/install/lslidar_driver/share/lslidar_driver/params/lsx10.yaml'].
[INFO] [robot_state_publisher-3]: process has finished cleanly [pid 38863]
[INFO] [static_transform_publisher-8]: process has finished cleanly [pid 38911]
[INFO] [ekf_node-7]: process has finished cleanly [pid 38871]
[component_container_isolated-16] [INFO] [1782640184.467376133] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-16] [INFO] [1782640184.467538383] [velocity_smoother]: Running Nav2 LifecycleNode rcl preshutdown (velocity_smoother)
[INFO] [map_server-13]: process has finished cleanly [pid 38997]
[INFO] [lifecycle_manager-15]: process has finished cleanly [pid 39001]
[INFO] [costmap_filter_info_server-14]: process has finished cleanly [pid 38999]
[static_transform_publisher-8] [INFO] [1782640184.467494008] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1782640184.467521675] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1782640184.467813425] [origincar_base]: Stop command sent to STM32 on shutdown.
[origincar_base_node-1] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[aurora930_node-9] [INFO] [1782640184.467538342] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[aurora930_node-9] I0628 17:49:44.474965 38913 ros2_node.cc:90] process quit succeed
[aurora930_node-9] I0628 17:49:44.475121 38913 aurora900_ros2_device.cc:83] begin stop()
[component_container_isolated-16] [INFO] [1782640184.468217467] [velocity_smoother]: Deactivating
[component_container_isolated-16] [INFO] [1782640184.468374467] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640184.499678170] [velocity_smoother]: Cleaning up
[component_container_isolated-16] [INFO] [1782640184.500014712] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640184.500118837] [bt_navigator]: Running Nav2 LifecycleNode rcl preshutdown (bt_navigator)
[component_container_isolated-16] [INFO] [1782640184.500272170] [bt_navigator]: Deactivating
[component_container_isolated-16] [WARN] [1782640184.500376045] [bt_navigator]: [navigate_through_poses] [ActionServer] Requested to deactivate server but goal is still executing. Should check if action server is running before deactivating.
[component_container_isolated-16] [WARN] [1782640184.525677616] [bt_navigator]: [navigate_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-16] [INFO] [1782640184.526310158] [bt_navigator]: Goal canceled
[component_container_isolated-16] [WARN] [1782640184.526432075] [bt_navigator]: [navigate_through_poses] [ActionServer] Stopping the thread per request.
[component_container_isolated-16] [INFO] [1782640184.526993159] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640184.580543095] [bt_navigator]: Cleaning up
[component_container_isolated-16] [INFO] [1782640184.643977958] [lifecycle_manager_navigation]: Have not received a heartbeat from bt_navigator.
[component_container_isolated-16] [ERROR] [1782640184.644165667] [lifecycle_manager_navigation]: CRITICAL FAILURE: SERVER bt_navigator IS DOWN after not receiving a heartbeat for 4000 ms. Shutting down related nodes.
[component_container_isolated-16] [INFO] [1782640184.644523459] [lifecycle_manager_navigation]: Terminating bond timer...
[component_container_isolated-16] [INFO] [1782640184.644618126] [lifecycle_manager_navigation]: Resetting managed nodes...
[component_container_isolated-16] [INFO] [1782640184.644681626] [lifecycle_manager_navigation]: Deactivating velocity_smoother
[component_container_isolated-16] [INFO] [1782640184.706790238] [local_costmap.local_costmap]: Message Filter dropping message: frame 'laser_link' at time 1782640184.405 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-16] [WARN] [1782640184.707644780] [rcl_lifecycle]: No transition matching 4 found for current state unconfigured
[component_container_isolated-16] [WARN] [1782640184.707718406] [rcl_lifecycle]: No transition matching 4 found for current state unconfigured
[component_container_isolated-16] [ERROR] [1782640184.707760239] [velocity_smoother]: Unable to start transition 4 from current state unconfigured: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-16] [ERROR] [1782640184.711383201] [lifecycle_manager_navigation]: Failed to change state for node: velocity_smoother
[component_container_isolated-16] [INFO] [1782640184.711606410] [lifecycle_manager_navigation]: Deactivating waypoint_follower
[component_container_isolated-16] [INFO] [1782640184.712774828] [waypoint_follower]: Deactivating
[component_container_isolated-16] [INFO] [1782640184.713089287] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640184.842551058] [lifecycle_manager_navigation]: Deactivating bt_navigator
[component_container_isolated-16] [WARN] [1782640184.843992310] [rcl_lifecycle]: No transition matching 4 found for current state cleaningup
[component_container_isolated-16] [WARN] [1782640184.844122602] [rcl_lifecycle]: No transition matching 4 found for current state cleaningup
[component_container_isolated-16] [ERROR] [1782640184.844164435] [bt_navigator]: Unable to start transition 4 from current state cleaningup: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-16] [ERROR] [1782640184.845925729] [lifecycle_manager_navigation]: Failed to change state for node: bt_navigator
[component_container_isolated-16] [INFO] [1782640184.846144396] [lifecycle_manager_navigation]: Deactivating behavior_server
[component_container_isolated-16] [INFO] [1782640184.847527814] [behavior_server]: Deactivating
[component_container_isolated-16] [INFO] [1782640184.847815189] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640184.971452871] [lifecycle_manager_navigation]: Deactivating planner_server
[component_container_isolated-16] [INFO] [1782640184.973061998] [planner_server]: Deactivating
[component_container_isolated-16] [INFO] [1782640184.973427123] [global_costmap.global_costmap]: Deactivating
[component_container_isolated-16] [INFO] [1782640185.235701129] [bt_navigator]: Completed Cleaning up
[component_container_isolated-16] [INFO] [1782640185.235928713] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640185.235988754] [lifecycle_manager_localization]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_localization)
[component_container_isolated-16] [INFO] [1782640185.236054921] [lifecycle_manager_localization]: Terminating bond timer...
[component_container_isolated-16] [INFO] [1782640185.274276756] [waypoint_follower]: Running Nav2 LifecycleNode rcl preshutdown (waypoint_follower)
[component_container_isolated-16] [INFO] [1782640185.274521173] [waypoint_follower]: Cleaning up
[component_container_isolated-16] [INFO] [1782640185.277021509] [planner_server]: Deactivating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-16] [INFO] [1782640185.277318093] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640185.293443736] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640185.293648611] [planner_server]: Running Nav2 LifecycleNode rcl preshutdown (planner_server)
[component_container_isolated-16] [INFO] [1782640185.293734237] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640185.293794028] [lifecycle_manager_navigation]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_navigation)
[component_container_isolated-16] [INFO] [1782640185.395938227] [lifecycle_manager_navigation]: Deactivating smoother_server
[component_container_isolated-16] [INFO] [1782640185.396956895] [smoother_server]: Deactivating
[component_container_isolated-16] [INFO] [1782640185.397094270] [smoother_server]: Deactivating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-16] [INFO] [1782640185.397269896] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640185.513246569] [lifecycle_manager_navigation]: Deactivating controller_server
[component_container_isolated-16] [INFO] [1782640185.514090028] [controller_server]: Deactivating
[component_container_isolated-16] [INFO] [1782640185.514197695] [controller_server]: Deactivating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-16] [INFO] [1782640185.514389570] [local_costmap.local_costmap]: Deactivating
[component_container_isolated-16] [INFO] [1782640185.522312287] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640185.637732501] [lifecycle_manager_navigation]: Cleaning up velocity_smoother
[component_container_isolated-16] [WARN] [1782640185.638663336] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-16] [WARN] [1782640185.638736378] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-16] [ERROR] [1782640185.638764961] [velocity_smoother]: Unable to start transition 2 from current state unconfigured: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-16] [INFO] [1782640185.639781129] [lifecycle_manager_navigation]: Cleaning up waypoint_follower
[component_container_isolated-16] [WARN] [1782640185.651875809] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-16] [WARN] [1782640185.651967643] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-16] [ERROR] [1782640185.651999226] [waypoint_follower]: Unable to start transition 2 from current state unconfigured: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-16] [INFO] [1782640185.653341977] [lifecycle_manager_navigation]: Cleaning up bt_navigator
[component_container_isolated-16] [WARN] [1782640185.697486777] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-16] [WARN] [1782640185.699463363] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-16] [ERROR] [1782640185.699518405] [bt_navigator]: Unable to start transition 2 from current state unconfigured: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-16] [INFO] [1782640185.701160157] [lifecycle_manager_navigation]: Cleaning up behavior_server
[component_container_isolated-16] [INFO] [1782640185.702221074] [behavior_server]: Cleaning up
[costmap_filter_info_server-14] [INFO] [1782640184.467941634] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-14] [INFO] [1782640184.468180051] [keepout_filter_info_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_filter_info_server)
[costmap_filter_info_server-14] [INFO] [1782640184.468424343] [keepout_filter_info_server]: Deactivating
[costmap_filter_info_server-14] [INFO] [1782640184.468528176] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-14] [INFO] [1782640184.489338866] [keepout_filter_info_server]: Cleaning up
[costmap_filter_info_server-14] [INFO] [1782640184.489715533] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-14] [INFO] [1782640184.688613801] [keepout_filter_info_server]: Destroying
[lifecycle_manager-15] [INFO] [1782640184.468236801] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-15] [INFO] [1782640184.468430843] [lifecycle_manager_keepout]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_keepout)
[lifecycle_manager-15] [INFO] [1782640184.468553426] [lifecycle_manager_keepout]: Terminating bond timer...
[lifecycle_manager-15] [INFO] [1782640184.691287512] [lifecycle_manager_keepout]: Destroying lifecycle_manager_keepout
[map_server-13] [INFO] [1782640184.468727426] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-13] [INFO] [1782640184.468922760] [keepout_mask_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_mask_server)
[map_server-13] [INFO] [1782640184.469174885] [keepout_mask_server]: Deactivating
[map_server-13] [INFO] [1782640184.469262718] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[map_server-13] [INFO] [1782640184.480023772] [keepout_mask_server]: Cleaning up
[map_server-13] [INFO] [1782640184.480252648] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[map_server-13] [INFO] [1782640184.669917404] [keepout_mask_server]: Destroying
[ekf_node-7] [INFO] [1782640184.468934593] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[robot_state_publisher-3] [INFO] [1782640184.469075677] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[competition_master_stage3.py-17] [INFO] [1782640184.578580259] [competition_master_stage3]: [MAIN] 收到 Ctrl+C, 停止录制 + 保存轨迹...
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[origincar_base_node-1] terminate called after throwing an instance of 'rclcpp::exceptions::RCLError'
[origincar_base_node-1]   what():  failed to create guard condition: the given context is not valid, either rcl_init() was not called or rcl_shutdown() was called., at ./src/rcl/guard_condition.c:67
[aurora930_node-9] I0628 17:49:44.582767 38913 aurora900_ros2_device.cc:103] stop stream
[aurora930_node-9] 2026-06-28 17:49:44.744 ( 173.582s) [        8EE34020]      aurora900_impl.cc:648   INFO| ir_stream_count_=0, rgb_stream_count_=0, depth_stream_count_=0
[aurora930_node-9] 2026-06-28 17:49:44.745 ( 173.582s) [        8EE34020]      aurora900_impl.cc:649   INFO| mask=7
[aurora930_node-9] I0628 17:49:44.982301 38913 aurora900_ros2_device.cc:105] destroy stream
[aurora930_node-9] I0628 17:49:44.982542 38913 aurora900_ros2_device.cc:110] close glog
[aurora930_node-9] WARNING: Logging before InitGoogleLogging() is written to STDERR
[aurora930_node-9] I0628 17:49:44.982698 38913 ros2_device.cc:113] close device...
[aurora930_node-9] 2026-06-28 17:49:45.482 ( 174.319s) [        53FF57E0]         cmd_backend.cc:40    INFO| RunBlocking is end!!!
[aurora930_node-9] 2026-06-28 17:49:45.683 ( 174.520s) [        8EE34020]deptrum_camera_vendor.c:121   INFO| device is close.
[aurora930_node-9] I0628 17:49:45.685218 38913 ros2_device.cc:116] quit succeed
[bmi088_iio_bridge.py-5] Traceback (most recent call last):
[bmi088_iio_bridge.py-5]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/bmi088_iio_bridge.py", line 493, in <module>
[bmi088_iio_bridge.py-5]     main()
[bmi088_iio_bridge.py-5]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/bmi088_iio_bridge.py", line 489, in main
[bmi088_iio_bridge.py-5]     rclpy.shutdown()
[bmi088_iio_bridge.py-5]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 130, in shutdown
[bmi088_iio_bridge.py-5]     _shutdown(context=context)
[bmi088_iio_bridge.py-5]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/utilities.py", line 58, in shutdown
[bmi088_iio_bridge.py-5]     return context.shutdown()
[bmi088_iio_bridge.py-5]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/context.py", line 102, in shutdown
[bmi088_iio_bridge.py-5]     self.__context.shutdown()
[bmi088_iio_bridge.py-5] rclpy._rclpy_pybind11.RCLError: failed to shutdown: rcl_shutdown already called on the given context, at ./src/rcl/init.c:241
[vision_ai_node-12] Traceback (most recent call last):
[vision_ai_node-12]   File "/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node", line 33, in <module>
[vision_ai_node-12]     sys.exit(load_entry_point('racing-vision-ai==0.0.1', 'console_scripts', 'vision_ai_node')())
[vision_ai_node-12]   File "/userdata/dev_ws/install/racing_vision_ai/lib/python3.10/site-packages/racing_vision_ai/vision_ai_node.py", line 283, in main
[vision_ai_node-12]     rclpy.shutdown()
[vision_ai_node-12]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 130, in shutdown
[vision_ai_node-12]     _shutdown(context=context)
[vision_ai_node-12]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/utilities.py", line 58, in shutdown
[vision_ai_node-12]     return context.shutdown()
[vision_ai_node-12]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/context.py", line 102, in shutdown
[vision_ai_node-12]     self.__context.shutdown()
[vision_ai_node-12] rclpy._rclpy_pybind11.RCLError: failed to shutdown: rcl_shutdown already called on the given context, at ./src/rcl/init.c:241
[component_container_isolated-16] [INFO] [1782640185.845525070] [lifecycle_manager_navigation]: Cleaning up planner_server
[component_container_isolated-16] [INFO] [1782640185.846380238] [planner_server]: Cleaning up
[component_container_isolated-16] [INFO] [1782640185.881432278] [global_costmap.global_costmap]: Cleaning up
[component_container_isolated-16] [INFO] [1782640185.894802084] [planner_server]: Cleaning up plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-16] [INFO] [1782640185.909738810] [planner_server]: Destroying plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-16] [INFO] [1782640185.946272393] [lifecycle_manager_navigation]: Cleaning up smoother_server
[component_container_isolated-16] [INFO] [1782640185.946888268] [smoother_server]: Cleaning up
[component_container_isolated-16] [INFO] [1782640185.947014894] [smoother_server]: Cleaning up smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-16] [INFO] [1782640185.987678190] [lifecycle_manager_navigation]: Cleaning up controller_server
[component_container_isolated-16] [INFO] [1782640185.988524441] [controller_server]: Cleaning up
[component_container_isolated-16] [INFO] [1782640185.988643316] [controller_server]: Cleaning up controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-16] [INFO] [1782640185.993844155] [local_costmap.local_costmap]: Cleaning up
[component_container_isolated-16] [INFO] [1782640186.054064557] [lifecycle_manager_navigation]: Managed nodes have been reset
[INFO] [imu_madgwick_filter.py-6]: process has finished cleanly [pid 38869]
[component_container_isolated-16] [INFO] [1782640186.126152638] [behavior_server]: Running Nav2 LifecycleNode rcl preshutdown (behavior_server)
[component_container_isolated-16] [INFO] [1782640186.126360555] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640186.126430722] [amcl]: Running Nav2 LifecycleNode rcl preshutdown (amcl)
[component_container_isolated-16] [INFO] [1782640186.126552889] [amcl]: Deactivating
[component_container_isolated-16] [INFO] [1782640186.126702472] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640186.140164196] [amcl]: Cleaning up
[competition_master_stage3.py-17] [INFO] [1782640186.154098545] [competition_master_stage3]: [BAG] 录制已停止
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.157863383] [competition_master_stage3]:
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.161082303] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.165380224] [competition_master_stage3]: >>> [Stage 3] 任务结束 <<<
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.169358687] [competition_master_stage3]:   最终状态: RETURN_P
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.173013733] [competition_master_stage3]:   总耗时:   147.6s
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[INFO] [imu_madgwick_filter.py-4]: process has finished cleanly [pid 38865]
[competition_master_stage3.py-17] [INFO] [1782640186.177081363] [competition_master_stage3]:   --- 各阶段耗时 ---
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.181221201] [competition_master_stage3]:   LAUNCH................ 17.3s
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[component_container_isolated-16] [INFO] [1782640186.177932197] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640186.178098239] [smoother_server]: Running Nav2 LifecycleNode rcl preshutdown (smoother_server)
[component_container_isolated-16] [INFO] [1782640186.178186031] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640186.178243281] [map_server]: Running Nav2 LifecycleNode rcl preshutdown (map_server)
[component_container_isolated-16] [INFO] [1782640186.178366531] [map_server]: Deactivating
[component_container_isolated-16] [INFO] [1782640186.178531364] [map_server]: Destroying bond (map_server) to lifecycle manager.
[competition_master_stage3.py-17] [INFO] [1782640186.184917246] [competition_master_stage3]:   NAV_TO_QR............. 14.8s
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.189342210] [competition_master_stage3]:   BACKING_UP............ 6.0s
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.193510048] [competition_master_stage3]:   CRUISE_CHANNEL........ 41.2s
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[component_container_isolated-16] [INFO] [1782640186.189011168] [map_server]: Cleaning up
[component_container_isolated-16] [INFO] [1782640186.189245376] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1782640186.189495377] [controller_server]: Running Nav2 LifecycleNode rcl preshutdown (controller_server)
[component_container_isolated-16] [INFO] [1782640186.189949502] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[competition_master_stage3.py-17] [INFO] [1782640186.197378177] [competition_master_stage3]:   (transition/overhead). 68.2s
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.201590390] [competition_master_stage3]:   --- ---
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.205893229] [competition_master_stage3]:   QR 原始数据: 1585
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.210004400] [competition_master_stage3]:   QR 方向:   顺时针 (CW=顺时针/odd, CCW=逆时针/even)
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.214211280] [competition_master_stage3]:   VLM 结果:  这张图片展示了**室内电梯区域的临时布置场景**，疑似处于施工保护或场地筹备状态，细节如下：
[competition_master_stage3.py-17]
[competition_master_stage3.py-17]
[competition_master_stage3.py-17] ### 场景与布局
[competition_master_stage3.py-17] 画面聚焦建筑内部的电梯厅区域，地面铺有**浅色（浅黄/白色）反光塑料布**（施工用地面保护膜，表面带褶皱、反光明显），整体氛围偏向“临时布置”（如施工、活动筹备）。
[competition_master_stage3.py-17]
[competition_master_stage3.py-17]
[competition_master_stage3.py-17] ### 核心物体与细节
[competition_master_stage3.py-17] 1. **电梯与按钮**：
[competition_master_stage3.py-17]    - 左侧是**银色电梯门**，两侧
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.218205826] [competition_master_stage3]:   超时限制:  180.0s (全局)
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.221994872] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.228756129] [competition_master_stage3]: [TRAJ] CSV已保存: /userdata/dev_ws/trajectory_20260628_174946.csv (96 点)
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[ERROR] [bmi088_iio_bridge.py-5]: process has died [pid 38867, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/bmi088_iio_bridge.py --ros-args -r __node:=bmi088_iio_bridge --params-file /tmp/launch_params_iild0e17'].
[ERROR] [rviz2-18]: process has died [pid 39176, exit code -11, cmd '/opt/ros/humble/lib/rviz2/rviz2 -d /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/rviz/nav.rviz --ros-args -r __node:=rviz2'].
[competition_master_stage3.py-17] [INFO] [1782640186.590214497] [competition_master_stage3]: [TRAJ] Nav2 params snapshot: 31 keys
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.594899294] [competition_master_stage3]: [TRAJ] 摘要JSON已保存: /userdata/dev_ws/trajectory_20260628_174946_summary.json
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.599116549] [competition_master_stage3]: [TRAJ] 规划历史已保存: /userdata/dev_ws/trajectory_20260628_174946_plans.csv (31 次规划)
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-17] [INFO] [1782640186.617830237] [competition_master_stage3]: [TRAJ] costmap PGM已保存: /userdata/dev_ws/trajectory_20260628_174946_costmap.pgm
[competition_master_stage3.py-17] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[ERROR] [vision_ai_node-12]: process has died [pid 38919, exit code 1, cmd '/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node --ros-args -r __node:=vision_ai_node'].
[INFO] [aurora930_node-9]: process has finished cleanly [pid 38913]
[INFO] [competition_master_stage3.py-17]: process has finished cleanly [pid 39172]
[ERROR] [component_container_isolated-16]: process[component_container_isolated-16] failed to terminate '5' seconds after receiving 'SIGINT', escalating to 'SIGTERM'
[INFO] [component_container_isolated-16]: sending signal 'SIGTERM' to process[component_container_isolated-16]
[component_container_isolated-16] [INFO] [1782640190.791971752] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [component_container_isolated-16]: process[component_container_isolated-16] failed to terminate '10.0' seconds after receiving 'SIGTERM', escalating to 'SIGKILL'
[INFO] [component_container_isolated-16]: sending signal 'SIGKILL' to process[component_container_isolated-16]
[ERROR] [component_container_isolated-16]: process has died [pid 39170, exit code -9, cmd '/opt/ros/humble/lib/rclcpp_components/component_container_isolated --ros-args --log-level info --ros-args -r __node:=nav2_container --params-file /tmp/launch_params_0utdds8o --params-file /tmp/launch_params_muuy4nas -r /tf:=tf -r /tf_static:=tf_static'].
root@ubuntu:/userdata/dev_ws#
