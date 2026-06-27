root@ubuntu:/userdata/dev_ws# ros2 launch origincar_bringup stage3_bringup.launch.py
[INFO] [launch]: All log files can be found below /root/.ros/log/2026-06-27-11-21-18-867208-ubuntu-32476
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [origincar_base_node-1]: process started with pid [32490]
[INFO] [lslidar_driver_node-2]: process started with pid [32492]
[INFO] [robot_state_publisher-3]: process started with pid [32494]
[INFO] [imu_madgwick_filter.py-4]: process started with pid [32496]
[INFO] [bmi088_iio_bridge.py-5]: process started with pid [32498]
[INFO] [imu_madgwick_filter.py-6]: process started with pid [32500]
[INFO] [ekf_node-7]: process started with pid [32502]
[INFO] [cmd_vel_mux.py-8]: process started with pid [32504]
[INFO] [velocity_pid.py-9]: process started with pid [32510]
[INFO] [static_transform_publisher-10]: process started with pid [32546]
[INFO] [aurora930_node-11]: process started with pid [32548]
[INFO] [qr_decoder-12]: process started with pid [32550]
[INFO] [qr_decision-13]: process started with pid [32552]
[INFO] [vision_ai_node-14]: process started with pid [32554]
[origincar_base_node-1] [INFO] [1782530479.600959647] [origincar_base]: origincar_base serial port opened
[lslidar_driver_node-2] [INFO] [1782530479.592384685] [lslidar_driver_node]: Lidar is N10
[lslidar_driver_node-2] [INFO] [1782530479.606773191] [lslidar_driver_node]: Initialised lslidar without error
[lslidar_driver_node-2] [INFO] [1782530479.606937982] [lslidar_driver_node]: Successfully initialize driver...
[robot_state_publisher-3] [INFO] [1782530479.598703896] [robot_state_publisher]: got segment base_footprint
[robot_state_publisher-3] [INFO] [1782530479.599060396] [robot_state_publisher]: got segment base_link
[robot_state_publisher-3] [INFO] [1782530479.599141438] [robot_state_publisher]: got segment gyro_link
[robot_state_publisher-3] [INFO] [1782530479.599188480] [robot_state_publisher]: got segment laser_link
[ekf_node-7] Both imu1_differential and imu1_relative were set to true. Using differential mode.
[static_transform_publisher-10] [INFO] [1782530479.903577174] [depth_camera_tf]: Spinning until stopped - publishing transform
[static_transform_publisher-10] translation: ('0.140000', '0.000000', '0.050000')
[static_transform_publisher-10] rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
[static_transform_publisher-10] from 'base_link' to 'depth_camera_link'
[aurora930_node-11] W0627 11:21:20.509768 32548 ros2_node.cc:35] hello aurora 900/930
[qr_decoder-12] [INFO] [1782530480.642447905] [qr_decoder_zbar]: QR decoder (ZBar) started: rgb=/aurora/rgb/image_raw, depth=/aurora/depth/image_raw, filter=on, range=[50, 4000]mm, min_qr_len=1, intrinsics: fx=421.3 fy=422.3 cx=320.3 cy=197.0
[aurora930_node-11] 2026-06-27 11:21:20.727 (   0.392s) [        AF734020] device_manager_impl.cc:89    INFO| hotplug has registed by user
[aurora930_node-11] I0627 11:21:20.769949 32548 aurora900_ros2_device.cc:153] BOOT_ORDER_1::Found 1 deptrum device
[aurora930_node-11] I0627 11:21:20.770501 32548 aurora900_ros2_device.cc:162] BOOT_ORDER_1::No serial number provided: picking first device
[aurora930_node-11] 2026-06-27 11:21:20.770 (   0.436s) [        AF734020] device_manager_impl.cc:318   INFO| Device information:
[aurora930_node-11]     ir_pid:0x1930, rgb_pid:0x0
[aurora930_node-11]     serial number:HY400529001015314G00248
[aurora930_node-11] I0627 11:21:20.770705 32548 aurora900_ros2_device.cc:206] BOOT_ORDER_1::0:device start opening
[aurora930_node-11] 2026-06-27 11:21:20.772 (   0.438s) [        AF734020]   custom_usb_device.cc:101   INFO| bulk in endpoint addr:129
[aurora930_node-11] 2026-06-27 11:21:20.772 (   0.438s) [        AF734020]   custom_usb_device.cc:98    INFO| bulk out endpoint addr:2
[aurora930_node-11] 2026-06-27 11:21:20.793 (   0.459s) [        AF734020]deptrum_camera_aurora93:53    INFO| doe_broken:0 ito_support:1 crash_count:0 wdt_count:0 hard_reset_count:2 heart_boot_count:0 boot_total:114 last_crash_time:N
[aurora930_node-11] I0627 11:21:20.793622 32548 aurora900_ros2_device.cc:247] device supported frame_mode:
[aurora930_node-11] I0627 11:21:20.793735 32548 aurora900_ros2_device.cc:252] [0]:ir_mode:=13 kRes320x200Ir8Bit rgb_mode:=31 kRes320x200RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0627 11:21:20.793783 32548 aurora900_ros2_device.cc:252] [1]:ir_mode:=17 kRes480x300Depth16Bit rgb_mode:=32 kRes480x300RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0627 11:21:20.793818 32548 aurora900_ros2_device.cc:252] [2]:ir_mode:=20 kRes640x400Ir8Bit rgb_mode:=33 kRes640x400RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0627 11:21:20.793850 32548 aurora900_ros2_device.cc:266] current set mode ir_mode:20:kRes640x400Ir8Bit,rgb_mode:33:kRes640x400RgbYuv
[INFO] [map_server-15]: process started with pid [32652]
[INFO] [costmap_filter_info_server-16]: process started with pid [32654]
[INFO] [lifecycle_manager-17]: process started with pid [32656]
[aurora930_node-11] device_count==========1
[lifecycle_manager-17] [INFO] [1782530481.187254190] [lifecycle_manager_keepout]: Creating
[costmap_filter_info_server-16] [INFO] [1782530481.242090378] [costmap_filter_info_server]: This is costmap filter info publisher
[lifecycle_manager-17] [INFO] [1782530481.258463009] [lifecycle_manager_keepout]: Creating and initializing lifecycle service clients
[map_server-15] [INFO] [1782530481.306487360] [keepout_mask_server]:
[map_server-15]         keepout_mask_server lifecycle node launched.
[map_server-15]         Waiting on external lifecycle transitions to activate
[map_server-15]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[map_server-15] [INFO] [1782530481.307008527] [keepout_mask_server]: Creating
[aurora930_node-11] I0627 11:21:21.315716 32548 aurora900_ros2_device.cc:387] Switch Auto Exposure
[aurora930_node-11] 2026-06-27 11:21:21.375 (   1.041s) [        AF734020]      aurora900_impl.cc:1106  INFO| SetHeartbeat user set heartbeat enable: 0
[lifecycle_manager-17] [INFO] [1782530481.578091254] [lifecycle_manager_keepout]: Starting managed nodes bringup...
[lifecycle_manager-17] [INFO] [1782530481.578626504] [lifecycle_manager_keepout]: Configuring keepout_mask_server
[map_server-15] [INFO] [1782530481.579781671] [keepout_mask_server]: Configuring
[map_server-15] [INFO] [1782530481.580084796] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.yaml
[map_server-15] [INFO] [1782530481.581440630] [map_io]: resolution: 0.05
[map_server-15] [INFO] [1782530481.581526630] [map_io]: origin[0]: -2.65
[map_server-15] [INFO] [1782530481.581558546] [map_io]: origin[1]: -4.5
[map_server-15] [INFO] [1782530481.581585588] [map_io]: origin[2]: 0
[map_server-15] [INFO] [1782530481.581614088] [map_io]: free_thresh: 0.5
[map_server-15] [INFO] [1782530481.581642588] [map_io]: occupied_thresh: 0.5
[map_server-15] [INFO] [1782530481.581689547] [map_io]: mode: scale
[map_server-15] [INFO] [1782530481.581720005] [map_io]: negate: 0
[map_server-15] [INFO] [1782530481.582528964] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm
[costmap_filter_info_server-16] [INFO] [1782530481.601043179] [keepout_filter_info_server]:
[costmap_filter_info_server-16]         keepout_filter_info_server lifecycle node launched.
[costmap_filter_info_server-16]         Waiting on external lifecycle transitions to activate
[costmap_filter_info_server-16]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[map_server-15] [INFO] [1782530481.633131316] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm: 163 X 141 map @ 0.05 m/cell
[lifecycle_manager-17] [INFO] [1782530481.686870419] [lifecycle_manager_keepout]: Configuring keepout_filter_info_server
[costmap_filter_info_server-16] [INFO] [1782530481.689206795] [keepout_filter_info_server]: Configuring
[lifecycle_manager-17] [INFO] [1782530481.724296308] [lifecycle_manager_keepout]: Activating keepout_mask_server
[map_server-15] [INFO] [1782530481.725255475] [keepout_mask_server]: Activating
[map_server-15] [INFO] [1782530481.725643767] [keepout_mask_server]: Creating bond (keepout_mask_server) to lifecycle manager.
[imu_madgwick_filter.py-4] [INFO] [1782530481.761682489] [imu_madgwick_filter]: [imu_madgwick] init: beta=0.0330, gyro_noise=0.0010, accel_noise=0.050
[imu_madgwick_filter.py-4] [INFO] [1782530481.768428783] [imu_madgwick_filter]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-4] [INFO] [1782530481.771397034] [imu_madgwick_filter]: [imu_madgwick] accel init: roll=-0.5deg, pitch=0.0deg
[aurora930_node-11] I0627 11:21:21.788837 32548 aurora900_ros2_device.cc:304] BOOT_ORDER_1::Device information:
[aurora930_node-11] I0627 11:21:21.789120 32548 aurora900_ros2_device.cc:305]    sdk version: 1.1.22
[aurora930_node-11] I0627 11:21:21.789186 32548 aurora900_ros2_device.cc:306]    device name: Aurora 930
[aurora930_node-11] I0627 11:21:21.789214 32548 aurora900_ros2_device.cc:307]    serial number: HY400529001015314G00248
[aurora930_node-11] I0627 11:21:21.789243 32548 aurora900_ros2_device.cc:308]    firmware version: 1.7.2
[aurora930_node-11] I0627 11:21:21.789300 32548 camera_parameters.cc:134] BOOT_ORDER_1::Camera Parameters:
[aurora930_node-11] I0627 11:21:21.789330 32548 camera_parameters.cc:135] BOOT_ORDER_1::         Ir Intrinsics:
[aurora930_node-11] I0627 11:21:21.789357 32548 camera_parameters.cc:146]                Resolution:
[aurora930_node-11] I0627 11:21:21.789383 32548 camera_parameters.cc:147]                        Rows:400
[aurora930_node-11] I0627 11:21:21.789408 32548 camera_parameters.cc:148]                        Cols:640
[aurora930_node-11] I0627 11:21:21.789433 32548 camera_parameters.cc:149]                Intrinsics:
[aurora930_node-11] I0627 11:21:21.789458 32548 camera_parameters.cc:150]                        fx: 421.307
[aurora930_node-11] I0627 11:21:21.789562 32548 camera_parameters.cc:151]                        fy: 422.254
[aurora930_node-11] I0627 11:21:21.789597 32548 camera_parameters.cc:152]                        cx: 320.27
[aurora930_node-11] I0627 11:21:21.789652 32548 camera_parameters.cc:153]                        cy: 197.01
[aurora930_node-11] I0627 11:21:21.789697 32548 camera_parameters.cc:154]                        k1: 0.0606853
[aurora930_node-11] I0627 11:21:21.789731 32548 camera_parameters.cc:155]                        k2: -0.10961
[aurora930_node-11] I0627 11:21:21.789763 32548 camera_parameters.cc:156]                        p1: 0.00126689
[aurora930_node-11] I0627 11:21:21.789794 32548 camera_parameters.cc:157]                        p2: -0.00120539
[aurora930_node-11] I0627 11:21:21.789824 32548 camera_parameters.cc:158]                        k3: 0.0522281
[aurora930_node-11] I0627 11:21:21.789855 32548 camera_parameters.cc:138] BOOT_ORDER_1::         Rgb Intrinsics:
[aurora930_node-11] I0627 11:21:21.789882 32548 camera_parameters.cc:146]                Resolution:
[aurora930_node-11] I0627 11:21:21.789907 32548 camera_parameters.cc:147]                        Rows:400
[aurora930_node-11] I0627 11:21:21.789932 32548 camera_parameters.cc:148]                        Cols:640
[aurora930_node-11] I0627 11:21:21.789958 32548 camera_parameters.cc:149]                Intrinsics:
[aurora930_node-11] I0627 11:21:21.789981 32548 camera_parameters.cc:150]                        fx: 416.49
[aurora930_node-11] I0627 11:21:21.790014 32548 camera_parameters.cc:151]                        fy: 417.383
[aurora930_node-11] I0627 11:21:21.790045 32548 camera_parameters.cc:152]                        cx: 316.832
[aurora930_node-11] I0627 11:21:21.790083 32548 camera_parameters.cc:153]                        cy: 188.753
[aurora930_node-11] I0627 11:21:21.790114 32548 camera_parameters.cc:154]                        k1: 0.00611878
[aurora930_node-11] I0627 11:21:21.790151 32548 camera_parameters.cc:155]                        k2: -0.0490436
[aurora930_node-11] I0627 11:21:21.790182 32548 camera_parameters.cc:156]                        p1: 0.000399548
[aurora930_node-11] I0627 11:21:21.790213 32548 camera_parameters.cc:157]                        p2: 0.000563892
[aurora930_node-11] I0627 11:21:21.790249 32548 camera_parameters.cc:158]                        k3: 0.0308458
[aurora930_node-11] I0627 11:21:21.790282 32548 camera_parameters.cc:141] BOOT_ORDER_1::         Ir to Rgb Extrinsic:
[aurora930_node-11] I0627 11:21:21.790307 32548 camera_parameters.cc:162]                Extrinsics:
[aurora930_node-11] I0627 11:21:21.790338 32548 camera_parameters.cc:163]                        Rotation[0]: 0.999973, 0.00724076, -0.00112023
[aurora930_node-11] I0627 11:21:21.790375 32548 camera_parameters.cc:165]                        Rotation[1]: -0.00724006, 0.999973, 0.000633162
[aurora930_node-11] I0627 11:21:21.790416 32548 camera_parameters.cc:167]                        Rotation[2]: 0.00112478, -0.000625033, 0.999999
[aurora930_node-11] I0627 11:21:21.790521 32548 camera_parameters.cc:169]                        Translation: -9.88662, 0.117748, 0.603513
[aurora930_node-11] 2026-06-27 11:21:21.791 (   1.456s) [        AF734020]      aurora900_impl.cc:578   INFO| stream_mask_:0, rgb_stream_count_:1
[bmi088_iio_bridge.py-5] [INFO] [1782530481.834067474] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1782530481.837222184] [bmi088_iio_bridge]:   DIAGNOSTIC: Scanning IIO devices under /sys/bus/iio/devices/
[bmi088_iio_bridge.py-5] [INFO] [1782530481.839983435] [bmi088_iio_bridge]:   Equivalent to: ls /sys/bus/iio/devices/*/name
[bmi088_iio_bridge.py-5] [INFO] [1782530481.843491978] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1782530481.846422521] [bmi088_iio_bridge]:   iio:device0/name = "34190000.adc"
[bmi088_iio_bridge.py-5] [INFO] [1782530481.862607818] [bmi088_iio_bridge]:   iio:device1/name = "bmi08x"
[bmi088_iio_bridge.py-5] [INFO] [1782530481.868006945] [bmi088_iio_bridge]:   trigger0/name = "34190000.adc-dev0"
[lifecycle_manager-17] [INFO] [1782530481.846356021] [lifecycle_manager_keepout]: Server keepout_mask_server connected with bond.
[lifecycle_manager-17] [INFO] [1782530481.846569062] [lifecycle_manager_keepout]: Activating keepout_filter_info_server
[costmap_filter_info_server-16] [INFO] [1782530481.847379896] [keepout_filter_info_server]: Activating
[costmap_filter_info_server-16] [INFO] [1782530481.847606021] [keepout_filter_info_server]: Creating bond (keepout_filter_info_server) to lifecycle manager.
[bmi088_iio_bridge.py-5] [INFO] [1782530481.870765780] [bmi088_iio_bridge]:   Total IIO devices found: 3
[cmd_vel_mux.py-8] [INFO] [1782530481.874258198] [cmd_vel_mux]:   nav: /nav_cmd_vel priority=10 timeout=0.5s
[bmi088_iio_bridge.py-5] [INFO] [1782530481.877120949] [bmi088_iio_bridge]:   BMI088 kernel module APPEARS LOADED: 1 BMI device(s) detected
[bmi088_iio_bridge.py-5] [INFO] [1782530481.882463868] [bmi088_iio_bridge]:   BMI device names: ['bmi08x']
[bmi088_iio_bridge.py-5] [INFO] [1782530481.890254204] [bmi088_iio_bridge]:   gyro:  /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_anglvel is_si=False scale_override=0.00053
[cmd_vel_mux.py-8] [INFO] [1782530481.897344040] [cmd_vel_mux]:   pid: /pid_cmd_vel priority=20 timeout=0.3s
[bmi088_iio_bridge.py-5] [INFO] [1782530481.898705915] [bmi088_iio_bridge]:   accel: /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_accel is_si=False scale_override=0.00341
[cmd_vel_mux.py-8] [INFO] [1782530481.921757382] [cmd_vel_mux]:   stop: /stop_cmd_vel priority=255 timeout=0.5s
[cmd_vel_mux.py-8] [INFO] [1782530481.948706226] [cmd_vel_mux]: cmd_vel_mux 就绪: 输出 → /cmd_vel_muxed
[lifecycle_manager-17] [INFO] [1782530481.963324481] [lifecycle_manager_keepout]: Server keepout_filter_info_server connected with bond.
[lifecycle_manager-17] [INFO] [1782530481.963478565] [lifecycle_manager_keepout]: Managed nodes are active
[lifecycle_manager-17] [INFO] [1782530481.963548440] [lifecycle_manager_keepout]: Creating bond timer...
[cmd_vel_mux.py-8] [INFO] [1782530481.983231364] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[imu_madgwick_filter.py-6] [INFO] [1782530481.995464868] [imu_madgwick_bmi088]: [imu_madgwick] init: beta=0.0030, gyro_noise=0.0002, accel_noise=0.010
[imu_madgwick_filter.py-6] [INFO] [1782530482.093890864] [imu_madgwick_bmi088]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-6] [INFO] [1782530482.097188323] [imu_madgwick_bmi088]: [imu_madgwick] accel init: roll=-2.2deg, pitch=-3.3deg
[INFO] [component_container_isolated-18]: process started with pid [32897]
[velocity_pid.py-9] [INFO] [1782530482.036680092] [velocity_pid]: VelocityPID 就绪: vx(Kp=0.8, Ki=0.60, Kd=0.05, max_i=0.68) wz(Kp=1.0, Ki=0.40, Kd=0.02, max_i=2.24) | feedback_timeout=0.5s
[velocity_pid.py-9] [INFO] [1782530482.046566679] [velocity_pid]: [vel_pid] ACTIVATED vx=0.00 wz=0.00
[bmi088_iio_bridge.py-5] [INFO] [1782530482.066012228] [bmi088_iio_bridge]: BMI088 IIO Bridge 启动 @ 100Hz -> /imu_data  [OK]
[bmi088_iio_bridge.py-5] [INFO] [1782530487.764698290] [bmi088_iio_bridge]:   gyro bias calibrated: (0.002904, 0.000670, -0.002788) rad/s
[aurora930_node-11] 2026-06-27 11:21:22.105 (   1.771s) [        7BFF57E0]deptrum_camera_aurora93:407    ERR| recv first frame time is 1782530482105
[qr_decision-13] [INFO] [1782530482.421239780] [qr_decision]: qr_decision started: cooldown=3.0s, awaiting /sign from qr_decoder
[lslidar_driver_node-2] port = /dev/ttyACM1, baud_rate = 230400
[lslidar_driver_node-2] open_port /dev/ttyACM1 OK !
[vision_ai_node-14] [INFO] [1782530485.976007074] [vision_ai_node]: 成功加载配置文件: /userdata/dev_ws/install/racing_vision_ai/share/racing_vision_ai/config/vision_ai_config.yaml
[vision_ai_node-14] [INFO] [1782530486.359057726] [vision_ai_node]: Volcengine Ark client initialized successfully
[vision_ai_node-14] [INFO] [1782530486.380512610] [vision_ai_node]: Vision AI Node initialized
[vision_ai_node-14] [INFO] [1782530486.383013861] [vision_ai_node]: Waiting for sign4return=100 signal...
[vision_ai_node-14] [INFO] [1782530486.385506778] [vision_ai_node]: Results will be published to vlm_result
[INFO] [competition_master_stage3.py-19]: process started with pid [32899]
[INFO] [rviz2-20]: process started with pid [32905]
[component_container_isolated-18] [INFO] [1782530489.731032220] [nav2_container]: Load Library: /opt/ros/humble/lib/libcontroller_server_core.so
[component_container_isolated-18] [INFO] [1782530489.761910650] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-18] [INFO] [1782530489.762092525] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-18] [INFO] [1782530489.844294642] [controller_server]:
[component_container_isolated-18]       controller_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782530489.870159695] [controller_server]: Creating controller server
[component_container_isolated-18] [INFO] [1782530489.973370196] [local_costmap.local_costmap]:
[component_container_isolated-18]       local_costmap lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782530489.977757989] [local_costmap.local_costmap]: Creating Costmap
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/controller_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782530490.014355046] [nav2_container]: Load Library: /opt/ros/humble/lib/libmap_server_core.so
[component_container_isolated-18] [INFO] [1782530490.073957404] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::CostmapFilterInfoServer>
[component_container_isolated-18] [INFO] [1782530490.074182196] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapSaver>
[component_container_isolated-18] [INFO] [1782530490.074318321] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-18] [INFO] [1782530490.074423071] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-18] [INFO] [1782530490.143390350] [map_server]:
[component_container_isolated-18]       map_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782530490.143762975] [map_server]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/map_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782530490.147867852] [nav2_container]: Load Library: /opt/ros/humble/lib/libsmoother_server_core.so
[component_container_isolated-18] [INFO] [1782530490.154547771] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-18] [INFO] [1782530490.154729563] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-18] [INFO] [1782530490.227206760] [smoother_server]:
[component_container_isolated-18]       smoother_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782530490.236995889] [smoother_server]: Creating smoother server
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/smoother_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782530490.245564434] [nav2_container]: Load Library: /opt/ros/humble/lib/libamcl_core.so
[component_container_isolated-18] [INFO] [1782530490.259738398] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-18] [INFO] [1782530490.259911232] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-18] [INFO] [1782530490.343926684] [amcl]:
[component_container_isolated-18]       amcl lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782530490.347766185] [amcl]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/amcl' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782530490.494487371] [nav2_container]: Load Library: /opt/ros/humble/lib/libplanner_server_core.so
[component_container_isolated-18] [INFO] [1782530490.498182123] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-18] [INFO] [1782530490.498353331] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-18] [INFO] [1782530490.576231947] [planner_server]:
[component_container_isolated-18]       planner_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782530490.589685995] [planner_server]: Creating
[component_container_isolated-18] [INFO] [1782530490.681219283] [global_costmap.global_costmap]:
[component_container_isolated-18]       global_costmap lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782530490.683529909] [global_costmap.global_costmap]: Creating Costmap
[component_container_isolated-18] [INFO] [1782530490.731877554] [nav2_container]: Load Library: /opt/ros/humble/lib/libnav2_lifecycle_manager_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/planner_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782530490.735781764] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1782530490.735969347] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1782530490.849928103] [lifecycle_manager_localization]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_localization' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782530490.878662240] [lifecycle_manager_localization]: Creating and initializing lifecycle service clients
[component_container_isolated-18] [INFO] [1782530490.879055074] [nav2_container]: Load Library: /opt/ros/humble/lib/libbehavior_server_core.so
[component_container_isolated-18] [INFO] [1782530490.899059999] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-18] [INFO] [1782530490.899294791] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-18] [INFO] [1782530490.945569727] [lifecycle_manager_localization]: Starting managed nodes bringup...
[component_container_isolated-18] [INFO] [1782530490.963127026] [lifecycle_manager_localization]: Configuring map_server
[component_container_isolated-18] [INFO] [1782530490.973590030] [map_server]: Configuring
[component_container_isolated-18] [INFO] [1782530490.974050530] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.yaml
[component_container_isolated-18] [INFO] [1782530490.975369947] [map_io]: resolution: 0.05
[component_container_isolated-18] [INFO] [1782530490.975473156] [map_io]: origin[0]: -2.65
[component_container_isolated-18] [INFO] [1782530490.975505572] [map_io]: origin[1]: -4.5
[component_container_isolated-18] [INFO] [1782530490.975533281] [map_io]: origin[2]: 0
[component_container_isolated-18] [INFO] [1782530490.975561864] [map_io]: free_thresh: 0.25
[component_container_isolated-18] [INFO] [1782530490.975589989] [map_io]: occupied_thresh: 0.65
[component_container_isolated-18] [INFO] [1782530490.975638198] [map_io]: mode: trinary
[component_container_isolated-18] [INFO] [1782530490.975670739] [map_io]: negate: 0
[component_container_isolated-18] [INFO] [1782530490.976519406] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm
[component_container_isolated-18] [INFO] [1782530490.985890785] [behavior_server]:
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/behavior_server' in container '/nav2_container'
[component_container_isolated-18]       behavior_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782530491.009495128] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm: 163 X 141 map @ 0.05 m/cell
[component_container_isolated-18] [INFO] [1782530491.035339639] [lifecycle_manager_localization]: Configuring amcl
[component_container_isolated-18] [INFO] [1782530491.037166223] [amcl]: Configuring
[component_container_isolated-18] [INFO] [1782530491.037821932] [amcl]: initTransforms
[component_container_isolated-18] [INFO] [1782530491.047083269] [nav2_container]: Load Library: /opt/ros/humble/lib/libbt_navigator_core.so
[component_container_isolated-18] [INFO] [1782530491.062106526] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-18] [INFO] [1782530491.062292026] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-18] [INFO] [1782530491.129100429] [amcl]: initPubSub
[component_container_isolated-18] [INFO] [1782530491.159583025] [amcl]: Subscribed to map topic.
[component_container_isolated-18] [INFO] [1782530491.201753043] [lifecycle_manager_localization]: Activating map_server
[component_container_isolated-18] [INFO] [1782530491.202648043] [map_server]: Activating
[component_container_isolated-18] [INFO] [1782530491.203145960] [map_server]: Creating bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530491.203345335] [amcl]: Received a 163 X 141 map @ 0.050 m/pix
[component_container_isolated-18] [INFO] [1782530491.258456192] [bt_navigator]:
[component_container_isolated-18]       bt_navigator lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/bt_navigator' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782530491.258798234] [bt_navigator]: Creating
[component_container_isolated-18] [INFO] [1782530491.273443323] [nav2_container]: Load Library: /opt/ros/humble/lib/libwaypoint_follower_core.so
[component_container_isolated-18] [INFO] [1782530491.277805367] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-18] [INFO] [1782530491.278748867] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-18] [INFO] [1782530491.326128137] [lifecycle_manager_localization]: Server map_server connected with bond.
[component_container_isolated-18] [INFO] [1782530491.326348512] [lifecycle_manager_localization]: Activating amcl
[component_container_isolated-18] [INFO] [1782530491.327335721] [amcl]: Activating
[component_container_isolated-18] [INFO] [1782530491.327569596] [amcl]: initialPoseReceived
[component_container_isolated-18] [INFO] [1782530491.328047971] [amcl]: Setting pose (1782530491.328042): -1.985 -0.014 0.262
[component_container_isolated-18] [INFO] [1782530491.332140140] [amcl]: Creating bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530491.367739988] [amcl]: createLaserObject
[component_container_isolated-18] [INFO] [1782530491.410678215] [waypoint_follower]:
[component_container_isolated-18]       waypoint_follower lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782530491.415829467] [waypoint_follower]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/waypoint_follower' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782530491.440015144] [nav2_container]: Load Library: /opt/ros/humble/lib/libvelocity_smoother_core.so
[component_container_isolated-18] [INFO] [1782530491.443086020] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-18] [INFO] [1782530491.443245395] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-18] [INFO] [1782530491.454168608] [lifecycle_manager_localization]: Server amcl connected with bond.
[component_container_isolated-18] [INFO] [1782530491.454366941] [lifecycle_manager_localization]: Managed nodes are active
[component_container_isolated-18] [INFO] [1782530491.454487108] [lifecycle_manager_localization]: Creating bond timer...
[component_container_isolated-18] [INFO] [1782530491.531696266] [velocity_smoother]:
[component_container_isolated-18]       velocity_smoother lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/velocity_smoother' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782530491.551233024] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1782530491.551421274] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[imu_madgwick_filter.py-4] [INFO] [1782530491.630875141] [imu_madgwick_filter]: [imu_madgwick ->] msgs=200 q_w=0.9996 angle=3.1deg beta=0.0330
[component_container_isolated-18] [INFO] [1782530491.636259310] [lifecycle_manager_navigation]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_navigation' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782530491.670910575] [lifecycle_manager_navigation]: Creating and initializing lifecycle service clients
[imu_madgwick_filter.py-6] [INFO] [1782530491.766141240] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=423 q_w=0.9994 angle=4.1deg beta=0.0030
[component_container_isolated-18] [INFO] [1782530491.801711255] [lifecycle_manager_navigation]: Starting managed nodes bringup...
[component_container_isolated-18] [INFO] [1782530491.802062422] [lifecycle_manager_navigation]: Configuring controller_server
[component_container_isolated-18] [INFO] [1782530491.803688172] [controller_server]: Configuring controller interface
[component_container_isolated-18] [INFO] [1782530491.805673923] [controller_server]: getting goal checker plugins..
[component_container_isolated-18] [INFO] [1782530491.807097090] [controller_server]: Controller frequency set to 10.0000Hz
[component_container_isolated-18] [INFO] [1782530491.807455591] [local_costmap.local_costmap]: Configuring
[component_container_isolated-18] [INFO] [1782530491.860684321] [local_costmap.local_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1782530491.892718043] [local_costmap.local_costmap]: Subscribed to Topics: scan aurora_points
[component_container_isolated-18] [INFO] [1782530491.994722836] [local_costmap.local_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1782530491.995097628] [local_costmap.local_costmap]: Using plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1782530492.023707474] [local_costmap.local_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1782530492.025990725] [local_costmap.local_costmap]: Using plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1782530492.051334694] [local_costmap.local_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1782530492.121944141] [controller_server]: Created progress_checker : progress_checker of type nav2_controller::SimpleProgressChecker
[component_container_isolated-18] [INFO] [1782530492.133265479] [controller_server]: Created goal checker : goal_checker of type nav2_controller::SimpleGoalChecker
[component_container_isolated-18] [INFO] [1782530492.145333609] [controller_server]: Controller Server has goal_checker  goal checkers available.
[component_container_isolated-18] [INFO] [1782530492.151279695] [controller_server]: Created controller : FollowPath of type nav2_regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1782530492.235253648] [controller_server]: Controller Server has FollowPath  controllers available.
[component_container_isolated-18] [INFO] [1782530492.307744137] [lifecycle_manager_navigation]: Configuring smoother_server
[component_container_isolated-18] [INFO] [1782530492.309049887] [smoother_server]: Configuring smoother server
[component_container_isolated-18] [INFO] [1782530492.385562128] [smoother_server]: Created smoother : SmoothPath of type nav2_constrained_smoother/ConstrainedSmoother
[component_container_isolated-18] [INFO] [1782530492.444669320] [smoother_server]: Smoother Server has SmoothPath  smoothers available.
[component_container_isolated-18] [INFO] [1782530492.485225629] [lifecycle_manager_navigation]: Configuring planner_server
[component_container_isolated-18] [INFO] [1782530492.486184755] [planner_server]: Configuring
[component_container_isolated-18] [INFO] [1782530492.486481088] [global_costmap.global_costmap]: Configuring
[component_container_isolated-18] [INFO] [1782530492.529564273] [global_costmap.global_costmap]: Using plugin "static_layer"
[component_container_isolated-18] [INFO] [1782530492.545311780] [global_costmap.global_costmap]: Subscribing to the map topic (/map) with transient local durability
[component_container_isolated-18] [INFO] [1782530492.558534244] [global_costmap.global_costmap]: Initialized plugin "static_layer"
[component_container_isolated-18] [INFO] [1782530492.558746577] [global_costmap.global_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1782530492.580135837] [global_costmap.global_costmap]: Subscribed to Topics: scan aurora_points
[competition_master_stage3.py-19] [INFO] [1782530492.653440493] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1782530492.660178954] [competition_master_stage3]: === [Stage 3] 总控节点初始化 ===
[competition_master_stage3.py-19] [INFO] [1782530492.669948292] [competition_master_stage3]:   QR点:    (0.41, -3.17, yaw=0.00)
[competition_master_stage3.py-19] [INFO] [1782530492.675296086] [competition_master_stage3]:   通道入口: (0.38, -1.10, yaw=0.00)
[competition_master_stage3.py-19] [INFO] [1782530492.679329796] [competition_master_stage3]:   P点:     (-1.99, -0.01, yaw=0.26)
[competition_master_stage3.py-19] [INFO] [1782530492.682209214] [competition_master_stage3]:   cruise_cw: 3 路点 → VLM=(3.12, -1.34)
[competition_master_stage3.py-19] [INFO] [1782530492.685956173] [competition_master_stage3]:   cruise_ccw: 4 路点 → VLM=(2.17, 0.69)
[competition_master_stage3.py-19] [INFO] [1782530492.694598469] [competition_master_stage3]:   超时: total=180.0s QR=90.0s entry=60.0s cruise=180.0s vlm=30.0s return=120.0s
[competition_master_stage3.py-19] [INFO] [1782530492.701068555] [competition_master_stage3]:   回退QR方向: 逆时针
[component_container_isolated-18] [INFO] [1782530492.698865096] [global_costmap.global_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1782530492.699099971] [global_costmap.global_costmap]: Using plugin "keepout_filter"
[competition_master_stage3.py-19] [INFO] [1782530492.705692474] [competition_master_stage3]:   VLM结果话题: vlm_result
[competition_master_stage3.py-19] [INFO] [1782530492.709922350] [competition_master_stage3]: ============================================================
[component_container_isolated-18] [INFO] [1782530492.718645229] [global_costmap.global_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1782530492.718858646] [global_costmap.global_costmap]: Using plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1782530492.729312567] [global_costmap.global_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1782530492.795032512] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 163 X 141 at 0.050000 m/pix
[component_container_isolated-18] [INFO] [1782530492.828436609] [planner_server]: Created global planner plugin GridBased of type nav2_smac_planner/SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1782530492.828691443] [planner_server]: Configuring GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1782530492.876706838] [planner_server]: Even sized heuristic lookup table size set 200.000000, increasing size by 1 to make odd
[rviz2-20] [INFO] [1782530493.703709820] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-20] [INFO] [1782530493.704702904] [rviz2]: OpenGl version: 4.5 (GLSL 4.5)
[rviz2-20] [INFO] [1782530494.034888130] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-20] [INFO] [1782530496.289948831] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[rviz2-20] [ERROR] [1782530496.693487511] [rviz2]: Vertex Program:rviz/glsl120/indexed_8bit_image.vert Fragment Program:rviz/glsl120/indexed_8bit_image.frag GLSL link result :
[rviz2-20] active samplers with a different type refer to the same texture image unit
[qr_decoder-12] [INFO] [1782530498.260502801] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=200 last_qr_frame=-1 gap=-1 frames rejects=0
[imu_madgwick_filter.py-4] [INFO] [1782530501.626639983] [imu_madgwick_filter]: [imu_madgwick ->] msgs=400 q_w=0.9986 angle=6.1deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1782530501.748051790] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=959 q_w=0.9994 angle=4.1deg beta=0.0030
[component_container_isolated-18] [INFO] [1782530506.844258126] [planner_server]: Configured plugin GridBased of type SmacPlannerHybrid with maximum iterations 1500, max on approach iterations 300, and not allowing unknown traversal. Tolerance 0.50.Using motion model: Reeds-Shepp.
[component_container_isolated-18] [INFO] [1782530506.844519001] [planner_server]: Planner Server has GridBased  planners available.
[component_container_isolated-18] [INFO] [1782530506.919761538] [lifecycle_manager_navigation]: Configuring behavior_server
[component_container_isolated-18] [INFO] [1782530506.921080872] [behavior_server]: Configuring
[component_container_isolated-18] [INFO] [1782530506.963223101] [behavior_server]: Creating behavior plugin spin of type nav2_behaviors/Spin
[component_container_isolated-18] [INFO] [1782530506.967359770] [behavior_server]: Configuring spin
[component_container_isolated-18] [INFO] [1782530507.021451130] [behavior_server]: Creating behavior plugin backup of type nav2_behaviors/BackUp
[component_container_isolated-18] [INFO] [1782530507.026701007] [behavior_server]: Configuring backup
[component_container_isolated-18] [INFO] [1782530507.069533362] [behavior_server]: Creating behavior plugin drive_on_heading of type nav2_behaviors/DriveOnHeading
[component_container_isolated-18] [INFO] [1782530507.073549364] [behavior_server]: Configuring drive_on_heading
[component_container_isolated-18] [INFO] [1782530507.122430888] [behavior_server]: Creating behavior plugin wait of type nav2_behaviors/Wait
[component_container_isolated-18] [INFO] [1782530507.127290016] [behavior_server]: Configuring wait
[component_container_isolated-18] [INFO] [1782530507.161831991] [lifecycle_manager_navigation]: Configuring bt_navigator
[component_container_isolated-18] [INFO] [1782530507.162568658] [bt_navigator]: Configuring
[competition_master_stage3.py-19] [INFO] [1782530507.444151673] [competition_master_stage3]: [LAUNCH] 发车阶段: 15.0s
[competition_master_stage3.py-19] [INFO] [1782530507.451159385] [competition_master_stage3]: >>> 系统就绪, 开始 Stage 3 导航
[competition_master_stage3.py-19] [INFO] [1782530507.462317349] [competition_master_stage3]: [BAG] 录制开始: stage3_20260627_112147
[competition_master_stage3.py-19] [INFO] [1782530507.468286644] [competition_master_stage3]: [状态机] INIT → NAV_TO_QR
[competition_master_stage3.py-19] [INFO] [1782530507.480906817] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-18] [INFO] [1782530507.673427412] [lifecycle_manager_navigation]: Configuring waypoint_follower
[component_container_isolated-18] [INFO] [1782530507.676534831] [waypoint_follower]: Configuring
[competition_master_stage3.py-19] [WARN] [1782530507.709910264] [competition_master_stage3]: 导航目标被拒绝, 3s 后重试...
[component_container_isolated-18] [INFO] [1782530507.801645393] [waypoint_follower]: Created waypoint_task_executor : wait_at_waypoint of type nav2_waypoint_follower::WaitAtWaypoint
[component_container_isolated-18] [INFO] [1782530507.811243856] [lifecycle_manager_navigation]: Configuring velocity_smoother
[component_container_isolated-18] [INFO] [1782530507.812444523] [velocity_smoother]: Configuring velocity smoother
[component_container_isolated-18] [INFO] [1782530507.856508587] [lifecycle_manager_navigation]: Activating controller_server
[component_container_isolated-18] [INFO] [1782530507.857901046] [controller_server]: Activating
[component_container_isolated-18] [INFO] [1782530507.858215129] [local_costmap.local_costmap]: Activating
[component_container_isolated-18] [INFO] [1782530507.858357838] [local_costmap.local_costmap]: Checking transform
[component_container_isolated-18] [INFO] [1782530507.858755796] [local_costmap.local_costmap]: start
[component_container_isolated-18] [INFO] [1782530507.873655679] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1782530507.883372350] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1782530507.883622184] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1782530507.892497730] [local_costmap.local_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[component_container_isolated-18] [INFO] [1782530508.183285125] [controller_server]: Activating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1782530508.183677126] [controller_server]: Creating bond (controller_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530508.304061269] [lifecycle_manager_navigation]: Server controller_server connected with bond.
[component_container_isolated-18] [INFO] [1782530508.304223894] [lifecycle_manager_navigation]: Activating smoother_server
[component_container_isolated-18] [INFO] [1782530508.305520020] [smoother_server]: Activating
[component_container_isolated-18] [INFO] [1782530508.305807354] [smoother_server]: Activating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1782530508.306078395] [smoother_server]: Creating bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530508.422759329] [lifecycle_manager_navigation]: Server smoother_server connected with bond.
[component_container_isolated-18] [INFO] [1782530508.422928246] [lifecycle_manager_navigation]: Activating planner_server
[component_container_isolated-18] [INFO] [1782530508.424442830] [planner_server]: Activating
[component_container_isolated-18] [INFO] [1782530508.424815705] [global_costmap.global_costmap]: Activating
[component_container_isolated-18] [INFO] [1782530508.424958997] [global_costmap.global_costmap]: Checking transform
[component_container_isolated-18] [INFO] [1782530508.425273997] [global_costmap.global_costmap]: start
[component_container_isolated-18] [INFO] [1782530508.440831713] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1782530508.453922678] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1782530508.454114970] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1782530508.462348016] [global_costmap.global_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[rviz2-20] [INFO] [1782530508.495739824] [rviz2]: Trying to create a map of size 60 x 60 using 1 swatches
[component_container_isolated-18] [INFO] [1782530509.453868057] [planner_server]: Activating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1782530509.461516186] [planner_server]: Creating bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530509.590833168] [lifecycle_manager_navigation]: Server planner_server connected with bond.
[component_container_isolated-18] [INFO] [1782530509.591020002] [lifecycle_manager_navigation]: Activating behavior_server
[component_container_isolated-18] [INFO] [1782530509.592298003] [behavior_server]: Activating
[component_container_isolated-18] [INFO] [1782530509.592427753] [behavior_server]: Activating spin
[component_container_isolated-18] [INFO] [1782530509.592590544] [behavior_server]: Activating backup
[component_container_isolated-18] [INFO] [1782530509.592681003] [behavior_server]: Activating drive_on_heading
[component_container_isolated-18] [INFO] [1782530509.592756378] [behavior_server]: Activating wait
[component_container_isolated-18] [INFO] [1782530509.592839003] [behavior_server]: Creating bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530509.713192730] [lifecycle_manager_navigation]: Server behavior_server connected with bond.
[component_container_isolated-18] [INFO] [1782530509.713457856] [lifecycle_manager_navigation]: Activating bt_navigator
[component_container_isolated-18] [INFO] [1782530509.714835773] [bt_navigator]: Activating
[rviz2-20] [INFO] [1782530509.797318606] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[component_container_isolated-18] [WARN] [1782530509.886953860] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1782530510.051243819] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1782530510.140900531] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1782530510.327050376] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1782530510.585480425] [bt_navigator_navigate_to_pose_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[competition_master_stage3.py-19] [INFO] [1782530510.728611332] [competition_master_stage3]: 重试发送导航目标 (QR点)...
[competition_master_stage3.py-19] [INFO] [1782530510.758564681] [competition_master_stage3]: [DIAG] nav目标距离: 3.97m, robot=(-2.00,-0.02) → target=(0.41,-3.17)
[competition_master_stage3.py-19] [INFO] [1782530510.770655812] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-18] [INFO] [1782530510.779868233] [bt_navigator]: Creating bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530510.818702836] [bt_navigator]: Begin navigating from current location (-1.98, -0.01) to (0.41, -3.17)
[competition_master_stage3.py-19] [INFO] [1782530510.836286262] [competition_master_stage3]: 导航目标已接受，车辆出发...
[component_container_isolated-18] [INFO] [1782530510.909685425] [lifecycle_manager_navigation]: Server bt_navigator connected with bond.
[component_container_isolated-18] [INFO] [1782530510.909890383] [lifecycle_manager_navigation]: Activating waypoint_follower
[component_container_isolated-18] [INFO] [1782530510.911283384] [waypoint_follower]: Activating
[component_container_isolated-18] [INFO] [1782530510.911564425] [waypoint_follower]: Creating bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530511.049271954] [lifecycle_manager_navigation]: Server waypoint_follower connected with bond.
[component_container_isolated-18] [INFO] [1782530511.049571663] [lifecycle_manager_navigation]: Activating velocity_smoother
[component_container_isolated-18] [INFO] [1782530511.051812747] [velocity_smoother]: Activating
[component_container_isolated-18] [INFO] [1782530511.052330831] [velocity_smoother]: Creating bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530511.174824519] [lifecycle_manager_navigation]: Server velocity_smoother connected with bond.
[component_container_isolated-18] [INFO] [1782530511.175013186] [lifecycle_manager_navigation]: Managed nodes are active
[component_container_isolated-18] [INFO] [1782530511.175072894] [lifecycle_manager_navigation]: Creating bond timer...
[component_container_isolated-18] [WARN] [1782530511.443735575] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.6273 Hz
[component_container_isolated-18] [INFO] [1782530511.625784002] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-18] [WARN] [1782530511.627305669] [controller_server]: No goal checker was specified in parameter 'current_goal_checker'. Server will use only plugin loaded goal_checker . This warning will appear once.
[imu_madgwick_filter.py-4] [INFO] [1782530511.628686212] [imu_madgwick_filter]: [imu_madgwick ->] msgs=599 q_w=0.9969 angle=9.0deg beta=0.0330
[cmd_vel_mux.py-8] [INFO] [1782530511.686584742] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=-0.12
[velocity_pid.py-9] [INFO] [1782530511.712559547] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.18 err=100.0%
[imu_madgwick_filter.py-6] [INFO] [1782530511.744517730] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1423 q_w=0.9994 angle=4.1deg beta=0.0030
[competition_master_stage3.py-19] [INFO] [1782530512.468758689] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.00,-0.02) yaw=14deg cmd=(vx=0.50 wz=-1.59) elapsed=4.9s plan[30pts 4.1m] (-2.00,-0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=77C cpu=100% mem=19%
[component_container_isolated-18] Reallocing temp weights 1500 - 60
[component_container_isolated-18] [WARN] [1782530513.458383373] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2007 Hz
[component_container_isolated-18] [INFO] [1782530513.627714754] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782530513.707857088] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.01 -> current=-0.11 dt=0.0346s, resetting
[qr_decoder-12] [INFO] [1782530514.176157168] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=400 last_qr_frame=-1 gap=-1 frames rejects=0
[competition_master_stage3.py-19] [INFO] [1782530514.462367986] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.25,-0.47) yaw=-53deg cmd=(vx=0.50 wz=-0.23) elapsed=6.9s plan[26pts 3.6m] (-1.50,-0.15)→(0.40,-3.15) cpuFreq=1500MHz cpuT=77C cpu=85% mem=19%
[velocity_pid.py-9] [INFO] [1782530514.812955588] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.09 -> current=0.04 dt=0.0396s, resetting
[cmd_vel_mux.py-8] [INFO] [1782530514.823084552] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.16
[velocity_pid.py-9] [INFO] [1782530514.823535011] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.01 err=22.7%
[velocity_pid.py-9] [INFO] [1782530515.040369876] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0339s, resetting
[component_container_isolated-18] [WARN] [1782530515.434335711] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4192 Hz
[component_container_isolated-18] [INFO] [1782530515.627665481] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782530515.718032571] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.20
[velocity_pid.py-9] [INFO] [1782530515.841352012] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0307s, resetting
[velocity_pid.py-9] [INFO] [1782530515.851917601] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.06 corrected=0.31 err=208.3%
[competition_master_stage3.py-19] [INFO] [1782530516.478799230] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.95,-0.99) yaw=-57deg cmd=(vx=0.50 wz=-0.44) elapsed=9.0s plan[19pts 2.7m] (-1.00,-0.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=78C cpu=87% mem=19%
[velocity_pid.py-9] [INFO] [1782530516.875429277] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.37 corrected=0.32 err=26.8%
[component_container_isolated-18] [WARN] [1782530517.434240580] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4019 Hz
[component_container_isolated-18] [INFO] [1782530517.627923060] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1782530518.461215182] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.65,-1.60) yaw=-63deg cmd=(vx=0.50 wz=0.25) elapsed=10.9s plan[17pts 2.3m] (-0.80,-1.25)→(0.40,-3.15) cpuFreq=1500MHz cpuT=78C cpu=100% mem=19%
[velocity_pid.py-9] [INFO] [1782530518.707436650] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.02 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1782530518.726621785] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.08
[velocity_pid.py-9] [INFO] [1782530518.740376460] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.08 dt=0.0335s, resetting
[velocity_pid.py-9] [INFO] [1782530518.939860194] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0322s, resetting
[qr_decoder-12] [INFO] [1782530519.399605573] [qr_decoder_zbar]: [qr_decoder] QR DETECTED frame=471 symbols=1 (gap=-1 frames)
[qr_decoder-12] [INFO] [1782530519.399875781] [qr_decoder_zbar]: [QR] 1584 | 3D:(-0.517, +0.164, 1.686)m | px(191,238) D:1686mm
[qr_decoder-12] [INFO] [1782530519.400530948] [qr_decoder_zbar]: [QR] 1584 | robot_pos: (0.94, -2.53, yaw=-1.52)
[qr_decision-13] [INFO] [1782530519.409908412] [qr_decision]: [QR] 1584 CCW @ (x=0.94, y=-2.54, yaw=-1.52) → /qr_event
[competition_master_stage3.py-19] [INFO] [1782530519.410981162] [competition_master_stage3]: [QR检测] 内容: 1584
[competition_master_stage3.py-19] [INFO] [1782530519.417511749] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decoder_zbar
[competition_master_stage3.py-19] [INFO] [1782530519.421098751] [competition_master_stage3]: >>> QR 解码已关闭, 等待方向判断 (/qr_event)...
[competition_master_stage3.py-19] [INFO] [1782530519.424112753] [competition_master_stage3]: [QR检测] 取消当前导航目标, 等待BT完成 cancel/halt 清理...
[component_container_isolated-18] [WARN] [1782530519.433759342] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4199 Hz
[qr_decoder-12] [INFO] [1782530519.458027063] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[qr_decision-13] [INFO] [1782530519.461898857] [qr_decision]: [检查点] qr_decision 发布 /qr_event (由 task_manager 决定停车)
[competition_master_stage3.py-19] [INFO] [1782530519.481223076] [competition_master_stage3]: [QR事件] 方向: 逆时针 (通道巡航阶段使用)
[competition_master_stage3.py-19] [INFO] [1782530519.488516330] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decision
[component_container_isolated-18] [INFO] [1782530519.527660602] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-18] [INFO] [1782530519.527843977] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1782530519.530449728] [bt_navigator]: [navigate_to_pose] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1782530519.531523604] [bt_navigator]: Goal canceled
[competition_master_stage3.py-19] [INFO] [1782530519.551162365] [competition_master_stage3]: [结果回调] BT取消确认完成 (STATUS_CANCELED), 准备发送通道入口目标...
[competition_master_stage3.py-19] [INFO] [1782530519.562585663] [competition_master_stage3]: [状态机] NAV_TO_QR → BACKING_UP
[competition_master_stage3.py-19] [INFO] [1782530519.583443508] [competition_master_stage3]: >>> BT取消完成, 右后退摆正车头→前进进通道...
[competition_master_stage3.py-19] [INFO] [1782530519.602415601] [competition_master_stage3]: [BACKUP] 右后退中: vx=-0.15 wz=0.80, 持续 6.0s...
[cmd_vel_mux.py-8] [INFO] [1782530519.619737153] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.00
[qr_decision-13] Traceback (most recent call last):
[qr_decision-13]   File "/userdata/dev_ws/install/origincar_qr/lib/origincar_qr/qr_decision", line 33, in <module>
[qr_decision-13]     sys.exit(load_entry_point('origincar-qr==0.0.0', 'console_scripts', 'qr_decision')())
[qr_decision-13]   File "/userdata/dev_ws/install/origincar_qr/lib/python3.10/site-packages/origincar_qr/qr_decision.py", line 97, in main
[qr_decision-13]     rclpy.spin(node)
[qr_decision-13]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 229, in spin
[qr_decision-13]     executor.spin_once()
[qr_decision-13]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 808, in spin_once
[qr_decision-13]     self._spin_once_impl(timeout_sec)
[qr_decision-13]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 797, in _spin_once_impl
[qr_decision-13]     handler, entity, node = self.wait_for_ready_callbacks(timeout_sec=timeout_sec)
[qr_decision-13]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 780, in wait_for_ready_callbacks
[qr_decision-13]     return next(self._cb_iter)
[qr_decision-13]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 681, in _wait_for_ready_callbacks
[qr_decision-13]     raise ExternalShutdownException()
[qr_decision-13] rclpy.executors.ExternalShutdownException
[INFO] [qr_decoder-12]: process has finished cleanly [pid 32550]
[competition_master_stage3.py-19] [INFO] [1782530520.473797168] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.48,-1.89) yaw=-59deg cmd=(vx=0.00 wz=0.00) elapsed=12.9s plan[10pts 1.4m] (-0.40,-2.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=78C cpu=70% mem=19%
[cmd_vel_mux.py-8] [INFO] [1782530520.620814625] [cmd_vel_mux]: [mux→] src=nav vx=-0.15 wz=0.80
[velocity_pid.py-9] [INFO] [1782530520.640722970] [velocity_pid]: [vel_pid→] desired=-0.15 actual=-0.06 corrected=-0.41 err=61.3%
[ERROR] [qr_decision-13]: process has died [pid 32552, exit code 1, cmd '/userdata/dev_ws/install/origincar_qr/lib/origincar_qr/qr_decision --ros-args -r __node:=qr_decision --params-file /tmp/launch_params_jvlhp3pt'].
[imu_madgwick_filter.py-4] [INFO] [1782530521.627375814] [imu_madgwick_filter]: [imu_madgwick ->] msgs=796 q_w=0.8970 angle=52.5deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1782530521.744222504] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1852 q_w=0.8522 angle=63.1deg beta=0.0030
[competition_master_stage3.py-19] [INFO] [1782530522.461741201] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.49,-1.88) yaw=-42deg cmd=(vx=-0.15 wz=0.80) elapsed=14.9s plan[10pts 1.4m] (-0.40,-2.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=77C cpu=77% mem=18%
[competition_master_stage3.py-19] [INFO] [1782530524.462494258] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.76,-1.79) yaw=15deg cmd=(vx=-0.15 wz=0.80) elapsed=16.9s plan[10pts 1.4m] (-0.40,-2.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=77C cpu=75% mem=18%
[competition_master_stage3.py-19] [INFO] [1782530525.594143620] [competition_master_stage3]: [状态机] BACKING_UP → CRUISE_CHANNEL
[competition_master_stage3.py-19] [INFO] [1782530525.597760872] [competition_master_stage3]: [CRUISE] 方向: CCW (逆时针, even QR), 路点: (0.25,-1.17), (1.66,-1.50), (2.90,-0.90), (2.17,0.69)
[competition_master_stage3.py-19] [INFO] [1782530525.609752004] [competition_master_stage3]: [CRUISE] NavigateThroughPoses: (0.38,-1.10), (0.25,-1.17), (1.66,-1.50), (2.90,-0.90), (2.17,0.69)
[component_container_isolated-18] [INFO] [1782530525.613616215] [bt_navigator]: Begin navigating from current location through 5 poses to (2.17, 0.69)
[cmd_vel_mux.py-8] [INFO] [1782530525.621731969] [cmd_vel_mux]: [mux→] src=stop vx=0.00 wz=0.00
[competition_master_stage3.py-19] [INFO] [1782530525.631294600] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[cmd_vel_mux.py-8] [INFO] [1782530526.116320548] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.52s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1782530526.128154972] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[component_container_isolated-18] [WARN] [1782530526.457537455] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.1987 Hz
[competition_master_stage3.py-19] [INFO] [1782530526.462606458] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.91,-1.85) yaw=43deg cmd=(vx=0.00 wz=0.00) elapsed=18.9s plan[10pts 1.4m] (-0.40,-2.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=77C cpu=85% mem=18%
[component_container_isolated-18] [INFO] [1782530526.619001800] [controller_server]: Received a goal, begin computing control effort.
[cmd_vel_mux.py-8] [INFO] [1782530526.683491546] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=-0.12
[velocity_pid.py-9] [INFO] [1782530526.708319560] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.07 err=100.0%
[imu_madgwick_filter.py-4] [WARN] [1782530527.451522871] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1500s > 0.15s, capping
[velocity_pid.py-9] [INFO] [1782530527.710926524] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.39 corrected=0.16 err=22.8%
[velocity_pid.py-9] [INFO] [1782530528.039802634] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.11 -> current=0.01 dt=0.0336s, resetting
[component_container_isolated-18] [WARN] [1782530528.455202505] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3588 Hz
[competition_master_stage3.py-19] [INFO] [1782530528.466712304] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.82,-1.78) yaw=27deg cmd=(vx=0.50 wz=0.27) elapsed=20.9s plan[64pts 8.7m] (-1.00,-1.95)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=100% mem=18%
[component_container_isolated-18] [INFO] [1782530528.619329019] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782530529.810111562] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.03 -> current=-0.10 dt=0.0346s, resetting
[velocity_pid.py-9] [INFO] [1782530529.815525982] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.11 err=22.7%
[cmd_vel_mux.py-8] [INFO] [1782530529.819150151] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.22
[velocity_pid.py-9] [INFO] [1782530530.052411873] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0423s, resetting
[component_container_isolated-18] [WARN] [1782530530.454007073] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3989 Hz
[competition_master_stage3.py-19] [INFO] [1782530530.467376581] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.23,-1.23) yaw=22deg cmd=(vx=-0.30 wz=0.06) elapsed=22.9s plan[60pts 8.2m] (-0.60,-1.65)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=80% mem=18%
[component_container_isolated-18] [INFO] [1782530530.619318423] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782530530.717726815] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.19
[velocity_pid.py-9] [INFO] [1782530530.840889681] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0338s, resetting
[velocity_pid.py-9] [INFO] [1782530530.845959726] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.08 corrected=0.32 err=230.0%
[imu_madgwick_filter.py-4] [INFO] [1782530531.629104366] [imu_madgwick_filter]: [imu_madgwick ->] msgs=994 q_w=0.9795 angle=23.2deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1782530531.745425145] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2365 q_w=0.9993 angle=4.2deg beta=0.0030
[velocity_pid.py-9] [INFO] [1782530531.874084390] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.37 corrected=0.27 err=25.4%
[component_container_isolated-18] [WARN] [1782530532.444259112] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2166 Hz
[competition_master_stage3.py-19] [INFO] [1782530532.463049124] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.44,-1.17) yaw=11deg cmd=(vx=0.50 wz=0.66) elapsed=24.9s plan[54pts 7.3m] (0.20,-1.25)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=88% mem=18%
[cmd_vel_mux.py-8] [INFO] [1782530532.618979802] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.46
[component_container_isolated-18] [INFO] [1782530532.619322969] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782530532.840388812] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.08 -> current=-0.04 dt=0.0336s, resetting
[cmd_vel_mux.py-8] [INFO] [1782530533.719398602] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-1.25
[velocity_pid.py-9] [INFO] [1782530533.740344282] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.48 corrected=-0.08 err=51.2%
[velocity_pid.py-9] [INFO] [1782530533.939858779] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0318s, resetting
[velocity_pid.py-9] [INFO] [1782530534.243260842] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.12 -> current=0.00 dt=0.0342s, resetting
[component_container_isolated-18] [WARN] [1782530534.443073382] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3974 Hz
[competition_master_stage3.py-19] [INFO] [1782530534.462734061] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.32,-0.95) yaw=-38deg cmd=(vx=-0.30 wz=0.38) elapsed=26.9s plan[47pts 6.2m] (0.50,-1.15)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=100% mem=19%
[component_container_isolated-18] [INFO] [1782530534.619323616] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782530534.724992473] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.56
[velocity_pid.py-9] [INFO] [1782530534.740858483] [velocity_pid]: [vel_pid→] desired=-0.12 actual=-0.07 corrected=-0.07 err=40.8%
[velocity_pid.py-9] [INFO] [1782530534.839595169] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0337s, resetting
[velocity_pid.py-9] [INFO] [1782530535.776578503] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.31 corrected=0.32 err=38.6%
[component_container_isolated-18] [WARN] [1782530536.454211302] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3605 Hz
[competition_master_stage3.py-19] [INFO] [1782530536.466191976] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.45,-1.07) yaw=-53deg cmd=(vx=0.50 wz=-0.15) elapsed=28.9s plan[41pts 5.5m] (1.40,-0.95)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=88% mem=19%
[velocity_pid.py-9] [INFO] [1782530536.508689378] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.02 -> current=0.10 dt=0.0339s, resetting
[component_container_isolated-18] [INFO] [1782530536.619540364] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782530537.607198946] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.04 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1782530537.652108807] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.31
[velocity_pid.py-9] [INFO] [1782530537.840502426] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0343s, resetting
[component_container_isolated-18] [WARN] [1782530538.438876140] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4095 Hz
[competition_master_stage3.py-19] [INFO] [1782530538.461770905] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.04,-1.88) yaw=-34deg cmd=(vx=-0.30 wz=-0.43) elapsed=30.9s plan[40pts 5.3m] (1.50,-1.15)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=70% mem=19%
[velocity_pid.py-9] [INFO] [1782530538.613516668] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.07 corrected=-0.33 err=76.3%
[component_container_isolated-18] [INFO] [1782530538.619339755] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782530538.718988443] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.19
[velocity_pid.py-9] [INFO] [1782530538.845335774] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0347s, resetting
[velocity_pid.py-9] [INFO] [1782530539.648630080] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.20 corrected=0.44 err=59.6%
[component_container_isolated-18] [WARN] [1782530540.432420000] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1782530540.432686584] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.90, -0.90)
[component_container_isolated-18] [WARN] [1782530540.432792209] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[competition_master_stage3.py-19] [INFO] [1782530540.461902019] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.06,-1.88) yaw=-33deg cmd=(vx=0.45 wz=0.62) elapsed=32.9s plan[32pts 4.3m] (2.00,-1.85)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=82% mem=19%
[component_container_isolated-18] [INFO] [1782530540.620026288] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1782530540.637804300] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1782530540.645450263] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1782530540.645620721] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1782530540.654325352] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1782530540.660125481] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1782530540.662225940] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[cmd_vel_mux.py-8] [INFO] [1782530541.117144234] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.49
[velocity_pid.py-9] [INFO] [1782530541.141131875] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.45 corrected=0.00 err=40.9%
[velocity_pid.py-9] [INFO] [1782530541.339892504] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0332s, resetting
[velocity_pid.py-9] [INFO] [1782530541.342919798] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.11 -> current=-0.01 dt=0.0332s, resetting
[component_container_isolated-18] [WARN] [1782530541.447742491] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.8936 Hz
[component_container_isolated-18] [INFO] [1782530541.619674478] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-4] [INFO] [1782530541.630833526] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1190 q_w=0.9714 angle=27.5deg beta=0.0330
[cmd_vel_mux.py-8] [INFO] [1782530541.717128124] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.33
[imu_madgwick_filter.py-6] [INFO] [1782530541.744631934] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2858 q_w=0.9980 angle=7.2deg beta=0.0030
[velocity_pid.py-9] [INFO] [1782530541.840604496] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0320s, resetting
[velocity_pid.py-9] [INFO] [1782530542.141440025] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.01 corrected=0.37 err=98.5%
[competition_master_stage3.py-19] [INFO] [1782530542.475455577] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.76,-1.93) yaw=12deg cmd=(vx=0.48 wz=1.30) elapsed=35.0s plan[26pts 3.5m] (2.70,-1.95)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=50% mem=19%
[component_container_isolated-18] [WARN] [1782530543.439672501] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3907 Hz
[velocity_pid.py-9] [INFO] [1782530543.608153237] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.02 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1782530543.618592577] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.84
[component_container_isolated-18] [INFO] [1782530543.619343828] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782530544.317733580] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.22
[velocity_pid.py-9] [INFO] [1782530544.440769037] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.09 -> current=-0.03 dt=0.0341s, resetting
[competition_master_stage3.py-19] [INFO] [1782530544.467006554] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.16,-1.11) yaw=106deg cmd=(vx=0.23 wz=0.09) elapsed=36.9s plan[23pts 3.0m] (3.10,-1.65)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=90% mem=19%
[velocity_pid.py-9] [INFO] [1782530544.539539102] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0331s, resetting
[velocity_pid.py-9] [INFO] [1782530544.613866235] [velocity_pid]: [vel_pid→] desired=-0.11 actual=0.41 corrected=-0.46 err=452.2%
[component_container_isolated-18] [WARN] [1782530545.433997322] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4001 Hz
[component_container_isolated-18] [INFO] [1782530545.619333320] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782530545.642113586] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.18 corrected=-0.30 err=41.3%
[cmd_vel_mux.py-8] [INFO] [1782530545.718678595] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.34
[velocity_pid.py-9] [INFO] [1782530545.840094884] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0322s, resetting
[competition_master_stage3.py-19] [INFO] [1782530546.462464885] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.01,-0.83) yaw=117deg cmd=(vx=0.50 wz=-0.16) elapsed=38.9s plan[14pts 2.0m] (3.10,-0.85)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=77% mem=19%
[velocity_pid.py-9] [INFO] [1782530546.673171568] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.23 corrected=0.40 err=54.2%
[component_container_isolated-18] [WARN] [1782530547.433421288] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4003 Hz
[component_container_isolated-18] [INFO] [1782530547.619339580] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1782530548.462981569] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.83,-0.47) yaw=116deg cmd=(vx=0.50 wz=-0.10) elapsed=40.9s plan[12pts 1.6m] (3.00,-0.65)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=87% mem=19%
[velocity_pid.py-9] [INFO] [1782530548.808707637] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.51 corrected=0.04 err=24.4%
[cmd_vel_mux.py-8] [INFO] [1782530548.820772979] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.05
[imu_madgwick_filter.py-4] [WARN] [1782530549.002006352] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1500s > 0.15s, capping
[velocity_pid.py-9] [INFO] [1782530549.040930420] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0333s, resetting
[component_container_isolated-18] [WARN] [1782530549.432884771] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4009 Hz
[component_container_isolated-18] [INFO] [1782530549.619537649] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782530549.718595800] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.31
[velocity_pid.py-9] [INFO] [1782530549.841835634] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0325s, resetting
[velocity_pid.py-9] [INFO] [1782530549.851014432] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.08 corrected=0.33 err=230.0%
[competition_master_stage3.py-19] [INFO] [1782530550.462705186] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.46,0.05) yaw=123deg cmd=(vx=0.50 wz=0.07) elapsed=42.9s plan[6pts 0.6m] (2.50,0.15)→(2.20,0.65) cpuFreq=1500MHz cpuT=78C cpu=100% mem=19%
[velocity_pid.py-9] [INFO] [1782530550.873774927] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.36 corrected=0.31 err=28.2%
[component_container_isolated-18] [INFO] [1782530551.320046361] [controller_server]: Reached the goal!
[cmd_vel_mux.py-8] [INFO] [1782530551.419324638] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.46
[component_container_isolated-18] [WARN] [1782530551.438573276] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3979 Hz
[imu_madgwick_filter.py-4] [INFO] [1782530551.632607244] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1382 q_w=0.5054 angle=119.3deg beta=0.0330
[component_container_isolated-18] [INFO] [1782530551.718279511] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-19] [INFO] [1782530551.728901394] [competition_master_stage3]: [结果回调] 巡航完成, 触发VLM推理...
[competition_master_stage3.py-19] [INFO] [1782530551.732027813] [competition_master_stage3]: [VLM] 发布 sign4return=100, 拍照推理中...
[competition_master_stage3.py-19] [INFO] [1782530551.737897900] [competition_master_stage3]: [状态机] CRUISE_CHANNEL → RETURN_P
[vision_ai_node-14] [INFO] [1782530551.736722441] [vision_ai_node]: Received sign4return: 100
[vision_ai_node-14] [INFO] [1782530551.739985526] [vision_ai_node]: Received trigger signal (sign4return=100), subscribing to image topic...
[competition_master_stage3.py-19] [INFO] [1782530551.744606780] [competition_master_stage3]: [RETURN] NavigateThroughPoses: 通道入口→P点 (0.38,-1.10)→(-1.99,-0.01)
[imu_madgwick_filter.py-6] [INFO] [1782530551.746497698] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3352 q_w=0.7438 angle=83.9deg beta=0.0030
[component_container_isolated-18] [INFO] [1782530551.754002203] [bt_navigator]: Begin navigating from current location through 2 poses to (-1.99, -0.01)
[competition_master_stage3.py-19] [INFO] [1782530551.756796830] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[vision_ai_node-14] [INFO] [1782530551.783577640] [vision_ai_node]: Subscribed to /aurora/rgb/image_raw topic
[vision_ai_node-14] [INFO] [1782530551.951908298] [vision_ai_node]: Received compressed image, processing with AI model...
[component_container_isolated-18] [WARN] [1782530552.443442265] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4691 Hz
[competition_master_stage3.py-19] [INFO] [1782530552.466933282] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.09,0.59) yaw=103deg cmd=(vx=0.00 wz=0.00) elapsed=44.9s plan[4pts 0.3m] (2.30,0.35)→(2.20,0.65) cpuFreq=1500MHz cpuT=77C cpu=100% mem=19%
[component_container_isolated-18] [INFO] [1782530552.555979760] [controller_server]: Received a goal, begin computing control effort.
[velocity_pid.py-9] [INFO] [1782530552.649822951] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.03 corrected=0.22 err=65.3%
[component_container_isolated-18] [INFO] [1782530552.656347580] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782530552.684572683] [cmd_vel_mux]: [mux→] src=nav vx=0.15 wz=0.25
[component_container_isolated-18] [WARN] [1782530554.442974083] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2776 Hz
[competition_master_stage3.py-19] [INFO] [1782530554.467529392] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.88,1.10) yaw=139deg cmd=(vx=0.50 wz=1.05) elapsed=46.9s plan[48pts 6.6m] (2.10,0.75)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=85% mem=19%
[component_container_isolated-18] [INFO] [1782530554.556353121] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-4] [WARN] [1782530554.761043182] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1508s > 0.15s, capping
[velocity_pid.py-9] [INFO] [1782530555.744167462] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.03 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1782530555.785836908] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.69
[velocity_pid.py-9] [INFO] [1782530556.009612025] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0338s, resetting
[component_container_isolated-18] [WARN] [1782530556.442252125] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2834 Hz
[competition_master_stage3.py-19] [INFO] [1782530556.463282682] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.93,0.88) yaw=-125deg cmd=(vx=-0.30 wz=-0.81) elapsed=48.9s plan[44pts 6.1m] (1.80,1.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=87% mem=19%
[component_container_isolated-18] [INFO] [1782530556.556354957] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782530556.684610965] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.53
[velocity_pid.py-9] [INFO] [1782530556.806856427] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1782530556.810280305] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.08 corrected=0.32 err=230.0%
[velocity_pid.py-9] [INFO] [1782530556.940097939] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.03 -> current=0.09 dt=0.0325s, resetting
[velocity_pid.py-9] [INFO] [1782530557.842702586] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.34 corrected=0.34 err=32.0%
[component_container_isolated-18] [WARN] [1782530558.438132432] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2949 Hz
[competition_master_stage3.py-19] [INFO] [1782530558.463181700] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.80,0.57) yaw=-96deg cmd=(vx=0.50 wz=0.79) elapsed=50.9s plan[38pts 5.2m] (0.90,0.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=90% mem=19%
[component_container_isolated-18] [INFO] [1782530558.556358351] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782530559.542817232] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.03 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1782530559.583457470] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.25
[velocity_pid.py-9] [INFO] [1782530559.808554591] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0341s, resetting
[component_container_isolated-18] [WARN] [1782530560.439118634] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2801 Hz
[competition_master_stage3.py-19] [INFO] [1782530560.463225235] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.10,-0.14) yaw=-66deg cmd=(vx=-0.30 wz=0.02) elapsed=52.9s plan[37pts 4.9m] (0.80,0.55)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=90% mem=19%
[component_container_isolated-18] [INFO] [1782530560.556497428] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782530560.577136110] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.04 corrected=-0.35 err=87.0%
[velocity_pid.py-9] [INFO] [1782530560.641684241] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.03 -> current=-0.10 dt=0.0336s, resetting
[cmd_vel_mux.py-8] [INFO] [1782530560.683625730] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.22
[velocity_pid.py-9] [INFO] [1782530560.808350321] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1782530561.609511658] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.25 corrected=0.35 err=50.4%
[imu_madgwick_filter.py-4] [INFO] [1782530561.633774676] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1573 q_w=-0.8570 angle=298.0deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1782530561.744557299] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3835 q_w=-0.7169 angle=271.6deg beta=0.0030
[component_container_isolated-18] [WARN] [1782530562.438356977] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2820 Hz
[competition_master_stage3.py-19] [INFO] [1782530562.465355289] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.30,-0.60) yaw=-85deg cmd=(vx=0.50 wz=-1.44) elapsed=54.9s plan[33pts 4.4m] (1.20,-0.35)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=80% mem=19%
[component_container_isolated-18] [INFO] [1782530562.556347314] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782530562.683766950] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-1.32
[velocity_pid.py-9] [INFO] [1782530562.709707677] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.48 corrected=-0.00 err=49.1%
[velocity_pid.py-9] [INFO] [1782530562.911823160] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0385s, resetting
[imu_madgwick_filter.py-4] [WARN] [1782530563.051929430] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1501s > 0.15s, capping
[velocity_pid.py-9] [INFO] [1782530563.710615878] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.09 corrected=-0.32 err=71.7%
[component_container_isolated-18] [WARN] [1782530564.437563961] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2820 Hz
[competition_master_stage3.py-19] [INFO] [1782530564.461403937] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.23,-0.91) yaw=-134deg cmd=(vx=-0.30 wz=1.67) elapsed=56.9s plan[29pts 3.7m] (1.20,-0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=77C cpu=57% mem=19%
[component_container_isolated-18] [INFO] [1782530564.556354550] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782530564.618064971] [cmd_vel_mux]: [mux→] src=nav vx=-0.13 wz=1.54
[velocity_pid.py-9] [INFO] [1782530564.740820479] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.04 -> current=0.05 dt=0.0325s, resetting
[velocity_pid.py-9] [INFO] [1782530564.745659108] [velocity_pid]: [vel_pid→] desired=0.05 actual=-0.27 corrected=0.77 err=631.2%
[velocity_pid.py-9] [INFO] [1782530565.317547620] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.08 dt=0.0407s, resetting
[velocity_pid.py-9] [INFO] [1782530565.774374671] [velocity_pid]: [vel_pid→] desired=0.49 actual=0.32 corrected=0.37 err=35.0%
[component_container_isolated-18] [WARN] [1782530566.435367836] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2860 Hz
[competition_master_stage3.py-19] [INFO] [1782530566.463489399] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.24,-0.97) yaw=-126deg cmd=(vx=0.50 wz=-1.52) elapsed=58.9s plan[28pts 3.8m] (1.30,-0.85)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=88% mem=19%
[component_container_isolated-18] [INFO] [1782530566.556356969] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782530567.441533889] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.10 -> current=0.01 dt=0.0326s, resetting
[velocity_pid.py-9] [INFO] [1782530567.940653768] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.51 corrected=0.05 err=24.4%
[cmd_vel_mux.py-8] [INFO] [1782530567.984475051] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.29
[velocity_pid.py-9] [INFO] [1782530568.210722140] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0311s, resetting
[component_container_isolated-18] [WARN] [1782530568.433904311] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2948 Hz
[competition_master_stage3.py-19] [INFO] [1782530568.469508379] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.27,-1.06) yaw=174deg cmd=(vx=-0.30 wz=0.17) elapsed=60.9s plan[27pts 3.7m] (1.20,-1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=88% mem=19%
[component_container_isolated-18] [INFO] [1782530568.556354029] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782530568.639650718] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.03 -> current=-0.10 dt=0.0329s, resetting
[cmd_vel_mux.py-8] [INFO] [1782530568.683541418] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.22
[velocity_pid.py-9] [INFO] [1782530568.807722346] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0332s, resetting
[velocity_pid.py-9] [INFO] [1782530568.942038782] [velocity_pid]: [vel_pid→] desired=0.29 actual=-0.02 corrected=0.37 err=106.7%
[velocity_pid.py-9] [INFO] [1782530570.208182962] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.03 -> current=0.09 dt=0.0296s, resetting
[component_container_isolated-18] [WARN] [1782530570.436550638] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2845 Hz
[competition_master_stage3.py-19] [INFO] [1782530570.463065534] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.01,-1.00) yaw=147deg cmd=(vx=0.50 wz=0.47) elapsed=62.9s plan[21pts 2.8m] (0.30,-1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=100% mem=19%
[component_container_isolated-18] [INFO] [1782530570.556606898] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-4] [INFO] [1782530571.627790893] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1765 q_w=-0.0138 angle=181.6deg beta=0.0330
[velocity_pid.py-9] [INFO] [1782530571.741494856] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.01 err=22.7%
[imu_madgwick_filter.py-6] [INFO] [1782530571.755278325] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4315 q_w=0.3043 angle=144.6deg beta=0.0030
[cmd_vel_mux.py-8] [INFO] [1782530571.786837767] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.02
[velocity_pid.py-9] [INFO] [1782530572.007315396] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0335s, resetting
[component_container_isolated-18] [WARN] [1782530572.434072937] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2920 Hz
[competition_master_stage3.py-19] [INFO] [1782530572.469168131] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.96,-0.53) yaw=157deg cmd=(vx=-0.30 wz=0.01) elapsed=64.9s plan[17pts 2.4m] (-0.10,-0.85)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=88% mem=19%
[component_container_isolated-18] [INFO] [1782530572.556801324] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782530572.683619215] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.26
[velocity_pid.py-9] [INFO] [1782530572.807123728] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1782530572.811542315] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.10 corrected=0.37 err=263.3%
[velocity_pid.py-9] [INFO] [1782530573.842033538] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.36 corrected=0.33 err=28.2%
[component_container_isolated-18] [WARN] [1782530574.433801003] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2905 Hz
[competition_master_stage3.py-19] [INFO] [1782530574.470877824] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.17,-0.48) yaw=161deg cmd=(vx=0.50 wz=-0.29) elapsed=66.9s plan[11pts 1.4m] (-1.00,-0.55)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=80% mem=19%
[component_container_isolated-18] [INFO] [1782530574.556683184] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782530575.242761308] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.04 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1782530575.284528508] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.76
[component_container_isolated-18] [INFO] [1782530575.457532728] [controller_server]: Reached the goal!
[velocity_pid.py-9] [INFO] [1782530575.507896768] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0345s, resetting
[component_container_isolated-18] [ERROR] [1782530576.358525276] [bt_navigator_navigate_through_poses_rclcpp_node]: Failed to get result for compute_path_through_poses in node halt!
[component_container_isolated-18] [WARN] [1782530576.359737319] [BehaviorTreeEngine]: Behavior Tree tick rate 10.00 was exceeded!
[component_container_isolated-18] [INFO] [1782530576.360429028] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-19] [INFO] [1782530576.374573081] [competition_master_stage3]: [结果回调] 返航完成, 已回到P点!
[component_container_isolated-18] [WARN] [1782530576.432887961] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2905 Hz
[cmd_vel_mux.py-8] [INFO] [1782530576.983938066] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.52s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1782530576.988899778] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[competition_master_stage3.py-19] [INFO] [1782530577.096253989] [competition_master_stage3]: [BAG] 录制已停止
[competition_master_stage3.py-19] [INFO] [1782530577.100704326] [competition_master_stage3]: [状态机] RETURN_P → DONE
[competition_master_stage3.py-19] [INFO] [1782530577.103922537] [competition_master_stage3]:
[competition_master_stage3.py-19] [INFO] [1782530577.109396499] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1782530577.111861376] [competition_master_stage3]: >>> [Stage 3] 任务结束 <<<
[competition_master_stage3.py-19] [INFO] [1782530577.115026421] [competition_master_stage3]:   最终状态: DONE
[competition_master_stage3.py-19] [INFO] [1782530577.117552548] [competition_master_stage3]:   总耗时:   69.6s
[cmd_vel_mux.py-8] [INFO] [1782530577.117339422] [cmd_vel_mux]: [mux→] src=stop vx=0.00 wz=0.00
[competition_master_stage3.py-19] [INFO] [1782530577.120147591] [competition_master_stage3]:   --- 各阶段耗时 ---
[competition_master_stage3.py-19] [INFO] [1782530577.123107219] [competition_master_stage3]:   LAUNCH................ 15.0s
[competition_master_stage3.py-19] [INFO] [1782530577.125679804] [competition_master_stage3]:   NAV_TO_QR............. 12.1s
[competition_master_stage3.py-19] [INFO] [1782530577.128338223] [competition_master_stage3]:   BACKING_UP............ 6.0s
[competition_master_stage3.py-19] [INFO] [1782530577.130670558] [competition_master_stage3]:   CRUISE_CHANNEL........ 26.1s
[competition_master_stage3.py-19] [INFO] [1782530577.133062602] [competition_master_stage3]:   RETURN_P.............. 25.4s
[competition_master_stage3.py-19] [INFO] [1782530577.135812270] [competition_master_stage3]:   (transition/overhead). -15.0s
[competition_master_stage3.py-19] [INFO] [1782530577.139234648] [competition_master_stage3]:   --- ---
[competition_master_stage3.py-19] [INFO] [1782530577.141656108] [competition_master_stage3]:   QR 原始数据: 1584
[competition_master_stage3.py-19] [INFO] [1782530577.144028944] [competition_master_stage3]:   QR 方向:   逆时针 (CW=顺时针/odd, CCW=逆时针/even)
[competition_master_stage3.py-19] [WARN] [1782530577.150775907] [competition_master_stage3]:   VLM 结果:  未收到
[competition_master_stage3.py-19] [INFO] [1782530577.156809579] [competition_master_stage3]:   超时限制:  180.0s (全局)
[competition_master_stage3.py-19] [INFO] [1782530577.159981831] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1782530577.169526881] [competition_master_stage3]: [TRAJ] CSV已保存: /userdata/dev_ws/trajectory_20260627_112257.csv (100 点)
[competition_master_stage3.py-19] [INFO] [1782530577.175869719] [competition_master_stage3]: [TRAJ] 摘要JSON已保存: /userdata/dev_ws/trajectory_20260627_112257_summary.json
[competition_master_stage3.py-19] [INFO] [1782530577.179448347] [competition_master_stage3]: [TRAJ] 规划历史已保存: /userdata/dev_ws/trajectory_20260627_112257_plans.csv (30 次规划)
[competition_master_stage3.py-19] [INFO] [1782530577.199591238] [competition_master_stage3]: [TRAJ] costmap PGM已保存: /userdata/dev_ws/trajectory_20260627_112257_costmap.pgm
[competition_master_stage3.py-19] [INFO] [1782530577.260404162] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.79,-0.10) yaw=98deg cmd=(vx=0.00 wz=0.00) elapsed=69.7s plan[8pts 1.0m] (-1.30,-0.45)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=80% mem=18%
[competition_master_stage3.py-19] [INFO] [1782530578.464130918] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.79,-0.10) yaw=98deg cmd=(vx=0.00 wz=0.00) elapsed=70.9s plan[4pts 0.4m] (-1.80,-0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=78C cpu=85% mem=18%
^C[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[map_server-15] [INFO] [1782530580.201964487] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-15] [INFO] [1782530580.202271488] [keepout_mask_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_mask_server)
[map_server-15] [INFO] [1782530580.202535821] [keepout_mask_server]: Deactivating
[map_server-15] [INFO] [1782530580.202630613] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[ERROR] [lslidar_driver_node-2]: process has died [pid 32492, exit code -6, cmd '/userdata/dev_ws/install/lslidar_driver/lib/lslidar_driver/lslidar_driver_node --ros-args -r __node:=lslidar_driver_node --params-file /userdata/dev_ws/install/lslidar_driver/share/lslidar_driver/params/lsx10.yaml'].
[ERROR] [origincar_base_node-1]: process has died [pid 32490, exit code -6, cmd '/userdata/dev_ws/install/origincar_base/lib/origincar_base/origincar_base_node --ros-args --params-file /tmp/launch_params_i3dqj3om --params-file /tmp/launch_params_a32f9ve5'].
[INFO] [static_transform_publisher-10]: process has finished cleanly [pid 32546]
[INFO] [robot_state_publisher-3]: process has finished cleanly [pid 32494]
[INFO] [cmd_vel_mux.py-8]: process has finished cleanly [pid 32504]
[INFO] [ekf_node-7]: process has finished cleanly [pid 32502]
[INFO] [map_server-15]: process has finished cleanly [pid 32652]
[INFO] [imu_madgwick_filter.py-4]: process has finished cleanly [pid 32496]
[INFO] [imu_madgwick_filter.py-6]: process has finished cleanly [pid 32500]
[INFO] [costmap_filter_info_server-16]: process has finished cleanly [pid 32654]
[INFO] [lifecycle_manager-17]: process has finished cleanly [pid 32656]
[ERROR] [rviz2-20]: process has died [pid 32905, exit code -11, cmd '/opt/ros/humble/lib/rviz2/rviz2 -d /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/rviz/nav.rviz --ros-args -r __node:=rviz2'].
[INFO] [velocity_pid.py-9]: process has finished cleanly [pid 32510]
[component_container_isolated-18] [INFO] [1782530580.202005154] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-18] [INFO] [1782530580.202147904] [lifecycle_manager_navigation]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_navigation)
[component_container_isolated-18] [INFO] [1782530580.202424863] [lifecycle_manager_navigation]: Terminating bond timer...
[rviz2-20] [INFO] [1782530580.202020571] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[aurora930_node-11] [INFO] [1782530580.202096237] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-16] [INFO] [1782530580.203698197] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-16] [INFO] [1782530580.203989822] [keepout_filter_info_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_filter_info_server)
[costmap_filter_info_server-16] [INFO] [1782530580.204395656] [keepout_filter_info_server]: Deactivating
[costmap_filter_info_server-16] [INFO] [1782530580.204534406] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-16] [INFO] [1782530580.218312626] [keepout_filter_info_server]: Cleaning up
[costmap_filter_info_server-16] [INFO] [1782530580.218624001] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-16] [INFO] [1782530580.379640465] [keepout_filter_info_server]: Destroying
[static_transform_publisher-10] [INFO] [1782530580.203679530] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[competition_master_stage3.py-19] [INFO] [1782530580.350802358] [competition_master_stage3]: [MAIN] 收到 Ctrl+C, 停止录制 + 保存轨迹...
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.364783494] [competition_master_stage3]:
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.375511170] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.383016301] [competition_master_stage3]: >>> [Stage 3] 任务结束 <<<
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.409285281] [competition_master_stage3]:   最终状态: DONE
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.433349883] [competition_master_stage3]:   总耗时:   72.9s
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.436661469] [competition_master_stage3]:   --- 各阶段耗时 ---
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.439740680] [competition_master_stage3]:   LAUNCH................ 15.0s
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.443317850] [competition_master_stage3]:   NAV_TO_QR............. 12.1s
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.448200229] [competition_master_stage3]:   BACKING_UP............ 6.0s
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.452345899] [competition_master_stage3]:   CRUISE_CHANNEL........ 26.1s
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.476363252] [competition_master_stage3]:   RETURN_P.............. 25.4s
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.479475921] [competition_master_stage3]:   (transition/overhead). -11.8s
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.482329715] [competition_master_stage3]:   --- ---
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.492652515] [competition_master_stage3]:   QR 原始数据: 1584
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.496349685] [competition_master_stage3]:   QR 方向:   逆时针 (CW=顺时针/odd, CCW=逆时针/even)
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [WARN] [1782530580.515880492] [competition_master_stage3]:   VLM 结果:  未收到
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.524038124] [competition_master_stage3]:   超时限制:  180.0s (全局)
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.535061341] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.544630599] [competition_master_stage3]: [TRAJ] CSV已保存: /userdata/dev_ws/trajectory_20260627_112300.csv (100 点)
[ekf_node-7] [INFO] [1782530580.205266740] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[robot_state_publisher-3] [INFO] [1782530580.206609533] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-17] [INFO] [1782530580.210008827] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-17] [INFO] [1782530580.210364244] [lifecycle_manager_keepout]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_keepout)
[lifecycle_manager-17] [INFO] [1782530580.210711703] [lifecycle_manager_keepout]: Terminating bond timer...
[lifecycle_manager-17] [INFO] [1782530580.392476767] [lifecycle_manager_keepout]: Destroying lifecycle_manager_keepout
[origincar_base_node-1] [INFO] [1782530580.215872957] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1782530580.216383332] [origincar_base]: Stop command sent to STM32 on shutdown.
[origincar_base_node-1] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[origincar_base_node-1] terminate called after throwing an instance of 'rclcpp::exceptions::RCLError'
[origincar_base_node-1]   what():  failed to create guard condition: the given context is not valid, either rcl_init() was not called or rcl_shutdown() was called., at ./src/rcl/guard_condition.c:67
[aurora930_node-11] I0627 11:23:00.217175 32548 ros2_node.cc:90] process quit succeed
[aurora930_node-11] I0627 11:23:00.217396 32548 aurora900_ros2_device.cc:83] begin stop()
[aurora930_node-11] I0627 11:23:00.281184 32548 aurora900_ros2_device.cc:103] stop stream
[aurora930_node-11] 2026-06-27 11:23:00.311 (  99.977s) [        AF734020]      aurora900_impl.cc:648   INFO| ir_stream_count_=0, rgb_stream_count_=0, depth_stream_count_=0
[aurora930_node-11] 2026-06-27 11:23:00.311 (  99.977s) [        AF734020]      aurora900_impl.cc:649   INFO| mask=7
[aurora930_node-11] I0627 11:23:00.568264 32548 aurora900_ros2_device.cc:105] destroy stream
[aurora930_node-11] I0627 11:23:00.568508 32548 aurora900_ros2_device.cc:110] close glog
[aurora930_node-11] WARNING: Logging before InitGoogleLogging() is written to STDERR
[aurora930_node-11] I0627 11:23:00.568708 32548 ros2_device.cc:113] close device...
[aurora930_node-11] 2026-06-27 11:23:01.068 ( 100.734s) [        7BFF57E0]         cmd_backend.cc:40    INFO| RunBlocking is end!!!
[aurora930_node-11] 2026-06-27 11:23:01.269 ( 100.935s) [        AF734020]deptrum_camera_vendor.c:121   INFO| device is close.
[aurora930_node-11] I0627 11:23:01.271284 32548 ros2_device.cc:116] quit succeed
[vision_ai_node-14] [INFO] [1782530580.228750051] [vision_ai_node]: Unsubscribed from image topic
[vision_ai_node-14] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[vision_ai_node-14] Traceback (most recent call last):
[vision_ai_node-14]   File "/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node", line 33, in <module>
[vision_ai_node-14]     sys.exit(load_entry_point('racing-vision-ai==0.0.1', 'console_scripts', 'vision_ai_node')())
[vision_ai_node-14]   File "/userdata/dev_ws/install/racing_vision_ai/lib/python3.10/site-packages/racing_vision_ai/vision_ai_node.py", line 283, in main
[vision_ai_node-14]     rclpy.shutdown()
[vision_ai_node-14]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 130, in shutdown
[vision_ai_node-14]     _shutdown(context=context)
[vision_ai_node-14]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/utilities.py", line 58, in shutdown
[vision_ai_node-14]     return context.shutdown()
[vision_ai_node-14]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/context.py", line 102, in shutdown
[vision_ai_node-14]     self.__context.shutdown()
[vision_ai_node-14] rclpy._rclpy_pybind11.RCLError: failed to shutdown: rcl_shutdown already called on the given context, at ./src/rcl/init.c:241
[map_server-15] [INFO] [1782530580.233952888] [keepout_mask_server]: Cleaning up
[map_server-15] [INFO] [1782530580.257359282] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[map_server-15] [INFO] [1782530580.382170050] [keepout_mask_server]: Destroying
[component_container_isolated-18] [INFO] [1782530580.436924470] [local_costmap.local_costmap]: Message Filter dropping message: frame 'laser_link' at time 1782530580.135 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-18] [INFO] [1782530580.857692895] [velocity_smoother]: Running Nav2 LifecycleNode rcl preshutdown (velocity_smoother)
[component_container_isolated-18] [INFO] [1782530580.858109728] [velocity_smoother]: Deactivating
[component_container_isolated-18] [INFO] [1782530580.858304020] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530580.868841154] [velocity_smoother]: Cleaning up
[component_container_isolated-18] [INFO] [1782530580.869155446] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530580.869262321] [waypoint_follower]: Running Nav2 LifecycleNode rcl preshutdown (waypoint_follower)
[component_container_isolated-18] [INFO] [1782530580.869390237] [waypoint_follower]: Deactivating
[component_container_isolated-18] [INFO] [1782530580.869523238] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530580.879907163] [waypoint_follower]: Cleaning up
[component_container_isolated-18] [INFO] [1782530580.906506601] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530580.906787935] [lifecycle_manager_localization]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_localization)
[component_container_isolated-18] [INFO] [1782530580.906875060] [lifecycle_manager_localization]: Terminating bond timer...
[component_container_isolated-18] [INFO] [1782530580.989183335] [amcl]: Running Nav2 LifecycleNode rcl preshutdown (amcl)
[component_container_isolated-18] [INFO] [1782530580.989505085] [amcl]: Deactivating
[component_container_isolated-18] [INFO] [1782530580.989682002] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530581.000062510] [amcl]: Cleaning up
[component_container_isolated-18] [INFO] [1782530581.024019155] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530581.024206738] [bt_navigator]: Running Nav2 LifecycleNode rcl preshutdown (bt_navigator)
[component_container_isolated-18] [INFO] [1782530581.024556655] [bt_navigator]: Deactivating
[component_container_isolated-18] [INFO] [1782530581.024920947] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530581.035340331] [bt_navigator]: Cleaning up
[component_container_isolated-18] [INFO] [1782530581.428813818] [bt_navigator]: Completed Cleaning up
[component_container_isolated-18] [INFO] [1782530581.429060610] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530581.429131444] [map_server]: Running Nav2 LifecycleNode rcl preshutdown (map_server)
[component_container_isolated-18] [INFO] [1782530581.429244444] [map_server]: Deactivating
[component_container_isolated-18] [INFO] [1782530581.429393110] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530581.439765744] [map_server]: Cleaning up
[component_container_isolated-18] [INFO] [1782530581.439978494] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530581.440043369] [behavior_server]: Running Nav2 LifecycleNode rcl preshutdown (behavior_server)
[component_container_isolated-18] [INFO] [1782530581.440147119] [behavior_server]: Deactivating
[component_container_isolated-18] [INFO] [1782530581.440304744] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530581.450927086] [behavior_server]: Cleaning up
[component_container_isolated-18] [INFO] [1782530581.493022621] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530581.493188038] [planner_server]: Running Nav2 LifecycleNode rcl preshutdown (planner_server)
[component_container_isolated-18] [INFO] [1782530581.493318746] [planner_server]: Deactivating
[component_container_isolated-18] [INFO] [1782530581.493565538] [global_costmap.global_costmap]: Deactivating
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
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.550753395] [competition_master_stage3]: [TRAJ] 摘要JSON已保存: /userdata/dev_ws/trajectory_20260627_112300_summary.json
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.555626733] [competition_master_stage3]: [TRAJ] 规划历史已保存: /userdata/dev_ws/trajectory_20260627_112300_plans.csv (31 次规划)
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782530580.585824549] [competition_master_stage3]: [TRAJ] costmap PGM已保存: /userdata/dev_ws/trajectory_20260627_112300_costmap.pgm
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[ERROR] [bmi088_iio_bridge.py-5]: process has died [pid 32498, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/bmi088_iio_bridge.py --ros-args -r __node:=bmi088_iio_bridge --params-file /tmp/launch_params_8kzxn00q'].
[INFO] [competition_master_stage3.py-19]: process has finished cleanly [pid 32899]
[INFO] [aurora930_node-11]: process has finished cleanly [pid 32548]
[component_container_isolated-18] [INFO] [1782530582.425721008] [planner_server]: Deactivating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1782530582.426054842] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530582.436546642] [planner_server]: Cleaning up
[ERROR] [vision_ai_node-14]: process has died [pid 32554, exit code 1, cmd '/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node --ros-args -r __node:=vision_ai_node'].
[component_container_isolated-18] [INFO] [1782530582.456904659] [global_costmap.global_costmap]: Cleaning up
[component_container_isolated-18] [INFO] [1782530582.465751874] [planner_server]: Cleaning up plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1782530582.468540793] [planner_server]: Destroying plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1782530582.490400061] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530582.490548728] [smoother_server]: Running Nav2 LifecycleNode rcl preshutdown (smoother_server)
[component_container_isolated-18] [INFO] [1782530582.490675437] [smoother_server]: Deactivating
[component_container_isolated-18] [INFO] [1782530582.490740728] [smoother_server]: Deactivating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1782530582.490885020] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530582.501254862] [smoother_server]: Cleaning up
[component_container_isolated-18] [INFO] [1782530582.501385779] [smoother_server]: Cleaning up smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1782530582.515987124] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530582.516157874] [controller_server]: Running Nav2 LifecycleNode rcl preshutdown (controller_server)
[component_container_isolated-18] [INFO] [1782530582.516287791] [controller_server]: Deactivating
[component_container_isolated-18] [INFO] [1782530582.516356249] [controller_server]: Deactivating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1782530582.516560458] [local_costmap.local_costmap]: Deactivating
[component_container_isolated-18] [INFO] [1782530582.659615158] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782530582.670170584] [controller_server]: Cleaning up
[component_container_isolated-18] [INFO] [1782530582.670262125] [controller_server]: Cleaning up controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1782530582.670483751] [local_costmap.local_costmap]: Cleaning up
[component_container_isolated-18] [INFO] [1782530583.713796776] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[ERROR] [component_container_isolated-18]: process[component_container_isolated-18] failed to terminate '5' seconds after receiving 'SIGINT', escalating to 'SIGTERM'
[INFO] [component_container_isolated-18]: sending signal 'SIGTERM' to process[component_container_isolated-18]
[component_container_isolated-18] [INFO] [1782530586.963463476] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [component_container_isolated-18]: process[component_container_isolated-18] failed to terminate '10.0' seconds after receiving 'SIGTERM', escalating to 'SIGKILL'
[INFO] [component_container_isolated-18]: sending signal 'SIGKILL' to process[component_container_isolated-18]
[ERROR] [component_container_isolated-18]: process has died [pid 32897, exit code -9, cmd '/opt/ros/humble/lib/rclcpp_components/component_container_isolated --ros-args --log-level info --ros-args -r __node:=nav2_container --params-file /tmp/launch_params_eskcrcgx --params-file /tmp/launch_params_cwf_eclu -r /tf:=tf -r /tf_static:=tf_static'].
root@ubuntu:/userdata/dev_ws#
