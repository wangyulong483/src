root@ubuntu:/userdata/dev_ws# ros2 launch origincar_bringup stage3_bringup.launch.py
[INFO] [launch]: All log files can be found below /root/.ros/log/2026-06-14-17-54-16-311598-ubuntu-26677
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [origincar_base_node-1]: process started with pid [26691]
[INFO] [lslidar_driver_node-2]: process started with pid [26693]
[INFO] [robot_state_publisher-3]: process started with pid [26695]
[INFO] [imu_madgwick_filter.py-4]: process started with pid [26697]
[INFO] [bmi088_iio_bridge.py-5]: process started with pid [26699]
[INFO] [imu_madgwick_filter.py-6]: process started with pid [26701]
[INFO] [ekf_node-7]: process started with pid [26703]
[INFO] [cmd_vel_mux.py-8]: process started with pid [26709]
[INFO] [velocity_pid.py-9]: process started with pid [26727]
[INFO] [static_transform_publisher-10]: process started with pid [26747]
[INFO] [aurora930_node-11]: process started with pid [26749]
[INFO] [qr_decoder-12]: process started with pid [26751]
[INFO] [qr_decision-13]: process started with pid [26753]
[INFO] [vision_ai_node-14]: process started with pid [26757]
[origincar_base_node-1] [INFO] [1781430857.056895071] [origincar_base]: origincar_base serial port opened
[lslidar_driver_node-2] [INFO] [1781430857.046294276] [lslidar_driver_node]: Lidar is N10
[lslidar_driver_node-2] [INFO] [1781430857.061622471] [lslidar_driver_node]: Initialised lslidar without error
[lslidar_driver_node-2] [INFO] [1781430857.061849137] [lslidar_driver_node]: Successfully initialize driver...
[robot_state_publisher-3] [INFO] [1781430857.143759759] [robot_state_publisher]: got segment base_footprint
[robot_state_publisher-3] [INFO] [1781430857.144295965] [robot_state_publisher]: got segment base_link
[robot_state_publisher-3] [INFO] [1781430857.144433215] [robot_state_publisher]: got segment gyro_link
[robot_state_publisher-3] [INFO] [1781430857.144895338] [robot_state_publisher]: got segment laser_link
[ekf_node-7] Both imu1_differential and imu1_relative were set to true. Using differential mode.
[static_transform_publisher-10] [INFO] [1781430857.344243205] [depth_camera_tf]: Spinning until stopped - publishing transform
[static_transform_publisher-10] translation: ('0.140000', '0.000000', '0.050000')
[static_transform_publisher-10] rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
[static_transform_publisher-10] from 'base_link' to 'depth_camera_link'
[aurora930_node-11] W0614 17:54:17.864667 26749 ros2_node.cc:35] hello aurora 900/930
[qr_decoder-12] [INFO] [1781430857.910816002] [qr_decoder_zbar]: QR decoder (ZBar) started: rgb=/aurora/rgb/image_raw, depth=/aurora/depth/image_raw, filter=on, range=[50, 4000]mm, min_qr_len=1, intrinsics: fx=421.3 fy=422.3 cx=320.3 cy=197.0
[aurora930_node-11] 2026-06-14 17:54:17.959 (   0.289s) [        9B7D4020] device_manager_impl.cc:89    INFO| hotplug has registed by user
[aurora930_node-11] device_count==========1
[aurora930_node-11] I0614 17:54:18.020083 26749 aurora900_ros2_device.cc:153] BOOT_ORDER_1::Found 1 deptrum device
[aurora930_node-11] I0614 17:54:18.025060 26749 aurora900_ros2_device.cc:162] BOOT_ORDER_1::No serial number provided: picking first device
[aurora930_node-11] 2026-06-14 17:54:18.025 (   0.354s) [        9B7D4020] device_manager_impl.cc:318   INFO| Device information:
[aurora930_node-11]     ir_pid:0x1930, rgb_pid:0x0
[aurora930_node-11]     serial number:HY400529001015314G00248
[aurora930_node-11] I0614 17:54:18.025345 26749 aurora900_ros2_device.cc:206] BOOT_ORDER_1::0:device start opening
[aurora930_node-11] 2026-06-14 17:54:18.033 (   0.362s) [        9B7D4020]   custom_usb_device.cc:101   INFO| bulk in endpoint addr:129
[aurora930_node-11] 2026-06-14 17:54:18.033 (   0.362s) [        9B7D4020]   custom_usb_device.cc:98    INFO| bulk out endpoint addr:2
[aurora930_node-11] 2026-06-14 17:54:18.061 (   0.390s) [        9B7D4020]deptrum_camera_aurora93:53    INFO| doe_broken:0 ito_support:1 crash_count:0 wdt_count:0 hard_reset_count:2 heart_boot_count:0 boot_total:95 last_crash_time:N
[aurora930_node-11] I0614 17:54:18.061120 26749 aurora900_ros2_device.cc:247] device supported frame_mode:
[aurora930_node-11] I0614 17:54:18.061235 26749 aurora900_ros2_device.cc:252] [0]:ir_mode:=13 kRes320x200Ir8Bit rgb_mode:=31 kRes320x200RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0614 17:54:18.061300 26749 aurora900_ros2_device.cc:252] [1]:ir_mode:=17 kRes480x300Depth16Bit rgb_mode:=32 kRes480x300RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0614 17:54:18.061342 26749 aurora900_ros2_device.cc:252] [2]:ir_mode:=20 kRes640x400Ir8Bit rgb_mode:=33 kRes640x400RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0614 17:54:18.061378 26749 aurora900_ros2_device.cc:266] current set mode ir_mode:20:kRes640x400Ir8Bit,rgb_mode:33:kRes640x400RgbYuv
[INFO] [map_server-15]: process started with pid [26855]
[INFO] [costmap_filter_info_server-16]: process started with pid [26857]
[INFO] [lifecycle_manager-17]: process started with pid [26861]
[aurora930_node-11] I0614 17:54:18.515122 26749 aurora900_ros2_device.cc:387] Switch Auto Exposure
[aurora930_node-11] 2026-06-14 17:54:18.569 (   0.899s) [        9B7D4020]      aurora900_impl.cc:1106  INFO| SetHeartbeat user set heartbeat enable: 0
[lifecycle_manager-17] [INFO] [1781430858.621239416] [lifecycle_manager_keepout]: Creating
[costmap_filter_info_server-16] [INFO] [1781430858.636969318] [costmap_filter_info_server]: This is costmap filter info publisher
[lifecycle_manager-17] [INFO] [1781430858.670066699] [lifecycle_manager_keepout]: Creating and initializing lifecycle service clients
[map_server-15] [INFO] [1781430858.707712023] [keepout_mask_server]:
[map_server-15]         keepout_mask_server lifecycle node launched.
[map_server-15]         Waiting on external lifecycle transitions to activate
[map_server-15]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[map_server-15] [INFO] [1781430858.709263226] [keepout_mask_server]: Creating
[costmap_filter_info_server-16] [INFO] [1781430858.792495553] [keepout_filter_info_server]:
[costmap_filter_info_server-16]         keepout_filter_info_server lifecycle node launched.
[costmap_filter_info_server-16]         Waiting on external lifecycle transitions to activate
[costmap_filter_info_server-16]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[aurora930_node-11] I0614 17:54:18.982183 26749 aurora900_ros2_device.cc:304] BOOT_ORDER_1::Device information:
[aurora930_node-11] I0614 17:54:18.982352 26749 aurora900_ros2_device.cc:305]    sdk version: 1.1.22
[aurora930_node-11] I0614 17:54:18.982424 26749 aurora900_ros2_device.cc:306]    device name: Aurora 930
[aurora930_node-11] I0614 17:54:18.982470 26749 aurora900_ros2_device.cc:307]    serial number: HY400529001015314G00248
[aurora930_node-11] I0614 17:54:18.982502 26749 aurora900_ros2_device.cc:308]    firmware version: 1.7.2
[aurora930_node-11] I0614 17:54:18.982563 26749 camera_parameters.cc:134] BOOT_ORDER_1::Camera Parameters:
[aurora930_node-11] I0614 17:54:18.982596 26749 camera_parameters.cc:135] BOOT_ORDER_1::         Ir Intrinsics:
[aurora930_node-11] I0614 17:54:18.982625 26749 camera_parameters.cc:146]                Resolution:
[aurora930_node-11] I0614 17:54:18.982651 26749 camera_parameters.cc:147]                        Rows:400
[aurora930_node-11] I0614 17:54:18.982676 26749 camera_parameters.cc:148]                        Cols:640
[aurora930_node-11] I0614 17:54:18.982702 26749 camera_parameters.cc:149]                Intrinsics:
[aurora930_node-11] I0614 17:54:18.982726 26749 camera_parameters.cc:150]                        fx: 421.307
[aurora930_node-11] I0614 17:54:18.982829 26749 camera_parameters.cc:151]                        fy: 422.254
[aurora930_node-11] I0614 17:54:18.982870 26749 camera_parameters.cc:152]                        cx: 320.27
[aurora930_node-11] I0614 17:54:18.982904 26749 camera_parameters.cc:153]                        cy: 197.01
[aurora930_node-11] I0614 17:54:18.982972 26749 camera_parameters.cc:154]                        k1: 0.0606853
[aurora930_node-11] I0614 17:54:18.983021 26749 camera_parameters.cc:155]                        k2: -0.10961
[aurora930_node-11] I0614 17:54:18.983052 26749 camera_parameters.cc:156]                        p1: 0.00126689
[aurora930_node-11] I0614 17:54:18.983084 26749 camera_parameters.cc:157]                        p2: -0.00120539
[aurora930_node-11] I0614 17:54:18.983116 26749 camera_parameters.cc:158]                        k3: 0.0522281
[aurora930_node-11] I0614 17:54:18.983173 26749 camera_parameters.cc:138] BOOT_ORDER_1::         Rgb Intrinsics:
[aurora930_node-11] I0614 17:54:18.983201 26749 camera_parameters.cc:146]                Resolution:
[aurora930_node-11] I0614 17:54:18.983227 26749 camera_parameters.cc:147]                        Rows:400
[aurora930_node-11] I0614 17:54:18.983251 26749 camera_parameters.cc:148]                        Cols:640
[aurora930_node-11] I0614 17:54:18.983276 26749 camera_parameters.cc:149]                Intrinsics:
[aurora930_node-11] I0614 17:54:18.983300 26749 camera_parameters.cc:150]                        fx: 416.49
[aurora930_node-11] I0614 17:54:18.983333 26749 camera_parameters.cc:151]                        fy: 417.383
[aurora930_node-11] I0614 17:54:18.983373 26749 camera_parameters.cc:152]                        cx: 316.832
[aurora930_node-11] I0614 17:54:18.983405 26749 camera_parameters.cc:153]                        cy: 188.753
[aurora930_node-11] I0614 17:54:18.983444 26749 camera_parameters.cc:154]                        k1: 0.00611878
[aurora930_node-11] I0614 17:54:18.983476 26749 camera_parameters.cc:155]                        k2: -0.0490436
[aurora930_node-11] I0614 17:54:18.983507 26749 camera_parameters.cc:156]                        p1: 0.000399548
[aurora930_node-11] I0614 17:54:18.983544 26749 camera_parameters.cc:157]                        p2: 0.000563892
[aurora930_node-11] I0614 17:54:18.983886 26749 camera_parameters.cc:158]                        k3: 0.0308458
[aurora930_node-11] I0614 17:54:18.983933 26749 camera_parameters.cc:141] BOOT_ORDER_1::         Ir to Rgb Extrinsic:
[aurora930_node-11] I0614 17:54:18.983963 26749 camera_parameters.cc:162]                Extrinsics:
[aurora930_node-11] I0614 17:54:18.983989 26749 camera_parameters.cc:163]                        Rotation[0]: 0.999973, 0.00724076, -0.00112023
[aurora930_node-11] I0614 17:54:18.984026 26749 camera_parameters.cc:165]                        Rotation[1]: -0.00724006, 0.999973, 0.000633162
[aurora930_node-11] I0614 17:54:18.984063 26749 camera_parameters.cc:167]                        Rotation[2]: 0.00112478, -0.000625033, 0.999999
[aurora930_node-11] I0614 17:54:18.984145 26749 camera_parameters.cc:169]                        Translation: -9.88662, 0.117748, 0.603513
[aurora930_node-11] 2026-06-14 17:54:18.984 (   1.314s) [        9B7D4020]      aurora900_impl.cc:578   INFO| stream_mask_:0, rgb_stream_count_:1
[lifecycle_manager-17] [INFO] [1781430859.004783626] [lifecycle_manager_keepout]: Starting managed nodes bringup...
[lifecycle_manager-17] [INFO] [1781430859.005456832] [lifecycle_manager_keepout]: Configuring keepout_mask_server
[map_server-15] [INFO] [1781430859.008639487] [keepout_mask_server]: Configuring
[map_server-15] [INFO] [1781430859.009142902] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.yaml
[map_server-15] [INFO] [1781430859.010771188] [map_io]: resolution: 0.05
[map_server-15] [INFO] [1781430859.010861604] [map_io]: origin[0]: -2.65
[map_server-15] [INFO] [1781430859.010892688] [map_io]: origin[1]: -4.5
[map_server-15] [INFO] [1781430859.010920354] [map_io]: origin[2]: 0
[map_server-15] [INFO] [1781430859.010949812] [map_io]: free_thresh: 0.5
[map_server-15] [INFO] [1781430859.010978771] [map_io]: occupied_thresh: 0.5
[map_server-15] [INFO] [1781430859.011014895] [map_io]: mode: scale
[map_server-15] [INFO] [1781430859.011046229] [map_io]: negate: 0
[map_server-15] [INFO] [1781430859.012165808] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm
[map_server-15] [INFO] [1781430859.045084441] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm: 163 X 141 map @ 0.05 m/cell
[lifecycle_manager-17] [INFO] [1781430859.114409110] [lifecycle_manager_keepout]: Configuring keepout_filter_info_server
[costmap_filter_info_server-16] [INFO] [1781430859.115997854] [keepout_filter_info_server]: Configuring
[lifecycle_manager-17] [INFO] [1781430859.136306699] [lifecycle_manager_keepout]: Activating keepout_mask_server
[map_server-15] [INFO] [1781430859.137198904] [keepout_mask_server]: Activating
[map_server-15] [INFO] [1781430859.137516069] [keepout_mask_server]: Creating bond (keepout_mask_server) to lifecycle manager.
[cmd_vel_mux.py-8] [INFO] [1781430859.196783483] [cmd_vel_mux]:   nav: /nav_cmd_vel priority=10 timeout=0.5s
[cmd_vel_mux.py-8] [INFO] [1781430859.220704773] [cmd_vel_mux]:   pid: /pid_cmd_vel priority=20 timeout=0.3s
[lifecycle_manager-17] [INFO] [1781430859.254956692] [lifecycle_manager_keepout]: Server keepout_mask_server connected with bond.
[lifecycle_manager-17] [INFO] [1781430859.255127941] [lifecycle_manager_keepout]: Activating keepout_filter_info_server
[costmap_filter_info_server-16] [INFO] [1781430859.255961314] [keepout_filter_info_server]: Activating
[costmap_filter_info_server-16] [INFO] [1781430859.256212146] [keepout_filter_info_server]: Creating bond (keepout_filter_info_server) to lifecycle manager.
[cmd_vel_mux.py-8] [INFO] [1781430859.257923890] [cmd_vel_mux]:   stop: /stop_cmd_vel priority=255 timeout=0.5s
[cmd_vel_mux.py-8] [INFO] [1781430859.287757283] [cmd_vel_mux]: cmd_vel_mux 就绪: 输出 → /cmd_vel_muxed
[aurora930_node-11] 2026-06-14 17:54:19.316 (   1.646s) [        67FF57E0]deptrum_camera_aurora93:407    ERR| recv first frame time is 1781430859316
[cmd_vel_mux.py-8] [INFO] [1781430859.322501826] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[imu_madgwick_filter.py-4] [INFO] [1781430859.335025615] [imu_madgwick_filter]: [imu_madgwick] init: beta=0.0330, gyro_noise=0.0010, accel_noise=0.050
[imu_madgwick_filter.py-4] [INFO] [1781430859.340590137] [imu_madgwick_filter]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-4] [INFO] [1781430859.343009920] [imu_madgwick_filter]: [imu_madgwick] accel init: roll=0.1deg, pitch=-0.3deg
[lifecycle_manager-17] [INFO] [1781430859.373556436] [lifecycle_manager_keepout]: Server keepout_filter_info_server connected with bond.
[lifecycle_manager-17] [INFO] [1781430859.373732852] [lifecycle_manager_keepout]: Managed nodes are active
[lifecycle_manager-17] [INFO] [1781430859.373814060] [lifecycle_manager_keepout]: Creating bond timer...
[imu_madgwick_filter.py-6] [INFO] [1781430859.382184905] [imu_madgwick_bmi088]: [imu_madgwick] init: beta=0.0030, gyro_noise=0.0002, accel_noise=0.010
[bmi088_iio_bridge.py-5] [INFO] [1781430859.385881600] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1781430859.391524622] [bmi088_iio_bridge]:   DIAGNOSTIC: Scanning IIO devices under /sys/bus/iio/devices/
[bmi088_iio_bridge.py-5] [INFO] [1781430859.398070932] [bmi088_iio_bridge]:   Equivalent to: ls /sys/bus/iio/devices/*/name
[bmi088_iio_bridge.py-5] [INFO] [1781430859.401974626] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1781430859.404313659] [bmi088_iio_bridge]:   iio:device0/name = "34190000.adc"
[bmi088_iio_bridge.py-5] [INFO] [1781430859.406805442] [bmi088_iio_bridge]:   iio:device1/name = "bmi08x"
[bmi088_iio_bridge.py-5] [INFO] [1781430859.409561266] [bmi088_iio_bridge]:   trigger0/name = "34190000.adc-dev0"
[bmi088_iio_bridge.py-5] [INFO] [1781430859.412344714] [bmi088_iio_bridge]:   Total IIO devices found: 3
[bmi088_iio_bridge.py-5] [INFO] [1781430859.416313992] [bmi088_iio_bridge]:   BMI088 kernel module APPEARS LOADED: 1 BMI device(s) detected
[bmi088_iio_bridge.py-5] [INFO] [1781430859.419084482] [bmi088_iio_bridge]:   BMI device names: ['bmi08x']
[velocity_pid.py-9] [INFO] [1781430859.420768934] [velocity_pid]: VelocityPID 就绪: vx(Kp=0.8, Ki=0.60, Kd=0.05, max_i=0.68) wz(Kp=1.0, Ki=0.40, Kd=0.02, max_i=2.24) | feedback_timeout=0.5s
[bmi088_iio_bridge.py-5] [INFO] [1781430859.422405637] [bmi088_iio_bridge]:   gyro:  /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_anglvel is_si=False scale_override=0.00053
[bmi088_iio_bridge.py-5] [INFO] [1781430859.425710875] [bmi088_iio_bridge]:   accel: /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_accel is_si=False scale_override=0.00341
[velocity_pid.py-9] [INFO] [1781430859.431016022] [velocity_pid]: [vel_pid] ACTIVATED vx=0.00 wz=0.00
[bmi088_iio_bridge.py-5] [INFO] [1781430859.550988720] [bmi088_iio_bridge]: BMI088 IIO Bridge 启动 @ 100Hz -> /imu_data  [OK]
[bmi088_iio_bridge.py-5] [INFO] [1781430865.043615876] [bmi088_iio_bridge]:   gyro bias calibrated: (0.003259, 0.001391, -0.002960) rad/s
[imu_madgwick_filter.py-6] [INFO] [1781430859.577087001] [imu_madgwick_bmi088]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-6] [INFO] [1781430859.579629701] [imu_madgwick_bmi088]: [imu_madgwick] accel init: roll=-2.2deg, pitch=-3.5deg
[qr_decision-13] [INFO] [1781430859.717011711] [qr_decision]: qr_decision started: cooldown=3.0s, awaiting /sign from qr_decoder
[INFO] [component_container_isolated-18]: process started with pid [27046]
[imu_madgwick_filter.py-4] [WARN] [1781430860.294390447] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1501s > 0.15s, capping
[lslidar_driver_node-2] port = /dev/ttyACM1, baud_rate = 230400
[lslidar_driver_node-2] open_port /dev/ttyACM1 OK !
[vision_ai_node-14] [INFO] [1781430863.465313114] [vision_ai_node]: 成功加载配置文件: /userdata/dev_ws/install/racing_vision_ai/share/racing_vision_ai/config/vision_ai_config.yaml
[vision_ai_node-14] [INFO] [1781430863.831247370] [vision_ai_node]: Volcengine Ark client initialized successfully
[vision_ai_node-14] [INFO] [1781430863.848821475] [vision_ai_node]: Vision AI Node initialized
[vision_ai_node-14] [INFO] [1781430863.851641090] [vision_ai_node]: Waiting for sign4return=100 signal...
[vision_ai_node-14] [INFO] [1781430863.854890454] [vision_ai_node]: Results will be published to vlm_result
[INFO] [competition_master_stage3.py-19]: process started with pid [27048]
[INFO] [rviz2-20]: process started with pid [27052]
[component_container_isolated-18] [INFO] [1781430866.136476318] [nav2_container]: Load Library: /opt/ros/humble/lib/libcontroller_server_core.so
[component_container_isolated-18] [INFO] [1781430866.178146465] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-18] [INFO] [1781430866.178317256] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[imu_madgwick_filter.py-4] [WARN] [1781430866.199271808] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1500s > 0.15s, capping
[component_container_isolated-18] [INFO] [1781430866.262912879] [controller_server]:
[component_container_isolated-18]       controller_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781430866.292545526] [controller_server]: Creating controller server
[component_container_isolated-18] [INFO] [1781430866.383131045] [local_costmap.local_costmap]:
[component_container_isolated-18]       local_costmap lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781430866.385600911] [local_costmap.local_costmap]: Creating Costmap
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/controller_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781430866.419230920] [nav2_container]: Load Library: /opt/ros/humble/lib/libmap_server_core.so
[component_container_isolated-18] [INFO] [1781430866.477699883] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::CostmapFilterInfoServer>
[component_container_isolated-18] [INFO] [1781430866.477891258] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapSaver>
[component_container_isolated-18] [INFO] [1781430866.477973841] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-18] [INFO] [1781430866.478034799] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-18] [INFO] [1781430866.552821247] [map_server]:
[component_container_isolated-18]       map_server lifecycle node launched.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/map_server' in container '/nav2_container'
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781430866.553913827] [map_server]: Creating
[component_container_isolated-18] [INFO] [1781430866.561525467] [nav2_container]: Load Library: /opt/ros/humble/lib/libsmoother_server_core.so
[component_container_isolated-18] [INFO] [1781430866.571120184] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-18] [INFO] [1781430866.571350391] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-18] [INFO] [1781430866.665191524] [smoother_server]:
[component_container_isolated-18]       smoother_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781430866.675226947] [smoother_server]: Creating smoother server
[component_container_isolated-18] [INFO] [1781430866.684865581] [nav2_container]: Load Library: /opt/ros/humble/lib/libamcl_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/smoother_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781430866.702236520] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-18] [INFO] [1781430866.702397895] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-18] [INFO] [1781430866.780543332] [amcl]:
[component_container_isolated-18]       amcl lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781430866.782778407] [amcl]: Creating
[component_container_isolated-18] [INFO] [1781430866.875459419] [nav2_container]: Load Library: /opt/ros/humble/lib/libplanner_server_core.so
[component_container_isolated-18] [INFO] [1781430866.880834650] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-18] [INFO] [1781430866.881023816] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/amcl' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781430866.990315853] [planner_server]:
[component_container_isolated-18]       planner_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781430867.001092024] [planner_server]: Creating
[component_container_isolated-18] [INFO] [1781430867.096768568] [global_costmap.global_costmap]:
[component_container_isolated-18]       global_costmap lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781430867.099659100] [global_costmap.global_costmap]: Creating Costmap
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/planner_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781430867.137162178] [nav2_container]: Load Library: /opt/ros/humble/lib/libnav2_lifecycle_manager_core.so
[component_container_isolated-18] [INFO] [1781430867.142655701] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781430867.142823450] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781430867.213832913] [lifecycle_manager_localization]: Creating
[component_container_isolated-18] [INFO] [1781430867.250678494] [nav2_container]: Load Library: /opt/ros/humble/lib/libbehavior_server_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_localization' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781430867.262750827] [lifecycle_manager_localization]: Creating and initializing lifecycle service clients
[component_container_isolated-18] [INFO] [1781430867.296100754] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-18] [INFO] [1781430867.300584488] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-18] [INFO] [1781430867.311622908] [lifecycle_manager_localization]: Starting managed nodes bringup...
[component_container_isolated-18] [INFO] [1781430867.316875973] [lifecycle_manager_localization]: Configuring map_server
[component_container_isolated-18] [INFO] [1781430867.317831928] [map_server]: Configuring
[component_container_isolated-18] [INFO] [1781430867.318112511] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.yaml
[component_container_isolated-18] [INFO] [1781430867.319308382] [map_io]: resolution: 0.05
[component_container_isolated-18] [INFO] [1781430867.319455589] [map_io]: origin[0]: -2.65
[component_container_isolated-18] [INFO] [1781430867.319490381] [map_io]: origin[1]: -4.5
[component_container_isolated-18] [INFO] [1781430867.319517964] [map_io]: origin[2]: 0
[component_container_isolated-18] [INFO] [1781430867.319546589] [map_io]: free_thresh: 0.25
[component_container_isolated-18] [INFO] [1781430867.319575339] [map_io]: occupied_thresh: 0.65
[component_container_isolated-18] [INFO] [1781430867.319622547] [map_io]: mode: trinary
[component_container_isolated-18] [INFO] [1781430867.319653089] [map_io]: negate: 0
[component_container_isolated-18] [INFO] [1781430867.320347086] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm
[component_container_isolated-18] [INFO] [1781430867.379109675] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm: 163 X 141 map @ 0.05 m/cell
[component_container_isolated-18] [INFO] [1781430867.404814877] [behavior_server]:
[component_container_isolated-18]       behavior_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781430867.415410716] [lifecycle_manager_localization]: Configuring amcl
[component_container_isolated-18] [INFO] [1781430867.416028672] [amcl]: Configuring
[component_container_isolated-18] [INFO] [1781430867.416394504] [amcl]: initTransforms
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/behavior_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781430867.476178589] [nav2_container]: Load Library: /opt/ros/humble/lib/libbt_navigator_core.so
[component_container_isolated-18] [INFO] [1781430867.484131270] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-18] [INFO] [1781430867.486385054] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-18] [INFO] [1781430867.496129687] [amcl]: initPubSub
[component_container_isolated-18] [INFO] [1781430867.548941462] [amcl]: Subscribed to map topic.
[component_container_isolated-18] [INFO] [1781430867.587464787] [lifecycle_manager_localization]: Activating map_server
[component_container_isolated-18] [INFO] [1781430867.589575280] [map_server]: Activating
[component_container_isolated-18] [INFO] [1781430867.590116862] [map_server]: Creating bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781430867.590326694] [amcl]: Received a 163 X 141 map @ 0.050 m/pix
[component_container_isolated-18] [INFO] [1781430867.639218775] [bt_navigator]:
[component_container_isolated-18]       bt_navigator lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/bt_navigator' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781430867.640218397] [bt_navigator]: Creating
[component_container_isolated-18] [INFO] [1781430867.657375962] [nav2_container]: Load Library: /opt/ros/humble/lib/libwaypoint_follower_core.so
[component_container_isolated-18] [INFO] [1781430867.660434410] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-18] [INFO] [1781430867.660606826] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-18] [INFO] [1781430867.719904996] [lifecycle_manager_localization]: Server map_server connected with bond.
[component_container_isolated-18] [INFO] [1781430867.720128995] [lifecycle_manager_localization]: Activating amcl
[component_container_isolated-18] [INFO] [1781430867.721409616] [amcl]: Activating
[component_container_isolated-18] [INFO] [1781430867.721693740] [amcl]: initialPoseReceived
[component_container_isolated-18] [INFO] [1781430867.722287113] [amcl]: Setting pose (1781430867.722280): -1.985 -0.014 0.262
[component_container_isolated-18] [INFO] [1781430867.724223731] [amcl]: Creating bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781430867.770718028] [waypoint_follower]:
[component_container_isolated-18]       waypoint_follower lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781430867.775798928] [waypoint_follower]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/waypoint_follower' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781430867.803583915] [nav2_container]: Load Library: /opt/ros/humble/lib/libvelocity_smoother_core.so
[component_container_isolated-18] [INFO] [1781430867.807559109] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-18] [INFO] [1781430867.807724025] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-18] [INFO] [1781430867.833462603] [amcl]: createLaserObject
[component_container_isolated-18] [INFO] [1781430867.843135820] [lifecycle_manager_localization]: Server amcl connected with bond.
[component_container_isolated-18] [INFO] [1781430867.843341236] [lifecycle_manager_localization]: Managed nodes are active
[component_container_isolated-18] [INFO] [1781430867.843498027] [lifecycle_manager_localization]: Creating bond timer...
[component_container_isolated-18] [INFO] [1781430867.899482125] [velocity_smoother]:
[component_container_isolated-18]       velocity_smoother lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/velocity_smoother' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781430867.916268442] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781430867.916425816] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781430868.016253971] [lifecycle_manager_navigation]: Creating
[component_container_isolated-18] [INFO] [1781430868.051955848] [lifecycle_manager_navigation]: Creating and initializing lifecycle service clients
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_navigation' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781430868.144758945] [lifecycle_manager_navigation]: Starting managed nodes bringup...
[component_container_isolated-18] [INFO] [1781430868.144989611] [lifecycle_manager_navigation]: Configuring controller_server
[component_container_isolated-18] [INFO] [1781430868.146300231] [controller_server]: Configuring controller interface
[component_container_isolated-18] [INFO] [1781430868.149211096] [controller_server]: getting goal checker plugins..
[component_container_isolated-18] [INFO] [1781430868.152210586] [controller_server]: Controller frequency set to 10.0000Hz
[component_container_isolated-18] [INFO] [1781430868.152552251] [local_costmap.local_costmap]: Configuring
[component_container_isolated-18] [INFO] [1781430868.205376819] [local_costmap.local_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781430868.236334546] [local_costmap.local_costmap]: Subscribed to Topics: scan aurora_points
[component_container_isolated-18] [INFO] [1781430868.334843415] [local_costmap.local_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781430868.336389201] [local_costmap.local_costmap]: Using plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781430868.366284390] [local_costmap.local_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781430868.372912825] [local_costmap.local_costmap]: Using plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781430868.390459265] [local_costmap.local_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781430868.468399830] [controller_server]: Created progress_checker : progress_checker of type nav2_controller::SimpleProgressChecker
[component_container_isolated-18] [INFO] [1781430868.479456416] [controller_server]: Created goal checker : goal_checker of type nav2_controller::SimpleGoalChecker
[component_container_isolated-18] [INFO] [1781430868.491007418] [controller_server]: Controller Server has goal_checker  goal checkers available.
[component_container_isolated-18] [INFO] [1781430868.495539111] [controller_server]: Created controller : FollowPath of type nav2_regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781430868.599190420] [controller_server]: Controller Server has FollowPath  controllers available.
[component_container_isolated-18] [INFO] [1781430868.666166481] [lifecycle_manager_navigation]: Configuring smoother_server
[component_container_isolated-18] [INFO] [1781430868.667266186] [smoother_server]: Configuring smoother server
[component_container_isolated-18] [INFO] [1781430868.774404733] [smoother_server]: Created smoother : SmoothPath of type nav2_constrained_smoother/ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781430868.851564843] [smoother_server]: Smoother Server has SmoothPath  smoothers available.
[component_container_isolated-18] [INFO] [1781430868.895553274] [lifecycle_manager_navigation]: Configuring planner_server
[component_container_isolated-18] [INFO] [1781430868.897051561] [planner_server]: Configuring
[component_container_isolated-18] [INFO] [1781430868.897430393] [global_costmap.global_costmap]: Configuring
[component_container_isolated-18] [INFO] [1781430868.936018385] [global_costmap.global_costmap]: Using plugin "static_layer"
[component_container_isolated-18] [INFO] [1781430868.956218649] [global_costmap.global_costmap]: Subscribing to the map topic (/map) with transient local durability
[component_container_isolated-18] [INFO] [1781430868.964197038] [global_costmap.global_costmap]: Initialized plugin "static_layer"
[component_container_isolated-18] [INFO] [1781430868.964465245] [global_costmap.global_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781430868.979039862] [global_costmap.global_costmap]: Subscribed to Topics: scan aurora_points
[imu_madgwick_filter.py-4] [INFO] [1781430869.011035210] [imu_madgwick_filter]: [imu_madgwick ->] msgs=185 q_w=0.9995 angle=3.6deg beta=0.0330
[competition_master_stage3.py-19] [INFO] [1781430869.043761222] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1781430869.047077503] [competition_master_stage3]: === [Stage 3] 总控节点初始化 ===
[competition_master_stage3.py-19] [INFO] [1781430869.050401366] [competition_master_stage3]:   QR点:    (0.41, -3.17, yaw=0.00)
[competition_master_stage3.py-19] [INFO] [1781430869.053534022] [competition_master_stage3]:   通道入口: (0.38, -1.10, yaw=0.00)
[competition_master_stage3.py-19] [INFO] [1781430869.061892702] [competition_master_stage3]:   P点:     (-1.99, -0.01, yaw=0.26)
[competition_master_stage3.py-19] [INFO] [1781430869.065232524] [competition_master_stage3]:   cruise_cw: 3 路点 → VLM=(3.12, -1.34)
[competition_master_stage3.py-19] [INFO] [1781430869.068662970] [competition_master_stage3]:   cruise_ccw: 3 路点 → VLM=(2.10, 0.92)
[competition_master_stage3.py-19] [INFO] [1781430869.072723123] [competition_master_stage3]:   超时: total=180.0s QR=90.0s entry=60.0s cruise=180.0s vlm=30.0s return=120.0s
[competition_master_stage3.py-19] [INFO] [1781430869.076251611] [competition_master_stage3]:   回退QR方向: 逆时针
[competition_master_stage3.py-19] [INFO] [1781430869.080024181] [competition_master_stage3]:   VLM结果话题: vlm_result
[competition_master_stage3.py-19] [INFO] [1781430869.083775418] [competition_master_stage3]: ============================================================
[component_container_isolated-18] [INFO] [1781430869.084996122] [global_costmap.global_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781430869.085264455] [global_costmap.global_costmap]: Using plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781430869.105612302] [global_costmap.global_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781430869.105813051] [global_costmap.global_costmap]: Using plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781430869.125984065] [global_costmap.global_costmap]: Initialized plugin "inflation_layer"
[imu_madgwick_filter.py-6] [INFO] [1781430869.172400906] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=412 q_w=0.9993 angle=4.2deg beta=0.0030
[component_container_isolated-18] [INFO] [1781430869.175165771] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 163 X 141 at 0.050000 m/pix
[component_container_isolated-18] [INFO] [1781430869.198667649] [planner_server]: Created global planner plugin GridBased of type nav2_smac_planner/SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781430869.199716145] [planner_server]: Configuring GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781430869.238192347] [planner_server]: Even sized heuristic lookup table size set 200.000000, increasing size by 1 to make odd
[rviz2-20] [INFO] [1781430869.455940391] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-20] [INFO] [1781430869.456771471] [rviz2]: OpenGl version: 4.5 (GLSL 4.5)
[rviz2-20] [INFO] [1781430869.680865285] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-20] [INFO] [1781430871.707019362] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[rviz2-20] [ERROR] [1781430872.080516425] [rviz2]: Vertex Program:rviz/glsl120/indexed_8bit_image.vert Fragment Program:rviz/glsl120/indexed_8bit_image.frag GLSL link result :
[rviz2-20] active samplers with a different type refer to the same texture image unit
[qr_decoder-12] [INFO] [1781430874.836210860] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=200 last_qr_frame=-1 gap=-1 frames rejects=0
[imu_madgwick_filter.py-4] [INFO] [1781430879.009153360] [imu_madgwick_filter]: [imu_madgwick ->] msgs=380 q_w=0.9980 angle=7.3deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781430879.160784026] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=943 q_w=0.9993 angle=4.2deg beta=0.0030
[component_container_isolated-18] [INFO] [1781430883.122284991] [planner_server]: Configured plugin GridBased of type SmacPlannerHybrid with maximum iterations 2000, max on approach iterations 300, and not allowing unknown traversal. Tolerance 0.50.Using motion model: Reeds-Shepp.
[component_container_isolated-18] [INFO] [1781430883.122571240] [planner_server]: Planner Server has GridBased  planners available.
[component_container_isolated-18] [INFO] [1781430883.192628679] [lifecycle_manager_navigation]: Configuring behavior_server
[component_container_isolated-18] [INFO] [1781430883.193861925] [behavior_server]: Configuring
[component_container_isolated-18] [INFO] [1781430883.244127720] [behavior_server]: Creating behavior plugin spin of type nav2_behaviors/Spin
[component_container_isolated-18] [INFO] [1781430883.248436915] [behavior_server]: Configuring spin
[component_container_isolated-18] [INFO] [1781430883.306646809] [behavior_server]: Creating behavior plugin backup of type nav2_behaviors/BackUp
[component_container_isolated-18] [INFO] [1781430883.310483630] [behavior_server]: Configuring backup
[component_container_isolated-18] [INFO] [1781430883.354462362] [behavior_server]: Creating behavior plugin drive_on_heading of type nav2_behaviors/DriveOnHeading
[component_container_isolated-18] [INFO] [1781430883.358129267] [behavior_server]: Configuring drive_on_heading
[component_container_isolated-18] [INFO] [1781430883.407218899] [behavior_server]: Creating behavior plugin wait of type nav2_behaviors/Wait
[component_container_isolated-18] [INFO] [1781430883.411653093] [behavior_server]: Configuring wait
[component_container_isolated-18] [INFO] [1781430883.437104760] [lifecycle_manager_navigation]: Configuring bt_navigator
[component_container_isolated-18] [INFO] [1781430883.438001632] [bt_navigator]: Configuring
[competition_master_stage3.py-19] [INFO] [1781430883.698579327] [competition_master_stage3]: [LAUNCH] 发车阶段: 14.9s
[competition_master_stage3.py-19] [INFO] [1781430883.702655689] [competition_master_stage3]: >>> 系统就绪, 开始 Stage 3 导航
[competition_master_stage3.py-19] [INFO] [1781430883.706532926] [competition_master_stage3]: [状态机] INIT → NAV_TO_QR
[competition_master_stage3.py-19] [INFO] [1781430883.711168620] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-18] [INFO] [1781430884.005131415] [lifecycle_manager_navigation]: Configuring waypoint_follower
[component_container_isolated-18] [INFO] [1781430884.006489077] [waypoint_follower]: Configuring
[competition_master_stage3.py-19] [WARN] [1781430884.014719383] [competition_master_stage3]: 导航目标被拒绝, 3s 后重试...
[component_container_isolated-18] [INFO] [1781430884.098447487] [waypoint_follower]: Created waypoint_task_executor : wait_at_waypoint of type nav2_waypoint_follower::WaitAtWaypoint
[component_container_isolated-18] [INFO] [1781430884.104273385] [lifecycle_manager_navigation]: Configuring velocity_smoother
[component_container_isolated-18] [INFO] [1781430884.105624756] [velocity_smoother]: Configuring velocity smoother
[component_container_isolated-18] [INFO] [1781430884.139040731] [lifecycle_manager_navigation]: Activating controller_server
[component_container_isolated-18] [INFO] [1781430884.140616643] [controller_server]: Activating
[component_container_isolated-18] [INFO] [1781430884.140938808] [local_costmap.local_costmap]: Activating
[component_container_isolated-18] [INFO] [1781430884.141161016] [local_costmap.local_costmap]: Checking transform
[component_container_isolated-18] [INFO] [1781430884.141625806] [local_costmap.local_costmap]: start
[component_container_isolated-18] [INFO] [1781430884.162935862] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781430884.172179541] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781430884.172378915] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781430884.177587315] [local_costmap.local_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[component_container_isolated-18] [INFO] [1781430884.372116352] [controller_server]: Activating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781430884.372409684] [controller_server]: Creating bond (controller_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781430884.485951025] [lifecycle_manager_navigation]: Server controller_server connected with bond.
[component_container_isolated-18] [INFO] [1781430884.486134649] [lifecycle_manager_navigation]: Activating smoother_server
[component_container_isolated-18] [INFO] [1781430884.487212396] [smoother_server]: Activating
[component_container_isolated-18] [INFO] [1781430884.487458062] [smoother_server]: Activating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781430884.488032852] [smoother_server]: Creating bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781430884.607368799] [lifecycle_manager_navigation]: Server smoother_server connected with bond.
[component_container_isolated-18] [INFO] [1781430884.607546757] [lifecycle_manager_navigation]: Activating planner_server
[component_container_isolated-18] [INFO] [1781430884.608833627] [planner_server]: Activating
[component_container_isolated-18] [INFO] [1781430884.609174168] [global_costmap.global_costmap]: Activating
[component_container_isolated-18] [INFO] [1781430884.609276668] [global_costmap.global_costmap]: Checking transform
[component_container_isolated-18] [INFO] [1781430884.609590542] [global_costmap.global_costmap]: start
[component_container_isolated-18] [INFO] [1781430884.624688451] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781430884.638290407] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781430884.638475198] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781430884.650077661] [global_costmap.global_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[rviz2-20] [INFO] [1781430884.784385143] [rviz2]: Trying to create a map of size 60 x 60 using 1 swatches
[imu_madgwick_filter.py-4] [WARN] [1781430884.793860820] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1500s > 0.15s, capping
[competition_master_stage3.py-19] [INFO] [1781430884.863211054] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.99,-0.01) yaw=19deg cmd=(vx=0.00 wz=0.00) elapsed=1.1s cpuFreq=1500MHz cpuT=68C cpu=73% mem=18%
[component_container_isolated-18] [INFO] [1781430885.689501514] [planner_server]: Activating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781430885.699001900] [planner_server]: Creating bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781430885.826315031] [lifecycle_manager_navigation]: Server planner_server connected with bond.
[component_container_isolated-18] [INFO] [1781430885.826512114] [lifecycle_manager_navigation]: Activating behavior_server
[component_container_isolated-18] [INFO] [1781430885.827512277] [behavior_server]: Activating
[component_container_isolated-18] [INFO] [1781430885.827640319] [behavior_server]: Activating spin
[component_container_isolated-18] [INFO] [1781430885.827789568] [behavior_server]: Activating backup
[component_container_isolated-18] [INFO] [1781430885.827864443] [behavior_server]: Activating drive_on_heading
[component_container_isolated-18] [INFO] [1781430885.827932859] [behavior_server]: Activating wait
[component_container_isolated-18] [INFO] [1781430885.828011859] [behavior_server]: Creating bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781430885.944830816] [lifecycle_manager_navigation]: Server behavior_server connected with bond.
[component_container_isolated-18] [INFO] [1781430885.945014315] [lifecycle_manager_navigation]: Activating bt_navigator
[component_container_isolated-18] [INFO] [1781430885.947352016] [bt_navigator]: Activating
[component_container_isolated-18] [WARN] [1781430886.080813337] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[rviz2-20] [INFO] [1781430886.088807020] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[component_container_isolated-18] [WARN] [1781430886.186157624] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781430886.253045451] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781430886.411073818] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781430886.671650523] [bt_navigator_navigate_to_pose_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [INFO] [1781430886.873681833] [bt_navigator]: Creating bond (bt_navigator) to lifecycle manager.
[competition_master_stage3.py-19] [INFO] [1781430886.894044434] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.99,-0.01) yaw=19deg cmd=(vx=0.00 wz=0.00) elapsed=3.1s cpuFreq=1500MHz cpuT=69C cpu=88% mem=19%
[component_container_isolated-18] [INFO] [1781430887.004431038] [lifecycle_manager_navigation]: Server bt_navigator connected with bond.
[component_container_isolated-18] [INFO] [1781430887.004656704] [lifecycle_manager_navigation]: Activating waypoint_follower
[component_container_isolated-18] [INFO] [1781430887.005894742] [waypoint_follower]: Activating
[component_container_isolated-18] [INFO] [1781430887.006163908] [waypoint_follower]: Creating bond (waypoint_follower) to lifecycle manager.
[competition_master_stage3.py-19] [INFO] [1781430887.026847550] [competition_master_stage3]: 重试发送导航目标 (QR点)...
[competition_master_stage3.py-19] [INFO] [1781430887.057261119] [competition_master_stage3]: [DIAG] nav目标距离: 3.96m, robot=(-1.99,-0.01) → target=(0.41,-3.17)
[competition_master_stage3.py-19] [INFO] [1781430887.067623753] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-18] [INFO] [1781430887.077474430] [bt_navigator]: Begin navigating from current location (-1.99, -0.01) to (0.41, -3.17)
[competition_master_stage3.py-19] [INFO] [1781430887.090239931] [competition_master_stage3]: 导航目标已接受，车辆出发...
[component_container_isolated-18] [INFO] [1781430887.143149470] [lifecycle_manager_navigation]: Server waypoint_follower connected with bond.
[component_container_isolated-18] [INFO] [1781430887.143309219] [lifecycle_manager_navigation]: Activating velocity_smoother
[component_container_isolated-18] [INFO] [1781430887.144636757] [velocity_smoother]: Activating
[component_container_isolated-18] [INFO] [1781430887.145150422] [velocity_smoother]: Creating bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781430887.274908007] [lifecycle_manager_navigation]: Server velocity_smoother connected with bond.
[component_container_isolated-18] [INFO] [1781430887.275077256] [lifecycle_manager_navigation]: Managed nodes are active
[component_container_isolated-18] [INFO] [1781430887.275136048] [lifecycle_manager_navigation]: Creating bond timer...
[component_container_isolated-18] [WARN] [1781430887.634394232] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.8156 Hz
[component_container_isolated-18] [INFO] [1781430887.779960600] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-18] [WARN] [1781430887.781262304] [controller_server]: No goal checker was specified in parameter 'current_goal_checker'. Server will use only plugin loaded goal_checker . This warning will appear once.
[cmd_vel_mux.py-8] [INFO] [1781430887.822883838] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=-0.12
[velocity_pid.py-9] [INFO] [1781430887.864693371] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.17 err=100.0%
[component_container_isolated-18] Reallocing temp weights 301 - 60
[competition_master_stage3.py-19] [INFO] [1781430888.863867354] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.99,-0.01) yaw=19deg cmd=(vx=0.45 wz=-1.37) elapsed=5.1s plan[29pts 4.1m] (-2.00,-0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=69C cpu=90% mem=19%
[imu_madgwick_filter.py-4] [INFO] [1781430889.010998343] [imu_madgwick_filter]: [imu_madgwick ->] msgs=578 q_w=0.9851 angle=19.8deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781430889.170524087] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1402 q_w=0.9320 angle=42.5deg beta=0.0030
[component_container_isolated-18] Reallocing temp weights 1158 - 60
[qr_decoder-12] [INFO] [1781430889.933222710] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=400 last_qr_frame=-1 gap=-1 frames rejects=0
[component_container_isolated-18] [WARN] [1781430890.629779008] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3350 Hz
[velocity_pid.py-9] [INFO] [1781430890.758155186] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.44 corrected=-0.02 err=21.7%
[cmd_vel_mux.py-8] [INFO] [1781430890.759755889] [cmd_vel_mux]: [mux→] src=nav vx=0.27 wz=0.28
[component_container_isolated-18] [INFO] [1781430890.781594153] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1781430890.862277149] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.41,-0.36) yaw=-61deg cmd=(vx=0.27 wz=0.28) elapsed=7.1s plan[23pts 3.2m] (-1.30,-0.45)→(0.40,-3.15) cpuFreq=1500MHz cpuT=69C cpu=75% mem=19%
[cmd_vel_mux.py-8] [INFO] [1781430892.458240881] [cmd_vel_mux]: [mux→] src=nav vx=0.27 wz=-0.17
[velocity_pid.py-9] [INFO] [1781430892.471446798] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.01 -> current=-0.12 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781430892.484918797] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.44 corrected=-0.04 err=23.6%
[velocity_pid.py-9] [INFO] [1781430892.692543188] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.00 -> current=-0.09 dt=0.0333s, resetting
[competition_master_stage3.py-19] [INFO] [1781430892.880322933] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.87,-1.31) yaw=-56deg cmd=(vx=-0.24 wz=-0.12) elapsed=9.1s plan[23pts 3.2m] (-1.30,-0.45)→(0.40,-3.15) cpuFreq=1500MHz cpuT=69C cpu=83% mem=19%
[velocity_pid.py-9] [INFO] [1781430893.491699982] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.11 corrected=-0.31 err=63.0%
[component_container_isolated-18] [WARN] [1781430893.640077727] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3170 Hz
[component_container_isolated-18] [INFO] [1781430893.781600410] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781430893.855591512] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.09 dt=0.0336s, resetting
[cmd_vel_mux.py-8] [INFO] [1781430893.858686878] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.11
[velocity_pid.py-9] [INFO] [1781430893.988690222] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781430894.499059927] [velocity_pid]: [vel_pid→] desired=0.45 actual=0.02 corrected=0.49 err=95.8%
[competition_master_stage3.py-19] [INFO] [1781430894.866182911] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.87,-1.31) yaw=-56deg cmd=(vx=0.45 wz=0.04) elapsed=11.1s plan[16pts 2.2m] (-0.80,-1.35)→(0.40,-3.15) cpuFreq=1500MHz cpuT=69C cpu=83% mem=19%
[component_container_isolated-18] Reallocing temp weights 1500 - 60
[component_container_isolated-18] [WARN] [1781430896.631865034] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3295 Hz
[component_container_isolated-18] [INFO] [1781430896.781590489] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1781430896.867860806] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.56,-1.75) yaw=-58deg cmd=(vx=0.45 wz=-0.02) elapsed=13.1s plan[11pts 1.5m] (-0.50,-1.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=69C cpu=89% mem=19%
[qr_decoder-12] [INFO] [1781430896.925255088] [qr_decoder_zbar]: [qr_decoder] QR DETECTED frame=495 symbols=1 (gap=-1 frames)
[qr_decoder-12] [INFO] [1781430896.925509712] [qr_decoder_zbar]: [QR] 1584 | depth=0mm (advisory, publishing anyway)
[qr_decoder-12] [INFO] [1781430896.925809253] [qr_decoder_zbar]: [QR] 1584 | robot_pos: (0.62, -2.65, yaw=-1.55)
[competition_master_stage3.py-19] [INFO] [1781430896.931960734] [competition_master_stage3]: [QR检测] 内容: 1584
[qr_decision-13] [INFO] [1781430896.940431291] [qr_decision]: [QR] 1584 CCW @ (x=0.62, y=-2.65, yaw=-1.55) → /qr_event
[qr_decision-13] [INFO] [1781430896.946303523] [qr_decision]: [检查点] qr_decision 发布 /qr_event (由 task_manager 决定停车)
[qr_decoder-12] [INFO] [1781430897.002633808] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[competition_master_stage3.py-19] [INFO] [1781430897.014063314] [competition_master_stage3]: [KILL] 已终止进程: qr_decoder_zbar
[competition_master_stage3.py-19] [INFO] [1781430897.022492663] [competition_master_stage3]: >>> QR 解码已关闭, 等待方向判断 (/qr_event)...
[competition_master_stage3.py-19] [INFO] [1781430897.044831886] [competition_master_stage3]: [QR检测] 取消当前导航目标, 等待BT完成 cancel/halt 清理...
[competition_master_stage3.py-19] [INFO] [1781430897.065277157] [competition_master_stage3]: [QR事件] 方向: 逆时针 (通道巡航阶段使用)
[component_container_isolated-18] [INFO] [1781430897.081601065] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-18] [INFO] [1781430897.081873147] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1781430897.082665020] [bt_navigator]: [navigate_to_pose] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1781430897.084806013] [bt_navigator]: Goal canceled
[competition_master_stage3.py-19] [INFO] [1781430897.144195873] [competition_master_stage3]: [KILL] 已终止进程: qr_decision
[velocity_pid.py-9] [INFO] [1781430897.157788539] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.45 corrected=0.03 err=25.3%
[competition_master_stage3.py-19] [INFO] [1781430897.166177847] [competition_master_stage3]: [结果回调] BT取消确认完成 (STATUS_CANCELED), 准备发送通道入口目标...
[competition_master_stage3.py-19] [INFO] [1781430897.173695532] [competition_master_stage3]: [状态机] NAV_TO_QR → BACKING_UP
[competition_master_stage3.py-19] [INFO] [1781430897.176539148] [competition_master_stage3]: >>> BT取消完成, 右后退摆正车头→前进进通道...
[competition_master_stage3.py-19] [INFO] [1781430897.181267176] [competition_master_stage3]: [BACKUP] 右后退中: vx=-0.15 wz=2.80, 持续 6.0s...
[cmd_vel_mux.py-8] [INFO] [1781430897.191170854] [cmd_vel_mux]: [mux→] src=nav vx=-0.15 wz=2.80
[velocity_pid.py-9] [INFO] [1781430897.221350303] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.27 -> current=-0.15 dt=0.0320s, resetting
[INFO] [qr_decoder-12]: process has finished cleanly [pid 26751]
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
[cmd_vel_mux.py-8] [INFO] [1781430897.728708536] [cmd_vel_mux]: [mux→] src=nav vx=0.00 wz=0.00
[velocity_pid.py-9] [INFO] [1781430898.160133213] [velocity_pid]: [vel_pid→] desired=-0.15 actual=0.00 corrected=-0.17 err=100.0%
[ERROR] [qr_decision-13]: process has died [pid 26753, exit code 1, cmd '/userdata/dev_ws/install/origincar_qr/lib/origincar_qr/qr_decision --ros-args -r __node:=qr_decision --params-file /tmp/launch_params_0j6hdp98'].
[competition_master_stage3.py-19] [INFO] [1781430898.862986022] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.24,-2.22) yaw=-60deg cmd=(vx=-0.15 wz=2.80) elapsed=15.1s plan[11pts 1.5m] (-0.50,-1.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=69C cpu=82% mem=18%
[imu_madgwick_filter.py-4] [INFO] [1781430899.009103492] [imu_madgwick_filter]: [imu_madgwick ->] msgs=774 q_w=0.8563 angle=62.2deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781430899.165363016] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1844 q_w=0.7887 angle=75.9deg beta=0.0030
[competition_master_stage3.py-19] [INFO] [1781430900.860438323] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.28,-2.18) yaw=-29deg cmd=(vx=-0.15 wz=2.80) elapsed=17.1s plan[11pts 1.5m] (-0.50,-1.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=69C cpu=70% mem=18%
[competition_master_stage3.py-19] [INFO] [1781430902.860440124] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.55,-2.16) yaw=20deg cmd=(vx=-0.15 wz=2.80) elapsed=19.1s plan[11pts 1.5m] (-0.50,-1.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=68C cpu=70% mem=18%
[competition_master_stage3.py-19] [INFO] [1781430903.183928278] [competition_master_stage3]: [状态机] BACKING_UP → CRUISE_CHANNEL
[cmd_vel_mux.py-8] [INFO] [1781430903.196683365] [cmd_vel_mux]: [mux→] src=stop vx=0.00 wz=0.00
[competition_master_stage3.py-19] [INFO] [1781430903.209033328] [competition_master_stage3]: [CRUISE] 方向: CCW (逆时针, even QR), 路点: (1.73,-1.98), (3.10,-1.35), (2.10,0.92)
[competition_master_stage3.py-19] [INFO] [1781430903.217756885] [competition_master_stage3]: [CRUISE] NavigateThroughPoses: (0.38,-1.10), (1.73,-1.98), (3.10,-1.35), (2.10,0.92)
[component_container_isolated-18] [INFO] [1781430903.220846168] [bt_navigator]: Begin navigating from current location through 4 poses to (2.10, 0.92)
[competition_master_stage3.py-19] [INFO] [1781430903.233516588] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[component_container_isolated-18] [WARN] [1781430903.645823895] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 2.3655 Hz
[cmd_vel_mux.py-8] [INFO] [1781430903.688332309] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.50s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1781430903.700575856] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[component_container_isolated-18] [INFO] [1781430903.823026364] [controller_server]: Received a goal, begin computing control effort.
[cmd_vel_mux.py-8] [INFO] [1781430903.855771182] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=-0.08
[velocity_pid.py-9] [INFO] [1781430903.888881375] [velocity_pid]: [vel_pid→] desired=0.07 actual=-0.05 corrected=0.15 err=169.3%
[competition_master_stage3.py-19] [INFO] [1781430904.861819762] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.66,-2.22) yaw=49deg cmd=(vx=0.45 wz=-0.05) elapsed=21.1s plan[65pts 8.6m] (-0.70,-2.25)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=78% mem=18%
[velocity_pid.py-9] [INFO] [1781430904.927096359] [velocity_pid]: [vel_pid→] desired=0.45 actual=0.36 corrected=0.18 err=20.2%
[velocity_pid.py-9] [INFO] [1781430906.593546665] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.45 corrected=-0.10 err=25.3%
[cmd_vel_mux.py-8] [INFO] [1781430906.623769034] [cmd_vel_mux]: [mux→] src=nav vx=0.27 wz=0.00
[component_container_isolated-18] [WARN] [1781430906.659707594] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3655 Hz
[component_container_isolated-18] [INFO] [1781430906.823412235] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781430906.860085876] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.00 -> current=-0.09 dt=0.0332s, resetting
[competition_master_stage3.py-19] [INFO] [1781430906.864540072] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.23,-1.69) yaw=48deg cmd=(vx=0.00 wz=0.02) elapsed=23.1s plan[59pts 7.8m] (-0.10,-1.65)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=100% mem=18%
[velocity_pid.py-9] [INFO] [1781430906.887628170] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.02 -> current=-0.11 dt=0.0334s, resetting
[cmd_vel_mux.py-8] [INFO] [1781430907.124265971] [cmd_vel_mux]: [mux→] src=nav vx=0.38 wz=-0.19
[velocity_pid.py-9] [INFO] [1781430907.622988419] [velocity_pid]: [vel_pid→] desired=0.45 actual=0.33 corrected=0.09 err=26.0%
[competition_master_stage3.py-19] [INFO] [1781430908.871700834] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.28,-1.19) yaw=17deg cmd=(vx=0.45 wz=-0.36) elapsed=25.1s plan[59pts 7.8m] (-0.10,-1.65)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=57% mem=18%
[velocity_pid.py-9] [INFO] [1781430908.995706345] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.46 corrected=-0.15 err=27.2%
[imu_madgwick_filter.py-4] [INFO] [1781430909.011738548] [imu_madgwick_filter]: [imu_madgwick ->] msgs=970 q_w=0.9999 angle=1.8deg beta=0.0330
[cmd_vel_mux.py-8] [INFO] [1781430909.022559183] [cmd_vel_mux]: [mux→] src=nav vx=0.27 wz=-0.11
[velocity_pid.py-9] [INFO] [1781430909.096027427] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.11 -> current=0.02 dt=0.0344s, resetting
[imu_madgwick_filter.py-6] [INFO] [1781430909.164593810] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2355 q_w=0.9791 angle=23.5deg beta=0.0030
[velocity_pid.py-9] [INFO] [1781430909.256714749] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.00 -> current=-0.09 dt=0.0346s, resetting
[component_container_isolated-18] [WARN] [1781430909.639049424] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3979 Hz
[component_container_isolated-18] [INFO] [1781430909.823419677] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781430909.927242373] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.24
[velocity_pid.py-9] [INFO] [1781430910.054532960] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781430910.059539529] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.11 -> current=-0.00 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781430910.063100186] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.11 corrected=0.40 err=285.0%
[competition_master_stage3.py-19] [INFO] [1781430910.874569950] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.78,-1.12) yaw=-4deg cmd=(vx=0.45 wz=-0.14) elapsed=27.1s plan[51pts 6.9m] (0.80,-1.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=94% mem=18%
[velocity_pid.py-9] [INFO] [1781430911.089711867] [velocity_pid]: [vel_pid→] desired=0.45 actual=0.35 corrected=0.27 err=21.6%
[component_container_isolated-18] [WARN] [1781430912.637247100] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4008 Hz
[velocity_pid.py-9] [INFO] [1781430912.688828826] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.46 corrected=-0.02 err=27.2%
[cmd_vel_mux.py-8] [INFO] [1781430912.759410497] [cmd_vel_mux]: [mux→] src=nav vx=0.18 wz=-0.10
[component_container_isolated-18] [INFO] [1781430912.823417021] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781430912.854431640] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.10 -> current=0.02 dt=0.0152s, resetting
[competition_master_stage3.py-19] [INFO] [1781430912.873055586] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.49,-1.34) yaw=-49deg cmd=(vx=0.18 wz=-0.10) elapsed=29.1s plan[45pts 6.0m] (1.50,-1.35)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=71% mem=18%
[cmd_vel_mux.py-8] [INFO] [1781430913.823562729] [cmd_vel_mux]: [mux→] src=nav vx=0.27 wz=-0.34
[velocity_pid.py-9] [INFO] [1781430913.856132302] [velocity_pid]: [vel_pid→] desired=0.27 actual=0.41 corrected=-0.05 err=52.6%
[velocity_pid.py-9] [INFO] [1781430913.987585591] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.09 -> current=0.03 dt=0.0330s, resetting
[velocity_pid.py-9] [INFO] [1781430914.054116359] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.00 -> current=-0.09 dt=0.0331s, resetting
[velocity_pid.py-9] [INFO] [1781430914.869968942] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.13 corrected=-0.27 err=56.7%
[competition_master_stage3.py-19] [INFO] [1781430914.874416721] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.75,-1.87) yaw=-87deg cmd=(vx=-0.30 wz=0.62) elapsed=31.1s plan[45pts 6.0m] (1.50,-1.35)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=100% mem=18%
[component_container_isolated-18] [WARN] [1781430915.637591046] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4056 Hz
[component_container_isolated-18] [INFO] [1781430915.823369225] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781430915.889102329] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.30 corrected=0.02 err=43.3%
[cmd_vel_mux.py-8] [INFO] [1781430915.926260723] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.34
[velocity_pid.py-9] [INFO] [1781430916.053824611] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1781430916.390167573] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.09 -> current=-0.04 dt=0.0340s, resetting
[competition_master_stage3.py-19] [INFO] [1781430916.862505776] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.69,-1.65) yaw=-61deg cmd=(vx=0.45 wz=-0.07) elapsed=33.1s plan[40pts 5.3m] (1.70,-1.75)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=78% mem=18%
[velocity_pid.py-9] [INFO] [1781430916.921695608] [velocity_pid]: [vel_pid→] desired=0.45 actual=0.25 corrected=0.34 err=44.9%
[component_container_isolated-18] [WARN] [1781430918.634496944] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4088 Hz
[component_container_isolated-18] [INFO] [1781430918.823366246] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1781430918.860067101] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.22,-2.07) yaw=-27deg cmd=(vx=0.45 wz=0.66) elapsed=35.1s plan[35pts 4.9m] (2.10,-2.05)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=80% mem=18%
[imu_madgwick_filter.py-4] [INFO] [1781430919.009513014] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1163 q_w=0.9921 angle=14.4deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781430919.160974674] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2846 q_w=0.9606 angle=32.3deg beta=0.0030
[velocity_pid.py-9] [INFO] [1781430920.393884018] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.45 corrected=0.05 err=25.3%
[cmd_vel_mux.py-8] [INFO] [1781430920.459450044] [cmd_vel_mux]: [mux→] src=nav vx=0.18 wz=0.39
[velocity_pid.py-9] [INFO] [1781430920.654222334] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.00 -> current=-0.09 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1781430920.689246320] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.02 -> current=-0.11 dt=0.0338s, resetting
[competition_master_stage3.py-19] [INFO] [1781430920.864141665] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.08,-1.96) yaw=41deg cmd=(vx=-0.30 wz=-0.36) elapsed=37.1s plan[35pts 4.9m] (2.10,-2.05)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=88% mem=18%
[velocity_pid.py-9] [INFO] [1781430921.422685947] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.10 corrected=-0.31 err=67.3%
[component_container_isolated-18] [WARN] [1781430921.630946369] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4176 Hz
[component_container_isolated-18] [INFO] [1781430921.823442459] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781430921.922567267] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.29
[velocity_pid.py-9] [INFO] [1781430922.056430980] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781430922.087851935] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.08 dt=0.0332s, resetting
[velocity_pid.py-9] [INFO] [1781430922.455455460] [velocity_pid]: [vel_pid→] desired=0.45 actual=0.00 corrected=0.42 err=100.0%
[competition_master_stage3.py-19] [INFO] [1781430922.860645174] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.13,-1.91) yaw=42deg cmd=(vx=0.45 wz=1.09) elapsed=39.1s plan[29pts 4.0m] (3.10,-1.95)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=80% mem=18%
[velocity_pid.py-9] [INFO] [1781430923.988868609] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.44 corrected=0.07 err=21.7%
[cmd_vel_mux.py-8] [INFO] [1781430924.056851089] [cmd_vel_mux]: [mux→] src=nav vx=0.18 wz=0.47
[velocity_pid.py-9] [INFO] [1781430924.254362131] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.00 -> current=-0.09 dt=0.0328s, resetting
[velocity_pid.py-9] [INFO] [1781430924.289915242] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.09 -> current=-0.03 dt=0.0339s, resetting
[component_container_isolated-18] [WARN] [1781430924.625758405] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1781430924.626006196] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.10, 0.92)
[component_container_isolated-18] [WARN] [1781430924.626111071] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1781430924.821789077] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781430924.834572750] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781430924.848841794] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781430924.848998794] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781430924.849297251] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1781430924.851479704] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1781430924.863949711] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-19] [INFO] [1781430924.868584865] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.25,-1.31) yaw=97deg cmd=(vx=-0.30 wz=-0.75) elapsed=41.1s plan[29pts 4.0m] (3.10,-1.95)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=94% mem=18%
[velocity_pid.py-9] [INFO] [1781430924.989441409] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.10 corrected=-0.31 err=67.3%
[component_container_isolated-18] [WARN] [1781430925.627222669] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1781430925.627454085] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.10, 0.92)
[component_container_isolated-18] [WARN] [1781430925.627546960] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1781430925.823422800] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-18] [INFO] [1781430925.823592092] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1781430925.824925046] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1781430925.842930997] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781430925.859184370] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781430925.865109562] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781430925.865384519] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781430925.874909577] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1781430925.879539856] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781430925.886727419] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1781430925.887721458] [behavior_server]: wait completed successfully
[component_container_isolated-18] [INFO] [1781430925.895983561] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781430925.896158435] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781430925.910886062] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[cmd_vel_mux.py-8] [INFO] [1781430925.922658155] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.11
[component_container_isolated-18] [INFO] [1781430926.128158804] [behavior_server]: Running backup
[component_container_isolated-18] [INFO] [1781430926.128953010] [behavior_server]: DriveOnHeading: no acceleration or deceleration limits set
[cmd_vel_mux.py-8] [INFO] [1781430926.855684578] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.00
[competition_master_stage3.py-19] [INFO] [1781430926.864489554] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.22,-1.51) yaw=80deg cmd=(vx=0.00 wz=0.00) elapsed=43.1s plan[29pts 4.0m] (3.10,-1.95)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=83% mem=18%
[velocity_pid.py-9] [INFO] [1781430926.888239448] [velocity_pid]: [vel_pid→] desired=-0.12 actual=-0.09 corrected=-0.30 err=29.2%
[competition_master_stage3.py-19] [INFO] [1781430928.859963124] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.15,-1.69) yaw=74deg cmd=(vx=-0.12 wz=0.00) elapsed=45.1s plan[29pts 4.0m] (3.10,-1.95)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=75% mem=18%
[imu_madgwick_filter.py-4] [INFO] [1781430929.008739516] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1360 q_w=0.7607 angle=80.9deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781430929.163865766] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3336 q_w=0.8949 angle=53.0deg beta=0.0030
[component_container_isolated-18] [WARN] [1781430929.229555174] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1781430929.229781340] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1781430929.229893589] [behavior_server]: [backup] [ActionServer] Aborting handle.
[cmd_vel_mux.py-8] [INFO] [1781430929.257032183] [cmd_vel_mux]: [mux→] src=nav vx=0.00 wz=0.00
[component_container_isolated-18] [INFO] [1781430929.523009262] [behavior_server]: Running wait
[cmd_vel_mux.py-8] [INFO] [1781430929.755502037] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.52s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1781430929.767934459] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[competition_master_stage3.py-19] [INFO] [1781430930.865821469] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.11,-1.88) yaw=75deg cmd=(vx=0.00 wz=0.00) elapsed=47.1s plan[29pts 4.0m] (3.10,-1.95)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=100% mem=18%
[component_container_isolated-18] [INFO] [1781430932.523405407] [behavior_server]: wait completed successfully
[competition_master_stage3.py-19] [INFO] [1781430932.860351928] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.11,-1.88) yaw=75deg cmd=(vx=0.00 wz=0.00) elapsed=49.1s plan[29pts 4.0m] (3.10,-1.95)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=62% mem=18%
[component_container_isolated-18] [WARN] [1781430933.634582329] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2327 Hz
[component_container_isolated-18] [INFO] [1781430933.825221247] [controller_server]: Received a goal, begin computing control effort.
[cmd_vel_mux.py-8] [INFO] [1781430933.859194570] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=0.11
[velocity_pid.py-9] [INFO] [1781430933.890006700] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.10 err=100.0%
[competition_master_stage3.py-19] [INFO] [1781430934.861077295] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.11,-1.88) yaw=75deg cmd=(vx=0.45 wz=0.22) elapsed=51.1s plan[24pts 3.4m] (3.10,-1.95)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=80% mem=18%
[component_container_isolated-18] [WARN] [1781430936.628239813] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4213 Hz
[velocity_pid.py-9] [INFO] [1781430936.691633567] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.45 corrected=-0.10 err=25.3%
[cmd_vel_mux.py-8] [INFO] [1781430936.722240867] [cmd_vel_mux]: [mux→] src=nav vx=0.27 wz=-0.01
[velocity_pid.py-9] [INFO] [1781430936.756402273] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.11 -> current=-0.01 dt=0.0331s, resetting
[component_container_isolated-18] [INFO] [1781430936.828622065] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1781430936.860498274] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.14,-1.11) yaw=97deg cmd=(vx=0.18 wz=-0.14) elapsed=53.1s plan[18pts 2.5m] (3.10,-1.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=80% mem=18%
[imu_madgwick_filter.py-4] [WARN] [1781430937.643731137] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1500s > 0.15s, capping
[velocity_pid.py-9] [INFO] [1781430938.604033847] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.44 corrected=-0.06 err=21.7%
[cmd_vel_mux.py-8] [INFO] [1781430938.626200232] [cmd_vel_mux]: [mux→] src=nav vx=0.27 wz=-0.18
[velocity_pid.py-9] [INFO] [1781430938.858221703] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.00 -> current=-0.09 dt=0.0349s, resetting
[competition_master_stage3.py-19] [INFO] [1781430938.868417275] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.92,-0.44) yaw=117deg cmd=(vx=0.00 wz=-0.23) elapsed=55.1s plan[18pts 2.5m] (3.10,-1.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=90% mem=18%
[imu_madgwick_filter.py-4] [INFO] [1781430939.008877884] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1556 q_w=0.4430 angle=127.4deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781430939.170260305] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3835 q_w=0.6441 angle=99.8deg beta=0.0030
[velocity_pid.py-9] [INFO] [1781430939.623828932] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.11 corrected=-0.29 err=63.0%
[component_container_isolated-18] [WARN] [1781430939.626883041] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4263 Hz
[component_container_isolated-18] [INFO] [1781430939.728638435] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781430939.822326286] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.03
[velocity_pid.py-9] [INFO] [1781430939.954332399] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0330s, resetting
[velocity_pid.py-9] [INFO] [1781430940.624753588] [velocity_pid]: [vel_pid→] desired=0.45 actual=0.14 corrected=0.38 err=69.6%
[competition_master_stage3.py-19] [INFO] [1781430940.862605120] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.73,-0.25) yaw=122deg cmd=(vx=0.45 wz=-0.20) elapsed=57.1s plan[11pts 1.5m] (2.70,-0.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=67% mem=18%
[velocity_pid.py-9] [INFO] [1781430942.203108065] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.10 -> current=0.03 dt=0.0333s, resetting
[component_container_isolated-18] [WARN] [1781430942.627206114] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2469 Hz
[competition_master_stage3.py-19] [INFO] [1781430942.865862732] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.38,0.52) yaw=115deg cmd=(vx=0.45 wz=0.28) elapsed=59.1s plan[6pts 0.7m] (2.40,0.55)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=93% mem=18%
[velocity_pid.py-9] [INFO] [1781430942.891202394] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.46 corrected=0.01 err=27.2%
[component_container_isolated-18] [INFO] [1781430942.928645995] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781430942.957108184] [cmd_vel_mux]: [mux→] src=nav vx=0.18 wz=-0.09
[velocity_pid.py-9] [INFO] [1781430942.987907152] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.03 -> current=-0.09 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1781430943.258519903] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.08 -> current=-0.01 dt=0.0334s, resetting
[component_container_isolated-18] [INFO] [1781430943.329451210] [controller_server]: Reached the goal!
[velocity_pid.py-9] [INFO] [1781430943.357778774] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.09 -> current=0.03 dt=0.0351s, resetting
[component_container_isolated-18] [INFO] [1781430943.822134375] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-19] [INFO] [1781430943.834048565] [competition_master_stage3]: [结果回调] 巡航完成, 到达VLM路点, 触发VLM推理...
[competition_master_stage3.py-19] [INFO] [1781430943.838114003] [competition_master_stage3]: [VLM] 发布 sign4return=100, 拍照推理中...
[competition_master_stage3.py-19] [INFO] [1781430943.845522173] [competition_master_stage3]: [状态机] CRUISE_CHANNEL → RETURN_P
[vision_ai_node-14] [INFO] [1781430943.848402325] [vision_ai_node]: Received sign4return: 100
[competition_master_stage3.py-19] [INFO] [1781430943.851728767] [competition_master_stage3]: [RETURN] 清除机器人周围1.5m + 直接返航至 P点 (-1.99,-0.01)
[vision_ai_node-14] [INFO] [1781430943.852249264] [vision_ai_node]: Received trigger signal (sign4return=100), subscribing to image topic...
[vision_ai_node-14] [INFO] [1781430943.877873759] [vision_ai_node]: Subscribed to /aurora/rgb/image_raw topic
[vision_ai_node-14] [INFO] [1781430943.897921824] [vision_ai_node]: Received compressed image, processing with AI model...
[competition_master_stage3.py-19] [INFO] [1781430944.359297863] [competition_master_stage3]: [DIAG] nav目标距离: 4.33m, robot=(2.30,0.64) → target=(-1.99,-0.01)
[competition_master_stage3.py-19] [INFO] [1781430944.362048724] [competition_master_stage3]: >>> 发送导航目标 [P点返航]: (-1.99, -0.01, yaw=0.26)
[component_container_isolated-18] [INFO] [1781430944.364873584] [bt_navigator]: Begin navigating from current location (2.21, 0.85) to (-1.99, -0.01)
[competition_master_stage3.py-19] [INFO] [1781430944.378734014] [competition_master_stage3]: 导航目标已接受，车辆出发...
[component_container_isolated-18] [WARN] [1781430944.636270544] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 3.7323 Hz
[component_container_isolated-18] [INFO] [1781430944.770155450] [controller_server]: Received a goal, begin computing control effort.
[cmd_vel_mux.py-8] [INFO] [1781430944.827185078] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=0.12
[velocity_pid.py-9] [INFO] [1781430944.856234431] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.09 err=100.0%
[competition_master_stage3.py-19] [INFO] [1781430944.861234489] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.30,0.64) yaw=115deg cmd=(vx=0.00 wz=0.00) elapsed=61.1s plan[44pts 6.1m] (2.20,0.85)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=86% mem=19%
[competition_master_stage3.py-19] [INFO] [1781430946.860100585] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.71,1.22) yaw=166deg cmd=(vx=0.45 wz=0.74) elapsed=63.1s plan[44pts 6.1m] (2.20,0.85)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=91% mem=19%
[velocity_pid.py-9] [INFO] [1781430947.355964847] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.45 corrected=-0.16 err=25.3%
[cmd_vel_mux.py-8] [INFO] [1781430947.356412261] [cmd_vel_mux]: [mux→] src=nav vx=0.27 wz=0.47
[velocity_pid.py-9] [INFO] [1781430947.588508181] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.00 -> current=-0.09 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781430947.592087289] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.10 -> current=-0.03 dt=0.0334s, resetting
[component_container_isolated-18] [WARN] [1781430947.637779851] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3025 Hz
[component_container_isolated-18] [INFO] [1781430947.770731810] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781430947.868149071] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.28
[velocity_pid.py-9] [INFO] [1781430947.991204788] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0351s, resetting
[velocity_pid.py-9] [INFO] [1781430948.054919386] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.03 -> current=0.10 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1781430948.357527249] [velocity_pid]: [vel_pid→] desired=0.45 actual=0.06 corrected=0.33 err=87.1%
[competition_master_stage3.py-19] [INFO] [1781430948.860215904] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.10,1.08) yaw=-144deg cmd=(vx=0.45 wz=0.99) elapsed=65.1s plan[38pts 5.4m] (1.30,1.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=80% mem=19%
[imu_madgwick_filter.py-4] [INFO] [1781430949.013459180] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1750 q_w=-0.5442 angle=245.9deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781430949.163112268] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4337 q_w=-0.3530 angle=221.3deg beta=0.0030
[velocity_pid.py-9] [INFO] [1781430950.004529286] [velocity_pid]: [vel_pid→] desired=0.27 actual=0.43 corrected=-0.08 err=59.6%
[cmd_vel_mux.py-8] [INFO] [1781430950.023490233] [cmd_vel_mux]: [mux→] src=nav vx=0.18 wz=0.06
[velocity_pid.py-9] [INFO] [1781430950.187561252] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.00 -> current=-0.09 dt=0.0334s, resetting
[component_container_isolated-18] [WARN] [1781430950.634691907] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3052 Hz
[component_container_isolated-18] [INFO] [1781430950.770716273] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781430950.856340223] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.29
[competition_master_stage3.py-19] [INFO] [1781430950.861391490] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.77,0.33) yaw=-87deg cmd=(vx=-0.30 wz=-0.54) elapsed=67.1s plan[31pts 4.3m] (0.80,0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=75% mem=19%
[velocity_pid.py-9] [INFO] [1781430950.989160397] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781430951.022929563] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.12 corrected=0.17 err=295.0%
[velocity_pid.py-9] [INFO] [1781430951.054917904] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.08 dt=0.0331s, resetting
[competition_master_stage3.py-19] [INFO] [1781430952.859784235] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.93,-0.22) yaw=-78deg cmd=(vx=0.45 wz=-0.68) elapsed=69.1s plan[31pts 4.3m] (0.80,0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=70% mem=19%
[component_container_isolated-18] [WARN] [1781430953.626495504] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1781430953.626736753] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (-1.99, -0.01)
[component_container_isolated-18] [WARN] [1781430953.626840752] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1781430953.765716028] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[velocity_pid.py-9] [INFO] [1781430953.766506940] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.45 corrected=0.00 err=25.3%
[component_container_isolated-18] [INFO] [1781430953.775928227] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781430953.790863571] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781430953.791007445] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781430953.810026435] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[cmd_vel_mux.py-8] [INFO] [1781430953.823512243] [cmd_vel_mux]: [mux→] src=nav vx=0.18 wz=-0.43
[velocity_pid.py-9] [INFO] [1781430953.992125789] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.00 -> current=-0.09 dt=0.0335s, resetting
[component_container_isolated-18] [WARN] [1781430954.628883542] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2284 Hz
[component_container_isolated-18] [INFO] [1781430954.770734639] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781430954.789209173] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.10 corrected=-0.31 err=65.3%
[cmd_vel_mux.py-8] [INFO] [1781430954.860801739] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.49
[competition_master_stage3.py-19] [INFO] [1781430954.861759276] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.78,-0.69) yaw=-151deg cmd=(vx=-0.30 wz=0.74) elapsed=71.1s plan[25pts 3.2m] (0.70,-0.75)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=80% mem=19%
[velocity_pid.py-9] [INFO] [1781430954.988839820] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0223s, resetting
[velocity_pid.py-9] [INFO] [1781430955.089785201] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.12 -> current=-0.01 dt=0.0337s, resetting
[velocity_pid.py-9] [INFO] [1781430955.794016760] [velocity_pid]: [vel_pid→] desired=0.45 actual=0.20 corrected=0.39 err=56.4%
[competition_master_stage3.py-19] [INFO] [1781430956.861753889] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.70,-0.76) yaw=-146deg cmd=(vx=0.45 wz=-0.40) elapsed=73.1s plan[25pts 3.2m] (0.70,-0.75)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=82% mem=19%
[component_container_isolated-18] [WARN] [1781430957.635822628] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3024 Hz
[component_container_isolated-18] [INFO] [1781430957.770730265] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1781430958.860626861] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.32,-0.91) yaw=158deg cmd=(vx=0.45 wz=-0.20) elapsed=75.1s plan[19pts 2.6m] (0.10,-0.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=80% mem=19%
[imu_madgwick_filter.py-4] [INFO] [1781430959.008203814] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1947 q_w=0.1086 angle=167.5deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781430959.170645613] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4834 q_w=0.4017 angle=132.6deg beta=0.0030
[velocity_pid.py-9] [INFO] [1781430959.756080622] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.45 corrected=0.02 err=25.3%
[cmd_vel_mux.py-8] [INFO] [1781430959.822348094] [cmd_vel_mux]: [mux→] src=nav vx=0.18 wz=0.20
[velocity_pid.py-9] [INFO] [1781430959.996449546] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.00 -> current=-0.09 dt=0.0385s, resetting
[component_container_isolated-18] [WARN] [1781430960.629384085] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3122 Hz
[velocity_pid.py-9] [INFO] [1781430960.757980634] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.12 corrected=-0.27 err=61.0%
[component_container_isolated-18] [INFO] [1781430960.779405739] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781430960.859247855] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.07
[competition_master_stage3.py-19] [INFO] [1781430960.860778139] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.79,-0.67) yaw=151deg cmd=(vx=-0.30 wz=0.07) elapsed=77.1s plan[11pts 1.5m] (-0.90,-0.55)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=90% mem=19%
[velocity_pid.py-9] [INFO] [1781430960.988338984] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0338s, resetting
[velocity_pid.py-9] [INFO] [1781430961.758667583] [velocity_pid]: [vel_pid→] desired=0.45 actual=0.20 corrected=0.33 err=55.1%
[competition_master_stage3.py-19] [INFO] [1781430962.864267922] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.20,-0.46) yaw=152deg cmd=(vx=0.45 wz=-0.19) elapsed=79.1s plan[11pts 1.5m] (-0.90,-0.55)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=88% mem=19%
[velocity_pid.py-9] [INFO] [1781430963.455411062] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.46 corrected=-0.00 err=27.2%
[cmd_vel_mux.py-8] [INFO] [1781430963.523139990] [cmd_vel_mux]: [mux→] src=nav vx=0.18 wz=-0.08
[velocity_pid.py-9] [INFO] [1781430963.621243272] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.08 -> current=0.04 dt=0.0321s, resetting
[component_container_isolated-18] [WARN] [1781430963.633506631] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3083 Hz
[velocity_pid.py-9] [INFO] [1781430963.689187491] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.00 -> current=-0.09 dt=0.0337s, resetting
[component_container_isolated-18] [INFO] [1781430963.770721477] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781430963.956070469] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.06 -> current=0.03 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1781430963.964560762] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.08 dt=0.0333s, resetting
[cmd_vel_mux.py-8] [INFO] [1781430964.058259067] [cmd_vel_mux]: [mux→] src=nav vx=0.23 wz=-0.34
[velocity_pid.py-9] [INFO] [1781430964.457936586] [velocity_pid]: [vel_pid→] desired=0.22 actual=0.13 corrected=0.08 err=39.7%
[competition_master_stage3.py-19] [INFO] [1781430964.865110320] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.64,-0.19) yaw=133deg cmd=(vx=0.20 wz=-0.24) elapsed=81.1s plan[6pts 0.7m] (-1.60,-0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=67% mem=19%
[cmd_vel_mux.py-8] [INFO] [1781430965.225400071] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=-0.13
[velocity_pid.py-9] [INFO] [1781430965.287836651] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.07 -> current=-0.02 dt=0.0337s, resetting
[velocity_pid.py-9] [INFO] [1781430965.365475117] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.00 -> current=0.12 dt=0.0342s, resetting
[velocity_pid.py-9] [INFO] [1781430965.488871158] [velocity_pid]: [vel_pid→] desired=-0.14 actual=0.14 corrected=-0.26 err=203.2%
[velocity_pid.py-9] [INFO] [1781430966.491069464] [velocity_pid]: [vel_pid→] desired=-0.14 actual=-0.09 corrected=-0.17 err=39.5%
[component_container_isolated-18] [WARN] [1781430966.631549135] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3110 Hz
[component_container_isolated-18] [INFO] [1781430966.770727395] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781430966.858931521] [cmd_vel_mux]: [mux→] src=nav vx=0.03 wz=-0.03
[competition_master_stage3.py-19] [INFO] [1781430966.859254561] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.71,-0.12) yaw=122deg cmd=(vx=-0.15 wz=0.22) elapsed=83.1s plan[5pts 0.5m] (-1.70,-0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=80% mem=19%
[velocity_pid.py-9] [INFO] [1781430966.892748445] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.06 -> current=0.03 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781430966.897300923] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.09 -> current=-0.03 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781430967.530998109] [velocity_pid]: [vel_pid→] desired=0.17 actual=0.01 corrected=0.21 err=96.5%
[velocity_pid.py-9] [INFO] [1781430968.656880534] [velocity_pid]: [vel_pid→] desired=0.12 actual=0.15 corrected=0.05 err=23.6%
[competition_master_stage3.py-19] [INFO] [1781430968.860257706] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.76,-0.03) yaw=108deg cmd=(vx=0.11 wz=-0.67) elapsed=85.1s plan[5pts 0.5m] (-1.70,-0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=80% mem=19%
[cmd_vel_mux.py-8] [INFO] [1781430968.922585080] [cmd_vel_mux]: [mux→] src=nav vx=0.01 wz=-0.62
[velocity_pid.py-9] [INFO] [1781430968.988497021] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.01 -> current=-0.08 dt=0.0261s, resetting
[imu_madgwick_filter.py-4] [INFO] [1781430969.008229596] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2146 q_w=0.5170 angle=117.7deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781430969.162146293] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5320 q_w=0.7760 angle=78.2deg beta=0.0030
[velocity_pid.py-9] [INFO] [1781430969.190014621] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.12 -> current=0.00 dt=0.0227s, resetting
[component_container_isolated-18] [WARN] [1781430969.626723665] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3251 Hz
[velocity_pid.py-9] [INFO] [1781430969.687876254] [velocity_pid]: [vel_pid→] desired=-0.11 actual=0.00 corrected=-0.15 err=100.0%
[component_container_isolated-18] [INFO] [1781430969.770726409] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781430969.859767826] [cmd_vel_mux]: [mux→] src=nav vx=0.08 wz=0.64
[velocity_pid.py-9] [INFO] [1781430969.888856524] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.01 -> current=0.08 dt=0.0337s, resetting
[velocity_pid.py-9] [INFO] [1781430970.690769455] [velocity_pid]: [vel_pid→] desired=0.14 actual=0.02 corrected=0.16 err=86.1%
[competition_master_stage3.py-19] [INFO] [1781430970.864100398] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.77,0.03) yaw=96deg cmd=(vx=0.14 wz=0.28) elapsed=87.1s plan[4pts 0.4m] (-1.80,0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=81% mem=19%
[cmd_vel_mux.py-8] [INFO] [1781430971.459443841] [cmd_vel_mux]: [mux→] src=nav vx=-0.03 wz=0.19
[velocity_pid.py-9] [INFO] [1781430971.488490290] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.06 -> current=-0.03 dt=0.0338s, resetting
[velocity_pid.py-9] [INFO] [1781430971.722468162] [velocity_pid]: [vel_pid→] desired=-0.10 actual=0.10 corrected=-0.18 err=204.0%
[component_container_isolated-18] [WARN] [1781430972.632459657] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.1721 Hz
[velocity_pid.py-9] [INFO] [1781430972.758082951] [velocity_pid]: [vel_pid→] desired=-0.12 actual=-0.09 corrected=-0.12 err=26.1%
[component_container_isolated-18] [INFO] [1781430972.770721809] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781430972.828423209] [cmd_vel_mux]: [mux→] src=nav vx=-0.03 wz=-0.90
[competition_master_stage3.py-19] [INFO] [1781430972.863735046] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.80,0.13) yaw=105deg cmd=(vx=-0.12 wz=-0.77) elapsed=89.1s plan[4pts 0.3m] (-1.80,0.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=80% mem=19%
[velocity_pid.py-9] [INFO] [1781430972.897717722] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0438s, resetting
[velocity_pid.py-9] [INFO] [1781430973.759590705] [velocity_pid]: [vel_pid→] desired=0.14 actual=0.01 corrected=0.18 err=95.8%
[cmd_vel_mux.py-8] [INFO] [1781430974.757536323] [cmd_vel_mux]: [mux→] src=nav vx=-0.02 wz=-0.40
[velocity_pid.py-9] [INFO] [1781430974.770657180] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.13 corrected=-0.06 err=80.4%
[velocity_pid.py-9] [INFO] [1781430974.789206594] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.07 -> current=-0.02 dt=0.0223s, resetting
[competition_master_stage3.py-19] [INFO] [1781430974.864746706] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.81,0.14) yaw=94deg cmd=(vx=-0.02 wz=-0.40) elapsed=91.1s plan[4pts 0.3m] (-1.80,0.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=93% mem=19%
[velocity_pid.py-9] [INFO] [1781430975.254694584] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.03 -> current=0.08 dt=0.0330s, resetting
[component_container_isolated-18] [WARN] [1781430975.627298377] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3215 Hz
[component_container_isolated-18] [INFO] [1781430975.770720429] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781430975.792896994] [velocity_pid]: [vel_pid→] desired=-0.13 actual=-0.09 corrected=-0.14 err=32.9%
[velocity_pid.py-9] [INFO] [1781430976.187911812] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.08 dt=0.0337s, resetting
[velocity_pid.py-9] [INFO] [1781430976.837102473] [velocity_pid]: [vel_pid→] desired=-0.10 actual=-0.16 corrected=-0.06 err=57.0%
[competition_master_stage3.py-19] [INFO] [1781430976.869497159] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.82,0.08) yaw=92deg cmd=(vx=-0.10 wz=-0.72) elapsed=93.1s plan[3pts 0.4m] (-1.80,0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=88% mem=19%
[component_container_isolated-18] [INFO] [1781430977.271362536] [controller_server]: Reached the goal!
[cmd_vel_mux.py-8] [INFO] [1781430977.322628428] [cmd_vel_mux]: [mux→] src=nav vx=-0.01 wz=-0.80
[component_container_isolated-18] [INFO] [1781430977.765839911] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-19] [INFO] [1781430977.778763227] [competition_master_stage3]: [结果回调] 已回到P点, 任务完成!
[competition_master_stage3.py-19] [INFO] [1781430977.782386461] [competition_master_stage3]: [状态机] RETURN_P → DONE
[competition_master_stage3.py-19] [INFO] [1781430977.785823903] [competition_master_stage3]:
[competition_master_stage3.py-19] [INFO] [1781430977.788765098] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1781430977.791583669] [competition_master_stage3]: >>> [Stage 3] 任务结束 <<<
[competition_master_stage3.py-19] [INFO] [1781430977.794991987] [competition_master_stage3]:   最终状态: DONE
[competition_master_stage3.py-19] [INFO] [1781430977.798733303] [competition_master_stage3]:   总耗时:   94.1s
[competition_master_stage3.py-19] [INFO] [1781430977.803860821] [competition_master_stage3]:   --- 各阶段耗时 ---
[competition_master_stage3.py-19] [INFO] [1781430977.806407685] [competition_master_stage3]:   LAUNCH................ 14.9s
[competition_master_stage3.py-19] [INFO] [1781430977.809197047] [competition_master_stage3]:   NAV_TO_QR............. 13.5s
[competition_master_stage3.py-19] [INFO] [1781430977.812287950] [competition_master_stage3]:   BACKING_UP............ 6.0s
[competition_master_stage3.py-19] [INFO] [1781430977.815157062] [competition_master_stage3]:   CRUISE_CHANNEL........ 40.7s
[competition_master_stage3.py-19] [INFO] [1781430977.818431130] [competition_master_stage3]:   RETURN_P.............. 33.9s
[competition_master_stage3.py-19] [INFO] [1781430977.822171405] [competition_master_stage3]:   (transition/overhead). -14.9s
[competition_master_stage3.py-19] [INFO] [1781430977.827170549] [competition_master_stage3]:   --- ---
[competition_master_stage3.py-19] [INFO] [1781430977.831740820] [competition_master_stage3]:   QR 原始数据: 1584
[competition_master_stage3.py-19] [INFO] [1781430977.835517302] [competition_master_stage3]:   QR 方向:   逆时针 (CW=顺时针/odd, CCW=逆时针/even)
[competition_master_stage3.py-19] [WARN] [1781430977.838835871] [competition_master_stage3]:   VLM 结果:  未收到
[competition_master_stage3.py-19] [INFO] [1781430977.841460109] [competition_master_stage3]:   超时限制:  180.0s (全局)
[competition_master_stage3.py-19] [INFO] [1781430977.845670131] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1781430977.851041690] [competition_master_stage3]: [TRAJ] 轨迹已保存: /userdata/dev_ws/trajectory.csv (101 点)
[cmd_vel_mux.py-8] [INFO] [1781430978.762523137] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.51s > 0.5s, marked inactive
[competition_master_stage3.py-19] [INFO] [1781430978.863049639] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.83,-0.07) yaw=79deg cmd=(vx=0.00 wz=0.00) elapsed=95.1s plan[3pts 0.4m] (-1.80,0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=88% mem=19%
[imu_madgwick_filter.py-4] [INFO] [1781430979.009545808] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2345 q_w=0.6598 angle=97.4deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781430979.161122206] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5798 q_w=0.8783 angle=57.1deg beta=0.0030
[competition_master_stage3.py-19] [INFO] [1781430980.865305057] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.83,-0.07) yaw=79deg cmd=(vx=0.00 wz=0.00) elapsed=97.1s plan[3pts 0.4m] (-1.80,0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=93% mem=19%
[competition_master_stage3.py-19] [INFO] [1781430982.866167831] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.83,-0.07) yaw=79deg cmd=(vx=0.00 wz=0.00) elapsed=99.1s plan[3pts 0.4m] (-1.80,0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=100% mem=19%
[vision_ai_node-14] [INFO] [1781430983.905486192] [vision_ai_node]: AI Analysis Result: 这是一张**室内装修阶段**的场景照片，整体简洁空旷，细节如下：
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] ### 场景与环境
[vision_ai_node-14] 画面呈现一个刚装修（或待装修）的房间：
[vision_ai_node-14] - **墙面**：覆盖**浅米色（偏暖）的光滑瓷砖**，拼接缝清晰；瓷砖表面反光强烈，左侧反射出室内窗户的影像（可见窗框、透入的光线），暗示瓷砖为抛光/釉面材质。
[vision_ai_node-14] - **地面**：铺有**浅黄色（前景）与浅绿色（中后景）的塑料保护膜**，表面褶皱明显，推测为施工时保护地面或墙面所用。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] ### 核心物体（饮料瓶）
[vision_ai_node-14] 画面**中下部**直立着一只塑料饮料瓶，视觉焦点集中于此：
[vision_ai_node-14] - **瓶身**：大部分为**透明材质**，内部残留少量液体（液面接近瓶底）；
[vision_ai_node-14] - **瓶盖**：**金色**，光泽感强；
[vision_ai_node-14] - **标签**：**红色**，带有白色图案与文字（疑似饮料品牌标识，设计风格简约）。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] ### 色彩与细节
[vision_ai_node-14] - **墙面**：浅米色（暖调），因光滑反光，左侧瓷砖映出室内窗户的轮廓与光线，增强空间的通透感。
[vision_ai_node-14] - **地面**：浅黄色（前景）+ 浅绿色（中后景），塑料膜的褶皱与色彩过渡，凸显“施工保护”的场景逻辑。
[vision_ai_node-14] - **右侧物体**：一块**亮蓝色的布料（或遮挡物）**，边缘整齐，与浅色调背景形成强烈色彩对比。
[vision_ai_node-14] - **饮料瓶**：透明（瓶身）、金色（盖）、红色（标签）的色彩组合，在浅色环境中格外醒目；少量液体的透明感，与“快喝完”的状态呼应。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] ### 场景逻辑
[vision_ai_node-14] 瓷砖墙的反光、地面的塑料膜，结合饮料瓶的“临时感”，暗示这是一个**装修中的房间**（如新房贴砖后、等待进一步施工的阶段）。右侧的蓝色遮挡物、左侧的窗户反光，丰富了空间的细节层次。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] 整体氛围简洁、空旷，色彩对比（红-金-蓝-浅暖）与材质对比（光滑瓷砖、褶皱塑料膜、透明瓶身），让场景既具“施工感”，又因饮料瓶的存在增添了一丝生活气息。
[competition_master_stage3.py-19] [INFO] [1781430983.917333681] [competition_master_stage3]: [VLM] 后台收到推理结果: 这是一张**室内装修阶段**的场景照片，整体简洁空旷，细节如下：
[competition_master_stage3.py-19]
[competition_master_stage3.py-19]
[competition_master_stage3.py-19] ### 场景与环境
[competition_master_stage3.py-19] 画面呈现一个刚装修（或待装修）的房间：
[competition_master_stage3.py-19] - **墙面**：覆盖**浅米色（偏暖）的光滑瓷砖**，拼接缝清晰；瓷砖表面反光强烈，左侧反射出室...
[vision_ai_node-14] [INFO] [1781430983.918762675] [vision_ai_node]: Unsubscribed from image topic
[competition_master_stage3.py-19] [INFO] [1781430984.877581493] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.83,-0.07) yaw=79deg cmd=(vx=0.00 wz=0.00) elapsed=101.1s plan[3pts 0.4m] (-1.80,0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=100% mem=19%
[competition_master_stage3.py-19] [INFO] [1781430986.859399179] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.83,-0.07) yaw=79deg cmd=(vx=0.00 wz=0.00) elapsed=103.1s plan[3pts 0.4m] (-1.80,0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=80% mem=19%
[competition_master_stage3.py-19] [INFO] [1781430988.866209730] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.83,-0.07) yaw=79deg cmd=(vx=0.00 wz=0.00) elapsed=105.1s plan[3pts 0.4m] (-1.80,0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=62% mem=19%
[imu_madgwick_filter.py-4] [INFO] [1781430989.007972982] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2545 q_w=0.6372 angle=100.8deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781430989.163879801] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=6287 q_w=0.8784 angle=57.1deg beta=0.0030
[competition_master_stage3.py-19] [INFO] [1781430990.865443872] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.83,-0.07) yaw=79deg cmd=(vx=0.00 wz=0.00) elapsed=107.1s plan[3pts 0.4m] (-1.80,0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=71% mem=19%
[competition_master_stage3.py-19] [INFO] [1781430992.863672368] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.83,-0.07) yaw=79deg cmd=(vx=0.00 wz=0.00) elapsed=109.1s plan[3pts 0.4m] (-1.80,0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=100% mem=19%
[competition_master_stage3.py-19] [INFO] [1781430994.861776340] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.83,-0.07) yaw=79deg cmd=(vx=0.00 wz=0.00) elapsed=111.1s plan[3pts 0.4m] (-1.80,0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=82% mem=19%
[competition_master_stage3.py-19] [INFO] [1781430996.860683532] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.83,-0.07) yaw=79deg cmd=(vx=0.00 wz=0.00) elapsed=113.1s plan[3pts 0.4m] (-1.80,0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=89% mem=19%
^C[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[rviz2-20] [INFO] [1781430997.903357841] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [origincar_base_node-1]: process has died [pid 26691, exit code -6, cmd '/userdata/dev_ws/install/origincar_base/lib/origincar_base/origincar_base_node --ros-args --params-file /tmp/launch_params_qcsuuvle --params-file /tmp/launch_params_t4xwcg2q'].
[ERROR] [lslidar_driver_node-2]: process has died [pid 26693, exit code -6, cmd '/userdata/dev_ws/install/lslidar_driver/lib/lslidar_driver/lslidar_driver_node --ros-args -r __node:=lslidar_driver_node --params-file /userdata/dev_ws/install/lslidar_driver/share/lslidar_driver/params/lsx10.yaml'].
[ERROR] [rviz2-20]: process has died [pid 27052, exit code -11, cmd '/opt/ros/humble/lib/rviz2/rviz2 -d /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/rviz/nav.rviz --ros-args -r __node:=rviz2'].
[INFO] [ekf_node-7]: process has finished cleanly [pid 26703]
[INFO] [static_transform_publisher-10]: process has finished cleanly [pid 26747]
[INFO] [map_server-15]: process has finished cleanly [pid 26855]
[INFO] [robot_state_publisher-3]: process has finished cleanly [pid 26695]
[INFO] [costmap_filter_info_server-16]: process has finished cleanly [pid 26857]
[INFO] [lifecycle_manager-17]: process has finished cleanly [pid 26861]
[component_container_isolated-18] [INFO] [1781430997.903482841] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-18] [INFO] [1781430997.903626798] [lifecycle_manager_navigation]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_navigation)
[component_container_isolated-18] [INFO] [1781430997.903924922] [lifecycle_manager_navigation]: Terminating bond timer...
[origincar_base_node-1] [INFO] [1781430997.903519091] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1781430997.903891839] [origincar_base]: Stop command sent to STM32 on shutdown.
[origincar_base_node-1] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[static_transform_publisher-10] [INFO] [1781430997.903648632] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-17] [INFO] [1781430997.903662257] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-17] [INFO] [1781430997.905402666] [lifecycle_manager_keepout]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_keepout)
[lifecycle_manager-17] [INFO] [1781430997.905626748] [lifecycle_manager_keepout]: Terminating bond timer...
[aurora930_node-11] [INFO] [1781430997.904034630] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[aurora930_node-11] I0614 17:56:38.017397 26749 ros2_node.cc:90] process quit succeed
[aurora930_node-11] I0614 17:56:38.017589 26749 aurora900_ros2_device.cc:83] begin stop()
[aurora930_node-11] I0614 17:56:38.017752 26749 aurora900_ros2_device.cc:103] stop stream
[aurora930_node-11] 2026-06-14 17:56:38.071 ( 140.401s) [        9B7D4020]      aurora900_impl.cc:648   INFO| ir_stream_count_=0, rgb_stream_count_=0, depth_stream_count_=0
[aurora930_node-11] 2026-06-14 17:56:38.071 ( 140.401s) [        9B7D4020]      aurora900_impl.cc:649   INFO| mask=7
[aurora930_node-11] I0614 17:56:38.281883 26749 aurora900_ros2_device.cc:105] destroy stream
[aurora930_node-11] I0614 17:56:38.282142 26749 aurora900_ros2_device.cc:110] close glog
[aurora930_node-11] WARNING: Logging before InitGoogleLogging() is written to STDERR
[aurora930_node-11] I0614 17:56:38.282297 26749 ros2_device.cc:113] close device...
[aurora930_node-11] 2026-06-14 17:56:38.781 ( 141.111s) [        67FF57E0]         cmd_backend.cc:40    INFO| RunBlocking is end!!!
[aurora930_node-11] 2026-06-14 17:56:38.982 ( 141.312s) [        9B7D4020]deptrum_camera_vendor.c:121   INFO| device is close.
[aurora930_node-11] I0614 17:56:38.984236 26749 ros2_device.cc:116] quit succeed
[costmap_filter_info_server-16] [INFO] [1781430997.904157546] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-16] [INFO] [1781430997.904362837] [keepout_filter_info_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_filter_info_server)
[costmap_filter_info_server-16] [INFO] [1781430997.904618753] [keepout_filter_info_server]: Deactivating
[costmap_filter_info_server-16] [INFO] [1781430997.904707752] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-16] [INFO] [1781430997.934033877] [keepout_filter_info_server]: Cleaning up
[costmap_filter_info_server-16] [INFO] [1781430997.934307835] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-16] [INFO] [1781430998.077471059] [keepout_filter_info_server]: Destroying
[robot_state_publisher-3] [INFO] [1781430997.905592790] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-15] [INFO] [1781430997.906041205] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-15] [INFO] [1781430997.906265996] [keepout_mask_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_mask_server)
[map_server-15] [INFO] [1781430997.907779031] [keepout_mask_server]: Deactivating
[map_server-15] [INFO] [1781430997.908017571] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[map_server-15] [INFO] [1781430997.921291473] [keepout_mask_server]: Cleaning up
[map_server-15] [INFO] [1781430997.921744471] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[map_server-15] [INFO] [1781430998.058497681] [keepout_mask_server]: Destroying
[ekf_node-7] [INFO] [1781430997.912906926] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[INFO] [imu_madgwick_filter.py-4]: process has finished cleanly [pid 26697]
[origincar_base_node-1] terminate called after throwing an instance of 'rclcpp::exceptions::RCLError'
[origincar_base_node-1]   what():  failed to create guard condition: the given context is not valid, either rcl_init() was not called or rcl_shutdown() was called., at ./src/rcl/guard_condition.c:67
[lifecycle_manager-17] [INFO] [1781430998.091698791] [lifecycle_manager_keepout]: Destroying lifecycle_manager_keepout
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
[component_container_isolated-18] [INFO] [1781430998.455100874] [waypoint_follower]: Running Nav2 LifecycleNode rcl preshutdown (waypoint_follower)
[component_container_isolated-18] [INFO] [1781430998.455508955] [waypoint_follower]: Deactivating
[component_container_isolated-18] [INFO] [1781430998.455637705] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781430998.466094410] [waypoint_follower]: Cleaning up
[component_container_isolated-18] [INFO] [1781430998.499434019] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781430998.499592143] [behavior_server]: Running Nav2 LifecycleNode rcl preshutdown (behavior_server)
[component_container_isolated-18] [INFO] [1781430998.499721351] [behavior_server]: Deactivating
[component_container_isolated-18] [INFO] [1781430998.500079100] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781430998.510697554] [behavior_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781430998.580664466] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781430998.580961798] [lifecycle_manager_localization]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_localization)
[component_container_isolated-18] [INFO] [1781430998.581052839] [lifecycle_manager_localization]: Terminating bond timer...
[component_container_isolated-18] [INFO] [1781430998.661308207] [planner_server]: Running Nav2 LifecycleNode rcl preshutdown (planner_server)
[component_container_isolated-18] [INFO] [1781430998.662308078] [planner_server]: Deactivating
[component_container_isolated-18] [INFO] [1781430998.662622952] [global_costmap.global_costmap]: Deactivating
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
[INFO] [velocity_pid.py-9]: process has finished cleanly [pid 26727]
[INFO] [cmd_vel_mux.py-8]: process has finished cleanly [pid 26709]
[INFO] [imu_madgwick_filter.py-6]: process has finished cleanly [pid 26701]
[component_container_isolated-18] [INFO] [1781430999.620100189] [planner_server]: Deactivating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781430999.620431938] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781430999.630851561] [planner_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781430999.652443678] [global_costmap.global_costmap]: Cleaning up
[component_container_isolated-18] [INFO] [1781430999.660298811] [planner_server]: Cleaning up plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781430999.661390306] [planner_server]: Destroying plugin GridBased of type SmacPlannerHybrid
[INFO] [competition_master_stage3.py-19]: process has finished cleanly [pid 27048]
[ERROR] [bmi088_iio_bridge.py-5]: process has died [pid 26699, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/bmi088_iio_bridge.py --ros-args -r __node:=bmi088_iio_bridge --params-file /tmp/launch_params_l_ic4r0e'].
[ERROR] [vision_ai_node-14]: process has died [pid 26757, exit code 1, cmd '/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node --ros-args -r __node:=vision_ai_node'].
[INFO] [aurora930_node-11]: process has finished cleanly [pid 26749]
[component_container_isolated-18] [INFO] [1781431000.685474527] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781431000.685638152] [velocity_smoother]: Running Nav2 LifecycleNode rcl preshutdown (velocity_smoother)
[component_container_isolated-18] [INFO] [1781431000.685752859] [velocity_smoother]: Deactivating
[component_container_isolated-18] [INFO] [1781431000.685900609] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781431000.696568939] [velocity_smoother]: Cleaning up
[component_container_isolated-18] [INFO] [1781431000.697115812] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781431000.697400727] [smoother_server]: Running Nav2 LifecycleNode rcl preshutdown (smoother_server)
[component_container_isolated-18] [INFO] [1781431000.697829517] [smoother_server]: Deactivating
[component_container_isolated-18] [INFO] [1781431000.698323431] [smoother_server]: Deactivating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781431000.698636097] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781431000.709162177] [smoother_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781431000.709268427] [smoother_server]: Cleaning up smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781431000.727395642] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781431000.727541725] [map_server]: Running Nav2 LifecycleNode rcl preshutdown (map_server)
[component_container_isolated-18] [INFO] [1781431000.727680891] [map_server]: Deactivating
[component_container_isolated-18] [INFO] [1781431000.727846349] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781431000.738292388] [map_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781431000.738601470] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781431000.738752636] [amcl]: Running Nav2 LifecycleNode rcl preshutdown (amcl)
[component_container_isolated-18] [INFO] [1781431000.738972177] [amcl]: Deactivating
[component_container_isolated-18] [INFO] [1781431000.739208343] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781431000.749843048] [amcl]: Cleaning up
[component_container_isolated-18] [INFO] [1781431000.764521694] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781431000.764753943] [bt_navigator]: Running Nav2 LifecycleNode rcl preshutdown (bt_navigator)
[component_container_isolated-18] [INFO] [1781431000.764990234] [bt_navigator]: Deactivating
[component_container_isolated-18] [INFO] [1781431000.765205025] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781431000.775551981] [bt_navigator]: Cleaning up
[component_container_isolated-18] [INFO] [1781431000.994043769] [bt_navigator]: Completed Cleaning up
[component_container_isolated-18] [INFO] [1781431000.994353059] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781431000.994500808] [controller_server]: Running Nav2 LifecycleNode rcl preshutdown (controller_server)
[component_container_isolated-18] [INFO] [1781431000.994718516] [controller_server]: Deactivating
[component_container_isolated-18] [INFO] [1781431000.994788557] [controller_server]: Deactivating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781431000.994991098] [local_costmap.local_costmap]: Deactivating
[component_container_isolated-18] [INFO] [1781431001.142417562] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781431001.152898351] [controller_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781431001.153004351] [controller_server]: Cleaning up controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781431001.153243225] [local_costmap.local_costmap]: Cleaning up
[component_container_isolated-18] [INFO] [1781431002.195805765] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[ERROR] [component_container_isolated-18]: process[component_container_isolated-18] failed to terminate '5' seconds after receiving 'SIGINT', escalating to 'SIGTERM'
[INFO] [component_container_isolated-18]: sending signal 'SIGTERM' to process[component_container_isolated-18]
[component_container_isolated-18] [INFO] [1781431004.381213767] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [component_container_isolated-18]: process[component_container_isolated-18] failed to terminate '10.0' seconds after receiving 'SIGTERM', escalating to 'SIGKILL'
[INFO] [component_container_isolated-18]: sending signal 'SIGKILL' to process[component_container_isolated-18]
[ERROR] [component_container_isolated-18]: process has died [pid 27046, exit code -9, cmd '/opt/ros/humble/lib/rclcpp_components/component_container_isolated --ros-args --log-level info --ros-args -r __node:=nav2_container --params-file /tmp/launch_params_4ldljf25 --params-file /tmp/launch_params_nx2g60ba -r /tf:=tf -r /tf_static:=tf_static'].
root@ubuntu:/userdata/dev_ws#
