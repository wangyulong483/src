root@ubuntu:/userdata/dev_ws# ros2 launch origincar_bringup stage3_bringup.launch.py
[INFO] [launch]: All log files can be found below /root/.ros/log/2026-06-15-11-03-32-172810-ubuntu-32530
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [origincar_base_node-1]: process started with pid [32552]
[INFO] [lslidar_driver_node-2]: process started with pid [32554]
[INFO] [robot_state_publisher-3]: process started with pid [32556]
[INFO] [imu_madgwick_filter.py-4]: process started with pid [32558]
[INFO] [bmi088_iio_bridge.py-5]: process started with pid [32560]
[INFO] [imu_madgwick_filter.py-6]: process started with pid [32562]
[INFO] [ekf_node-7]: process started with pid [32564]
[INFO] [cmd_vel_mux.py-8]: process started with pid [32570]
[INFO] [velocity_pid.py-9]: process started with pid [32588]
[INFO] [static_transform_publisher-10]: process started with pid [32614]
[INFO] [aurora930_node-11]: process started with pid [32616]
[INFO] [qr_decoder-12]: process started with pid [32618]
[INFO] [qr_decision-13]: process started with pid [32622]
[INFO] [vision_ai_node-14]: process started with pid [32631]
[origincar_base_node-1] [INFO] [1781492612.923585024] [origincar_base]: origincar_base serial port opened
[lslidar_driver_node-2] [INFO] [1781492612.883316185] [lslidar_driver_node]: Lidar is N10
[lslidar_driver_node-2] [INFO] [1781492612.891883153] [lslidar_driver_node]: Initialised lslidar without error
[lslidar_driver_node-2] [INFO] [1781492612.892060028] [lslidar_driver_node]: Successfully initialize driver...
[robot_state_publisher-3] [INFO] [1781492612.934922495] [robot_state_publisher]: got segment base_footprint
[robot_state_publisher-3] [INFO] [1781492612.935785579] [robot_state_publisher]: got segment base_link
[robot_state_publisher-3] [INFO] [1781492612.935909955] [robot_state_publisher]: got segment gyro_link
[robot_state_publisher-3] [INFO] [1781492612.935962955] [robot_state_publisher]: got segment laser_link
[ekf_node-7] Both imu1_differential and imu1_relative were set to true. Using differential mode.
[static_transform_publisher-10] [INFO] [1781492613.176789236] [depth_camera_tf]: Spinning until stopped - publishing transform
[static_transform_publisher-10] translation: ('0.140000', '0.000000', '0.050000')
[static_transform_publisher-10] rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
[static_transform_publisher-10] from 'base_link' to 'depth_camera_link'
[qr_decoder-12] [INFO] [1781492613.961352650] [qr_decoder_zbar]: QR decoder (ZBar) started: rgb=/aurora/rgb/image_raw, depth=/aurora/depth/image_raw, filter=on, range=[50, 4000]mm, min_qr_len=1, intrinsics: fx=421.3 fy=422.3 cx=320.3 cy=197.0
[aurora930_node-11] W0615 11:03:34.004536 32616 ros2_node.cc:35] hello aurora 900/930
[aurora930_node-11] 2026-06-15 11:03:34.156 (   0.373s) [        ACFD4020] device_manager_impl.cc:89    INFO| hotplug has registed by user
[aurora930_node-11] I0615 11:03:34.191356 32616 aurora900_ros2_device.cc:153] BOOT_ORDER_1::Found 1 deptrum device
[aurora930_node-11] I0615 11:03:34.191926 32616 aurora900_ros2_device.cc:162] BOOT_ORDER_1::No serial number provided: picking first device
[aurora930_node-11] 2026-06-15 11:03:34.192 (   0.409s) [        ACFD4020] device_manager_impl.cc:318   INFO| Device information:
[aurora930_node-11]     ir_pid:0x1930, rgb_pid:0x0
[aurora930_node-11]     serial number:HY400529001015314G00248
[aurora930_node-11] I0615 11:03:34.192119 32616 aurora900_ros2_device.cc:206] BOOT_ORDER_1::0:device start opening
[aurora930_node-11] 2026-06-15 11:03:34.196 (   0.413s) [        ACFD4020]   custom_usb_device.cc:101   INFO| bulk in endpoint addr:129
[aurora930_node-11] 2026-06-15 11:03:34.196 (   0.413s) [        ACFD4020]   custom_usb_device.cc:98    INFO| bulk out endpoint addr:2
[aurora930_node-11] 2026-06-15 11:03:34.203 (   0.421s) [        ACFD4020]deptrum_camera_aurora93:53    INFO| doe_broken:0 ito_support:1 crash_count:0 wdt_count:0 hard_reset_count:2 heart_boot_count:0 boot_total:97 last_crash_time:N
[aurora930_node-11] I0615 11:03:34.203716 32616 aurora900_ros2_device.cc:247] device supported frame_mode:
[aurora930_node-11] I0615 11:03:34.203838 32616 aurora900_ros2_device.cc:252] [0]:ir_mode:=13 kRes320x200Ir8Bit rgb_mode:=31 kRes320x200RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0615 11:03:34.203888 32616 aurora900_ros2_device.cc:252] [1]:ir_mode:=17 kRes480x300Depth16Bit rgb_mode:=32 kRes480x300RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0615 11:03:34.203924 32616 aurora900_ros2_device.cc:252] [2]:ir_mode:=20 kRes640x400Ir8Bit rgb_mode:=33 kRes640x400RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0615 11:03:34.203956 32616 aurora900_ros2_device.cc:266] current set mode ir_mode:20:kRes640x400Ir8Bit,rgb_mode:33:kRes640x400RgbYuv
[INFO] [map_server-15]: process started with pid [32732]
[INFO] [costmap_filter_info_server-16]: process started with pid [32735]
[INFO] [lifecycle_manager-17]: process started with pid [32737]
[aurora930_node-11] device_count==========1
[lifecycle_manager-17] [INFO] [1781492614.438156247] [lifecycle_manager_keepout]: Creating
[costmap_filter_info_server-16] [INFO] [1781492614.452789972] [costmap_filter_info_server]: This is costmap filter info publisher
[lifecycle_manager-17] [INFO] [1781492614.478483335] [lifecycle_manager_keepout]: Creating and initializing lifecycle service clients
[map_server-15] [INFO] [1781492614.549064459] [keepout_mask_server]:
[map_server-15]         keepout_mask_server lifecycle node launched.
[map_server-15]         Waiting on external lifecycle transitions to activate
[map_server-15]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[map_server-15] [INFO] [1781492614.549611543] [keepout_mask_server]: Creating
[costmap_filter_info_server-16] [INFO] [1781492614.691438875] [keepout_filter_info_server]:
[costmap_filter_info_server-16]         keepout_filter_info_server lifecycle node launched.
[costmap_filter_info_server-16]         Waiting on external lifecycle transitions to activate
[costmap_filter_info_server-16]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[aurora930_node-11] I0615 11:03:34.721696 32616 aurora900_ros2_device.cc:387] Switch Auto Exposure
[lifecycle_manager-17] [INFO] [1781492614.752271071] [lifecycle_manager_keepout]: Starting managed nodes bringup...
[lifecycle_manager-17] [INFO] [1781492614.759116079] [lifecycle_manager_keepout]: Configuring keepout_mask_server
[map_server-15] [INFO] [1781492614.763793251] [keepout_mask_server]: Configuring
[map_server-15] [INFO] [1781492614.764064918] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.yaml
[map_server-15] [INFO] [1781492614.765159586] [map_io]: resolution: 0.05
[map_server-15] [INFO] [1781492614.765219544] [map_io]: origin[0]: -2.65
[map_server-15] [INFO] [1781492614.765248627] [map_io]: origin[1]: -4.5
[map_server-15] [INFO] [1781492614.765275836] [map_io]: origin[2]: 0
[map_server-15] [INFO] [1781492614.765303544] [map_io]: free_thresh: 0.5
[map_server-15] [INFO] [1781492614.765331961] [map_io]: occupied_thresh: 0.5
[map_server-15] [INFO] [1781492614.765363211] [map_io]: mode: scale
[map_server-15] [INFO] [1781492614.765392044] [map_io]: negate: 0
[map_server-15] [INFO] [1781492614.766061045] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm
[aurora930_node-11] 2026-06-15 11:03:34.782 (   0.999s) [        ACFD4020]      aurora900_impl.cc:1106  INFO| SetHeartbeat user set heartbeat enable: 0
[map_server-15] [INFO] [1781492614.800328710] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm: 163 X 141 map @ 0.05 m/cell
[lifecycle_manager-17] [INFO] [1781492614.844827928] [lifecycle_manager_keepout]: Configuring keepout_filter_info_server
[costmap_filter_info_server-16] [INFO] [1781492614.848335641] [keepout_filter_info_server]: Configuring
[lifecycle_manager-17] [INFO] [1781492614.872823669] [lifecycle_manager_keepout]: Activating keepout_mask_server
[map_server-15] [INFO] [1781492614.873772254] [keepout_mask_server]: Activating
[map_server-15] [INFO] [1781492614.874122296] [keepout_mask_server]: Creating bond (keepout_mask_server) to lifecycle manager.
[imu_madgwick_filter.py-4] [INFO] [1781492614.914561509] [imu_madgwick_filter]: [imu_madgwick] init: beta=0.0330, gyro_noise=0.0010, accel_noise=0.050
[imu_madgwick_filter.py-4] [INFO] [1781492614.924494479] [imu_madgwick_filter]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-4] [INFO] [1781492614.934477033] [imu_madgwick_filter]: [imu_madgwick] accel init: roll=0.1deg, pitch=0.3deg
[lifecycle_manager-17] [INFO] [1781492614.985087633] [lifecycle_manager_keepout]: Server keepout_mask_server connected with bond.
[lifecycle_manager-17] [INFO] [1781492614.985251175] [lifecycle_manager_keepout]: Activating keepout_filter_info_server
[costmap_filter_info_server-16] [INFO] [1781492614.986577510] [keepout_filter_info_server]: Activating
[costmap_filter_info_server-16] [INFO] [1781492614.987877178] [keepout_filter_info_server]: Creating bond (keepout_filter_info_server) to lifecycle manager.
[bmi088_iio_bridge.py-5] [INFO] [1781492615.086872001] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1781492615.089775463] [bmi088_iio_bridge]:   DIAGNOSTIC: Scanning IIO devices under /sys/bus/iio/devices/
[bmi088_iio_bridge.py-5] [INFO] [1781492615.092368008] [bmi088_iio_bridge]:   Equivalent to: ls /sys/bus/iio/devices/*/name
[imu_madgwick_filter.py-6] [INFO] [1781492615.093158842] [imu_madgwick_bmi088]: [imu_madgwick] init: beta=0.0030, gyro_noise=0.0002, accel_noise=0.010
[bmi088_iio_bridge.py-5] [INFO] [1781492615.094970177] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1781492615.097655722] [bmi088_iio_bridge]:   iio:device0/name = "34190000.adc"
[bmi088_iio_bridge.py-5] [INFO] [1781492615.100290267] [bmi088_iio_bridge]:   iio:device1/name = "bmi08x"
[bmi088_iio_bridge.py-5] [INFO] [1781492615.102962145] [bmi088_iio_bridge]:   trigger0/name = "34190000.adc-dev0"
[bmi088_iio_bridge.py-5] [INFO] [1781492615.105814732] [bmi088_iio_bridge]:   Total IIO devices found: 3
[lifecycle_manager-17] [INFO] [1781492615.103177229] [lifecycle_manager_keepout]: Server keepout_filter_info_server connected with bond.
[lifecycle_manager-17] [INFO] [1781492615.103343354] [lifecycle_manager_keepout]: Managed nodes are active
[lifecycle_manager-17] [INFO] [1781492615.103416646] [lifecycle_manager_keepout]: Creating bond timer...
[bmi088_iio_bridge.py-5] [INFO] [1781492615.108531402] [bmi088_iio_bridge]:   BMI088 kernel module APPEARS LOADED: 1 BMI device(s) detected
[bmi088_iio_bridge.py-5] [INFO] [1781492615.111025404] [bmi088_iio_bridge]:   BMI device names: ['bmi08x']
[bmi088_iio_bridge.py-5] [INFO] [1781492615.114253408] [bmi088_iio_bridge]:   gyro:  /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_anglvel is_si=False scale_override=0.00053
[bmi088_iio_bridge.py-5] [INFO] [1781492615.117480037] [bmi088_iio_bridge]:   accel: /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_accel is_si=False scale_override=0.00341
[aurora930_node-11] I0615 11:03:35.194751 32616 aurora900_ros2_device.cc:304] BOOT_ORDER_1::Device information:
[aurora930_node-11] I0615 11:03:35.194944 32616 aurora900_ros2_device.cc:305]    sdk version: 1.1.22
[aurora930_node-11] I0615 11:03:35.195034 32616 aurora900_ros2_device.cc:306]    device name: Aurora 930
[aurora930_node-11] I0615 11:03:35.195083 32616 aurora900_ros2_device.cc:307]    serial number: HY400529001015314G00248
[aurora930_node-11] I0615 11:03:35.195119 32616 aurora900_ros2_device.cc:308]    firmware version: 1.7.2
[aurora930_node-11] I0615 11:03:35.195181 32616 camera_parameters.cc:134] BOOT_ORDER_1::Camera Parameters:
[aurora930_node-11] I0615 11:03:35.195218 32616 camera_parameters.cc:135] BOOT_ORDER_1::         Ir Intrinsics:
[aurora930_node-11] I0615 11:03:35.195246 32616 camera_parameters.cc:146]                Resolution:
[aurora930_node-11] I0615 11:03:35.195273 32616 camera_parameters.cc:147]                        Rows:400
[aurora930_node-11] I0615 11:03:35.195310 32616 camera_parameters.cc:148]                        Cols:640
[aurora930_node-11] I0615 11:03:35.195338 32616 camera_parameters.cc:149]                Intrinsics:
[aurora930_node-11] I0615 11:03:35.195363 32616 camera_parameters.cc:150]                        fx: 421.307
[aurora930_node-11] I0615 11:03:35.195483 32616 camera_parameters.cc:151]                        fy: 422.254
[aurora930_node-11] I0615 11:03:35.195533 32616 camera_parameters.cc:152]                        cx: 320.27
[aurora930_node-11] I0615 11:03:35.195575 32616 camera_parameters.cc:153]                        cy: 197.01
[aurora930_node-11] I0615 11:03:35.195611 32616 camera_parameters.cc:154]                        k1: 0.0606853
[aurora930_node-11] I0615 11:03:35.195652 32616 camera_parameters.cc:155]                        k2: -0.10961
[aurora930_node-11] I0615 11:03:35.195685 32616 camera_parameters.cc:156]                        p1: 0.00126689
[aurora930_node-11] I0615 11:03:35.195719 32616 camera_parameters.cc:157]                        p2: -0.00120539
[aurora930_node-11] I0615 11:03:35.195766 32616 camera_parameters.cc:158]                        k3: 0.0522281
[aurora930_node-11] I0615 11:03:35.195807 32616 camera_parameters.cc:138] BOOT_ORDER_1::         Rgb Intrinsics:
[aurora930_node-11] I0615 11:03:35.195834 32616 camera_parameters.cc:146]                Resolution:
[aurora930_node-11] I0615 11:03:35.195860 32616 camera_parameters.cc:147]                        Rows:400
[aurora930_node-11] I0615 11:03:35.195885 32616 camera_parameters.cc:148]                        Cols:640
[aurora930_node-11] I0615 11:03:35.195911 32616 camera_parameters.cc:149]                Intrinsics:
[aurora930_node-11] I0615 11:03:35.195936 32616 camera_parameters.cc:150]                        fx: 416.49
[aurora930_node-11] I0615 11:03:35.195968 32616 camera_parameters.cc:151]                        fy: 417.383
[aurora930_node-11] I0615 11:03:35.196002 32616 camera_parameters.cc:152]                        cx: 316.832
[aurora930_node-11] I0615 11:03:35.196033 32616 camera_parameters.cc:153]                        cy: 188.753
[aurora930_node-11] I0615 11:03:35.196064 32616 camera_parameters.cc:154]                        k1: 0.00611878
[aurora930_node-11] I0615 11:03:35.196095 32616 camera_parameters.cc:155]                        k2: -0.0490436
[aurora930_node-11] I0615 11:03:35.196127 32616 camera_parameters.cc:156]                        p1: 0.000399548
[aurora930_node-11] I0615 11:03:35.196166 32616 camera_parameters.cc:157]                        p2: 0.000563892
[aurora930_node-11] I0615 11:03:35.196197 32616 camera_parameters.cc:158]                        k3: 0.0308458
[aurora930_node-11] I0615 11:03:35.196228 32616 camera_parameters.cc:141] BOOT_ORDER_1::         Ir to Rgb Extrinsic:
[aurora930_node-11] I0615 11:03:35.196261 32616 camera_parameters.cc:162]                Extrinsics:
[aurora930_node-11] I0615 11:03:35.196287 32616 camera_parameters.cc:163]                        Rotation[0]: 0.999973, 0.00724076, -0.00112023
[aurora930_node-11] I0615 11:03:35.196329 32616 camera_parameters.cc:165]                        Rotation[1]: -0.00724006, 0.999973, 0.000633162
[aurora930_node-11] I0615 11:03:35.196367 32616 camera_parameters.cc:167]                        Rotation[2]: 0.00112478, -0.000625033, 0.999999
[aurora930_node-11] I0615 11:03:35.196456 32616 camera_parameters.cc:169]                        Translation: -9.88662, 0.117748, 0.603513
[aurora930_node-11] 2026-06-15 11:03:35.197 (   1.414s) [        ACFD4020]      aurora900_impl.cc:578   INFO| stream_mask_:0, rgb_stream_count_:1
[bmi088_iio_bridge.py-5] [INFO] [1781492615.239033970] [bmi088_iio_bridge]: BMI088 IIO Bridge 启动 @ 100Hz -> /imu_data  [OK]
[velocity_pid.py-9] [INFO] [1781492615.260359370] [velocity_pid]: VelocityPID 就绪: vx(Kp=0.8, Ki=0.60, Kd=0.05, max_i=0.68) wz(Kp=1.0, Ki=0.40, Kd=0.02, max_i=2.24) | feedback_timeout=0.5s
[imu_madgwick_filter.py-6] [INFO] [1781492615.267631753] [imu_madgwick_bmi088]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-6] [INFO] [1781492615.270557631] [imu_madgwick_bmi088]: [imu_madgwick] accel init: roll=-2.0deg, pitch=-3.4deg
[cmd_vel_mux.py-8] [INFO] [1781492615.393665149] [cmd_vel_mux]:   nav: /nav_cmd_vel priority=10 timeout=0.5s
[cmd_vel_mux.py-8] [INFO] [1781492615.407095915] [cmd_vel_mux]:   pid: /pid_cmd_vel priority=20 timeout=0.3s
[cmd_vel_mux.py-8] [INFO] [1781492615.419553138] [cmd_vel_mux]:   stop: /stop_cmd_vel priority=255 timeout=0.5s
[cmd_vel_mux.py-8] [INFO] [1781492615.433977863] [cmd_vel_mux]: cmd_vel_mux 就绪: 输出 → /cmd_vel_muxed
[cmd_vel_mux.py-8] [INFO] [1781492615.468542945] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[qr_decision-13] [INFO] [1781492615.414469965] [qr_decision]: qr_decision started: cooldown=3.0s, awaiting /sign from qr_decoder
[velocity_pid.py-9] [INFO] [1781492615.470662822] [velocity_pid]: [vel_pid] ACTIVATED vx=0.00 wz=0.00
[INFO] [component_container_isolated-18]: process started with pid [32900]
[aurora930_node-11] 2026-06-15 11:03:35.536 (   1.754s) [        7D9E37E0]deptrum_camera_aurora93:407    ERR| recv first frame time is 1781492615536
[lslidar_driver_node-2] port = /dev/ttyACM1, baud_rate = 230400
[lslidar_driver_node-2] open_port /dev/ttyACM1 OK !
[vision_ai_node-14] [INFO] [1781492619.210354527] [vision_ai_node]: 成功加载配置文件: /userdata/dev_ws/install/racing_vision_ai/share/racing_vision_ai/config/vision_ai_config.yaml
[vision_ai_node-14] [INFO] [1781492619.585018042] [vision_ai_node]: Volcengine Ark client initialized successfully
[vision_ai_node-14] [INFO] [1781492619.603111938] [vision_ai_node]: Vision AI Node initialized
[vision_ai_node-14] [INFO] [1781492619.605592691] [vision_ai_node]: Waiting for sign4return=100 signal...
[vision_ai_node-14] [INFO] [1781492619.607894402] [vision_ai_node]: Results will be published to vlm_result
[bmi088_iio_bridge.py-5] [INFO] [1781492620.906174981] [bmi088_iio_bridge]:   gyro bias calibrated: (0.002756, 0.001299, -0.002613) rad/s
[INFO] [competition_master_stage3.py-19]: process started with pid [32908]
[INFO] [rviz2-20]: process started with pid [32912]
[component_container_isolated-18] [INFO] [1781492621.328493675] [nav2_container]: Load Library: /opt/ros/humble/lib/libcontroller_server_core.so
[component_container_isolated-18] [INFO] [1781492621.362343380] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-18] [INFO] [1781492621.362516839] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-18] [INFO] [1781492621.449752939] [controller_server]:
[component_container_isolated-18]       controller_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781492621.476509095] [controller_server]: Creating controller server
[component_container_isolated-18] [INFO] [1781492621.579700755] [local_costmap.local_costmap]:
[component_container_isolated-18]       local_costmap lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781492621.582736675] [local_costmap.local_costmap]: Creating Costmap
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/controller_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781492621.612654126] [nav2_container]: Load Library: /opt/ros/humble/lib/libmap_server_core.so
[component_container_isolated-18] [INFO] [1781492621.668381648] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::CostmapFilterInfoServer>
[component_container_isolated-18] [INFO] [1781492621.668600940] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapSaver>
[component_container_isolated-18] [INFO] [1781492621.668694982] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-18] [INFO] [1781492621.668760232] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-18] [INFO] [1781492621.738099895] [map_server]:
[component_container_isolated-18]       map_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/map_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781492621.738391312] [map_server]: Creating
[component_container_isolated-18] [INFO] [1781492621.744563403] [nav2_container]: Load Library: /opt/ros/humble/lib/libsmoother_server_core.so
[component_container_isolated-18] [INFO] [1781492621.750747160] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-18] [INFO] [1781492621.751043160] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-18] [INFO] [1781492621.821500199] [smoother_server]:
[component_container_isolated-18]       smoother_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781492621.833344380] [smoother_server]: Creating smoother server
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/smoother_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781492621.844229059] [nav2_container]: Load Library: /opt/ros/humble/lib/libamcl_core.so
[component_container_isolated-18] [INFO] [1781492621.855902072] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-18] [INFO] [1781492621.856167531] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-18] [INFO] [1781492621.949542638] [amcl]:
[component_container_isolated-18]       amcl lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781492621.951821557] [amcl]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/amcl' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781492622.000485280] [nav2_container]: Load Library: /opt/ros/humble/lib/libplanner_server_core.so
[component_container_isolated-18] [INFO] [1781492622.004079118] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-18] [INFO] [1781492622.004243201] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-18] [INFO] [1781492622.067439482] [planner_server]:
[component_container_isolated-18]       planner_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781492622.080048455] [planner_server]: Creating
[component_container_isolated-18] [INFO] [1781492622.184165032] [global_costmap.global_costmap]:
[component_container_isolated-18]       global_costmap lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781492622.186625702] [global_costmap.global_costmap]: Creating Costmap
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/planner_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781492622.218307572] [nav2_container]: Load Library: /opt/ros/humble/lib/libnav2_lifecycle_manager_core.so
[component_container_isolated-18] [INFO] [1781492622.221541617] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781492622.221710284] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781492622.312735597] [lifecycle_manager_localization]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_localization' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781492622.371731164] [lifecycle_manager_localization]: Creating and initializing lifecycle service clients
[component_container_isolated-18] [INFO] [1781492622.371892914] [nav2_container]: Load Library: /opt/ros/humble/lib/libbehavior_server_core.so
[component_container_isolated-18] [INFO] [1781492622.404551869] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-18] [INFO] [1781492622.404724660] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-18] [INFO] [1781492622.416524841] [lifecycle_manager_localization]: Starting managed nodes bringup...
[component_container_isolated-18] [INFO] [1781492622.418343343] [lifecycle_manager_localization]: Configuring map_server
[component_container_isolated-18] [INFO] [1781492622.422911348] [map_server]: Configuring
[component_container_isolated-18] [INFO] [1781492622.423255015] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.yaml
[component_container_isolated-18] [INFO] [1781492622.424478266] [map_io]: resolution: 0.05
[component_container_isolated-18] [INFO] [1781492622.424583933] [map_io]: origin[0]: -2.65
[component_container_isolated-18] [INFO] [1781492622.424615600] [map_io]: origin[1]: -4.5
[component_container_isolated-18] [INFO] [1781492622.424642808] [map_io]: origin[2]: 0
[component_container_isolated-18] [INFO] [1781492622.424671767] [map_io]: free_thresh: 0.25
[component_container_isolated-18] [INFO] [1781492622.424699933] [map_io]: occupied_thresh: 0.65
[component_container_isolated-18] [INFO] [1781492622.424746267] [map_io]: mode: trinary
[component_container_isolated-18] [INFO] [1781492622.424776933] [map_io]: negate: 0
[component_container_isolated-18] [INFO] [1781492622.425560601] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm
[component_container_isolated-18] [INFO] [1781492622.486494671] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm: 163 X 141 map @ 0.05 m/cell
[component_container_isolated-18] [INFO] [1781492622.515188495] [behavior_server]:
[component_container_isolated-18]       behavior_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781492622.527912843] [lifecycle_manager_localization]: Configuring amcl
[component_container_isolated-18] [INFO] [1781492622.529095886] [amcl]: Configuring
[component_container_isolated-18] [INFO] [1781492622.529533970] [amcl]: initTransforms
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/behavior_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781492622.589710789] [nav2_container]: Load Library: /opt/ros/humble/lib/libbt_navigator_core.so
[component_container_isolated-18] [INFO] [1781492622.604701973] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-18] [INFO] [1781492622.604886140] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-18] [INFO] [1781492622.614762068] [amcl]: initPubSub
[component_container_isolated-18] [INFO] [1781492622.658605243] [amcl]: Subscribed to map topic.
[component_container_isolated-18] [INFO] [1781492622.697885247] [lifecycle_manager_localization]: Activating map_server
[component_container_isolated-18] [INFO] [1781492622.704895296] [map_server]: Activating
[component_container_isolated-18] [INFO] [1781492622.705393297] [map_server]: Creating bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492622.712669514] [amcl]: Received a 163 X 141 map @ 0.050 m/pix
[component_container_isolated-18] [INFO] [1781492622.760929236] [bt_navigator]:
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/bt_navigator' in container '/nav2_container'
[component_container_isolated-18]       bt_navigator lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781492622.761297486] [bt_navigator]: Creating
[component_container_isolated-18] [INFO] [1781492622.778409631] [nav2_container]: Load Library: /opt/ros/humble/lib/libwaypoint_follower_core.so
[component_container_isolated-18] [INFO] [1781492622.785235597] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-18] [INFO] [1781492622.785419889] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-18] [INFO] [1781492622.836350031] [lifecycle_manager_localization]: Server map_server connected with bond.
[component_container_isolated-18] [INFO] [1781492622.836559531] [lifecycle_manager_localization]: Activating amcl
[component_container_isolated-18] [INFO] [1781492622.838183324] [amcl]: Activating
[component_container_isolated-18] [INFO] [1781492622.838616741] [amcl]: initialPoseReceived
[component_container_isolated-18] [INFO] [1781492622.839212159] [amcl]: Setting pose (1781492622.839206): -1.985 -0.014 0.262
[component_container_isolated-18] [INFO] [1781492622.845040082] [amcl]: Creating bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492622.862153977] [amcl]: createLaserObject
[component_container_isolated-18] [INFO] [1781492622.883075334] [waypoint_follower]:
[component_container_isolated-18]       waypoint_follower lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781492622.887659756] [waypoint_follower]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/waypoint_follower' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781492622.915302996] [nav2_container]: Load Library: /opt/ros/humble/lib/libvelocity_smoother_core.so
[component_container_isolated-18] [INFO] [1781492622.919005834] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-18] [INFO] [1781492622.919236709] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-18] [INFO] [1781492622.975164773] [lifecycle_manager_localization]: Server amcl connected with bond.
[component_container_isolated-18] [INFO] [1781492622.975350398] [lifecycle_manager_localization]: Managed nodes are active
[component_container_isolated-18] [INFO] [1781492622.975466607] [lifecycle_manager_localization]: Creating bond timer...
[component_container_isolated-18] [INFO] [1781492623.017475197] [velocity_smoother]:
[component_container_isolated-18]       velocity_smoother lifecycle node launched.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/velocity_smoother' in container '/nav2_container'
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781492623.030215586] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781492623.031574671] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781492623.120803815] [lifecycle_manager_navigation]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_navigation' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781492623.155019646] [lifecycle_manager_navigation]: Creating and initializing lifecycle service clients
[component_container_isolated-18] [INFO] [1781492623.281707124] [lifecycle_manager_navigation]: Starting managed nodes bringup...
[component_container_isolated-18] [INFO] [1781492623.282117708] [lifecycle_manager_navigation]: Configuring controller_server
[component_container_isolated-18] [INFO] [1781492623.284487502] [controller_server]: Configuring controller interface
[component_container_isolated-18] [INFO] [1781492623.285808796] [controller_server]: getting goal checker plugins..
[component_container_isolated-18] [INFO] [1781492623.288464549] [controller_server]: Controller frequency set to 10.0000Hz
[component_container_isolated-18] [INFO] [1781492623.289158883] [local_costmap.local_costmap]: Configuring
[component_container_isolated-18] [INFO] [1781492623.332304682] [local_costmap.local_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781492623.387747871] [local_costmap.local_costmap]: Subscribed to Topics: scan aurora_points
[component_container_isolated-18] [INFO] [1781492623.502640544] [local_costmap.local_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781492623.502833169] [local_costmap.local_costmap]: Using plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781492623.525420445] [local_costmap.local_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781492623.526174154] [local_costmap.local_costmap]: Using plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781492623.548279179] [local_costmap.local_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781492623.614346630] [controller_server]: Created progress_checker : progress_checker of type nav2_controller::SimpleProgressChecker
[component_container_isolated-18] [INFO] [1781492623.627128853] [controller_server]: Created goal checker : goal_checker of type nav2_controller::SimpleGoalChecker
[component_container_isolated-18] [INFO] [1781492623.642289037] [controller_server]: Controller Server has goal_checker  goal checkers available.
[component_container_isolated-18] [INFO] [1781492623.648016835] [controller_server]: Created controller : FollowPath of type nav2_regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781492623.757981211] [controller_server]: Controller Server has FollowPath  controllers available.
[component_container_isolated-18] [INFO] [1781492623.819195240] [lifecycle_manager_navigation]: Configuring smoother_server
[component_container_isolated-18] [INFO] [1781492623.820446699] [smoother_server]: Configuring smoother server
[component_container_isolated-18] [INFO] [1781492623.888908486] [smoother_server]: Created smoother : SmoothPath of type nav2_constrained_smoother/ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781492623.942740214] [smoother_server]: Smoother Server has SmoothPath  smoothers available.
[competition_master_stage3.py-19] [INFO] [1781492623.942744006] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1781492623.945702176] [competition_master_stage3]: === [Stage 3] 总控节点初始化 ===
[competition_master_stage3.py-19] [INFO] [1781492623.948818638] [competition_master_stage3]:   QR点:    (0.41, -3.17, yaw=0.00)
[competition_master_stage3.py-19] [INFO] [1781492623.951571766] [competition_master_stage3]:   通道入口: (0.38, -1.10, yaw=0.00)
[competition_master_stage3.py-19] [INFO] [1781492623.954729020] [competition_master_stage3]:   P点:     (-1.99, -0.01, yaw=0.26)
[competition_master_stage3.py-19] [INFO] [1781492623.957897565] [competition_master_stage3]:   cruise_cw: 3 路点 → VLM=(3.12, -1.34)
[competition_master_stage3.py-19] [INFO] [1781492623.961287527] [competition_master_stage3]:   cruise_ccw: 3 路点 → VLM=(2.10, 0.92)
[competition_master_stage3.py-19] [INFO] [1781492623.964157197] [competition_master_stage3]:   超时: total=180.0s QR=90.0s entry=60.0s cruise=180.0s vlm=30.0s return=120.0s
[competition_master_stage3.py-19] [INFO] [1781492623.966862909] [competition_master_stage3]:   回退QR方向: 逆时针
[competition_master_stage3.py-19] [INFO] [1781492623.969623662] [competition_master_stage3]:   VLM结果话题: vlm_result
[competition_master_stage3.py-19] [INFO] [1781492623.972708999] [competition_master_stage3]: ============================================================
[component_container_isolated-18] [INFO] [1781492623.990568352] [lifecycle_manager_navigation]: Configuring planner_server
[component_container_isolated-18] [INFO] [1781492623.991837771] [planner_server]: Configuring
[component_container_isolated-18] [INFO] [1781492623.992203813] [global_costmap.global_costmap]: Configuring
[component_container_isolated-18] [INFO] [1781492624.034898653] [global_costmap.global_costmap]: Using plugin "static_layer"
[component_container_isolated-18] [INFO] [1781492624.051368547] [global_costmap.global_costmap]: Subscribing to the map topic (/map) with transient local durability
[component_container_isolated-18] [INFO] [1781492624.056417594] [global_costmap.global_costmap]: Initialized plugin "static_layer"
[component_container_isolated-18] [INFO] [1781492624.056572803] [global_costmap.global_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781492624.074263073] [global_costmap.global_costmap]: Subscribed to Topics: scan aurora_points
[component_container_isolated-18] [INFO] [1781492624.174354396] [global_costmap.global_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781492624.174520396] [global_costmap.global_costmap]: Using plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781492624.191430707] [global_costmap.global_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781492624.191628416] [global_costmap.global_costmap]: Using plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781492624.210156728] [global_costmap.global_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781492624.254701571] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 163 X 141 at 0.050000 m/pix
[component_container_isolated-18] [INFO] [1781492624.282888562] [planner_server]: Created global planner plugin GridBased of type nav2_smac_planner/SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781492624.283106729] [planner_server]: Configuring GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781492624.324190442] [planner_server]: Even sized heuristic lookup table size set 200.000000, increasing size by 1 to make odd
[rviz2-20] [INFO] [1781492624.366958158] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-20] [INFO] [1781492624.369835411] [rviz2]: OpenGl version: 4.5 (GLSL 4.5)
[rviz2-20] [INFO] [1781492624.550725368] [rviz2]: Stereo is NOT SUPPORTED
[imu_madgwick_filter.py-4] [INFO] [1781492624.663595913] [imu_madgwick_filter]: [imu_madgwick ->] msgs=200 q_w=0.9995 angle=3.5deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781492624.905736773] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=414 q_w=0.9994 angle=4.1deg beta=0.0030
[rviz2-20] [INFO] [1781492626.560213160] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[rviz2-20] [ERROR] [1781492626.942401220] [rviz2]: Vertex Program:rviz/glsl120/indexed_8bit_image.vert Fragment Program:rviz/glsl120/indexed_8bit_image.frag GLSL link result :
[rviz2-20] active samplers with a different type refer to the same texture image unit
[qr_decoder-12] [INFO] [1781492631.335248741] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=200 last_qr_frame=-1 gap=-1 frames rejects=0
[imu_madgwick_filter.py-4] [INFO] [1781492634.665906407] [imu_madgwick_filter]: [imu_madgwick ->] msgs=400 q_w=0.9981 angle=7.0deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781492634.905635926] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=940 q_w=0.9993 angle=4.2deg beta=0.0030
[component_container_isolated-18] [INFO] [1781492638.294495300] [planner_server]: Configured plugin GridBased of type SmacPlannerHybrid with maximum iterations 2000, max on approach iterations 300, and not allowing unknown traversal. Tolerance 0.50.Using motion model: Reeds-Shepp.
[component_container_isolated-18] [INFO] [1781492638.295176717] [planner_server]: Planner Server has GridBased  planners available.
[component_container_isolated-18] [INFO] [1781492638.353775866] [lifecycle_manager_navigation]: Configuring behavior_server
[component_container_isolated-18] [INFO] [1781492638.354879992] [behavior_server]: Configuring
[component_container_isolated-18] [INFO] [1781492638.399922876] [behavior_server]: Creating behavior plugin spin of type nav2_behaviors/Spin
[component_container_isolated-18] [INFO] [1781492638.404635631] [behavior_server]: Configuring spin
[component_container_isolated-18] [INFO] [1781492638.463242904] [behavior_server]: Creating behavior plugin backup of type nav2_behaviors/BackUp
[component_container_isolated-18] [INFO] [1781492638.467591701] [behavior_server]: Configuring backup
[component_container_isolated-18] [INFO] [1781492638.516523005] [behavior_server]: Creating behavior plugin drive_on_heading of type nav2_behaviors/DriveOnHeading
[component_container_isolated-18] [INFO] [1781492638.521978762] [behavior_server]: Configuring drive_on_heading
[component_container_isolated-18] [INFO] [1781492638.579584201] [behavior_server]: Creating behavior plugin wait of type nav2_behaviors/Wait
[component_container_isolated-18] [INFO] [1781492638.584566081] [behavior_server]: Configuring wait
[component_container_isolated-18] [INFO] [1781492638.616007950] [lifecycle_manager_navigation]: Configuring bt_navigator
[component_container_isolated-18] [INFO] [1781492638.617154576] [bt_navigator]: Configuring
[competition_master_stage3.py-19] [INFO] [1781492639.082599303] [competition_master_stage3]: [LAUNCH] 发车阶段: 15.3s
[competition_master_stage3.py-19] [INFO] [1781492639.088881060] [competition_master_stage3]: >>> 系统就绪, 开始 Stage 3 导航
[competition_master_stage3.py-19] [INFO] [1781492639.095099150] [competition_master_stage3]: [状态机] INIT → NAV_TO_QR
[competition_master_stage3.py-19] [INFO] [1781492639.105200078] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-18] [INFO] [1781492639.193283843] [lifecycle_manager_navigation]: Configuring waypoint_follower
[component_container_isolated-18] [INFO] [1781492639.194708011] [waypoint_follower]: Configuring
[competition_master_stage3.py-19] [WARN] [1781492639.206018065] [competition_master_stage3]: 导航目标被拒绝, 3s 后重试...
[component_container_isolated-18] [INFO] [1781492639.294436122] [waypoint_follower]: Created waypoint_task_executor : wait_at_waypoint of type nav2_waypoint_follower::WaitAtWaypoint
[component_container_isolated-18] [INFO] [1781492639.305927385] [lifecycle_manager_navigation]: Configuring velocity_smoother
[component_container_isolated-18] [INFO] [1781492639.307593387] [velocity_smoother]: Configuring velocity smoother
[component_container_isolated-18] [INFO] [1781492639.350798518] [lifecycle_manager_navigation]: Activating controller_server
[component_container_isolated-18] [INFO] [1781492639.352031978] [controller_server]: Activating
[component_container_isolated-18] [INFO] [1781492639.352298603] [local_costmap.local_costmap]: Activating
[component_container_isolated-18] [INFO] [1781492639.352411270] [local_costmap.local_costmap]: Checking transform
[component_container_isolated-18] [INFO] [1781492639.352775645] [local_costmap.local_costmap]: start
[component_container_isolated-18] [INFO] [1781492639.362950698] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781492639.372147750] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781492639.372334667] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781492639.378998966] [local_costmap.local_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[component_container_isolated-18] [INFO] [1781492639.622130028] [controller_server]: Activating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781492639.622505070] [controller_server]: Creating bond (controller_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492639.736909323] [lifecycle_manager_navigation]: Server controller_server connected with bond.
[component_container_isolated-18] [INFO] [1781492639.737108823] [lifecycle_manager_navigation]: Activating smoother_server
[component_container_isolated-18] [INFO] [1781492639.738424074] [smoother_server]: Activating
[component_container_isolated-18] [INFO] [1781492639.738726200] [smoother_server]: Activating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781492639.738878033] [smoother_server]: Creating bond (smoother_server) to lifecycle manager.
[competition_master_stage3.py-19] [INFO] [1781492639.832218470] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.00,-0.02) yaw=16deg cmd=(vx=0.00 wz=0.00) elapsed=0.7s cpuFreq=1500MHz cpuT=71C cpu=56% mem=20%
[component_container_isolated-18] [INFO] [1781492639.868277885] [lifecycle_manager_navigation]: Server smoother_server connected with bond.
[component_container_isolated-18] [INFO] [1781492639.868460052] [lifecycle_manager_navigation]: Activating planner_server
[component_container_isolated-18] [INFO] [1781492639.870835180] [planner_server]: Activating
[component_container_isolated-18] [INFO] [1781492639.871353014] [global_costmap.global_costmap]: Activating
[component_container_isolated-18] [INFO] [1781492639.871476597] [global_costmap.global_costmap]: Checking transform
[component_container_isolated-18] [INFO] [1781492639.871813848] [global_costmap.global_costmap]: start
[component_container_isolated-18] [INFO] [1781492639.892870871] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781492639.905336302] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781492639.905515427] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781492639.913662144] [global_costmap.global_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[rviz2-20] [INFO] [1781492640.117522079] [rviz2]: Trying to create a map of size 60 x 60 using 1 swatches
[component_container_isolated-18] [INFO] [1781492640.905232996] [planner_server]: Activating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781492640.910775960] [planner_server]: Creating bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492641.036449141] [lifecycle_manager_navigation]: Server planner_server connected with bond.
[component_container_isolated-18] [INFO] [1781492641.036671308] [lifecycle_manager_navigation]: Activating behavior_server
[component_container_isolated-18] [INFO] [1781492641.038076685] [behavior_server]: Activating
[component_container_isolated-18] [INFO] [1781492641.038222227] [behavior_server]: Activating spin
[component_container_isolated-18] [INFO] [1781492641.038376352] [behavior_server]: Activating backup
[component_container_isolated-18] [INFO] [1781492641.038459727] [behavior_server]: Activating drive_on_heading
[component_container_isolated-18] [INFO] [1781492641.038540102] [behavior_server]: Activating wait
[component_container_isolated-18] [INFO] [1781492641.038624602] [behavior_server]: Creating bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492641.148561932] [lifecycle_manager_navigation]: Server behavior_server connected with bond.
[component_container_isolated-18] [INFO] [1781492641.148835933] [lifecycle_manager_navigation]: Activating bt_navigator
[component_container_isolated-18] [INFO] [1781492641.150661185] [bt_navigator]: Activating
[component_container_isolated-18] [WARN] [1781492641.281280705] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[rviz2-20] [INFO] [1781492641.322987542] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[component_container_isolated-18] [WARN] [1781492641.419820858] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781492641.499064779] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781492641.686271445] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[competition_master_stage3.py-19] [INFO] [1781492641.840168157] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.00,-0.02) yaw=16deg cmd=(vx=0.00 wz=0.00) elapsed=2.7s cpuFreq=1500MHz cpuT=72C cpu=100% mem=20%
[component_container_isolated-18] [WARN] [1781492641.913457239] [bt_navigator_navigate_to_pose_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [INFO] [1781492642.089514100] [bt_navigator]: Creating bond (bt_navigator) to lifecycle manager.
[competition_master_stage3.py-19] [INFO] [1781492642.210706985] [competition_master_stage3]: 重试发送导航目标 (QR点)...
[component_container_isolated-18] [INFO] [1781492642.214219572] [lifecycle_manager_navigation]: Server bt_navigator connected with bond.
[component_container_isolated-18] [INFO] [1781492642.214374780] [lifecycle_manager_navigation]: Activating waypoint_follower
[component_container_isolated-18] [INFO] [1781492642.215465240] [waypoint_follower]: Activating
[component_container_isolated-18] [INFO] [1781492642.215707448] [waypoint_follower]: Creating bond (waypoint_follower) to lifecycle manager.
[competition_master_stage3.py-19] [INFO] [1781492642.228569504] [competition_master_stage3]: [DIAG] nav目标距离: 3.97m, robot=(-2.00,-0.02) → target=(0.41,-3.17)
[competition_master_stage3.py-19] [INFO] [1781492642.233131134] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-18] [INFO] [1781492642.241624852] [bt_navigator]: Begin navigating from current location (-2.00, -0.02) to (0.41, -3.17)
[competition_master_stage3.py-19] [INFO] [1781492642.257695245] [competition_master_stage3]: 导航目标已接受，车辆出发...
[component_container_isolated-18] [INFO] [1781492642.345356759] [lifecycle_manager_navigation]: Server waypoint_follower connected with bond.
[component_container_isolated-18] [INFO] [1781492642.345525300] [lifecycle_manager_navigation]: Activating velocity_smoother
[component_container_isolated-18] [INFO] [1781492642.346788760] [velocity_smoother]: Activating
[component_container_isolated-18] [INFO] [1781492642.347115802] [velocity_smoother]: Creating bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492642.471675357] [lifecycle_manager_navigation]: Server velocity_smoother connected with bond.
[component_container_isolated-18] [INFO] [1781492642.471874649] [lifecycle_manager_navigation]: Managed nodes are active
[component_container_isolated-18] [INFO] [1781492642.471947190] [lifecycle_manager_navigation]: Creating bond timer...
[component_container_isolated-18] [WARN] [1781492642.903202459] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.5377 Hz
[component_container_isolated-18] [INFO] [1781492643.047167577] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-18] [WARN] [1781492643.051126123] [controller_server]: No goal checker was specified in parameter 'current_goal_checker'. Server will use only plugin loaded goal_checker . This warning will appear once.
[cmd_vel_mux.py-8] [INFO] [1781492643.136859926] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=-0.12
[velocity_pid.py-9] [INFO] [1781492643.170604963] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.17 err=100.0%
[competition_master_stage3.py-19] [INFO] [1781492643.823665518] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.00,-0.02) yaw=16deg cmd=(vx=0.50 wz=-1.48) elapsed=4.7s plan[31pts 4.3m] (-2.00,-0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=71C cpu=67% mem=20%
[component_container_isolated-18] Reallocing temp weights 301 - 60
[imu_madgwick_filter.py-4] [INFO] [1781492644.663903237] [imu_madgwick_filter]: [imu_madgwick ->] msgs=599 q_w=0.9517 angle=35.7deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781492644.909429216] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1393 q_w=0.9023 angle=51.1deg beta=0.0030
[cmd_vel_mux.py-8] [INFO] [1781492645.268239277] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.20
[velocity_pid.py-9] [INFO] [1781492645.268520153] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.51 corrected=-0.09 err=24.4%
[velocity_pid.py-9] [INFO] [1781492645.501208534] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0333s, resetting
[competition_master_stage3.py-19] [INFO] [1781492645.821850262] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.24,-0.32) yaw=-36deg cmd=(vx=-0.30 wz=0.24) elapsed=6.7s plan[31pts 4.3m] (-2.00,-0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=72C cpu=82% mem=21%
[component_container_isolated-18] [WARN] [1781492645.900166098] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3241 Hz
[component_container_isolated-18] Reallocing temp weights 1500 - 60
[component_container_isolated-18] [INFO] [1781492646.052006765] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781492646.171646480] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.12
[velocity_pid.py-9] [INFO] [1781492646.200992554] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.01 -> current=-0.12 dt=0.0325s, resetting
[velocity_pid.py-9] [INFO] [1781492646.302280582] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0327s, resetting
[velocity_pid.py-9] [INFO] [1781492646.307669838] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.10 corrected=0.38 err=273.3%
[qr_decoder-12] [INFO] [1781492646.819359608] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=400 last_qr_frame=-1 gap=-1 frames rejects=0
[competition_master_stage3.py-19] [INFO] [1781492647.829225716] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.99,-0.53) yaw=-54deg cmd=(vx=0.50 wz=0.22) elapsed=8.7s plan[24pts 3.2m] (-1.10,-0.45)→(0.40,-3.15) cpuFreq=1500MHz cpuT=72C cpu=64% mem=21%
[velocity_pid.py-9] [INFO] [1781492648.668459177] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.00 err=22.7%
[cmd_vel_mux.py-8] [INFO] [1781492648.677598062] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.02
[component_container_isolated-18] [WARN] [1781492648.899168180] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3288 Hz
[velocity_pid.py-9] [INFO] [1781492648.905576978] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0335s, resetting
[component_container_isolated-18] [INFO] [1781492649.051463555] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781492649.281310514] [cmd_vel_mux]: [mux→] src=nav vx=0.06 wz=-0.54
[velocity_pid.py-9] [INFO] [1781492649.301417370] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0329s, resetting
[velocity_pid.py-9] [INFO] [1781492649.668464354] [velocity_pid]: [vel_pid→] desired=0.38 actual=0.06 corrected=0.30 err=84.6%
[competition_master_stage3.py-19] [INFO] [1781492649.830289323] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.62,-1.00) yaw=-47deg cmd=(vx=0.37 wz=-1.66) elapsed=10.7s plan[17pts 2.4m] (-0.60,-1.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=72C cpu=86% mem=21%
[cmd_vel_mux.py-8] [INFO] [1781492650.143609581] [cmd_vel_mux]: [mux→] src=nav vx=0.50 wz=-1.60
[velocity_pid.py-9] [INFO] [1781492650.842110802] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.10 -> current=0.02 dt=0.0356s, resetting
[cmd_vel_mux.py-8] [INFO] [1781492651.271038894] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.90
[velocity_pid.py-9] [INFO] [1781492651.302377303] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.48 corrected=-0.13 err=51.2%
[velocity_pid.py-9] [INFO] [1781492651.500615811] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0332s, resetting
[competition_master_stage3.py-19] [INFO] [1781492651.838789929] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.36,-1.76) yaw=-92deg cmd=(vx=-0.30 wz=0.31) elapsed=12.7s plan[17pts 2.4m] (-0.60,-1.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=72C cpu=100% mem=21%
[qr_decoder-12] [INFO] [1781492651.851062651] [qr_decoder_zbar]: [qr_decoder] QR DETECTED frame=467 symbols=1 (gap=-1 frames)
[qr_decoder-12] [INFO] [1781492651.851318568] [qr_decoder_zbar]: [QR] 1584 | 3D:(-1.051, +0.182, 1.597)m | px(43,245) D:1597mm
[qr_decoder-12] [INFO] [1781492651.851844068] [qr_decoder_zbar]: [QR] 1584 | robot_pos: (0.63, -2.41, yaw=-2.21)
[qr_decision-13] [INFO] [1781492651.856101156] [qr_decision]: [QR] 1584 CCW @ (x=0.63, y=-2.42, yaw=-2.22) → /qr_event
[qr_decision-13] [INFO] [1781492651.864126457] [qr_decision]: [检查点] qr_decision 发布 /qr_event (由 task_manager 决定停车)
[competition_master_stage3.py-19] [INFO] [1781492651.869683296] [competition_master_stage3]: [QR检测] 内容: 1584
[component_container_isolated-18] [WARN] [1781492651.896778867] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3326 Hz
[qr_decoder-12] [INFO] [1781492651.928145652] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[competition_master_stage3.py-19] [INFO] [1781492651.941117041] [competition_master_stage3]: [KILL] 已终止进程: qr_decoder_zbar
[competition_master_stage3.py-19] [INFO] [1781492651.955498848] [competition_master_stage3]: >>> QR 解码已关闭, 等待方向判断 (/qr_event)...
[competition_master_stage3.py-19] [INFO] [1781492651.972792700] [competition_master_stage3]: [QR检测] 取消当前导航目标, 等待BT完成 cancel/halt 清理...
[competition_master_stage3.py-19] [INFO] [1781492652.013464411] [competition_master_stage3]: [QR事件] 方向: 逆时针 (通道巡航阶段使用)
[component_container_isolated-18] [INFO] [1781492652.051522452] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-18] [INFO] [1781492652.051797869] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1781492652.054762789] [bt_navigator]: [navigate_to_pose] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1781492652.058221918] [bt_navigator]: Goal canceled
[competition_master_stage3.py-19] [INFO] [1781492652.080933443] [competition_master_stage3]: [KILL] 已终止进程: qr_decision
[competition_master_stage3.py-19] [INFO] [1781492652.110017016] [competition_master_stage3]: [结果回调] BT取消确认完成 (STATUS_CANCELED), 准备发送通道入口目标...
[competition_master_stage3.py-19] [INFO] [1781492652.113374853] [competition_master_stage3]: [状态机] NAV_TO_QR → BACKING_UP
[competition_master_stage3.py-19] [INFO] [1781492652.115981148] [competition_master_stage3]: >>> BT取消完成, 右后退摆正车头→前进进通道...
[competition_master_stage3.py-19] [INFO] [1781492652.119839735] [competition_master_stage3]: [BACKUP] 右后退中: vx=-0.15 wz=0.80, 持续 6.0s...
[cmd_vel_mux.py-8] [INFO] [1781492652.145591055] [cmd_vel_mux]: [mux→] src=nav vx=-0.15 wz=0.80
[INFO] [qr_decoder-12]: process has finished cleanly [pid 32618]
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
[velocity_pid.py-9] [INFO] [1781492652.368363839] [velocity_pid]: [vel_pid→] desired=-0.15 actual=-0.11 corrected=-0.40 err=26.0%
[qr_decision-13]     raise ExternalShutdownException()
[qr_decision-13] rclpy.executors.ExternalShutdownException
[cmd_vel_mux.py-8] [INFO] [1781492652.673215670] [cmd_vel_mux]: [mux→] src=nav vx=0.00 wz=0.00
[ERROR] [qr_decision-13]: process has died [pid 32622, exit code 1, cmd '/userdata/dev_ws/install/origincar_qr/lib/origincar_qr/qr_decision --ros-args -r __node:=qr_decision --params-file /tmp/launch_params_yg39_tot'].
[velocity_pid.py-9] [INFO] [1781492653.401708920] [velocity_pid]: [vel_pid→] desired=-0.15 actual=-0.09 corrected=-0.17 err=39.3%
[competition_master_stage3.py-19] [INFO] [1781492653.827282590] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.37,-1.80) yaw=-84deg cmd=(vx=-0.15 wz=0.80) elapsed=14.7s plan[11pts 1.5m] (-0.40,-1.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=72C cpu=56% mem=20%
[imu_madgwick_filter.py-4] [INFO] [1781492654.666785916] [imu_madgwick_filter]: [imu_madgwick ->] msgs=797 q_w=0.8758 angle=57.7deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781492654.907260426] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1848 q_w=0.8325 angle=67.3deg beta=0.0030
[competition_master_stage3.py-19] [INFO] [1781492655.821171207] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.49,-1.61) yaw=-42deg cmd=(vx=-0.15 wz=0.80) elapsed=16.7s plan[11pts 1.5m] (-0.40,-1.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=71C cpu=62% mem=20%
[competition_master_stage3.py-19] [INFO] [1781492657.822353407] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.79,-1.53) yaw=14deg cmd=(vx=-0.15 wz=0.80) elapsed=18.7s plan[11pts 1.5m] (-0.40,-1.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=71C cpu=38% mem=20%
[competition_master_stage3.py-19] [INFO] [1781492658.123519481] [competition_master_stage3]: [状态机] BACKING_UP → CRUISE_CHANNEL
[competition_master_stage3.py-19] [INFO] [1781492658.130508864] [competition_master_stage3]: [CRUISE] 方向: CCW (逆时针, even QR), 路点: (1.73,-1.98), (3.10,-1.35), (2.10,0.92)
[cmd_vel_mux.py-8] [INFO] [1781492658.136382620] [cmd_vel_mux]: [mux→] src=stop vx=0.00 wz=0.00
[competition_master_stage3.py-19] [INFO] [1781492658.142149418] [competition_master_stage3]: [CRUISE] NavigateThroughPoses: (0.38,-1.10), (1.73,-1.98), (3.10,-1.35), (2.10,0.92)
[component_container_isolated-18] [INFO] [1781492658.145242963] [bt_navigator]: Begin navigating from current location through 4 poses to (2.10, 0.92)
[competition_master_stage3.py-19] [INFO] [1781492658.154821223] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[cmd_vel_mux.py-8] [INFO] [1781492658.634711239] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.51s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1781492658.650132173] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[component_container_isolated-18] [WARN] [1781492658.911505454] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3109 Hz
[component_container_isolated-18] [INFO] [1781492659.047357433] [controller_server]: Received a goal, begin computing control effort.
[cmd_vel_mux.py-8] [INFO] [1781492659.137169613] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=-0.12
[velocity_pid.py-9] [INFO] [1781492659.167251978] [velocity_pid]: [vel_pid→] desired=0.07 actual=-0.02 corrected=0.11 err=125.3%
[competition_master_stage3.py-19] [INFO] [1781492659.841419161] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.90,-1.56) yaw=32deg cmd=(vx=0.50 wz=-0.55) elapsed=20.7s plan[62pts 8.1m] (-0.90,-1.55)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=100% mem=20%
[velocity_pid.py-9] [INFO] [1781492661.269096899] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.14 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1781492661.269717691] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.14
[velocity_pid.py-9] [INFO] [1781492661.500369104] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0330s, resetting
[competition_master_stage3.py-19] [INFO] [1781492661.821624240] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.12,-1.30) yaw=12deg cmd=(vx=-0.30 wz=0.06) elapsed=22.7s plan[62pts 8.1m] (-0.90,-1.55)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=14% mem=20%
[component_container_isolated-18] [WARN] [1781492661.906815831] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3183 Hz
[component_container_isolated-18] [INFO] [1781492662.047813607] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781492662.168270069] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.06
[velocity_pid.py-9] [INFO] [1781492662.300969669] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0336s, resetting
[velocity_pid.py-9] [INFO] [1781492662.305267548] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.12 corrected=0.42 err=306.7%
[competition_master_stage3.py-19] [INFO] [1781492663.830820717] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.06,-1.24) yaw=17deg cmd=(vx=0.50 wz=-0.42) elapsed=24.7s plan[55pts 7.2m] (-0.00,-1.25)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=33% mem=20%
[velocity_pid.py-9] [INFO] [1781492664.533965299] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.01 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1781492664.582602434] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.11
[imu_madgwick_filter.py-4] [INFO] [1781492664.664770314] [imu_madgwick_filter]: [imu_madgwick ->] msgs=995 q_w=0.9999 angle=1.9deg beta=0.0330
[velocity_pid.py-9] [INFO] [1781492664.667344525] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.11 -> current=0.01 dt=0.0339s, resetting
[velocity_pid.py-9] [INFO] [1781492664.801745918] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0342s, resetting
[component_container_isolated-18] [WARN] [1781492664.902028149] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3263 Hz
[imu_madgwick_filter.py-6] [INFO] [1781492664.907283322] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2378 q_w=0.9807 angle=22.5deg beta=0.0030
[component_container_isolated-18] [INFO] [1781492665.047810638] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781492665.169134225] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.02
[velocity_pid.py-9] [INFO] [1781492665.212262687] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.10 -> current=-0.02 dt=0.0416s, resetting
[velocity_pid.py-9] [INFO] [1781492665.300348114] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0332s, resetting
[velocity_pid.py-9] [INFO] [1781492665.535216989] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.00 corrected=0.32 err=100.0%
[competition_master_stage3.py-19] [INFO] [1781492665.844804276] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.71,-1.12) yaw=-6deg cmd=(vx=0.50 wz=-0.39) elapsed=26.7s plan[47pts 6.3m] (0.80,-1.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=80% mem=20%
[velocity_pid.py-9] [INFO] [1781492667.269171328] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.03 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1781492667.269491203] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.70
[velocity_pid.py-9] [INFO] [1781492667.512033501] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0400s, resetting
[competition_master_stage3.py-19] [INFO] [1781492667.824255790] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.58,-1.42) yaw=-60deg cmd=(vx=-0.30 wz=0.43) elapsed=28.7s plan[47pts 6.3m] (0.80,-1.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=50% mem=20%
[component_container_isolated-18] [WARN] [1781492667.899784745] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3291 Hz
[component_container_isolated-18] [INFO] [1781492668.047752485] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781492668.168102570] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.54
[velocity_pid.py-9] [INFO] [1781492668.301050628] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0280s, resetting
[velocity_pid.py-9] [INFO] [1781492668.307698885] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.11 corrected=0.45 err=285.0%
[velocity_pid.py-9] [INFO] [1781492668.433462267] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.09 dt=0.0334s, resetting
[competition_master_stage3.py-19] [INFO] [1781492669.834095621] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.63,-1.57) yaw=-76deg cmd=(vx=0.50 wz=0.55) elapsed=30.7s plan[41pts 5.3m] (1.60,-1.55)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=38% mem=20%
[cmd_vel_mux.py-8] [INFO] [1781492669.871177118] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.80
[velocity_pid.py-9] [INFO] [1781492669.871816035] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.01 err=21.2%
[velocity_pid.py-9] [INFO] [1781492670.110455204] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0365s, resetting
[velocity_pid.py-9] [INFO] [1781492670.300678070] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.09 dt=0.0332s, resetting
[component_container_isolated-18] [WARN] [1781492670.896609573] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3349 Hz
[velocity_pid.py-9] [INFO] [1781492670.904111914] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.14 corrected=-0.26 err=54.3%
[component_container_isolated-18] [INFO] [1781492671.047869315] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781492671.174825324] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.04
[velocity_pid.py-9] [INFO] [1781492671.267152337] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.09 dt=0.0331s, resetting
[velocity_pid.py-9] [INFO] [1781492671.300282747] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0333s, resetting
[competition_master_stage3.py-19] [INFO] [1781492671.848349448] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.66,-1.95) yaw=-76deg cmd=(vx=0.50 wz=0.59) elapsed=32.7s plan[37pts 5.0m] (1.70,-2.05)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=79% mem=20%
[velocity_pid.py-9] [INFO] [1781492671.904255757] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.14 corrected=0.42 err=72.6%
[competition_master_stage3.py-19] [INFO] [1781492673.821699017] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.25,-2.38) yaw=-4deg cmd=(vx=0.50 wz=0.96) elapsed=34.7s plan[37pts 5.0m] (1.70,-2.05)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=80% mem=20%
[cmd_vel_mux.py-8] [INFO] [1781492673.871461861] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.71
[velocity_pid.py-9] [INFO] [1781492673.872615529] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.03 err=22.7%
[component_container_isolated-18] [WARN] [1781492673.897656972] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3349 Hz
[component_container_isolated-18] [INFO] [1781492674.047756170] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781492674.101045226] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0329s, resetting
[imu_madgwick_filter.py-4] [INFO] [1781492674.666142608] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1192 q_w=0.9213 angle=45.8deg beta=0.0330
[velocity_pid.py-9] [INFO] [1781492674.900801395] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.37 corrected=0.16 err=25.4%
[imu_madgwick_filter.py-6] [INFO] [1781492674.911505073] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2888 q_w=0.9548 angle=34.6deg beta=0.0030
[cmd_vel_mux.py-8] [INFO] [1781492675.268657154] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.18
[velocity_pid.py-9] [INFO] [1781492675.501046814] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0326s, resetting
[competition_master_stage3.py-19] [INFO] [1781492675.829653156] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.88,-1.84) yaw=64deg cmd=(vx=-0.30 wz=-0.50) elapsed=36.7s plan[33pts 4.4m] (2.30,-2.35)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=29% mem=20%
[velocity_pid.py-9] [INFO] [1781492675.901069564] [velocity_pid]: [vel_pid→] desired=-0.30 actual=0.07 corrected=-0.33 err=123.7%
[component_container_isolated-18] [WARN] [1781492676.896087893] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3390 Hz
[component_container_isolated-18] [INFO] [1781492677.047758759] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781492677.272355117] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.20
[velocity_pid.py-9] [INFO] [1781492677.272750159] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.27 corrected=-0.01 err=30.5%
[velocity_pid.py-9] [INFO] [1781492677.405993798] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0338s, resetting
[competition_master_stage3.py-19] [INFO] [1781492677.822543023] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.68,-1.98) yaw=41deg cmd=(vx=0.50 wz=-0.44) elapsed=38.7s plan[29pts 3.8m] (2.90,-1.85)→(2.10,0.95) cpuFreq=1500MHz cpuT=72C cpu=62% mem=20%
[velocity_pid.py-9] [INFO] [1781492678.303948023] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.33 corrected=0.32 err=33.4%
[cmd_vel_mux.py-8] [INFO] [1781492678.769390922] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.48
[velocity_pid.py-9] [INFO] [1781492679.000820496] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1781492679.004635583] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.11 -> current=0.02 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1781492679.334368550] [velocity_pid]: [vel_pid→] desired=-0.30 actual=0.14 corrected=-0.36 err=145.7%
[competition_master_stage3.py-19] [INFO] [1781492679.825814017] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.10,-1.84) yaw=-7deg cmd=(vx=-0.30 wz=1.07) elapsed=40.7s plan[29pts 3.8m] (2.90,-1.85)→(2.10,0.95) cpuFreq=1500MHz cpuT=72C cpu=38% mem=20%
[component_container_isolated-18] [WARN] [1781492679.896757549] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3396 Hz
[component_container_isolated-18] [INFO] [1781492680.047778206] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781492680.168853206] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.95
[velocity_pid.py-9] [INFO] [1781492680.300250467] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0330s, resetting
[velocity_pid.py-9] [INFO] [1781492680.335524628] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.22 corrected=0.21 err=458.3%
[cmd_vel_mux.py-8] [INFO] [1781492681.235018766] [cmd_vel_mux]: [mux→] src=nav vx=0.40 wz=-1.67
[velocity_pid.py-9] [INFO] [1781492681.467254298] [velocity_pid]: [vel_pid→] desired=0.25 actual=0.40 corrected=-0.04 err=58.7%
[cmd_vel_mux.py-8] [INFO] [1781492681.735541741] [cmd_vel_mux]: [mux→] src=nav vx=-0.07 wz=-1.54
[competition_master_stage3.py-19] [INFO] [1781492681.822001664] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.17,-1.84) yaw=-12deg cmd=(vx=-0.07 wz=-1.54) elapsed=42.7s plan[27pts 3.6m] (3.10,-1.85)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=64% mem=20%
[velocity_pid.py-9] [INFO] [1781492682.407105351] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.08 dt=0.0330s, resetting
[velocity_pid.py-9] [INFO] [1781492682.467492621] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.10 corrected=-0.14 err=67.3%
[component_container_isolated-18] [WARN] [1781492682.898184648] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3435 Hz
[component_container_isolated-18] [INFO] [1781492683.047830011] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781492683.734915218] [velocity_pid]: [vel_pid→] desired=-0.17 actual=-0.27 corrected=0.23 err=62.4%
[cmd_vel_mux.py-8] [INFO] [1781492683.768236294] [cmd_vel_mux]: [mux→] src=nav vx=-0.08 wz=0.58
[competition_master_stage3.py-19] [INFO] [1781492683.829833899] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.05,-1.81) yaw=3deg cmd=(vx=-0.17 wz=0.46) elapsed=44.7s plan[26pts 3.5m] (3.20,-1.85)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=100% mem=20%
[velocity_pid.py-9] [INFO] [1781492683.867317979] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.08 -> current=0.01 dt=0.0336s, resetting
[imu_madgwick_filter.py-4] [INFO] [1781492684.665974133] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1389 q_w=0.9643 angle=30.7deg beta=0.0330
[velocity_pid.py-9] [INFO] [1781492684.775936370] [velocity_pid]: [vel_pid→] desired=0.35 actual=0.20 corrected=0.30 err=42.8%
[imu_madgwick_filter.py-6] [INFO] [1781492684.907719547] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3386 q_w=0.9933 angle=13.3deg beta=0.0030
[competition_master_stage3.py-19] [INFO] [1781492685.828531033] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.17,-1.58) yaw=63deg cmd=(vx=0.36 wz=1.67) elapsed=46.7s plan[26pts 3.5m] (3.20,-1.85)→(2.10,0.95) cpuFreq=1500MHz cpuT=72C cpu=33% mem=20%
[component_container_isolated-18] [WARN] [1781492685.897012437] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3340 Hz
[component_container_isolated-18] [INFO] [1781492686.147759943] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781492686.301910351] [velocity_pid]: [vel_pid→] desired=0.47 actual=0.34 corrected=0.41 err=27.2%
[cmd_vel_mux.py-8] [INFO] [1781492686.435409904] [cmd_vel_mux]: [mux→] src=nav vx=0.50 wz=1.54
[cmd_vel_mux.py-8] [INFO] [1781492687.481469682] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.29
[velocity_pid.py-9] [INFO] [1781492687.500963911] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.48 corrected=-0.06 err=51.2%
[velocity_pid.py-9] [INFO] [1781492687.700086197] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0331s, resetting
[competition_master_stage3.py-19] [INFO] [1781492687.827228160] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.99,-0.88) yaw=135deg cmd=(vx=-0.11 wz=-0.67) elapsed=48.7s plan[21pts 3.0m] (3.20,-1.55)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=43% mem=20%
[velocity_pid.py-9] [INFO] [1781492688.501237765] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.10 corrected=-0.29 err=65.3%
[component_container_isolated-18] [WARN] [1781492688.897235752] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3378 Hz
[component_container_isolated-18] [INFO] [1781492689.047870530] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781492689.171780281] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.02
[velocity_pid.py-9] [INFO] [1781492689.200433602] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.11 -> current=0.02 dt=0.0330s, resetting
[velocity_pid.py-9] [INFO] [1781492689.300617371] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0288s, resetting
[velocity_pid.py-9] [INFO] [1781492689.501457659] [velocity_pid]: [vel_pid→] desired=0.36 actual=-0.17 corrected=0.53 err=147.2%
[competition_master_stage3.py-19] [INFO] [1781492689.824753571] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.87,-0.90) yaw=120deg cmd=(vx=0.50 wz=0.56) elapsed=50.7s plan[15pts 2.1m] (2.80,-0.75)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=54% mem=20%
[velocity_pid.py-9] [INFO] [1781492690.471681437] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.09 dt=0.0338s, resetting
[competition_master_stage3.py-19] [INFO] [1781492691.825144227] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.52,-0.51) yaw=120deg cmd=(vx=0.50 wz=-0.17) elapsed=52.7s plan[15pts 2.1m] (2.80,-0.75)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=56% mem=20%
[velocity_pid.py-9] [INFO] [1781492691.868894147] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.51 corrected=0.01 err=24.4%
[cmd_vel_mux.py-8] [INFO] [1781492691.871628274] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.08
[component_container_isolated-18] [WARN] [1781492691.892977713] [planner_server]: GridBased: failed to create plan, no valid path found.
[component_container_isolated-18] [WARN] [1781492691.893242755] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.10, 0.92)
[component_container_isolated-18] [WARN] [1781492691.893352755] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1781492692.046050035] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781492692.054730002] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781492692.066397805] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781492692.066622597] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781492692.073019604] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1781492692.073502396] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1781492692.081206070] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[velocity_pid.py-9] [INFO] [1781492692.107081388] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0386s, resetting
[velocity_pid.py-9] [INFO] [1781492692.901143692] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.12 corrected=-0.28 err=61.0%
[component_container_isolated-18] [WARN] [1781492692.901141359] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.8090 Hz
[component_container_isolated-18] [INFO] [1781492693.047789299] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781492693.169508755] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.06
[velocity_pid.py-9] [INFO] [1781492693.301210513] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0335s, resetting
[competition_master_stage3.py-19] [INFO] [1781492693.822523998] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.31,-0.00) yaw=113deg cmd=(vx=0.50 wz=-1.43) elapsed=54.7s plan[10pts 1.3m] (2.40,-0.05)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=43% mem=20%
[velocity_pid.py-9] [INFO] [1781492693.942540911] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.16 corrected=0.41 err=67.4%
[imu_madgwick_filter.py-4] [INFO] [1781492694.664284723] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1588 q_w=0.6842 angle=93.7deg beta=0.0330
[velocity_pid.py-9] [INFO] [1781492694.867327136] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.09 dt=0.0336s, resetting
[imu_madgwick_filter.py-6] [INFO] [1781492694.905787883] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3891 q_w=0.8981 angle=52.2deg beta=0.0030
[cmd_vel_mux.py-8] [INFO] [1781492695.468718409] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.61
[velocity_pid.py-9] [INFO] [1781492695.505688487] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.50 corrected=-0.06 err=55.3%
[velocity_pid.py-9] [INFO] [1781492695.711589736] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0426s, resetting
[competition_master_stage3.py-19] [INFO] [1781492695.822352931] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.43,0.59) yaw=89deg cmd=(vx=-0.11 wz=0.05) elapsed=56.7s plan[10pts 1.3m] (2.40,-0.05)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=57% mem=20%
[component_container_isolated-18] [WARN] [1781492695.892885169] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1781492695.893191336] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.10, 0.92)
[component_container_isolated-18] [WARN] [1781492695.893301461] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1781492696.046119865] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781492696.059337170] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781492696.069883472] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781492696.070067306] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781492696.072122474] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1781492696.072512308] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1781492696.083942486] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[velocity_pid.py-9] [INFO] [1781492696.534658773] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.16 corrected=-0.25 err=47.7%
[component_container_isolated-18] [WARN] [1781492696.902938893] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.8109 Hz
[component_container_isolated-18] [INFO] [1781492697.047853414] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781492697.202370569] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.04
[velocity_pid.py-9] [INFO] [1781492697.239427272] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.09 -> current=0.04 dt=0.0332s, resetting
[velocity_pid.py-9] [INFO] [1781492697.301275543] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0336s, resetting
[velocity_pid.py-9] [INFO] [1781492697.545032287] [velocity_pid]: [vel_pid→] desired=0.36 actual=-0.13 corrected=0.39 err=136.1%
[competition_master_stage3.py-19] [INFO] [1781492697.830020323] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.42,0.59) yaw=91deg cmd=(vx=0.50 wz=0.61) elapsed=58.7s plan[9pts 1.0m] (2.40,0.65)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=17% mem=20%
[cmd_vel_mux.py-8] [INFO] [1781492698.907341903] [cmd_vel_mux]: [mux→] src=nav vx=0.40 wz=1.67
[velocity_pid.py-9] [INFO] [1781492698.939017893] [velocity_pid]: [vel_pid→] desired=0.40 actual=0.48 corrected=0.12 err=21.6%
[component_container_isolated-18] [INFO] [1781492699.148703269] [controller_server]: Reached the goal!
[competition_master_stage3.py-19] [INFO] [1781492699.821833276] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.08,1.06) yaw=151deg cmd=(vx=0.00 wz=0.04) elapsed=60.7s plan[9pts 1.0m] (2.40,0.65)→(2.10,0.95) cpuFreq=1500MHz cpuT=71C cpu=58% mem=20%
[component_container_isolated-18] [WARN] [1781492699.893255472] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3465 Hz
[component_container_isolated-18] [WARN] [1781492699.894409640] [BehaviorTreeEngine]: Behavior Tree tick rate 10.00 was exceeded!
[component_container_isolated-18] [INFO] [1781492699.895136766] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-19] [INFO] [1781492699.910475864] [competition_master_stage3]: [结果回调] 巡航完成, 到达VLM路点, 触发VLM推理...
[competition_master_stage3.py-19] [INFO] [1781492699.913499951] [competition_master_stage3]: [VLM] 发布 sign4return=100, 拍照推理中...
[competition_master_stage3.py-19] [INFO] [1781492699.917274996] [competition_master_stage3]: [状态机] CRUISE_CHANNEL → RETURN_P
[vision_ai_node-14] [INFO] [1781492699.917639580] [vision_ai_node]: Received sign4return: 100
[competition_master_stage3.py-19] [INFO] [1781492699.923679044] [competition_master_stage3]: [RETURN] 清除机器人周围1.5m + 直接返航至 P点 (-1.99,-0.01)
[vision_ai_node-14] [INFO] [1781492699.921333167] [vision_ai_node]: Received trigger signal (sign4return=100), subscribing to image topic...
[vision_ai_node-14] [INFO] [1781492699.966303587] [vision_ai_node]: Subscribed to /aurora/rgb/image_raw topic
[vision_ai_node-14] [INFO] [1781492700.016130720] [vision_ai_node]: Received compressed image, processing with AI model...
[competition_master_stage3.py-19] [INFO] [1781492700.433702845] [competition_master_stage3]: [DIAG] nav目标距离: 4.20m, robot=(2.08,1.06) → target=(-1.99,-0.01)
[competition_master_stage3.py-19] [INFO] [1781492700.438232225] [competition_master_stage3]: >>> 发送导航目标 [P点返航]: (-1.99, -0.01, yaw=2.64)
[component_container_isolated-18] [INFO] [1781492700.442586021] [bt_navigator]: Begin navigating from current location (2.03, 1.08) to (-1.99, -0.01)
[competition_master_stage3.py-19] [INFO] [1781492700.456004492] [competition_master_stage3]: 导航目标已接受，车辆出发...
[cmd_vel_mux.py-8] [INFO] [1781492700.672352958] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.52s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1781492700.678500756] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[component_container_isolated-18] [WARN] [1781492700.901043562] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 2.1975 Hz
[component_container_isolated-18] [INFO] [1781492701.044599663] [controller_server]: Received a goal, begin computing control effort.
[cmd_vel_mux.py-8] [INFO] [1781492701.069235688] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=0.12
[velocity_pid.py-9] [INFO] [1781492701.101634345] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.27 err=100.0%
[competition_master_stage3.py-19] [INFO] [1781492701.821751521] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.08,1.06) yaw=151deg cmd=(vx=0.50 wz=1.03) elapsed=62.7s plan[42pts 6.0m] (2.00,1.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=33% mem=20%
[velocity_pid.py-9] [INFO] [1781492703.000856944] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.02 err=22.7%
[cmd_vel_mux.py-8] [INFO] [1781492703.039225690] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.27
[velocity_pid.py-9] [INFO] [1781492703.206271398] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.02 -> current=-0.11 dt=0.0357s, resetting
[velocity_pid.py-9] [INFO] [1781492703.267312084] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0333s, resetting
[competition_master_stage3.py-19] [INFO] [1781492703.829860767] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.05,0.79) yaw=-131deg cmd=(vx=-0.30 wz=-0.62) elapsed=64.7s plan[42pts 6.0m] (2.00,1.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=38% mem=20%
[component_container_isolated-18] [WARN] [1781492703.897778960] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3344 Hz
[velocity_pid.py-9] [INFO] [1781492704.036676847] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.13 corrected=-0.26 err=56.7%
[component_container_isolated-18] [INFO] [1781492704.045021397] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781492704.136399780] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.35
[velocity_pid.py-9] [INFO] [1781492704.267568701] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781492704.301690027] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.10 -> current=0.03 dt=0.0340s, resetting
[imu_madgwick_filter.py-4] [INFO] [1781492704.665895388] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1784 q_w=-0.4660 angle=235.5deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781492704.906261293] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4393 q_w=-0.2126 angle=204.6deg beta=0.0030
[velocity_pid.py-9] [INFO] [1781492705.067836286] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.29 corrected=0.36 err=41.2%
[competition_master_stage3.py-19] [INFO] [1781492705.822055449] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.97,0.60) yaw=-114deg cmd=(vx=0.50 wz=0.81) elapsed=66.7s plan[35pts 4.9m] (1.20,0.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=62% mem=20%
[cmd_vel_mux.py-8] [INFO] [1781492706.004770880] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.49
[velocity_pid.py-9] [INFO] [1781492706.101156933] [velocity_pid]: [vel_pid→] desired=0.23 actual=0.48 corrected=-0.11 err=110.4%
[velocity_pid.py-9] [INFO] [1781492706.271638102] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0346s, resetting
[velocity_pid.py-9] [INFO] [1781492706.278232691] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.12 -> current=-0.01 dt=0.0346s, resetting
[component_container_isolated-18] [WARN] [1781492706.896109093] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3342 Hz
[component_container_isolated-18] [INFO] [1781492707.045172032] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781492707.104175215] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.84
[velocity_pid.py-9] [INFO] [1781492707.135271204] [velocity_pid]: [vel_pid→] desired=-0.12 actual=-0.16 corrected=0.02 err=35.8%
[velocity_pid.py-9] [INFO] [1781492707.270776421] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0338s, resetting
[competition_master_stage3.py-19] [INFO] [1781492707.822814007] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.95,0.18) yaw=-79deg cmd=(vx=0.50 wz=-0.54) elapsed=68.7s plan[30pts 3.9m] (0.90,0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=29% mem=20%
[velocity_pid.py-9] [INFO] [1781492708.167524305] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.34 corrected=0.33 err=32.0%
[velocity_pid.py-9] [INFO] [1781492709.236605315] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.00 err=22.7%
[cmd_vel_mux.py-8] [INFO] [1781492709.272051183] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.30
[velocity_pid.py-9] [INFO] [1781492709.501533700] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0331s, resetting
[competition_master_stage3.py-19] [INFO] [1781492709.823752058] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.92,-0.34) yaw=-107deg cmd=(vx=-0.30 wz=0.43) elapsed=70.7s plan[30pts 3.9m] (0.90,0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=57% mem=20%
[component_container_isolated-18] [WARN] [1781492709.894348794] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3364 Hz
[component_container_isolated-18] [INFO] [1781492710.045065109] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781492710.136529574] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.21
[velocity_pid.py-9] [INFO] [1781492710.269028454] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0339s, resetting
[velocity_pid.py-9] [INFO] [1781492710.273183583] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.09 -> current=-0.04 dt=0.0339s, resetting
[velocity_pid.py-9] [INFO] [1781492710.282777551] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.10 corrected=0.36 err=263.3%
[competition_master_stage3.py-19] [INFO] [1781492711.824935187] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.68,-0.74) yaw=-154deg cmd=(vx=0.50 wz=-0.97) elapsed=72.7s plan[22pts 3.1m] (0.80,-0.55)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=17% mem=20%
[velocity_pid.py-9] [INFO] [1781492712.601943321] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.01 -> current=0.11 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781492712.700478876] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.51 corrected=-0.03 err=24.4%
[cmd_vel_mux.py-8] [INFO] [1781492712.703797546] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.37
[component_container_isolated-18] [WARN] [1781492712.898078944] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3287 Hz
[velocity_pid.py-9] [INFO] [1781492712.968307554] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0329s, resetting
[component_container_isolated-18] [INFO] [1781492713.045082712] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781492713.237666692] [cmd_vel_mux]: [mux→] src=nav vx=0.16 wz=0.18
[velocity_pid.py-9] [INFO] [1781492713.703644355] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.23 corrected=0.21 err=53.0%
[competition_master_stage3.py-19] [INFO] [1781492713.831969813] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.08,-0.66) yaw=166deg cmd=(vx=0.50 wz=-0.10) elapsed=74.7s plan[16pts 2.2m] (0.10,-0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=91% mem=20%
[imu_madgwick_filter.py-4] [INFO] [1781492714.666185626] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1983 q_w=0.0111 angle=178.7deg beta=0.0330
[velocity_pid.py-9] [INFO] [1781492714.801800633] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.08 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781492714.807591514] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.14 err=22.7%
[cmd_vel_mux.py-8] [INFO] [1781492714.840024129] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.21
[imu_madgwick_filter.py-6] [INFO] [1781492714.907440486] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4892 q_w=0.3254 angle=142.0deg beta=0.0030
[velocity_pid.py-9] [INFO] [1781492715.034776069] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0338s, resetting
[competition_master_stage3.py-19] [INFO] [1781492715.825563356] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.52,-0.52) yaw=159deg cmd=(vx=-0.30 wz=0.01) elapsed=76.7s plan[16pts 2.2m] (0.10,-0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=78% mem=20%
[velocity_pid.py-9] [INFO] [1781492715.834038282] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.13 corrected=-0.26 err=56.7%
[component_container_isolated-18] [WARN] [1781492715.897692390] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3297 Hz
[component_container_isolated-18] [INFO] [1781492716.045015030] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781492716.101791507] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.02 -> current=-0.10 dt=0.0344s, resetting
[cmd_vel_mux.py-8] [INFO] [1781492716.142731163] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.19
[velocity_pid.py-9] [INFO] [1781492716.267467637] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0331s, resetting
[velocity_pid.py-9] [INFO] [1781492716.867571043] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.13 corrected=0.46 err=74.0%
[competition_master_stage3.py-19] [INFO] [1781492717.822852041] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.77,-0.44) yaw=160deg cmd=(vx=0.50 wz=0.03) elapsed=78.7s plan[10pts 1.4m] (-0.70,-0.45)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=71C cpu=62% mem=20%
[velocity_pid.py-9] [INFO] [1781492718.601209886] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.51 corrected=-0.00 err=24.4%
[cmd_vel_mux.py-8] [INFO] [1781492718.603880391] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.03
[velocity_pid.py-9] [INFO] [1781492718.867474694] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0327s, resetting
[component_container_isolated-18] [WARN] [1781492718.916597824] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3015 Hz
[component_container_isolated-18] [INFO] [1781492719.045030427] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781492719.101417694] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.00 -> current=-0.12 dt=0.0328s, resetting
[cmd_vel_mux.py-8] [INFO] [1781492719.134970337] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.25
[velocity_pid.py-9] [INFO] [1781492719.234245181] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0327s, resetting
[velocity_pid.py-9] [INFO] [1781492719.634144475] [velocity_pid]: [vel_pid→] desired=0.22 actual=0.06 corrected=0.13 err=70.4%
[competition_master_stage3.py-19] [INFO] [1781492719.824661022] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.47,-0.21) yaw=160deg cmd=(vx=0.22 wz=-0.37) elapsed=80.7s plan[4pts 0.5m] (-1.40,-0.15)→(-1.84,-0.01) cpuFreq=1500MHz cpuT=71C cpu=38% mem=20%
[component_container_isolated-18] [INFO] [1781492720.545630470] [controller_server]: Reached the goal!
[cmd_vel_mux.py-8] [INFO] [1781492720.571217349] [cmd_vel_mux]: [mux→] src=nav vx=0.05 wz=-0.04
[velocity_pid.py-9] [INFO] [1781492720.637222758] [velocity_pid]: [vel_pid→] desired=0.05 actual=0.17 corrected=-0.04 err=228.1%
[component_container_isolated-18] [INFO] [1781492721.043708438] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-19] [INFO] [1781492721.054124956] [competition_master_stage3]: [结果回调] 已回到P点, 任务完成!
[competition_master_stage3.py-19] [INFO] [1781492721.063320097] [competition_master_stage3]: [状态机] RETURN_P → DONE
[competition_master_stage3.py-19] [INFO] [1781492721.067758064] [competition_master_stage3]:
[competition_master_stage3.py-19] [INFO] [1781492721.071218903] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1781492721.074491659] [competition_master_stage3]: >>> [Stage 3] 任务结束 <<<
[competition_master_stage3.py-19] [INFO] [1781492721.077633748] [competition_master_stage3]:   最终状态: DONE
[cmd_vel_mux.py-8] [INFO] [1781492721.079627585] [cmd_vel_mux]: [mux→] src=stop vx=0.00 wz=0.00
[competition_master_stage3.py-19] [INFO] [1781492721.080882920] [competition_master_stage3]:   总耗时:   82.0s
[competition_master_stage3.py-19] [INFO] [1781492721.083865717] [competition_master_stage3]:   --- 各阶段耗时 ---
[competition_master_stage3.py-19] [INFO] [1781492721.086786556] [competition_master_stage3]:   LAUNCH................ 15.3s
[competition_master_stage3.py-19] [INFO] [1781492721.089892728] [competition_master_stage3]:   NAV_TO_QR............. 13.0s
[competition_master_stage3.py-19] [INFO] [1781492721.092676608] [competition_master_stage3]:   BACKING_UP............ 6.0s
[competition_master_stage3.py-19] [INFO] [1781492721.095711072] [competition_master_stage3]:   CRUISE_CHANNEL........ 41.8s
[competition_master_stage3.py-19] [INFO] [1781492721.099051786] [competition_master_stage3]:   RETURN_P.............. 21.1s
[competition_master_stage3.py-19] [INFO] [1781492721.102286667] [competition_master_stage3]:   (transition/overhead). -15.3s
[competition_master_stage3.py-19] [INFO] [1781492721.105565589] [competition_master_stage3]:   --- ---
[competition_master_stage3.py-19] [INFO] [1781492721.108776303] [competition_master_stage3]:   QR 原始数据: 1584
[competition_master_stage3.py-19] [INFO] [1781492721.111986184] [competition_master_stage3]:   QR 方向:   逆时针 (CW=顺时针/odd, CCW=逆时针/even)
[competition_master_stage3.py-19] [WARN] [1781492721.115352148] [competition_master_stage3]:   VLM 结果:  未收到
[competition_master_stage3.py-19] [INFO] [1781492721.118452528] [competition_master_stage3]:   超时限制:  180.0s (全局)
[competition_master_stage3.py-19] [INFO] [1781492721.121164450] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1781492721.126538876] [competition_master_stage3]: [TRAJ] 轨迹已保存: /userdata/dev_ws/trajectory.csv (105 点)
[competition_master_stage3.py-19] [INFO] [1781492721.825159115] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.67,-0.16) yaw=152deg cmd=(vx=0.00 wz=0.00) elapsed=82.7s plan[4pts 0.5m] (-1.40,-0.15)→(-1.84,-0.01) cpuFreq=1500MHz cpuT=71C cpu=60% mem=20%
[cmd_vel_mux.py-8] [INFO] [1781492722.034844028] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.53s > 0.5s, marked inactive
[competition_master_stage3.py-19] [INFO] [1781492723.822897314] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.67,-0.16) yaw=152deg cmd=(vx=0.00 wz=0.00) elapsed=84.7s plan[4pts 0.5m] (-1.40,-0.15)→(-1.84,-0.01) cpuFreq=1500MHz cpuT=71C cpu=64% mem=20%
[imu_madgwick_filter.py-4] [INFO] [1781492724.663328838] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2182 q_w=0.0960 angle=169.0deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781492724.908799729] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5390 q_w=0.4258 angle=129.6deg beta=0.0030
[competition_master_stage3.py-19] [INFO] [1781492725.833016648] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.67,-0.16) yaw=152deg cmd=(vx=0.00 wz=0.00) elapsed=86.7s plan[4pts 0.5m] (-1.40,-0.15)→(-1.84,-0.01) cpuFreq=1500MHz cpuT=72C cpu=43% mem=20%
^C[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[rviz2-20] [INFO] [1781492725.892054794] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [lslidar_driver_node-2]: process has died [pid 32554, exit code -6, cmd '/userdata/dev_ws/install/lslidar_driver/lib/lslidar_driver/lslidar_driver_node --ros-args -r __node:=lslidar_driver_node --params-file /userdata/dev_ws/install/lslidar_driver/share/lslidar_driver/params/lsx10.yaml'].
[ERROR] [origincar_base_node-1]: process has died [pid 32552, exit code -6, cmd '/userdata/dev_ws/install/origincar_base/lib/origincar_base/origincar_base_node --ros-args --params-file /tmp/launch_params_5m2ijr_n --params-file /tmp/launch_params_g5cic6bn'].
[INFO] [map_server-15]: process has finished cleanly [pid 32732]
[INFO] [costmap_filter_info_server-16]: process has finished cleanly [pid 32735]
[INFO] [robot_state_publisher-3]: process has finished cleanly [pid 32556]
[INFO] [ekf_node-7]: process has finished cleanly [pid 32564]
[INFO] [lifecycle_manager-17]: process has finished cleanly [pid 32737]
[INFO] [static_transform_publisher-10]: process has finished cleanly [pid 32614]
[ERROR] [rviz2-20]: process has died [pid 32912, exit code -11, cmd '/opt/ros/humble/lib/rviz2/rviz2 -d /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/rviz/nav.rviz --ros-args -r __node:=rviz2'].
[INFO] [velocity_pid.py-9]: process has finished cleanly [pid 32588]
[INFO] [imu_madgwick_filter.py-6]: process has finished cleanly [pid 32562]
[map_server-15] [INFO] [1781492725.892138502] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-15] [INFO] [1781492725.892383336] [keepout_mask_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_mask_server)
[map_server-15] [INFO] [1781492725.892665087] [keepout_mask_server]: Deactivating
[map_server-15] [INFO] [1781492725.892755462] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[static_transform_publisher-10] [INFO] [1781492725.892137336] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-16] [INFO] [1781492725.892300961] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-16] [INFO] [1781492725.892522045] [keepout_filter_info_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_filter_info_server)
[costmap_filter_info_server-16] [INFO] [1781492725.892772462] [keepout_filter_info_server]: Deactivating
[costmap_filter_info_server-16] [INFO] [1781492725.892945545] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[lifecycle_manager-17] [INFO] [1781492725.892570711] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-17] [INFO] [1781492725.892786378] [lifecycle_manager_keepout]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_keepout)
[lifecycle_manager-17] [INFO] [1781492725.892899379] [lifecycle_manager_keepout]: Terminating bond timer...
[component_container_isolated-18] [INFO] [1781492725.892563045] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-18] [INFO] [1781492725.892724712] [lifecycle_manager_navigation]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_navigation)
[component_container_isolated-18] [INFO] [1781492725.892956920] [lifecycle_manager_navigation]: Terminating bond timer...
[aurora930_node-11] [INFO] [1781492725.892926754] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[robot_state_publisher-3] [INFO] [1781492725.893544505] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1781492725.895624258] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1781492725.896138968] [origincar_base]: Stop command sent to STM32 on shutdown.
[origincar_base_node-1] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[origincar_base_node-1] terminate called after throwing an instance of 'rclcpp::exceptions::RCLError'
[origincar_base_node-1]   what():  failed to create guard condition: the given context is not valid, either rcl_init() was not called or rcl_shutdown() was called., at ./src/rcl/guard_condition.c:67
[ekf_node-7] [INFO] [1781492725.895686259] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[INFO] [imu_madgwick_filter.py-4]: process has finished cleanly [pid 32558]
[INFO] [cmd_vel_mux.py-8]: process has finished cleanly [pid 32570]
[costmap_filter_info_server-16] [INFO] [1781492725.904470482] [keepout_filter_info_server]: Cleaning up
[costmap_filter_info_server-16] [INFO] [1781492725.904724691] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-16] [INFO] [1781492726.160674433] [keepout_filter_info_server]: Destroying
[aurora930_node-11] I0615 11:05:25.917764 32616 ros2_node.cc:90] process quit succeed
[aurora930_node-11] I0615 11:05:25.917984 32616 aurora900_ros2_device.cc:83] begin stop()
[aurora930_node-11] I0615 11:05:25.948776 32616 aurora900_ros2_device.cc:103] stop stream
[aurora930_node-11] 2026-06-15 11:05:26.061 ( 112.279s) [        ACFD4020]      aurora900_impl.cc:648   INFO| ir_stream_count_=0, rgb_stream_count_=0, depth_stream_count_=0
[aurora930_node-11] 2026-06-15 11:05:26.061 ( 112.279s) [        ACFD4020]      aurora900_impl.cc:649   INFO| mask=7
[aurora930_node-11] I0615 11:05:26.268875 32616 aurora900_ros2_device.cc:105] destroy stream
[aurora930_node-11] I0615 11:05:26.269120 32616 aurora900_ros2_device.cc:110] close glog
[aurora930_node-11] WARNING: Logging before InitGoogleLogging() is written to STDERR
[aurora930_node-11] I0615 11:05:26.269300 32616 ros2_device.cc:113] close device...
[aurora930_node-11] 2026-06-15 11:05:26.766 ( 112.984s) [        7D9E37E0]         cmd_backend.cc:40    INFO| RunBlocking is end!!!
[aurora930_node-11] 2026-06-15 11:05:26.967 ( 113.185s) [        ACFD4020]deptrum_camera_vendor.c:121   INFO| device is close.
[aurora930_node-11] I0615 11:05:26.970340 32616 ros2_device.cc:116] quit succeed
[map_server-15] [INFO] [1781492725.918602174] [keepout_mask_server]: Cleaning up
[map_server-15] [INFO] [1781492725.918838008] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[map_server-15] [INFO] [1781492726.171768536] [keepout_mask_server]: Destroying
[vision_ai_node-14] [INFO] [1781492725.991064551] [vision_ai_node]: Unsubscribed from image topic
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
[component_container_isolated-18] [INFO] [1781492726.181391053] [local_costmap.local_costmap]: Message Filter dropping message: frame 'laser_link' at time 1781492725.880 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-18] [INFO] [1781492726.453859948] [velocity_smoother]: Running Nav2 LifecycleNode rcl preshutdown (velocity_smoother)
[component_container_isolated-18] [INFO] [1781492726.454231574] [velocity_smoother]: Deactivating
[component_container_isolated-18] [INFO] [1781492726.454365782] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492726.465080759] [velocity_smoother]: Cleaning up
[component_container_isolated-18] [INFO] [1781492726.465344676] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492726.465419885] [behavior_server]: Running Nav2 LifecycleNode rcl preshutdown (behavior_server)
[component_container_isolated-18] [INFO] [1781492726.465526177] [behavior_server]: Deactivating
[component_container_isolated-18] [INFO] [1781492726.465627385] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492726.476036362] [behavior_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781492726.516104307] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492726.516301183] [lifecycle_manager_localization]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_localization)
[component_container_isolated-18] [INFO] [1781492726.516415641] [lifecycle_manager_localization]: Terminating bond timer...
[component_container_isolated-18] [INFO] [1781492726.576923122] [waypoint_follower]: Running Nav2 LifecycleNode rcl preshutdown (waypoint_follower)
[component_container_isolated-18] [INFO] [1781492726.577187165] [waypoint_follower]: Deactivating
[component_container_isolated-18] [INFO] [1781492726.577383082] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492726.587792183] [waypoint_follower]: Cleaning up
[component_container_isolated-18] [INFO] [1781492726.617440944] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492726.617610444] [planner_server]: Running Nav2 LifecycleNode rcl preshutdown (planner_server)
[component_container_isolated-18] [INFO] [1781492726.617740611] [planner_server]: Deactivating
[component_container_isolated-18] [INFO] [1781492726.617990361] [global_costmap.global_costmap]: Deactivating
[component_container_isolated-18] [INFO] [1781492726.880773531] [amcl]: Message Filter dropping message: frame 'laser_link' at time 1781492725.880 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-18] [INFO] [1781492726.886237833] [planner_server]: Deactivating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781492726.886482458] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492726.896938060] [planner_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781492726.931743079] [global_costmap.global_costmap]: Cleaning up
[component_container_isolated-18] [INFO] [1781492726.946135730] [planner_server]: Cleaning up plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781492726.947274815] [planner_server]: Destroying plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781492726.989207139] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492726.989367097] [smoother_server]: Running Nav2 LifecycleNode rcl preshutdown (smoother_server)
[component_container_isolated-18] [INFO] [1781492726.989501306] [smoother_server]: Deactivating
[component_container_isolated-18] [INFO] [1781492726.989560972] [smoother_server]: Deactivating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781492726.989707014] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492727.000135158] [smoother_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781492727.000298616] [smoother_server]: Cleaning up smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781492727.033765217] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492727.033928217] [bt_navigator]: Running Nav2 LifecycleNode rcl preshutdown (bt_navigator)
[component_container_isolated-18] [INFO] [1781492727.034081301] [bt_navigator]: Deactivating
[component_container_isolated-18] [INFO] [1781492727.034263509] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492727.044656319] [bt_navigator]: Cleaning up
[component_container_isolated-18] [INFO] [1781492727.433251584] [bt_navigator]: Completed Cleaning up
[component_container_isolated-18] [INFO] [1781492727.433483543] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492727.433684335] [map_server]: Running Nav2 LifecycleNode rcl preshutdown (map_server)
[component_container_isolated-18] [INFO] [1781492727.433817627] [map_server]: Deactivating
[component_container_isolated-18] [INFO] [1781492727.433966627] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492727.444343854] [map_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781492727.444556896] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492727.444624979] [amcl]: Running Nav2 LifecycleNode rcl preshutdown (amcl)
[component_container_isolated-18] [INFO] [1781492727.444737938] [amcl]: Deactivating
[component_container_isolated-18] [INFO] [1781492727.444879604] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492727.455238956] [amcl]: Cleaning up
[lifecycle_manager-17] [INFO] [1781492726.195123910] [lifecycle_manager_keepout]: Destroying lifecycle_manager_keepout
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
[component_container_isolated-18] [INFO] [1781492727.467193019] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492727.467344936] [controller_server]: Running Nav2 LifecycleNode rcl preshutdown (controller_server)
[component_container_isolated-18] [INFO] [1781492727.467477811] [controller_server]: Deactivating
[component_container_isolated-18] [INFO] [1781492727.467544186] [controller_server]: Deactivating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781492727.467768270] [local_costmap.local_costmap]: Deactivating
[component_container_isolated-18] [INFO] [1781492727.553327628] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781492727.563796771] [controller_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781492727.563939397] [controller_server]: Cleaning up controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781492727.564221939] [local_costmap.local_costmap]: Cleaning up
[INFO] [competition_master_stage3.py-19]: process has finished cleanly [pid 32908]
[ERROR] [bmi088_iio_bridge.py-5]: process has died [pid 32560, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/bmi088_iio_bridge.py --ros-args -r __node:=bmi088_iio_bridge --params-file /tmp/launch_params__z1e2y5g'].
[INFO] [aurora930_node-11]: process has finished cleanly [pid 32616]
[ERROR] [vision_ai_node-14]: process has died [pid 32631, exit code 1, cmd '/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node --ros-args -r __node:=vision_ai_node'].
[component_container_isolated-18] [INFO] [1781492728.604865012] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
