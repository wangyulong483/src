root@ubuntu:/userdata/dev_ws# ros2 launch origincar_bringup stage3_bringup.launch.py
[INFO] [launch]: All log files can be found below /root/.ros/log/2026-06-15-15-40-33-528868-ubuntu-62970
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [origincar_base_node-1]: process started with pid [62984]
[INFO] [lslidar_driver_node-2]: process started with pid [62986]
[INFO] [robot_state_publisher-3]: process started with pid [62988]
[INFO] [imu_madgwick_filter.py-4]: process started with pid [62990]
[INFO] [bmi088_iio_bridge.py-5]: process started with pid [62992]
[INFO] [imu_madgwick_filter.py-6]: process started with pid [62994]
[INFO] [ekf_node-7]: process started with pid [62996]
[INFO] [cmd_vel_mux.py-8]: process started with pid [63002]
[INFO] [velocity_pid.py-9]: process started with pid [63017]
[INFO] [static_transform_publisher-10]: process started with pid [63042]
[INFO] [aurora930_node-11]: process started with pid [63045]
[INFO] [qr_decoder-12]: process started with pid [63048]
[INFO] [qr_decision-13]: process started with pid [63052]
[INFO] [vision_ai_node-14]: process started with pid [63063]
[origincar_base_node-1] [INFO] [1781509234.246676024] [origincar_base]: origincar_base serial port opened
[lslidar_driver_node-2] [INFO] [1781509234.254166607] [lslidar_driver_node]: Lidar is N10
[lslidar_driver_node-2] [INFO] [1781509234.269599399] [lslidar_driver_node]: Initialised lslidar without error
[lslidar_driver_node-2] [INFO] [1781509234.269785024] [lslidar_driver_node]: Successfully initialize driver...
[robot_state_publisher-3] [INFO] [1781509234.299746441] [robot_state_publisher]: got segment base_footprint
[robot_state_publisher-3] [INFO] [1781509234.300151899] [robot_state_publisher]: got segment base_link
[robot_state_publisher-3] [INFO] [1781509234.300275691] [robot_state_publisher]: got segment gyro_link
[robot_state_publisher-3] [INFO] [1781509234.300343191] [robot_state_publisher]: got segment laser_link
[ekf_node-7] Both imu1_differential and imu1_relative were set to true. Using differential mode.
[static_transform_publisher-10] [INFO] [1781509234.527684902] [depth_camera_tf]: Spinning until stopped - publishing transform
[static_transform_publisher-10] translation: ('0.140000', '0.000000', '0.050000')
[static_transform_publisher-10] rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
[static_transform_publisher-10] from 'base_link' to 'depth_camera_link'
[aurora930_node-11] W0615 15:40:35.344950 63045 ros2_node.cc:35] hello aurora 900/930
[aurora930_node-11] 2026-06-15 15:40:35.483 (   0.313s) [        8C9B4020] device_manager_impl.cc:89    INFO| hotplug has registed by user
[aurora930_node-11] I0615 15:40:35.580670 63045 aurora900_ros2_device.cc:153] BOOT_ORDER_1::Found 1 deptrum device
[aurora930_node-11] I0615 15:40:35.581465 63045 aurora900_ros2_device.cc:162] BOOT_ORDER_1::No serial number provided: picking first device
[aurora930_node-11] 2026-06-15 15:40:35.581 (   0.411s) [        8C9B4020] device_manager_impl.cc:318   INFO| Device information:
[aurora930_node-11]     ir_pid:0x1930, rgb_pid:0x0
[aurora930_node-11]     serial number:HY400529001015314G00248
[aurora930_node-11] I0615 15:40:35.581707 63045 aurora900_ros2_device.cc:206] BOOT_ORDER_1::0:device start opening
[aurora930_node-11] 2026-06-15 15:40:35.583 (   0.414s) [        8C9B4020]   custom_usb_device.cc:101   INFO| bulk in endpoint addr:129
[aurora930_node-11] 2026-06-15 15:40:35.584 (   0.414s) [        8C9B4020]   custom_usb_device.cc:98    INFO| bulk out endpoint addr:2
[aurora930_node-11] 2026-06-15 15:40:35.602 (   0.432s) [        8C9B4020]deptrum_camera_aurora93:53    INFO| doe_broken:0 ito_support:1 crash_count:0 wdt_count:0 hard_reset_count:2 heart_boot_count:0 boot_total:99 last_crash_time:N
[aurora930_node-11] I0615 15:40:35.602873 63045 aurora900_ros2_device.cc:247] device supported frame_mode:
[aurora930_node-11] I0615 15:40:35.603008 63045 aurora900_ros2_device.cc:252] [0]:ir_mode:=13 kRes320x200Ir8Bit rgb_mode:=31 kRes320x200RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0615 15:40:35.603093 63045 aurora900_ros2_device.cc:252] [1]:ir_mode:=17 kRes480x300Depth16Bit rgb_mode:=32 kRes480x300RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0615 15:40:35.603142 63045 aurora900_ros2_device.cc:252] [2]:ir_mode:=20 kRes640x400Ir8Bit rgb_mode:=33 kRes640x400RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0615 15:40:35.603184 63045 aurora900_ros2_device.cc:266] current set mode ir_mode:20:kRes640x400Ir8Bit,rgb_mode:33:kRes640x400RgbYuv
[aurora930_node-11] device_count==========1
[INFO] [map_server-15]: process started with pid [63163]
[INFO] [costmap_filter_info_server-16]: process started with pid [63166]
[INFO] [lifecycle_manager-17]: process started with pid [63179]
[qr_decoder-12] [INFO] [1781509235.623786375] [qr_decoder_zbar]: QR decoder (ZBar) started: rgb=/aurora/rgb/image_raw, depth=/aurora/depth/image_raw, filter=on, range=[50, 4000]mm, min_qr_len=1, intrinsics: fx=421.3 fy=422.3 cx=320.3 cy=197.0
[costmap_filter_info_server-16] [INFO] [1781509235.814880294] [costmap_filter_info_server]: This is costmap filter info publisher
[lifecycle_manager-17] [INFO] [1781509235.913082837] [lifecycle_manager_keepout]: Creating
[costmap_filter_info_server-16] [INFO] [1781509235.945751213] [keepout_filter_info_server]:
[costmap_filter_info_server-16]         keepout_filter_info_server lifecycle node launched.
[costmap_filter_info_server-16]         Waiting on external lifecycle transitions to activate
[costmap_filter_info_server-16]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[lifecycle_manager-17] [INFO] [1781509235.953938921] [lifecycle_manager_keepout]: Creating and initializing lifecycle service clients
[map_server-15] [INFO] [1781509235.980178838] [keepout_mask_server]:
[map_server-15]         keepout_mask_server lifecycle node launched.
[map_server-15]         Waiting on external lifecycle transitions to activate
[map_server-15]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[map_server-15] [INFO] [1781509235.980893130] [keepout_mask_server]: Creating
[aurora930_node-11] I0615 15:40:36.096297 63045 aurora900_ros2_device.cc:387] Switch Auto Exposure
[lifecycle_manager-17] [INFO] [1781509236.115953965] [lifecycle_manager_keepout]: Starting managed nodes bringup...
[lifecycle_manager-17] [INFO] [1781509236.123813132] [lifecycle_manager_keepout]: Configuring keepout_mask_server
[map_server-15] [INFO] [1781509236.132899548] [keepout_mask_server]: Configuring
[map_server-15] [INFO] [1781509236.133222257] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.yaml
[map_server-15] [INFO] [1781509236.134367507] [map_io]: resolution: 0.05
[map_server-15] [INFO] [1781509236.134453840] [map_io]: origin[0]: -2.65
[map_server-15] [INFO] [1781509236.134484298] [map_io]: origin[1]: -4.5
[map_server-15] [INFO] [1781509236.134511298] [map_io]: origin[2]: 0
[map_server-15] [INFO] [1781509236.134540215] [map_io]: free_thresh: 0.5
[map_server-15] [INFO] [1781509236.134569257] [map_io]: occupied_thresh: 0.5
[map_server-15] [INFO] [1781509236.134605382] [map_io]: mode: scale
[map_server-15] [INFO] [1781509236.134635257] [map_io]: negate: 0
[map_server-15] [INFO] [1781509236.135374965] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm
[aurora930_node-11] 2026-06-15 15:40:36.149 (   0.979s) [        8C9B4020]      aurora900_impl.cc:1106  INFO| SetHeartbeat user set heartbeat enable: 0
[map_server-15] [INFO] [1781509236.175356257] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm: 163 X 141 map @ 0.05 m/cell
[lifecycle_manager-17] [INFO] [1781509236.245410966] [lifecycle_manager_keepout]: Configuring keepout_filter_info_server
[costmap_filter_info_server-16] [INFO] [1781509236.246567841] [keepout_filter_info_server]: Configuring
[lifecycle_manager-17] [INFO] [1781509236.272302425] [lifecycle_manager_keepout]: Activating keepout_mask_server
[bmi088_iio_bridge.py-5] [INFO] [1781509236.275833842] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1781509236.279132342] [bmi088_iio_bridge]:   DIAGNOSTIC: Scanning IIO devices under /sys/bus/iio/devices/
[bmi088_iio_bridge.py-5] [INFO] [1781509236.281918467] [bmi088_iio_bridge]:   Equivalent to: ls /sys/bus/iio/devices/*/name
[bmi088_iio_bridge.py-5] [INFO] [1781509236.284580009] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1781509236.287421175] [bmi088_iio_bridge]:   iio:device0/name = "34190000.adc"
[map_server-15] [INFO] [1781509236.284901217] [keepout_mask_server]: Activating
[map_server-15] [INFO] [1781509236.285247550] [keepout_mask_server]: Creating bond (keepout_mask_server) to lifecycle manager.
[bmi088_iio_bridge.py-5] [INFO] [1781509236.292394759] [bmi088_iio_bridge]:   iio:device1/name = "bmi08x"
[bmi088_iio_bridge.py-5] [INFO] [1781509236.296106759] [bmi088_iio_bridge]:   trigger0/name = "34190000.adc-dev0"
[bmi088_iio_bridge.py-5] [INFO] [1781509236.300259842] [bmi088_iio_bridge]:   Total IIO devices found: 3
[bmi088_iio_bridge.py-5] [INFO] [1781509236.305835842] [bmi088_iio_bridge]:   BMI088 kernel module APPEARS LOADED: 1 BMI device(s) detected
[bmi088_iio_bridge.py-5] [INFO] [1781509236.318631009] [bmi088_iio_bridge]:   BMI device names: ['bmi08x']
[bmi088_iio_bridge.py-5] [INFO] [1781509236.327506718] [bmi088_iio_bridge]:   gyro:  /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_anglvel is_si=False scale_override=0.00053
[bmi088_iio_bridge.py-5] [INFO] [1781509236.337902426] [bmi088_iio_bridge]:   accel: /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_accel is_si=False scale_override=0.00341
[lifecycle_manager-17] [INFO] [1781509236.413536885] [lifecycle_manager_keepout]: Server keepout_mask_server connected with bond.
[lifecycle_manager-17] [INFO] [1781509236.413720219] [lifecycle_manager_keepout]: Activating keepout_filter_info_server
[costmap_filter_info_server-16] [INFO] [1781509236.414698677] [keepout_filter_info_server]: Activating
[costmap_filter_info_server-16] [INFO] [1781509236.414925677] [keepout_filter_info_server]: Creating bond (keepout_filter_info_server) to lifecycle manager.
[imu_madgwick_filter.py-6] [INFO] [1781509236.452022427] [imu_madgwick_bmi088]: [imu_madgwick] init: beta=0.0030, gyro_noise=0.0002, accel_noise=0.010
[bmi088_iio_bridge.py-5] [INFO] [1781509236.502052761] [bmi088_iio_bridge]: BMI088 IIO Bridge 启动 @ 100Hz -> /imu_data  [OK]
[lifecycle_manager-17] [INFO] [1781509236.524726053] [lifecycle_manager_keepout]: Server keepout_filter_info_server connected with bond.
[lifecycle_manager-17] [INFO] [1781509236.524902428] [lifecycle_manager_keepout]: Managed nodes are active
[lifecycle_manager-17] [INFO] [1781509236.524999095] [lifecycle_manager_keepout]: Creating bond timer...
[imu_madgwick_filter.py-6] [INFO] [1781509236.530979595] [imu_madgwick_bmi088]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-6] [INFO] [1781509236.533536887] [imu_madgwick_bmi088]: [imu_madgwick] accel init: roll=-2.4deg, pitch=-3.6deg
[velocity_pid.py-9] [INFO] [1781509236.538952720] [velocity_pid]: VelocityPID 就绪: vx(Kp=0.8, Ki=0.60, Kd=0.05, max_i=0.68) wz(Kp=1.0, Ki=0.40, Kd=0.02, max_i=2.24) | feedback_timeout=0.5s
[imu_madgwick_filter.py-4] [INFO] [1781509236.544178179] [imu_madgwick_filter]: [imu_madgwick] init: beta=0.0330, gyro_noise=0.0010, accel_noise=0.050
[imu_madgwick_filter.py-4] [INFO] [1781509236.549711512] [imu_madgwick_filter]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-4] [INFO] [1781509236.552346887] [imu_madgwick_filter]: [imu_madgwick] accel init: roll=0.0deg, pitch=0.2deg
[aurora930_node-11] I0615 15:40:36.561030 63045 aurora900_ros2_device.cc:304] BOOT_ORDER_1::Device information:
[aurora930_node-11] I0615 15:40:36.561210 63045 aurora900_ros2_device.cc:305]    sdk version: 1.1.22
[aurora930_node-11] I0615 15:40:36.561249 63045 aurora900_ros2_device.cc:306]    device name: Aurora 930
[aurora930_node-11] I0615 15:40:36.561283 63045 aurora900_ros2_device.cc:307]    serial number: HY400529001015314G00248
[aurora930_node-11] I0615 15:40:36.561311 63045 aurora900_ros2_device.cc:308]    firmware version: 1.7.2
[aurora930_node-11] I0615 15:40:36.561378 63045 camera_parameters.cc:134] BOOT_ORDER_1::Camera Parameters:
[aurora930_node-11] I0615 15:40:36.561409 63045 camera_parameters.cc:135] BOOT_ORDER_1::         Ir Intrinsics:
[aurora930_node-11] I0615 15:40:36.561435 63045 camera_parameters.cc:146]                Resolution:
[aurora930_node-11] I0615 15:40:36.561486 63045 camera_parameters.cc:147]                        Rows:400
[aurora930_node-11] I0615 15:40:36.561522 63045 camera_parameters.cc:148]                        Cols:640
[aurora930_node-11] I0615 15:40:36.561547 63045 camera_parameters.cc:149]                Intrinsics:
[aurora930_node-11] I0615 15:40:36.561573 63045 camera_parameters.cc:150]                        fx: 421.307
[aurora930_node-11] I0615 15:40:36.561679 63045 camera_parameters.cc:151]                        fy: 422.254
[aurora930_node-11] I0615 15:40:36.561713 63045 camera_parameters.cc:152]                        cx: 320.27
[aurora930_node-11] I0615 15:40:36.561744 63045 camera_parameters.cc:153]                        cy: 197.01
[aurora930_node-11] I0615 15:40:36.561776 63045 camera_parameters.cc:154]                        k1: 0.0606853
[aurora930_node-11] I0615 15:40:36.561808 63045 camera_parameters.cc:155]                        k2: -0.10961
[aurora930_node-11] I0615 15:40:36.561839 63045 camera_parameters.cc:156]                        p1: 0.00126689
[aurora930_node-11] I0615 15:40:36.561870 63045 camera_parameters.cc:157]                        p2: -0.00120539
[aurora930_node-11] I0615 15:40:36.561908 63045 camera_parameters.cc:158]                        k3: 0.0522281
[aurora930_node-11] I0615 15:40:36.561939 63045 camera_parameters.cc:138] BOOT_ORDER_1::         Rgb Intrinsics:
[aurora930_node-11] I0615 15:40:36.561970 63045 camera_parameters.cc:146]                Resolution:
[aurora930_node-11] I0615 15:40:36.561996 63045 camera_parameters.cc:147]                        Rows:400
[aurora930_node-11] I0615 15:40:36.562021 63045 camera_parameters.cc:148]                        Cols:640
[aurora930_node-11] I0615 15:40:36.562050 63045 camera_parameters.cc:149]                Intrinsics:
[aurora930_node-11] I0615 15:40:36.562076 63045 camera_parameters.cc:150]                        fx: 416.49
[aurora930_node-11] I0615 15:40:36.562108 63045 camera_parameters.cc:151]                        fy: 417.383
[aurora930_node-11] I0615 15:40:36.562144 63045 camera_parameters.cc:152]                        cx: 316.832
[aurora930_node-11] I0615 15:40:36.562176 63045 camera_parameters.cc:153]                        cy: 188.753
[aurora930_node-11] I0615 15:40:36.562207 63045 camera_parameters.cc:154]                        k1: 0.00611878
[aurora930_node-11] I0615 15:40:36.562244 63045 camera_parameters.cc:155]                        k2: -0.0490436
[aurora930_node-11] I0615 15:40:36.562276 63045 camera_parameters.cc:156]                        p1: 0.000399548
[aurora930_node-11] I0615 15:40:36.562327 63045 camera_parameters.cc:157]                        p2: 0.000563892
[aurora930_node-11] I0615 15:40:36.562361 63045 camera_parameters.cc:158]                        k3: 0.0308458
[aurora930_node-11] I0615 15:40:36.562391 63045 camera_parameters.cc:141] BOOT_ORDER_1::         Ir to Rgb Extrinsic:
[aurora930_node-11] I0615 15:40:36.562418 63045 camera_parameters.cc:162]                Extrinsics:
[aurora930_node-11] I0615 15:40:36.562443 63045 camera_parameters.cc:163]                        Rotation[0]: 0.999973, 0.00724076, -0.00112023
[aurora930_node-11] I0615 15:40:36.562479 63045 camera_parameters.cc:165]                        Rotation[1]: -0.00724006, 0.999973, 0.000633162
[aurora930_node-11] I0615 15:40:36.562515 63045 camera_parameters.cc:167]                        Rotation[2]: 0.00112478, -0.000625033, 0.999999
[aurora930_node-11] I0615 15:40:36.562601 63045 camera_parameters.cc:169]                        Translation: -9.88662, 0.117748, 0.603513
[aurora930_node-11] 2026-06-15 15:40:36.563 (   1.393s) [        8C9B4020]      aurora900_impl.cc:578   INFO| stream_mask_:0, rgb_stream_count_:1
[cmd_vel_mux.py-8] [INFO] [1781509236.567755387] [cmd_vel_mux]:   nav: /nav_cmd_vel priority=10 timeout=0.5s
[cmd_vel_mux.py-8] [INFO] [1781509236.582634679] [cmd_vel_mux]:   pid: /pid_cmd_vel priority=20 timeout=0.3s
[cmd_vel_mux.py-8] [INFO] [1781509236.595802679] [cmd_vel_mux]:   stop: /stop_cmd_vel priority=255 timeout=0.5s
[cmd_vel_mux.py-8] [INFO] [1781509236.609916763] [cmd_vel_mux]: cmd_vel_mux 就绪: 输出 → /cmd_vel_muxed
[cmd_vel_mux.py-8] [INFO] [1781509236.645759722] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[velocity_pid.py-9] [INFO] [1781509236.646573305] [velocity_pid]: [vel_pid] ACTIVATED vx=0.00 wz=0.00
[aurora930_node-11] 2026-06-15 15:40:36.854 (   1.684s) [        6D1D37E0]deptrum_camera_aurora93:407    ERR| recv first frame time is 1781509236854
[qr_decision-13] [INFO] [1781509236.903731850] [qr_decision]: qr_decision started: cooldown=3.0s, awaiting /sign from qr_decoder
[lslidar_driver_node-2] port = /dev/ttyACM1, baud_rate = 230400
[lslidar_driver_node-2] open_port /dev/ttyACM1 OK !
[INFO] [component_container_isolated-18]: process started with pid [63341]
[vision_ai_node-14] [INFO] [1781509240.437508313] [vision_ai_node]: 成功加载配置文件: /userdata/dev_ws/install/racing_vision_ai/share/racing_vision_ai/config/vision_ai_config.yaml
[vision_ai_node-14] [INFO] [1781509240.814420360] [vision_ai_node]: Volcengine Ark client initialized successfully
[vision_ai_node-14] [INFO] [1781509240.833177193] [vision_ai_node]: Vision AI Node initialized
[vision_ai_node-14] [INFO] [1781509240.835839527] [vision_ai_node]: Waiting for sign4return=100 signal...
[vision_ai_node-14] [INFO] [1781509240.838104860] [vision_ai_node]: Results will be published to vlm_result
[bmi088_iio_bridge.py-5] [INFO] [1781509242.051003917] [bmi088_iio_bridge]:   gyro bias calibrated: (0.002994, 0.001076, -0.002920) rad/s
[INFO] [competition_master_stage3.py-19]: process started with pid [63343]
[INFO] [rviz2-20]: process started with pid [63345]
[component_container_isolated-18] [INFO] [1781509242.805460261] [nav2_container]: Load Library: /opt/ros/humble/lib/libmap_server_core.so
[component_container_isolated-18] [INFO] [1781509242.867711261] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::CostmapFilterInfoServer>
[component_container_isolated-18] [INFO] [1781509242.867892720] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapSaver>
[component_container_isolated-18] [INFO] [1781509242.867943470] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-18] [INFO] [1781509242.867990011] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-18] [INFO] [1781509242.936725804] [map_server]:
[component_container_isolated-18]       map_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781509242.936999887] [map_server]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/map_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781509242.942227012] [nav2_container]: Load Library: /opt/ros/humble/lib/libcontroller_server_core.so
[component_container_isolated-18] [INFO] [1781509242.962775846] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-18] [INFO] [1781509242.963006221] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-18] [INFO] [1781509243.051285722] [controller_server]:
[component_container_isolated-18]       controller_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781509243.076482222] [controller_server]: Creating controller server
[component_container_isolated-18] [INFO] [1781509243.175888724] [local_costmap.local_costmap]:
[component_container_isolated-18]       local_costmap lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781509243.178460765] [local_costmap.local_costmap]: Creating Costmap
[component_container_isolated-18] [INFO] [1781509243.213601391] [nav2_container]: Load Library: /opt/ros/humble/lib/libamcl_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/controller_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781509243.222946558] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-18] [INFO] [1781509243.223103099] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-18] [INFO] [1781509243.292044559] [amcl]:
[component_container_isolated-18]       amcl lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781509243.297476309] [amcl]: Creating
[component_container_isolated-18] [INFO] [1781509243.352692018] [nav2_container]: Load Library: /opt/ros/humble/lib/libsmoother_server_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/amcl' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781509243.361159184] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-18] [INFO] [1781509243.361402310] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-18] [INFO] [1781509243.431041560] [smoother_server]:
[component_container_isolated-18]       smoother_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781509243.440103894] [smoother_server]: Creating smoother server
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/smoother_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781509243.452213394] [nav2_container]: Load Library: /opt/ros/humble/lib/libnav2_lifecycle_manager_core.so
[component_container_isolated-18] [INFO] [1781509243.455994019] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781509243.456150811] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781509243.535464020] [lifecycle_manager_localization]: Creating
[component_container_isolated-18] [INFO] [1781509243.561125104] [nav2_container]: Load Library: /opt/ros/humble/lib/libplanner_server_core.so
[component_container_isolated-18] [INFO] [1781509243.561785145] [lifecycle_manager_localization]: Creating and initializing lifecycle service clients
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_localization' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781509243.566804729] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-18] [INFO] [1781509243.567247479] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-18] [INFO] [1781509243.606278938] [lifecycle_manager_localization]: Starting managed nodes bringup...
[component_container_isolated-18] [INFO] [1781509243.606524979] [lifecycle_manager_localization]: Configuring map_server
[component_container_isolated-18] [INFO] [1781509243.607592563] [map_server]: Configuring
[component_container_isolated-18] [INFO] [1781509243.607988896] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.yaml
[component_container_isolated-18] [INFO] [1781509243.609262521] [map_io]: resolution: 0.05
[component_container_isolated-18] [INFO] [1781509243.609386063] [map_io]: origin[0]: -2.65
[component_container_isolated-18] [INFO] [1781509243.609437854] [map_io]: origin[1]: -4.5
[component_container_isolated-18] [INFO] [1781509243.609473729] [map_io]: origin[2]: 0
[component_container_isolated-18] [INFO] [1781509243.610557979] [map_io]: free_thresh: 0.25
[component_container_isolated-18] [INFO] [1781509243.610651229] [map_io]: occupied_thresh: 0.65
[component_container_isolated-18] [INFO] [1781509243.610762104] [map_io]: mode: trinary
[component_container_isolated-18] [INFO] [1781509243.610811271] [map_io]: negate: 0
[component_container_isolated-18] [INFO] [1781509243.614295438] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm
[component_container_isolated-18] [INFO] [1781509243.663081980] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm: 163 X 141 map @ 0.05 m/cell
[component_container_isolated-18] [INFO] [1781509243.664699397] [planner_server]:
[component_container_isolated-18]       planner_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781509243.686177105] [planner_server]: Creating
[component_container_isolated-18] [INFO] [1781509243.693232105] [lifecycle_manager_localization]: Configuring amcl
[component_container_isolated-18] [INFO] [1781509243.699951606] [amcl]: Configuring
[component_container_isolated-18] [INFO] [1781509243.700463064] [amcl]: initTransforms
[component_container_isolated-18] [INFO] [1781509243.760678065] [amcl]: initPubSub
[component_container_isolated-18] [INFO] [1781509243.791977607] [amcl]: Subscribed to map topic.
[component_container_isolated-18] [INFO] [1781509243.823067982] [global_costmap.global_costmap]:
[component_container_isolated-18]       global_costmap lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781509243.825967482] [global_costmap.global_costmap]: Creating Costmap
[component_container_isolated-18] [INFO] [1781509243.828115941] [lifecycle_manager_localization]: Activating map_server
[component_container_isolated-18] [INFO] [1781509243.832443524] [map_server]: Activating
[component_container_isolated-18] [INFO] [1781509243.832917274] [map_server]: Creating bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509243.833102232] [amcl]: Received a 163 X 141 map @ 0.050 m/pix
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/planner_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781509243.875838900] [nav2_container]: Load Library: /opt/ros/humble/lib/libbehavior_server_core.so
[component_container_isolated-18] [INFO] [1781509243.900211608] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-18] [INFO] [1781509243.900453942] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-18] [INFO] [1781509243.961654359] [lifecycle_manager_localization]: Server map_server connected with bond.
[component_container_isolated-18] [INFO] [1781509243.961889817] [lifecycle_manager_localization]: Activating amcl
[component_container_isolated-18] [INFO] [1781509243.962929401] [amcl]: Activating
[component_container_isolated-18] [INFO] [1781509243.963163484] [amcl]: initialPoseReceived
[component_container_isolated-18] [INFO] [1781509243.963694276] [amcl]: Setting pose (1781509243.963688): -1.985 -0.014 0.262
[component_container_isolated-18] [INFO] [1781509243.965605692] [amcl]: Creating bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509243.974951193] [behavior_server]:
[component_container_isolated-18]       behavior_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/behavior_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781509244.018034026] [nav2_container]: Load Library: /opt/ros/humble/lib/libbt_navigator_core.so
[component_container_isolated-18] [INFO] [1781509244.027443193] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-18] [INFO] [1781509244.027617985] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-18] [INFO] [1781509244.085331819] [lifecycle_manager_localization]: Server amcl connected with bond.
[component_container_isolated-18] [INFO] [1781509244.085551694] [lifecycle_manager_localization]: Managed nodes are active
[component_container_isolated-18] [INFO] [1781509244.085827569] [lifecycle_manager_localization]: Creating bond timer...
[component_container_isolated-18] [INFO] [1781509244.089360986] [amcl]: createLaserObject
[component_container_isolated-18] [INFO] [1781509244.140887486] [bt_navigator]:
[component_container_isolated-18]       bt_navigator lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/bt_navigator' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781509244.142258570] [bt_navigator]: Creating
[component_container_isolated-18] [INFO] [1781509244.160349820] [nav2_container]: Load Library: /opt/ros/humble/lib/libwaypoint_follower_core.so
[component_container_isolated-18] [INFO] [1781509244.165095945] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-18] [INFO] [1781509244.165283945] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-18] [INFO] [1781509244.255641113] [waypoint_follower]:
[component_container_isolated-18]       waypoint_follower lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781509244.258502571] [waypoint_follower]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/waypoint_follower' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781509244.277585321] [nav2_container]: Load Library: /opt/ros/humble/lib/libvelocity_smoother_core.so
[component_container_isolated-18] [INFO] [1781509244.281253197] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-18] [INFO] [1781509244.281405363] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-18] [INFO] [1781509244.368275239] [velocity_smoother]:
[component_container_isolated-18]       velocity_smoother lifecycle node launched.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/velocity_smoother' in container '/nav2_container'
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781509244.381767656] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781509244.381991573] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781509244.454585157] [lifecycle_manager_navigation]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_navigation' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781509244.478040866] [lifecycle_manager_navigation]: Creating and initializing lifecycle service clients
[component_container_isolated-18] [INFO] [1781509244.578528075] [lifecycle_manager_navigation]: Starting managed nodes bringup...
[component_container_isolated-18] [INFO] [1781509244.578955117] [lifecycle_manager_navigation]: Configuring controller_server
[component_container_isolated-18] [INFO] [1781509244.582365575] [controller_server]: Configuring controller interface
[component_container_isolated-18] [INFO] [1781509244.583657867] [controller_server]: getting goal checker plugins..
[component_container_isolated-18] [INFO] [1781509244.586088034] [controller_server]: Controller frequency set to 10.0000Hz
[component_container_isolated-18] [INFO] [1781509244.586505659] [local_costmap.local_costmap]: Configuring
[component_container_isolated-18] [INFO] [1781509244.619310993] [local_costmap.local_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781509244.649241243] [local_costmap.local_costmap]: Subscribed to Topics: scan aurora_points
[component_container_isolated-18] [INFO] [1781509244.752597953] [local_costmap.local_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781509244.752950036] [local_costmap.local_costmap]: Using plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781509244.778655953] [local_costmap.local_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781509244.779412703] [local_costmap.local_costmap]: Using plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781509244.793222412] [local_costmap.local_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781509244.855520454] [controller_server]: Created progress_checker : progress_checker of type nav2_controller::SimpleProgressChecker
[component_container_isolated-18] [INFO] [1781509244.863209704] [controller_server]: Created goal checker : goal_checker of type nav2_controller::SimpleGoalChecker
[component_container_isolated-18] [INFO] [1781509244.870618079] [controller_server]: Controller Server has goal_checker  goal checkers available.
[component_container_isolated-18] [INFO] [1781509244.874533954] [controller_server]: Created controller : FollowPath of type nav2_regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781509244.950837580] [controller_server]: Controller Server has FollowPath  controllers available.
[component_container_isolated-18] [INFO] [1781509245.002210498] [lifecycle_manager_navigation]: Configuring smoother_server
[component_container_isolated-18] [INFO] [1781509245.003026289] [smoother_server]: Configuring smoother server
[component_container_isolated-18] [INFO] [1781509245.089759124] [smoother_server]: Created smoother : SmoothPath of type nav2_constrained_smoother/ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781509245.156133666] [smoother_server]: Smoother Server has SmoothPath  smoothers available.
[component_container_isolated-18] [INFO] [1781509245.204490709] [lifecycle_manager_navigation]: Configuring planner_server
[component_container_isolated-18] [INFO] [1781509245.205353709] [planner_server]: Configuring
[component_container_isolated-18] [INFO] [1781509245.205642959] [global_costmap.global_costmap]: Configuring
[component_container_isolated-18] [INFO] [1781509245.256404834] [global_costmap.global_costmap]: Using plugin "static_layer"
[component_container_isolated-18] [INFO] [1781509245.287518168] [global_costmap.global_costmap]: Subscribing to the map topic (/map) with transient local durability
[component_container_isolated-18] [INFO] [1781509245.295719335] [global_costmap.global_costmap]: Initialized plugin "static_layer"
[component_container_isolated-18] [INFO] [1781509245.295925960] [global_costmap.global_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781509245.324223168] [global_costmap.global_costmap]: Subscribed to Topics: scan aurora_points
[component_container_isolated-18] [INFO] [1781509245.449608503] [global_costmap.global_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781509245.452476587] [global_costmap.global_costmap]: Using plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781509245.466049879] [global_costmap.global_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781509245.466261004] [global_costmap.global_costmap]: Using plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781509245.481471462] [global_costmap.global_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781509245.537255255] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 163 X 141 at 0.050000 m/pix
[competition_master_stage3.py-19] [INFO] [1781509245.560094672] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1781509245.563837088] [competition_master_stage3]: === [Stage 3] 总控节点初始化 ===
[competition_master_stage3.py-19] [INFO] [1781509245.566360213] [competition_master_stage3]:   QR点:    (0.41, -3.17, yaw=0.00)
[component_container_isolated-18] [INFO] [1781509245.567185255] [planner_server]: Created global planner plugin GridBased of type nav2_smac_planner/SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781509245.567424547] [planner_server]: Configuring GridBased of type SmacPlannerHybrid
[competition_master_stage3.py-19] [INFO] [1781509245.569613422] [competition_master_stage3]:   通道入口: (0.38, -1.10, yaw=0.00)
[competition_master_stage3.py-19] [INFO] [1781509245.572918630] [competition_master_stage3]:   P点:     (-1.99, -0.01, yaw=0.26)
[competition_master_stage3.py-19] [INFO] [1781509245.576164755] [competition_master_stage3]:   cruise_cw: 3 路点 → VLM=(3.12, -1.34)
[competition_master_stage3.py-19] [INFO] [1781509245.579883047] [competition_master_stage3]:   cruise_ccw: 3 路点 → VLM=(2.10, 0.92)
[competition_master_stage3.py-19] [INFO] [1781509245.583213047] [competition_master_stage3]:   超时: total=180.0s QR=90.0s entry=60.0s cruise=180.0s vlm=30.0s return=120.0s
[competition_master_stage3.py-19] [INFO] [1781509245.586202089] [competition_master_stage3]:   回退QR方向: 逆时针
[competition_master_stage3.py-19] [INFO] [1781509245.589446505] [competition_master_stage3]:   VLM结果话题: vlm_result
[competition_master_stage3.py-19] [INFO] [1781509245.593722130] [competition_master_stage3]: ============================================================
[component_container_isolated-18] [INFO] [1781509245.622712547] [planner_server]: Even sized heuristic lookup table size set 200.000000, increasing size by 1 to make odd
[imu_madgwick_filter.py-6] [INFO] [1781509246.217359638] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=437 q_w=0.9993 angle=4.2deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1781509246.412525599] [imu_madgwick_filter]: [imu_madgwick ->] msgs=200 q_w=0.9996 angle=3.3deg beta=0.0330
[qr_decoder-12] [INFO] [1781509252.342888718] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=200 last_qr_frame=-1 gap=-1 frames rejects=0
[imu_madgwick_filter.py-6] [INFO] [1781509256.217532518] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1051 q_w=0.9993 angle=4.2deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1781509256.413097313] [imu_madgwick_filter]: [imu_madgwick ->] msgs=400 q_w=0.9984 angle=6.6deg beta=0.0330
[component_container_isolated-18] [INFO] [1781509259.130912098] [planner_server]: Configured plugin GridBased of type SmacPlannerHybrid with maximum iterations 1500, max on approach iterations 300, and not allowing unknown traversal. Tolerance 0.50.Using motion model: Reeds-Shepp.
[component_container_isolated-18] [INFO] [1781509259.131173515] [planner_server]: Planner Server has GridBased  planners available.
[component_container_isolated-18] [INFO] [1781509259.178882057] [lifecycle_manager_navigation]: Configuring behavior_server
[component_container_isolated-18] [INFO] [1781509259.179870265] [behavior_server]: Configuring
[component_container_isolated-18] [INFO] [1781509259.211088849] [behavior_server]: Creating behavior plugin spin of type nav2_behaviors/Spin
[component_container_isolated-18] [INFO] [1781509259.215231474] [behavior_server]: Configuring spin
[component_container_isolated-18] [INFO] [1781509259.256711266] [behavior_server]: Creating behavior plugin backup of type nav2_behaviors/BackUp
[component_container_isolated-18] [INFO] [1781509259.262630433] [behavior_server]: Configuring backup
[component_container_isolated-18] [INFO] [1781509259.298158392] [behavior_server]: Creating behavior plugin drive_on_heading of type nav2_behaviors/DriveOnHeading
[component_container_isolated-18] [INFO] [1781509259.302231392] [behavior_server]: Configuring drive_on_heading
[component_container_isolated-18] [INFO] [1781509259.338717184] [behavior_server]: Creating behavior plugin wait of type nav2_behaviors/Wait
[component_container_isolated-18] [INFO] [1781509259.342299767] [behavior_server]: Configuring wait
[component_container_isolated-18] [INFO] [1781509259.369671684] [lifecycle_manager_navigation]: Configuring bt_navigator
[component_container_isolated-18] [INFO] [1781509259.370662976] [bt_navigator]: Configuring
[rviz2-20] [INFO] [1781509259.607496896] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-20] [INFO] [1781509259.608744604] [rviz2]: OpenGl version: 4.5 (GLSL 4.5)
[competition_master_stage3.py-19] [INFO] [1781509259.791301356] [competition_master_stage3]: [LAUNCH] 发车阶段: 14.4s
[competition_master_stage3.py-19] [INFO] [1781509259.800148232] [competition_master_stage3]: >>> 系统就绪, 开始 Stage 3 导航
[competition_master_stage3.py-19] [INFO] [1781509259.809987773] [competition_master_stage3]: [状态机] INIT → NAV_TO_QR
[competition_master_stage3.py-19] [INFO] [1781509259.819898398] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-18] [INFO] [1781509259.837772065] [lifecycle_manager_navigation]: Configuring waypoint_follower
[component_container_isolated-18] [INFO] [1781509259.838781274] [waypoint_follower]: Configuring
[competition_master_stage3.py-19] [WARN] [1781509259.858677357] [competition_master_stage3]: 导航目标被拒绝, 3s 后重试...
[component_container_isolated-18] [INFO] [1781509259.925695316] [waypoint_follower]: Created waypoint_task_executor : wait_at_waypoint of type nav2_waypoint_follower::WaitAtWaypoint
[component_container_isolated-18] [INFO] [1781509259.933418108] [lifecycle_manager_navigation]: Configuring velocity_smoother
[component_container_isolated-18] [INFO] [1781509259.934438733] [velocity_smoother]: Configuring velocity smoother
[component_container_isolated-18] [INFO] [1781509259.967894400] [lifecycle_manager_navigation]: Activating controller_server
[component_container_isolated-18] [INFO] [1781509259.968702775] [controller_server]: Activating
[component_container_isolated-18] [INFO] [1781509259.968952942] [local_costmap.local_costmap]: Activating
[component_container_isolated-18] [INFO] [1781509259.969048359] [local_costmap.local_costmap]: Checking transform
[component_container_isolated-18] [INFO] [1781509259.969449400] [local_costmap.local_costmap]: start
[component_container_isolated-18] [INFO] [1781509259.984703817] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781509259.993752276] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781509259.993946609] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781509260.000232776] [local_costmap.local_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[component_container_isolated-18] [INFO] [1781509260.343723780] [controller_server]: Activating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781509260.344043405] [controller_server]: Creating bond (controller_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509260.454885365] [lifecycle_manager_navigation]: Server controller_server connected with bond.
[component_container_isolated-18] [INFO] [1781509260.455108823] [lifecycle_manager_navigation]: Activating smoother_server
[component_container_isolated-18] [INFO] [1781509260.456554907] [smoother_server]: Activating
[component_container_isolated-18] [INFO] [1781509260.457431615] [smoother_server]: Activating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781509260.457596740] [smoother_server]: Creating bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509260.572793825] [lifecycle_manager_navigation]: Server smoother_server connected with bond.
[component_container_isolated-18] [INFO] [1781509260.572968283] [lifecycle_manager_navigation]: Activating planner_server
[component_container_isolated-18] [INFO] [1781509260.573976200] [planner_server]: Activating
[component_container_isolated-18] [INFO] [1781509260.574272992] [global_costmap.global_costmap]: Activating
[component_container_isolated-18] [INFO] [1781509260.574354700] [global_costmap.global_costmap]: Checking transform
[component_container_isolated-18] [INFO] [1781509260.574663242] [global_costmap.global_costmap]: start
[component_container_isolated-18] [INFO] [1781509260.585274325] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781509260.593954450] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781509260.594145825] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781509260.600493992] [global_costmap.global_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[rviz2-20] [INFO] [1781509261.519419379] [rviz2]: Stereo is NOT SUPPORTED
[component_container_isolated-18] [INFO] [1781509261.745707965] [planner_server]: Activating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781509261.753411423] [planner_server]: Creating bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509261.883869758] [lifecycle_manager_navigation]: Server planner_server connected with bond.
[component_container_isolated-18] [INFO] [1781509261.884061800] [lifecycle_manager_navigation]: Activating behavior_server
[component_container_isolated-18] [INFO] [1781509261.885724925] [behavior_server]: Activating
[component_container_isolated-18] [INFO] [1781509261.885922134] [behavior_server]: Activating spin
[component_container_isolated-18] [INFO] [1781509261.886179217] [behavior_server]: Activating backup
[component_container_isolated-18] [INFO] [1781509261.886486467] [behavior_server]: Activating drive_on_heading
[component_container_isolated-18] [INFO] [1781509261.886591675] [behavior_server]: Activating wait
[component_container_isolated-18] [INFO] [1781509261.886768009] [behavior_server]: Creating bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509261.998328135] [lifecycle_manager_navigation]: Server behavior_server connected with bond.
[component_container_isolated-18] [INFO] [1781509261.998517343] [lifecycle_manager_navigation]: Activating bt_navigator
[component_container_isolated-18] [INFO] [1781509261.999740093] [bt_navigator]: Activating
[component_container_isolated-18] [WARN] [1781509262.115178428] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781509262.207266346] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781509262.287519097] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781509262.499199683] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781509262.803872020] [bt_navigator_navigate_to_pose_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[competition_master_stage3.py-19] [INFO] [1781509262.868379980] [competition_master_stage3]: 重试发送导航目标 (QR点)...
[competition_master_stage3.py-19] [INFO] [1781509262.875329730] [competition_master_stage3]: [DIAG] nav目标距离: 3.97m, robot=(-2.01,-0.02) → target=(0.41,-3.17)
[competition_master_stage3.py-19] [INFO] [1781509262.886350938] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-18] [INFO] [1781509263.064503899] [bt_navigator]: Creating bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509263.138613983] [bt_navigator]: Begin navigating from current location (-2.01, -0.02) to (0.41, -3.17)
[competition_master_stage3.py-19] [INFO] [1781509263.139084150] [competition_master_stage3]: 导航目标已接受，车辆出发...
[component_container_isolated-18] [INFO] [1781509263.224339192] [lifecycle_manager_navigation]: Server bt_navigator connected with bond.
[component_container_isolated-18] [INFO] [1781509263.224520442] [lifecycle_manager_navigation]: Activating waypoint_follower
[component_container_isolated-18] [INFO] [1781509263.226293859] [waypoint_follower]: Activating
[component_container_isolated-18] [INFO] [1781509263.227090068] [waypoint_follower]: Creating bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509263.337682152] [lifecycle_manager_navigation]: Server waypoint_follower connected with bond.
[component_container_isolated-18] [INFO] [1781509263.337888611] [lifecycle_manager_navigation]: Activating velocity_smoother
[component_container_isolated-18] [INFO] [1781509263.339224402] [velocity_smoother]: Activating
[component_container_isolated-18] [INFO] [1781509263.339583361] [velocity_smoother]: Creating bond (velocity_smoother) to lifecycle manager.
[competition_master_stage3.py-19] [INFO] [1781509263.446807737] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.01,-0.02) yaw=14deg cmd=(vx=0.00 wz=0.00) elapsed=3.6s cpuFreq=1500MHz cpuT=70C cpu=100% mem=19%
[component_container_isolated-18] [INFO] [1781509263.473672237] [lifecycle_manager_navigation]: Server velocity_smoother connected with bond.
[component_container_isolated-18] [INFO] [1781509263.473848737] [lifecycle_manager_navigation]: Managed nodes are active
[component_container_isolated-18] [INFO] [1781509263.473916196] [lifecycle_manager_navigation]: Creating bond timer...
[component_container_isolated-18] [WARN] [1781509263.847475117] [planner_server]: GridBased: failed to create plan, no valid path found.
[component_container_isolated-18] [WARN] [1781509263.847772784] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.41, -3.17)
[component_container_isolated-18] [WARN] [1781509263.847887784] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1781509264.039947370] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781509264.057142120] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781509264.070479245] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781509264.070639162] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781509264.088180662] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781509265.012724132] [planner_server]: GridBased: failed to create plan, no valid path found.
[component_container_isolated-18] [WARN] [1781509265.013023591] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.41, -3.17)
[component_container_isolated-18] [WARN] [1781509265.013135091] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1781509265.139880134] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1781509265.367342928] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781509265.375030887] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781509265.381034470] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781509265.381185012] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781509265.388636137] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [WARN] [1781509265.402508846] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1781509265.413037471] [behavior_server]: Running backup
[component_container_isolated-18] [INFO] [1781509265.413074429] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781509265.414668346] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781509265.414524637] [behavior_server]: DriveOnHeading: no acceleration or deceleration limits set
[component_container_isolated-18] [WARN] [1781509265.425429346] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1781509265.429099763] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1781509265.429430429] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1781509265.429941179] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-19] [INFO] [1781509265.442769846] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.01,-0.02) yaw=14deg cmd=(vx=0.00 wz=0.00) elapsed=5.6s cpuFreq=1500MHz cpuT=71C cpu=67% mem=19%
[cmd_vel_mux.py-8] [INFO] [1781509265.448083680] [cmd_vel_mux]: [mux→] src=nav vx=0.00 wz=0.00
[component_container_isolated-18] [INFO] [1781509265.648198057] [behavior_server]: Running wait
[cmd_vel_mux.py-8] [INFO] [1781509265.943561561] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.52s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1781509265.947965353] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[imu_madgwick_filter.py-6] [INFO] [1781509266.218978856] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1523 q_w=0.9993 angle=4.2deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1781509266.413681650] [imu_madgwick_filter]: [imu_madgwick ->] msgs=600 q_w=0.9963 angle=9.9deg beta=0.0330
[competition_master_stage3.py-19] [INFO] [1781509267.431520955] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.01,-0.02) yaw=14deg cmd=(vx=0.00 wz=0.00) elapsed=7.6s cpuFreq=1500MHz cpuT=71C cpu=100% mem=19%
[qr_decoder-12] [INFO] [1781509268.349907550] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=400 last_qr_frame=-1 gap=-1 frames rejects=0
[component_container_isolated-18] [INFO] [1781509268.649026096] [behavior_server]: wait completed successfully
[competition_master_stage3.py-19] [INFO] [1781509269.423834647] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.01,-0.02) yaw=14deg cmd=(vx=0.00 wz=0.00) elapsed=9.6s cpuFreq=1500MHz cpuT=71C cpu=62% mem=20%
[component_container_isolated-18] [WARN] [1781509269.602489400] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.5342 Hz
[component_container_isolated-18] [INFO] [1781509269.740687027] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-18] [WARN] [1781509269.741031943] [controller_server]: No goal checker was specified in parameter 'current_goal_checker'. Server will use only plugin loaded goal_checker . This warning will appear once.
[cmd_vel_mux.py-8] [INFO] [1781509269.810667402] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=-0.12
[velocity_pid.py-9] [INFO] [1781509269.829428486] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.17 err=100.0%
[competition_master_stage3.py-19] [INFO] [1781509271.424503965] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.63,-0.10) yaw=-32deg cmd=(vx=0.50 wz=-0.36) elapsed=11.6s plan[31pts 4.2m] (-2.00,-0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=70C cpu=38% mem=19%
[component_container_isolated-18] [WARN] [1781509271.588586217] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3482 Hz
[component_container_isolated-18] [INFO] [1781509271.741413427] [controller_server]: Passing new path to controller.
[component_container_isolated-18] Reallocing temp weights 301 - 60
[rviz2-20] [INFO] [1781509272.623559105] [rviz2]: Message Filter dropping message: frame 'odom' at time 1781509263.502 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[velocity_pid.py-9] [INFO] [1781509272.929888734] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.52 corrected=-0.07 err=26.1%
[cmd_vel_mux.py-8] [INFO] [1781509272.978220360] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.06
[velocity_pid.py-9] [INFO] [1781509273.201023571] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0355s, resetting
[competition_master_stage3.py-19] [INFO] [1781509273.421452157] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.02,-0.73) yaw=-43deg cmd=(vx=-0.26 wz=-0.10) elapsed=13.6s plan[26pts 3.7m] (-1.50,-0.15)→(0.40,-3.15) cpuFreq=1500MHz cpuT=70C cpu=29% mem=19%
[rviz2-20] [INFO] [1781509273.469528866] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[rviz2-20] [INFO] [1781509273.472664908] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[component_container_isolated-18] [WARN] [1781509273.584814576] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3466 Hz
[component_container_isolated-18] [INFO] [1781509273.741458120] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781509273.877719371] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.29
[velocity_pid.py-9] [INFO] [1781509274.001848081] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0392s, resetting
[velocity_pid.py-9] [INFO] [1781509274.006866998] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.10 corrected=0.34 err=273.3%
[component_container_isolated-18] Reallocing temp weights 1500 - 60
[velocity_pid.py-9] [INFO] [1781509275.029703178] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.40 corrected=0.28 err=20.2%
[velocity_pid.py-9] [INFO] [1781509275.329722473] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.08 -> current=0.04 dt=0.0314s, resetting
[competition_master_stage3.py-19] [INFO] [1781509275.423116433] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.77,-1.02) yaw=-68deg cmd=(vx=0.50 wz=0.04) elapsed=15.6s plan[20pts 2.7m] (-0.90,-0.85)→(0.40,-3.15) cpuFreq=1500MHz cpuT=70C cpu=67% mem=19%
[component_container_isolated-18] [WARN] [1781509275.583446060] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3471 Hz
[component_container_isolated-18] [INFO] [1781509275.741815187] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-6] [INFO] [1781509276.218400235] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2031 q_w=0.7415 angle=84.3deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1781509276.413833529] [imu_madgwick_filter]: [imu_madgwick ->] msgs=800 q_w=0.8328 angle=67.2deg beta=0.0330
[velocity_pid.py-9] [INFO] [1781509276.729262533] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.51 corrected=-0.05 err=24.4%
[cmd_vel_mux.py-8] [INFO] [1781509276.779784617] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.00
[velocity_pid.py-9] [INFO] [1781509276.829143409] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.00 -> current=-0.12 dt=0.0278s, resetting
[velocity_pid.py-9] [INFO] [1781509276.999779162] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0341s, resetting
[qr_decoder-12] [INFO] [1781509277.353828583] [qr_decoder_zbar]: [qr_decoder] QR DETECTED frame=528 symbols=1 (gap=-1 frames)
[qr_decoder-12] [INFO] [1781509277.357970416] [qr_decoder_zbar]: [QR] 1584 | 3D:(-0.461, +0.192, 1.763)m | px(210,243) D:1763mm
[qr_decoder-12] [INFO] [1781509277.361625583] [qr_decoder_zbar]: [QR] 1584 | robot_pos: (0.76, -2.52, yaw=-1.71)
[qr_decision-13] [INFO] [1781509277.365589291] [qr_decision]: [QR] 1584 CCW @ (x=0.76, y=-2.52, yaw=-1.72) → /qr_event
[competition_master_stage3.py-19] [INFO] [1781509277.367365708] [competition_master_stage3]: [QR检测] 内容: 1584
[competition_master_stage3.py-19] [INFO] [1781509277.374818916] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decoder_zbar
[qr_decision-13] [INFO] [1781509277.377875125] [qr_decision]: [检查点] qr_decision 发布 /qr_event (由 task_manager 决定停车)
[competition_master_stage3.py-19] [INFO] [1781509277.378230708] [competition_master_stage3]: >>> QR 解码已关闭, 等待方向判断 (/qr_event)...
[competition_master_stage3.py-19] [INFO] [1781509277.380810666] [competition_master_stage3]: [QR检测] 取消当前导航目标, 等待BT完成 cancel/halt 清理...
[qr_decoder-12] [INFO] [1781509277.432752667] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[competition_master_stage3.py-19] [INFO] [1781509277.474036334] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.43,-1.79) yaw=-60deg cmd=(vx=-0.30 wz=-0.07) elapsed=17.6s plan[17pts 2.3m] (-0.70,-1.15)→(0.40,-3.15) cpuFreq=1500MHz cpuT=70C cpu=86% mem=19%
[rviz2-20] [ERROR] [1781509277.504684751] [rviz2]: Vertex Program:rviz/glsl120/indexed_8bit_image.vert Fragment Program:rviz/glsl120/indexed_8bit_image.frag GLSL link result :
[rviz2-20] active samplers with a different type refer to the same texture image unit
[competition_master_stage3.py-19] [INFO] [1781509277.506399501] [competition_master_stage3]: [QR事件] 方向: 逆时针 (通道巡航阶段使用)
[competition_master_stage3.py-19] [INFO] [1781509277.524450377] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decision
[component_container_isolated-18] [WARN] [1781509277.585185502] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3448 Hz
[component_container_isolated-18] [INFO] [1781509277.641722795] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-18] [INFO] [1781509277.641924753] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1781509277.643197128] [bt_navigator]: [navigate_to_pose] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1781509277.643869628] [bt_navigator]: Goal canceled
[competition_master_stage3.py-19] [INFO] [1781509277.653244503] [competition_master_stage3]: [结果回调] BT取消确认完成 (STATUS_CANCELED), 准备发送通道入口目标...
[competition_master_stage3.py-19] [INFO] [1781509277.658796962] [competition_master_stage3]: [状态机] NAV_TO_QR → BACKING_UP
[competition_master_stage3.py-19] [INFO] [1781509277.661745087] [competition_master_stage3]: >>> BT取消完成, 右后退摆正车头→前进进通道...
[competition_master_stage3.py-19] [INFO] [1781509277.671578545] [competition_master_stage3]: [BACKUP] 右后退中: vx=-0.15 wz=0.80, 持续 6.0s...
[cmd_vel_mux.py-8] [INFO] [1781509277.677294129] [cmd_vel_mux]: [mux→] src=nav vx=-0.15 wz=0.80
[velocity_pid.py-9] [INFO] [1781509277.701121170] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.08 -> current=0.80 dt=0.0353s, resetting
[velocity_pid.py-9] [INFO] [1781509277.730515629] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.09 corrected=-0.34 err=56.7%
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
[INFO] [qr_decoder-12]: process has finished cleanly [pid 63048]
[rviz2-20] [INFO] [1781509277.985903549] [rviz2]: Trying to create a map of size 60 x 60 using 1 swatches
[cmd_vel_mux.py-8] [INFO] [1781509278.177693427] [cmd_vel_mux]: [mux→] src=nav vx=-0.15 wz=0.80
[ERROR] [qr_decision-13]: process has died [pid 63052, exit code 1, cmd '/userdata/dev_ws/install/origincar_qr/lib/origincar_qr/qr_decision --ros-args -r __node:=qr_decision --params-file /tmp/launch_params_q7bsaoh2'].
[velocity_pid.py-9] [INFO] [1781509278.763208059] [velocity_pid]: [vel_pid→] desired=-0.15 actual=-0.01 corrected=-0.27 err=91.3%
[competition_master_stage3.py-19] [INFO] [1781509279.428338943] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.43,-1.79) yaw=-60deg cmd=(vx=-0.15 wz=0.80) elapsed=19.6s plan[11pts 1.5m] (-0.40,-1.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=70C cpu=60% mem=19%
[competition_master_stage3.py-19] [INFO] [1781509281.422790760] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.54,-1.65) yaw=-30deg cmd=(vx=-0.15 wz=0.80) elapsed=21.6s plan[11pts 1.5m] (-0.40,-1.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=70C cpu=40% mem=19%
[competition_master_stage3.py-19] [INFO] [1781509283.424123285] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.85,-1.67) yaw=26deg cmd=(vx=-0.15 wz=0.80) elapsed=23.6s plan[11pts 1.5m] (-0.40,-1.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=69C cpu=67% mem=19%
[competition_master_stage3.py-19] [INFO] [1781509283.671922122] [competition_master_stage3]: [状态机] BACKING_UP → CRUISE_CHANNEL
[competition_master_stage3.py-19] [INFO] [1781509283.676375414] [competition_master_stage3]: [CRUISE] 方向: CCW (逆时针, even QR), 路点: (1.73,-1.98), (3.10,-1.35), (2.10,0.92)
[cmd_vel_mux.py-8] [INFO] [1781509283.678439914] [cmd_vel_mux]: [mux→] src=stop vx=0.00 wz=0.00
[competition_master_stage3.py-19] [INFO] [1781509283.685839039] [competition_master_stage3]: [CRUISE] NavigateThroughPoses: (0.38,-1.10), (1.73,-1.98), (3.10,-1.35), (2.10,0.92)
[component_container_isolated-18] [INFO] [1781509283.690453247] [bt_navigator]: Begin navigating from current location through 4 poses to (2.10, 0.92)
[competition_master_stage3.py-19] [INFO] [1781509283.701317372] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[cmd_vel_mux.py-8] [INFO] [1781509284.177220795] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.50s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1781509284.184189962] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[component_container_isolated-18] [WARN] [1781509284.598309425] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.1062 Hz
[component_container_isolated-18] [INFO] [1781509284.803986886] [controller_server]: Received a goal, begin computing control effort.
[cmd_vel_mux.py-8] [INFO] [1781509284.877848554] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=-0.12
[velocity_pid.py-9] [INFO] [1781509284.896345346] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.04 err=100.0%
[competition_master_stage3.py-19] [INFO] [1781509285.422762103] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.91,-1.71) yaw=39deg cmd=(vx=0.50 wz=-0.79) elapsed=25.6s plan[64pts 8.6m] (-1.00,-1.75)→(2.10,0.95) cpuFreq=1500MHz cpuT=70C cpu=60% mem=19%
[imu_madgwick_filter.py-6] [INFO] [1781509286.219460863] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2587 q_w=0.9985 angle=6.2deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1781509286.414115199] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1000 q_w=0.9817 angle=22.0deg beta=0.0330
[component_container_isolated-18] [WARN] [1781509286.593698951] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4425 Hz
[component_container_isolated-18] [INFO] [1781509286.804433079] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1781509287.421646962] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.48,-1.49) yaw=18deg cmd=(vx=0.50 wz=0.22) elapsed=27.6s plan[60pts 8.0m] (-0.50,-1.55)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=38% mem=19%
[velocity_pid.py-9] [INFO] [1781509287.798299675] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.01 -> current=-0.12 dt=0.0336s, resetting
[velocity_pid.py-9] [INFO] [1781509287.998545469] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.17 err=22.7%
[cmd_vel_mux.py-8] [INFO] [1781509288.012627427] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.04
[velocity_pid.py-9] [INFO] [1781509288.229207430] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0327s, resetting
[component_container_isolated-18] [WARN] [1781509288.593651935] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4267 Hz
[component_container_isolated-18] [INFO] [1781509288.804569521] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781509288.897302355] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.01 -> current=-0.12 dt=0.0336s, resetting
[cmd_vel_mux.py-8] [INFO] [1781509288.911676939] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.24
[velocity_pid.py-9] [INFO] [1781509289.029396482] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781509289.035004857] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.10 corrected=0.37 err=263.3%
[competition_master_stage3.py-19] [INFO] [1781509289.422987654] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.12,-1.27) yaw=23deg cmd=(vx=0.50 wz=-0.65) elapsed=29.6s plan[53pts 6.9m] (0.40,-1.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=0% mem=19%
[component_container_isolated-18] [WARN] [1781509290.593730502] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4304 Hz
[component_container_isolated-18] [INFO] [1781509290.811514921] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1781509291.421939554] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.85,-1.15) yaw=-12deg cmd=(vx=0.50 wz=-0.59) elapsed=31.6s plan[51pts 6.5m] (0.70,-1.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=29% mem=19%
[velocity_pid.py-9] [INFO] [1781509292.000640645] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.00 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1781509292.010763353] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.13
[velocity_pid.py-9] [INFO] [1781509292.131829022] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.01 -> current=0.12 dt=0.0331s, resetting
[velocity_pid.py-9] [INFO] [1781509292.229538606] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0316s, resetting
[component_container_isolated-18] [WARN] [1781509292.590342402] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4338 Hz
[component_container_isolated-18] [INFO] [1781509292.804429488] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781509292.912436740] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.21
[velocity_pid.py-9] [INFO] [1781509293.028914658] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0287s, resetting
[velocity_pid.py-9] [INFO] [1781509293.031736866] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.09 -> current=-0.04 dt=0.0287s, resetting
[velocity_pid.py-9] [INFO] [1781509293.036100491] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.09 corrected=0.39 err=251.7%
[competition_master_stage3.py-19] [INFO] [1781509293.422859746] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.38,-1.42) yaw=-49deg cmd=(vx=0.50 wz=-0.68) elapsed=33.6s plan[43pts 5.6m] (1.50,-1.55)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=33% mem=19%
[velocity_pid.py-9] [INFO] [1781509294.062409588] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.39 corrected=0.27 err=21.6%
[component_container_isolated-18] [WARN] [1781509294.588905928] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4467 Hz
[cmd_vel_mux.py-8] [INFO] [1781509294.611083053] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.25
[component_container_isolated-18] [INFO] [1781509294.704423471] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781509295.064656017] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.39 corrected=0.26 err=21.6%
[imu_madgwick_filter.py-4] [WARN] [1781509295.095083809] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1500s > 0.15s, capping
[competition_master_stage3.py-19] [INFO] [1781509295.421158688] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.64,-1.82) yaw=-63deg cmd=(vx=0.50 wz=1.33) elapsed=35.6s plan[41pts 5.2m] (1.60,-1.85)→(2.10,0.95) cpuFreq=1500MHz cpuT=70C cpu=29% mem=19%
[velocity_pid.py-9] [INFO] [1781509296.196764323] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.01 err=22.7%
[cmd_vel_mux.py-8] [INFO] [1781509296.211154490] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.54
[imu_madgwick_filter.py-6] [INFO] [1781509296.218599073] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3154 q_w=0.9863 angle=19.0deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1781509296.413851993] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1197 q_w=0.9990 angle=5.2deg beta=0.0330
[velocity_pid.py-9] [INFO] [1781509296.430185576] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781509296.497837952] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.08 dt=0.0351s, resetting
[component_container_isolated-18] [WARN] [1781509296.587935412] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2576 Hz
[component_container_isolated-18] [INFO] [1781509296.704470913] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781509296.819448914] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.43
[velocity_pid.py-9] [INFO] [1781509296.929435208] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0322s, resetting
[velocity_pid.py-9] [INFO] [1781509297.199411419] [velocity_pid]: [vel_pid→] desired=0.44 actual=0.01 corrected=0.48 err=98.6%
[competition_master_stage3.py-19] [INFO] [1781509297.421524797] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.40,-2.21) yaw=9deg cmd=(vx=0.50 wz=0.82) elapsed=37.6s plan[31pts 4.3m] (2.30,-2.25)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=43% mem=19%
[component_container_isolated-18] [WARN] [1781509298.585441437] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2720 Hz
[component_container_isolated-18] [INFO] [1781509298.704422105] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781509298.710010313] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.01 err=22.7%
[cmd_vel_mux.py-8] [INFO] [1781509298.711594272] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.10
[velocity_pid.py-9] [INFO] [1781509298.730543897] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.02 -> current=-0.10 dt=0.0206s, resetting
[cmd_vel_mux.py-8] [INFO] [1781509299.412546031] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.51
[competition_master_stage3.py-19] [INFO] [1781509299.425861698] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.94,-1.84) yaw=48deg cmd=(vx=0.50 wz=0.76) elapsed=39.6s plan[28pts 3.6m] (2.80,-1.95)→(2.10,0.95) cpuFreq=1500MHz cpuT=69C cpu=100% mem=19%
[velocity_pid.py-9] [INFO] [1781509299.629337158] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0292s, resetting
[velocity_pid.py-9] [INFO] [1781509299.698603618] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.01 -> current=-0.12 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1781509299.729924951] [velocity_pid]: [vel_pid→] desired=-0.19 actual=0.41 corrected=-0.59 err=313.2%
[component_container_isolated-18] [WARN] [1781509300.586283171] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2620 Hz
[component_container_isolated-18] [INFO] [1781509300.704428755] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781509300.763334798] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.23 corrected=-0.22 err=23.7%
[cmd_vel_mux.py-8] [INFO] [1781509300.810845090] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.22
[velocity_pid.py-9] [INFO] [1781509300.928805842] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0332s, resetting
[velocity_pid.py-9] [INFO] [1781509300.931717633] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.09 -> current=0.03 dt=0.0332s, resetting
[competition_master_stage3.py-19] [INFO] [1781509301.422204264] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.21,-1.38) yaw=71deg cmd=(vx=0.50 wz=1.03) elapsed=41.6s plan[21pts 2.8m] (3.20,-1.35)→(2.10,0.95) cpuFreq=1500MHz cpuT=70C cpu=25% mem=19%
[velocity_pid.py-9] [INFO] [1781509301.798123519] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.31 corrected=0.31 err=37.2%
[component_container_isolated-18] [WARN] [1781509302.583647988] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1781509302.583922946] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.10, 0.92)
[component_container_isolated-18] [WARN] [1781509302.584089238] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1781509302.691328614] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781509302.703068114] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781509302.712454739] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781509302.712634239] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781509302.713503614] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1781509302.713747573] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1781509302.722333656] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[cmd_vel_mux.py-8] [INFO] [1781509303.411733498] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.26
[competition_master_stage3.py-19] [INFO] [1781509303.427251623] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.89,-0.57) yaw=135deg cmd=(vx=0.50 wz=-0.01) elapsed=43.6s plan[21pts 2.8m] (3.20,-1.35)→(2.10,0.95) cpuFreq=1500MHz cpuT=70C cpu=57% mem=19%
[velocity_pid.py-9] [INFO] [1781509303.429128748] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.49 corrected=-0.05 err=53.1%
[component_container_isolated-18] [WARN] [1781509303.591896334] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.7176 Hz
[velocity_pid.py-9] [INFO] [1781509303.629023834] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0330s, resetting
[component_container_isolated-18] [INFO] [1781509303.804432920] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781509304.013477881] [cmd_vel_mux]: [mux→] src=nav vx=0.06 wz=-0.42
[velocity_pid.py-9] [INFO] [1781509304.029492339] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0298s, resetting
[velocity_pid.py-9] [INFO] [1781509304.429594428] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.12 corrected=0.37 err=75.2%
[cmd_vel_mux.py-8] [INFO] [1781509305.411937565] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.55
[competition_master_stage3.py-19] [INFO] [1781509305.424390315] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.59,-0.27) yaw=113deg cmd=(vx=0.50 wz=0.30) elapsed=45.6s plan[15pts 1.9m] (2.90,-0.55)→(2.10,0.95) cpuFreq=1500MHz cpuT=70C cpu=50% mem=19%
[velocity_pid.py-9] [INFO] [1781509305.431485774] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.50 corrected=-0.15 err=57.2%
[component_container_isolated-18] [WARN] [1781509305.582080609] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4568 Hz
[velocity_pid.py-9] [INFO] [1781509305.629665193] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0328s, resetting
[component_container_isolated-18] [INFO] [1781509305.704458485] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781509305.897986488] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.01 -> current=0.08 dt=0.0334s, resetting
[cmd_vel_mux.py-8] [INFO] [1781509305.918985530] [cmd_vel_mux]: [mux→] src=nav vx=0.16 wz=0.42
[imu_madgwick_filter.py-6] [INFO] [1781509306.218166117] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3713 q_w=0.6143 angle=104.2deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1781509306.413103869] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1396 q_w=0.4567 angle=125.7deg beta=0.0330
[velocity_pid.py-9] [INFO] [1781509306.463434078] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.28 corrected=0.22 err=43.8%
[velocity_pid.py-9] [INFO] [1781509306.898797125] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.02 -> current=-0.11 dt=0.0350s, resetting
[competition_master_stage3.py-19] [INFO] [1781509307.423979590] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.16,0.41) yaw=129deg cmd=(vx=0.50 wz=-1.01) elapsed=47.6s plan[8pts 1.1m] (2.40,0.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=70C cpu=60% mem=19%
[component_container_isolated-18] [WARN] [1781509307.582034926] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2727 Hz
[cmd_vel_mux.py-8] [INFO] [1781509307.610310468] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-1.17
[velocity_pid.py-9] [INFO] [1781509307.630465093] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.48 corrected=-0.16 err=51.2%
[component_container_isolated-18] [INFO] [1781509307.704422344] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [INFO] [1781509308.005137014] [controller_server]: Reached the goal!
[component_container_isolated-18] [INFO] [1781509308.491499687] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-19] [INFO] [1781509308.497157896] [competition_master_stage3]: [结果回调] 巡航完成, 到达VLM路点, 触发VLM推理...
[competition_master_stage3.py-19] [INFO] [1781509308.499966437] [competition_master_stage3]: [VLM] 发布 sign4return=100, 拍照推理中...
[competition_master_stage3.py-19] [INFO] [1781509308.502954104] [competition_master_stage3]: [状态机] CRUISE_CHANNEL → RETURN_P
[vision_ai_node-14] [INFO] [1781509308.503818771] [vision_ai_node]: Received sign4return: 100
[vision_ai_node-14] [INFO] [1781509308.508082187] [vision_ai_node]: Received trigger signal (sign4return=100), subscribing to image topic...
[competition_master_stage3.py-19] [INFO] [1781509308.513390229] [competition_master_stage3]: [RETURN] 清除机器人周围1.5m + 直接返航至 P点 (-1.99,-0.01)
[vision_ai_node-14] [INFO] [1781509308.536837479] [vision_ai_node]: Subscribed to /aurora/rgb/image_raw topic
[vision_ai_node-14] [INFO] [1781509308.596377230] [vision_ai_node]: Received compressed image, processing with AI model...
[competition_master_stage3.py-19] [INFO] [1781509308.629874856] [competition_master_stage3]: [RETURN] NavigateThroughPoses→P点(-1.99,-0.01), 0.4m半径通过
[component_container_isolated-18] [INFO] [1781509308.632266522] [bt_navigator]: Begin navigating from current location through 1 poses to (-1.99, -0.01)
[competition_master_stage3.py-19] [INFO] [1781509308.642546356] [competition_master_stage3]: RETURN NavigateThroughPoses 已接受, 车辆出发...
[competition_master_stage3.py-19] [INFO] [1781509309.422346366] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.03,0.75) yaw=75deg cmd=(vx=0.00 wz=0.00) elapsed=49.6s plan[5pts 0.6m] (2.10,0.55)→(2.10,0.95) cpuFreq=1500MHz cpuT=70C cpu=78% mem=19%
[cmd_vel_mux.py-8] [INFO] [1781509309.510798658] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.52s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1781509309.514463367] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[component_container_isolated-18] [WARN] [1781509309.591657034] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.0449 Hz
[component_container_isolated-18] [INFO] [1781509309.734378411] [controller_server]: Received a goal, begin computing control effort.
[cmd_vel_mux.py-8] [INFO] [1781509309.776962662] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=0.12
[velocity_pid.py-9] [INFO] [1781509309.797620954] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.14 err=100.0%
[competition_master_stage3.py-19] [INFO] [1781509311.422237724] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.06,1.19) yaw=108deg cmd=(vx=0.43 wz=1.67) elapsed=51.6s plan[48pts 6.9m] (2.10,0.85)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=71% mem=19%
[component_container_isolated-18] [WARN] [1781509311.590889268] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3217 Hz
[cmd_vel_mux.py-8] [INFO] [1781509311.678219602] [cmd_vel_mux]: [mux→] src=nav vx=0.48 wz=1.67
[component_container_isolated-18] [INFO] [1781509311.734687686] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781509311.830022896] [velocity_pid]: [vel_pid→] desired=0.30 actual=0.43 corrected=-0.14 err=45.6%
[velocity_pid.py-9] [INFO] [1781509312.029047315] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.03 -> current=-0.06 dt=0.0327s, resetting
[velocity_pid.py-9] [INFO] [1781509312.428948237] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.08 dt=0.0304s, resetting
[velocity_pid.py-9] [INFO] [1781509312.863286534] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.12 corrected=-0.28 err=61.0%
[competition_master_stage3.py-19] [INFO] [1781509313.421813749] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.67,1.48) yaw=162deg cmd=(vx=-0.30 wz=-0.60) elapsed=53.6s plan[44pts 6.5m] (2.00,1.35)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=17% mem=19%
[component_container_isolated-18] [WARN] [1781509313.586671085] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1781509313.586973501] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (-1.99, -0.01)
[component_container_isolated-18] [WARN] [1781509313.587084918] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1781509313.733387837] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781509313.746668962] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781509313.753389420] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781509313.753533629] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781509313.756016212] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1781509313.756367795] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1781509313.762006254] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[velocity_pid.py-9] [INFO] [1781509314.496672513] [velocity_pid]: [vel_pid→] desired=-0.16 actual=-0.27 corrected=0.00 err=68.3%
[cmd_vel_mux.py-8] [INFO] [1781509314.512168096] [cmd_vel_mux]: [mux→] src=nav vx=-0.07 wz=1.42
[component_container_isolated-18] [WARN] [1781509314.592532931] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.7955 Hz
[component_container_isolated-18] [INFO] [1781509314.734694099] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781509314.928557602] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0333s, resetting
[cmd_vel_mux.py-8] [INFO] [1781509315.111066396] [cmd_vel_mux]: [mux→] src=nav vx=0.36 wz=0.42
[competition_master_stage3.py-19] [INFO] [1781509315.422225483] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.00,1.28) yaw=-174deg cmd=(vx=0.50 wz=-0.05) elapsed=55.6s plan[44pts 6.4m] (2.00,1.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=60% mem=19%
[velocity_pid.py-9] [INFO] [1781509315.499655651] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.09 corrected=0.45 err=81.8%
[velocity_pid.py-9] [INFO] [1781509316.099740158] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.09 -> current=0.01 dt=0.0350s, resetting
[imu_madgwick_filter.py-6] [INFO] [1781509316.217791910] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4280 q_w=0.0512 angle=174.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1781509316.416653370] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1594 q_w=-0.1569 angle=198.1deg beta=0.0330
[component_container_isolated-18] [WARN] [1781509316.590355039] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3229 Hz
[component_container_isolated-18] [INFO] [1781509316.734692041] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1781509317.423492425] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.44,1.14) yaw=-159deg cmd=(vx=0.50 wz=0.77) elapsed=57.6s plan[43pts 6.2m] (1.70,1.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=71% mem=19%
[velocity_pid.py-9] [INFO] [1781509317.899766389] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.05 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1781509317.910638139] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.60
[velocity_pid.py-9] [INFO] [1781509318.128948392] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781509318.200467726] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.10 -> current=-0.03 dt=0.0285s, resetting
[component_container_isolated-18] [WARN] [1781509318.589032939] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3259 Hz
[component_container_isolated-18] [INFO] [1781509318.734692858] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781509318.810918192] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.29
[velocity_pid.py-9] [INFO] [1781509318.928802360] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0339s, resetting
[velocity_pid.py-9] [INFO] [1781509318.931487569] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.10 corrected=0.38 err=273.3%
[velocity_pid.py-9] [INFO] [1781509318.996956903] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.09 dt=0.0336s, resetting
[competition_master_stage3.py-19] [INFO] [1781509319.423766950] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.04,0.85) yaw=-129deg cmd=(vx=0.50 wz=0.96) elapsed=59.6s plan[37pts 5.4m] (1.00,0.75)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=71% mem=19%
[velocity_pid.py-9] [INFO] [1781509319.965080915] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.37 corrected=0.31 err=26.8%
[component_container_isolated-18] [WARN] [1781509320.584856631] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3384 Hz
[component_container_isolated-18] [INFO] [1781509320.734706133] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781509320.897620760] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.01 -> current=-0.12 dt=0.0332s, resetting
[competition_master_stage3.py-19] [INFO] [1781509321.423345183] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.02,-0.00) yaw=-76deg cmd=(vx=0.50 wz=-0.78) elapsed=61.6s plan[33pts 4.7m] (0.90,0.35)→(-2.00,-0.05) cpuFreq=1200MHz cpuT=69C cpu=57% mem=19%
[cmd_vel_mux.py-8] [INFO] [1781509321.710506812] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.62
[velocity_pid.py-9] [INFO] [1781509321.729121062] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.48 corrected=-0.04 err=51.2%
[velocity_pid.py-9] [INFO] [1781509321.929773815] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0286s, resetting
[velocity_pid.py-9] [INFO] [1781509321.996706107] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.12 -> current=0.00 dt=0.0335s, resetting
[component_container_isolated-18] [WARN] [1781509322.584678114] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3380 Hz
[velocity_pid.py-9] [INFO] [1781509322.729695741] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.06 corrected=-0.36 err=80.7%
[component_container_isolated-18] [INFO] [1781509322.734695491] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781509322.811228701] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.42
[velocity_pid.py-9] [INFO] [1781509322.930451077] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0341s, resetting
[competition_master_stage3.py-19] [INFO] [1781509323.426900792] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.02,-0.43) yaw=-112deg cmd=(vx=0.50 wz=0.28) elapsed=63.6s plan[28pts 4.0m] (1.00,-0.55)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=29% mem=19%
[velocity_pid.py-9] [INFO] [1781509323.762727754] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.27 corrected=0.31 err=45.2%
[component_container_isolated-18] [WARN] [1781509324.589022223] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3256 Hz
[component_container_isolated-18] [INFO] [1781509324.734700391] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1781509325.423979275] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.77,-1.00) yaw=-138deg cmd=(vx=0.50 wz=-0.57) elapsed=65.6s plan[25pts 3.6m] (0.90,-0.75)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=33% mem=19%
[velocity_pid.py-9] [INFO] [1781509325.496986068] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.03 err=22.7%
[cmd_vel_mux.py-8] [INFO] [1781509325.510999109] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.23
[velocity_pid.py-9] [INFO] [1781509325.629639944] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.10 -> current=0.02 dt=0.0328s, resetting
[velocity_pid.py-9] [INFO] [1781509325.729972320] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0317s, resetting
[imu_madgwick_filter.py-6] [INFO] [1781509326.217720577] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4847 q_w=-0.0458 angle=185.2deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1781509326.413362746] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1793 q_w=-0.2819 angle=212.7deg beta=0.0330
[velocity_pid.py-9] [INFO] [1781509326.497583955] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.05 corrected=-0.33 err=85.0%
[component_container_isolated-18] [WARN] [1781509326.587896581] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3277 Hz
[component_container_isolated-18] [INFO] [1781509326.734710333] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781509326.810577459] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.76
[velocity_pid.py-9] [INFO] [1781509326.929924794] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0342s, resetting
[velocity_pid.py-9] [INFO] [1781509327.198273839] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.03 -> current=-0.09 dt=0.0329s, resetting
[competition_master_stage3.py-19] [INFO] [1781509327.423306592] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.50,-1.14) yaw=-150deg cmd=(vx=0.50 wz=-0.32) elapsed=67.6s plan[21pts 2.8m] (0.40,-1.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=62% mem=19%
[velocity_pid.py-9] [INFO] [1781509327.498388426] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.08 corrected=0.44 err=84.4%
[cmd_vel_mux.py-8] [INFO] [1781509328.217381268] [cmd_vel_mux]: [mux→] src=nav vx=0.36 wz=-1.06
[velocity_pid.py-9] [INFO] [1781509328.496990230] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.00 -> current=-0.09 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1781509328.500022605] [velocity_pid]: [vel_pid→] desired=-0.09 actual=0.39 corrected=-0.85 err=552.6%
[component_container_isolated-18] [WARN] [1781509328.587291648] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3291 Hz
[component_container_isolated-18] [INFO] [1781509328.734696150] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781509328.810972067] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.44
[velocity_pid.py-9] [INFO] [1781509328.929010944] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0328s, resetting
[competition_master_stage3.py-19] [INFO] [1781509329.424575158] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.18,-1.29) yaw=-179deg cmd=(vx=0.22 wz=1.67) elapsed=69.6s plan[21pts 2.8m] (0.20,-1.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=56% mem=19%
[velocity_pid.py-9] [INFO] [1781509329.530448743] [velocity_pid]: [vel_pid→] desired=0.26 actual=0.12 corrected=0.17 err=53.0%
[cmd_vel_mux.py-8] [INFO] [1781509330.077818666] [cmd_vel_mux]: [mux→] src=nav vx=0.09 wz=1.54
[velocity_pid.py-9] [INFO] [1781509330.197798376] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.00 -> current=-0.09 dt=0.0332s, resetting
[velocity_pid.py-9] [INFO] [1781509330.563046673] [velocity_pid]: [vel_pid→] desired=-0.30 actual=0.02 corrected=-0.32 err=106.3%
[component_container_isolated-18] [WARN] [1781509330.582514423] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3391 Hz
[velocity_pid.py-9] [INFO] [1781509330.729643300] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.08 dt=0.0339s, resetting
[component_container_isolated-18] [INFO] [1781509330.734704591] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781509330.810718467] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.17
[velocity_pid.py-9] [INFO] [1781509330.930726719] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0311s, resetting
[competition_master_stage3.py-19] [INFO] [1781509331.422132475] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.03,-1.32) yaw=-162deg cmd=(vx=0.28 wz=1.42) elapsed=71.6s plan[20pts 2.6m] (-0.00,-1.35)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=25% mem=19%
[velocity_pid.py-9] [INFO] [1781509331.567378977] [velocity_pid]: [vel_pid→] desired=0.26 actual=0.01 corrected=0.30 err=97.7%
[cmd_vel_mux.py-8] [INFO] [1781509332.278219111] [cmd_vel_mux]: [mux→] src=nav vx=0.10 wz=1.54
[velocity_pid.py-9] [INFO] [1781509332.398498362] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.01 -> current=-0.08 dt=0.0345s, resetting
[component_container_isolated-18] [WARN] [1781509332.588974531] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3256 Hz
[velocity_pid.py-9] [INFO] [1781509332.597949198] [velocity_pid]: [vel_pid→] desired=-0.26 actual=0.13 corrected=-0.35 err=150.9%
[component_container_isolated-18] [INFO] [1781509332.734722575] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1781509333.423083500] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.15,-1.42) yaw=-130deg cmd=(vx=-0.30 wz=1.67) elapsed=73.6s plan[18pts 2.4m] (-0.20,-1.45)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=50% mem=19%
[velocity_pid.py-9] [INFO] [1781509333.599040835] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.22 corrected=-0.22 err=26.0%
[vision_ai_node-14] [INFO] [1781509334.088029008] [vision_ai_node]: AI Analysis Result: 这张图片呈现的是**室内一角**的场景，元素细节如下：
[vision_ai_node-14]
[vision_ai_node-14] ### 物体与位置
[vision_ai_node-14] - **饮料瓶**：画面左侧偏下位置，有一个**透明塑料瓶**，瓶盖为**黄色**，瓶身贴有**红色标签**（标签带黑色、白色文字，推测为品牌标识），瓶内残留少量液体（或为空瓶），整体简洁干净。
[vision_ai_node-14] - **墙面**：背景墙由**浅米色（或白色）瓷砖**铺成，瓷砖间有清晰的**白色勾缝**，墙面平整、整洁，营造出简约的质感。
[vision_ai_node-14] - **深蓝色布料**：画面右侧占据较大面积，是一块**深蓝色厚布料**，表面有自然褶皱，底部露出**黑色支撑结构**（疑似固定布料的支架），布料质感厚实，视觉上有遮挡或分隔空间的作用。
[vision_ai_node-14] - **地面**：覆盖**浅绿色塑料布（或地垫）**，左下角露出一小片**浅黄色区域**，地面平整，材质看起来光滑、防水，推测为临时布置的地垫（如体育馆、活动室的角落）。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] ### 颜色与氛围
[vision_ai_node-14] - 色彩对比鲜明：透明瓶身+黄盖+红标签（活泼）、浅白墙面（柔和）、深蓝布料（厚重）、浅绿地面（清新），整体色调协调。
[vision_ai_node-14] - 场景氛围：光线柔和，空间感简洁，推测为**室内活动空间的角落**（如体育馆、活动室），给人一种临时布置、安静闲置的感觉。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] ### 材质与细节
[vision_ai_node-14] - 饮料瓶：塑料材质，透明感强，瓶盖光滑（塑料/金属质感），标签纸质（或塑料）。
[vision_ai_node-14] - 墙面：瓷砖材质，冷硬质感，勾缝工整。
[vision_ai_node-14] - 布料：厚织物材质，褶皱自然，垂坠感强。
[vision_ai_node-14] - 地面：塑料/地垫材质，表面平滑，色彩均匀（除左下角浅黄色区域）。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] 整体而言，这是一个简洁的室内角落场景，元素布局清晰，色彩搭配和谐，传递出一种安静、临时的空间氛围。
[competition_master_stage3.py-19] [INFO] [1781509334.094302258] [competition_master_stage3]: [VLM] 后台收到推理结果: 这张图片呈现的是**室内一角**的场景，元素细节如下：
[competition_master_stage3.py-19]
[competition_master_stage3.py-19] ### 物体与位置
[competition_master_stage3.py-19] - **饮料瓶**：画面左侧偏下位置，有一个**透明塑料瓶**，瓶盖为**黄色**，瓶身贴有**红色标签**（标签带黑色、白色文字，推测为品牌标识），瓶内...
[vision_ai_node-14] [INFO] [1781509334.099346383] [vision_ai_node]: Unsubscribed from image topic
[cmd_vel_mux.py-8] [INFO] [1781509334.611444140] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=1.42
[velocity_pid.py-9] [INFO] [1781509334.629887432] [velocity_pid]: [vel_pid→] desired=-0.12 actual=-0.29 corrected=0.08 err=139.2%
[component_container_isolated-18] [WARN] [1781509334.685463849] [planner_server]: GridBased: failed to create plan, exceeded maximum iterations.
[component_container_isolated-18] [WARN] [1781509334.685712057] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (-1.99, -0.01)
[component_container_isolated-18] [WARN] [1781509334.685832099] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[velocity_pid.py-9] [INFO] [1781509334.729637891] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0342s, resetting
[component_container_isolated-18] [INFO] [1781509334.833024684] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1781509334.845425518] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781509334.852867601] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781509334.853002143] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781509334.853162309] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1781509334.854580893] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1781509334.862824268] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[velocity_pid.py-9] [INFO] [1781509335.230850189] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.08 dt=0.0340s, resetting
[competition_master_stage3.py-19] [INFO] [1781509335.424515941] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.17,-1.18) yaw=-50deg cmd=(vx=0.39 wz=-0.33) elapsed=75.6s plan[18pts 2.4m] (-0.20,-1.45)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=70C cpu=50% mem=19%
[component_container_isolated-18] [WARN] [1781509335.587967860] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 2.2072 Hz
[velocity_pid.py-9] [INFO] [1781509335.630123736] [velocity_pid]: [vel_pid→] desired=0.36 actual=0.19 corrected=0.36 err=48.1%
[cmd_vel_mux.py-8] [INFO] [1781509335.710582320] [cmd_vel_mux]: [mux→] src=nav vx=0.18 wz=-0.83
[component_container_isolated-18] [INFO] [1781509335.734706445] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781509335.898259197] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.00 -> current=-0.09 dt=0.0345s, resetting
[velocity_pid.py-9] [INFO] [1781509336.099509117] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.08 -> current=0.04 dt=0.0350s, resetting
[imu_madgwick_filter.py-6] [INFO] [1781509336.219110660] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5416 q_w=-0.7940 angle=285.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1781509336.413525662] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1993 q_w=-0.9236 angle=314.9deg beta=0.0330
[velocity_pid.py-9] [INFO] [1781509336.663370707] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.06 corrected=-0.32 err=78.3%
[competition_master_stage3.py-19] [INFO] [1781509337.422485508] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.10,-1.26) yaw=-53deg cmd=(vx=-0.30 wz=0.35) elapsed=77.6s plan[15pts 2.1m] (-0.20,-1.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=25% mem=19%
[component_container_isolated-18] [WARN] [1781509337.587157510] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3291 Hz
[velocity_pid.py-9] [INFO] [1781509337.697696303] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.10 -> current=-0.01 dt=0.0331s, resetting
[component_container_isolated-18] [INFO] [1781509337.734692762] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781509338.798254608] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.30 corrected=-0.01 err=43.3%
[cmd_vel_mux.py-8] [INFO] [1781509338.811174359] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.18
[velocity_pid.py-9] [INFO] [1781509338.928750402] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0335s, resetting
[competition_master_stage3.py-19] [INFO] [1781509339.422745949] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.55,-0.92) yaw=-30deg cmd=(vx=0.50 wz=-0.05) elapsed=79.6s plan[15pts 2.1m] (-0.20,-1.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=0% mem=19%
[component_container_isolated-18] [WARN] [1781509339.587136410] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3292 Hz
[component_container_isolated-18] [INFO] [1781509339.734696495] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781509339.810700871] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.29
[velocity_pid.py-9] [INFO] [1781509339.896099372] [velocity_pid]: [vel_pid→] desired=0.23 actual=0.32 corrected=0.03 err=39.1%
[velocity_pid.py-9] [INFO] [1781509340.028849124] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0331s, resetting
[velocity_pid.py-9] [INFO] [1781509340.897156634] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.12 corrected=-0.31 err=58.7%
[competition_master_stage3.py-19] [INFO] [1781509341.421299308] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.55,-0.92) yaw=-30deg cmd=(vx=-0.30 wz=0.05) elapsed=81.6s plan[12pts 1.6m] (-0.60,-0.85)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=60% mem=19%
[component_container_isolated-18] [WARN] [1781509341.586650226] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3294 Hz
[component_container_isolated-18] [INFO] [1781509341.734703895] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781509342.899167201] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.31 corrected=0.00 err=46.2%
[cmd_vel_mux.py-8] [INFO] [1781509342.912110118] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.65
[velocity_pid.py-9] [INFO] [1781509343.029710286] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0332s, resetting
[competition_master_stage3.py-19] [INFO] [1781509343.421903874] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.88,-0.77) yaw=-17deg cmd=(vx=0.50 wz=-0.42) elapsed=83.6s plan[12pts 1.7m] (-0.60,-0.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=0% mem=19%
[component_container_isolated-18] [WARN] [1781509343.582717751] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3370 Hz
[component_container_isolated-18] [INFO] [1781509343.734689961] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781509343.810981254] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.13
[velocity_pid.py-9] [INFO] [1781509343.930602797] [velocity_pid]: [vel_pid→] desired=0.14 actual=0.28 corrected=-0.03 err=100.7%
[velocity_pid.py-9] [INFO] [1781509344.029194507] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0326s, resetting
[velocity_pid.py-9] [INFO] [1781509344.329787719] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.01 -> current=0.12 dt=0.0318s, resetting
[velocity_pid.py-9] [INFO] [1781509344.964271393] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.15 corrected=-0.29 err=50.0%
[competition_master_stage3.py-19] [INFO] [1781509345.421751149] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.89,-0.79) yaw=-33deg cmd=(vx=-0.30 wz=0.07) elapsed=85.6s plan[9pts 1.2m] (-1.00,-0.75)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=67% mem=19%
[component_container_isolated-18] [WARN] [1781509345.582259901] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3384 Hz
[component_container_isolated-18] [INFO] [1781509345.734688028] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-6] [INFO] [1781509346.219271159] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=6003 q_w=-0.9128 angle=311.8deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1781509346.412854744] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2193 q_w=-0.9889 angle=342.9deg beta=0.0330
[velocity_pid.py-9] [INFO] [1781509346.900056875] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.29 corrected=-0.04 err=40.0%
[cmd_vel_mux.py-8] [INFO] [1781509346.911331584] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.22
[velocity_pid.py-9] [INFO] [1781509347.030454169] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0332s, resetting
[competition_master_stage3.py-19] [INFO] [1781509347.422632465] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.27,-0.55) yaw=-42deg cmd=(vx=0.50 wz=-0.03) elapsed=87.6s plan[9pts 1.2m] (-1.00,-0.75)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=57% mem=19%
[component_container_isolated-18] [WARN] [1781509347.587236259] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3293 Hz
[component_container_isolated-18] [INFO] [1781509347.734697511] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781509347.811045595] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.18
[velocity_pid.py-9] [INFO] [1781509347.929641138] [velocity_pid]: [vel_pid→] desired=0.14 actual=0.26 corrected=-0.02 err=86.4%
[velocity_pid.py-9] [INFO] [1781509348.030338681] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0258s, resetting
[velocity_pid.py-9] [INFO] [1781509348.929758359] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.13 corrected=-0.32 err=56.7%
[competition_master_stage3.py-19] [INFO] [1781509349.422738740] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.26,-0.55) yaw=-34deg cmd=(vx=-0.30 wz=-0.08) elapsed=89.6s plan[6pts 0.7m] (-1.40,-0.45)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=33% mem=19%
[component_container_isolated-18] [WARN] [1781509349.586680284] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3295 Hz
[component_container_isolated-18] [INFO] [1781509349.734712244] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781509350.878560133] [cmd_vel_mux]: [mux→] src=nav vx=-0.17 wz=0.14
[velocity_pid.py-9] [INFO] [1781509350.896069842] [velocity_pid]: [vel_pid→] desired=-0.17 actual=-0.29 corrected=0.03 err=73.8%
[velocity_pid.py-9] [INFO] [1781509350.996499884] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.08 -> current=0.01 dt=0.0340s, resetting
[competition_master_stage3.py-19] [INFO] [1781509351.422724265] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.64,-0.25) yaw=-43deg cmd=(vx=0.16 wz=-0.01) elapsed=91.6s plan[6pts 0.7m] (-1.40,-0.45)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=20% mem=19%
[component_container_isolated-18] [WARN] [1781509351.582224683] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3390 Hz
[component_container_isolated-18] [INFO] [1781509351.734702310] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781509351.778144144] [cmd_vel_mux]: [mux→] src=nav vx=0.05 wz=0.11
[velocity_pid.py-9] [INFO] [1781509351.796889394] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.01 -> current=0.11 dt=0.0326s, resetting
[velocity_pid.py-9] [INFO] [1781509351.828909270] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0339s, resetting
[velocity_pid.py-9] [INFO] [1781509351.896989687] [velocity_pid]: [vel_pid→] desired=-0.11 actual=0.01 corrected=-0.22 err=111.5%
[velocity_pid.py-9] [INFO] [1781509352.899361991] [velocity_pid]: [vel_pid→] desired=-0.14 actual=-0.09 corrected=-0.11 err=40.2%
[component_container_isolated-18] [INFO] [1781509353.035282785] [controller_server]: Reached the goal!
[cmd_vel_mux.py-8] [INFO] [1781509353.110552202] [cmd_vel_mux]: [mux→] src=nav vx=0.00 wz=0.05
[competition_master_stage3.py-19] [INFO] [1781509353.422538914] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.80,-0.15) yaw=-33deg cmd=(vx=0.00 wz=0.00) elapsed=93.6s plan[2pts 0.2m] (-1.80,-0.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=67% mem=19%
[component_container_isolated-18] [WARN] [1781509353.586558791] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3297 Hz
[component_container_isolated-18] [WARN] [1781509353.587686375] [BehaviorTreeEngine]: Behavior Tree tick rate 10.00 was exceeded!
[component_container_isolated-18] [INFO] [1781509353.588554250] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-19] [INFO] [1781509353.606341917] [competition_master_stage3]: [结果回调] 已通过P点, 任务完成!
[competition_master_stage3.py-19] [INFO] [1781509353.610764958] [competition_master_stage3]: [状态机] RETURN_P → DONE
[competition_master_stage3.py-19] [INFO] [1781509353.615034542] [competition_master_stage3]:
[competition_master_stage3.py-19] [INFO] [1781509353.618918542] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1781509353.622307209] [competition_master_stage3]: >>> [Stage 3] 任务结束 <<<
[competition_master_stage3.py-19] [INFO] [1781509353.625449625] [competition_master_stage3]:   最终状态: DONE
[competition_master_stage3.py-19] [INFO] [1781509353.629049959] [competition_master_stage3]:   总耗时:   93.8s
[competition_master_stage3.py-19] [INFO] [1781509353.631963459] [competition_master_stage3]:   --- 各阶段耗时 ---
[competition_master_stage3.py-19] [INFO] [1781509353.635493584] [competition_master_stage3]:   LAUNCH................ 14.4s
[competition_master_stage3.py-19] [INFO] [1781509353.638360792] [competition_master_stage3]:   NAV_TO_QR............. 17.9s
[competition_master_stage3.py-19] [INFO] [1781509353.642026417] [competition_master_stage3]:   BACKING_UP............ 6.0s
[cmd_vel_mux.py-8] [INFO] [1781509353.643718625] [cmd_vel_mux]: [mux→] src=stop vx=0.00 wz=0.00
[competition_master_stage3.py-19] [INFO] [1781509353.645468334] [competition_master_stage3]:   CRUISE_CHANNEL........ 24.8s
[competition_master_stage3.py-19] [INFO] [1781509353.648815042] [competition_master_stage3]:   RETURN_P.............. 45.1s
[competition_master_stage3.py-19] [INFO] [1781509353.651625459] [competition_master_stage3]:   (transition/overhead). -14.4s
[competition_master_stage3.py-19] [INFO] [1781509353.654244251] [competition_master_stage3]:   --- ---
[competition_master_stage3.py-19] [INFO] [1781509353.657279167] [competition_master_stage3]:   QR 原始数据: 1584
[competition_master_stage3.py-19] [INFO] [1781509353.660597001] [competition_master_stage3]:   QR 方向:   逆时针 (CW=顺时针/odd, CCW=逆时针/even)
[competition_master_stage3.py-19] [INFO] [1781509353.663559876] [competition_master_stage3]:   VLM 结果:  这张图片呈现的是**室内一角**的场景，元素细节如下：
[competition_master_stage3.py-19]
[competition_master_stage3.py-19] ### 物体与位置
[competition_master_stage3.py-19] - **饮料瓶**：画面左侧偏下位置，有一个**透明塑料瓶**，瓶盖为**黄色**，瓶身贴有**红色标签**（标签带黑色、白色文字，推测为品牌标识），瓶内残留少量液体（或为空瓶），整体简洁干净。
[competition_master_stage3.py-19] - **墙面**：背景墙由**浅米色（或白色）瓷砖**铺成，瓷砖间有清晰的**白色勾缝**，墙面平整、整洁，营造出
[competition_master_stage3.py-19] [INFO] [1781509353.667173959] [competition_master_stage3]:   超时限制:  180.0s (全局)
[competition_master_stage3.py-19] [INFO] [1781509353.671574251] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1781509353.677726834] [competition_master_stage3]: [TRAJ] 轨迹已保存: /userdata/dev_ws/trajectory.csv (104 点)
[cmd_vel_mux.py-8] [INFO] [1781509354.509966303] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.52s > 0.5s, marked inactive
[competition_master_stage3.py-19] [INFO] [1781509355.421899231] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.80,-0.15) yaw=-33deg cmd=(vx=0.00 wz=0.00) elapsed=95.6s plan[2pts 0.1m] (-1.90,-0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=0% mem=19%
[imu_madgwick_filter.py-6] [INFO] [1781509356.218806241] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=6590 q_w=-0.9418 angle=320.7deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1781509356.413651951] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2393 q_w=-0.9998 angle=357.6deg beta=0.0330
[competition_master_stage3.py-19] [INFO] [1781509357.421086130] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.80,-0.15) yaw=-33deg cmd=(vx=0.00 wz=0.00) elapsed=97.6s plan[2pts 0.1m] (-1.90,-0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=33% mem=19%
[competition_master_stage3.py-19] [INFO] [1781509359.423224697] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.80,-0.15) yaw=-33deg cmd=(vx=0.00 wz=0.00) elapsed=99.6s plan[2pts 0.1m] (-1.90,-0.05)→(-2.00,-0.05) cpuFreq=1200MHz cpuT=69C cpu=57% mem=19%
[competition_master_stage3.py-19] [INFO] [1781509361.423631846] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.80,-0.15) yaw=-33deg cmd=(vx=0.00 wz=0.00) elapsed=101.6s plan[2pts 0.1m] (-1.90,-0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=69C cpu=33% mem=19%
[competition_master_stage3.py-19] [INFO] [1781509363.422940787] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.80,-0.15) yaw=-33deg cmd=(vx=0.00 wz=0.00) elapsed=103.6s plan[2pts 0.1m] (-1.90,-0.05)→(-2.00,-0.05) cpuFreq=1200MHz cpuT=69C cpu=62% mem=19%
^C[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[component_container_isolated-18] [INFO] [1781509364.400920008] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-18] [INFO] [1781509364.401140341] [velocity_smoother]: Running Nav2 LifecycleNode rcl preshutdown (velocity_smoother)
[component_container_isolated-18] [INFO] [1781509364.401538799] [velocity_smoother]: Deactivating
[component_container_isolated-18] [INFO] [1781509364.401685091] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[ERROR] [origincar_base_node-1]: process has died [pid 62984, exit code -6, cmd '/userdata/dev_ws/install/origincar_base/lib/origincar_base/origincar_base_node --ros-args --params-file /tmp/launch_params_xn44hnw8 --params-file /tmp/launch_params_3jku0wne'].
[ERROR] [lslidar_driver_node-2]: process has died [pid 62986, exit code -6, cmd '/userdata/dev_ws/install/lslidar_driver/lib/lslidar_driver/lslidar_driver_node --ros-args -r __node:=lslidar_driver_node --params-file /userdata/dev_ws/install/lslidar_driver/share/lslidar_driver/params/lsx10.yaml'].
[INFO] [lifecycle_manager-17]: process has finished cleanly [pid 63179]
[INFO] [static_transform_publisher-10]: process has finished cleanly [pid 63042]
[INFO] [robot_state_publisher-3]: process has finished cleanly [pid 62988]
[INFO] [ekf_node-7]: process has finished cleanly [pid 62996]
[INFO] [costmap_filter_info_server-16]: process has finished cleanly [pid 63166]
[INFO] [map_server-15]: process has finished cleanly [pid 63163]
[map_server-15] [INFO] [1781509364.400996966] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-15] [INFO] [1781509364.401274341] [keepout_mask_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_mask_server)
[map_server-15] [INFO] [1781509364.401539008] [keepout_mask_server]: Deactivating
[map_server-15] [INFO] [1781509364.401661508] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[lifecycle_manager-17] [INFO] [1781509364.401048924] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-17] [INFO] [1781509364.401278508] [lifecycle_manager_keepout]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_keepout)
[lifecycle_manager-17] [INFO] [1781509364.401420466] [lifecycle_manager_keepout]: Terminating bond timer...
[aurora930_node-11] [INFO] [1781509364.401160674] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[static_transform_publisher-10] [INFO] [1781509364.401201716] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[robot_state_publisher-3] [INFO] [1781509364.402349466] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1781509364.402427299] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1781509364.402738883] [origincar_base]: Stop command sent to STM32 on shutdown.
[origincar_base_node-1] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[ekf_node-7] [INFO] [1781509364.403503299] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-16] [INFO] [1781509364.404971966] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-16] [INFO] [1781509364.405290424] [keepout_filter_info_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_filter_info_server)
[costmap_filter_info_server-16] [INFO] [1781509364.405578883] [keepout_filter_info_server]: Deactivating
[map_server-15] [INFO] [1781509364.417834925] [keepout_mask_server]: Cleaning up
[map_server-15] [INFO] [1781509364.418121716] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[map_server-15] [INFO] [1781509364.515941842] [keepout_mask_server]: Destroying
[costmap_filter_info_server-16] [INFO] [1781509364.406144549] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-16] [INFO] [1781509364.427452258] [keepout_filter_info_server]: Cleaning up
[costmap_filter_info_server-16] [INFO] [1781509364.427697341] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-16] [INFO] [1781509364.543050801] [keepout_filter_info_server]: Destroying
[aurora930_node-11] I0615 15:42:44.431092 63045 ros2_node.cc:90] process quit succeed
[aurora930_node-11] I0615 15:42:44.431293 63045 aurora900_ros2_device.cc:83] begin stop()
[aurora930_node-11] I0615 15:42:44.493489 63045 aurora900_ros2_device.cc:103] stop stream
[aurora930_node-11] 2026-06-15 15:42:44.508 ( 129.339s) [        8C9B4020]      aurora900_impl.cc:648   INFO| ir_stream_count_=0, rgb_stream_count_=0, depth_stream_count_=0
[aurora930_node-11] 2026-06-15 15:42:44.508 ( 129.339s) [        8C9B4020]      aurora900_impl.cc:649   INFO| mask=7
[aurora930_node-11] I0615 15:42:44.873013 63045 aurora900_ros2_device.cc:105] destroy stream
[aurora930_node-11] I0615 15:42:44.873247 63045 aurora900_ros2_device.cc:110] close glog
[aurora930_node-11] WARNING: Logging before InitGoogleLogging() is written to STDERR
[aurora930_node-11] I0615 15:42:44.873368 63045 ros2_device.cc:113] close device...
[aurora930_node-11] 2026-06-15 15:42:45.373 ( 130.203s) [        6D1D37E0]         cmd_backend.cc:40    INFO| RunBlocking is end!!!
[aurora930_node-11] 2026-06-15 15:42:45.573 ( 130.403s) [        8C9B4020]deptrum_camera_vendor.c:121   INFO| device is close.
[aurora930_node-11] I0615 15:42:45.575807 63045 ros2_device.cc:116] quit succeed
[rviz2-20] [INFO] [1781509364.436269800] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] terminate called after throwing an instance of 'rclcpp::exceptions::RCLError'
[origincar_base_node-1]   what():  failed to create guard condition: the given context is not valid, either rcl_init() was not called or rcl_shutdown() was called., at ./src/rcl/guard_condition.c:67
[component_container_isolated-18] [INFO] [1781509364.505912884] [velocity_smoother]: Cleaning up
[component_container_isolated-18] [INFO] [1781509364.506191384] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509364.506344176] [bt_navigator]: Running Nav2 LifecycleNode rcl preshutdown (bt_navigator)
[component_container_isolated-18] [INFO] [1781509364.506495092] [bt_navigator]: Deactivating
[component_container_isolated-18] [INFO] [1781509364.507841134] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509364.629066302] [bt_navigator]: Cleaning up
[component_container_isolated-18] [INFO] [1781509364.629756844] [local_costmap.local_costmap]: Message Filter dropping message: frame 'laser_link' at time 1781509364.328 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-18] [INFO] [1781509364.674157803] [lifecycle_manager_navigation]: Have not received a heartbeat from bt_navigator.
[component_container_isolated-18] [ERROR] [1781509364.674372928] [lifecycle_manager_navigation]: CRITICAL FAILURE: SERVER bt_navigator IS DOWN after not receiving a heartbeat for 4000 ms. Shutting down related nodes.
[component_container_isolated-18] [INFO] [1781509364.674709969] [lifecycle_manager_navigation]: Terminating bond timer...
[component_container_isolated-18] [INFO] [1781509364.674813678] [lifecycle_manager_navigation]: Resetting managed nodes...
[component_container_isolated-18] [INFO] [1781509364.674875928] [lifecycle_manager_navigation]: Deactivating velocity_smoother
[component_container_isolated-18] [WARN] [1781509364.676043553] [rcl_lifecycle]: No transition matching 4 found for current state unconfigured
[component_container_isolated-18] [WARN] [1781509364.676122761] [rcl_lifecycle]: No transition matching 4 found for current state unconfigured
[component_container_isolated-18] [ERROR] [1781509364.676163678] [velocity_smoother]: Unable to start transition 4 from current state unconfigured: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-18] [ERROR] [1781509364.678704094] [lifecycle_manager_navigation]: Failed to change state for node: velocity_smoother
[component_container_isolated-18] [INFO] [1781509364.678945761] [lifecycle_manager_navigation]: Deactivating waypoint_follower
[component_container_isolated-18] [INFO] [1781509364.680252469] [waypoint_follower]: Deactivating
[component_container_isolated-18] [INFO] [1781509364.680501261] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509364.800492013] [lifecycle_manager_navigation]: Deactivating bt_navigator
[component_container_isolated-18] [WARN] [1781509364.801554221] [rcl_lifecycle]: No transition matching 4 found for current state cleaningup
[component_container_isolated-18] [WARN] [1781509364.801670679] [rcl_lifecycle]: No transition matching 4 found for current state cleaningup
[component_container_isolated-18] [ERROR] [1781509364.801702554] [bt_navigator]: Unable to start transition 4 from current state cleaningup: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-18] [ERROR] [1781509364.803304304] [lifecycle_manager_navigation]: Failed to change state for node: bt_navigator
[component_container_isolated-18] [INFO] [1781509364.803519429] [lifecycle_manager_navigation]: Deactivating behavior_server
[component_container_isolated-18] [INFO] [1781509364.804499846] [behavior_server]: Deactivating
[component_container_isolated-18] [INFO] [1781509364.804785138] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509364.928743472] [lifecycle_manager_navigation]: Deactivating planner_server
[component_container_isolated-18] [INFO] [1781509364.929948556] [planner_server]: Deactivating
[component_container_isolated-18] [INFO] [1781509364.930362598] [global_costmap.global_costmap]: Deactivating
[component_container_isolated-18] [INFO] [1781509365.131918183] [bt_navigator]: Completed Cleaning up
[component_container_isolated-18] [INFO] [1781509365.132171642] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509365.132252933] [behavior_server]: Running Nav2 LifecycleNode rcl preshutdown (behavior_server)
[component_container_isolated-18] [INFO] [1781509365.132376350] [behavior_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781509365.143204850] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509365.143350683] [planner_server]: Running Nav2 LifecycleNode rcl preshutdown (planner_server)
[component_container_isolated-18] [INFO] [1781509365.143425600] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509365.250134851] [smoother_server]: Running Nav2 LifecycleNode rcl preshutdown (smoother_server)
[component_container_isolated-18] [INFO] [1781509365.250515768] [smoother_server]: Deactivating
[component_container_isolated-18] [INFO] [1781509365.250601226] [smoother_server]: Deactivating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781509365.250875351] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509365.262057685] [smoother_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781509365.262230352] [smoother_server]: Cleaning up smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781509365.297697185] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509365.297834144] [lifecycle_manager_localization]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_localization)
[component_container_isolated-18] [INFO] [1781509365.297895560] [lifecycle_manager_localization]: Terminating bond timer...
[component_container_isolated-18] [INFO] [1781509365.332846394] [amcl]: Running Nav2 LifecycleNode rcl preshutdown (amcl)
[component_container_isolated-18] [INFO] [1781509365.333092269] [amcl]: Deactivating
[component_container_isolated-18] [INFO] [1781509365.333273227] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509365.343656561] [amcl]: Cleaning up
[component_container_isolated-18] [INFO] [1781509365.359933478] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509365.360111228] [lifecycle_manager_navigation]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_navigation)
[component_container_isolated-18] [INFO] [1781509365.575185314] [planner_server]: Deactivating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781509365.575490022] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509365.586857481] [lifecycle_manager_navigation]: Deactivating smoother_server
[component_container_isolated-18] [WARN] [1781509365.587666397] [rcl_lifecycle]: No transition matching 4 found for current state unconfigured
[component_container_isolated-18] [WARN] [1781509365.587738439] [rcl_lifecycle]: No transition matching 4 found for current state unconfigured
[component_container_isolated-18] [ERROR] [1781509365.587767897] [smoother_server]: Unable to start transition 4 from current state unconfigured: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-18] [ERROR] [1781509365.589474147] [lifecycle_manager_navigation]: Failed to change state for node: smoother_server
[component_container_isolated-18] [INFO] [1781509365.589680939] [lifecycle_manager_navigation]: Deactivating controller_server
[component_container_isolated-18] [INFO] [1781509365.590454439] [controller_server]: Deactivating
[component_container_isolated-18] [INFO] [1781509365.590584772] [controller_server]: Deactivating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781509365.590824231] [local_costmap.local_costmap]: Deactivating
[component_container_isolated-18] [INFO] [1781509365.614549189] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509365.731349316] [lifecycle_manager_navigation]: Cleaning up velocity_smoother
[component_container_isolated-18] [WARN] [1781509365.732360607] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-18] [WARN] [1781509365.732450691] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-18] [ERROR] [1781509365.732481399] [velocity_smoother]: Unable to start transition 2 from current state unconfigured: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-18] [INFO] [1781509365.733731399] [lifecycle_manager_navigation]: Cleaning up waypoint_follower
[component_container_isolated-18] [INFO] [1781509365.734481399] [waypoint_follower]: Cleaning up
[component_container_isolated-18] [INFO] [1781509365.765458691] [lifecycle_manager_navigation]: Cleaning up bt_navigator
[component_container_isolated-18] [WARN] [1781509365.766199941] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-18] [WARN] [1781509365.766324858] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-18] [ERROR] [1781509365.766355191] [bt_navigator]: Unable to start transition 2 from current state unconfigured: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-18] [INFO] [1781509365.767467399] [lifecycle_manager_navigation]: Cleaning up behavior_server
[component_container_isolated-18] [WARN] [1781509365.768189816] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-18] [WARN] [1781509365.768273399] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-18] [ERROR] [1781509365.768310441] [behavior_server]: Unable to start transition 2 from current state unconfigured: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-18] [INFO] [1781509365.769489358] [lifecycle_manager_navigation]: Cleaning up planner_server
[component_container_isolated-18] [INFO] [1781509365.770322399] [planner_server]: Cleaning up
[lifecycle_manager-17] [INFO] [1781509364.552678718] [lifecycle_manager_keepout]: Destroying lifecycle_manager_keepout
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
[component_container_isolated-18] [INFO] [1781509365.815448150] [global_costmap.global_costmap]: Cleaning up
[component_container_isolated-18] [INFO] [1781509365.838938692] [planner_server]: Cleaning up plugin GridBased of type SmacPlannerHybrid
[imu_madgwick_filter.py-6] Traceback (most recent call last):
[imu_madgwick_filter.py-6]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/imu_madgwick_filter.py", line 301, in <module>
[imu_madgwick_filter.py-6]     main()
[imu_madgwick_filter.py-6]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/imu_madgwick_filter.py", line 286, in main
[imu_madgwick_filter.py-6]     rclpy.spin(node)
[imu_madgwick_filter.py-6]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 229, in spin
[imu_madgwick_filter.py-6]     executor.spin_once()
[imu_madgwick_filter.py-6]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 808, in spin_once
[imu_madgwick_filter.py-6]     self._spin_once_impl(timeout_sec)
[imu_madgwick_filter.py-6]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 805, in _spin_once_impl
[imu_madgwick_filter.py-6]     raise handler.exception()
[imu_madgwick_filter.py-6]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/task.py", line 272, in _execute_coroutine_step
[component_container_isolated-18] [INFO] [1781509365.881456109] [planner_server]: Destroying plugin GridBased of type SmacPlannerHybrid
[imu_madgwick_filter.py-6]     result = coro.send(None)
[imu_madgwick_filter.py-6]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 478, in handler
[imu_madgwick_filter.py-6]     arg = take_from_wait_list(entity)
[imu_madgwick_filter.py-6]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 400, in _take_subscription
[imu_madgwick_filter.py-6]     msg_info = sub.handle.take_message(sub.msg_type, sub.raw)
[imu_madgwick_filter.py-6] RuntimeError: Unable to convert call argument to Python object (compile in debug mode for details)
[component_container_isolated-18] [INFO] [1781509365.916469651] [lifecycle_manager_navigation]: Cleaning up smoother_server
[component_container_isolated-18] [WARN] [1781509365.917176860] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-18] [WARN] [1781509365.917259193] [rcl_lifecycle]: No transition matching 2 found for current state unconfigured
[component_container_isolated-18] [ERROR] [1781509365.917292443] [smoother_server]: Unable to start transition 2 from current state unconfigured: Transition is not registered., at ./src/rcl_lifecycle.c:355
[component_container_isolated-18] [INFO] [1781509365.918406360] [lifecycle_manager_navigation]: Cleaning up controller_server
[component_container_isolated-18] [INFO] [1781509365.919256318] [controller_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781509365.919408026] [controller_server]: Cleaning up controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781509365.927710360] [local_costmap.local_costmap]: Cleaning up
[component_container_isolated-18] [INFO] [1781509366.016372486] [lifecycle_manager_navigation]: Managed nodes have been reset
[INFO] [imu_madgwick_filter.py-4]: process has finished cleanly [pid 62990]
[component_container_isolated-18] [INFO] [1781509366.088153112] [waypoint_follower]: Running Nav2 LifecycleNode rcl preshutdown (waypoint_follower)
[component_container_isolated-18] [INFO] [1781509366.088365903] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509366.088435112] [controller_server]: Running Nav2 LifecycleNode rcl preshutdown (controller_server)
[component_container_isolated-18] [INFO] [1781509366.088508028] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781509366.088563445] [map_server]: Running Nav2 LifecycleNode rcl preshutdown (map_server)
[component_container_isolated-18] [INFO] [1781509366.088690028] [map_server]: Deactivating
[component_container_isolated-18] [INFO] [1781509366.088847737] [map_server]: Destroying bond (map_server) to lifecycle manager.
[INFO] [cmd_vel_mux.py-8]: process has finished cleanly [pid 63002]
[component_container_isolated-18] [INFO] [1781509366.099902862] [map_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781509366.100138320] [map_server]: Destroying bond (map_server) to lifecycle manager.
[INFO] [velocity_pid.py-9]: process has finished cleanly [pid 63017]
[INFO] [competition_master_stage3.py-19]: process has finished cleanly [pid 63343]
[ERROR] [bmi088_iio_bridge.py-5]: process has died [pid 62992, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/bmi088_iio_bridge.py --ros-args -r __node:=bmi088_iio_bridge --params-file /tmp/launch_params_v4g409lr'].
[ERROR] [imu_madgwick_filter.py-6]: process has died [pid 62994, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/imu_madgwick_filter.py --ros-args -r __node:=imu_madgwick_bmi088 --params-file /userdata/dev_ws/install/origincar_base/share/origincar_base/config/imu_madgwick_bmi088.yaml -r /imu/data_raw:=/imu_data -r /imu/data/madgwick:=/imu/data/bmi088_madgwick'].
[ERROR] [vision_ai_node-14]: process has died [pid 63063, exit code 1, cmd '/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node --ros-args -r __node:=vision_ai_node'].
[INFO] [aurora930_node-11]: process has finished cleanly [pid 63045]
[ERROR] [rviz2-20]: process has died [pid 63345, exit code -11, cmd '/opt/ros/humble/lib/rviz2/rviz2 -d /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/rviz/nav.rviz --ros-args -r __node:=rviz2'].
[ERROR] [component_container_isolated-18]: process[component_container_isolated-18] failed to terminate '5' seconds after receiving 'SIGINT', escalating to 'SIGTERM'
[INFO] [component_container_isolated-18]: sending signal 'SIGTERM' to process[component_container_isolated-18]
[component_container_isolated-18] [INFO] [1781509370.785137502] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [component_container_isolated-18]: process[component_container_isolated-18] failed to terminate '10.0' seconds after receiving 'SIGTERM', escalating to 'SIGKILL'
[INFO] [component_container_isolated-18]: sending signal 'SIGKILL' to process[component_container_isolated-18]
[ERROR] [component_container_isolated-18]: process has died [pid 63341, exit code -9, cmd '/opt/ros/humble/lib/rclcpp_components/component_container_isolated --ros-args --log-level info --ros-args -r __node:=nav2_container --params-file /tmp/launch_params_qmi413qn --params-file /tmp/launch_params_qk9lvnzi -r /tf:=tf -r /tf_static:=tf_static'].
root@ubuntu:/userdata/dev_ws#
