root@ubuntu:/userdata/dev_ws# ros2 launch origincar_bringup stage3_bringup.launch.py
[INFO] [launch]: All log files can be found below /root/.ros/log/2026-06-25-18-11-10-139792-ubuntu-15300
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [origincar_base_node-1]: process started with pid [15322]
[INFO] [lslidar_driver_node-2]: process started with pid [15324]
[INFO] [robot_state_publisher-3]: process started with pid [15326]
[INFO] [imu_madgwick_filter.py-4]: process started with pid [15328]
[INFO] [bmi088_iio_bridge.py-5]: process started with pid [15330]
[INFO] [imu_madgwick_filter.py-6]: process started with pid [15332]
[INFO] [ekf_node-7]: process started with pid [15334]
[INFO] [cmd_vel_mux.py-8]: process started with pid [15336]
[INFO] [velocity_pid.py-9]: process started with pid [15342]
[INFO] [static_transform_publisher-10]: process started with pid [15378]
[INFO] [aurora930_node-11]: process started with pid [15380]
[INFO] [qr_decoder-12]: process started with pid [15382]
[INFO] [qr_decision-13]: process started with pid [15384]
[INFO] [vision_ai_node-14]: process started with pid [15388]
[origincar_base_node-1] [INFO] [1782382270.878815619] [origincar_base]: origincar_base serial port opened
[lslidar_driver_node-2] [INFO] [1782382270.870755686] [lslidar_driver_node]: Lidar is N10
[lslidar_driver_node-2] [INFO] [1782382270.881615999] [lslidar_driver_node]: Initialised lslidar without error
[lslidar_driver_node-2] [INFO] [1782382270.881774749] [lslidar_driver_node]: Successfully initialize driver...
[robot_state_publisher-3] [INFO] [1782382270.906694800] [robot_state_publisher]: got segment base_footprint
[robot_state_publisher-3] [INFO] [1782382270.907101884] [robot_state_publisher]: got segment base_link
[robot_state_publisher-3] [INFO] [1782382270.907211384] [robot_state_publisher]: got segment gyro_link
[robot_state_publisher-3] [INFO] [1782382270.907702219] [robot_state_publisher]: got segment laser_link
[ekf_node-7] Both imu1_differential and imu1_relative were set to true. Using differential mode.
[static_transform_publisher-10] [INFO] [1782382271.148574122] [depth_camera_tf]: Spinning until stopped - publishing transform
[static_transform_publisher-10] translation: ('0.140000', '0.000000', '0.050000')
[static_transform_publisher-10] rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
[static_transform_publisher-10] from 'base_link' to 'depth_camera_link'
[aurora930_node-11] W0625 18:11:11.645052 15380 ros2_node.cc:35] hello aurora 900/930
[aurora930_node-11] 2026-06-25 18:11:11.740 (   0.176s) [        94B94020] device_manager_impl.cc:89    INFO| hotplug has registed by user
[aurora930_node-11] device_count==========1
[aurora930_node-11] I0625 18:11:11.804227 15380 aurora900_ros2_device.cc:153] BOOT_ORDER_1::Found 1 deptrum device
[aurora930_node-11] I0625 18:11:11.804754 15380 aurora900_ros2_device.cc:162] BOOT_ORDER_1::No serial number provided: picking first device
[aurora930_node-11] 2026-06-25 18:11:11.804 (   0.240s) [        94B94020] device_manager_impl.cc:318   INFO| Device information:
[aurora930_node-11]     ir_pid:0x1930, rgb_pid:0x0
[aurora930_node-11]     serial number:HY400529001015314G00248
[aurora930_node-11] I0625 18:11:11.804927 15380 aurora900_ros2_device.cc:206] BOOT_ORDER_1::0:device start opening
[aurora930_node-11] 2026-06-25 18:11:11.806 (   0.242s) [        94B94020]   custom_usb_device.cc:101   INFO| bulk in endpoint addr:129
[aurora930_node-11] 2026-06-25 18:11:11.806 (   0.242s) [        94B94020]   custom_usb_device.cc:98    INFO| bulk out endpoint addr:2
[aurora930_node-11] 2026-06-25 18:11:11.827 (   0.262s) [        94B94020]deptrum_camera_aurora93:53    INFO| doe_broken:0 ito_support:1 crash_count:0 wdt_count:0 hard_reset_count:2 heart_boot_count:0 boot_total:109 last_crash_time:N
[aurora930_node-11] I0625 18:11:11.827368 15380 aurora900_ros2_device.cc:247] device supported frame_mode:
[aurora930_node-11] I0625 18:11:11.827486 15380 aurora900_ros2_device.cc:252] [0]:ir_mode:=13 kRes320x200Ir8Bit rgb_mode:=31 kRes320x200RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0625 18:11:11.827539 15380 aurora900_ros2_device.cc:252] [1]:ir_mode:=17 kRes480x300Depth16Bit rgb_mode:=32 kRes480x300RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0625 18:11:11.827574 15380 aurora900_ros2_device.cc:252] [2]:ir_mode:=20 kRes640x400Ir8Bit rgb_mode:=33 kRes640x400RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0625 18:11:11.827605 15380 aurora900_ros2_device.cc:266] current set mode ir_mode:20:kRes640x400Ir8Bit,rgb_mode:33:kRes640x400RgbYuv
[qr_decoder-12] [INFO] [1782382272.066271392] [qr_decoder_zbar]: QR decoder (ZBar) started: rgb=/aurora/rgb/image_raw, depth=/aurora/depth/image_raw, filter=on, range=[50, 4000]mm, min_qr_len=1, intrinsics: fx=421.3 fy=422.3 cx=320.3 cy=197.0
[INFO] [map_server-15]: process started with pid [15478]
[INFO] [costmap_filter_info_server-16]: process started with pid [15480]
[INFO] [lifecycle_manager-17]: process started with pid [15482]
[costmap_filter_info_server-16] [INFO] [1782382272.300395906] [costmap_filter_info_server]: This is costmap filter info publisher
[aurora930_node-11] I0625 18:11:12.367715 15380 aurora900_ros2_device.cc:387] Switch Auto Exposure
[lifecycle_manager-17] [INFO] [1782382272.396987392] [lifecycle_manager_keepout]: Creating
[aurora930_node-11] 2026-06-25 18:11:12.434 (   0.870s) [        94B94020]      aurora900_impl.cc:1106  INFO| SetHeartbeat user set heartbeat enable: 0
[map_server-15] [INFO] [1782382272.440597480] [keepout_mask_server]:
[map_server-15]         keepout_mask_server lifecycle node launched.
[map_server-15]         Waiting on external lifecycle transitions to activate
[map_server-15]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[map_server-15] [INFO] [1782382272.442121692] [keepout_mask_server]: Creating
[lifecycle_manager-17] [INFO] [1782382272.474262423] [lifecycle_manager_keepout]: Creating and initializing lifecycle service clients
[costmap_filter_info_server-16] [INFO] [1782382272.527962823] [keepout_filter_info_server]:
[costmap_filter_info_server-16]         keepout_filter_info_server lifecycle node launched.
[costmap_filter_info_server-16]         Waiting on external lifecycle transitions to activate
[costmap_filter_info_server-16]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[lifecycle_manager-17] [INFO] [1782382272.554984336] [lifecycle_manager_keepout]: Starting managed nodes bringup...
[lifecycle_manager-17] [INFO] [1782382272.562418268] [lifecycle_manager_keepout]: Configuring keepout_mask_server
[map_server-15] [INFO] [1782382272.567875154] [keepout_mask_server]: Configuring
[map_server-15] [INFO] [1782382272.568189946] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.yaml
[map_server-15] [INFO] [1782382272.569379240] [map_io]: resolution: 0.05
[map_server-15] [INFO] [1782382272.569476282] [map_io]: origin[0]: -2.65
[map_server-15] [INFO] [1782382272.569507615] [map_io]: origin[1]: -4.5
[map_server-15] [INFO] [1782382272.569535532] [map_io]: origin[2]: 0
[map_server-15] [INFO] [1782382272.569564282] [map_io]: free_thresh: 0.5
[map_server-15] [INFO] [1782382272.569592907] [map_io]: occupied_thresh: 0.5
[map_server-15] [INFO] [1782382272.569631990] [map_io]: mode: scale
[map_server-15] [INFO] [1782382272.569662824] [map_io]: negate: 0
[map_server-15] [INFO] [1782382272.570388117] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm
[map_server-15] [INFO] [1782382272.629043694] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm: 163 X 141 map @ 0.05 m/cell
[lifecycle_manager-17] [INFO] [1782382272.689015648] [lifecycle_manager_keepout]: Configuring keepout_filter_info_server
[costmap_filter_info_server-16] [INFO] [1782382272.690539443] [keepout_filter_info_server]: Configuring
[lifecycle_manager-17] [INFO] [1782382272.715191242] [lifecycle_manager_keepout]: Activating keepout_mask_server
[map_server-15] [INFO] [1782382272.717384913] [keepout_mask_server]: Activating
[map_server-15] [INFO] [1782382272.717756622] [keepout_mask_server]: Creating bond (keepout_mask_server) to lifecycle manager.
[lifecycle_manager-17] [INFO] [1782382272.832518771] [lifecycle_manager_keepout]: Server keepout_mask_server connected with bond.
[lifecycle_manager-17] [INFO] [1782382272.832733688] [lifecycle_manager_keepout]: Activating keepout_filter_info_server
[costmap_filter_info_server-16] [INFO] [1782382272.833740523] [keepout_filter_info_server]: Activating
[costmap_filter_info_server-16] [INFO] [1782382272.833971607] [keepout_filter_info_server]: Creating bond (keepout_filter_info_server) to lifecycle manager.
[aurora930_node-11] I0625 18:11:12.865414 15380 aurora900_ros2_device.cc:304] BOOT_ORDER_1::Device information:
[aurora930_node-11] I0625 18:11:12.865594 15380 aurora900_ros2_device.cc:305]    sdk version: 1.1.22
[aurora930_node-11] I0625 18:11:12.865679 15380 aurora900_ros2_device.cc:306]    device name: Aurora 930
[aurora930_node-11] I0625 18:11:12.865721 15380 aurora900_ros2_device.cc:307]    serial number: HY400529001015314G00248
[aurora930_node-11] I0625 18:11:12.865756 15380 aurora900_ros2_device.cc:308]    firmware version: 1.7.2
[aurora930_node-11] I0625 18:11:12.865814 15380 camera_parameters.cc:134] BOOT_ORDER_1::Camera Parameters:
[aurora930_node-11] I0625 18:11:12.865847 15380 camera_parameters.cc:135] BOOT_ORDER_1::         Ir Intrinsics:
[aurora930_node-11] I0625 18:11:12.865875 15380 camera_parameters.cc:146]                Resolution:
[aurora930_node-11] I0625 18:11:12.865903 15380 camera_parameters.cc:147]                        Rows:400
[aurora930_node-11] I0625 18:11:12.865929 15380 camera_parameters.cc:148]                        Cols:640
[aurora930_node-11] I0625 18:11:12.865954 15380 camera_parameters.cc:149]                Intrinsics:
[aurora930_node-11] I0625 18:11:12.866010 15380 camera_parameters.cc:150]                        fx: 421.307
[aurora930_node-11] I0625 18:11:12.866130 15380 camera_parameters.cc:151]                        fy: 422.254
[aurora930_node-11] I0625 18:11:12.866171 15380 camera_parameters.cc:152]                        cx: 320.27
[aurora930_node-11] I0625 18:11:12.866207 15380 camera_parameters.cc:153]                        cy: 197.01
[aurora930_node-11] I0625 18:11:12.866240 15380 camera_parameters.cc:154]                        k1: 0.0606853
[aurora930_node-11] I0625 18:11:12.866273 15380 camera_parameters.cc:155]                        k2: -0.10961
[aurora930_node-11] I0625 18:11:12.866305 15380 camera_parameters.cc:156]                        p1: 0.00126689
[aurora930_node-11] I0625 18:11:12.866338 15380 camera_parameters.cc:157]                        p2: -0.00120539
[aurora930_node-11] I0625 18:11:12.866369 15380 camera_parameters.cc:158]                        k3: 0.0522281
[aurora930_node-11] I0625 18:11:12.866412 15380 camera_parameters.cc:138] BOOT_ORDER_1::         Rgb Intrinsics:
[aurora930_node-11] I0625 18:11:12.871826 15380 camera_parameters.cc:146]                Resolution:
[aurora930_node-11] I0625 18:11:12.871984 15380 camera_parameters.cc:147]                        Rows:400
[aurora930_node-11] I0625 18:11:12.872056 15380 camera_parameters.cc:148]                        Cols:640
[aurora930_node-11] I0625 18:11:12.872097 15380 camera_parameters.cc:149]                Intrinsics:
[aurora930_node-11] I0625 18:11:12.872130 15380 camera_parameters.cc:150]                        fx: 416.49
[aurora930_node-11] I0625 18:11:12.872193 15380 camera_parameters.cc:151]                        fy: 417.383
[aurora930_node-11] I0625 18:11:12.872246 15380 camera_parameters.cc:152]                        cx: 316.832
[aurora930_node-11] I0625 18:11:12.872287 15380 camera_parameters.cc:153]                        cy: 188.753
[aurora930_node-11] I0625 18:11:12.872329 15380 camera_parameters.cc:154]                        k1: 0.00611878
[aurora930_node-11] I0625 18:11:12.872364 15380 camera_parameters.cc:155]                        k2: -0.0490436
[aurora930_node-11] I0625 18:11:12.872401 15380 camera_parameters.cc:156]                        p1: 0.000399548
[aurora930_node-11] I0625 18:11:12.872434 15380 camera_parameters.cc:157]                        p2: 0.000563892
[aurora930_node-11] I0625 18:11:12.872465 15380 camera_parameters.cc:158]                        k3: 0.0308458
[aurora930_node-11] I0625 18:11:12.872504 15380 camera_parameters.cc:141] BOOT_ORDER_1::         Ir to Rgb Extrinsic:
[aurora930_node-11] I0625 18:11:12.872532 15380 camera_parameters.cc:162]                Extrinsics:
[aurora930_node-11] I0625 18:11:12.872558 15380 camera_parameters.cc:163]                        Rotation[0]: 0.999973, 0.00724076, -0.00112023
[aurora930_node-11] I0625 18:11:12.872602 15380 camera_parameters.cc:165]                        Rotation[1]: -0.00724006, 0.999973, 0.000633162
[aurora930_node-11] I0625 18:11:12.872639 15380 camera_parameters.cc:167]                        Rotation[2]: 0.00112478, -0.000625033, 0.999999
[aurora930_node-11] I0625 18:11:12.872761 15380 camera_parameters.cc:169]                        Translation: -9.88662, 0.117748, 0.603513
[aurora930_node-11] 2026-06-25 18:11:12.873 (   1.309s) [        94B94020]      aurora900_impl.cc:578   INFO| stream_mask_:0, rgb_stream_count_:1
[bmi088_iio_bridge.py-5] [INFO] [1782382272.923584829] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1782382272.928648881] [bmi088_iio_bridge]:   DIAGNOSTIC: Scanning IIO devices under /sys/bus/iio/devices/
[bmi088_iio_bridge.py-5] [INFO] [1782382272.936656314] [bmi088_iio_bridge]:   Equivalent to: ls /sys/bus/iio/devices/*/name
[bmi088_iio_bridge.py-5] [INFO] [1782382272.946099875] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1782382272.954075057] [bmi088_iio_bridge]:   iio:device0/name = "34190000.adc"
[lifecycle_manager-17] [INFO] [1782382272.942045408] [lifecycle_manager_keepout]: Server keepout_filter_info_server connected with bond.
[lifecycle_manager-17] [INFO] [1782382272.942206492] [lifecycle_manager_keepout]: Managed nodes are active
[lifecycle_manager-17] [INFO] [1782382272.942274950] [lifecycle_manager_keepout]: Creating bond timer...
[bmi088_iio_bridge.py-5] [INFO] [1782382272.970511841] [bmi088_iio_bridge]:   iio:device1/name = "bmi08x"
[bmi088_iio_bridge.py-5] [INFO] [1782382272.973181138] [bmi088_iio_bridge]:   trigger0/name = "34190000.adc-dev0"
[bmi088_iio_bridge.py-5] [INFO] [1782382272.975651893] [bmi088_iio_bridge]:   Total IIO devices found: 3
[imu_madgwick_filter.py-6] [INFO] [1782382272.975095683] [imu_madgwick_bmi088]: [imu_madgwick] init: beta=0.0030, gyro_noise=0.0002, accel_noise=0.010
[bmi088_iio_bridge.py-5] [INFO] [1782382272.983060116] [bmi088_iio_bridge]:   BMI088 kernel module APPEARS LOADED: 1 BMI device(s) detected
[bmi088_iio_bridge.py-5] [INFO] [1782382272.991472008] [bmi088_iio_bridge]:   BMI device names: ['bmi08x']
[bmi088_iio_bridge.py-5] [INFO] [1782382272.996819560] [bmi088_iio_bridge]:   gyro:  /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_anglvel is_si=False scale_override=0.00053
[bmi088_iio_bridge.py-5] [INFO] [1782382273.001120861] [bmi088_iio_bridge]:   accel: /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_accel is_si=False scale_override=0.00341
[imu_madgwick_filter.py-4] [INFO] [1782382273.113966296] [imu_madgwick_filter]: [imu_madgwick] init: beta=0.0330, gyro_noise=0.0010, accel_noise=0.050
[velocity_pid.py-9] [INFO] [1782382273.116483301] [velocity_pid]: VelocityPID 就绪: vx(Kp=0.8, Ki=0.60, Kd=0.05, max_i=0.68) wz(Kp=1.0, Ki=0.40, Kd=0.02, max_i=2.24) | feedback_timeout=0.5s
[imu_madgwick_filter.py-4] [INFO] [1782382273.119249849] [imu_madgwick_filter]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-4] [INFO] [1782382273.132726834] [imu_madgwick_filter]: [imu_madgwick] accel init: roll=-0.2deg, pitch=-0.1deg
[bmi088_iio_bridge.py-5] [INFO] [1782382273.185625524] [bmi088_iio_bridge]: BMI088 IIO Bridge 启动 @ 100Hz -> /imu_data  [OK]
[aurora930_node-11] 2026-06-25 18:11:13.210 (   1.646s) [        7D1D37E0]deptrum_camera_aurora93:407    ERR| recv first frame time is 1782382273210
[imu_madgwick_filter.py-6] [INFO] [1782382273.212374536] [imu_madgwick_bmi088]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-6] [INFO] [1782382273.215298000] [imu_madgwick_bmi088]: [imu_madgwick] accel init: roll=-2.1deg, pitch=-3.5deg
[cmd_vel_mux.py-8] [INFO] [1782382273.223076433] [cmd_vel_mux]:   nav: /nav_cmd_vel priority=10 timeout=0.5s
[cmd_vel_mux.py-8] [INFO] [1782382273.240805927] [cmd_vel_mux]:   pid: /pid_cmd_vel priority=20 timeout=0.3s
[cmd_vel_mux.py-8] [INFO] [1782382273.259249672] [cmd_vel_mux]:   stop: /stop_cmd_vel priority=255 timeout=0.5s
[cmd_vel_mux.py-8] [INFO] [1782382273.274687453] [cmd_vel_mux]: cmd_vel_mux 就绪: 输出 → /cmd_vel_muxed
[cmd_vel_mux.py-8] [INFO] [1782382273.309413398] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[INFO] [component_container_isolated-18]: process started with pid [15668]
[velocity_pid.py-9] [INFO] [1782382273.310557525] [velocity_pid]: [vel_pid] ACTIVATED vx=0.00 wz=0.00
[qr_decision-13] [INFO] [1782382273.730969789] [qr_decision]: qr_decision started: cooldown=3.0s, awaiting /sign from qr_decoder
[lslidar_driver_node-2] port = /dev/ttyACM1, baud_rate = 230400
[lslidar_driver_node-2] open_port /dev/ttyACM1 OK !
[vision_ai_node-14] [INFO] [1782382277.323368753] [vision_ai_node]: 成功加载配置文件: /userdata/dev_ws/install/racing_vision_ai/share/racing_vision_ai/config/vision_ai_config.yaml
[vision_ai_node-14] [INFO] [1782382277.726257435] [vision_ai_node]: Volcengine Ark client initialized successfully
[vision_ai_node-14] [INFO] [1782382277.748467937] [vision_ai_node]: Vision AI Node initialized
[vision_ai_node-14] [INFO] [1782382277.751553360] [vision_ai_node]: Waiting for sign4return=100 signal...
[vision_ai_node-14] [INFO] [1782382277.754470283] [vision_ai_node]: Results will be published to vlm_result
[bmi088_iio_bridge.py-5] [INFO] [1782382278.867941593] [bmi088_iio_bridge]:   gyro bias calibrated: (0.002676, 0.001206, -0.002745) rad/s
[INFO] [competition_master_stage3.py-19]: process started with pid [15671]
[INFO] [rviz2-20]: process started with pid [15680]
[component_container_isolated-18] [INFO] [1782382279.371494599] [nav2_container]: Load Library: /opt/ros/humble/lib/libcontroller_server_core.so
[component_container_isolated-18] [INFO] [1782382279.404200706] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-18] [INFO] [1782382279.405064916] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-18] [INFO] [1782382279.488730083] [controller_server]:
[component_container_isolated-18]       controller_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782382279.517964642] [controller_server]: Creating controller server
[component_container_isolated-18] [INFO] [1782382279.605974359] [local_costmap.local_costmap]:
[component_container_isolated-18]       local_costmap lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782382279.610316118] [local_costmap.local_costmap]: Creating Costmap
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/controller_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782382279.649221362] [nav2_container]: Load Library: /opt/ros/humble/lib/libmap_server_core.so
[component_container_isolated-18] [INFO] [1782382279.704708181] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::CostmapFilterInfoServer>
[component_container_isolated-18] [INFO] [1782382279.704896723] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapSaver>
[component_container_isolated-18] [INFO] [1782382279.704954349] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-18] [INFO] [1782382279.705004015] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-18] [INFO] [1782382279.763906133] [map_server]:
[component_container_isolated-18]       map_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782382279.764224884] [map_server]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/map_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782382279.771503565] [nav2_container]: Load Library: /opt/ros/humble/lib/libsmoother_server_core.so
[component_container_isolated-18] [INFO] [1782382279.780908917] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-18] [INFO] [1782382279.781077751] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-18] [INFO] [1782382279.864033291] [smoother_server]:
[component_container_isolated-18]       smoother_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782382279.883028288] [smoother_server]: Creating smoother server
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/smoother_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782382279.895891105] [nav2_container]: Load Library: /opt/ros/humble/lib/libamcl_core.so
[component_container_isolated-18] [INFO] [1782382279.908036046] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-18] [INFO] [1782382279.908210838] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-18] [INFO] [1782382279.999232645] [amcl]:
[component_container_isolated-18]       amcl lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782382280.001596149] [amcl]: Creating
[component_container_isolated-18] [INFO] [1782382280.089655367] [nav2_container]: Load Library: /opt/ros/humble/lib/libplanner_server_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/amcl' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782382280.093341457] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-18] [INFO] [1782382280.093508583] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-18] [INFO] [1782382280.166631937] [planner_server]:
[component_container_isolated-18]       planner_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782382280.177727667] [planner_server]: Creating
[component_container_isolated-18] [INFO] [1782382280.255368739] [global_costmap.global_costmap]:
[component_container_isolated-18]       global_costmap lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782382280.257682618] [global_costmap.global_costmap]: Creating Costmap
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/planner_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782382280.289083973] [nav2_container]: Load Library: /opt/ros/humble/lib/libnav2_lifecycle_manager_core.so
[component_container_isolated-18] [INFO] [1782382280.292538563] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1782382280.292715396] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1782382280.357401859] [lifecycle_manager_localization]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_localization' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782382280.382187908] [lifecycle_manager_localization]: Creating and initializing lifecycle service clients
[component_container_isolated-18] [INFO] [1782382280.382700326] [nav2_container]: Load Library: /opt/ros/humble/lib/libbehavior_server_core.so
[component_container_isolated-18] [INFO] [1782382280.408743670] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-18] [INFO] [1782382280.409022337] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-18] [INFO] [1782382280.459915313] [lifecycle_manager_localization]: Starting managed nodes bringup...
[component_container_isolated-18] [INFO] [1782382280.460325147] [lifecycle_manager_localization]: Configuring map_server
[component_container_isolated-18] [INFO] [1782382280.462630694] [map_server]: Configuring
[component_container_isolated-18] [INFO] [1782382280.463219528] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.yaml
[component_container_isolated-18] [INFO] [1782382280.472266880] [map_io]: resolution: 0.05
[component_container_isolated-18] [INFO] [1782382280.472402130] [map_io]: origin[0]: -2.65
[component_container_isolated-18] [INFO] [1782382280.472436255] [map_io]: origin[1]: -4.5
[component_container_isolated-18] [INFO] [1782382280.472464422] [map_io]: origin[2]: 0
[component_container_isolated-18] [INFO] [1782382280.472493463] [map_io]: free_thresh: 0.25
[component_container_isolated-18] [INFO] [1782382280.472522630] [map_io]: occupied_thresh: 0.65
[component_container_isolated-18] [INFO] [1782382280.472570797] [map_io]: mode: trinary
[component_container_isolated-18] [INFO] [1782382280.472601839] [map_io]: negate: 0
[component_container_isolated-18] [INFO] [1782382280.475349636] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm
[component_container_isolated-18] [INFO] [1782382280.517029385] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm: 163 X 141 map @ 0.05 m/cell
[component_container_isolated-18] [INFO] [1782382280.562143559] [lifecycle_manager_localization]: Configuring amcl
[component_container_isolated-18] [INFO] [1782382280.563100352] [amcl]: Configuring
[component_container_isolated-18] [INFO] [1782382280.563688187] [amcl]: initTransforms
[component_container_isolated-18] [INFO] [1782382280.572319454] [behavior_server]:
[component_container_isolated-18]       behavior_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/behavior_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782382280.645612142] [amcl]: initPubSub
[component_container_isolated-18] [INFO] [1782382280.652357905] [nav2_container]: Load Library: /opt/ros/humble/lib/libbt_navigator_core.so
[component_container_isolated-18] [INFO] [1782382280.674284991] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-18] [INFO] [1782382280.674470199] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-18] [INFO] [1782382280.698213580] [amcl]: Subscribed to map topic.
[component_container_isolated-18] [INFO] [1782382280.721779169] [lifecycle_manager_localization]: Activating map_server
[component_container_isolated-18] [INFO] [1782382280.722702546] [map_server]: Activating
[component_container_isolated-18] [INFO] [1782382280.723182380] [map_server]: Creating bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382280.723736006] [amcl]: Received a 163 X 141 map @ 0.050 m/pix
[component_container_isolated-18] [INFO] [1782382280.830497261] [bt_navigator]:
[component_container_isolated-18]       bt_navigator lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782382280.830850803] [bt_navigator]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/bt_navigator' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782382280.838135276] [lifecycle_manager_localization]: Server map_server connected with bond.
[component_container_isolated-18] [INFO] [1782382280.838304109] [lifecycle_manager_localization]: Activating amcl
[component_container_isolated-18] [INFO] [1782382280.839180778] [amcl]: Activating
[component_container_isolated-18] [INFO] [1782382280.839416278] [amcl]: initialPoseReceived
[component_container_isolated-18] [INFO] [1782382280.839891238] [amcl]: Setting pose (1782382280.839886): -1.985 -0.014 0.262
[component_container_isolated-18] [INFO] [1782382280.842920285] [amcl]: Creating bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382280.856412479] [nav2_container]: Load Library: /opt/ros/humble/lib/libwaypoint_follower_core.so
[component_container_isolated-18] [INFO] [1782382280.859385235] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-18] [INFO] [1782382280.859554985] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-18] [INFO] [1782382280.864466245] [amcl]: createLaserObject
[component_container_isolated-18] [INFO] [1782382280.961837272] [lifecycle_manager_localization]: Server amcl connected with bond.
[component_container_isolated-18] [INFO] [1782382280.962058231] [lifecycle_manager_localization]: Managed nodes are active
[component_container_isolated-18] [INFO] [1782382280.962186523] [lifecycle_manager_localization]: Creating bond timer...
[component_container_isolated-18] [INFO] [1782382280.983208482] [waypoint_follower]:
[component_container_isolated-18]       waypoint_follower lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782382280.985785862] [waypoint_follower]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/waypoint_follower' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782382281.006811779] [nav2_container]: Load Library: /opt/ros/humble/lib/libvelocity_smoother_core.so
[component_container_isolated-18] [INFO] [1782382281.010534203] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-18] [INFO] [1782382281.010712578] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-18] [INFO] [1782382281.098899921] [velocity_smoother]:
[component_container_isolated-18]       velocity_smoother lifecycle node launched.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/velocity_smoother' in container '/nav2_container'
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1782382281.111462862] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1782382281.111637738] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1782382281.181817711] [lifecycle_manager_navigation]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_navigation' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1782382281.204990715] [lifecycle_manager_navigation]: Creating and initializing lifecycle service clients
[component_container_isolated-18] [INFO] [1782382281.281008450] [lifecycle_manager_navigation]: Starting managed nodes bringup...
[component_container_isolated-18] [INFO] [1782382281.287334171] [lifecycle_manager_navigation]: Configuring controller_server
[component_container_isolated-18] [INFO] [1782382281.291009553] [controller_server]: Configuring controller interface
[component_container_isolated-18] [INFO] [1782382281.292194264] [controller_server]: getting goal checker plugins..
[component_container_isolated-18] [INFO] [1782382281.293687183] [controller_server]: Controller frequency set to 10.0000Hz
[component_container_isolated-18] [INFO] [1782382281.294025892] [local_costmap.local_costmap]: Configuring
[component_container_isolated-18] [INFO] [1782382281.360234274] [local_costmap.local_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1782382281.403532611] [local_costmap.local_costmap]: Subscribed to Topics: scan aurora_points
[component_container_isolated-18] [INFO] [1782382281.526489897] [local_costmap.local_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1782382281.527888233] [local_costmap.local_costmap]: Using plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1782382281.553667034] [local_costmap.local_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1782382281.553871660] [local_costmap.local_costmap]: Using plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1782382281.570895360] [local_costmap.local_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1782382281.640397707] [controller_server]: Created progress_checker : progress_checker of type nav2_controller::SimpleProgressChecker
[component_container_isolated-18] [INFO] [1782382281.648860391] [controller_server]: Created goal checker : goal_checker of type nav2_controller::SimpleGoalChecker
[component_container_isolated-18] [INFO] [1782382281.658988369] [controller_server]: Controller Server has goal_checker  goal checkers available.
[component_container_isolated-18] [INFO] [1782382281.662378793] [controller_server]: Created controller : FollowPath of type nav2_regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1782382281.747062670] [controller_server]: Controller Server has FollowPath  controllers available.
[component_container_isolated-18] [INFO] [1782382281.814591221] [lifecycle_manager_navigation]: Configuring smoother_server
[component_container_isolated-18] [INFO] [1782382281.817247184] [smoother_server]: Configuring smoother server
[component_container_isolated-18] [INFO] [1782382281.910112244] [smoother_server]: Created smoother : SmoothPath of type nav2_constrained_smoother/ConstrainedSmoother
[component_container_isolated-18] [INFO] [1782382281.967871234] [smoother_server]: Smoother Server has SmoothPath  smoothers available.
[component_container_isolated-18] [INFO] [1782382282.009794776] [lifecycle_manager_navigation]: Configuring planner_server
[component_container_isolated-18] [INFO] [1782382282.011345279] [planner_server]: Configuring
[component_container_isolated-18] [INFO] [1782382282.011669947] [global_costmap.global_costmap]: Configuring
[component_container_isolated-18] [INFO] [1782382282.053460238] [global_costmap.global_costmap]: Using plugin "static_layer"
[component_container_isolated-18] [INFO] [1782382282.070859439] [global_costmap.global_costmap]: Subscribing to the map topic (/map) with transient local durability
[component_container_isolated-18] [INFO] [1782382282.079306498] [global_costmap.global_costmap]: Initialized plugin "static_layer"
[component_container_isolated-18] [INFO] [1782382282.079480206] [global_costmap.global_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1782382282.095158529] [global_costmap.global_costmap]: Subscribed to Topics: scan aurora_points
[competition_master_stage3.py-19] [INFO] [1782382282.152859352] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1782382282.156304318] [competition_master_stage3]: === [Stage 3] 总控节点初始化 ===
[competition_master_stage3.py-19] [INFO] [1782382282.159983491] [competition_master_stage3]:   QR点:    (0.41, -3.17, yaw=0.00)
[competition_master_stage3.py-19] [INFO] [1782382282.163242790] [competition_master_stage3]:   通道入口: (0.38, -1.10, yaw=0.00)
[competition_master_stage3.py-19] [INFO] [1782382282.166459629] [competition_master_stage3]:   P点:     (-1.99, -0.01, yaw=0.26)
[competition_master_stage3.py-19] [INFO] [1782382282.171654306] [competition_master_stage3]:   cruise_cw: 3 路点 → VLM=(3.12, -1.34)
[competition_master_stage3.py-19] [INFO] [1782382282.176263982] [competition_master_stage3]:   cruise_ccw: 3 路点 → VLM=(2.10, 0.92)
[component_container_isolated-18] [INFO] [1782382282.176769525] [global_costmap.global_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1782382282.176943650] [global_costmap.global_costmap]: Using plugin "keepout_filter"
[competition_master_stage3.py-19] [INFO] [1782382282.183909414] [competition_master_stage3]:   超时: total=180.0s QR=90.0s entry=60.0s cruise=180.0s vlm=30.0s return=120.0s
[competition_master_stage3.py-19] [INFO] [1782382282.187478254] [competition_master_stage3]:   回退QR方向: 逆时针
[competition_master_stage3.py-19] [INFO] [1782382282.191088345] [competition_master_stage3]:   VLM结果话题: vlm_result
[competition_master_stage3.py-19] [INFO] [1782382282.194569144] [competition_master_stage3]: ============================================================
[component_container_isolated-18] [INFO] [1782382282.193915892] [global_costmap.global_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1782382282.194454435] [global_costmap.global_costmap]: Using plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1782382282.212365346] [global_costmap.global_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1782382282.259392189] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 163 X 141 at 0.050000 m/pix
[component_container_isolated-18] [INFO] [1782382282.284388156] [planner_server]: Created global planner plugin GridBased of type nav2_smac_planner/SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1782382282.284609364] [planner_server]: Configuring GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1782382282.324824153] [planner_server]: Even sized heuristic lookup table size set 200.000000, increasing size by 1 to make odd
[imu_madgwick_filter.py-6] [INFO] [1782382282.738701851] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=401 q_w=0.9993 angle=4.2deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782382282.911114735] [imu_madgwick_filter]: [imu_madgwick ->] msgs=200 q_w=0.9989 angle=5.4deg beta=0.0330
[rviz2-20] [INFO] [1782382282.984097464] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-20] [INFO] [1782382282.984973965] [rviz2]: OpenGl version: 4.5 (GLSL 4.5)
[rviz2-20] [INFO] [1782382283.189342205] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-20] [INFO] [1782382285.453354237] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[rviz2-20] [ERROR] [1782382285.908953264] [rviz2]: Vertex Program:rviz/glsl120/indexed_8bit_image.vert Fragment Program:rviz/glsl120/indexed_8bit_image.frag GLSL link result :
[rviz2-20] active samplers with a different type refer to the same texture image unit
[qr_decoder-12] [INFO] [1782382289.028492259] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=200 last_qr_frame=-1 gap=-1 frames rejects=0
[imu_madgwick_filter.py-6] [INFO] [1782382292.739860138] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=939 q_w=0.9993 angle=4.2deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782382292.911134141] [imu_madgwick_filter]: [imu_madgwick ->] msgs=400 q_w=0.9955 angle=10.8deg beta=0.0330
[component_container_isolated-18] [INFO] [1782382296.111260151] [planner_server]: Configured plugin GridBased of type SmacPlannerHybrid with maximum iterations 1500, max on approach iterations 300, and not allowing unknown traversal. Tolerance 0.50.Using motion model: Reeds-Shepp.
[component_container_isolated-18] [INFO] [1782382296.112251987] [planner_server]: Planner Server has GridBased  planners available.
[component_container_isolated-18] [INFO] [1782382296.168664555] [lifecycle_manager_navigation]: Configuring behavior_server
[component_container_isolated-18] [INFO] [1782382296.169349181] [behavior_server]: Configuring
[component_container_isolated-18] [INFO] [1782382296.198645988] [behavior_server]: Creating behavior plugin spin of type nav2_behaviors/Spin
[component_container_isolated-18] [INFO] [1782382296.202229454] [behavior_server]: Configuring spin
[component_container_isolated-18] [INFO] [1782382296.236919980] [behavior_server]: Creating behavior plugin backup of type nav2_behaviors/BackUp
[component_container_isolated-18] [INFO] [1782382296.241082280] [behavior_server]: Configuring backup
[component_container_isolated-18] [INFO] [1782382296.293933633] [behavior_server]: Creating behavior plugin drive_on_heading of type nav2_behaviors/DriveOnHeading
[component_container_isolated-18] [INFO] [1782382296.297731848] [behavior_server]: Configuring drive_on_heading
[component_container_isolated-18] [INFO] [1782382296.350420451] [behavior_server]: Creating behavior plugin wait of type nav2_behaviors/Wait
[component_container_isolated-18] [INFO] [1782382296.355097127] [behavior_server]: Configuring wait
[component_container_isolated-18] [INFO] [1782382296.401253175] [lifecycle_manager_navigation]: Configuring bt_navigator
[component_container_isolated-18] [INFO] [1782382296.403063596] [bt_navigator]: Configuring
[competition_master_stage3.py-19] [INFO] [1782382296.659733513] [competition_master_stage3]: [LAUNCH] 发车阶段: 14.7s
[competition_master_stage3.py-19] [INFO] [1782382296.664306147] [competition_master_stage3]: >>> 系统就绪, 开始 Stage 3 导航
[competition_master_stage3.py-19] [INFO] [1782382296.668630197] [competition_master_stage3]: [状态机] INIT → NAV_TO_QR
[competition_master_stage3.py-19] [INFO] [1782382296.681868098] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-18] [INFO] [1782382296.881380029] [lifecycle_manager_navigation]: Configuring waypoint_follower
[component_container_isolated-18] [INFO] [1782382296.883267241] [waypoint_follower]: Configuring
[competition_master_stage3.py-19] [WARN] [1782382296.896912517] [competition_master_stage3]: 导航目标被拒绝, 3s 后重试...
[component_container_isolated-18] [INFO] [1782382296.969189533] [waypoint_follower]: Created waypoint_task_executor : wait_at_waypoint of type nav2_waypoint_follower::WaitAtWaypoint
[component_container_isolated-18] [INFO] [1782382296.980478930] [lifecycle_manager_navigation]: Configuring velocity_smoother
[component_container_isolated-18] [INFO] [1782382296.981568224] [velocity_smoother]: Configuring velocity smoother
[component_container_isolated-18] [INFO] [1782382297.012573826] [lifecycle_manager_navigation]: Activating controller_server
[component_container_isolated-18] [INFO] [1782382297.014246913] [controller_server]: Activating
[component_container_isolated-18] [INFO] [1782382297.014548372] [local_costmap.local_costmap]: Activating
[component_container_isolated-18] [INFO] [1782382297.014680580] [local_costmap.local_costmap]: Checking transform
[component_container_isolated-18] [INFO] [1782382297.015095248] [local_costmap.local_costmap]: start
[component_container_isolated-18] [INFO] [1782382297.028802316] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1782382297.038932086] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1782382297.039176420] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1782382297.046943852] [local_costmap.local_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[component_container_isolated-18] [INFO] [1782382297.240271812] [controller_server]: Activating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1782382297.240605271] [controller_server]: Creating bond (controller_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382297.356550413] [lifecycle_manager_navigation]: Server controller_server connected with bond.
[component_container_isolated-18] [INFO] [1782382297.356840456] [lifecycle_manager_navigation]: Activating smoother_server
[component_container_isolated-18] [INFO] [1782382297.358929376] [smoother_server]: Activating
[component_container_isolated-18] [INFO] [1782382297.359187377] [smoother_server]: Activating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1782382297.359349127] [smoother_server]: Creating bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382297.482211450] [lifecycle_manager_navigation]: Server smoother_server connected with bond.
[component_container_isolated-18] [INFO] [1782382297.482391200] [lifecycle_manager_navigation]: Activating planner_server
[component_container_isolated-18] [INFO] [1782382297.483363910] [planner_server]: Activating
[component_container_isolated-18] [INFO] [1782382297.483760161] [global_costmap.global_costmap]: Activating
[component_container_isolated-18] [INFO] [1782382297.483852245] [global_costmap.global_costmap]: Checking transform
[component_container_isolated-18] [INFO] [1782382297.484134412] [global_costmap.global_costmap]: start
[component_container_isolated-18] [INFO] [1782382297.502439656] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1782382297.513440927] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1782382297.513757428] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1782382297.526896745] [global_costmap.global_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[rviz2-20] [INFO] [1782382297.697708328] [rviz2]: Trying to create a map of size 60 x 60 using 1 swatches
[competition_master_stage3.py-19] [INFO] [1782382298.004039258] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.01,-0.02) yaw=17deg cmd=(vx=0.00 wz=0.00) elapsed=1.3s cpuFreq=1500MHz cpuT=71C cpu=80% mem=18%
[component_container_isolated-18] [INFO] [1782382298.513334249] [planner_server]: Activating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1782382298.517410799] [planner_server]: Creating bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382298.642247625] [lifecycle_manager_navigation]: Server planner_server connected with bond.
[component_container_isolated-18] [INFO] [1782382298.642441042] [lifecycle_manager_navigation]: Activating behavior_server
[component_container_isolated-18] [INFO] [1782382298.643697836] [behavior_server]: Activating
[component_container_isolated-18] [INFO] [1782382298.643836295] [behavior_server]: Activating spin
[component_container_isolated-18] [INFO] [1782382298.643994212] [behavior_server]: Activating backup
[component_container_isolated-18] [INFO] [1782382298.644085462] [behavior_server]: Activating drive_on_heading
[component_container_isolated-18] [INFO] [1782382298.644188504] [behavior_server]: Activating wait
[component_container_isolated-18] [INFO] [1782382298.644293129] [behavior_server]: Creating bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382298.765008031] [lifecycle_manager_navigation]: Server behavior_server connected with bond.
[component_container_isolated-18] [INFO] [1782382298.765202781] [lifecycle_manager_navigation]: Activating bt_navigator
[component_container_isolated-18] [INFO] [1782382298.766490325] [bt_navigator]: Activating
[component_container_isolated-18] [WARN] [1782382298.914104112] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1782382299.014548224] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1782382299.060665064] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[rviz2-20] [INFO] [1782382299.123772937] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[component_container_isolated-18] [WARN] [1782382299.196607620] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1782382299.420850472] [bt_navigator_navigate_to_pose_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [INFO] [1782382299.580672241] [bt_navigator]: Creating bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382299.699097680] [lifecycle_manager_navigation]: Server bt_navigator connected with bond.
[component_container_isolated-18] [INFO] [1782382299.699296638] [lifecycle_manager_navigation]: Activating waypoint_follower
[component_container_isolated-18] [INFO] [1782382299.708355948] [waypoint_follower]: Activating
[component_container_isolated-18] [INFO] [1782382299.708626782] [waypoint_follower]: Creating bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382299.830634227] [lifecycle_manager_navigation]: Server waypoint_follower connected with bond.
[component_container_isolated-18] [INFO] [1782382299.830814144] [lifecycle_manager_navigation]: Activating velocity_smoother
[component_container_isolated-18] [INFO] [1782382299.831918896] [velocity_smoother]: Activating
[component_container_isolated-18] [INFO] [1782382299.832255272] [velocity_smoother]: Creating bond (velocity_smoother) to lifecycle manager.
[competition_master_stage3.py-19] [INFO] [1782382299.904986455] [competition_master_stage3]: 重试发送导航目标 (QR点)...
[competition_master_stage3.py-19] [INFO] [1782382299.914361681] [competition_master_stage3]: [DIAG] nav目标距离: 3.97m, robot=(-2.01,-0.02) → target=(0.41,-3.17)
[competition_master_stage3.py-19] [INFO] [1782382299.921145820] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-18] [INFO] [1782382299.932160091] [bt_navigator]: Begin navigating from current location (-2.01, -0.02) to (0.41, -3.17)
[competition_master_stage3.py-19] [INFO] [1782382299.938553645] [competition_master_stage3]: 导航目标已接受，车辆出发...
[component_container_isolated-18] [INFO] [1782382299.956972139] [lifecycle_manager_navigation]: Server velocity_smoother connected with bond.
[component_container_isolated-18] [INFO] [1782382299.957152681] [lifecycle_manager_navigation]: Managed nodes are active
[component_container_isolated-18] [INFO] [1782382299.957217223] [lifecycle_manager_navigation]: Creating bond timer...
[competition_master_stage3.py-19] [INFO] [1782382300.013011248] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.01,-0.02) yaw=17deg cmd=(vx=0.00 wz=0.00) elapsed=3.3s cpuFreq=1500MHz cpuT=73C cpu=50% mem=18%
[component_container_isolated-18] [WARN] [1782382300.498398440] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.7828 Hz
[component_container_isolated-18] [INFO] [1782382300.634618829] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-18] [WARN] [1782382300.635261497] [controller_server]: No goal checker was specified in parameter 'current_goal_checker'. Server will use only plugin loaded goal_checker . This warning will appear once.
[cmd_vel_mux.py-8] [INFO] [1782382300.710190851] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=-0.12
[velocity_pid.py-9] [INFO] [1782382300.719802703] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.17 err=100.0%
[cmd_vel_mux.py-8] [INFO] [1782382301.610623472] [cmd_vel_mux]: [mux→] src=nav vx=0.49 wz=-1.67
[velocity_pid.py-9] [INFO] [1782382301.720147976] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.37 corrected=0.28 err=26.8%
[competition_master_stage3.py-19] [INFO] [1782382302.007877492] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.85,-0.00) yaw=-5deg cmd=(vx=0.50 wz=-1.29) elapsed=5.3s plan[29pts 4.1m] (-2.00,-0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=73C cpu=84% mem=18%
[component_container_isolated-18] Reallocing temp weights 301 - 60
[component_container_isolated-18] [WARN] [1782382302.496948563] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3497 Hz
[component_container_isolated-18] [INFO] [1782382302.635605207] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-6] [INFO] [1782382302.741872788] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1392 q_w=0.7577 angle=81.5deg beta=0.0030
[velocity_pid.py-9] [INFO] [1782382302.755928190] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.08 -> current=0.03 dt=0.0333s, resetting
[imu_madgwick_filter.py-4] [INFO] [1782382302.911366491] [imu_madgwick_filter]: [imu_madgwick ->] msgs=600 q_w=0.8424 angle=65.2deg beta=0.0330
[velocity_pid.py-9] [INFO] [1782382303.630421464] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.03 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1782382303.644748283] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.24
[velocity_pid.py-9] [INFO] [1782382303.756023665] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.11 -> current=-0.01 dt=0.0343s, resetting
[velocity_pid.py-9] [INFO] [1782382303.856310776] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0338s, resetting
[competition_master_stage3.py-19] [INFO] [1782382304.021712762] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.21,-0.75) yaw=-44deg cmd=(vx=-0.19 wz=-0.48) elapsed=7.3s plan[26pts 3.7m] (-1.50,-0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=73C cpu=83% mem=18%
[component_container_isolated-18] [WARN] [1782382304.492904672] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3201 Hz
[qr_decoder-12] [INFO] [1782382304.554947666] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=400 last_qr_frame=-1 gap=-1 frames rejects=0
[component_container_isolated-18] [INFO] [1782382304.635618739] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782382304.654235983] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.11 corrected=-0.28 err=63.0%
[cmd_vel_mux.py-8] [INFO] [1782382304.746522495] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.73
[velocity_pid.py-9] [INFO] [1782382304.852843325] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0338s, resetting
[velocity_pid.py-9] [INFO] [1782382305.654294162] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.24 corrected=0.35 err=51.6%
[competition_master_stage3.py-19] [INFO] [1782382306.009068804] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.21,-0.75) yaw=-44deg cmd=(vx=0.50 wz=-0.26) elapsed=9.3s plan[20pts 2.8m] (-1.10,-0.85)→(0.40,-3.15) cpuFreq=1500MHz cpuT=73C cpu=75% mem=18%
[component_container_isolated-18] [WARN] [1782382306.495809200] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3221 Hz
[component_container_isolated-18] [INFO] [1782382306.635657011] [controller_server]: Passing new path to controller.
[component_container_isolated-18] Reallocing temp weights 893 - 60
[velocity_pid.py-9] [INFO] [1782382307.620766739] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.04 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1782382307.645232703] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.08
[velocity_pid.py-9] [INFO] [1782382307.654562471] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.08 dt=0.0340s, resetting
[velocity_pid.py-9] [INFO] [1782382307.866382420] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0249s, resetting
[competition_master_stage3.py-19] [INFO] [1782382308.011838991] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.73,-1.51) yaw=-63deg cmd=(vx=-0.11 wz=-0.14) elapsed=11.3s plan[18pts 2.5m] (-0.90,-1.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=73C cpu=80% mem=18%
[qr_decoder-12] [INFO] [1782382308.414838599] [qr_decoder_zbar]: [qr_decoder] QR DETECTED frame=454 symbols=1 (gap=-1 frames)
[qr_decoder-12] [INFO] [1782382308.415076057] [qr_decoder_zbar]: [QR] 1584 | depth=0mm (advisory, publishing anyway)
[qr_decoder-12] [INFO] [1782382308.415558600] [qr_decoder_zbar]: [QR] 1584 | robot_pos: (0.50, -2.43, yaw=-1.80)
[qr_decision-13] [INFO] [1782382308.419491983] [qr_decision]: [QR] 1584 CCW @ (x=0.50, y=-2.43, yaw=-1.80) → /qr_event
[competition_master_stage3.py-19] [INFO] [1782382308.421104111] [competition_master_stage3]: [QR检测] 内容: 1584
[qr_decision-13] [INFO] [1782382308.422513572] [qr_decision]: [检查点] qr_decision 发布 /qr_event (由 task_manager 决定停车)
[competition_master_stage3.py-19] [INFO] [1782382308.438661519] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decoder_zbar
[competition_master_stage3.py-19] [INFO] [1782382308.445207782] [competition_master_stage3]: >>> QR 解码已关闭, 等待方向判断 (/qr_event)...
[competition_master_stage3.py-19] [INFO] [1782382308.450843043] [competition_master_stage3]: [QR检测] 取消当前导航目标, 等待BT完成 cancel/halt 清理...
[competition_master_stage3.py-19] [INFO] [1782382308.470253580] [competition_master_stage3]: [QR事件] 方向: 逆时针 (通道巡航阶段使用)
[qr_decoder-12] [INFO] [1782382308.480016682] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-18] [WARN] [1782382308.492075414] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3242 Hz
[competition_master_stage3.py-19] [INFO] [1782382308.495307837] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decision
[component_container_isolated-18] [INFO] [1782382308.635615356] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-18] [INFO] [1782382308.635809606] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1782382308.636398024] [bt_navigator]: [navigate_to_pose] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1782382308.637711527] [bt_navigator]: Goal canceled
[velocity_pid.py-9] [INFO] [1782382308.639664989] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.10 corrected=-0.31 err=67.3%
[competition_master_stage3.py-19] [INFO] [1782382308.653307265] [competition_master_stage3]: [结果回调] BT取消确认完成 (STATUS_CANCELED), 准备发送通道入口目标...
[competition_master_stage3.py-19] [INFO] [1782382308.657139064] [competition_master_stage3]: [状态机] NAV_TO_QR → BACKING_UP
[competition_master_stage3.py-19] [INFO] [1782382308.663109992] [competition_master_stage3]: >>> BT取消完成, 右后退摆正车头→前进进通道...
[competition_master_stage3.py-19] [INFO] [1782382308.668943503] [competition_master_stage3]: [BACKUP] 右后退中: vx=-0.15 wz=0.80, 持续 6.0s...
[cmd_vel_mux.py-8] [INFO] [1782382308.678155688] [cmd_vel_mux]: [mux→] src=nav vx=-0.15 wz=0.80
[velocity_pid.py-9] [INFO] [1782382308.696288181] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.80 dt=0.0348s, resetting
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
[INFO] [qr_decoder-12]: process has finished cleanly [pid 15382]
[cmd_vel_mux.py-8] [INFO] [1782382309.209766166] [cmd_vel_mux]: [mux→] src=nav vx=0.00 wz=0.00
[ERROR] [qr_decision-13]: process has died [pid 15384, exit code 1, cmd '/userdata/dev_ws/install/origincar_qr/lib/origincar_qr/qr_decision --ros-args -r __node:=qr_decision --params-file /tmp/launch_params_yudy8glh'].
[velocity_pid.py-9] [INFO] [1782382309.686595998] [velocity_pid]: [vel_pid→] desired=-0.15 actual=-0.06 corrected=-0.41 err=61.3%
[competition_master_stage3.py-19] [INFO] [1782382310.005930443] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.53,-1.74) yaw=-62deg cmd=(vx=-0.15 wz=0.80) elapsed=13.3s plan[12pts 1.6m] (-0.50,-1.85)→(0.40,-3.15) cpuFreq=1500MHz cpuT=73C cpu=100% mem=18%
[competition_master_stage3.py-19] [INFO] [1782382312.003266058] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.71,-1.48) yaw=-27deg cmd=(vx=-0.15 wz=0.80) elapsed=15.3s plan[12pts 1.6m] (-0.50,-1.85)→(0.40,-3.15) cpuFreq=1500MHz cpuT=72C cpu=50% mem=18%
[imu_madgwick_filter.py-6] [INFO] [1782382312.739498423] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1855 q_w=0.9839 angle=20.6deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782382312.911345877] [imu_madgwick_filter]: [imu_madgwick ->] msgs=800 q_w=0.9992 angle=4.5deg beta=0.0330
[competition_master_stage3.py-19] [INFO] [1782382314.007019218] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.98,-1.47) yaw=16deg cmd=(vx=-0.15 wz=0.80) elapsed=17.3s plan[12pts 1.6m] (-0.50,-1.85)→(0.40,-3.15) cpuFreq=1500MHz cpuT=72C cpu=75% mem=18%
[velocity_pid.py-9] [INFO] [1782382314.386007898] [velocity_pid]: [vel_pid→] desired=-0.15 actual=-0.18 corrected=-0.09 err=22.0%
[competition_master_stage3.py-19] [INFO] [1782382314.678173497] [competition_master_stage3]: [状态机] BACKING_UP → CRUISE_CHANNEL
[competition_master_stage3.py-19] [INFO] [1782382314.683034256] [competition_master_stage3]: [CRUISE] 方向: CCW (逆时针, even QR), 路点: (1.73,-1.98), (3.10,-1.35), (2.10,0.92)
[competition_master_stage3.py-19] [INFO] [1782382314.690555729] [competition_master_stage3]: [CRUISE] NavigateThroughPoses: (0.38,-1.10), (1.73,-1.98), (3.10,-1.35), (2.10,0.92)
[component_container_isolated-18] [INFO] [1782382314.705878674] [bt_navigator]: Begin navigating from current location through 4 poses to (2.10, 0.92)
[cmd_vel_mux.py-8] [INFO] [1782382314.709892099] [cmd_vel_mux]: [mux→] src=stop vx=0.00 wz=0.00
[competition_master_stage3.py-19] [INFO] [1782382314.716193944] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[cmd_vel_mux.py-8] [INFO] [1782382315.209352217] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.53s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1782382315.215919688] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[component_container_isolated-18] [WARN] [1782382315.517328886] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2471 Hz
[component_container_isolated-18] [INFO] [1782382315.712089507] [controller_server]: Received a goal, begin computing control effort.
[cmd_vel_mux.py-8] [INFO] [1782382315.742716565] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=-0.12
[velocity_pid.py-9] [INFO] [1782382315.755161547] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.08 err=100.0%
[competition_master_stage3.py-19] [INFO] [1782382316.003131769] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-1.07,-1.52) yaw=44deg cmd=(vx=0.38 wz=-0.62) elapsed=19.3s plan[64pts 8.7m] (-1.20,-1.65)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=71% mem=18%
[cmd_vel_mux.py-8] [INFO] [1782382316.647018201] [cmd_vel_mux]: [mux→] src=nav vx=0.50 wz=-1.58
[velocity_pid.py-9] [INFO] [1782382316.755543949] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.36 corrected=0.17 err=28.2%
[component_container_isolated-18] [WARN] [1782382317.510249383] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4324 Hz
[component_container_isolated-18] [INFO] [1782382317.712470725] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1782382318.005949949] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.69,-1.45) yaw=-4deg cmd=(vx=0.50 wz=0.60) elapsed=21.3s plan[61pts 8.1m] (-0.70,-1.45)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=60% mem=18%
[velocity_pid.py-9] [INFO] [1782382318.955470249] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.00 -> current=-0.12 dt=0.0335s, resetting
[velocity_pid.py-9] [INFO] [1782382318.961218093] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.52 corrected=-0.15 err=26.1%
[cmd_vel_mux.py-8] [INFO] [1782382319.009713768] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.25
[velocity_pid.py-9] [INFO] [1782382319.219649249] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0336s, resetting
[component_container_isolated-18] [WARN] [1782382319.509956882] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4321 Hz
[component_container_isolated-18] [INFO] [1782382319.712468766] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782382319.809269949] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.33
[velocity_pid.py-9] [INFO] [1782382319.918589323] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0332s, resetting
[velocity_pid.py-9] [INFO] [1782382319.985930992] [velocity_pid]: [vel_pid→] desired=0.14 actual=-0.08 corrected=0.18 err=157.8%
[competition_master_stage3.py-19] [INFO] [1782382320.003940568] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.01,-1.29) yaw=27deg cmd=(vx=0.14 wz=-0.53) elapsed=23.3s plan[55pts 7.3m] (0.10,-1.25)→(2.10,0.95) cpuFreq=1500MHz cpuT=72C cpu=83% mem=18%
[component_container_isolated-18] [WARN] [1782382321.503417319] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4455 Hz
[component_container_isolated-18] [INFO] [1782382321.612474692] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1782382322.005654476] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.73,-1.13) yaw=-7deg cmd=(vx=0.50 wz=-0.32) elapsed=25.3s plan[52pts 6.8m] (0.50,-1.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=33% mem=18%
[velocity_pid.py-9] [INFO] [1782382322.654070449] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.00 err=22.7%
[cmd_vel_mux.py-8] [INFO] [1782382322.710801723] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.24
[imu_madgwick_filter.py-6] [INFO] [1782382322.739076610] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2375 q_w=0.9192 angle=46.4deg beta=0.0030
[velocity_pid.py-9] [INFO] [1782382322.823372894] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.11 -> current=0.01 dt=0.0332s, resetting
[imu_madgwick_filter.py-4] [INFO] [1782382322.911132684] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1000 q_w=0.9859 angle=19.3deg beta=0.0330
[velocity_pid.py-9] [INFO] [1782382322.919190824] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0333s, resetting
[component_container_isolated-18] [WARN] [1782382323.504368719] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2630 Hz
[component_container_isolated-18] [INFO] [1782382323.612459089] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782382323.654440627] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.09 corrected=-0.09 err=56.7%
[cmd_vel_mux.py-8] [INFO] [1782382323.732339523] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.62
[velocity_pid.py-9] [INFO] [1782382323.819863688] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0333s, resetting
[competition_master_stage3.py-19] [INFO] [1782382324.003145159] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.28,-1.31) yaw=-32deg cmd=(vx=0.29 wz=0.67) elapsed=27.3s plan[46pts 6.2m] (1.40,-1.35)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=75% mem=18%
[velocity_pid.py-9] [INFO] [1782382324.655177594] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.27 corrected=0.35 err=45.2%
[cmd_vel_mux.py-8] [INFO] [1782382325.410361764] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.00
[velocity_pid.py-9] [INFO] [1782382325.455145807] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.00 -> current=-0.12 dt=0.0330s, resetting
[component_container_isolated-18] [WARN] [1782382325.500726434] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2680 Hz
[component_container_isolated-18] [INFO] [1782382325.612475227] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782382325.618615031] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0332s, resetting
[velocity_pid.py-9] [INFO] [1782382325.691728543] [velocity_pid]: [vel_pid→] desired=0.05 actual=0.43 corrected=-0.26 err=762.0%
[competition_master_stage3.py-19] [INFO] [1782382326.003710171] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.85,-1.48) yaw=-21deg cmd=(vx=0.37 wz=-1.17) elapsed=29.3s plan[44pts 5.7m] (1.60,-1.45)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=85% mem=18%
[cmd_vel_mux.py-8] [INFO] [1782382326.109274161] [cmd_vel_mux]: [mux→] src=nav vx=0.11 wz=-1.17
[velocity_pid.py-9] [INFO] [1782382326.218865367] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.02 -> current=-0.07 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1782382326.721477518] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.02 corrected=-0.35 err=93.7%
[component_container_isolated-18] [WARN] [1782382327.493224216] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1782382327.493462133] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (1.73, -1.98)
[component_container_isolated-18] [WARN] [1782382327.493586050] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1782382327.610266185] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1782382327.618177158] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1782382327.633689396] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1782382327.634122063] [behavior_server]: wait completed successfully
[component_container_isolated-18] [INFO] [1782382327.649659384] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1782382327.649860426] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1782382327.667363209] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[velocity_pid.py-9] [INFO] [1782382327.755014873] [velocity_pid]: [vel_pid→] desired=-0.18 actual=-0.28 corrected=0.05 err=57.6%
[cmd_vel_mux.py-8] [INFO] [1782382327.809679809] [cmd_vel_mux]: [mux→] src=nav vx=-0.09 wz=1.42
[velocity_pid.py-9] [INFO] [1782382327.854544893] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.09 -> current=0.00 dt=0.0337s, resetting
[competition_master_stage3.py-19] [INFO] [1782382328.002155253] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.84,-1.46) yaw=-22deg cmd=(vx=0.15 wz=1.04) elapsed=31.3s plan[44pts 5.7m] (1.60,-1.45)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=54% mem=18%
[velocity_pid.py-9] [INFO] [1782382328.420032827] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.08 dt=0.0329s, resetting
[component_container_isolated-18] [WARN] [1782382328.501483313] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.6974 Hz
[cmd_vel_mux.py-8] [INFO] [1782382328.511052665] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=0.17
[velocity_pid.py-9] [INFO] [1782382328.554503996] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.07 -> current=-0.02 dt=0.0334s, resetting
[component_container_isolated-18] [INFO] [1782382328.612479104] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782382328.790822397] [velocity_pid]: [vel_pid→] desired=-0.30 actual=0.03 corrected=-0.37 err=110.7%
[velocity_pid.py-9] [INFO] [1782382328.820096452] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.08 dt=0.0336s, resetting
[velocity_pid.py-9] [INFO] [1782382329.959241207] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.28 corrected=0.06 err=33.8%
[competition_master_stage3.py-19] [INFO] [1782382330.004969001] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.64,-1.41) yaw=-7deg cmd=(vx=-0.21 wz=-1.32) elapsed=33.3s plan[44pts 5.9m] (1.70,-1.45)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=70% mem=18%
[cmd_vel_mux.py-8] [INFO] [1782382330.009487218] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-1.20
[velocity_pid.py-9] [INFO] [1782382330.118627964] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0328s, resetting
[component_container_isolated-18] [WARN] [1782382330.499635259] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2690 Hz
[velocity_pid.py-9] [INFO] [1782382330.553647735] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.07 -> current=0.18 dt=0.0274s, resetting
[component_container_isolated-18] [INFO] [1782382330.612472178] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782382330.986987669] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.30 corrected=0.37 err=39.8%
[cmd_vel_mux.py-8] [INFO] [1782382331.909688974] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.88
[competition_master_stage3.py-19] [INFO] [1782382332.009700285] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.76,-1.63) yaw=-66deg cmd=(vx=0.23 wz=-0.76) elapsed=35.3s plan[44pts 5.8m] (1.50,-1.35)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=57% mem=18%
[velocity_pid.py-9] [INFO] [1782382332.020999098] [velocity_pid]: [vel_pid→] desired=0.14 actual=0.49 corrected=-0.17 err=250.0%
[velocity_pid.py-9] [INFO] [1782382332.122090495] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1782382332.320644073] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.01 -> current=0.12 dt=0.0307s, resetting
[component_container_isolated-18] [WARN] [1782382332.500292491] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2680 Hz
[component_container_isolated-18] [INFO] [1782382332.612472450] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782382332.710222591] [cmd_vel_mux]: [mux→] src=nav vx=-0.18 wz=0.62
[imu_madgwick_filter.py-6] [INFO] [1782382332.746523867] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2879 q_w=0.4416 angle=127.6deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782382332.912020967] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1200 q_w=0.6971 angle=91.6deg beta=0.0330
[velocity_pid.py-9] [INFO] [1782382332.952672792] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.12 -> current=-0.01 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1782382333.055115817] [velocity_pid]: [vel_pid→] desired=-0.18 actual=-0.10 corrected=-0.20 err=42.2%
[cmd_vel_mux.py-8] [INFO] [1782382333.509956746] [cmd_vel_mux]: [mux→] src=nav vx=0.00 wz=-0.88
[velocity_pid.py-9] [INFO] [1782382333.918935966] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.01 -> current=0.12 dt=0.0334s, resetting
[competition_master_stage3.py-19] [INFO] [1782382334.004216000] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.78,-1.84) yaw=-108deg cmd=(vx=0.38 wz=0.24) elapsed=37.3s plan[41pts 5.3m] (1.80,-1.95)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=50% mem=18%
[velocity_pid.py-9] [INFO] [1782382334.088543531] [velocity_pid]: [vel_pid→] desired=0.40 actual=0.05 corrected=0.22 err=88.9%
[cmd_vel_mux.py-8] [INFO] [1782382334.446348655] [cmd_vel_mux]: [mux→] src=nav vx=0.26 wz=1.49
[component_container_isolated-18] [WARN] [1782382334.502433217] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2754 Hz
[component_container_isolated-18] [INFO] [1782382334.612463089] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1782382336.008400556] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.80,-2.18) yaw=-65deg cmd=(vx=0.43 wz=1.67) elapsed=39.3s plan[38pts 5.4m] (1.80,-1.85)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=50% mem=18%
[velocity_pid.py-9] [INFO] [1782382336.052607680] [velocity_pid]: [vel_pid→] desired=0.34 actual=0.41 corrected=-0.17 err=20.4%
[cmd_vel_mux.py-8] [INFO] [1782382336.115801255] [cmd_vel_mux]: [mux→] src=nav vx=0.25 wz=1.42
[velocity_pid.py-9] [INFO] [1782382336.255681140] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.07 -> current=-0.02 dt=0.0333s, resetting
[component_container_isolated-18] [WARN] [1782382336.496972170] [planner_server]: GridBased: failed to create plan, no valid path found.
[component_container_isolated-18] [WARN] [1782382336.497227421] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (3.10, -1.35)
[component_container_isolated-18] [WARN] [1782382336.497332421] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1782382336.610242130] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1782382336.617364310] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1782382336.631821129] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1782382336.632121963] [behavior_server]: wait completed successfully
[component_container_isolated-18] [INFO] [1782382336.635800720] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1782382336.635962137] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1782382336.650879206] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[velocity_pid.py-9] [INFO] [1782382336.719514500] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.08 dt=0.0328s, resetting
[velocity_pid.py-9] [INFO] [1782382337.057891544] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.09 corrected=-0.33 err=69.7%
[component_container_isolated-18] [WARN] [1782382337.497909359] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.7073 Hz
[component_container_isolated-18] [INFO] [1782382337.612522113] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782382337.710081877] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.83
[velocity_pid.py-9] [INFO] [1782382337.819199704] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0332s, resetting
[competition_master_stage3.py-19] [INFO] [1782382338.007429552] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.08,-2.40) yaw=-29deg cmd=(vx=0.29 wz=-0.21) elapsed=41.3s plan[36pts 4.9m] (2.00,-2.35)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=66% mem=18%
[velocity_pid.py-9] [INFO] [1782382338.054492306] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.08 -> current=0.04 dt=0.0343s, resetting
[velocity_pid.py-9] [INFO] [1782382338.058840314] [velocity_pid]: [vel_pid→] desired=0.44 actual=-0.20 corrected=0.64 err=145.1%
[component_container_isolated-18] [WARN] [1782382339.518931889] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2397 Hz
[component_container_isolated-18] [INFO] [1782382339.712458163] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1782382340.002017365] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.34,-2.40) yaw=2deg cmd=(vx=0.50 wz=0.94) elapsed=43.3s plan[34pts 4.7m] (2.30,-2.45)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=63% mem=18%
[velocity_pid.py-9] [INFO] [1782382340.857733903] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.06 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1782382340.910837917] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.07
[velocity_pid.py-9] [INFO] [1782382341.119457052] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0331s, resetting
[component_container_isolated-18] [WARN] [1782382341.497405040] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2746 Hz
[component_container_isolated-18] [INFO] [1782382341.612466002] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782382341.712263978] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.13
[velocity_pid.py-9] [INFO] [1782382341.818924966] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0331s, resetting
[velocity_pid.py-9] [INFO] [1782382341.825722354] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.00 -> current=0.12 dt=0.0331s, resetting
[velocity_pid.py-9] [INFO] [1782382341.862491713] [velocity_pid]: [vel_pid→] desired=0.14 actual=-0.06 corrected=0.29 err=148.1%
[competition_master_stage3.py-19] [INFO] [1782382342.006213812] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.91,-1.90) yaw=62deg cmd=(vx=0.29 wz=0.50) elapsed=45.3s plan[27pts 3.5m] (3.00,-1.85)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=77% mem=18%
[imu_madgwick_filter.py-6] [INFO] [1782382342.741448207] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3372 q_w=0.8942 angle=53.2deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782382342.914066150] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1399 q_w=0.6733 angle=95.4deg beta=0.0330
[velocity_pid.py-9] [INFO] [1782382343.020453221] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.11 -> current=-0.01 dt=0.0334s, resetting
[cmd_vel_mux.py-8] [INFO] [1782382343.211133696] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.08
[velocity_pid.py-9] [INFO] [1782382343.220283963] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.48 corrected=-0.06 err=51.2%
[velocity_pid.py-9] [INFO] [1782382343.422750169] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0336s, resetting
[component_container_isolated-18] [WARN] [1782382343.495467427] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2757 Hz
[component_container_isolated-18] [INFO] [1782382343.612480809] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782382343.652629425] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.10 -> current=0.02 dt=0.0333s, resetting
[cmd_vel_mux.py-8] [INFO] [1782382343.809318546] [cmd_vel_mux]: [mux→] src=nav vx=0.06 wz=0.40
[velocity_pid.py-9] [INFO] [1782382343.818567147] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0332s, resetting
[competition_master_stage3.py-19] [INFO] [1782382344.006229033] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.07,-1.42) yaw=81deg cmd=(vx=0.29 wz=0.77) elapsed=47.3s plan[19pts 2.7m] (3.10,-1.35)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=75% mem=18%
[velocity_pid.py-9] [INFO] [1782382344.221388345] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.06 corrected=0.35 err=84.3%
[cmd_vel_mux.py-8] [INFO] [1782382344.778838911] [cmd_vel_mux]: [mux→] src=nav vx=0.50 wz=1.54
[component_container_isolated-18] [WARN] [1782382345.494931600] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2765 Hz
[component_container_isolated-18] [INFO] [1782382345.612481732] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1782382346.003061949] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.81,-0.59) yaw=134deg cmd=(vx=0.50 wz=-0.65) elapsed=49.3s plan[15pts 2.1m] (3.00,-0.85)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=66% mem=18%
[velocity_pid.py-9] [INFO] [1782382346.653487599] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.52 corrected=-0.05 err=26.1%
[cmd_vel_mux.py-8] [INFO] [1782382346.709776952] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.00
[velocity_pid.py-9] [INFO] [1782382346.719028178] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.12 -> current=0.00 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1782382346.920376630] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0285s, resetting
[component_container_isolated-18] [WARN] [1782382347.495505099] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2772 Hz
[component_container_isolated-18] [INFO] [1782382347.612475314] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782382347.654273515] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.08 corrected=-0.08 err=62.9%
[cmd_vel_mux.py-8] [INFO] [1782382347.709652908] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.20
[velocity_pid.py-9] [INFO] [1782382347.856610552] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.14 dt=0.0325s, resetting
[competition_master_stage3.py-19] [INFO] [1782382348.006437868] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.46,-0.02) yaw=113deg cmd=(vx=0.29 wz=0.02) elapsed=51.3s plan[8pts 1.0m] (2.40,0.05)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=72% mem=18%
[velocity_pid.py-9] [INFO] [1782382348.654477469] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.28 corrected=0.33 err=43.8%
[component_container_isolated-18] [WARN] [1782382349.491838041] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2815 Hz
[component_container_isolated-18] [INFO] [1782382349.612473511] [controller_server]: Passing new path to controller.
[component_container_isolated-18] Reallocing temp weights 1500 - 60
[velocity_pid.py-9] [INFO] [1782382349.686652438] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.15 err=22.7%
[cmd_vel_mux.py-8] [INFO] [1782382349.847705149] [cmd_vel_mux]: [mux→] src=nav vx=0.31 wz=-0.04
[competition_master_stage3.py-19] [INFO] [1782382350.006071813] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.32,0.25) yaw=115deg cmd=(vx=0.29 wz=-0.04) elapsed=53.3s plan[6pts 0.7m] (2.30,0.35)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=77% mem=18%
[cmd_vel_mux.py-8] [INFO] [1782382350.446545200] [cmd_vel_mux]: [mux→] src=nav vx=0.09 wz=0.04
[velocity_pid.py-9] [INFO] [1782382350.456366176] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.09 -> current=0.04 dt=0.0361s, resetting
[velocity_pid.py-9] [INFO] [1782382350.518736207] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.09 -> current=-0.00 dt=0.0333s, resetting
[component_container_isolated-18] [INFO] [1782382350.615802134] [controller_server]: Reached the goal!
[component_container_isolated-18] [WARN] [1782382351.494161610] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2781 Hz
[component_container_isolated-18] [WARN] [1782382351.500423829] [BehaviorTreeEngine]: Behavior Tree tick rate 10.00 was exceeded!
[component_container_isolated-18] [INFO] [1782382351.501105956] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-19] [INFO] [1782382351.518689196] [competition_master_stage3]: [结果回调] 巡航完成, 到达VLM路点, 触发VLM推理...
[competition_master_stage3.py-19] [INFO] [1782382351.523784289] [competition_master_stage3]: [VLM] 发布 sign4return=100, 拍照推理中...
[vision_ai_node-14] [INFO] [1782382351.528696423] [vision_ai_node]: Received sign4return: 100
[competition_master_stage3.py-19] [INFO] [1782382351.530070050] [competition_master_stage3]: [状态机] CRUISE_CHANNEL → RETURN_P
[vision_ai_node-14] [INFO] [1782382351.533052931] [vision_ai_node]: Received trigger signal (sign4return=100), subscribing to image topic...
[competition_master_stage3.py-19] [INFO] [1782382351.541119445] [competition_master_stage3]: [RETURN] 返航至 P点 (-1.99,-0.01)
[vision_ai_node-14] [INFO] [1782382351.566306699] [vision_ai_node]: Subscribed to /aurora/rgb/image_raw topic
[vision_ai_node-14] [INFO] [1782382351.626714184] [vision_ai_node]: Received compressed image, processing with AI model...
[competition_master_stage3.py-19] [INFO] [1782382351.651631397] [competition_master_stage3]: [DIAG] nav目标距离: 4.10m, robot=(2.05,0.76) → target=(-1.99,-0.01)
[competition_master_stage3.py-19] [INFO] [1782382351.655019444] [competition_master_stage3]: >>> 发送导航目标 [P点返航]: (-1.99, -0.01, yaw=1.98)
[component_container_isolated-18] [INFO] [1782382351.660905205] [bt_navigator]: Begin navigating from current location (2.04, 0.81) to (-1.99, -0.01)
[competition_master_stage3.py-19] [INFO] [1782382351.679340280] [competition_master_stage3]: 导航目标已接受，车辆出发...
[competition_master_stage3.py-19] [INFO] [1782382352.007383420] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.05,0.76) yaw=114deg cmd=(vx=0.00 wz=0.00) elapsed=55.3s plan[3pts 0.2m] (2.10,0.75)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=77% mem=18%
[cmd_vel_mux.py-8] [INFO] [1782382352.109322147] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.52s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1782382352.113319946] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[component_container_isolated-18] [WARN] [1782382352.551033076] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.1337 Hz
[component_container_isolated-18] [INFO] [1782382352.666360952] [controller_server]: Received a goal, begin computing control effort.
[cmd_vel_mux.py-8] [INFO] [1782382352.709129280] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=0.12
[velocity_pid.py-9] [INFO] [1782382352.722132512] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.11 err=100.0%
[imu_madgwick_filter.py-6] [INFO] [1782382352.738872751] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3869 q_w=0.6639 angle=96.8deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782382352.912066149] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1599 q_w=0.3259 angle=142.0deg beta=0.0330
[competition_master_stage3.py-19] [INFO] [1782382354.007921100] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.97,0.88) yaw=126deg cmd=(vx=0.50 wz=0.98) elapsed=57.3s plan[46pts 6.6m] (2.00,0.85)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=62% mem=18%
[component_container_isolated-18] [WARN] [1782382354.551612420] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2736 Hz
[component_container_isolated-18] [INFO] [1782382354.668316924] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782382355.520341344] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.12 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1782382355.544059179] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.73
[velocity_pid.py-9] [INFO] [1782382355.787074911] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1782382355.853476074] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.11 -> current=-0.02 dt=0.0336s, resetting
[competition_master_stage3.py-19] [INFO] [1782382356.005198557] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.88,0.80) yaw=-126deg cmd=(vx=-0.30 wz=-0.27) elapsed=59.3s plan[39pts 5.8m] (1.60,1.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=77% mem=18%
[velocity_pid.py-9] [INFO] [1782382356.521203325] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.09 corrected=-0.33 err=71.7%
[component_container_isolated-18] [WARN] [1782382356.538610482] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2968 Hz
[component_container_isolated-18] [INFO] [1782382356.668340633] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782382356.744597105] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.49
[velocity_pid.py-9] [INFO] [1782382356.854288387] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0335s, resetting
[velocity_pid.py-9] [INFO] [1782382356.953769984] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.11 -> current=0.01 dt=0.0338s, resetting
[velocity_pid.py-9] [INFO] [1782382357.521477303] [velocity_pid]: [vel_pid→] desired=0.48 actual=0.11 corrected=0.47 err=76.7%
[competition_master_stage3.py-19] [INFO] [1782382358.002471173] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.75,0.54) yaw=-105deg cmd=(vx=0.50 wz=1.50) elapsed=61.3s plan[36pts 5.0m] (0.80,0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=77% mem=18%
[imu_madgwick_filter.py-4] [WARN] [1782382358.024584046] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1500s > 0.15s, capping
[component_container_isolated-18] [WARN] [1782382358.592246530] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2111 Hz
[component_container_isolated-18] [INFO] [1782382358.768310015] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782382358.819266691] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.52 corrected=0.03 err=27.6%
[cmd_vel_mux.py-8] [INFO] [1782382358.850587706] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.19
[velocity_pid.py-9] [INFO] [1782382359.056305536] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0344s, resetting
[velocity_pid.py-9] [INFO] [1782382359.822735669] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.06 corrected=-0.35 err=78.3%
[competition_master_stage3.py-19] [INFO] [1782382360.012283470] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.93,-0.10) yaw=-70deg cmd=(vx=-0.30 wz=0.14) elapsed=63.3s plan[38pts 5.0m] (0.70,0.35)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=50% mem=18%
[component_container_isolated-18] [WARN] [1782382360.584731669] [planner_server]: GridBased: failed to create plan, exceeded maximum iterations.
[component_container_isolated-18] [WARN] [1782382360.586070046] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (-1.99, -0.01)
[component_container_isolated-18] [WARN] [1782382360.586185505] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1782382360.765093536] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1782382360.774418677] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1782382360.788231244] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1782382360.788428828] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1782382360.807885363] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[velocity_pid.py-9] [INFO] [1782382360.853984571] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.03 -> current=-0.10 dt=0.0336s, resetting
[component_container_isolated-18] [WARN] [1782382361.602364878] [planner_server]: GridBased: failed to create plan, exceeded maximum iterations.
[component_container_isolated-18] [WARN] [1782382361.606085718] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (-1.99, -0.01)
[component_container_isolated-18] [WARN] [1782382361.609311598] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1782382361.768341760] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-18] [INFO] [1782382361.768527885] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1782382361.770096346] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1782382361.779551530] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1782382361.789965132] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1782382361.790020257] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1782382361.790234883] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1782382361.805069659] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1782382361.810585961] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1782382361.825411571] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1782382361.825574905] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[velocity_pid.py-9] [INFO] [1782382361.832371167] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.28 corrected=-0.04 err=33.8%
[component_container_isolated-18] [INFO] [1782382361.837718926] [behavior_server]: Running backup
[component_container_isolated-18] [INFO] [1782382361.838846470] [behavior_server]: DriveOnHeading: no acceleration or deceleration limits set
[component_container_isolated-18] [WARN] [1782382361.841434558] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[cmd_vel_mux.py-8] [INFO] [1782382361.847377610] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-1.14
[competition_master_stage3.py-19] [INFO] [1782382362.002031931] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.79,0.29) yaw=-73deg cmd=(vx=0.00 wz=-0.89) elapsed=65.3s plan[38pts 5.0m] (0.70,0.35)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=77% mem=18%
[cmd_vel_mux.py-8] [INFO] [1782382362.377107897] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.00
[imu_madgwick_filter.py-6] [INFO] [1782382362.741009635] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4367 q_w=-0.6038 angle=254.3deg beta=0.0030
[velocity_pid.py-9] [INFO] [1782382362.857737595] [velocity_pid]: [vel_pid→] desired=-0.12 actual=-0.07 corrected=-0.17 err=40.8%
[imu_madgwick_filter.py-4] [INFO] [1782382362.911121566] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1797 q_w=-0.8612 angle=298.9deg beta=0.0330
[competition_master_stage3.py-19] [INFO] [1782382364.008012038] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.79,0.51) yaw=-90deg cmd=(vx=-0.12 wz=0.00) elapsed=67.3s plan[38pts 5.0m] (0.70,0.35)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=63% mem=18%
[component_container_isolated-18] [WARN] [1782382365.738990435] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1782382365.739184186] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1782382365.739294061] [behavior_server]: [backup] [ActionServer] Aborting handle.
[cmd_vel_mux.py-8] [INFO] [1782382365.776668586] [cmd_vel_mux]: [mux→] src=nav vx=0.00 wz=0.00
[component_container_isolated-18] [INFO] [1782382365.965621425] [behavior_server]: Running wait
[competition_master_stage3.py-19] [INFO] [1782382366.002954075] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.79,0.70) yaw=-92deg cmd=(vx=0.00 wz=0.00) elapsed=69.3s plan[38pts 5.0m] (0.70,0.35)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=100% mem=18%
[cmd_vel_mux.py-8] [INFO] [1782382366.275575022] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.53s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1782382366.289182880] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[competition_master_stage3.py-19] [INFO] [1782382368.002195571] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.79,0.70) yaw=-92deg cmd=(vx=0.00 wz=0.00) elapsed=71.3s plan[38pts 5.0m] (0.70,0.35)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=75% mem=18%
[component_container_isolated-18] [INFO] [1782382368.966312836] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1782382369.516495318] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 3.9998 Hz
[component_container_isolated-18] [INFO] [1782382369.665889251] [controller_server]: Received a goal, begin computing control effort.
[cmd_vel_mux.py-8] [INFO] [1782382369.711405624] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=0.12
[velocity_pid.py-9] [INFO] [1782382369.724882190] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.07 err=100.0%
[competition_master_stage3.py-19] [INFO] [1782382370.005426566] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.79,0.70) yaw=-92deg cmd=(vx=0.45 wz=0.64) elapsed=73.3s plan[38pts 5.0m] (0.80,0.95)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=60% mem=18%
[velocity_pid.py-9] [INFO] [1782382370.921609241] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.11 -> current=-0.01 dt=0.0332s, resetting
[vision_ai_node-14] [INFO] [1782382371.210037755] [vision_ai_node]: AI Analysis Result: 这张图片呈现了一个**室内装修（或装修后）的场景**，细节如下：
[vision_ai_node-14]
[vision_ai_node-14] ### 背景与墙面
[vision_ai_node-14] 背景是一面由**浅米色（或米白色）光滑瓷砖**铺成的墙面，瓷砖表面带有**反光效果**，左侧能隐约看到**窗户及室内物体的倒影**（如窗框、室内陈设的模糊轮廓），既增强了空间明亮感，也暗示此处是封闭/半封闭的室内环境（如房间、走廊）。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] ### 地面与保护材料
[vision_ai_node-14] 地面覆盖着两层**保护材料**：
[vision_ai_node-14] - 上层是**浅绿色的塑料薄膜**，材质平整但边缘略带自然褶皱；
[vision_ai_node-14] - 下层是**米黄色的布（或纸类材料）**，表面褶皱更明显，整体用于装修期间保护地面（推测为防止瓷砖/地板被划伤、污染）。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] ### 核心物体：饮料瓶
[vision_ai_node-14] 画面右侧立着一个**透明塑料饮料瓶**：
[vision_ai_node-14] - 瓶身贴有**红色标签**，瓶盖为**黄色**，瓶内**残留少量液体**（推测是未喝完的饮料）；
[vision_ai_node-14] - 瓶身简洁的造型与周围“装修保护”的场景形成对比，成为视觉焦点之一。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] ### 整体氛围与色调
[vision_ai_node-14] 场景色调以**浅色系**为主（浅米黄瓷砖、浅绿色/米黄保护材料），搭配饮料瓶的“红+黄+透明”，整体氛围**简洁柔和**，却因地面保护材料的褶皱、未整理感，透出“施工后暂未完全整理”的状态，推测此处是**正在装修（或刚完成基础装修）的室内空间**（如新房、翻新后的房间）。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] 这幅画面通过“瓷砖反光的墙面+地面保护材料+残留饮料瓶”的组合，传递出一种“装修过渡阶段”的真实感，细节（如瓷砖倒影、瓶内残液）让场景更具生活气息。
[competition_master_stage3.py-19] [INFO] [1782382371.219037688] [competition_master_stage3]: [VLM] 后台收到推理结果: 这张图片呈现了一个**室内装修（或装修后）的场景**，细节如下：
[competition_master_stage3.py-19]
[competition_master_stage3.py-19] ### 背景与墙面
[competition_master_stage3.py-19] 背景是一面由**浅米色（或米白色）光滑瓷砖**铺成的墙面，瓷砖表面带有**反光效果**，左侧能隐约看到**窗户及室内物体的倒影**（如窗框、室内...
[vision_ai_node-14] [INFO] [1782382371.229272290] [vision_ai_node]: Unsubscribed from image topic
[component_container_isolated-18] [WARN] [1782382371.518970681] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3282 Hz
[component_container_isolated-18] [INFO] [1782382371.666208443] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1782382372.004481045] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.93,0.33) yaw=-76deg cmd=(vx=0.50 wz=-0.35) elapsed=75.3s plan[34pts 4.5m] (0.90,0.45)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=100% mem=18%
[imu_madgwick_filter.py-6] [INFO] [1782382372.740059563] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4878 q_w=-0.5823 angle=251.2deg beta=0.0030
[cmd_vel_mux.py-8] [INFO] [1782382372.843578789] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.26
[velocity_pid.py-9] [INFO] [1782382372.852883263] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.49 corrected=-0.20 err=53.1%
[imu_madgwick_filter.py-4] [INFO] [1782382372.915847875] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1996 q_w=-0.8572 angle=298.0deg beta=0.0330
[velocity_pid.py-9] [INFO] [1782382373.019257143] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.01 -> current=0.12 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1782382373.052435410] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0331s, resetting
[component_container_isolated-18] [WARN] [1782382373.555610346] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2668 Hz
[component_container_isolated-18] [INFO] [1782382373.666218168] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782382373.744807516] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.04
[velocity_pid.py-9] [INFO] [1782382373.819022064] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.08 dt=0.0323s, resetting
[velocity_pid.py-9] [INFO] [1782382373.852187623] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1782382373.858189426] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.10 corrected=0.38 err=273.3%
[competition_master_stage3.py-19] [INFO] [1782382374.002211015] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.02,-0.28) yaw=-95deg cmd=(vx=0.21 wz=-0.46) elapsed=77.3s plan[25pts 3.5m] (1.00,-0.45)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=75% mem=18%
[velocity_pid.py-9] [INFO] [1782382374.889411049] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.37 corrected=0.32 err=25.4%
[component_container_isolated-18] [WARN] [1782382375.576589726] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2341 Hz
[component_container_isolated-18] [INFO] [1782382375.766208562] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1782382376.004349193] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.73,-0.77) yaw=-154deg cmd=(vx=0.50 wz=0.07) elapsed=79.3s plan[26pts 3.3m] (0.80,-0.75)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=66% mem=18%
[velocity_pid.py-9] [INFO] [1782382376.720701795] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.01 err=22.7%
[cmd_vel_mux.py-8] [INFO] [1782382376.743832253] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.08
[velocity_pid.py-9] [INFO] [1782382376.986387183] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0334s, resetting
[component_container_isolated-18] [WARN] [1782382377.571608802] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4216 Hz
[velocity_pid.py-9] [INFO] [1782382377.721114191] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.09 corrected=-0.33 err=69.7%
[component_container_isolated-18] [INFO] [1782382377.766211813] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782382377.819505616] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.02 -> current=-0.11 dt=0.0334s, resetting
[cmd_vel_mux.py-8] [INFO] [1782382377.843401783] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.23
[velocity_pid.py-9] [INFO] [1782382377.952151184] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0334s, resetting
[competition_master_stage3.py-19] [INFO] [1782382378.003433733] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.16,-1.02) yaw=-155deg cmd=(vx=0.06 wz=-0.48) elapsed=81.3s plan[20pts 2.5m] (-0.00,-1.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=66% mem=18%
[velocity_pid.py-9] [INFO] [1782382378.753364975] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.25 corrected=0.34 err=50.4%
[component_container_isolated-18] [WARN] [1782382379.586395488] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4019 Hz
[component_container_isolated-18] [INFO] [1782382379.766771307] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1782382380.003068683] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.43,-1.13) yaw=159deg cmd=(vx=0.50 wz=-0.40) elapsed=83.3s plan[17pts 2.2m] (-0.20,-1.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=66% mem=18%
[velocity_pid.py-9] [INFO] [1782382380.719631238] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.12 -> current=0.01 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1782382380.723207245] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.03 err=22.7%
[cmd_vel_mux.py-8] [INFO] [1782382380.746553536] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.13
[velocity_pid.py-9] [INFO] [1782382380.977286235] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0462s, resetting
[component_container_isolated-18] [WARN] [1782382381.515778142] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.5414 Hz
[component_container_isolated-18] [INFO] [1782382381.668629536] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782382381.752980352] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.11 corrected=-0.22 err=47.1%
[cmd_vel_mux.py-8] [INFO] [1782382381.777665353] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.03
[velocity_pid.py-9] [INFO] [1782382381.785997160] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.10 -> current=-0.03 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1782382381.852540027] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0336s, resetting
[competition_master_stage3.py-19] [INFO] [1782382382.012318934] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.93,-0.78) yaw=139deg cmd=(vx=0.21 wz=-0.53) elapsed=85.3s plan[10pts 1.4m] (-1.00,-0.75)→(-1.96,0.09) cpuFreq=1500MHz cpuT=73C cpu=66% mem=18%
[imu_madgwick_filter.py-6] [INFO] [1782382382.739348255] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5390 q_w=0.5096 angle=118.7deg beta=0.0030
[velocity_pid.py-9] [INFO] [1782382382.753753405] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.32 corrected=0.30 err=36.0%
[imu_madgwick_filter.py-4] [INFO] [1782382382.911536225] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2195 q_w=0.0803 angle=170.8deg beta=0.0330
[velocity_pid.py-9] [INFO] [1782382383.452803427] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.01 -> current=0.10 dt=0.0336s, resetting
[component_container_isolated-18] [WARN] [1782382383.495259793] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3725 Hz
[component_container_isolated-18] [INFO] [1782382383.666224427] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1782382384.005175523] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.18,-0.42) yaw=112deg cmd=(vx=0.50 wz=1.25) elapsed=87.3s plan[9pts 1.0m] (-1.20,-0.45)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=72% mem=18%
[cmd_vel_mux.py-8] [INFO] [1782382384.143725642] [cmd_vel_mux]: [mux→] src=nav vx=0.38 wz=1.67
[velocity_pid.py-9] [INFO] [1782382384.155239329] [velocity_pid]: [vel_pid→] desired=0.38 actual=0.47 corrected=0.14 err=23.8%
[velocity_pid.py-9] [INFO] [1782382384.420277752] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.02 -> current=-0.07 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1782382384.854722599] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.08 dt=0.0342s, resetting
[velocity_pid.py-9] [INFO] [1782382385.186356431] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.10 corrected=-0.30 err=67.3%
[component_container_isolated-18] [WARN] [1782382385.505405449] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3530 Hz
[component_container_isolated-18] [INFO] [1782382385.666211107] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782382385.743389450] [cmd_vel_mux]: [mux→] src=nav vx=-0.19 wz=-0.55
[competition_master_stage3.py-19] [INFO] [1782382386.007324830] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.47,-0.09) yaw=138deg cmd=(vx=-0.18 wz=-0.05) elapsed=89.3s plan[7pts 0.9m] (-1.40,-0.05)→(-1.96,0.13) cpuFreq=1500MHz cpuT=73C cpu=72% mem=18%
[velocity_pid.py-9] [INFO] [1782382386.186811395] [velocity_pid]: [vel_pid→] desired=0.15 actual=-0.20 corrected=0.10 err=234.7%
[cmd_vel_mux.py-8] [INFO] [1782382386.248592586] [cmd_vel_mux]: [mux→] src=nav vx=0.30 wz=-0.72
[cmd_vel_mux.py-8] [INFO] [1782382387.010341297] [cmd_vel_mux]: [mux→] src=nav vx=0.31 wz=-1.47
[velocity_pid.py-9] [INFO] [1782382387.218790495] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.04 -> current=-0.05 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1782382387.222758919] [velocity_pid]: [vel_pid→] desired=-0.05 actual=0.37 corrected=-0.85 err=785.2%
[component_container_isolated-18] [WARN] [1782382387.497426233] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3679 Hz
[component_container_isolated-18] [INFO] [1782382387.666202362] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782382387.709874647] [cmd_vel_mux]: [mux→] src=nav vx=-0.28 wz=0.03
[velocity_pid.py-9] [INFO] [1782382387.721440375] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.09 -> current=0.03 dt=0.0336s, resetting
[competition_master_stage3.py-19] [INFO] [1782382388.004755163] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.42,-0.07) yaw=93deg cmd=(vx=-0.30 wz=0.66) elapsed=91.3s plan[8pts 0.9m] (-1.40,-0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=62% mem=18%
[velocity_pid.py-9] [INFO] [1782382388.254534392] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.14 corrected=-0.30 err=52.3%
[cmd_vel_mux.py-8] [INFO] [1782382388.611123974] [cmd_vel_mux]: [mux→] src=nav vx=-0.11 wz=1.54
[velocity_pid.py-9] [INFO] [1782382388.719398913] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.02 -> current=0.07 dt=0.0330s, resetting
[velocity_pid.py-9] [INFO] [1782382389.254365807] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.08 dt=0.0337s, resetting
[velocity_pid.py-9] [INFO] [1782382389.260421234] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.06 corrected=0.48 err=88.4%
[component_container_isolated-18] [WARN] [1782382389.492688307] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3798 Hz
[cmd_vel_mux.py-8] [INFO] [1782382389.511844799] [cmd_vel_mux]: [mux→] src=nav vx=0.37 wz=-0.71
[component_container_isolated-18] [INFO] [1782382389.666225110] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1782382390.004445451] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.41,-0.07) yaw=108deg cmd=(vx=0.27 wz=-0.33) elapsed=93.3s plan[6pts 0.7m] (-1.40,-0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=63% mem=18%
[cmd_vel_mux.py-8] [INFO] [1782382390.114339810] [cmd_vel_mux]: [mux→] src=nav vx=0.14 wz=-0.21
[velocity_pid.py-9] [INFO] [1782382390.218958200] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0332s, resetting
[velocity_pid.py-9] [INFO] [1782382390.286432110] [velocity_pid]: [vel_pid→] desired=-0.11 actual=0.30 corrected=-0.33 err=368.8%
[velocity_pid.py-9] [INFO] [1782382390.719531658] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.08 -> current=0.04 dt=0.0308s, resetting
[velocity_pid.py-9] [INFO] [1782382391.286562397] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.22 corrected=-0.21 err=26.0%
[component_container_isolated-18] [WARN] [1782382391.492644590] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3771 Hz
[component_container_isolated-18] [INFO] [1782382391.666238059] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782382391.709277259] [cmd_vel_mux]: [mux→] src=nav vx=-0.18 wz=-0.06
[competition_master_stage3.py-19] [INFO] [1782382392.006817236] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.42,-0.05) yaw=91deg cmd=(vx=0.00 wz=0.06) elapsed=95.3s plan[8pts 0.8m] (-1.40,0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=74C cpu=81% mem=18%
[cmd_vel_mux.py-8] [INFO] [1782382392.242692772] [cmd_vel_mux]: [mux→] src=nav vx=0.45 wz=-0.69
[velocity_pid.py-9] [INFO] [1782382392.291239149] [velocity_pid]: [vel_pid→] desired=0.45 actual=-0.09 corrected=0.26 err=118.9%
[imu_madgwick_filter.py-6] [INFO] [1782382392.740153014] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5884 q_w=0.7933 angle=75.0deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782382392.912269480] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2395 q_w=0.4004 angle=132.8deg beta=0.0330
[cmd_vel_mux.py-8] [INFO] [1782382393.345682901] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.00
[velocity_pid.py-9] [INFO] [1782382393.355417335] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.48 corrected=-0.20 err=49.1%
[velocity_pid.py-9] [INFO] [1782382393.423946288] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.00 -> current=0.12 dt=0.0340s, resetting
[component_container_isolated-18] [WARN] [1782382393.494747078] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3725 Hz
[velocity_pid.py-9] [INFO] [1782382393.553199596] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0335s, resetting
[component_container_isolated-18] [INFO] [1782382393.666217959] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-19] [INFO] [1782382394.009624224] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.39,0.14) yaw=74deg cmd=(vx=-0.30 wz=0.35) elapsed=97.3s plan[10pts 1.3m] (-1.40,0.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=20% mem=18%
[velocity_pid.py-9] [INFO] [1782382394.387932173] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.13 corrected=-0.26 err=56.7%
[component_container_isolated-18] [WARN] [1782382395.492668384] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3774 Hz
[component_container_isolated-18] [INFO] [1782382395.666249144] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782382395.836796482] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.30 corrected=0.00 err=43.3%
[cmd_vel_mux.py-8] [INFO] [1782382395.844682454] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.32
[velocity_pid.py-9] [INFO] [1782382395.954213186] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0338s, resetting
[competition_master_stage3.py-19] [INFO] [1782382396.016822920] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.38,-0.07) yaw=100deg cmd=(vx=-0.03 wz=0.19) elapsed=99.3s plan[8pts 0.8m] (-1.40,0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=88% mem=18%
[velocity_pid.py-9] [INFO] [1782382396.853807663] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.29 corrected=0.34 err=41.2%
[cmd_vel_mux.py-8] [INFO] [1782382397.242863588] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-1.14
[velocity_pid.py-9] [INFO] [1782382397.452875827] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0334s, resetting
[component_container_isolated-18] [WARN] [1782382397.494675649] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3730 Hz
[component_container_isolated-18] [INFO] [1782382397.666217030] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1782382397.752567805] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.02 -> current=0.11 dt=0.0335s, resetting
[velocity_pid.py-9] [INFO] [1782382397.886116870] [velocity_pid]: [vel_pid→] desired=-0.30 actual=0.07 corrected=-0.32 err=123.7%
[competition_master_stage3.py-19] [INFO] [1782382398.014017758] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.32,0.25) yaw=56deg cmd=(vx=-0.30 wz=0.48) elapsed=101.3s plan[10pts 1.2m] (-1.40,0.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=100% mem=18%
[cmd_vel_mux.py-8] [INFO] [1782382399.209457869] [cmd_vel_mux]: [mux→] src=nav vx=-0.17 wz=1.67
[velocity_pid.py-9] [INFO] [1782382399.219534595] [velocity_pid]: [vel_pid→] desired=-0.17 actual=-0.29 corrected=0.02 err=69.8%
[velocity_pid.py-9] [INFO] [1782382399.319150934] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.08 -> current=0.01 dt=0.0328s, resetting
[component_container_isolated-18] [WARN] [1782382399.491598232] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3810 Hz
[component_container_isolated-18] [INFO] [1782382399.666216784] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782382399.743757293] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.43
[velocity_pid.py-9] [INFO] [1782382399.956149452] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0324s, resetting
[competition_master_stage3.py-19] [INFO] [1782382400.001059822] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.40,-0.03) yaw=102deg cmd=(vx=0.05 wz=0.61) elapsed=103.3s plan[8pts 0.9m] (-1.40,-0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=44% mem=18%
[velocity_pid.py-9] [INFO] [1782382400.220504534] [velocity_pid]: [vel_pid→] desired=-0.30 actual=0.06 corrected=-0.34 err=121.7%
[velocity_pid.py-9] [INFO] [1782382401.220978679] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.25 corrected=0.01 err=21.4%
[cmd_vel_mux.py-8] [INFO] [1782382401.245509638] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.69
[velocity_pid.py-9] [INFO] [1782382401.354493410] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0336s, resetting
[component_container_isolated-18] [WARN] [1782382401.495185778] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3948 Hz
[component_container_isolated-18] [INFO] [1782382401.666335323] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782382401.745923502] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.56
[velocity_pid.py-9] [INFO] [1782382401.952672234] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0332s, resetting
[competition_master_stage3.py-19] [INFO] [1782382402.002137278] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.38,-0.11) yaw=114deg cmd=(vx=-0.04 wz=1.06) elapsed=105.3s plan[8pts 1.0m] (-1.30,-0.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=55% mem=18%
[velocity_pid.py-9] [INFO] [1782382402.254954755] [velocity_pid]: [vel_pid→] desired=-0.18 actual=0.04 corrected=-0.20 err=121.7%
[imu_madgwick_filter.py-6] [INFO] [1782382402.769230601] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=6383 q_w=0.7146 angle=88.8deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782382402.911503429] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2594 q_w=0.2062 angle=156.2deg beta=0.0330
[cmd_vel_mux.py-8] [INFO] [1782382403.148954797] [cmd_vel_mux]: [mux→] src=nav vx=0.00 wz=2.45
[velocity_pid.py-9] [INFO] [1782382403.286498534] [velocity_pid]: [vel_pid→] desired=0.15 actual=-0.14 corrected=0.14 err=195.3%
[component_container_isolated-18] [WARN] [1782382403.492681889] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3783 Hz
[component_container_isolated-18] [INFO] [1782382403.666209063] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1782382403.743236654] [cmd_vel_mux]: [mux→] src=nav vx=0.43 wz=1.45
[competition_master_stage3.py-19] [INFO] [1782382404.004541854] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.32,-0.30) yaw=113deg cmd=(vx=0.44 wz=1.67) elapsed=107.3s plan[6pts 0.8m] (-1.30,-0.35)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=81% mem=18%
[velocity_pid.py-9] [INFO] [1782382404.286843048] [velocity_pid]: [vel_pid→] desired=0.43 actual=0.30 corrected=0.12 err=30.3%
[velocity_pid.py-9] [INFO] [1782382405.191051062] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.08 -> current=-0.04 dt=0.0318s, resetting
[component_container_isolated-18] [INFO] [1782382405.467144329] [controller_server]: Reached the goal!
[component_container_isolated-18] [WARN] [1782382405.498901508] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2020 Hz
[cmd_vel_mux.py-8] [INFO] [1782382405.544758504] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.40
[velocity_pid.py-9] [INFO] [1782382405.553786978] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.50 corrected=-0.17 err=55.3%
[component_container_isolated-18] [INFO] [1782382405.665657087] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-18] [INFO] [1782382405.666331421] [controller_server]: Reached the goal!
[competition_master_stage3.py-19] [INFO] [1782382406.006063380] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.75,-0.10) yaw=177deg cmd=(vx=0.00 wz=0.00) elapsed=109.3s plan[3pts 0.2m] (-1.80,-0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=50% mem=18%
[component_container_isolated-18] [INFO] [1782382406.065205565] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-19] [INFO] [1782382406.074577623] [competition_master_stage3]: [结果回调] 已回到P点, 任务完成!
[competition_master_stage3.py-19] [INFO] [1782382406.078180713] [competition_master_stage3]: [状态机] RETURN_P → DONE
[competition_master_stage3.py-19] [INFO] [1782382406.082250053] [competition_master_stage3]:
[competition_master_stage3.py-19] [INFO] [1782382406.085410558] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1782382406.089042231] [competition_master_stage3]: >>> [Stage 3] 任务结束 <<<
[competition_master_stage3.py-19] [INFO] [1782382406.091895195] [competition_master_stage3]:   最终状态: DONE
[competition_master_stage3.py-19] [INFO] [1782382406.095528201] [competition_master_stage3]:   总耗时:   109.4s
[competition_master_stage3.py-19] [INFO] [1782382406.098440622] [competition_master_stage3]:   --- 各阶段耗时 ---
[competition_master_stage3.py-19] [INFO] [1782382406.101006127] [competition_master_stage3]:   LAUNCH................ 14.7s
[competition_master_stage3.py-19] [INFO] [1782382406.103431256] [competition_master_stage3]:   NAV_TO_QR............. 12.0s
[competition_master_stage3.py-19] [INFO] [1782382406.105783885] [competition_master_stage3]:   BACKING_UP............ 6.0s
[competition_master_stage3.py-19] [INFO] [1782382406.108141931] [competition_master_stage3]:   CRUISE_CHANNEL........ 36.9s
[cmd_vel_mux.py-8] [INFO] [1782382406.109283766] [cmd_vel_mux]: [mux→] src=stop vx=0.00 wz=0.00
[competition_master_stage3.py-19] [INFO] [1782382406.110541935] [competition_master_stage3]:   RETURN_P.............. 54.6s
[competition_master_stage3.py-19] [INFO] [1782382406.112925814] [competition_master_stage3]:   (transition/overhead). -14.7s
[competition_master_stage3.py-19] [INFO] [1782382406.115161110] [competition_master_stage3]:   --- ---
[competition_master_stage3.py-19] [INFO] [1782382406.117375155] [competition_master_stage3]:   QR 原始数据: 1584
[competition_master_stage3.py-19] [INFO] [1782382406.119873618] [competition_master_stage3]:   QR 方向:   逆时针 (CW=顺时针/odd, CCW=逆时针/even)
[competition_master_stage3.py-19] [INFO] [1782382406.122550247] [competition_master_stage3]:   VLM 结果:  这张图片呈现了一个**室内装修（或装修后）的场景**，细节如下：
[competition_master_stage3.py-19]
[competition_master_stage3.py-19] ### 背景与墙面
[competition_master_stage3.py-19] 背景是一面由**浅米色（或米白色）光滑瓷砖**铺成的墙面，瓷砖表面带有**反光效果**，左侧能隐约看到**窗户及室内物体的倒影**（如窗框、室内陈设的模糊轮廓），既增强了空间明亮感，也暗示此处是封闭/半封闭的室内环境（如房间、走廊）。
[competition_master_stage3.py-19]
[competition_master_stage3.py-19]
[competition_master_stage3.py-19] ### 地面与保护材料
[competition_master_stage3.py-19] 地面覆盖着两层**保护材料**：
[competition_master_stage3.py-19] [INFO] [1782382406.125305044] [competition_master_stage3]:   超时限制:  180.0s (全局)
[competition_master_stage3.py-19] [INFO] [1782382406.127632548] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-19] [INFO] [1782382406.134271059] [competition_master_stage3]: [TRAJ] CSV已保存: /userdata/dev_ws/trajectory_20260625_181326.csv (137 点)
[competition_master_stage3.py-19] [INFO] [1782382406.139022650] [competition_master_stage3]: [TRAJ] 摘要JSON已保存: /userdata/dev_ws/trajectory_20260625_181326_summary.json
[competition_master_stage3.py-19] [INFO] [1782382406.143675200] [competition_master_stage3]: [TRAJ] 规划历史已保存: /userdata/dev_ws/trajectory_20260625_181326_plans.csv (46 次规划)
[competition_master_stage3.py-19] [INFO] [1782382406.162982567] [competition_master_stage3]: [TRAJ] costmap PGM已保存: /userdata/dev_ws/trajectory_20260625_181326_costmap.pgm
[cmd_vel_mux.py-8] [INFO] [1782382407.145660921] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.51s > 0.5s, marked inactive
[competition_master_stage3.py-19] [INFO] [1782382408.001763432] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.98,-0.09) yaw=-178deg cmd=(vx=0.00 wz=0.00) elapsed=111.3s plan[3pts 0.2m] (-1.80,-0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=70% mem=18%
[competition_master_stage3.py-19] [INFO] [1782382410.000769565] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.98,-0.09) yaw=-178deg cmd=(vx=0.00 wz=0.00) elapsed=113.3s plan[3pts 0.2m] (-1.80,-0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=70% mem=18%
[competition_master_stage3.py-19] [INFO] [1782382412.002715739] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.98,-0.09) yaw=-178deg cmd=(vx=0.00 wz=0.00) elapsed=115.3s plan[3pts 0.2m] (-1.80,-0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=66% mem=18%
[imu_madgwick_filter.py-6] [INFO] [1782382412.739487872] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=6894 q_w=0.0963 angle=168.9deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1782382412.911682291] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2794 q_w=-0.5119 angle=241.6deg beta=0.0330
[competition_master_stage3.py-19] [INFO] [1782382414.003990529] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.98,-0.09) yaw=-178deg cmd=(vx=0.00 wz=0.00) elapsed=117.3s plan[3pts 0.2m] (-1.80,-0.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=63% mem=18%
^C[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[rviz2-20] [INFO] [1782382415.755340846] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [origincar_base_node-1]: process has died [pid 15322, exit code -6, cmd '/userdata/dev_ws/install/origincar_base/lib/origincar_base/origincar_base_node --ros-args --params-file /tmp/launch_params_bfcdcjon --params-file /tmp/launch_params_4snxnunv'].
[ERROR] [lslidar_driver_node-2]: process has died [pid 15324, exit code -6, cmd '/userdata/dev_ws/install/lslidar_driver/lib/lslidar_driver/lslidar_driver_node --ros-args -r __node:=lslidar_driver_node --params-file /userdata/dev_ws/install/lslidar_driver/share/lslidar_driver/params/lsx10.yaml'].
[INFO] [imu_madgwick_filter.py-6]: process has finished cleanly [pid 15332]
[INFO] [robot_state_publisher-3]: process has finished cleanly [pid 15326]
[INFO] [costmap_filter_info_server-16]: process has finished cleanly [pid 15480]
[INFO] [lifecycle_manager-17]: process has finished cleanly [pid 15482]
[INFO] [static_transform_publisher-10]: process has finished cleanly [pid 15378]
[INFO] [ekf_node-7]: process has finished cleanly [pid 15334]
[INFO] [imu_madgwick_filter.py-4]: process has finished cleanly [pid 15328]
[ERROR] [rviz2-20]: process has died [pid 15680, exit code -11, cmd '/opt/ros/humble/lib/rviz2/rviz2 -d /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/rviz/nav.rviz --ros-args -r __node:=rviz2'].
[INFO] [map_server-15]: process has finished cleanly [pid 15478]
[INFO] [velocity_pid.py-9]: process has finished cleanly [pid 15342]
[INFO] [cmd_vel_mux.py-8]: process has finished cleanly [pid 15336]
[component_container_isolated-18] [INFO] [1782382415.755361638] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-18] [INFO] [1782382415.755526472] [lifecycle_manager_navigation]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_navigation)
[component_container_isolated-18] [INFO] [1782382415.755802264] [lifecycle_manager_navigation]: Terminating bond timer...
[lifecycle_manager-17] [INFO] [1782382415.755375763] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-17] [INFO] [1782382415.755689055] [lifecycle_manager_keepout]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_keepout)
[lifecycle_manager-17] [INFO] [1782382415.755824055] [lifecycle_manager_keepout]: Terminating bond timer...
[aurora930_node-11] [INFO] [1782382415.755497305] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[static_transform_publisher-10] [INFO] [1782382415.755995264] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1782382415.759850854] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1782382415.760308813] [origincar_base]: Stop command sent to STM32 on shutdown.
[origincar_base_node-1] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[origincar_base_node-1] terminate called after throwing an instance of 'rclcpp::exceptions::RCLError'
[origincar_base_node-1]   what():  failed to create guard condition: the given context is not valid, either rcl_init() was not called or rcl_shutdown() was called., at ./src/rcl/guard_condition.c:67
[costmap_filter_info_server-16] [INFO] [1782382415.760828772] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-16] [INFO] [1782382415.761084064] [keepout_filter_info_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_filter_info_server)
[costmap_filter_info_server-16] [INFO] [1782382415.764732196] [keepout_filter_info_server]: Deactivating
[costmap_filter_info_server-16] [INFO] [1782382415.764873612] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-16] [INFO] [1782382415.796154374] [keepout_filter_info_server]: Cleaning up
[costmap_filter_info_server-16] [INFO] [1782382415.796381583] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-16] [INFO] [1782382415.990749747] [keepout_filter_info_server]: Destroying
[robot_state_publisher-3] [INFO] [1782382415.762420942] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[competition_master_stage3.py-19] [INFO] [1782382415.810159523] [competition_master_stage3]: [MAIN] 收到 Ctrl+C, 正在保存轨迹...
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782382415.878226930] [competition_master_stage3]: [TRAJ] CSV已保存: /userdata/dev_ws/trajectory_20260625_181335.csv (137 点)
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782382415.891905412] [competition_master_stage3]: [TRAJ] 摘要JSON已保存: /userdata/dev_ws/trajectory_20260625_181335_summary.json
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782382415.908790232] [competition_master_stage3]: [TRAJ] 规划历史已保存: /userdata/dev_ws/trajectory_20260625_181335_plans.csv (46 次规划)
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-19] [INFO] [1782382415.969636628] [competition_master_stage3]: [TRAJ] costmap PGM已保存: /userdata/dev_ws/trajectory_20260625_181335_costmap.pgm
[competition_master_stage3.py-19] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[map_server-15] [INFO] [1782382415.780004388] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-15] [INFO] [1782382415.780328847] [keepout_mask_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_mask_server)
[map_server-15] [INFO] [1782382415.780639264] [keepout_mask_server]: Deactivating
[map_server-15] [INFO] [1782382415.780743223] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[map_server-15] [INFO] [1782382415.791597033] [keepout_mask_server]: Cleaning up
[map_server-15] [INFO] [1782382415.791849908] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[map_server-15] [INFO] [1782382416.016913333] [keepout_mask_server]: Destroying
[aurora930_node-11] I0625 18:13:35.783182 15380 ros2_node.cc:90] process quit succeed
[aurora930_node-11] I0625 18:13:35.783385 15380 aurora900_ros2_device.cc:83] begin stop()
[aurora930_node-11] I0625 18:13:35.913527 15380 aurora900_ros2_device.cc:103] stop stream
[aurora930_node-11] 2026-06-25 18:13:36.009 ( 144.445s) [        94B94020]      aurora900_impl.cc:648   INFO| ir_stream_count_=0, rgb_stream_count_=0, depth_stream_count_=0
[aurora930_node-11] 2026-06-25 18:13:36.009 ( 144.445s) [        94B94020]      aurora900_impl.cc:649   INFO| mask=7
[aurora930_node-11] I0625 18:13:36.226548 15380 aurora900_ros2_device.cc:105] destroy stream
[aurora930_node-11] I0625 18:13:36.226773 15380 aurora900_ros2_device.cc:110] close glog
[aurora930_node-11] WARNING: Logging before InitGoogleLogging() is written to STDERR
[aurora930_node-11] I0625 18:13:36.226883 15380 ros2_device.cc:113] close device...
[aurora930_node-11] 2026-06-25 18:13:36.726 ( 145.162s) [        7D1D37E0]         cmd_backend.cc:40    INFO| RunBlocking is end!!!
[aurora930_node-11] 2026-06-25 18:13:36.927 ( 145.363s) [        94B94020]deptrum_camera_vendor.c:121   INFO| device is close.
[aurora930_node-11] I0625 18:13:36.929680 15380 ros2_device.cc:116] quit succeed
[ekf_node-7] [INFO] [1782382415.810295315] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-18] [INFO] [1782382416.000513889] [local_costmap.local_costmap]: Message Filter dropping message: frame 'laser_link' at time 1782382415.699 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-18] [INFO] [1782382416.369299183] [waypoint_follower]: Running Nav2 LifecycleNode rcl preshutdown (waypoint_follower)
[component_container_isolated-18] [INFO] [1782382416.369710767] [waypoint_follower]: Deactivating
[component_container_isolated-18] [INFO] [1782382416.369873434] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382416.380370535] [waypoint_follower]: Cleaning up
[component_container_isolated-18] [INFO] [1782382416.447312399] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382416.447470774] [velocity_smoother]: Running Nav2 LifecycleNode rcl preshutdown (velocity_smoother)
[component_container_isolated-18] [INFO] [1782382416.447611733] [velocity_smoother]: Deactivating
[component_container_isolated-18] [INFO] [1782382416.447767358] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382416.459291877] [velocity_smoother]: Cleaning up
[component_container_isolated-18] [INFO] [1782382416.460324921] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382416.460462296] [planner_server]: Running Nav2 LifecycleNode rcl preshutdown (planner_server)
[component_container_isolated-18] [INFO] [1782382416.460599421] [planner_server]: Deactivating
[component_container_isolated-18] [INFO] [1782382416.461116547] [global_costmap.global_costmap]: Deactivating
[component_container_isolated-18] [INFO] [1782382416.484601837] [planner_server]: Deactivating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1782382416.484954338] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382416.495404105] [planner_server]: Cleaning up
[component_container_isolated-18] [INFO] [1782382416.546294192] [global_costmap.global_costmap]: Cleaning up
[component_container_isolated-18] [INFO] [1782382416.567312936] [planner_server]: Cleaning up plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1782382416.568717022] [planner_server]: Destroying plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1782382416.603369622] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382416.603511498] [lifecycle_manager_localization]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_localization)
[component_container_isolated-18] [INFO] [1782382416.603607373] [lifecycle_manager_localization]: Terminating bond timer...
[component_container_isolated-18] [INFO] [1782382416.640813436] [amcl]: Running Nav2 LifecycleNode rcl preshutdown (amcl)
[component_container_isolated-18] [INFO] [1782382416.641051895] [amcl]: Deactivating
[component_container_isolated-18] [INFO] [1782382416.641207187] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382416.651531038] [amcl]: Cleaning up
[component_container_isolated-18] [INFO] [1782382416.692767650] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382416.692907816] [smoother_server]: Running Nav2 LifecycleNode rcl preshutdown (smoother_server)
[component_container_isolated-18] [INFO] [1782382416.693027733] [smoother_server]: Deactivating
[component_container_isolated-18] [INFO] [1782382416.693089817] [smoother_server]: Deactivating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1782382416.693232650] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382416.703674168] [smoother_server]: Cleaning up
[component_container_isolated-18] [INFO] [1782382416.703825710] [smoother_server]: Cleaning up smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1782382416.730012963] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382416.730180172] [bt_navigator]: Running Nav2 LifecycleNode rcl preshutdown (bt_navigator)
[component_container_isolated-18] [INFO] [1782382416.730347547] [bt_navigator]: Deactivating
[component_container_isolated-18] [INFO] [1782382416.730531380] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382416.740903523] [bt_navigator]: Cleaning up
[component_container_isolated-18] [INFO] [1782382417.140499119] [bt_navigator]: Completed Cleaning up
[component_container_isolated-18] [INFO] [1782382417.140820828] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382417.141090162] [map_server]: Running Nav2 LifecycleNode rcl preshutdown (map_server)
[component_container_isolated-18] [INFO] [1782382417.141302829] [map_server]: Deactivating
[component_container_isolated-18] [INFO] [1782382417.141501954] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382417.152020639] [map_server]: Cleaning up
[component_container_isolated-18] [INFO] [1782382417.152307598] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382417.152459598] [behavior_server]: Running Nav2 LifecycleNode rcl preshutdown (behavior_server)
[component_container_isolated-18] [INFO] [1782382417.152635265] [behavior_server]: Deactivating
[component_container_isolated-18] [INFO] [1782382417.152858890] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382417.163358783] [behavior_server]: Cleaning up
[component_container_isolated-18] [INFO] [1782382417.178392767] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382417.178630267] [controller_server]: Running Nav2 LifecycleNode rcl preshutdown (controller_server)
[component_container_isolated-18] [INFO] [1782382417.178784351] [controller_server]: Deactivating
[component_container_isolated-18] [INFO] [1782382417.178852309] [controller_server]: Deactivating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1782382417.179089768] [local_costmap.local_costmap]: Deactivating
[component_container_isolated-18] [INFO] [1782382417.217635917] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1782382417.228182977] [controller_server]: Cleaning up
[component_container_isolated-18] [INFO] [1782382417.228345310] [controller_server]: Cleaning up controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1782382417.228639186] [local_costmap.local_costmap]: Cleaning up
[lifecycle_manager-17] [INFO] [1782382416.059206905] [lifecycle_manager_keepout]: Destroying lifecycle_manager_keepout
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
[ERROR] [bmi088_iio_bridge.py-5]: process has died [pid 15330, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/bmi088_iio_bridge.py --ros-args -r __node:=bmi088_iio_bridge --params-file /tmp/launch_params_4s9yvqh5'].
[INFO] [competition_master_stage3.py-19]: process has finished cleanly [pid 15671]
[ERROR] [vision_ai_node-14]: process has died [pid 15388, exit code 1, cmd '/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node --ros-args -r __node:=vision_ai_node'].
[INFO] [aurora930_node-11]: process has finished cleanly [pid 15380]
[component_container_isolated-18] [INFO] [1782382418.297361376] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[ERROR] [component_container_isolated-18]: process[component_container_isolated-18] failed to terminate '5' seconds after receiving 'SIGINT', escalating to 'SIGTERM'
[INFO] [component_container_isolated-18]: sending signal 'SIGTERM' to process[component_container_isolated-18]
[component_container_isolated-18] [INFO] [1782382422.538028730] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [component_container_isolated-18]: process[component_container_isolated-18] failed to terminate '10.0' seconds after receiving 'SIGTERM', escalating to 'SIGKILL'
[INFO] [component_container_isolated-18]: sending signal 'SIGKILL' to process[component_container_isolated-18]
[ERROR] [component_container_isolated-18]: process has died [pid 15668, exit code -9, cmd '/opt/ros/humble/lib/rclcpp_components/component_container_isolated --ros-args --log-level info --ros-args -r __node:=nav2_container --params-file /tmp/launch_params_xqw9b6br --params-file /tmp/launch_params_g4wsl9vk -r /tf:=tf -r /tf_static:=tf_static'].
root@ubuntu:/userdata/dev_ws#
