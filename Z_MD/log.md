root@ubuntu:/userdata/dev_ws# ros2 launch origincar_bringup stage3_bringup.launch.py
[INFO] [launch]: All log files can be found below /root/.ros/log/2026-06-16-19-27-00-650450-ubuntu-12819
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [origincar_base_node-1]: process started with pid [12842]
[INFO] [lslidar_driver_node-2]: process started with pid [12844]
[INFO] [robot_state_publisher-3]: process started with pid [12846]
[INFO] [imu_madgwick_filter.py-4]: process started with pid [12848]
[INFO] [bmi088_iio_bridge.py-5]: process started with pid [12850]
[INFO] [imu_madgwick_filter.py-6]: process started with pid [12852]
[INFO] [ekf_node-7]: process started with pid [12854]
[INFO] [cmd_vel_mux.py-8]: process started with pid [12856]
[INFO] [velocity_pid.py-9]: process started with pid [12858]
[INFO] [static_transform_publisher-10]: process started with pid [12898]
[INFO] [aurora930_node-11]: process started with pid [12900]
[INFO] [qr_decoder-12]: process started with pid [12902]
[INFO] [qr_decision-13]: process started with pid [12904]
[INFO] [vision_ai_node-14]: process started with pid [12908]
[origincar_base_node-1] [INFO] [1781609221.459581803] [origincar_base]: origincar_base serial port opened
[lslidar_driver_node-2] [INFO] [1781609221.417117708] [lslidar_driver_node]: Lidar is N10
[lslidar_driver_node-2] [INFO] [1781609221.436747970] [lslidar_driver_node]: Initialised lslidar without error
[lslidar_driver_node-2] [INFO] [1781609221.437127177] [lslidar_driver_node]: Successfully initialize driver...
[robot_state_publisher-3] [INFO] [1781609221.397636321] [robot_state_publisher]: got segment base_footprint
[robot_state_publisher-3] [INFO] [1781609221.397982736] [robot_state_publisher]: got segment base_link
[robot_state_publisher-3] [INFO] [1781609221.398059194] [robot_state_publisher]: got segment gyro_link
[robot_state_publisher-3] [INFO] [1781609221.398107694] [robot_state_publisher]: got segment laser_link
[ekf_node-7] Both imu1_differential and imu1_relative were set to true. Using differential mode.
[static_transform_publisher-10] [INFO] [1781609221.695530735] [depth_camera_tf]: Spinning until stopped - publishing transform
[static_transform_publisher-10] translation: ('0.140000', '0.000000', '0.050000')
[static_transform_publisher-10] rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
[static_transform_publisher-10] from 'base_link' to 'depth_camera_link'
[aurora930_node-11] W0616 19:27:02.195291 12900 ros2_node.cc:35] hello aurora 900/930
[aurora930_node-11] 2026-06-16 19:27:02.380 (   0.356s) [        85BA4020] device_manager_impl.cc:89    INFO| hotplug has registed by user
[aurora930_node-11] I0616 19:27:02.451249 12900 aurora900_ros2_device.cc:153] BOOT_ORDER_1::Found 1 deptrum device
[aurora930_node-11] I0616 19:27:02.451879 12900 aurora900_ros2_device.cc:162] BOOT_ORDER_1::No serial number provided: picking first device
[aurora930_node-11] 2026-06-16 19:27:02.452 (   0.428s) [        85BA4020] device_manager_impl.cc:318   INFO| Device information:
[aurora930_node-11]     ir_pid:0x1930, rgb_pid:0x0
[aurora930_node-11]     serial number:HY400529001015314G00248
[aurora930_node-11] I0616 19:27:02.452247 12900 aurora900_ros2_device.cc:206] BOOT_ORDER_1::0:device start opening
[aurora930_node-11] 2026-06-16 19:27:02.454 (   0.431s) [        85BA4020]   custom_usb_device.cc:101   INFO| bulk in endpoint addr:129
[aurora930_node-11] 2026-06-16 19:27:02.454 (   0.431s) [        85BA4020]   custom_usb_device.cc:98    INFO| bulk out endpoint addr:2
[aurora930_node-11] 2026-06-16 19:27:02.478 (   0.454s) [        85BA4020]deptrum_camera_aurora93:53    INFO| doe_broken:0 ito_support:1 crash_count:0 wdt_count:0 hard_reset_count:2 heart_boot_count:0 boot_total:101 last_crash_time:N
[aurora930_node-11] I0616 19:27:02.478416 12900 aurora900_ros2_device.cc:247] device supported frame_mode:
[aurora930_node-11] I0616 19:27:02.478528 12900 aurora900_ros2_device.cc:252] [0]:ir_mode:=13 kRes320x200Ir8Bit rgb_mode:=31 kRes320x200RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0616 19:27:02.478575 12900 aurora900_ros2_device.cc:252] [1]:ir_mode:=17 kRes480x300Depth16Bit rgb_mode:=32 kRes480x300RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0616 19:27:02.478609 12900 aurora900_ros2_device.cc:252] [2]:ir_mode:=20 kRes640x400Ir8Bit rgb_mode:=33 kRes640x400RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0616 19:27:02.478641 12900 aurora900_ros2_device.cc:266] current set mode ir_mode:20:kRes640x400Ir8Bit,rgb_mode:33:kRes640x400RgbYuv
[aurora930_node-11] device_count==========1
[INFO] [map_server-15]: process started with pid [12989]
[INFO] [costmap_filter_info_server-16]: process started with pid [12993]
[INFO] [lifecycle_manager-17]: process started with pid [13004]
[qr_decoder-12] [INFO] [1781609222.489057779] [qr_decoder_zbar]: QR decoder (ZBar) started: rgb=/aurora/rgb/image_raw, depth=/aurora/depth/image_raw, filter=on, range=[50, 4000]mm, min_qr_len=1, intrinsics: fx=421.3 fy=422.3 cx=320.3 cy=197.0
[costmap_filter_info_server-16] [INFO] [1781609222.865114508] [costmap_filter_info_server]: This is costmap filter info publisher
[aurora930_node-11] I0616 19:27:02.940872 12900 aurora900_ros2_device.cc:387] Switch Auto Exposure
[costmap_filter_info_server-16] [INFO] [1781609222.968848259] [keepout_filter_info_server]:
[costmap_filter_info_server-16]         keepout_filter_info_server lifecycle node launched.
[costmap_filter_info_server-16]         Waiting on external lifecycle transitions to activate
[costmap_filter_info_server-16]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[lifecycle_manager-17] [INFO] [1781609222.990080099] [lifecycle_manager_keepout]: Creating
[aurora930_node-11] 2026-06-16 19:27:02.995 (   0.971s) [        85BA4020]      aurora900_impl.cc:1106  INFO| SetHeartbeat user set heartbeat enable: 0
[lifecycle_manager-17] [INFO] [1781609223.069501733] [lifecycle_manager_keepout]: Creating and initializing lifecycle service clients
[lifecycle_manager-17] [INFO] [1781609223.198176442] [lifecycle_manager_keepout]: Starting managed nodes bringup...
[lifecycle_manager-17] [INFO] [1781609223.198478357] [lifecycle_manager_keepout]: Configuring keepout_mask_server
[map_server-15] [INFO] [1781609223.209478318] [keepout_mask_server]:
[map_server-15]         keepout_mask_server lifecycle node launched.
[map_server-15]         Waiting on external lifecycle transitions to activate
[map_server-15]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[map_server-15] [INFO] [1781609223.210071941] [keepout_mask_server]: Creating
[map_server-15] [INFO] [1781609223.219396491] [keepout_mask_server]: Configuring
[map_server-15] [INFO] [1781609223.219678032] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.yaml
[map_server-15] [INFO] [1781609223.220798278] [map_io]: resolution: 0.05
[map_server-15] [INFO] [1781609223.220878736] [map_io]: origin[0]: -2.65
[map_server-15] [INFO] [1781609223.220912402] [map_io]: origin[1]: -4.5
[map_server-15] [INFO] [1781609223.220941611] [map_io]: origin[2]: 0
[map_server-15] [INFO] [1781609223.220971361] [map_io]: free_thresh: 0.5
[map_server-15] [INFO] [1781609223.221000027] [map_io]: occupied_thresh: 0.5
[map_server-15] [INFO] [1781609223.221034069] [map_io]: mode: scale
[map_server-15] [INFO] [1781609223.221064194] [map_io]: negate: 0
[map_server-15] [INFO] [1781609223.221739358] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm
[map_server-15] [INFO] [1781609223.246775435] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm: 163 X 141 map @ 0.05 m/cell
[lifecycle_manager-17] [INFO] [1781609223.313167783] [lifecycle_manager_keepout]: Configuring keepout_filter_info_server
[costmap_filter_info_server-16] [INFO] [1781609223.314495195] [keepout_filter_info_server]: Configuring
[lifecycle_manager-17] [INFO] [1781609223.340486144] [lifecycle_manager_keepout]: Activating keepout_mask_server
[map_server-15] [INFO] [1781609223.341484057] [keepout_mask_server]: Activating
[map_server-15] [INFO] [1781609223.341864806] [keepout_mask_server]: Creating bond (keepout_mask_server) to lifecycle manager.
[aurora930_node-11] I0616 19:27:03.408120 12900 aurora900_ros2_device.cc:304] BOOT_ORDER_1::Device information:
[aurora930_node-11] I0616 19:27:03.408922 12900 aurora900_ros2_device.cc:305]    sdk version: 1.1.22
[aurora930_node-11] I0616 19:27:03.409039 12900 aurora900_ros2_device.cc:306]    device name: Aurora 930
[aurora930_node-11] I0616 19:27:03.409070 12900 aurora900_ros2_device.cc:307]    serial number: HY400529001015314G00248
[aurora930_node-11] I0616 19:27:03.409097 12900 aurora900_ros2_device.cc:308]    firmware version: 1.7.2
[aurora930_node-11] I0616 19:27:03.409152 12900 camera_parameters.cc:134] BOOT_ORDER_1::Camera Parameters:
[aurora930_node-11] I0616 19:27:03.409183 12900 camera_parameters.cc:135] BOOT_ORDER_1::         Ir Intrinsics:
[aurora930_node-11] I0616 19:27:03.409210 12900 camera_parameters.cc:146]                Resolution:
[aurora930_node-11] I0616 19:27:03.409236 12900 camera_parameters.cc:147]                        Rows:400
[aurora930_node-11] I0616 19:27:03.409271 12900 camera_parameters.cc:148]                        Cols:640
[aurora930_node-11] I0616 19:27:03.409297 12900 camera_parameters.cc:149]                Intrinsics:
[aurora930_node-11] I0616 19:27:03.409322 12900 camera_parameters.cc:150]                        fx: 421.307
[aurora930_node-11] I0616 19:27:03.409440 12900 camera_parameters.cc:151]                        fy: 422.254
[aurora930_node-11] I0616 19:27:03.410291 12900 camera_parameters.cc:152]                        cx: 320.27
[aurora930_node-11] I0616 19:27:03.410420 12900 camera_parameters.cc:153]                        cy: 197.01
[aurora930_node-11] I0616 19:27:03.410465 12900 camera_parameters.cc:154]                        k1: 0.0606853
[aurora930_node-11] I0616 19:27:03.410504 12900 camera_parameters.cc:155]                        k2: -0.10961
[aurora930_node-11] I0616 19:27:03.410537 12900 camera_parameters.cc:156]                        p1: 0.00126689
[aurora930_node-11] I0616 19:27:03.411142 12900 camera_parameters.cc:157]                        p2: -0.00120539
[aurora930_node-11] I0616 19:27:03.411211 12900 camera_parameters.cc:158]                        k3: 0.0522281
[aurora930_node-11] I0616 19:27:03.411244 12900 camera_parameters.cc:138] BOOT_ORDER_1::         Rgb Intrinsics:
[aurora930_node-11] I0616 19:27:03.411278 12900 camera_parameters.cc:146]                Resolution:
[aurora930_node-11] I0616 19:27:03.411304 12900 camera_parameters.cc:147]                        Rows:400
[aurora930_node-11] I0616 19:27:03.411329 12900 camera_parameters.cc:148]                        Cols:640
[aurora930_node-11] I0616 19:27:03.411360 12900 camera_parameters.cc:149]                Intrinsics:
[aurora930_node-11] I0616 19:27:03.411386 12900 camera_parameters.cc:150]                        fx: 416.49
[aurora930_node-11] I0616 19:27:03.411422 12900 camera_parameters.cc:151]                        fy: 417.383
[aurora930_node-11] I0616 19:27:03.411459 12900 camera_parameters.cc:152]                        cx: 316.832
[aurora930_node-11] I0616 19:27:03.411491 12900 camera_parameters.cc:153]                        cy: 188.753
[aurora930_node-11] I0616 19:27:03.411528 12900 camera_parameters.cc:154]                        k1: 0.00611878
[aurora930_node-11] I0616 19:27:03.411561 12900 camera_parameters.cc:155]                        k2: -0.0490436
[aurora930_node-11] I0616 19:27:03.411592 12900 camera_parameters.cc:156]                        p1: 0.000399548
[aurora930_node-11] I0616 19:27:03.411629 12900 camera_parameters.cc:157]                        p2: 0.000563892
[aurora930_node-11] I0616 19:27:03.411660 12900 camera_parameters.cc:158]                        k3: 0.0308458
[aurora930_node-11] I0616 19:27:03.411729 12900 camera_parameters.cc:141] BOOT_ORDER_1::         Ir to Rgb Extrinsic:
[aurora930_node-11] I0616 19:27:03.411759 12900 camera_parameters.cc:162]                Extrinsics:
[aurora930_node-11] I0616 19:27:03.411801 12900 camera_parameters.cc:163]                        Rotation[0]: 0.999973, 0.00724076, -0.00112023
[aurora930_node-11] I0616 19:27:03.411839 12900 camera_parameters.cc:165]                        Rotation[1]: -0.00724006, 0.999973, 0.000633162
[aurora930_node-11] I0616 19:27:03.411875 12900 camera_parameters.cc:167]                        Rotation[2]: 0.00112478, -0.000625033, 0.999999
[aurora930_node-11] I0616 19:27:03.411969 12900 camera_parameters.cc:169]                        Translation: -9.88662, 0.117748, 0.603513
[aurora930_node-11] 2026-06-16 19:27:03.412 (   1.389s) [        85BA4020]      aurora900_impl.cc:578   INFO| stream_mask_:0, rgb_stream_count_:1
[bmi088_iio_bridge.py-5] [INFO] [1781609223.410213937] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1781609223.415305586] [bmi088_iio_bridge]:   DIAGNOSTIC: Scanning IIO devices under /sys/bus/iio/devices/
[bmi088_iio_bridge.py-5] [INFO] [1781609223.419397905] [bmi088_iio_bridge]:   Equivalent to: ls /sys/bus/iio/devices/*/name
[bmi088_iio_bridge.py-5] [INFO] [1781609223.430889239] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1781609223.437414924] [bmi088_iio_bridge]:   iio:device0/name = "34190000.adc"
[bmi088_iio_bridge.py-5] [INFO] [1781609223.441248327] [bmi088_iio_bridge]:   iio:device1/name = "bmi08x"
[bmi088_iio_bridge.py-5] [INFO] [1781609223.445171480] [bmi088_iio_bridge]:   trigger0/name = "34190000.adc-dev0"
[bmi088_iio_bridge.py-5] [INFO] [1781609223.449668172] [bmi088_iio_bridge]:   Total IIO devices found: 3
[bmi088_iio_bridge.py-5] [INFO] [1781609223.454022157] [bmi088_iio_bridge]:   BMI088 kernel module APPEARS LOADED: 1 BMI device(s) detected
[bmi088_iio_bridge.py-5] [INFO] [1781609223.461174381] [bmi088_iio_bridge]:   BMI device names: ['bmi08x']
[lifecycle_manager-17] [INFO] [1781609223.453207284] [lifecycle_manager_keepout]: Server keepout_mask_server connected with bond.
[lifecycle_manager-17] [INFO] [1781609223.453361617] [lifecycle_manager_keepout]: Activating keepout_filter_info_server
[costmap_filter_info_server-16] [INFO] [1781609223.454253531] [keepout_filter_info_server]: Activating
[costmap_filter_info_server-16] [INFO] [1781609223.455086444] [keepout_filter_info_server]: Creating bond (keepout_filter_info_server) to lifecycle manager.
[bmi088_iio_bridge.py-5] [INFO] [1781609223.469364894] [bmi088_iio_bridge]:   gyro:  /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_anglvel is_si=False scale_override=0.00053
[bmi088_iio_bridge.py-5] [INFO] [1781609223.473649920] [bmi088_iio_bridge]:   accel: /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_accel is_si=False scale_override=0.00341
[velocity_pid.py-9] [INFO] [1781609223.552452890] [velocity_pid]: VelocityPID 就绪: vx(Kp=0.8, Ki=0.60, Kd=0.05, max_i=0.68) wz(Kp=1.0, Ki=0.40, Kd=0.02, max_i=2.24) | feedback_timeout=0.5s
[lifecycle_manager-17] [INFO] [1781609223.565548593] [lifecycle_manager_keepout]: Server keepout_filter_info_server connected with bond.
[lifecycle_manager-17] [INFO] [1781609223.565727467] [lifecycle_manager_keepout]: Managed nodes are active
[lifecycle_manager-17] [INFO] [1781609223.565800342] [lifecycle_manager_keepout]: Creating bond timer...
[cmd_vel_mux.py-8] [INFO] [1781609223.603853623] [cmd_vel_mux]:   nav: /nav_cmd_vel priority=10 timeout=0.5s
[cmd_vel_mux.py-8] [INFO] [1781609223.619084944] [cmd_vel_mux]:   pid: /pid_cmd_vel priority=20 timeout=0.3s
[cmd_vel_mux.py-8] [INFO] [1781609223.636741381] [cmd_vel_mux]:   stop: /stop_cmd_vel priority=255 timeout=0.5s
[bmi088_iio_bridge.py-5] [INFO] [1781609223.650609207] [bmi088_iio_bridge]: BMI088 IIO Bridge 启动 @ 100Hz -> /imu_data  [OK]
[cmd_vel_mux.py-8] [INFO] [1781609223.660517380] [cmd_vel_mux]: cmd_vel_mux 就绪: 输出 → /cmd_vel_muxed
[velocity_pid.py-9] [INFO] [1781609223.693244097] [velocity_pid]: [vel_pid] ACTIVATED vx=0.00 wz=0.00
[cmd_vel_mux.py-8] [INFO] [1781609223.699231868] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[aurora930_node-11] 2026-06-16 19:27:03.744 (   1.721s) [        660D47E0]deptrum_camera_aurora93:407    ERR| recv first frame time is 1781609223744
[imu_madgwick_filter.py-6] [INFO] [1781609223.849779999] [imu_madgwick_bmi088]: [imu_madgwick] init: beta=0.0030, gyro_noise=0.0002, accel_noise=0.010
[imu_madgwick_filter.py-6] [INFO] [1781609223.857008056] [imu_madgwick_bmi088]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-6] [INFO] [1781609223.860733668] [imu_madgwick_bmi088]: [imu_madgwick] accel init: roll=-2.2deg, pitch=-3.2deg
[imu_madgwick_filter.py-4] [INFO] [1781609223.878327064] [imu_madgwick_filter]: [imu_madgwick] init: beta=0.0330, gyro_noise=0.0010, accel_noise=0.050
[imu_madgwick_filter.py-4] [INFO] [1781609223.884074293] [imu_madgwick_filter]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-4] [INFO] [1781609223.888628610] [imu_madgwick_filter]: [imu_madgwick] accel init: roll=0.1deg, pitch=0.2deg
[qr_decision-13] [INFO] [1781609223.889849981] [qr_decision]: qr_decision started: cooldown=3.0s, awaiting /sign from qr_decoder
[INFO] [component_container_isolated-18]: process started with pid [13189]
[lslidar_driver_node-2] port = /dev/ttyACM1, baud_rate = 230400
[lslidar_driver_node-2] open_port /dev/ttyACM1 OK !
[vision_ai_node-14] [INFO] [1781609228.015148125] [vision_ai_node]: 成功加载配置文件: /userdata/dev_ws/install/racing_vision_ai/share/racing_vision_ai/config/vision_ai_config.yaml
[vision_ai_node-14] [INFO] [1781609228.438672170] [vision_ai_node]: Volcengine Ark client initialized successfully
[vision_ai_node-14] [INFO] [1781609228.459606516] [vision_ai_node]: Vision AI Node initialized
[vision_ai_node-14] [INFO] [1781609228.462404215] [vision_ai_node]: Waiting for sign4return=100 signal...
[vision_ai_node-14] [INFO] [1781609228.464968707] [vision_ai_node]: Results will be published to vlm_result
[bmi088_iio_bridge.py-5] [INFO] [1781609229.107959857] [bmi088_iio_bridge]:   gyro bias calibrated: (0.002783, 0.001256, -0.002764) rad/s
[INFO] [competition_master_stage3.py-19]: process started with pid [13191]
[INFO] [rviz2-20]: process started with pid [13195]
[component_container_isolated-18] [INFO] [1781609229.760075542] [nav2_container]: Load Library: /opt/ros/humble/lib/libcontroller_server_core.so
[component_container_isolated-18] [INFO] [1781609229.789945069] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-18] [INFO] [1781609229.790818733] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-18] [INFO] [1781609229.886156294] [controller_server]:
[component_container_isolated-18]       controller_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781609229.913968411] [controller_server]: Creating controller server
[component_container_isolated-18] [INFO] [1781609230.008508974] [local_costmap.local_costmap]:
[component_container_isolated-18]       local_costmap lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781609230.011472048] [local_costmap.local_costmap]: Creating Costmap
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/controller_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781609230.036732383] [nav2_container]: Load Library: /opt/ros/humble/lib/libmap_server_core.so
[component_container_isolated-18] [INFO] [1781609230.086862928] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::CostmapFilterInfoServer>
[component_container_isolated-18] [INFO] [1781609230.087063427] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapSaver>
[component_container_isolated-18] [INFO] [1781609230.087120010] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-18] [INFO] [1781609230.087170344] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-18] [INFO] [1781609230.151919425] [map_server]:
[component_container_isolated-18]       map_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/map_server' in container '/nav2_container'
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781609230.153240337] [map_server]: Creating
[component_container_isolated-18] [INFO] [1781609230.157790489] [nav2_container]: Load Library: /opt/ros/humble/lib/libsmoother_server_core.so
[component_container_isolated-18] [INFO] [1781609230.163865094] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-18] [INFO] [1781609230.164053344] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-18] [INFO] [1781609230.237719521] [smoother_server]:
[component_container_isolated-18]       smoother_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781609230.247915904] [smoother_server]: Creating smoother server
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/smoother_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781609230.256477085] [nav2_container]: Load Library: /opt/ros/humble/lib/libamcl_core.so
[component_container_isolated-18] [INFO] [1781609230.266974593] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-18] [INFO] [1781609230.267145300] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-18] [INFO] [1781609230.391069272] [amcl]:
[component_container_isolated-18]       amcl lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781609230.393157807] [amcl]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/amcl' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781609230.462172833] [nav2_container]: Load Library: /opt/ros/humble/lib/libplanner_server_core.so
[component_container_isolated-18] [INFO] [1781609230.466335194] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-18] [INFO] [1781609230.466501569] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-18] [INFO] [1781609230.544116650] [planner_server]:
[component_container_isolated-18]       planner_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781609230.553356120] [planner_server]: Creating
[component_container_isolated-18] [INFO] [1781609230.638395094] [global_costmap.global_costmap]:
[component_container_isolated-18]       global_costmap lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781609230.640764711] [global_costmap.global_costmap]: Creating Costmap
[component_container_isolated-18] [INFO] [1781609230.678918087] [nav2_container]: Load Library: /opt/ros/humble/lib/libnav2_lifecycle_manager_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/planner_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781609230.683922904] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781609230.684100903] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781609230.748141653] [lifecycle_manager_localization]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_localization' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781609230.770023332] [lifecycle_manager_localization]: Creating and initializing lifecycle service clients
[component_container_isolated-18] [INFO] [1781609230.770885371] [nav2_container]: Load Library: /opt/ros/humble/lib/libbehavior_server_core.so
[component_container_isolated-18] [INFO] [1781609230.795832415] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-18] [INFO] [1781609230.796051789] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-18] [INFO] [1781609230.809580995] [lifecycle_manager_localization]: Starting managed nodes bringup...
[component_container_isolated-18] [INFO] [1781609230.812804110] [lifecycle_manager_localization]: Configuring map_server
[component_container_isolated-18] [INFO] [1781609230.813750524] [map_server]: Configuring
[component_container_isolated-18] [INFO] [1781609230.814050148] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.yaml
[component_container_isolated-18] [INFO] [1781609230.815213935] [map_io]: resolution: 0.05
[component_container_isolated-18] [INFO] [1781609230.815318060] [map_io]: origin[0]: -2.65
[component_container_isolated-18] [INFO] [1781609230.815353810] [map_io]: origin[1]: -4.5
[component_container_isolated-18] [INFO] [1781609230.815381393] [map_io]: origin[2]: 0
[component_container_isolated-18] [INFO] [1781609230.815410226] [map_io]: free_thresh: 0.25
[component_container_isolated-18] [INFO] [1781609230.815438101] [map_io]: occupied_thresh: 0.65
[component_container_isolated-18] [INFO] [1781609230.815486976] [map_io]: mode: trinary
[component_container_isolated-18] [INFO] [1781609230.815518184] [map_io]: negate: 0
[component_container_isolated-18] [INFO] [1781609230.816290724] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm
[component_container_isolated-18] [INFO] [1781609230.852764438] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm: 163 X 141 map @ 0.05 m/cell
[component_container_isolated-18] [INFO] [1781609230.881165513] [lifecycle_manager_localization]: Configuring amcl
[component_container_isolated-18] [INFO] [1781609230.882034218] [amcl]: Configuring
[component_container_isolated-18] [INFO] [1781609230.882497842] [amcl]: initTransforms
[component_container_isolated-18] [INFO] [1781609230.903648690] [behavior_server]:
[component_container_isolated-18]       behavior_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/behavior_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781609230.946370884] [nav2_container]: Load Library: /opt/ros/humble/lib/libbt_navigator_core.so
[component_container_isolated-18] [INFO] [1781609230.956627976] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-18] [INFO] [1781609230.956843225] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-18] [INFO] [1781609230.969787516] [amcl]: initPubSub
[component_container_isolated-18] [INFO] [1781609231.006232648] [amcl]: Subscribed to map topic.
[component_container_isolated-18] [INFO] [1781609231.050405256] [lifecycle_manager_localization]: Activating map_server
[component_container_isolated-18] [INFO] [1781609231.051532003] [map_server]: Activating
[component_container_isolated-18] [INFO] [1781609231.051976043] [map_server]: Creating bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609231.053705121] [amcl]: Received a 163 X 141 map @ 0.050 m/pix
[component_container_isolated-18] [INFO] [1781609231.097778188] [bt_navigator]:
[component_container_isolated-18]       bt_navigator lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/bt_navigator' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781609231.098843518] [bt_navigator]: Creating
[component_container_isolated-18] [INFO] [1781609231.118723162] [nav2_container]: Load Library: /opt/ros/humble/lib/libwaypoint_follower_core.so
[component_container_isolated-18] [INFO] [1781609231.124044270] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-18] [INFO] [1781609231.124240686] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-18] [INFO] [1781609231.175264981] [lifecycle_manager_localization]: Server map_server connected with bond.
[component_container_isolated-18] [INFO] [1781609231.175535063] [lifecycle_manager_localization]: Activating amcl
[component_container_isolated-18] [INFO] [1781609231.176761768] [amcl]: Activating
[component_container_isolated-18] [INFO] [1781609231.177277183] [amcl]: initialPoseReceived
[component_container_isolated-18] [INFO] [1781609231.178986177] [amcl]: Setting pose (1781609231.178979): -1.985 -0.014 0.262
[component_container_isolated-18] [INFO] [1781609231.181590544] [amcl]: Creating bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609231.234808498] [waypoint_follower]:
[component_container_isolated-18]       waypoint_follower lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/waypoint_follower' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781609231.236166827] [amcl]: createLaserObject
[component_container_isolated-18] [INFO] [1781609231.237991988] [waypoint_follower]: Creating
[component_container_isolated-18] [INFO] [1781609231.259106629] [nav2_container]: Load Library: /opt/ros/humble/lib/libvelocity_smoother_core.so
[component_container_isolated-18] [INFO] [1781609231.263365073] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-18] [INFO] [1781609231.263648322] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-18] [INFO] [1781609231.304807440] [lifecycle_manager_localization]: Server amcl connected with bond.
[component_container_isolated-18] [INFO] [1781609231.305008148] [lifecycle_manager_localization]: Managed nodes are active
[component_container_isolated-18] [INFO] [1781609231.305137773] [lifecycle_manager_localization]: Creating bond timer...
[component_container_isolated-18] [INFO] [1781609231.373437679] [velocity_smoother]:
[component_container_isolated-18]       velocity_smoother lifecycle node launched.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/velocity_smoother' in container '/nav2_container'
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781609231.390268708] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781609231.390633373] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781609231.502909430] [lifecycle_manager_navigation]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_navigation' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781609231.535383659] [lifecycle_manager_navigation]: Creating and initializing lifecycle service clients
[component_container_isolated-18] [INFO] [1781609231.642462482] [lifecycle_manager_navigation]: Starting managed nodes bringup...
[component_container_isolated-18] [INFO] [1781609231.642663148] [lifecycle_manager_navigation]: Configuring controller_server
[component_container_isolated-18] [INFO] [1781609231.643402979] [controller_server]: Configuring controller interface
[component_container_isolated-18] [INFO] [1781609231.644423101] [controller_server]: getting goal checker plugins..
[component_container_isolated-18] [INFO] [1781609231.645579806] [controller_server]: Controller frequency set to 10.0000Hz
[component_container_isolated-18] [INFO] [1781609231.645887346] [local_costmap.local_costmap]: Configuring
[component_container_isolated-18] [INFO] [1781609231.684790138] [local_costmap.local_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781609231.711602761] [local_costmap.local_costmap]: Subscribed to Topics: scan aurora_points
[component_container_isolated-18] [INFO] [1781609231.828776968] [local_costmap.local_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781609231.829070717] [local_costmap.local_costmap]: Using plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781609231.856321213] [local_costmap.local_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781609231.856687212] [local_costmap.local_costmap]: Using plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781609231.873022826] [local_costmap.local_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781609231.942585145] [controller_server]: Created progress_checker : progress_checker of type nav2_controller::SimpleProgressChecker
[component_container_isolated-18] [INFO] [1781609231.952622571] [controller_server]: Created goal checker : goal_checker of type nav2_controller::SimpleGoalChecker
[component_container_isolated-18] [INFO] [1781609231.963432203] [controller_server]: Controller Server has goal_checker  goal checkers available.
[component_container_isolated-18] [INFO] [1781609231.967352315] [controller_server]: Created controller : FollowPath of type nav2_regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781609232.114727764] [controller_server]: Controller Server has FollowPath  controllers available.
[component_container_isolated-18] [INFO] [1781609232.173965868] [lifecycle_manager_navigation]: Configuring smoother_server
[component_container_isolated-18] [INFO] [1781609232.174931949] [smoother_server]: Configuring smoother server
[component_container_isolated-18] [INFO] [1781609232.242686901] [smoother_server]: Created smoother : SmoothPath of type nav2_constrained_smoother/ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781609232.297578727] [smoother_server]: Smoother Server has SmoothPath  smoothers available.
[competition_master_stage3.py-19] [INFO] [1781609232.308099027] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1781609232.312206348] [competition_master_stage3]: === [Stage 3] 总控节点初始化 ===
[competition_master_stage3.py-19] [INFO] [1781609232.316148085] [competition_master_stage3]:   QR点:    (0.41, -3.17, yaw=0.00)
[competition_master_stage3.py-19] [INFO] [1781609232.320535988] [competition_master_stage3]:   通道入口: (0.38, -1.10, yaw=0.00)
[competition_master_stage3.py-19] [INFO] [1781609232.325125265] [competition_master_stage3]:   P点:     (-1.99, -0.01, yaw=0.26)
[competition_master_stage3.py-19] [INFO] [1781609232.329567876] [competition_master_stage3]:   cruise_cw: 3 路点 → VLM=(3.12, -1.34)
[competition_master_stage3.py-19] [INFO] [1781609232.334392152] [competition_master_stage3]:   cruise_ccw: 3 路点 → VLM=(2.10, 0.92)
[competition_master_stage3.py-19] [INFO] [1781609232.338254640] [competition_master_stage3]:   超时: total=180.0s QR=90.0s entry=60.0s cruise=180.0s vlm=30.0s return=120.0s
[component_container_isolated-18] [INFO] [1781609232.334537194] [lifecycle_manager_navigation]: Configuring planner_server
[component_container_isolated-18] [INFO] [1781609232.335463232] [planner_server]: Configuring
[component_container_isolated-18] [INFO] [1781609232.335746648] [global_costmap.global_costmap]: Configuring
[competition_master_stage3.py-19] [INFO] [1781609232.342228544] [competition_master_stage3]:   回退QR方向: 逆时针
[competition_master_stage3.py-19] [INFO] [1781609232.346395864] [competition_master_stage3]:   VLM结果话题: vlm_result
[competition_master_stage3.py-19] [INFO] [1781609232.350763059] [competition_master_stage3]: ============================================================
[component_container_isolated-18] [INFO] [1781609232.380009466] [global_costmap.global_costmap]: Using plugin "static_layer"
[component_container_isolated-18] [INFO] [1781609232.399429155] [global_costmap.global_costmap]: Subscribing to the map topic (/map) with transient local durability
[component_container_isolated-18] [INFO] [1781609232.407400796] [global_costmap.global_costmap]: Initialized plugin "static_layer"
[component_container_isolated-18] [INFO] [1781609232.407592129] [global_costmap.global_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781609232.425010991] [global_costmap.global_costmap]: Subscribed to Topics: scan aurora_points
[component_container_isolated-18] [INFO] [1781609232.502833036] [global_costmap.global_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781609232.504188823] [global_costmap.global_costmap]: Using plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781609232.515595579] [global_costmap.global_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781609232.515776037] [global_costmap.global_costmap]: Using plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781609232.533616147] [global_costmap.global_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781609232.575225182] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 163 X 141 at 0.050000 m/pix
[component_container_isolated-18] [INFO] [1781609232.604962088] [planner_server]: Created global planner plugin GridBased of type nav2_smac_planner/SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781609232.605240295] [planner_server]: Configuring GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781609232.646551165] [planner_server]: Even sized heuristic lookup table size set 200.000000, increasing size by 1 to make odd
[imu_madgwick_filter.py-4] [INFO] [1781609233.671228284] [imu_madgwick_filter]: [imu_madgwick ->] msgs=200 q_w=0.9999 angle=1.2deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781609233.688930479] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=449 q_w=0.9994 angle=4.0deg beta=0.0030
[qr_decoder-12] [INFO] [1781609239.287397212] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=200 last_qr_frame=-1 gap=-1 frames rejects=0
[imu_madgwick_filter.py-4] [INFO] [1781609243.669845503] [imu_madgwick_filter]: [imu_madgwick ->] msgs=400 q_w=0.9998 angle=2.4deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781609243.689487825] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1073 q_w=0.9994 angle=4.1deg beta=0.0030
[component_container_isolated-18] [INFO] [1781609246.688620095] [planner_server]: Configured plugin GridBased of type SmacPlannerHybrid with maximum iterations 1500, max on approach iterations 300, and not allowing unknown traversal. Tolerance 0.50.Using motion model: Reeds-Shepp.
[component_container_isolated-18] [INFO] [1781609246.688887469] [planner_server]: Planner Server has GridBased  planners available.
[component_container_isolated-18] [INFO] [1781609246.739081798] [lifecycle_manager_navigation]: Configuring behavior_server
[component_container_isolated-18] [INFO] [1781609246.739777213] [behavior_server]: Configuring
[component_container_isolated-18] [INFO] [1781609246.767273975] [behavior_server]: Creating behavior plugin spin of type nav2_behaviors/Spin
[component_container_isolated-18] [INFO] [1781609246.774009499] [behavior_server]: Configuring spin
[component_container_isolated-18] [INFO] [1781609246.821600793] [behavior_server]: Creating behavior plugin backup of type nav2_behaviors/BackUp
[component_container_isolated-18] [INFO] [1781609246.825419242] [behavior_server]: Configuring backup
[component_container_isolated-18] [INFO] [1781609246.865291680] [behavior_server]: Creating behavior plugin drive_on_heading of type nav2_behaviors/DriveOnHeading
[component_container_isolated-18] [INFO] [1781609246.869285087] [behavior_server]: Configuring drive_on_heading
[component_container_isolated-18] [INFO] [1781609246.906199325] [behavior_server]: Creating behavior plugin wait of type nav2_behaviors/Wait
[component_container_isolated-18] [INFO] [1781609246.911061479] [behavior_server]: Configuring wait
[component_container_isolated-18] [INFO] [1781609246.941883900] [lifecycle_manager_navigation]: Configuring bt_navigator
[component_container_isolated-18] [INFO] [1781609246.942457398] [bt_navigator]: Configuring
[competition_master_stage3.py-19] [INFO] [1781609247.295584541] [competition_master_stage3]: [LAUNCH] 发车阶段: 15.2s
[competition_master_stage3.py-19] [INFO] [1781609247.299178282] [competition_master_stage3]: >>> 系统就绪, 开始 Stage 3 导航
[competition_master_stage3.py-19] [INFO] [1781609247.305109016] [competition_master_stage3]: [状态机] INIT → NAV_TO_QR
[competition_master_stage3.py-19] [INFO] [1781609247.310498294] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-18] [INFO] [1781609247.366704485] [lifecycle_manager_navigation]: Configuring waypoint_follower
[component_container_isolated-18] [INFO] [1781609247.368249398] [waypoint_follower]: Configuring
[competition_master_stage3.py-19] [WARN] [1781609247.378009331] [competition_master_stage3]: 导航目标被拒绝, 3s 后重试...
[component_container_isolated-18] [INFO] [1781609247.457793754] [waypoint_follower]: Created waypoint_task_executor : wait_at_waypoint of type nav2_waypoint_follower::WaitAtWaypoint
[component_container_isolated-18] [INFO] [1781609247.464924111] [lifecycle_manager_navigation]: Configuring velocity_smoother
[component_container_isolated-18] [INFO] [1781609247.465886567] [velocity_smoother]: Configuring velocity smoother
[component_container_isolated-18] [INFO] [1781609247.523814461] [lifecycle_manager_navigation]: Activating controller_server
[component_container_isolated-18] [INFO] [1781609247.524828542] [controller_server]: Activating
[component_container_isolated-18] [INFO] [1781609247.525132416] [local_costmap.local_costmap]: Activating
[component_container_isolated-18] [INFO] [1781609247.525260916] [local_costmap.local_costmap]: Checking transform
[component_container_isolated-18] [INFO] [1781609247.526244788] [local_costmap.local_costmap]: start
[component_container_isolated-18] [INFO] [1781609247.538862548] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609247.549636021] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609247.549856520] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781609247.755087499] [local_costmap.local_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[component_container_isolated-18] [INFO] [1781609247.849558509] [controller_server]: Activating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781609247.849771717] [controller_server]: Creating bond (controller_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609247.962180432] [lifecycle_manager_navigation]: Server controller_server connected with bond.
[component_container_isolated-18] [INFO] [1781609247.962369306] [lifecycle_manager_navigation]: Activating smoother_server
[component_container_isolated-18] [INFO] [1781609247.963685094] [smoother_server]: Activating
[component_container_isolated-18] [INFO] [1781609247.963953510] [smoother_server]: Activating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781609247.964149843] [smoother_server]: Creating bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609248.080927050] [lifecycle_manager_navigation]: Server smoother_server connected with bond.
[component_container_isolated-18] [INFO] [1781609248.081110174] [lifecycle_manager_navigation]: Activating planner_server
[component_container_isolated-18] [INFO] [1781609248.082032672] [planner_server]: Activating
[component_container_isolated-18] [INFO] [1781609248.082368838] [global_costmap.global_costmap]: Activating
[component_container_isolated-18] [INFO] [1781609248.082461213] [global_costmap.global_costmap]: Checking transform
[component_container_isolated-18] [INFO] [1781609248.082750129] [global_costmap.global_costmap]: start
[component_container_isolated-18] [INFO] [1781609248.092199480] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609248.100771917] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609248.100922083] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781609248.108732480] [global_costmap.global_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[component_container_isolated-18] [INFO] [1781609249.200640302] [planner_server]: Activating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781609249.205880622] [planner_server]: Creating bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609249.320736381] [lifecycle_manager_navigation]: Server planner_server connected with bond.
[component_container_isolated-18] [INFO] [1781609249.320907298] [lifecycle_manager_navigation]: Activating behavior_server
[component_container_isolated-18] [INFO] [1781609249.321959170] [behavior_server]: Activating
[component_container_isolated-18] [INFO] [1781609249.322091503] [behavior_server]: Activating spin
[component_container_isolated-18] [INFO] [1781609249.322765168] [behavior_server]: Activating backup
[component_container_isolated-18] [INFO] [1781609249.322980501] [behavior_server]: Activating drive_on_heading
[component_container_isolated-18] [INFO] [1781609249.323143376] [behavior_server]: Activating wait
[component_container_isolated-18] [INFO] [1781609249.323269125] [behavior_server]: Creating bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609249.449797564] [lifecycle_manager_navigation]: Server behavior_server connected with bond.
[component_container_isolated-18] [INFO] [1781609249.449968439] [lifecycle_manager_navigation]: Activating bt_navigator
[component_container_isolated-18] [INFO] [1781609249.451465893] [bt_navigator]: Activating
[component_container_isolated-18] [WARN] [1781609249.570105102] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781609249.660366797] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781609249.716729908] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781609249.851474160] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781609250.052474251] [bt_navigator_navigate_to_pose_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [INFO] [1781609250.235116810] [bt_navigator]: Creating bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609250.358221095] [lifecycle_manager_navigation]: Server bt_navigator connected with bond.
[component_container_isolated-18] [INFO] [1781609250.358390428] [lifecycle_manager_navigation]: Activating waypoint_follower
[component_container_isolated-18] [INFO] [1781609250.359465300] [waypoint_follower]: Activating
[component_container_isolated-18] [INFO] [1781609250.359721633] [waypoint_follower]: Creating bond (waypoint_follower) to lifecycle manager.
[competition_master_stage3.py-19] [INFO] [1781609250.391554056] [competition_master_stage3]: 重试发送导航目标 (QR点)...
[competition_master_stage3.py-19] [INFO] [1781609250.397758583] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-18] [INFO] [1781609250.408882848] [bt_navigator]: Begin navigating from current location (-1.98, -0.01) to (0.41, -3.17)
[competition_master_stage3.py-19] [INFO] [1781609250.412321464] [competition_master_stage3]: 导航目标已接受，车辆出发...
[component_container_isolated-18] [INFO] [1781609250.477288432] [lifecycle_manager_navigation]: Server waypoint_follower connected with bond.
[component_container_isolated-18] [INFO] [1781609250.477478848] [lifecycle_manager_navigation]: Activating velocity_smoother
[component_container_isolated-18] [INFO] [1781609250.478835803] [velocity_smoother]: Activating
[component_container_isolated-18] [INFO] [1781609250.479191761] [velocity_smoother]: Creating bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609250.605682413] [lifecycle_manager_navigation]: Server velocity_smoother connected with bond.
[component_container_isolated-18] [INFO] [1781609250.605849080] [lifecycle_manager_navigation]: Managed nodes are active
[component_container_isolated-18] [INFO] [1781609250.605910705] [lifecycle_manager_navigation]: Creating bond timer...
[component_container_isolated-18] [WARN] [1781609251.099972555] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4545 Hz
[component_container_isolated-18] [INFO] [1781609251.211557748] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-18] [WARN] [1781609251.212012455] [controller_server]: No goal checker was specified in parameter 'current_goal_checker'. Server will use only plugin loaded goal_checker . This warning will appear once.
[cmd_vel_mux.py-8] [INFO] [1781609251.259310468] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=-0.12
[velocity_pid.py-9] [INFO] [1781609251.282695246] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.15 err=100.0%
[component_container_isolated-18] Reallocing temp weights 301 - 60
[competition_master_stage3.py-19] [INFO] [1781609252.163006908] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.94,-0.00) yaw=13deg cmd=(vx=0.50 wz=-1.16) elapsed=4.8s plan[31pts 4.1m] (-2.00,-0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=70C cpu=67% mem=18%
[component_container_isolated-18] [WARN] [1781609253.096581354] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2742 Hz
[component_container_isolated-18] [INFO] [1781609253.212363754] [controller_server]: Passing new path to controller.
[rviz2-20] [INFO] [1781609253.331270731] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-20] [INFO] [1781609253.335833012] [rviz2]: OpenGl version: 4.5 (GLSL 4.5)
[imu_madgwick_filter.py-4] [INFO] [1781609253.670718659] [imu_madgwick_filter]: [imu_madgwick ->] msgs=600 q_w=0.7937 angle=74.9deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781609253.688182952] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1602 q_w=0.7966 angle=74.4deg beta=0.0030
[component_container_isolated-18] Reallocing temp weights 1500 - 60
[rviz2-20] [INFO] [1781609253.742582577] [rviz2]: Stereo is NOT SUPPORTED
[qr_decoder-12] [INFO] [1781609254.074276151] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=400 last_qr_frame=-1 gap=-1 frames rejects=0
[competition_master_stage3.py-19] [INFO] [1781609254.158845626] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.17,-0.49) yaw=-60deg cmd=(vx=0.50 wz=-0.07) elapsed=6.8s plan[26pts 3.6m] (-1.50,-0.15)→(0.40,-3.15) cpuFreq=1500MHz cpuT=70C cpu=70% mem=19%
[velocity_pid.py-9] [INFO] [1781609254.391041143] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.52 corrected=-0.06 err=26.1%
[cmd_vel_mux.py-8] [INFO] [1781609254.423538820] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.27
[velocity_pid.py-9] [INFO] [1781609254.608706776] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0337s, resetting
[component_container_isolated-18] [WARN] [1781609255.094887265] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2764 Hz
[component_container_isolated-18] [INFO] [1781609255.212429504] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781609255.301076974] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.12
[velocity_pid.py-9] [INFO] [1781609255.408996276] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0340s, resetting
[velocity_pid.py-9] [INFO] [1781609255.414719846] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.06 corrected=0.29 err=208.3%
[competition_master_stage3.py-19] [INFO] [1781609256.159391991] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.99,-0.87) yaw=-57deg cmd=(vx=0.50 wz=0.13) elapsed=8.8s plan[19pts 2.6m] (-0.90,-0.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=71C cpu=50% mem=19%
[velocity_pid.py-9] [INFO] [1781609256.443332955] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.37 corrected=0.32 err=26.8%
[rviz2-20] [INFO] [1781609256.838900092] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[rviz2-20] [INFO] [1781609256.841722378] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[component_container_isolated-18] [WARN] [1781609257.094012997] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2776 Hz
[component_container_isolated-18] [INFO] [1781609257.212495077] [controller_server]: Passing new path to controller.
[rviz2-20] [ERROR] [1781609257.430997067] [rviz2]: Vertex Program:rviz/glsl120/indexed_8bit_image.vert Fragment Program:rviz/glsl120/indexed_8bit_image.frag GLSL link result :
[rviz2-20] active samplers with a different type refer to the same texture image unit
[competition_master_stage3.py-19] [INFO] [1781609258.159541304] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.58,-1.48) yaw=-63deg cmd=(vx=0.50 wz=-0.14) elapsed=10.8s plan[17pts 2.3m] (-0.80,-1.25)→(0.40,-3.15) cpuFreq=1500MHz cpuT=71C cpu=17% mem=19%
[rviz2-20] [INFO] [1781609258.392360815] [rviz2]: Trying to create a map of size 60 x 60 using 1 swatches
[cmd_vel_mux.py-8] [INFO] [1781609258.395667350] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.21
[velocity_pid.py-9] [INFO] [1781609258.395745891] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.08 dt=0.0481s, resetting
[velocity_pid.py-9] [INFO] [1781609258.400751672] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.06 err=22.7%
[velocity_pid.py-9] [INFO] [1781609258.608057986] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0335s, resetting
[qr_decoder-12] [INFO] [1781609258.796983380] [qr_decoder_zbar]: [qr_decoder] QR DETECTED frame=465 symbols=1 (gap=-1 frames)
[qr_decoder-12] [INFO] [1781609258.797211380] [qr_decoder_zbar]: [QR] 1584 | 3D:(-0.674, +0.138, 1.761)m | px(159,230) D:1761mm
[qr_decoder-12] [INFO] [1781609258.798112170] [qr_decoder_zbar]: [QR] 1584 | robot_pos: (0.81, -2.55, yaw=-1.59)
[qr_decision-13] [INFO] [1781609258.802144120] [qr_decision]: [QR] 1584 CCW @ (x=0.80, y=-2.57, yaw=-1.57) → /qr_event
[qr_decision-13] [INFO] [1781609258.805699404] [qr_decision]: [检查点] qr_decision 发布 /qr_event (由 task_manager 决定停车)
[competition_master_stage3.py-19] [INFO] [1781609258.809230271] [competition_master_stage3]: [QR检测] 内容: 1584
[competition_master_stage3.py-19] [INFO] [1781609258.814184594] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decoder_zbar
[competition_master_stage3.py-19] [INFO] [1781609258.816961338] [competition_master_stage3]: >>> QR 解码已关闭, 等待方向判断 (/qr_event)...
[competition_master_stage3.py-19] [INFO] [1781609258.819393083] [competition_master_stage3]: [QR检测] 取消当前导航目标, 等待BT完成 cancel/halt 清理...
[competition_master_stage3.py-19] [INFO] [1781609258.832431389] [competition_master_stage3]: [QR事件] 方向: 逆时针 (通道巡航阶段使用)
[competition_master_stage3.py-19] [INFO] [1781609258.840173790] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decision
[qr_decoder-12] [INFO] [1781609258.871142433] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-18] [WARN] [1781609259.090448058] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3115 Hz
[component_container_isolated-18] [INFO] [1781609259.112372430] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-18] [INFO] [1781609259.112563221] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1781609259.113148803] [bt_navigator]: [navigate_to_pose] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1781609259.113863760] [bt_navigator]: Goal canceled
[competition_master_stage3.py-19] [INFO] [1781609259.121516119] [competition_master_stage3]: [结果回调] BT取消确认完成 (STATUS_CANCELED), 准备发送通道入口目标...
[competition_master_stage3.py-19] [INFO] [1781609259.124700863] [competition_master_stage3]: [状态机] NAV_TO_QR → BACKING_UP
[competition_master_stage3.py-19] [INFO] [1781609259.129191103] [competition_master_stage3]: >>> BT取消完成, 右后退摆正车头→前进进通道...
[competition_master_stage3.py-19] [INFO] [1781609259.135597673] [competition_master_stage3]: [BACKUP] 右后退中: vx=-0.15 wz=0.80, 持续 6.0s...
[cmd_vel_mux.py-8] [INFO] [1781609259.161905536] [cmd_vel_mux]: [mux→] src=nav vx=-0.15 wz=0.80
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
[INFO] [qr_decoder-12]: process has finished cleanly [pid 12902]
[velocity_pid.py-9] [INFO] [1781609259.574901683] [velocity_pid]: [vel_pid→] desired=-0.15 actual=-0.07 corrected=-0.43 err=52.7%
[cmd_vel_mux.py-8] [INFO] [1781609259.697277222] [cmd_vel_mux]: [mux→] src=nav vx=0.00 wz=0.00
[ERROR] [qr_decision-13]: process has died [pid 12904, exit code 1, cmd '/userdata/dev_ws/install/origincar_qr/lib/origincar_qr/qr_decision --ros-args -r __node:=qr_decision --params-file /tmp/launch_params_36l62z9b'].
[competition_master_stage3.py-19] [INFO] [1781609260.157574194] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.40,-1.86) yaw=-72deg cmd=(vx=0.00 wz=0.00) elapsed=12.8s plan[10pts 1.4m] (-0.30,-2.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=71C cpu=50% mem=18%
[velocity_pid.py-9] [INFO] [1781609260.575822805] [velocity_pid]: [vel_pid→] desired=-0.15 actual=-0.10 corrected=-0.19 err=34.7%
[competition_master_stage3.py-19] [INFO] [1781609262.156142279] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.44,-1.84) yaw=-30deg cmd=(vx=-0.15 wz=0.80) elapsed=14.8s plan[10pts 1.4m] (-0.30,-2.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=71C cpu=14% mem=18%
[imu_madgwick_filter.py-4] [INFO] [1781609263.670318561] [imu_madgwick_filter]: [imu_madgwick ->] msgs=797 q_w=0.9953 angle=11.1deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781609263.688670109] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2095 q_w=0.9984 angle=6.5deg beta=0.0030
[competition_master_stage3.py-19] [INFO] [1781609264.155414473] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.67,-1.76) yaw=13deg cmd=(vx=-0.15 wz=0.80) elapsed=16.8s plan[10pts 1.4m] (-0.30,-2.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=70C cpu=0% mem=19%
[rviz2-20] [INFO] [1781609264.236478488] [rviz2]: Message Filter dropping message: frame 'odom' at time 1781609255.132 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[competition_master_stage3.py-19] [INFO] [1781609265.138855761] [competition_master_stage3]: [状态机] BACKING_UP → CRUISE_CHANNEL
[competition_master_stage3.py-19] [INFO] [1781609265.142346129] [competition_master_stage3]: [CRUISE] 方向: CCW (逆时针, even QR), 路点: (1.73,-1.98), (3.10,-1.35), (2.10,0.92)
[competition_master_stage3.py-19] [INFO] [1781609265.150618989] [competition_master_stage3]: [CRUISE] NavigateThroughPoses: (0.38,-1.10), (1.73,-1.98), (3.10,-1.35), (2.10,0.92)
[component_container_isolated-18] [INFO] [1781609265.153252109] [bt_navigator]: Begin navigating from current location through 4 poses to (2.10, 0.92)
[cmd_vel_mux.py-8] [INFO] [1781609265.161016845] [cmd_vel_mux]: [mux→] src=stop vx=0.00 wz=0.00
[competition_master_stage3.py-19] [INFO] [1781609265.162058968] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[cmd_vel_mux.py-8] [INFO] [1781609265.659260514] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.52s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1781609265.667298249] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[component_container_isolated-18] [WARN] [1781609266.110990106] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.0466 Hz
[competition_master_stage3.py-19] [INFO] [1781609266.161851097] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.88,-1.89) yaw=54deg cmd=(vx=0.00 wz=0.00) elapsed=18.8s plan[10pts 1.4m] (-0.30,-2.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=71C cpu=70% mem=19%
[component_container_isolated-18] [INFO] [1781609266.255425346] [controller_server]: Received a goal, begin computing control effort.
[cmd_vel_mux.py-8] [INFO] [1781609266.291322531] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=-0.12
[velocity_pid.py-9] [INFO] [1781609266.308529875] [velocity_pid]: [vel_pid→] desired=0.07 actual=-0.01 corrected=0.08 err=108.0%
[velocity_pid.py-9] [INFO] [1781609267.309462504] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.37 corrected=0.19 err=26.8%
[velocity_pid.py-9] [INFO] [1781609267.682787347] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.02 -> current=0.10 dt=0.0328s, resetting
[component_container_isolated-18] [WARN] [1781609268.111625304] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3224 Hz
[competition_master_stage3.py-19] [INFO] [1781609268.159275556] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.69,-1.75) yaw=20deg cmd=(vx=0.50 wz=0.51) elapsed=20.8s plan[64pts 8.7m] (-0.90,-1.95)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=57% mem=19%
[component_container_isolated-18] [INFO] [1781609268.255789223] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781609269.409381750] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.12 err=22.7%
[cmd_vel_mux.py-8] [INFO] [1781609269.464430032] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.13
[velocity_pid.py-9] [INFO] [1781609269.575253720] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.00 -> current=0.10 dt=0.0292s, resetting
[velocity_pid.py-9] [INFO] [1781609269.674490512] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0333s, resetting
[component_container_isolated-18] [WARN] [1781609270.112903777] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3242 Hz
[competition_master_stage3.py-19] [INFO] [1781609270.155739081] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.15,-1.23) yaw=32deg cmd=(vx=-0.30 wz=0.09) elapsed=22.8s plan[61pts 8.3m] (-0.50,-1.75)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=75% mem=19%
[component_container_isolated-18] [INFO] [1781609270.255802666] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781609270.308116788] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.09 -> current=-0.03 dt=0.0338s, resetting
[cmd_vel_mux.py-8] [INFO] [1781609270.371242226] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.16
[velocity_pid.py-9] [INFO] [1781609270.475588345] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0332s, resetting
[velocity_pid.py-9] [INFO] [1781609270.481484919] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.08 corrected=0.32 err=230.0%
[velocity_pid.py-9] [INFO] [1781609271.508162620] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.37 corrected=0.32 err=26.8%
[velocity_pid.py-9] [INFO] [1781609272.007972564] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.09 -> current=0.02 dt=0.0324s, resetting
[component_container_isolated-18] [WARN] [1781609272.103622872] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3395 Hz
[competition_master_stage3.py-19] [INFO] [1781609272.160519991] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.49,-1.08) yaw=-5deg cmd=(vx=0.50 wz=0.14) elapsed=24.8s plan[55pts 7.4m] (0.20,-1.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=57% mem=19%
[component_container_isolated-18] [INFO] [1781609272.255820841] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781609273.508905386] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.02 err=22.7%
[cmd_vel_mux.py-8] [INFO] [1781609273.559591516] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.53
[imu_madgwick_filter.py-4] [INFO] [1781609273.670534679] [imu_madgwick_filter]: [imu_madgwick ->] msgs=992 q_w=0.8672 angle=59.7deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781609273.688148943] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2630 q_w=0.8795 angle=56.8deg beta=0.0030
[velocity_pid.py-9] [INFO] [1781609273.779305845] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781609273.809100007] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.03 -> current=0.09 dt=0.0339s, resetting
[component_container_isolated-18] [WARN] [1781609274.101103311] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3413 Hz
[competition_master_stage3.py-19] [INFO] [1781609274.156219604] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.36,-1.36) yaw=-36deg cmd=(vx=-0.30 wz=0.59) elapsed=26.8s plan[53pts 6.9m] (0.60,-1.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=56% mem=19%
[component_container_isolated-18] [INFO] [1781609274.255794662] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781609274.363073960] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.35
[velocity_pid.py-9] [INFO] [1781609274.477140163] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781609274.508578449] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.10 -> current=-0.03 dt=0.0341s, resetting
[velocity_pid.py-9] [INFO] [1781609274.511754653] [velocity_pid]: [vel_pid→] desired=0.14 actual=-0.06 corrected=0.31 err=148.1%
[velocity_pid.py-9] [INFO] [1781609276.008424984] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.12 -> current=-0.00 dt=0.0337s, resetting
[velocity_pid.py-9] [INFO] [1781609276.012706102] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.02 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1781609276.058962286] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.13
[component_container_isolated-18] [WARN] [1781609276.100299769] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.1999 Hz
[competition_master_stage3.py-19] [INFO] [1781609276.158756644] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.60,-1.65) yaw=-60deg cmd=(vx=0.23 wz=-0.06) elapsed=28.8s plan[44pts 6.0m] (1.50,-1.45)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=67% mem=19%
[component_container_isolated-18] [INFO] [1781609276.255800172] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781609276.278626806] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0325s, resetting
[cmd_vel_mux.py-8] [INFO] [1781609276.559059322] [cmd_vel_mux]: [mux→] src=nav vx=-0.20 wz=-0.30
[velocity_pid.py-9] [INFO] [1781609277.041989966] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.03 corrected=-0.34 err=91.3%
[cmd_vel_mux.py-8] [INFO] [1781609277.996193678] [cmd_vel_mux]: [mux→] src=nav vx=-0.03 wz=-0.27
[velocity_pid.py-9] [INFO] [1781609278.076483986] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0335s, resetting
[velocity_pid.py-9] [INFO] [1781609278.082548019] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.26 corrected=0.74 err=535.0%
[component_container_isolated-18] [WARN] [1781609278.096734500] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3491 Hz
[competition_master_stage3.py-19] [INFO] [1781609278.156318086] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.76,-1.91) yaw=-66deg cmd=(vx=0.14 wz=-0.02) elapsed=30.8s plan[42pts 5.7m] (1.70,-1.75)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=57% mem=19%
[velocity_pid.py-9] [INFO] [1781609278.177325724] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.02 -> current=0.11 dt=0.0327s, resetting
[component_container_isolated-18] [INFO] [1781609278.255813159] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781609279.108589047] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.35 corrected=0.34 err=29.4%
[component_container_isolated-18] [WARN] [1781609280.095628246] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3524 Hz
[competition_master_stage3.py-19] [INFO] [1781609280.171556856] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.85,-2.04) yaw=-57deg cmd=(vx=0.50 wz=1.27) elapsed=32.8s plan[33pts 4.5m] (2.00,-2.25)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=71% mem=19%
[component_container_isolated-18] [INFO] [1781609280.255803748] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781609281.514566023] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.51 corrected=0.07 err=24.4%
[cmd_vel_mux.py-8] [INFO] [1781609281.560606132] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.49
[velocity_pid.py-9] [INFO] [1781609281.776932361] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0329s, resetting
[velocity_pid.py-9] [INFO] [1781609281.780181315] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.12 -> current=-0.01 dt=0.0329s, resetting
[component_container_isolated-18] [WARN] [1781609282.095614591] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3516 Hz
[competition_master_stage3.py-19] [INFO] [1781609282.169817751] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.82,-2.03) yaw=48deg cmd=(vx=-0.30 wz=-0.72) elapsed=34.8s plan[27pts 3.8m] (2.90,-1.95)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=62% mem=19%
[component_container_isolated-18] [INFO] [1781609282.264413011] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781609282.361515518] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.47
[velocity_pid.py-9] [INFO] [1781609282.481969330] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0395s, resetting
[velocity_pid.py-9] [INFO] [1781609282.542151840] [velocity_pid]: [vel_pid→] desired=0.14 actual=-0.06 corrected=0.19 err=148.1%
[imu_madgwick_filter.py-4] [INFO] [1781609283.673064823] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1189 q_w=0.9630 angle=31.3deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781609283.689066304] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3154 q_w=0.9408 angle=39.6deg beta=0.0030
[cmd_vel_mux.py-8] [INFO] [1781609284.059313286] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.25
[velocity_pid.py-9] [INFO] [1781609284.078228139] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.49 corrected=-0.06 err=53.1%
[component_container_isolated-18] [WARN] [1781609284.095176078] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2094 Hz
[competition_master_stage3.py-19] [INFO] [1781609284.168278994] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.03,-1.65) yaw=58deg cmd=(vx=0.23 wz=0.13) elapsed=36.8s plan[24pts 3.3m] (3.10,-1.55)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=78% mem=19%
[component_container_isolated-18] [INFO] [1781609284.261663304] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781609284.280420158] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0335s, resetting
[cmd_vel_mux.py-8] [INFO] [1781609284.561768711] [cmd_vel_mux]: [mux→] src=nav vx=0.10 wz=0.36
[velocity_pid.py-9] [INFO] [1781609284.677386537] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.01 -> current=-0.08 dt=0.0336s, resetting
[velocity_pid.py-9] [INFO] [1781609284.709962333] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.11 -> current=-0.02 dt=0.0343s, resetting
[velocity_pid.py-9] [INFO] [1781609285.108645880] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.01 corrected=-0.29 err=95.7%
[component_container_isolated-18] [WARN] [1781609286.091227042] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3596 Hz
[competition_master_stage3.py-19] [INFO] [1781609286.170985707] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.17,-1.43) yaw=61deg cmd=(vx=-0.30 wz=-0.24) elapsed=38.8s plan[20pts 2.8m] (3.20,-1.45)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=83% mem=19%
[velocity_pid.py-9] [INFO] [1781609286.208289083] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.11 -> current=0.01 dt=0.0338s, resetting
[component_container_isolated-18] [INFO] [1781609286.255820241] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781609286.308143309] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.29 corrected=0.00 err=40.0%
[cmd_vel_mux.py-8] [INFO] [1781609286.363289375] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.31
[velocity_pid.py-9] [INFO] [1781609286.475315963] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0332s, resetting
[velocity_pid.py-9] [INFO] [1781609286.908476622] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.12 -> current=-0.00 dt=0.0341s, resetting
[velocity_pid.py-9] [INFO] [1781609287.308451536] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.23 corrected=0.41 err=53.0%
[component_container_isolated-18] [WARN] [1781609288.092176807] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.1964 Hz
[competition_master_stage3.py-19] [INFO] [1781609288.163613610] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.15,-1.34) yaw=62deg cmd=(vx=0.50 wz=1.32) elapsed=40.8s plan[19pts 2.7m] (3.20,-1.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=86% mem=19%
[component_container_isolated-18] [INFO] [1781609288.255792059] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781609288.342579680] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.20 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1781609288.362679827] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=1.02
[velocity_pid.py-9] [INFO] [1781609288.577878152] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781609288.808904878] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.02 -> current=-0.10 dt=0.0346s, resetting
[velocity_pid.py-9] [INFO] [1781609289.375906321] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.09 corrected=-0.34 err=69.7%
[component_container_isolated-18] [WARN] [1781609290.091021962] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1781609290.091271504] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.10, 0.92)
[component_container_isolated-18] [WARN] [1781609290.091377879] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[competition_master_stage3.py-19] [INFO] [1781609290.157244025] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.15,-0.81) yaw=102deg cmd=(vx=-0.30 wz=-0.03) elapsed=42.8s plan[19pts 2.7m] (3.20,-1.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=20% mem=19%
[component_container_isolated-18] [INFO] [1781609290.254083185] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781609290.264915841] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609290.274751040] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1781609290.275185248] [behavior_server]: wait completed successfully
[component_container_isolated-18] [INFO] [1781609290.277099746] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609290.277248080] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781609290.288748902] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781609291.091465445] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3601 Hz
[component_container_isolated-18] [INFO] [1781609291.255789630] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781609291.307869749] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.31 corrected=0.00 err=46.2%
[cmd_vel_mux.py-8] [INFO] [1781609291.359590328] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.45
[velocity_pid.py-9] [INFO] [1781609291.478470679] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0332s, resetting
[competition_master_stage3.py-19] [INFO] [1781609292.162522191] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.20,-1.34) yaw=92deg cmd=(vx=0.50 wz=0.06) elapsed=44.8s plan[18pts 2.4m] (3.20,-1.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=78% mem=19%
[velocity_pid.py-9] [INFO] [1781609292.308869231] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.23 corrected=0.40 err=53.0%
[component_container_isolated-18] [WARN] [1781609293.092110345] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1781609293.092439595] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.10, 0.92)
[component_container_isolated-18] [WARN] [1781609293.092584636] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1781609293.254186085] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781609293.267956656] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609293.279733855] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1781609293.280868854] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609293.282084728] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781609293.282042311] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1781609293.292732802] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-4] [INFO] [1781609293.669876737] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1385 q_w=0.6805 angle=94.2deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781609293.690771470] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3677 q_w=0.5996 angle=106.3deg beta=0.0030
[component_container_isolated-18] [WARN] [1781609294.098077591] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.8443 Hz
[velocity_pid.py-9] [INFO] [1781609294.109878082] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.11 -> current=-0.01 dt=0.0338s, resetting
[velocity_pid.py-9] [INFO] [1781609294.113623662] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.08 err=21.2%
[competition_master_stage3.py-19] [INFO] [1781609294.155373504] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.96,-0.67) yaw=128deg cmd=(vx=0.41 wz=-0.01) elapsed=46.8s plan[18pts 2.4m] (3.20,-1.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=29% mem=19%
[cmd_vel_mux.py-8] [INFO] [1781609294.157988168] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.14
[component_container_isolated-18] [INFO] [1781609294.255803465] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781609295.743123090] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.19 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1781609295.760678243] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.26
[velocity_pid.py-9] [INFO] [1781609295.980106408] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0333s, resetting
[component_container_isolated-18] [WARN] [1781609296.092889616] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3919 Hz
[competition_master_stage3.py-19] [INFO] [1781609296.165725521] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.40,0.04) yaw=117deg cmd=(vx=-0.26 wz=0.16) elapsed=48.8s plan[7pts 0.9m] (2.40,0.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=60% mem=19%
[component_container_isolated-18] [INFO] [1781609296.255794496] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781609296.364181917] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.12
[velocity_pid.py-9] [INFO] [1781609296.375662533] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.00 -> current=-0.12 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1781609296.477652708] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0325s, resetting
[velocity_pid.py-9] [INFO] [1781609296.778437071] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.01 corrected=0.55 err=98.8%
[component_container_isolated-18] [WARN] [1781609298.091921104] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2016 Hz
[competition_master_stage3.py-19] [INFO] [1781609298.157503144] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.16,0.44) yaw=108deg cmd=(vx=0.50 wz=-0.41) elapsed=50.8s plan[3pts 0.4m] (2.10,0.55)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=0% mem=19%
[component_container_isolated-18] [INFO] [1781609298.255796953] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781609298.309327917] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.02 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1781609298.358031260] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.22
[component_container_isolated-18] [INFO] [1781609298.456493694] [controller_server]: Reached the goal!
[component_container_isolated-18] [INFO] [1781609298.954236862] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-19] [INFO] [1781609298.963659689] [competition_master_stage3]: [结果回调] 巡航完成, 到达VLM路点, 触发VLM推理...
[competition_master_stage3.py-19] [INFO] [1781609298.966014312] [competition_master_stage3]: [VLM] 发布 sign4return=100, 拍照推理中...
[competition_master_stage3.py-19] [INFO] [1781609298.969517393] [competition_master_stage3]: [状态机] CRUISE_CHANNEL → RETURN_P
[vision_ai_node-14] [INFO] [1781609298.970343309] [vision_ai_node]: Received sign4return: 100
[vision_ai_node-14] [INFO] [1781609298.973250391] [vision_ai_node]: Received trigger signal (sign4return=100), subscribing to image topic...
[competition_master_stage3.py-19] [INFO] [1781609298.975550848] [competition_master_stage3]: [RETURN] 清除机器人周围1.5m + 直接返航至 P点 (-1.99,-0.01)
[vision_ai_node-14] [INFO] [1781609298.995988709] [vision_ai_node]: Subscribed to /aurora/rgb/image_raw topic
[vision_ai_node-14] [INFO] [1781609299.016344696] [vision_ai_node]: Received compressed image, processing with AI model...
[competition_master_stage3.py-19] [INFO] [1781609299.084785736] [competition_master_stage3]: [DIAG] nav目标距离: 4.12m, robot=(2.01,0.97) → target=(-1.99,-0.01)
[competition_master_stage3.py-19] [INFO] [1781609299.088710691] [competition_master_stage3]: >>> 发送导航目标 [P点返航]: (-1.99, -0.01, yaw=1.58)
[component_container_isolated-18] [INFO] [1781609299.099234643] [bt_navigator]: Begin navigating from current location (2.07, 0.97) to (-1.99, -0.01)
[competition_master_stage3.py-19] [INFO] [1781609299.103447807] [competition_master_stage3]: 导航目标已接受，车辆出发...
[cmd_vel_mux.py-8] [INFO] [1781609299.957867223] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.52s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1781609299.963825178] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[component_container_isolated-18] [WARN] [1781609300.103062968] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 0.9984 Hz
[competition_master_stage3.py-19] [INFO] [1781609300.160030058] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.01,0.97) yaw=90deg cmd=(vx=0.00 wz=0.00) elapsed=52.8s plan[3pts 0.4m] (2.10,0.55)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=25% mem=19%
[component_container_isolated-18] [INFO] [1781609300.302745473] [controller_server]: Received a goal, begin computing control effort.
[cmd_vel_mux.py-8] [INFO] [1781609300.371216515] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=0.12
[velocity_pid.py-9] [INFO] [1781609300.384874465] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.19 err=100.0%
[component_container_isolated-18] [WARN] [1781609302.093251893] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1781609302.093507809] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (-1.99, -0.01)
[component_container_isolated-18] [WARN] [1781609302.093604351] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[competition_master_stage3.py-19] [INFO] [1781609302.158211399] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.82,1.38) yaw=139deg cmd=(vx=0.50 wz=1.65) elapsed=54.8s plan[45pts 6.7m] (2.00,1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=40% mem=19%
[component_container_isolated-18] [INFO] [1781609302.199931002] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781609302.209454622] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609302.216435493] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609302.216579618] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781609302.229819361] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[cmd_vel_mux.py-8] [INFO] [1781609302.692769196] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=1.12
[velocity_pid.py-9] [INFO] [1781609302.709679270] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.49 corrected=-0.10 err=53.1%
[velocity_pid.py-9] [INFO] [1781609302.909021705] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0348s, resetting
[component_container_isolated-18] [WARN] [1781609303.096874941] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1781609303.097134982] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (-1.99, -0.01)
[component_container_isolated-18] [WARN] [1781609303.097225316] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[velocity_pid.py-9] [INFO] [1781609303.175520610] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.12 -> current=-0.01 dt=0.0307s, resetting
[component_container_isolated-18] [INFO] [1781609303.203716095] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-18] [INFO] [1781609303.203891595] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1781609303.204524720] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1781609303.211093133] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609303.220462254] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781609303.220510129] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609303.220731045] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781609303.236141454] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1781609303.239917661] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609303.252465738] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609303.254657903] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781609303.252817696] [behavior_server]: Running backup
[component_container_isolated-18] [INFO] [1781609303.255821403] [behavior_server]: DriveOnHeading: no acceleration or deceleration limits set
[component_container_isolated-18] [WARN] [1781609303.257360152] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1781609303.257526902] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1781609303.259176609] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1781609303.267998063] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[cmd_vel_mux.py-8] [INFO] [1781609303.293255842] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.00
[component_container_isolated-18] [INFO] [1781609303.500852988] [behavior_server]: Running wait
[imu_madgwick_filter.py-4] [INFO] [1781609303.671155485] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1578 q_w=0.0237 angle=177.3deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781609303.688991143] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4194 q_w=-0.0863 angle=189.9deg beta=0.0030
[competition_master_stage3.py-19] [INFO] [1781609304.155269080] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.11,1.40) yaw=-157deg cmd=(vx=0.00 wz=0.00) elapsed=56.8s plan[45pts 6.7m] (2.00,1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=38% mem=19%
[cmd_vel_mux.py-8] [INFO] [1781609304.691294035] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.51s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1781609304.695048242] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[competition_master_stage3.py-19] [INFO] [1781609306.162516635] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.11,1.40) yaw=-157deg cmd=(vx=0.00 wz=0.00) elapsed=58.8s plan[45pts 6.7m] (2.00,1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=33% mem=19%
[component_container_isolated-18] [INFO] [1781609306.501325081] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1781609307.090081552] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1781609307.090357802] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (-1.99, -0.01)
[component_container_isolated-18] [WARN] [1781609307.090458261] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1781609307.200035761] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781609307.209532091] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609307.214886297] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609307.215099964] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781609307.224073627] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781609308.103040093] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1781609308.103265843] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (-1.99, -0.01)
[component_container_isolated-18] [WARN] [1781609308.103350384] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[competition_master_stage3.py-19] [INFO] [1781609308.160087407] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.11,1.40) yaw=-157deg cmd=(vx=0.00 wz=0.00) elapsed=60.8s plan[45pts 6.7m] (2.00,1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=70% mem=19%
[component_container_isolated-18] [INFO] [1781609308.200023393] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1781609308.209165015] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609308.213023014] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781609308.213273680] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609308.213461972] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781609308.222979885] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1781609308.229755675] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609308.239643254] [behavior_server]: Running backup
[component_container_isolated-18] [WARN] [1781609308.240663712] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1781609308.240810587] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1781609308.240878171] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1781609308.241091629] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609308.241168212] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781609308.254801666] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[cmd_vel_mux.py-8] [INFO] [1781609308.261629497] [cmd_vel_mux]: [mux→] src=nav vx=0.00 wz=0.00
[component_container_isolated-18] [INFO] [1781609308.500099665] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1781609308.513802994] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609308.525347532] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781609308.525393740] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609308.531687904] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781609308.536738403] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609308.546396816] [behavior_server]: Running backup
[component_container_isolated-18] [WARN] [1781609308.548183149] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1781609308.548327149] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1781609308.548929149] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1781609308.548450732] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609308.549659440] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781609308.550996273] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781609308.562553644] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1781609308.819767764] [behavior_server]: Running wait
[cmd_vel_mux.py-8] [INFO] [1781609309.058165184] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.50s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1781609309.062542475] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[competition_master_stage3.py-19] [INFO] [1781609310.156571181] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.11,1.40) yaw=-157deg cmd=(vx=0.00 wz=0.00) elapsed=62.8s plan[45pts 6.7m] (2.00,1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=17% mem=19%
[component_container_isolated-18] [INFO] [1781609311.822671575] [behavior_server]: wait completed successfully
[competition_master_stage3.py-19] [INFO] [1781609312.155617206] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.11,1.40) yaw=-157deg cmd=(vx=0.00 wz=0.00) elapsed=64.8s plan[45pts 6.7m] (2.00,1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=25% mem=19%
[component_container_isolated-18] [WARN] [1781609313.093296715] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1781609313.093562881] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (-1.99, -0.01)
[component_container_isolated-18] [WARN] [1781609313.093675340] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1781609313.199987653] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781609313.211677610] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609313.217974692] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609313.218148942] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781609313.228299982] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-4] [INFO] [1781609313.671829525] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1778 q_w=0.0378 angle=175.7deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781609313.689851521] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4722 q_w=-0.0861 angle=189.9deg beta=0.0030
[component_container_isolated-18] [WARN] [1781609314.091207700] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1781609314.091592367] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (-1.99, -0.01)
[component_container_isolated-18] [WARN] [1781609314.091769992] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[competition_master_stage3.py-19] [INFO] [1781609314.158661856] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.11,1.40) yaw=-157deg cmd=(vx=0.00 wz=0.00) elapsed=66.8s plan[45pts 6.7m] (2.00,1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=69% mem=19%
[component_container_isolated-18] [INFO] [1781609314.200009142] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1781609314.208839599] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609314.215722098] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609314.215869639] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781609314.215721931] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [WARN] [1781609314.230501220] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1781609314.235819636] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609314.245513885] [behavior_server]: Running backup
[component_container_isolated-18] [WARN] [1781609314.246169926] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1781609314.246342926] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1781609314.246410134] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1781609314.249763467] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609314.249917634] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[cmd_vel_mux.py-8] [INFO] [1781609314.259442674] [cmd_vel_mux]: [mux→] src=nav vx=0.00 wz=0.00
[component_container_isolated-18] [WARN] [1781609314.262104382] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1781609314.300153793] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1781609314.309096458] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609314.315191707] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609314.315360624] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781609314.315193582] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [WARN] [1781609314.328546580] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1781609314.338423370] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609314.349802077] [behavior_server]: Running backup
[component_container_isolated-18] [WARN] [1781609314.350837702] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1781609314.351092618] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1781609314.351188535] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1781609314.352693202] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609314.352860826] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781609314.366005991] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1781609314.600306914] [behavior_server]: Running wait
[cmd_vel_mux.py-8] [INFO] [1781609314.891267536] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.53s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1781609314.894655827] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[competition_master_stage3.py-19] [INFO] [1781609316.162451506] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.92,1.05) yaw=-98deg cmd=(vx=0.00 wz=0.00) elapsed=68.8s plan[45pts 6.7m] (2.00,1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=89% mem=19%
[component_container_isolated-18] [INFO] [1781609317.600684060] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1781609318.122981199] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 4.5110 Hz
[competition_master_stage3.py-19] [INFO] [1781609318.163534947] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.92,0.89) yaw=-88deg cmd=(vx=0.00 wz=0.00) elapsed=70.8s plan[45pts 6.7m] (2.00,1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=67% mem=19%
[component_container_isolated-18] [INFO] [1781609318.300726277] [controller_server]: Received a goal, begin computing control effort.
[cmd_vel_mux.py-8] [INFO] [1781609318.362246692] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=-0.12
[velocity_pid.py-9] [INFO] [1781609318.377539441] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.04 err=100.0%
[velocity_pid.py-9] [INFO] [1781609319.377711964] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.39 corrected=0.14 err=22.8%
[component_container_isolated-18] [WARN] [1781609320.093683843] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1781609320.093966509] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (-1.99, -0.01)
[component_container_isolated-18] [WARN] [1781609320.094100426] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[competition_master_stage3.py-19] [INFO] [1781609320.157957303] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.92,0.46) yaw=-90deg cmd=(vx=0.50 wz=0.16) elapsed=72.8s plan[37pts 5.3m] (0.90,0.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=75% mem=19%
[component_container_isolated-18] [INFO] [1781609320.200054013] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781609320.212781680] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781609320.222479430] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781609320.222636680] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781609320.230382472] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[cmd_vel_mux.py-8] [INFO] [1781609320.391743644] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.05
[velocity_pid.py-9] [INFO] [1781609320.408483727] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.48 corrected=-0.17 err=49.1%
[velocity_pid.py-9] [INFO] [1781609320.609124567] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0344s, resetting
[component_container_isolated-18] [WARN] [1781609321.112186003] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.1367 Hz
[component_container_isolated-18] [INFO] [1781609321.301027473] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781609321.375022811] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.02 -> current=0.11 dt=0.0331s, resetting
[velocity_pid.py-9] [INFO] [1781609321.442814440] [velocity_pid]: [vel_pid→] desired=-0.24 actual=-0.10 corrected=-0.27 err=57.1%
[cmd_vel_mux.py-8] [INFO] [1781609321.658435953] [cmd_vel_mux]: [mux→] src=nav vx=-0.18 wz=0.86
[competition_master_stage3.py-19] [INFO] [1781609322.162406405] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.96,0.05) yaw=-78deg cmd=(vx=0.15 wz=0.98) elapsed=74.8s plan[33pts 4.5m] (0.90,-0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=100% mem=19%
[cmd_vel_mux.py-8] [INFO] [1781609322.258876414] [cmd_vel_mux]: [mux→] src=nav vx=0.26 wz=0.61
[velocity_pid.py-9] [INFO] [1781609322.443016723] [velocity_pid]: [vel_pid→] desired=0.29 actual=-0.01 corrected=0.06 err=104.5%
[velocity_pid.py-9] [INFO] [1781609322.508493687] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.11 -> current=-0.02 dt=0.0338s, resetting
[component_container_isolated-18] [WARN] [1781609323.113273954] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4049 Hz
[cmd_vel_mux.py-8] [INFO] [1781609323.362899068] [cmd_vel_mux]: [mux→] src=nav vx=0.09 wz=-1.89
[component_container_isolated-18] [INFO] [1781609323.401032990] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781609323.475046290] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.20 corrected=-0.02 err=169.3%
[imu_madgwick_filter.py-4] [INFO] [1781609323.670662522] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1975 q_w=-0.4851 angle=238.0deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781609323.690090650] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5266 q_w=-0.6101 angle=255.2deg beta=0.0030
[competition_master_stage3.py-19] [INFO] [1781609324.169095171] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.96,-0.14) yaw=-98deg cmd=(vx=0.50 wz=-0.02) elapsed=76.8s plan[32pts 4.4m] (1.00,0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=100% mem=19%
[velocity_pid.py-9] [INFO] [1781609324.210618053] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.02 -> current=0.11 dt=0.0321s, resetting
[vision_ai_node-14] [INFO] [1781609324.671127498] [vision_ai_node]: AI Analysis Result: 这张图片展现了一个**昏暗的室内角落**，整体氛围静谧简约：
[vision_ai_node-14]
[vision_ai_node-14] ### 场景与背景
[vision_ai_node-14] - **墙面**：浅灰色（或米白色）的拼接板材/瓷砖，水平拼接缝清晰，风格简洁朴素。
[vision_ai_node-14] - **平面（桌面/地板）**：浅绿色的光滑表面（疑似桌面或地板），色调柔和。
[vision_ai_node-14] - **右侧物件**：一个**深色（近黑色/深蓝色）的大型家具**（如柜子、冰箱），底部露出金属支撑脚，显得厚重规整。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] ### 核心物体（塑料瓶）
[vision_ai_node-14] 画面中央偏左，摆放着一个**透明塑料瓶**：
[vision_ai_node-14] - 瓶身贴有**红色标签**（标签含黑色、白色的文字/图案，风格类似可乐类饮料标）；
[vision_ai_node-14] - 瓶盖为**明黄色**；
[vision_ai_node-14] - 瓶内液体极少，底部仅余少量残留（或近乎空置），透明瓶身清晰暴露内部空荡状态。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] ### 细节与色彩
[vision_ai_node-14] - **小物件**：墙面与浅绿色平面的交界处，散落一个**黑色小物件**（如笔、细棍）。
[vision_ai_node-14] - **光影**：塑料瓶的影子投射在浅绿色平面上，暗示光源方向（光线昏暗，室内照明不足）。
[vision_ai_node-14] - **色彩对比**：墙面浅素、平面浅绿、瓶身透明、标签艳红、瓶盖明黄、右侧物件深暗，冷暖色调含蓄碰撞，视觉焦点集中在中央的塑料瓶上。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] 整体氛围昏暗静谧，塑料瓶（似闲置的饮料瓶）、浅绿平面、素色墙面与深色家具的组合，传递出一种“闲置角落”的安静感。
[competition_master_stage3.py-19] [INFO] [1781609324.678874291] [competition_master_stage3]: [VLM] 后台收到推理结果: 这张图片展现了一个**昏暗的室内角落**，整体氛围静谧简约：
[competition_master_stage3.py-19]
[competition_master_stage3.py-19] ### 场景与背景
[competition_master_stage3.py-19] - **墙面**：浅灰色（或米白色）的拼接板材/瓷砖，水平拼接缝清晰，风格简洁朴素。
[competition_master_stage3.py-19] - **平面（桌面/地板）**：浅绿色的光滑表面（疑似桌面...
[vision_ai_node-14] [INFO] [1781609324.687868792] [vision_ai_node]: Unsubscribed from image topic
[component_container_isolated-18] [WARN] [1781609325.106389817] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2426 Hz
[velocity_pid.py-9] [INFO] [1781609325.178965705] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.51 corrected=-0.16 err=24.4%
[cmd_vel_mux.py-8] [INFO] [1781609325.191220166] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.39
[component_container_isolated-18] [INFO] [1781609325.301015269] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1781609326.159011846] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.70,-0.94) yaw=-137deg cmd=(vx=0.50 wz=-1.29) elapsed=78.8s plan[26pts 3.3m] (0.90,-0.55)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=38% mem=19%
[cmd_vel_mux.py-8] [INFO] [1781609326.492189917] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.67
[velocity_pid.py-9] [INFO] [1781609326.508416962] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.48 corrected=-0.19 err=49.1%
[velocity_pid.py-9] [INFO] [1781609326.708200838] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0341s, resetting
[velocity_pid.py-9] [INFO] [1781609326.808868859] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.08 dt=0.0344s, resetting
[component_container_isolated-18] [WARN] [1781609327.096064381] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4451 Hz
[component_container_isolated-18] [INFO] [1781609327.201050656] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781609327.291040761] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.80
[velocity_pid.py-9] [INFO] [1781609327.414076749] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0367s, resetting
[velocity_pid.py-9] [INFO] [1781609327.542440113] [velocity_pid]: [vel_pid→] desired=0.21 actual=-0.05 corrected=0.22 err=124.8%
[velocity_pid.py-9] [INFO] [1781609328.077972245] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.00 -> current=0.12 dt=0.0331s, resetting
[competition_master_stage3.py-19] [INFO] [1781609328.163374935] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.30,-1.03) yaw=164deg cmd=(vx=0.50 wz=0.15) elapsed=80.8s plan[20pts 2.6m] (0.30,-1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=50% mem=19%
[velocity_pid.py-9] [INFO] [1781609328.576749255] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.03 -> current=-0.09 dt=0.0333s, resetting
[component_container_isolated-18] [WARN] [1781609329.098697691] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2563 Hz
[component_container_isolated-18] [INFO] [1781609329.311586963] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1781609330.161308473] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.52,-0.76) yaw=144deg cmd=(vx=0.50 wz=-0.23) elapsed=82.8s plan[18pts 2.3m] (-0.10,-0.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=78% mem=19%
[velocity_pid.py-9] [INFO] [1781609330.376845252] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.51 corrected=-0.02 err=24.4%
[cmd_vel_mux.py-8] [INFO] [1781609330.392677049] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.30
[velocity_pid.py-9] [INFO] [1781609330.608949120] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0326s, resetting
[component_container_isolated-18] [WARN] [1781609331.096819534] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4406 Hz
[component_container_isolated-18] [INFO] [1781609331.301007565] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781609331.391008472] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.18
[velocity_pid.py-9] [INFO] [1781609331.410693938] [velocity_pid]: [vel_pid→] desired=-0.12 actual=-0.09 corrected=-0.04 err=29.2%
[velocity_pid.py-9] [INFO] [1781609331.508277014] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0338s, resetting
[competition_master_stage3.py-19] [INFO] [1781609332.162100795] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.78,-0.52) yaw=137deg cmd=(vx=0.50 wz=-0.69) elapsed=84.8s plan[10pts 1.3m] (-0.90,-0.35)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=50% mem=19%
[velocity_pid.py-9] [INFO] [1781609332.412640142] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.28 corrected=0.35 err=43.8%
[velocity_pid.py-9] [INFO] [1781609332.780888952] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.02 -> current=0.10 dt=0.0328s, resetting
[component_container_isolated-18] [WARN] [1781609333.090744283] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2786 Hz
[component_container_isolated-18] [INFO] [1781609333.201023787] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-4] [INFO] [1781609333.669956441] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2168 q_w=0.5567 angle=112.3deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781609333.689514366] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5807 q_w=0.3682 angle=136.8deg beta=0.0030
[competition_master_stage3.py-19] [INFO] [1781609334.158558607] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.23,-0.03) yaw=148deg cmd=(vx=0.50 wz=0.73) elapsed=86.8s plan[9pts 1.1m] (-1.00,-0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=43% mem=19%
[velocity_pid.py-9] [INFO] [1781609334.479997584] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.52 corrected=0.00 err=26.1%
[cmd_vel_mux.py-8] [INFO] [1781609334.491916423] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.13
[velocity_pid.py-9] [INFO] [1781609334.608628641] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.01 -> current=-0.12 dt=0.0339s, resetting
[velocity_pid.py-9] [INFO] [1781609334.708353477] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0338s, resetting
[component_container_isolated-18] [INFO] [1781609334.903264981] [controller_server]: Reached the goal!
[cmd_vel_mux.py-8] [INFO] [1781609334.993721313] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.41
[component_container_isolated-18] [WARN] [1781609335.120854998] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2205 Hz
[component_container_isolated-18] [INFO] [1781609335.400306089] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-19] [INFO] [1781609335.406774550] [competition_master_stage3]: [结果回调] 已回到P点, 任务完成!
[competition_master_stage3.py-19] [INFO] [1781609335.410659219] [competition_master_stage3]: [状态机] RETURN_P → DONE
[competition_master_stage3.py-19] [INFO] [1781609335.413681387] [competition_master_stage3]:
[competition_master_stage3.py-19] [INFO] [1781609335.417062805] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1781609335.421544516] [competition_master_stage3]: >>> [Stage 3] 任务结束 <<<
[competition_master_stage3.py-19] [INFO] [1781609335.424422684] [competition_master_stage3]:   最终状态: DONE
[competition_master_stage3.py-19] [INFO] [1781609335.428493686] [competition_master_stage3]:   总耗时:   88.1s
[competition_master_stage3.py-19] [INFO] [1781609335.434068105] [competition_master_stage3]:   --- 各阶段耗时 ---
[competition_master_stage3.py-19] [INFO] [1781609335.438612815] [competition_master_stage3]:   LAUNCH................ 15.2s
[competition_master_stage3.py-19] [INFO] [1781609335.442025942] [competition_master_stage3]:   NAV_TO_QR............. 11.8s
[competition_master_stage3.py-19] [INFO] [1781609335.444927485] [competition_master_stage3]:   BACKING_UP............ 6.0s
[competition_master_stage3.py-19] [INFO] [1781609335.448548028] [competition_master_stage3]:   CRUISE_CHANNEL........ 33.8s
[competition_master_stage3.py-19] [INFO] [1781609335.452093322] [competition_master_stage3]:   RETURN_P.............. 36.4s
[competition_master_stage3.py-19] [INFO] [1781609335.454784490] [competition_master_stage3]:   (transition/overhead). -15.2s
[competition_master_stage3.py-19] [INFO] [1781609335.457215241] [competition_master_stage3]:   --- ---
[competition_master_stage3.py-19] [INFO] [1781609335.459984450] [competition_master_stage3]:   QR 原始数据: 1584
[competition_master_stage3.py-19] [INFO] [1781609335.462715077] [competition_master_stage3]:   QR 方向:   逆时针 (CW=顺时针/odd, CCW=逆时针/even)
[competition_master_stage3.py-19] [INFO] [1781609335.465680328] [competition_master_stage3]:   VLM 结果:  这张图片展现了一个**昏暗的室内角落**，整体氛围静谧简约：
[competition_master_stage3.py-19]
[competition_master_stage3.py-19] ### 场景与背景
[competition_master_stage3.py-19] - **墙面**：浅灰色（或米白色）的拼接板材/瓷砖，水平拼接缝清晰，风格简洁朴素。
[competition_master_stage3.py-19] - **平面（桌面/地板）**：浅绿色的光滑表面（疑似桌面或地板），色调柔和。
[competition_master_stage3.py-19] - **右侧物件**：一个**深色（近黑色/深蓝色）的大型家具**（如柜子、冰箱），底部露出金属支撑脚，显得厚重规整。
[competition_master_stage3.py-19]
[competition_master_stage3.py-19]
[competition_master_stage3.py-19] ###
[competition_master_stage3.py-19] [INFO] [1781609335.468765871] [competition_master_stage3]:   超时限制:  180.0s (全局)
[competition_master_stage3.py-19] [INFO] [1781609335.472156456] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1781609335.477774167] [competition_master_stage3]: [TRAJ] 轨迹已保存: /userdata/dev_ws/trajectory.csv (104 点)
[competition_master_stage3.py-19] [INFO] [1781609336.155610160] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.95,-0.09) yaw=-163deg cmd=(vx=0.00 wz=0.00) elapsed=88.8s plan[4pts 0.5m] (-1.90,-0.05)→(-1.99,0.14) cpuFreq=1500MHz cpuT=71C cpu=20% mem=19%
[cmd_vel_mux.py-8] [INFO] [1781609336.391167987] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.51s > 0.5s, marked inactive
[competition_master_stage3.py-19] [INFO] [1781609338.157131079] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.95,-0.09) yaw=-163deg cmd=(vx=0.00 wz=0.00) elapsed=90.8s plan[4pts 0.5m] (-1.90,-0.05)→(-1.99,0.14) cpuFreq=1500MHz cpuT=71C cpu=25% mem=19%
[competition_master_stage3.py-19] [INFO] [1781609340.158392861] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.95,-0.09) yaw=-163deg cmd=(vx=0.00 wz=0.00) elapsed=92.8s plan[4pts 0.5m] (-1.90,-0.05)→(-1.99,0.14) cpuFreq=1500MHz cpuT=71C cpu=43% mem=19%
[competition_master_stage3.py-19] [INFO] [1781609342.161845550] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.95,-0.09) yaw=-163deg cmd=(vx=0.00 wz=0.00) elapsed=94.8s plan[4pts 0.5m] (-1.90,-0.05)→(-1.99,0.14) cpuFreq=1500MHz cpuT=71C cpu=75% mem=19%
[imu_madgwick_filter.py-4] [INFO] [1781609343.671180625] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2368 q_w=0.1652 angle=161.0deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781609343.690352680] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=6349 q_w=-0.0269 angle=183.1deg beta=0.0030
[competition_master_stage3.py-19] [INFO] [1781609344.160250263] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.95,-0.09) yaw=-163deg cmd=(vx=0.00 wz=0.00) elapsed=96.8s plan[4pts 0.5m] (-1.90,-0.05)→(-1.99,0.14) cpuFreq=1500MHz cpuT=71C cpu=57% mem=19%
[competition_master_stage3.py-19] [INFO] [1781609346.158548937] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.95,-0.09) yaw=-163deg cmd=(vx=0.00 wz=0.00) elapsed=98.8s plan[4pts 0.5m] (-1.90,-0.05)→(-1.99,0.14) cpuFreq=1500MHz cpuT=70C cpu=56% mem=19%
[competition_master_stage3.py-19] [INFO] [1781609348.158985486] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.95,-0.09) yaw=-163deg cmd=(vx=0.00 wz=0.00) elapsed=100.8s plan[4pts 0.5m] (-1.90,-0.05)→(-1.99,0.14) cpuFreq=1500MHz cpuT=70C cpu=64% mem=19%
[competition_master_stage3.py-19] [INFO] [1781609350.159684439] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.95,-0.09) yaw=-163deg cmd=(vx=0.00 wz=0.00) elapsed=102.8s plan[4pts 0.5m] (-1.90,-0.05)→(-1.99,0.14) cpuFreq=1500MHz cpuT=71C cpu=33% mem=19%
[competition_master_stage3.py-19] [INFO] [1781609352.159382405] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.95,-0.09) yaw=-163deg cmd=(vx=0.00 wz=0.00) elapsed=104.8s plan[4pts 0.5m] (-1.90,-0.05)→(-1.99,0.14) cpuFreq=1500MHz cpuT=71C cpu=33% mem=19%
[imu_madgwick_filter.py-4] [INFO] [1781609353.669987062] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2568 q_w=0.1791 angle=159.4deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781609353.690471236] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=6902 q_w=-0.0263 angle=183.0deg beta=0.0030
[competition_master_stage3.py-19] [INFO] [1781609354.159310018] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.95,-0.09) yaw=-163deg cmd=(vx=0.00 wz=0.00) elapsed=106.8s plan[4pts 0.5m] (-1.90,-0.05)→(-1.99,0.14) cpuFreq=1500MHz cpuT=71C cpu=43% mem=19%
[competition_master_stage3.py-19] [INFO] [1781609356.159318195] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.95,-0.09) yaw=-163deg cmd=(vx=0.00 wz=0.00) elapsed=108.8s plan[4pts 0.5m] (-1.90,-0.05)→(-1.99,0.14) cpuFreq=1500MHz cpuT=71C cpu=75% mem=19%
[competition_master_stage3.py-19] [INFO] [1781609358.158902069] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.95,-0.09) yaw=-163deg cmd=(vx=0.00 wz=0.00) elapsed=110.8s plan[4pts 0.5m] (-1.90,-0.05)→(-1.99,0.14) cpuFreq=1500MHz cpuT=71C cpu=50% mem=19%
[competition_master_stage3.py-19] [INFO] [1781609360.158937574] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.95,-0.09) yaw=-163deg cmd=(vx=0.00 wz=0.00) elapsed=112.8s plan[4pts 0.5m] (-1.90,-0.05)→(-1.99,0.14) cpuFreq=1500MHz cpuT=71C cpu=20% mem=19%
^C[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[robot_state_publisher-3] [INFO] [1781609360.725025141] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [lslidar_driver_node-2]: process has died [pid 12844, exit code -6, cmd '/userdata/dev_ws/install/lslidar_driver/lib/lslidar_driver/lslidar_driver_node --ros-args -r __node:=lslidar_driver_node --params-file /userdata/dev_ws/install/lslidar_driver/share/lslidar_driver/params/lsx10.yaml'].
[ERROR] [origincar_base_node-1]: process has died [pid 12842, exit code -6, cmd '/userdata/dev_ws/install/origincar_base/lib/origincar_base/origincar_base_node --ros-args --params-file /tmp/launch_params_b9d_zggo --params-file /tmp/launch_params_jlc2fk3b'].
[ERROR] [rviz2-20]: process has died [pid 13195, exit code -11, cmd '/opt/ros/humble/lib/rviz2/rviz2 -d /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/rviz/nav.rviz --ros-args -r __node:=rviz2'].
[INFO] [cmd_vel_mux.py-8]: process has finished cleanly [pid 12856]
[INFO] [map_server-15]: process has finished cleanly [pid 12989]
[INFO] [lifecycle_manager-17]: process has finished cleanly [pid 13004]
[INFO] [imu_madgwick_filter.py-6]: process has finished cleanly [pid 12852]
[INFO] [costmap_filter_info_server-16]: process has finished cleanly [pid 12993]
[INFO] [velocity_pid.py-9]: process has finished cleanly [pid 12858]
[INFO] [static_transform_publisher-10]: process has finished cleanly [pid 12898]
[INFO] [bmi088_iio_bridge.py-5]: process has finished cleanly [pid 12850]
[ERROR] [imu_madgwick_filter.py-4]: process has died [pid 12848, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/imu_madgwick_filter.py --ros-args -r __node:=imu_madgwick_filter --params-file /userdata/dev_ws/install/origincar_base/share/origincar_base/config/imu_madgwick.yaml'].
[INFO] [robot_state_publisher-3]: process has finished cleanly [pid 12846]
[INFO] [competition_master_stage3.py-19]: process has finished cleanly [pid 13191]
[INFO] [ekf_node-7]: process has finished cleanly [pid 12854]
[map_server-15] [INFO] [1781609360.725123305] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-15] [INFO] [1781609360.725356841] [keepout_mask_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_mask_server)
[map_server-15] [INFO] [1781609360.725634460] [keepout_mask_server]: Deactivating
[map_server-15] [INFO] [1781609360.725726083] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[map_server-15] [INFO] [1781609360.739412222] [keepout_mask_server]: Cleaning up
[map_server-15] [INFO] [1781609360.739685258] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[lifecycle_manager-17] [INFO] [1781609360.725196137] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-17] [INFO] [1781609360.725422798] [lifecycle_manager_keepout]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_keepout)
[lifecycle_manager-17] [INFO] [1781609360.725557462] [lifecycle_manager_keepout]: Terminating bond timer...
[lifecycle_manager-17] [INFO] [1781609360.904710039] [lifecycle_manager_keepout]: Destroying lifecycle_manager_keepout
[rviz2-20] [INFO] [1781609360.725739082] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[aurora930_node-11] [INFO] [1781609360.727010094] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[aurora930_node-11] I0616 19:29:20.758960 12900 ros2_node.cc:90] process quit succeed
[aurora930_node-11] I0616 19:29:20.759145 12900 aurora900_ros2_device.cc:83] begin stop()
[aurora930_node-11] I0616 19:29:20.844194 12900 aurora900_ros2_device.cc:103] stop stream
[aurora930_node-11] 2026-06-16 19:29:20.886 ( 138.862s) [        85BA4020]      aurora900_impl.cc:648   INFO| ir_stream_count_=0, rgb_stream_count_=0, depth_stream_count_=0
[aurora930_node-11] 2026-06-16 19:29:20.886 ( 138.862s) [        85BA4020]      aurora900_impl.cc:649   INFO| mask=7
[aurora930_node-11] I0616 19:29:21.117408 12900 aurora900_ros2_device.cc:105] destroy stream
[aurora930_node-11] I0616 19:29:21.117684 12900 aurora900_ros2_device.cc:110] close glog
[aurora930_node-11] WARNING: Logging before InitGoogleLogging() is written to STDERR
[aurora930_node-11] I0616 19:29:21.117930 12900 ros2_device.cc:113] close device...
[aurora930_node-11] 2026-06-16 19:29:21.617 ( 139.594s) [        660D47E0]         cmd_backend.cc:40    INFO| RunBlocking is end!!!
[aurora930_node-11] 2026-06-16 19:29:21.818 ( 139.795s) [        85BA4020]deptrum_camera_vendor.c:121   INFO| device is close.
[aurora930_node-11] I0616 19:29:21.820324 12900 ros2_device.cc:116] quit succeed
[static_transform_publisher-10] [INFO] [1781609360.727250297] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-16] [INFO] [1781609360.728507851] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-16] [INFO] [1781609360.728767928] [keepout_filter_info_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_filter_info_server)
[costmap_filter_info_server-16] [INFO] [1781609360.729065505] [keepout_filter_info_server]: Deactivating
[costmap_filter_info_server-16] [INFO] [1781609360.729166252] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-16] [INFO] [1781609360.747708987] [keepout_filter_info_server]: Cleaning up
[costmap_filter_info_server-16] [INFO] [1781609360.761259130] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-16] [INFO] [1781609360.872062008] [keepout_filter_info_server]: Destroying
[component_container_isolated-18] [INFO] [1781609360.726339110] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-18] [INFO] [1781609360.729021256] [velocity_smoother]: Running Nav2 LifecycleNode rcl preshutdown (velocity_smoother)
[component_container_isolated-18] [INFO] [1781609360.734996117] [velocity_smoother]: Deactivating
[component_container_isolated-18] [INFO] [1781609360.754570161] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609360.922948281] [velocity_smoother]: Cleaning up
[component_container_isolated-18] [INFO] [1781609360.923243274] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609360.923354938] [behavior_server]: Running Nav2 LifecycleNode rcl preshutdown (behavior_server)
[component_container_isolated-18] [INFO] [1781609360.923481435] [behavior_server]: Deactivating
[component_container_isolated-18] [INFO] [1781609360.923596391] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609360.981508084] [local_costmap.local_costmap]: Message Filter dropping message: frame 'laser_link' at time 1781609360.678 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-18] [INFO] [1781609361.005754019] [lifecycle_manager_navigation]: Have not received a heartbeat from velocity_smoother.
[component_container_isolated-18] [ERROR] [1781609361.005991389] [lifecycle_manager_navigation]: CRITICAL FAILURE: SERVER velocity_smoother IS DOWN after not receiving a heartbeat for 4000 ms. Shutting down related nodes.
[component_container_isolated-18] [INFO] [1781609361.006369297] [lifecycle_manager_navigation]: Terminating bond timer...
[component_container_isolated-18] [INFO] [1781609361.006492127] [lifecycle_manager_navigation]: Resetting managed nodes...
[component_container_isolated-18] [INFO] [1781609361.006567834] [lifecycle_manager_navigation]: Deactivating velocity_smoother
[component_container_isolated-18] [WARN] [1781609361.008595495] [rcl_lifecycle]: No transition matching 4 found for current state unconfigured
[component_container_isolated-18] [WARN] [1781609361.008683118] [rcl_lifecycle]: No transition matching 4 found for current state unconfigured
[component_container_isolated-18] [ERROR] [1781609361.008732700] [velocity_smoother]: Unable to start transition 4 from current state unconfigured: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-18] [ERROR] [1781609361.010564741] [lifecycle_manager_navigation]: Failed to change state for node: velocity_smoother
[component_container_isolated-18] [INFO] [1781609361.010791611] [lifecycle_manager_navigation]: Deactivating waypoint_follower
[component_container_isolated-18] [INFO] [1781609361.012225036] [waypoint_follower]: Deactivating
[component_container_isolated-18] [INFO] [1781609361.012478530] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609361.024643373] [behavior_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781609361.077084616] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609361.077247029] [lifecycle_manager_localization]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_localization)
[component_container_isolated-18] [INFO] [1781609361.077697310] [lifecycle_manager_localization]: Terminating bond timer...
[component_container_isolated-18] [INFO] [1781609361.139164218] [bt_navigator]: Running Nav2 LifecycleNode rcl preshutdown (bt_navigator)
[component_container_isolated-18] [INFO] [1781609361.139427462] [bt_navigator]: Deactivating
[component_container_isolated-18] [INFO] [1781609361.139620624] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609361.153719589] [lifecycle_manager_navigation]: Deactivating bt_navigator
[component_container_isolated-18] [INFO] [1781609361.155065183] [bt_navigator]: Cleaning up
[component_container_isolated-18] [WARN] [1781609361.240203918] [rcl_lifecycle]: No transition matching 4 found for current state cleaningup
[component_container_isolated-18] [WARN] [1781609361.240292957] [rcl_lifecycle]: No transition matching 4 found for current state cleaningup
[component_container_isolated-18] [ERROR] [1781609361.240327957] [bt_navigator]: Unable to start transition 4 from current state cleaningup: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-18] [ERROR] [1781609361.242986812] [lifecycle_manager_navigation]: Failed to change state for node: bt_navigator
[component_container_isolated-18] [INFO] [1781609361.243242764] [lifecycle_manager_navigation]: Deactivating behavior_server
[component_container_isolated-18] [WARN] [1781609361.276092794] [rcl_lifecycle]: No transition matching 4 found for current state unconfigured
[component_container_isolated-18] [WARN] [1781609361.276183000] [rcl_lifecycle]: No transition matching 4 found for current state unconfigured
[component_container_isolated-18] [ERROR] [1781609361.276224291] [behavior_server]: Unable to start transition 4 from current state unconfigured: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-18] [ERROR] [1781609361.279009643] [lifecycle_manager_navigation]: Failed to change state for node: behavior_server
[component_container_isolated-18] [INFO] [1781609361.279237929] [lifecycle_manager_navigation]: Deactivating planner_server
[component_container_isolated-18] [INFO] [1781609361.281316881] [planner_server]: Deactivating
[component_container_isolated-18] [INFO] [1781609361.281629249] [global_costmap.global_costmap]: Deactivating
[component_container_isolated-18] [INFO] [1781609361.627653311] [bt_navigator]: Completed Cleaning up
[component_container_isolated-18] [INFO] [1781609361.627867264] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609361.627930804] [planner_server]: Running Nav2 LifecycleNode rcl preshutdown (planner_server)
[component_container_isolated-18] [INFO] [1781609361.627996928] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609361.680148511] [amcl]: Message Filter dropping message: frame 'laser_link' at time 1781609360.678 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-18] [INFO] [1781609361.733239196] [lifecycle_manager_navigation]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_navigation)
[component_container_isolated-18] [INFO] [1781609362.083342130] [planner_server]: Deactivating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781609362.083693164] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609362.095274272] [lifecycle_manager_navigation]: Deactivating smoother_server
[component_container_isolated-18] [INFO] [1781609362.096334997] [smoother_server]: Deactivating
[component_container_isolated-18] [INFO] [1781609362.096484827] [smoother_server]: Deactivating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781609362.096649032] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609362.222579709] [lifecycle_manager_navigation]: Deactivating controller_server
[component_container_isolated-18] [INFO] [1781609362.223716350] [controller_server]: Deactivating
[component_container_isolated-18] [INFO] [1781609362.223878596] [controller_server]: Deactivating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781609362.224135965] [local_costmap.local_costmap]: Deactivating
[component_container_isolated-18] [INFO] [1781609362.330945000] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609362.445504857] [lifecycle_manager_navigation]: Cleaning up velocity_smoother
[component_container_isolated-18] [WARN] [1781609362.446564124] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-18] [WARN] [1781609362.446645747] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-18] [ERROR] [1781609362.446674830] [velocity_smoother]: Unable to start transition 2 from current state unconfigured: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-18] [INFO] [1781609362.447792762] [lifecycle_manager_navigation]: Cleaning up waypoint_follower
[component_container_isolated-18] [INFO] [1781609362.448438997] [waypoint_follower]: Cleaning up
[component_container_isolated-18] [INFO] [1781609362.468851068] [lifecycle_manager_navigation]: Cleaning up bt_navigator
[component_container_isolated-18] [WARN] [1781609362.492140114] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-18] [WARN] [1781609362.492240320] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-18] [ERROR] [1781609362.492270111] [bt_navigator]: Unable to start transition 2 from current state unconfigured: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-18] [INFO] [1781609362.493454250] [lifecycle_manager_navigation]: Cleaning up behavior_server
[component_container_isolated-18] [WARN] [1781609362.494119818] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-18] [WARN] [1781609362.494191400] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-18] [ERROR] [1781609362.494220816] [behavior_server]: Unable to start transition 2 from current state unconfigured: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-18] [INFO] [1781609362.495177669] [lifecycle_manager_navigation]: Cleaning up planner_server
[component_container_isolated-18] [INFO] [1781609362.495820196] [planner_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781609362.518486381] [global_costmap.global_costmap]: Cleaning up
[component_container_isolated-18] [INFO] [1781609362.525809879] [planner_server]: Cleaning up plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781609362.534134312] [planner_server]: Destroying plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781609362.554745044] [lifecycle_manager_navigation]: Cleaning up smoother_server
[component_container_isolated-18] [INFO] [1781609362.555350655] [smoother_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781609362.555451361] [smoother_server]: Cleaning up smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781609362.574989786] [lifecycle_manager_navigation]: Cleaning up controller_server
[component_container_isolated-18] [INFO] [1781609362.575562147] [controller_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781609362.575666103] [controller_server]: Cleaning up controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781609362.579292561] [local_costmap.local_costmap]: Cleaning up
[origincar_base_node-1] [INFO] [1781609360.744764389] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1781609360.745206504] [origincar_base]: Stop command sent to STM32 on shutdown.
[origincar_base_node-1] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[origincar_base_node-1] terminate called after throwing an instance of 'rclcpp::exceptions::RCLError'
[origincar_base_node-1]   what():  failed to create guard condition: the given context is not valid, either rcl_init() was not called or rcl_shutdown() was called., at ./src/rcl/guard_condition.c:67
[ekf_node-7] [INFO] [1781609360.764516471] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-15] [INFO] [1781609360.782551676] [keepout_mask_server]: Destroying
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
[ERROR] [vision_ai_node-14]: process has died [pid 12908, exit code 1, cmd '/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node --ros-args -r __node:=vision_ai_node'].
[INFO] [aurora930_node-11]: process has finished cleanly [pid 12900]
[component_container_isolated-18] [INFO] [1781609363.629901051] [lifecycle_manager_navigation]: Managed nodes have been reset
[component_container_isolated-18] [INFO] [1781609363.700579303] [waypoint_follower]: Running Nav2 LifecycleNode rcl preshutdown (waypoint_follower)
[component_container_isolated-18] [INFO] [1781609363.700734341] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609363.700790340] [amcl]: Running Nav2 LifecycleNode rcl preshutdown (amcl)
[component_container_isolated-18] [INFO] [1781609363.700901879] [amcl]: Deactivating
[component_container_isolated-18] [INFO] [1781609363.701038626] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609363.711370722] [amcl]: Cleaning up
[component_container_isolated-18] [INFO] [1781609363.727187233] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609363.727338272] [smoother_server]: Running Nav2 LifecycleNode rcl preshutdown (smoother_server)
[component_container_isolated-18] [INFO] [1781609363.727453852] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609363.727515393] [map_server]: Running Nav2 LifecycleNode rcl preshutdown (map_server)
[component_container_isolated-18] [INFO] [1781609363.727660764] [map_server]: Deactivating
[component_container_isolated-18] [INFO] [1781609363.727784428] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609363.738206814] [map_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781609363.738513307] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781609363.738642429] [controller_server]: Running Nav2 LifecycleNode rcl preshutdown (controller_server)
[component_container_isolated-18] [INFO] [1781609363.738784842] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[ERROR] [component_container_isolated-18]: process[component_container_isolated-18] failed to terminate '5' seconds after receiving 'SIGINT', escalating to 'SIGTERM'
[INFO] [component_container_isolated-18]: sending signal 'SIGTERM' to process[component_container_isolated-18]
[component_container_isolated-18] [INFO] [1781609367.768851149] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [component_container_isolated-18]: process[component_container_isolated-18] failed to terminate '10.0' seconds after receiving 'SIGTERM', escalating to 'SIGKILL'
[INFO] [component_container_isolated-18]: sending signal 'SIGKILL' to process[component_container_isolated-18]
[ERROR] [component_container_isolated-18]: process has died [pid 13189, exit code -9, cmd '/opt/ros/humble/lib/rclcpp_components/component_container_isolated --ros-args --log-level info --ros-args -r __node:=nav2_container --params-file /tmp/launch_params_48c2im0g --params-file /tmp/launch_params_svls2rl9 -r /tf:=tf -r /tf_static:=tf_static'].
root@ubuntu:/userdata/dev_ws#
