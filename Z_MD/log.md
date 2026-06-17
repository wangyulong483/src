root@ubuntu:/userdata/dev_ws# ros2 launch origincar_bringup stage3_bringup.launch.py
[INFO] [launch]: All log files can be found below /root/.ros/log/2026-06-17-17-12-53-361669-ubuntu-47874
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [origincar_base_node-1]: process started with pid [47888]
[INFO] [lslidar_driver_node-2]: process started with pid [47890]
[INFO] [robot_state_publisher-3]: process started with pid [47892]
[INFO] [imu_madgwick_filter.py-4]: process started with pid [47894]
[INFO] [bmi088_iio_bridge.py-5]: process started with pid [47896]
[INFO] [imu_madgwick_filter.py-6]: process started with pid [47898]
[INFO] [ekf_node-7]: process started with pid [47900]
[INFO] [cmd_vel_mux.py-8]: process started with pid [47906]
[INFO] [velocity_pid.py-9]: process started with pid [47916]
[INFO] [static_transform_publisher-10]: process started with pid [47944]
[INFO] [aurora930_node-11]: process started with pid [47946]
[INFO] [qr_decoder-12]: process started with pid [47948]
[INFO] [qr_decision-13]: process started with pid [47950]
[INFO] [vision_ai_node-14]: process started with pid [47957]
[origincar_base_node-1] [INFO] [1781687574.052876711] [origincar_base]: origincar_base serial port opened
[lslidar_driver_node-2] [INFO] [1781687574.062861799] [lslidar_driver_node]: Lidar is N10
[lslidar_driver_node-2] [INFO] [1781687574.072026303] [lslidar_driver_node]: Initialised lslidar without error
[lslidar_driver_node-2] [INFO] [1781687574.072881179] [lslidar_driver_node]: Successfully initialize driver...
[robot_state_publisher-3] [INFO] [1781687574.058708589] [robot_state_publisher]: got segment base_footprint
[robot_state_publisher-3] [INFO] [1781687574.059074214] [robot_state_publisher]: got segment base_link
[robot_state_publisher-3] [INFO] [1781687574.059165672] [robot_state_publisher]: got segment gyro_link
[robot_state_publisher-3] [INFO] [1781687574.059215797] [robot_state_publisher]: got segment laser_link
[ekf_node-7] Both imu1_differential and imu1_relative were set to true. Using differential mode.
[static_transform_publisher-10] [INFO] [1781687574.307803576] [depth_camera_tf]: Spinning until stopped - publishing transform
[static_transform_publisher-10] translation: ('0.140000', '0.000000', '0.050000')
[static_transform_publisher-10] rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
[static_transform_publisher-10] from 'base_link' to 'depth_camera_link'
[aurora930_node-11] W0617 17:12:54.934513 47946 ros2_node.cc:35] hello aurora 900/930
[aurora930_node-11] 2026-06-17 17:12:55.103 (   0.296s) [        B5494020] device_manager_impl.cc:89    INFO| hotplug has registed by user
[aurora930_node-11] I0617 17:12:55.162386 47946 aurora900_ros2_device.cc:153] BOOT_ORDER_1::Found 1 deptrum device
[aurora930_node-11] I0617 17:12:55.162967 47946 aurora900_ros2_device.cc:162] BOOT_ORDER_1::No serial number provided: picking first device
[aurora930_node-11] 2026-06-17 17:12:55.163 (   0.356s) [        B5494020] device_manager_impl.cc:318   INFO| Device information:
[aurora930_node-11]     ir_pid:0x1930, rgb_pid:0x0
[aurora930_node-11]     serial number:HY400529001015314G00248
[aurora930_node-11] I0617 17:12:55.163164 47946 aurora900_ros2_device.cc:206] BOOT_ORDER_1::0:device start opening
[aurora930_node-11] 2026-06-17 17:12:55.165 (   0.358s) [        B5494020]   custom_usb_device.cc:101   INFO| bulk in endpoint addr:129
[aurora930_node-11] 2026-06-17 17:12:55.165 (   0.358s) [        B5494020]   custom_usb_device.cc:98    INFO| bulk out endpoint addr:2
[aurora930_node-11] 2026-06-17 17:12:55.187 (   0.380s) [        B5494020]deptrum_camera_aurora93:53    INFO| doe_broken:0 ito_support:1 crash_count:0 wdt_count:0 hard_reset_count:2 heart_boot_count:0 boot_total:103 last_crash_time:N
[aurora930_node-11] I0617 17:12:55.187417 47946 aurora900_ros2_device.cc:247] device supported frame_mode:
[aurora930_node-11] I0617 17:12:55.187525 47946 aurora900_ros2_device.cc:252] [0]:ir_mode:=13 kRes320x200Ir8Bit rgb_mode:=31 kRes320x200RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0617 17:12:55.187568 47946 aurora900_ros2_device.cc:252] [1]:ir_mode:=17 kRes480x300Depth16Bit rgb_mode:=32 kRes480x300RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0617 17:12:55.187601 47946 aurora900_ros2_device.cc:252] [2]:ir_mode:=20 kRes640x400Ir8Bit rgb_mode:=33 kRes640x400RgbYuv depth_mode:=0 kInvalid
[aurora930_node-11] I0617 17:12:55.187634 47946 aurora900_ros2_device.cc:266] current set mode ir_mode:20:kRes640x400Ir8Bit,rgb_mode:33:kRes640x400RgbYuv
[aurora930_node-11] device_count==========1
[INFO] [map_server-15]: process started with pid [48067]
[INFO] [costmap_filter_info_server-16]: process started with pid [48070]
[INFO] [lifecycle_manager-17]: process started with pid [48074]
[qr_decoder-12] [INFO] [1781687575.336313412] [qr_decoder_zbar]: QR decoder (ZBar) started: rgb=/aurora/rgb/image_raw, depth=/aurora/depth/image_raw, filter=on, range=[50, 4000]mm, min_qr_len=1, intrinsics: fx=421.3 fy=422.3 cx=320.3 cy=197.0
[map_server-15] [INFO] [1781687575.694700657] [keepout_mask_server]:
[map_server-15]         keepout_mask_server lifecycle node launched.
[map_server-15]         Waiting on external lifecycle transitions to activate
[map_server-15]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[map_server-15] [INFO] [1781687575.695241407] [keepout_mask_server]: Creating
[costmap_filter_info_server-16] [INFO] [1781687575.695850324] [costmap_filter_info_server]: This is costmap filter info publisher
[lifecycle_manager-17] [INFO] [1781687575.710933789] [lifecycle_manager_keepout]: Creating
[aurora930_node-11] I0617 17:12:55.726428 47946 aurora900_ros2_device.cc:387] Switch Auto Exposure
[lifecycle_manager-17] [INFO] [1781687575.775755776] [lifecycle_manager_keepout]: Creating and initializing lifecycle service clients
[aurora930_node-11] 2026-06-17 17:12:55.787 (   0.981s) [        B5494020]      aurora900_impl.cc:1106  INFO| SetHeartbeat user set heartbeat enable: 0
[costmap_filter_info_server-16] [INFO] [1781687575.917315506] [keepout_filter_info_server]:
[costmap_filter_info_server-16]         keepout_filter_info_server lifecycle node launched.
[costmap_filter_info_server-16]         Waiting on external lifecycle transitions to activate
[costmap_filter_info_server-16]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[lifecycle_manager-17] [INFO] [1781687575.965869320] [lifecycle_manager_keepout]: Starting managed nodes bringup...
[lifecycle_manager-17] [INFO] [1781687575.971353447] [lifecycle_manager_keepout]: Configuring keepout_mask_server
[map_server-15] [INFO] [1781687575.977240325] [keepout_mask_server]: Configuring
[map_server-15] [INFO] [1781687575.977532575] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.yaml
[map_server-15] [INFO] [1781687575.978666076] [map_io]: resolution: 0.05
[map_server-15] [INFO] [1781687575.978748826] [map_io]: origin[0]: -2.65
[map_server-15] [INFO] [1781687575.978780409] [map_io]: origin[1]: -4.5
[map_server-15] [INFO] [1781687575.978807992] [map_io]: origin[2]: 0
[map_server-15] [INFO] [1781687575.978837242] [map_io]: free_thresh: 0.5
[map_server-15] [INFO] [1781687575.978865492] [map_io]: occupied_thresh: 0.5
[map_server-15] [INFO] [1781687575.978903076] [map_io]: mode: scale
[map_server-15] [INFO] [1781687575.978934659] [map_io]: negate: 0
[map_server-15] [INFO] [1781687575.979693951] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm
[map_server-15] [INFO] [1781687576.029020848] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm: 163 X 141 map @ 0.05 m/cell
[lifecycle_manager-17] [INFO] [1781687576.067036740] [lifecycle_manager_keepout]: Configuring keepout_filter_info_server
[costmap_filter_info_server-16] [INFO] [1781687576.068230324] [keepout_filter_info_server]: Configuring
[lifecycle_manager-17] [INFO] [1781687576.088789500] [lifecycle_manager_keepout]: Activating keepout_mask_server
[map_server-15] [INFO] [1781687576.093549211] [keepout_mask_server]: Activating
[map_server-15] [INFO] [1781687576.093970461] [keepout_mask_server]: Creating bond (keepout_mask_server) to lifecycle manager.
[imu_madgwick_filter.py-4] [INFO] [1781687576.197458424] [imu_madgwick_filter]: [imu_madgwick] init: beta=0.0330, gyro_noise=0.0010, accel_noise=0.050
[aurora930_node-11] I0617 17:12:56.198571 47946 aurora900_ros2_device.cc:304] BOOT_ORDER_1::Device information:
[aurora930_node-11] I0617 17:12:56.198733 47946 aurora900_ros2_device.cc:305]    sdk version: 1.1.22
[aurora930_node-11] I0617 17:12:56.198776 47946 aurora900_ros2_device.cc:306]    device name: Aurora 930
[aurora930_node-11] I0617 17:12:56.198805 47946 aurora900_ros2_device.cc:307]    serial number: HY400529001015314G00248
[aurora930_node-11] I0617 17:12:56.198832 47946 aurora900_ros2_device.cc:308]    firmware version: 1.7.2
[aurora930_node-11] I0617 17:12:56.198887 47946 camera_parameters.cc:134] BOOT_ORDER_1::Camera Parameters:
[aurora930_node-11] I0617 17:12:56.198918 47946 camera_parameters.cc:135] BOOT_ORDER_1::         Ir Intrinsics:
[aurora930_node-11] I0617 17:12:56.198967 47946 camera_parameters.cc:146]                Resolution:
[aurora930_node-11] I0617 17:12:56.198997 47946 camera_parameters.cc:147]                        Rows:400
[aurora930_node-11] I0617 17:12:56.199031 47946 camera_parameters.cc:148]                        Cols:640
[aurora930_node-11] I0617 17:12:56.199057 47946 camera_parameters.cc:149]                Intrinsics:
[aurora930_node-11] I0617 17:12:56.199082 47946 camera_parameters.cc:150]                        fx: 421.307
[aurora930_node-11] I0617 17:12:56.199182 47946 camera_parameters.cc:151]                        fy: 422.254
[aurora930_node-11] I0617 17:12:56.199218 47946 camera_parameters.cc:152]                        cx: 320.27
[aurora930_node-11] I0617 17:12:56.199250 47946 camera_parameters.cc:153]                        cy: 197.01
[aurora930_node-11] I0617 17:12:56.202502 47946 camera_parameters.cc:154]                        k1: 0.0606853
[aurora930_node-11] I0617 17:12:56.202584 47946 camera_parameters.cc:155]                        k2: -0.10961
[aurora930_node-11] I0617 17:12:56.202620 47946 camera_parameters.cc:156]                        p1: 0.00126689
[aurora930_node-11] I0617 17:12:56.202653 47946 camera_parameters.cc:157]                        p2: -0.00120539
[aurora930_node-11] I0617 17:12:56.202685 47946 camera_parameters.cc:158]                        k3: 0.0522281
[aurora930_node-11] I0617 17:12:56.202716 47946 camera_parameters.cc:138] BOOT_ORDER_1::         Rgb Intrinsics:
[aurora930_node-11] I0617 17:12:56.202744 47946 camera_parameters.cc:146]                Resolution:
[aurora930_node-11] I0617 17:12:56.202768 47946 camera_parameters.cc:147]                        Rows:400
[aurora930_node-11] I0617 17:12:56.202795 47946 camera_parameters.cc:148]                        Cols:640
[aurora930_node-11] I0617 17:12:56.202819 47946 camera_parameters.cc:149]                Intrinsics:
[aurora930_node-11] I0617 17:12:56.202844 47946 camera_parameters.cc:150]                        fx: 416.49
[aurora930_node-11] I0617 17:12:56.203394 47946 camera_parameters.cc:151]                        fy: 417.383
[aurora930_node-11] I0617 17:12:56.204232 47946 camera_parameters.cc:152]                        cx: 316.832
[imu_madgwick_filter.py-4] [INFO] [1781687576.204253344] [imu_madgwick_filter]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-4] [INFO] [1781687576.208361554] [imu_madgwick_filter]: [imu_madgwick] accel init: roll=-0.1deg, pitch=-0.0deg
[lifecycle_manager-17] [INFO] [1781687576.207622053] [lifecycle_manager_keepout]: Server keepout_mask_server connected with bond.
[lifecycle_manager-17] [INFO] [1781687576.207789012] [lifecycle_manager_keepout]: Activating keepout_filter_info_server
[costmap_filter_info_server-16] [INFO] [1781687576.208946846] [keepout_filter_info_server]: Activating
[costmap_filter_info_server-16] [INFO] [1781687576.209194596] [keepout_filter_info_server]: Creating bond (keepout_filter_info_server) to lifecycle manager.
[aurora930_node-11] I0617 17:12:56.205193 47946 camera_parameters.cc:153]                        cy: 188.753
[aurora930_node-11] I0617 17:12:56.209965 47946 camera_parameters.cc:154]                        k1: 0.00611878
[aurora930_node-11] I0617 17:12:56.210035 47946 camera_parameters.cc:155]                        k2: -0.0490436
[aurora930_node-11] I0617 17:12:56.210071 47946 camera_parameters.cc:156]                        p1: 0.000399548
[aurora930_node-11] I0617 17:12:56.210103 47946 camera_parameters.cc:157]                        p2: 0.000563892
[aurora930_node-11] I0617 17:12:56.210135 47946 camera_parameters.cc:158]                        k3: 0.0308458
[aurora930_node-11] I0617 17:12:56.210167 47946 camera_parameters.cc:141] BOOT_ORDER_1::         Ir to Rgb Extrinsic:
[aurora930_node-11] I0617 17:12:56.210193 47946 camera_parameters.cc:162]                Extrinsics:
[aurora930_node-11] I0617 17:12:56.210219 47946 camera_parameters.cc:163]                        Rotation[0]: 0.999973, 0.00724076, -0.00112023
[aurora930_node-11] I0617 17:12:56.210255 47946 camera_parameters.cc:165]                        Rotation[1]: -0.00724006, 0.999973, 0.000633162
[aurora930_node-11] I0617 17:12:56.210291 47946 camera_parameters.cc:167]                        Rotation[2]: 0.00112478, -0.000625033, 0.999999
[aurora930_node-11] I0617 17:12:56.210382 47946 camera_parameters.cc:169]                        Translation: -9.88662, 0.117748, 0.603513
[aurora930_node-11] 2026-06-17 17:12:56.211 (   1.404s) [        B5494020]      aurora900_impl.cc:578   INFO| stream_mask_:0, rgb_stream_count_:1
[cmd_vel_mux.py-8] [INFO] [1781687576.219676559] [cmd_vel_mux]:   nav: /nav_cmd_vel priority=10 timeout=0.5s
[cmd_vel_mux.py-8] [INFO] [1781687576.247397863] [cmd_vel_mux]:   pid: /pid_cmd_vel priority=20 timeout=0.3s
[cmd_vel_mux.py-8] [INFO] [1781687576.269502789] [cmd_vel_mux]:   stop: /stop_cmd_vel priority=255 timeout=0.5s
[bmi088_iio_bridge.py-5] [INFO] [1781687576.274064375] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1781687576.278255335] [bmi088_iio_bridge]:   DIAGNOSTIC: Scanning IIO devices under /sys/bus/iio/devices/
[bmi088_iio_bridge.py-5] [INFO] [1781687576.282117753] [bmi088_iio_bridge]:   Equivalent to: ls /sys/bus/iio/devices/*/name
[cmd_vel_mux.py-8] [INFO] [1781687576.284303379] [cmd_vel_mux]: cmd_vel_mux 就绪: 输出 → /cmd_vel_muxed
[bmi088_iio_bridge.py-5] [INFO] [1781687576.285330713] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1781687576.289264673] [bmi088_iio_bridge]:   iio:device0/name = "34190000.adc"
[bmi088_iio_bridge.py-5] [INFO] [1781687576.292384800] [bmi088_iio_bridge]:   iio:device1/name = "bmi08x"
[bmi088_iio_bridge.py-5] [INFO] [1781687576.295152926] [bmi088_iio_bridge]:   trigger0/name = "34190000.adc-dev0"
[bmi088_iio_bridge.py-5] [INFO] [1781687576.297787427] [bmi088_iio_bridge]:   Total IIO devices found: 3
[bmi088_iio_bridge.py-5] [INFO] [1781687576.300596095] [bmi088_iio_bridge]:   BMI088 kernel module APPEARS LOADED: 1 BMI device(s) detected
[bmi088_iio_bridge.py-5] [INFO] [1781687576.303647263] [bmi088_iio_bridge]:   BMI device names: ['bmi08x']
[bmi088_iio_bridge.py-5] [INFO] [1781687576.308446557] [bmi088_iio_bridge]:   gyro:  /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_anglvel is_si=False scale_override=0.00053
[bmi088_iio_bridge.py-5] [INFO] [1781687576.312237559] [bmi088_iio_bridge]:   accel: /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_accel is_si=False scale_override=0.00341
[cmd_vel_mux.py-8] [INFO] [1781687576.319151228] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[lifecycle_manager-17] [INFO] [1781687576.319406020] [lifecycle_manager_keepout]: Server keepout_filter_info_server connected with bond.
[lifecycle_manager-17] [INFO] [1781687576.319538895] [lifecycle_manager_keepout]: Managed nodes are active
[lifecycle_manager-17] [INFO] [1781687576.319618770] [lifecycle_manager_keepout]: Creating bond timer...
[imu_madgwick_filter.py-6] [INFO] [1781687576.363889373] [imu_madgwick_bmi088]: [imu_madgwick] init: beta=0.0030, gyro_noise=0.0002, accel_noise=0.010
[bmi088_iio_bridge.py-5] [INFO] [1781687576.434725655] [bmi088_iio_bridge]: BMI088 IIO Bridge 启动 @ 100Hz -> /imu_data  [OK]
[imu_madgwick_filter.py-6] [INFO] [1781687576.459186666] [imu_madgwick_bmi088]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-6] [INFO] [1781687576.461787751] [imu_madgwick_bmi088]: [imu_madgwick] accel init: roll=-2.3deg, pitch=-3.4deg
[velocity_pid.py-9] [INFO] [1781687576.481392093] [velocity_pid]: VelocityPID 就绪: vx(Kp=0.8, Ki=0.60, Kd=0.05, max_i=0.68) wz(Kp=1.0, Ki=0.40, Kd=0.02, max_i=2.24) | feedback_timeout=0.5s
[velocity_pid.py-9] [INFO] [1781687576.490876430] [velocity_pid]: [vel_pid] ACTIVATED vx=0.00 wz=0.00
[aurora930_node-11] 2026-06-17 17:12:56.556 (   1.750s) [        819E37E0]deptrum_camera_aurora93:407    ERR| recv first frame time is 1781687576556
[qr_decision-13] [INFO] [1781687576.585372681] [qr_decision]: qr_decision started: cooldown=3.0s, awaiting /sign from qr_decoder
[INFO] [component_container_isolated-18]: process started with pid [48245]
[lslidar_driver_node-2] port = /dev/ttyACM1, baud_rate = 230400
[lslidar_driver_node-2] open_port /dev/ttyACM1 OK !
[vision_ai_node-14] [INFO] [1781687580.397605139] [vision_ai_node]: 成功加载配置文件: /userdata/dev_ws/install/racing_vision_ai/share/racing_vision_ai/config/vision_ai_config.yaml
[vision_ai_node-14] [INFO] [1781687580.764490345] [vision_ai_node]: Volcengine Ark client initialized successfully
[vision_ai_node-14] [INFO] [1781687580.779354477] [vision_ai_node]: Vision AI Node initialized
[vision_ai_node-14] [INFO] [1781687580.782003894] [vision_ai_node]: Waiting for sign4return=100 signal...
[vision_ai_node-14] [INFO] [1781687580.784425437] [vision_ai_node]: Results will be published to vlm_result
[bmi088_iio_bridge.py-5] [INFO] [1781687582.138704293] [bmi088_iio_bridge]:   gyro bias calibrated: (0.002700, 0.001179, -0.002653) rad/s
[INFO] [competition_master_stage3.py-20]: process started with pid [48251]
[INFO] [lidar_cone_detector.py-19]: process started with pid [48247]
[INFO] [rviz2-21]: process started with pid [48260]
[component_container_isolated-18] [INFO] [1781687582.444632513] [nav2_container]: Load Library: /opt/ros/humble/lib/libcontroller_server_core.so
[component_container_isolated-18] [INFO] [1781687582.474894027] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-18] [INFO] [1781687582.475093443] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-18] [INFO] [1781687582.578199239] [controller_server]:
[component_container_isolated-18]       controller_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781687582.608971336] [controller_server]: Creating controller server
[component_container_isolated-18] [INFO] [1781687582.721558053] [local_costmap.local_costmap]:
[component_container_isolated-18]       local_costmap lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781687582.725962764] [local_costmap.local_costmap]: Creating Costmap
[component_container_isolated-18] [INFO] [1781687582.769039366] [nav2_container]: Load Library: /opt/ros/humble/lib/libmap_server_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/controller_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781687582.828876310] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::CostmapFilterInfoServer>
[component_container_isolated-18] [INFO] [1781687582.829903602] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapSaver>
[component_container_isolated-18] [INFO] [1781687582.830034519] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-18] [INFO] [1781687582.830085644] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-18] [INFO] [1781687582.931642022] [map_server]:
[component_container_isolated-18]       map_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781687582.932112106] [map_server]: Creating
[component_container_isolated-18] [INFO] [1781687582.940129401] [nav2_container]: Load Library: /opt/ros/humble/lib/libsmoother_server_core.so
[component_container_isolated-18] [INFO] [1781687582.946946321] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/map_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781687582.947137279] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-18] [INFO] [1781687583.100592223] [smoother_server]:
[component_container_isolated-18]       smoother_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781687583.111472394] [smoother_server]: Creating smoother server
[component_container_isolated-18] [INFO] [1781687583.122932941] [nav2_container]: Load Library: /opt/ros/humble/lib/libamcl_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/smoother_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781687583.141449741] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-18] [INFO] [1781687583.141623950] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-18] [INFO] [1781687583.220433818] [amcl]:
[component_container_isolated-18]       amcl lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781687583.224822112] [amcl]: Creating
[component_container_isolated-18] [INFO] [1781687583.312866443] [nav2_container]: Load Library: /opt/ros/humble/lib/libplanner_server_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/amcl' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781687583.319234779] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-18] [INFO] [1781687583.319476487] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-18] [INFO] [1781687583.383183099] [planner_server]:
[component_container_isolated-18]       planner_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781687583.395288271] [planner_server]: Creating
[component_container_isolated-18] [INFO] [1781687583.474934598] [global_costmap.global_costmap]:
[component_container_isolated-18]       global_costmap lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781687583.477370641] [global_costmap.global_costmap]: Creating Costmap
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/planner_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781687583.511147948] [nav2_container]: Load Library: /opt/ros/humble/lib/libnav2_lifecycle_manager_core.so
[component_container_isolated-18] [INFO] [1781687583.516526950] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781687583.516780326] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781687583.593139110] [lifecycle_manager_localization]: Creating
[component_container_isolated-18] [INFO] [1781687583.611787201] [nav2_container]: Load Library: /opt/ros/humble/lib/libbehavior_server_core.so
[component_container_isolated-18] [INFO] [1781687583.613859369] [lifecycle_manager_localization]: Creating and initializing lifecycle service clients
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_localization' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781687583.633188211] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-18] [INFO] [1781687583.633364753] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-18] [INFO] [1781687583.677533939] [lifecycle_manager_localization]: Starting managed nodes bringup...
[component_container_isolated-18] [INFO] [1781687583.677775939] [lifecycle_manager_localization]: Configuring map_server
[component_container_isolated-18] [INFO] [1781687583.679787440] [map_server]: Configuring
[component_container_isolated-18] [INFO] [1781687583.680091898] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.yaml
[component_container_isolated-18] [INFO] [1781687583.681262149] [map_io]: resolution: 0.05
[component_container_isolated-18] [INFO] [1781687583.681370607] [map_io]: origin[0]: -2.65
[component_container_isolated-18] [INFO] [1781687583.681416107] [map_io]: origin[1]: -4.5
[component_container_isolated-18] [INFO] [1781687583.681449899] [map_io]: origin[2]: 0
[component_container_isolated-18] [INFO] [1781687583.681482441] [map_io]: free_thresh: 0.25
[component_container_isolated-18] [INFO] [1781687583.681512357] [map_io]: occupied_thresh: 0.65
[component_container_isolated-18] [INFO] [1781687583.681562232] [map_io]: mode: trinary
[component_container_isolated-18] [INFO] [1781687583.681594149] [map_io]: negate: 0
[component_container_isolated-18] [INFO] [1781687583.682366566] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm
[component_container_isolated-18] [INFO] [1781687583.721295625] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm: 163 X 141 map @ 0.05 m/cell
[component_container_isolated-18] [INFO] [1781687583.734368214] [behavior_server]:
[component_container_isolated-18]       behavior_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781687583.761221601] [lifecycle_manager_localization]: Configuring amcl
[component_container_isolated-18] [INFO] [1781687583.762082602] [amcl]: Configuring
[component_container_isolated-18] [INFO] [1781687583.762542144] [amcl]: initTransforms
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/behavior_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781687583.806983038] [nav2_container]: Load Library: /opt/ros/humble/lib/libbt_navigator_core.so
[component_container_isolated-18] [INFO] [1781687583.815333209] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-18] [INFO] [1781687583.815504584] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-18] [INFO] [1781687583.840668137] [amcl]: initPubSub
[component_container_isolated-18] [INFO] [1781687583.876321194] [amcl]: Subscribed to map topic.
[component_container_isolated-18] [INFO] [1781687583.907548500] [lifecycle_manager_localization]: Activating map_server
[component_container_isolated-18] [INFO] [1781687583.908460834] [map_server]: Activating
[component_container_isolated-18] [INFO] [1781687583.908908001] [map_server]: Creating bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687583.913991086] [amcl]: Received a 163 X 141 map @ 0.050 m/pix
[component_container_isolated-18] [INFO] [1781687583.961942358] [bt_navigator]:
[component_container_isolated-18]       bt_navigator lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781687583.963644067] [bt_navigator]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/bt_navigator' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781687583.990075495] [nav2_container]: Load Library: /opt/ros/humble/lib/libwaypoint_follower_core.so
[component_container_isolated-18] [INFO] [1781687583.993233122] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-18] [INFO] [1781687583.993395705] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-18] [INFO] [1781687584.025931886] [lifecycle_manager_localization]: Server map_server connected with bond.
[component_container_isolated-18] [INFO] [1781687584.026145428] [lifecycle_manager_localization]: Activating amcl
[component_container_isolated-18] [INFO] [1781687584.027091137] [amcl]: Activating
[component_container_isolated-18] [INFO] [1781687584.027356262] [amcl]: initialPoseReceived
[component_container_isolated-18] [INFO] [1781687584.027883804] [amcl]: Setting pose (1781687584.027878): -1.985 -0.014 0.262
[component_container_isolated-18] [INFO] [1781687584.030389388] [amcl]: Creating bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687584.102196962] [amcl]: createLaserObject
[component_container_isolated-18] [INFO] [1781687584.139638895] [waypoint_follower]:
[component_container_isolated-18]       waypoint_follower lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781687584.154072902] [lifecycle_manager_localization]: Server amcl connected with bond.
[component_container_isolated-18] [INFO] [1781687584.154275694] [lifecycle_manager_localization]: Managed nodes are active
[component_container_isolated-18] [INFO] [1781687584.154389277] [lifecycle_manager_localization]: Creating bond timer...
[component_container_isolated-18] [INFO] [1781687584.158588196] [waypoint_follower]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/waypoint_follower' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781687584.186018874] [nav2_container]: Load Library: /opt/ros/humble/lib/libvelocity_smoother_core.so
[component_container_isolated-18] [INFO] [1781687584.189492584] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-18] [INFO] [1781687584.189657376] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-18] [INFO] [1781687584.300523301] [velocity_smoother]:
[component_container_isolated-18]       velocity_smoother lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/velocity_smoother' in container '/nav2_container'
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1781687584.319472392] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781687584.319635559] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1781687584.437148362] [lifecycle_manager_navigation]: Creating
[component_container_isolated-18] [INFO] [1781687584.466355541] [lifecycle_manager_navigation]: Creating and initializing lifecycle service clients
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_navigation' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1781687584.579637467] [lifecycle_manager_navigation]: Starting managed nodes bringup...
[component_container_isolated-18] [INFO] [1781687584.579916634] [lifecycle_manager_navigation]: Configuring controller_server
[component_container_isolated-18] [INFO] [1781687584.582702968] [controller_server]: Configuring controller interface
[component_container_isolated-18] [INFO] [1781687584.583668719] [controller_server]: getting goal checker plugins..
[component_container_isolated-18] [INFO] [1781687584.584784428] [controller_server]: Controller frequency set to 10.0000Hz
[component_container_isolated-18] [INFO] [1781687584.585083219] [local_costmap.local_costmap]: Configuring
[component_container_isolated-18] [INFO] [1781687584.641153411] [local_costmap.local_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781687584.673956801] [local_costmap.local_costmap]: Subscribed to Topics: scan aurora_points
[component_container_isolated-18] [INFO] [1781687584.799921774] [local_costmap.local_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781687584.800112732] [local_costmap.local_costmap]: Using plugin "keepout_filter"
[lidar_cone_detector.py-19] [INFO] [1781687584.806053318] [lidar_cone_detector]: [lidar_cone] map+cluster mode: channel=[0.3,3.5]x[-2.5,1.5] cluster=0.3m min=2pts debounce=5
[component_container_isolated-18] [INFO] [1781687584.830646371] [local_costmap.local_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781687584.831130579] [local_costmap.local_costmap]: Using plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781687584.855957674] [local_costmap.local_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781687584.933916833] [controller_server]: Created progress_checker : progress_checker of type nav2_controller::SimpleProgressChecker
[component_container_isolated-18] [INFO] [1781687584.945370880] [controller_server]: Created goal checker : goal_checker of type nav2_controller::SimpleGoalChecker
[component_container_isolated-18] [INFO] [1781687584.959716345] [controller_server]: Controller Server has goal_checker  goal checkers available.
[component_container_isolated-18] [INFO] [1781687584.964534805] [controller_server]: Created controller : FollowPath of type nav2_regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781687585.054119345] [controller_server]: Controller Server has FollowPath  controllers available.
[component_container_isolated-18] [INFO] [1781687585.107627119] [lifecycle_manager_navigation]: Configuring smoother_server
[component_container_isolated-18] [INFO] [1781687585.108498911] [smoother_server]: Configuring smoother server
[competition_master_stage3.py-20] [INFO] [1781687585.141139968] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-20] [INFO] [1781687585.148566929] [competition_master_stage3]: === [Stage 3] 总控节点初始化 ===
[competition_master_stage3.py-20] [INFO] [1781687585.151571347] [competition_master_stage3]:   QR点:    (0.41, -3.17, yaw=0.00)
[competition_master_stage3.py-20] [INFO] [1781687585.156187391] [competition_master_stage3]:   通道入口: (0.38, -1.10, yaw=0.00)
[competition_master_stage3.py-20] [INFO] [1781687585.159376101] [competition_master_stage3]:   P点:     (-1.99, -0.01, yaw=0.26)
[competition_master_stage3.py-20] [INFO] [1781687585.162854561] [competition_master_stage3]:   cruise_cw: 3 路点 → VLM=(3.12, -1.34)
[competition_master_stage3.py-20] [INFO] [1781687585.165884312] [competition_master_stage3]:   cruise_ccw: 3 路点 → VLM=(2.10, 0.92)
[competition_master_stage3.py-20] [INFO] [1781687585.169281230] [competition_master_stage3]:   超时: total=180.0s QR=90.0s entry=60.0s cruise=180.0s vlm=30.0s return=120.0s
[competition_master_stage3.py-20] [INFO] [1781687585.175303525] [competition_master_stage3]:   回退QR方向: 逆时针
[competition_master_stage3.py-20] [INFO] [1781687585.178782526] [competition_master_stage3]:   VLM结果话题: vlm_result
[competition_master_stage3.py-20] [INFO] [1781687585.182086528] [competition_master_stage3]: ============================================================
[component_container_isolated-18] [INFO] [1781687585.203949912] [smoother_server]: Created smoother : SmoothPath of type nav2_constrained_smoother/ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781687585.246794765] [smoother_server]: Smoother Server has SmoothPath  smoothers available.
[component_container_isolated-18] [INFO] [1781687585.288082658] [lifecycle_manager_navigation]: Configuring planner_server
[component_container_isolated-18] [INFO] [1781687585.289094075] [planner_server]: Configuring
[component_container_isolated-18] [INFO] [1781687585.289375325] [global_costmap.global_costmap]: Configuring
[component_container_isolated-18] [INFO] [1781687585.322738340] [global_costmap.global_costmap]: Using plugin "static_layer"
[component_container_isolated-18] [INFO] [1781687585.332786595] [global_costmap.global_costmap]: Subscribing to the map topic (/map) with transient local durability
[component_container_isolated-18] [INFO] [1781687585.339889056] [global_costmap.global_costmap]: Initialized plugin "static_layer"
[component_container_isolated-18] [INFO] [1781687585.340054056] [global_costmap.global_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781687585.353938271] [global_costmap.global_costmap]: Subscribed to Topics: scan aurora_points
[component_container_isolated-18] [INFO] [1781687585.428157554] [global_costmap.global_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1781687585.428350846] [global_costmap.global_costmap]: Using plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781687585.442403269] [global_costmap.global_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1781687585.442585560] [global_costmap.global_costmap]: Using plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781687585.454878899] [global_costmap.global_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1781687585.498033044] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 163 X 141 at 0.050000 m/pix
[component_container_isolated-18] [INFO] [1781687585.523439847] [planner_server]: Created global planner plugin GridBased of type nav2_smac_planner/SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781687585.523662472] [planner_server]: Configuring GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781687585.571147410] [planner_server]: Even sized heuristic lookup table size set 200.000000, increasing size by 1 to make odd
[lidar_cone_detector.py-19] [INFO] [1781687585.977695883] [lidar_cone_detector]: [lidar_cone] cone→CONE_DETECTED
[imu_madgwick_filter.py-4] [INFO] [1781687586.003192311] [imu_madgwick_filter]: [imu_madgwick ->] msgs=200 q_w=0.9992 angle=4.5deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781687586.174608804] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=421 q_w=0.9993 angle=4.2deg beta=0.0030
[qr_decoder-12] [INFO] [1781687592.910965345] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=200 last_qr_frame=-1 gap=-1 frames rejects=0
[imu_madgwick_filter.py-4] [INFO] [1781687596.003128927] [imu_madgwick_filter]: [imu_madgwick ->] msgs=400 q_w=0.9970 angle=8.9deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781687596.177170963] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1040 q_w=0.9993 angle=4.2deg beta=0.0030
[component_container_isolated-18] [INFO] [1781687599.700915066] [planner_server]: Configured plugin GridBased of type SmacPlannerHybrid with maximum iterations 1500, max on approach iterations 300, and not allowing unknown traversal. Tolerance 0.50.Using motion model: Reeds-Shepp.
[component_container_isolated-18] [INFO] [1781687599.701154483] [planner_server]: Planner Server has GridBased  planners available.
[component_container_isolated-18] [INFO] [1781687599.760527718] [lifecycle_manager_navigation]: Configuring behavior_server
[component_container_isolated-18] [INFO] [1781687599.761381718] [behavior_server]: Configuring
[component_container_isolated-18] [INFO] [1781687599.789881231] [behavior_server]: Creating behavior plugin spin of type nav2_behaviors/Spin
[component_container_isolated-18] [INFO] [1781687599.794351358] [behavior_server]: Configuring spin
[component_container_isolated-18] [INFO] [1781687599.831228874] [behavior_server]: Creating behavior plugin backup of type nav2_behaviors/BackUp
[component_container_isolated-18] [INFO] [1781687599.835576709] [behavior_server]: Configuring backup
[component_container_isolated-18] [INFO] [1781687599.866055640] [behavior_server]: Creating behavior plugin drive_on_heading of type nav2_behaviors/DriveOnHeading
[component_container_isolated-18] [INFO] [1781687599.870173141] [behavior_server]: Configuring drive_on_heading
[component_container_isolated-18] [INFO] [1781687599.906821616] [behavior_server]: Creating behavior plugin wait of type nav2_behaviors/Wait
[component_container_isolated-18] [INFO] [1781687599.911369410] [behavior_server]: Configuring wait
[component_container_isolated-18] [INFO] [1781687599.940274381] [lifecycle_manager_navigation]: Configuring bt_navigator
[component_container_isolated-18] [INFO] [1781687599.941117673] [bt_navigator]: Configuring
[competition_master_stage3.py-20] [INFO] [1781687600.129524256] [competition_master_stage3]: [LAUNCH] 发车阶段: 15.2s
[competition_master_stage3.py-20] [INFO] [1781687600.140761428] [competition_master_stage3]: >>> 系统就绪, 开始 Stage 3 导航
[competition_master_stage3.py-20] [INFO] [1781687600.144509555] [competition_master_stage3]: [状态机] INIT → NAV_TO_QR
[competition_master_stage3.py-20] [INFO] [1781687600.149630932] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-18] [INFO] [1781687600.374437865] [lifecycle_manager_navigation]: Configuring waypoint_follower
[component_container_isolated-18] [INFO] [1781687600.375590032] [waypoint_follower]: Configuring
[competition_master_stage3.py-20] [WARN] [1781687600.392027414] [competition_master_stage3]: 导航目标被拒绝, 3s 后重试...
[component_container_isolated-18] [INFO] [1781687600.456100359] [waypoint_follower]: Created waypoint_task_executor : wait_at_waypoint of type nav2_waypoint_follower::WaitAtWaypoint
[component_container_isolated-18] [INFO] [1781687600.462393779] [lifecycle_manager_navigation]: Configuring velocity_smoother
[component_container_isolated-18] [INFO] [1781687600.463272987] [velocity_smoother]: Configuring velocity smoother
[component_container_isolated-18] [INFO] [1781687600.497323419] [lifecycle_manager_navigation]: Activating controller_server
[component_container_isolated-18] [INFO] [1781687600.500651379] [controller_server]: Activating
[component_container_isolated-18] [INFO] [1781687600.500988379] [local_costmap.local_costmap]: Activating
[component_container_isolated-18] [INFO] [1781687600.501113837] [local_costmap.local_costmap]: Checking transform
[component_container_isolated-18] [INFO] [1781687600.501535338] [local_costmap.local_costmap]: start
[component_container_isolated-18] [INFO] [1781687600.516611886] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781687600.526175890] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781687600.526365349] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781687600.533357810] [local_costmap.local_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[component_container_isolated-18] [INFO] [1781687600.827115482] [controller_server]: Activating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781687600.827396190] [controller_server]: Creating bond (controller_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687600.951105412] [lifecycle_manager_navigation]: Server controller_server connected with bond.
[component_container_isolated-18] [INFO] [1781687600.951295203] [lifecycle_manager_navigation]: Activating smoother_server
[component_container_isolated-18] [INFO] [1781687600.952539079] [smoother_server]: Activating
[component_container_isolated-18] [INFO] [1781687600.952782329] [smoother_server]: Activating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781687600.952893079] [smoother_server]: Creating bond (smoother_server) to lifecycle manager.
[competition_master_stage3.py-20] [INFO] [1781687601.017432441] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.01,-0.02) yaw=15deg cmd=(vx=0.00 wz=0.00) elapsed=0.8s cpuFreq=1500MHz cpuT=71C cpu=44% mem=18%
[component_container_isolated-18] [INFO] [1781687601.070332381] [lifecycle_manager_navigation]: Server smoother_server connected with bond.
[component_container_isolated-18] [INFO] [1781687601.070509048] [lifecycle_manager_navigation]: Activating planner_server
[component_container_isolated-18] [INFO] [1781687601.071329465] [planner_server]: Activating
[component_container_isolated-18] [INFO] [1781687601.071572590] [global_costmap.global_costmap]: Activating
[component_container_isolated-18] [INFO] [1781687601.071639215] [global_costmap.global_costmap]: Checking transform
[component_container_isolated-18] [INFO] [1781687601.071941840] [global_costmap.global_costmap]: start
[component_container_isolated-18] [INFO] [1781687601.076809509] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1781687601.092727766] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1781687601.092998891] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781687601.098972060] [global_costmap.global_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[component_container_isolated-18] [INFO] [1781687602.133525143] [planner_server]: Activating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781687602.159440738] [planner_server]: Creating bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687602.286629169] [lifecycle_manager_navigation]: Server planner_server connected with bond.
[component_container_isolated-18] [INFO] [1781687602.286825586] [lifecycle_manager_navigation]: Activating behavior_server
[component_container_isolated-18] [INFO] [1781687602.288198753] [behavior_server]: Activating
[component_container_isolated-18] [INFO] [1781687602.288360462] [behavior_server]: Activating spin
[component_container_isolated-18] [INFO] [1781687602.288529420] [behavior_server]: Activating backup
[component_container_isolated-18] [INFO] [1781687602.288618962] [behavior_server]: Activating drive_on_heading
[component_container_isolated-18] [INFO] [1781687602.288694878] [behavior_server]: Activating wait
[component_container_isolated-18] [INFO] [1781687602.288776420] [behavior_server]: Creating bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687602.428052565] [lifecycle_manager_navigation]: Server behavior_server connected with bond.
[component_container_isolated-18] [INFO] [1781687602.428220107] [lifecycle_manager_navigation]: Activating bt_navigator
[component_container_isolated-18] [INFO] [1781687602.429180691] [bt_navigator]: Activating
[component_container_isolated-18] [WARN] [1781687602.526373234] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781687602.609708437] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781687602.665997462] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781687602.784953223] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1781687602.985237770] [bt_navigator_navigate_to_pose_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[competition_master_stage3.py-20] [INFO] [1781687603.039301544] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.01,-0.02) yaw=15deg cmd=(vx=0.00 wz=0.00) elapsed=2.8s cpuFreq=1500MHz cpuT=72C cpu=100% mem=18%
[component_container_isolated-18] [INFO] [1781687603.150721385] [bt_navigator]: Creating bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687603.269416479] [lifecycle_manager_navigation]: Server bt_navigator connected with bond.
[component_container_isolated-18] [INFO] [1781687603.269586937] [lifecycle_manager_navigation]: Activating waypoint_follower
[component_container_isolated-18] [INFO] [1781687603.270718313] [waypoint_follower]: Activating
[component_container_isolated-18] [INFO] [1781687603.270960730] [waypoint_follower]: Creating bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687603.389092990] [lifecycle_manager_navigation]: Server waypoint_follower connected with bond.
[component_container_isolated-18] [INFO] [1781687603.389290157] [lifecycle_manager_navigation]: Activating velocity_smoother
[component_container_isolated-18] [INFO] [1781687603.392816742] [velocity_smoother]: Activating
[component_container_isolated-18] [INFO] [1781687603.393148159] [velocity_smoother]: Creating bond (velocity_smoother) to lifecycle manager.
[competition_master_stage3.py-20] [INFO] [1781687603.398863953] [competition_master_stage3]: 重试发送导航目标 (QR点)...
[competition_master_stage3.py-20] [INFO] [1781687603.407517290] [competition_master_stage3]: [DIAG] nav目标距离: 3.97m, robot=(-2.01,-0.02) → target=(0.41,-3.17)
[competition_master_stage3.py-20] [INFO] [1781687603.416413252] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-18] [INFO] [1781687603.427207632] [bt_navigator]: Begin navigating from current location (-2.01, -0.02) to (0.41, -3.17)
[competition_master_stage3.py-20] [INFO] [1781687603.433613551] [competition_master_stage3]: 导航目标已接受，车辆出发...
[component_container_isolated-18] [INFO] [1781687603.516628921] [lifecycle_manager_navigation]: Server velocity_smoother connected with bond.
[component_container_isolated-18] [INFO] [1781687603.516796588] [lifecycle_manager_navigation]: Managed nodes are active
[component_container_isolated-18] [INFO] [1781687603.516859505] [lifecycle_manager_navigation]: Creating bond timer...
[component_container_isolated-18] [WARN] [1781687604.092431051] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.5123 Hz
[component_container_isolated-18] [INFO] [1781687604.229228778] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-18] [WARN] [1781687604.229510736] [controller_server]: No goal checker was specified in parameter 'current_goal_checker'. Server will use only plugin loaded goal_checker . This warning will appear once.
[cmd_vel_mux.py-8] [INFO] [1781687604.257480541] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=-0.12
[velocity_pid.py-9] [INFO] [1781687604.288272346] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.17 err=100.0%
[competition_master_stage3.py-20] [INFO] [1781687605.021744170] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.01,-0.02) yaw=15deg cmd=(vx=0.50 wz=-1.44) elapsed=4.8s plan[31pts 4.4m] (-2.00,-0.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=72C cpu=86% mem=18%
[component_container_isolated-18] Reallocing temp weights 301 - 60
[imu_madgwick_filter.py-4] [INFO] [1781687606.005240646] [imu_madgwick_filter]: [imu_madgwick ->] msgs=599 q_w=0.9589 angle=33.0deg beta=0.0330
[component_container_isolated-18] [WARN] [1781687606.086069140] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3228 Hz
[rviz2-21] [INFO] [1781687606.131428535] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-21] [INFO] [1781687606.132351202] [rviz2]: OpenGl version: 4.5 (GLSL 4.5)
[imu_madgwick_filter.py-6] [INFO] [1781687606.175872763] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1581 q_w=0.9132 angle=48.1deg beta=0.0030
[component_container_isolated-18] [INFO] [1781687606.229774578] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687606.354664133] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.01 -> current=-0.11 dt=0.0337s, resetting
[rviz2-21] [INFO] [1781687606.721200128] [rviz2]: Stereo is NOT SUPPORTED
[competition_master_stage3.py-20] [INFO] [1781687607.013548924] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.42,-0.23) yaw=-32deg cmd=(vx=0.50 wz=-0.15) elapsed=6.8s plan[27pts 3.7m] (-1.50,-0.15)→(0.40,-3.15) cpuFreq=1500MHz cpuT=72C cpu=75% mem=19%
[velocity_pid.py-9] [INFO] [1781687607.290522380] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.10 -> current=0.03 dt=0.0360s, resetting
[velocity_pid.py-9] [INFO] [1781687607.305769220] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.02 err=22.7%
[lidar_cone_detector.py-19] [INFO] [1781687607.311749847] [lidar_cone_detector]: [lidar_cone] no_cone→CLEAR
[cmd_vel_mux.py-8] [INFO] [1781687607.326134604] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.15
[velocity_pid.py-9] [INFO] [1781687607.555074538] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0334s, resetting
[component_container_isolated-18] [WARN] [1781687608.084468271] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3287 Hz
[component_container_isolated-18] [INFO] [1781687608.229762419] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781687608.319518250] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.20
[velocity_pid.py-9] [INFO] [1781687608.323325335] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.09 corrected=-0.24 err=59.5%
[velocity_pid.py-9] [INFO] [1781687608.454334434] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0333s, resetting
[qr_decoder-12] [INFO] [1781687608.884268707] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=400 last_qr_frame=-1 gap=-1 frames rejects=0
[competition_master_stage3.py-20] [INFO] [1781687609.014203348] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.96,-0.61) yaw=-48deg cmd=(vx=0.50 wz=-1.02) elapsed=8.8s plan[21pts 2.9m] (-0.90,-0.65)→(0.40,-3.15) cpuFreq=1500MHz cpuT=72C cpu=43% mem=19%
[velocity_pid.py-9] [INFO] [1781687609.324888901] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.31 corrected=0.29 err=37.2%
[lidar_cone_detector.py-19] [INFO] [1781687609.596994396] [lidar_cone_detector]: [lidar_cone] cone→CONE_DETECTED
[velocity_pid.py-9] [INFO] [1781687609.894621486] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.09 dt=0.0334s, resetting
[component_container_isolated-18] [WARN] [1781687610.082414819] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3292 Hz
[component_container_isolated-18] [INFO] [1781687610.229769258] [controller_server]: Passing new path to controller.
[rviz2-21] [INFO] [1781687610.707669177] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[rviz2-21] [INFO] [1781687610.711123054] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[competition_master_stage3.py-20] [INFO] [1781687611.012334186] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.67,-1.14) yaw=-77deg cmd=(vx=0.50 wz=0.34) elapsed=10.8s plan[18pts 2.5m] (-0.70,-0.95)→(0.40,-3.15) cpuFreq=1500MHz cpuT=72C cpu=86% mem=19%
[velocity_pid.py-9] [INFO] [1781687611.191157265] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.04 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1781687611.230164657] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.02
[velocity_pid.py-9] [INFO] [1781687611.295051103] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.02 -> current=-0.11 dt=0.0408s, resetting
[velocity_pid.py-9] [INFO] [1781687611.453569964] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0327s, resetting
[rviz2-21] [ERROR] [1781687611.691579735] [rviz2]: Vertex Program:rviz/glsl120/indexed_8bit_image.vert Fragment Program:rviz/glsl120/indexed_8bit_image.frag GLSL link result :
[rviz2-21] active samplers with a different type refer to the same texture image unit
[component_container_isolated-18] [WARN] [1781687612.082076241] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3291 Hz
[velocity_pid.py-9] [INFO] [1781687612.200200126] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.07 corrected=-0.35 err=76.3%
[component_container_isolated-18] [INFO] [1781687612.229768014] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781687612.321922138] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.32
[velocity_pid.py-9] [INFO] [1781687612.457741573] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0286s, resetting
[competition_master_stage3.py-20] [INFO] [1781687613.013955484] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.41,-1.67) yaw=-62deg cmd=(vx=0.50 wz=-0.37) elapsed=12.8s plan[12pts 1.7m] (-0.40,-1.75)→(0.40,-3.15) cpuFreq=1500MHz cpuT=73C cpu=75% mem=19%
[rviz2-21] [INFO] [1781687613.076746803] [rviz2]: Trying to create a map of size 60 x 60 using 1 swatches
[velocity_pid.py-9] [INFO] [1781687613.223646951] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.23 corrected=0.38 err=53.0%
[velocity_pid.py-9] [INFO] [1781687613.494545320] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.12 -> current=0.01 dt=0.0254s, resetting
[qr_decoder-12] [INFO] [1781687613.841472889] [qr_decoder_zbar]: [qr_decoder] QR DETECTED frame=467 symbols=1 (gap=-1 frames)
[qr_decoder-12] [INFO] [1781687613.841722140] [qr_decoder_zbar]: [QR] 1584 | 3D:(-0.850, +0.126, 1.562)m | px(91,231) D:1562mm
[qr_decoder-12] [INFO] [1781687613.842137806] [qr_decoder_zbar]: [QR] 1584 | robot_pos: (0.75, -2.37, yaw=-1.97)
[qr_decision-13] [INFO] [1781687613.846468308] [qr_decision]: [QR] 1584 CCW @ (x=0.74, y=-2.40, yaw=-1.97) → /qr_event
[qr_decision-13] [INFO] [1781687613.849979727] [qr_decision]: [检查点] qr_decision 发布 /qr_event (由 task_manager 决定停车)
[competition_master_stage3.py-20] [INFO] [1781687613.853994562] [competition_master_stage3]: [QR检测] 内容: 1584
[competition_master_stage3.py-20] [INFO] [1781687613.862508690] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decoder_zbar
[competition_master_stage3.py-20] [INFO] [1781687613.865838484] [competition_master_stage3]: >>> QR 解码已关闭, 等待方向判断 (/qr_event)...
[competition_master_stage3.py-20] [INFO] [1781687613.868867652] [competition_master_stage3]: [QR检测] 取消当前导航目标, 等待BT完成 cancel/halt 清理...
[competition_master_stage3.py-20] [INFO] [1781687613.890059494] [competition_master_stage3]: [QR事件] 方向: 逆时针 (通道巡航阶段使用)
[competition_master_stage3.py-20] [INFO] [1781687613.897000414] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decision
[qr_decoder-12] [INFO] [1781687613.910921003] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-18] [WARN] [1781687614.083232746] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3293 Hz
[component_container_isolated-18] [INFO] [1781687614.130934975] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-18] [INFO] [1781687614.131130350] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1781687614.134094726] [bt_navigator]: [navigate_to_pose] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1781687614.134800477] [bt_navigator]: Goal canceled
[competition_master_stage3.py-20] [INFO] [1781687614.147604316] [competition_master_stage3]: [结果回调] BT取消确认完成 (STATUS_CANCELED), 准备发送通道入口目标...
[competition_master_stage3.py-20] [INFO] [1781687614.153347360] [competition_master_stage3]: [状态机] NAV_TO_QR → BACKING_UP
[competition_master_stage3.py-20] [INFO] [1781687614.165784490] [competition_master_stage3]: >>> BT取消完成, 右后退摆正车头→前进进通道...
[competition_master_stage3.py-20] [INFO] [1781687614.173845577] [competition_master_stage3]: [BACKUP] 右后退中: vx=-0.15 wz=0.80, 持续 6.0s...
[cmd_vel_mux.py-8] [INFO] [1781687614.191623460] [cmd_vel_mux]: [mux→] src=nav vx=-0.15 wz=0.80
[velocity_pid.py-9] [INFO] [1781687614.238168147] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.41 -> current=-0.15 dt=0.0437s, resetting
[velocity_pid.py-9] [INFO] [1781687614.245419484] [velocity_pid]: [vel_pid→] desired=-0.15 actual=0.49 corrected=-0.85 err=426.7%
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
[INFO] [qr_decoder-12]: process has finished cleanly [pid 47948]
[cmd_vel_mux.py-8] [INFO] [1781687614.695518515] [cmd_vel_mux]: [mux→] src=nav vx=-0.15 wz=0.80
[ERROR] [qr_decision-13]: process has died [pid 47950, exit code 1, cmd '/userdata/dev_ws/install/origincar_qr/lib/origincar_qr/qr_decision --ros-args -r __node:=qr_decision --params-file /tmp/launch_params_baeb9glc'].
[competition_master_stage3.py-20] [INFO] [1781687615.012316404] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.20,-2.36) yaw=-77deg cmd=(vx=0.00 wz=0.00) elapsed=14.8s plan[10pts 1.4m] (-0.30,-2.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=73C cpu=62% mem=18%
[velocity_pid.py-9] [INFO] [1781687615.256425303] [velocity_pid]: [vel_pid→] desired=-0.15 actual=0.00 corrected=-0.20 err=100.0%
[imu_madgwick_filter.py-4] [INFO] [1781687616.003310048] [imu_madgwick_filter]: [imu_madgwick ->] msgs=798 q_w=0.8231 angle=69.2deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781687616.174549664] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2071 q_w=0.7373 angle=85.0deg beta=0.0030
[velocity_pid.py-9] [INFO] [1781687616.294367759] [velocity_pid]: [vel_pid→] desired=-0.15 actual=-0.12 corrected=-0.16 err=22.0%
[competition_master_stage3.py-20] [INFO] [1781687617.012948366] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.22,-2.29) yaw=-63deg cmd=(vx=-0.15 wz=0.80) elapsed=16.8s plan[10pts 1.4m] (-0.30,-2.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=73C cpu=38% mem=18%
[rviz2-21] [INFO] [1781687617.223940833] [rviz2]: Message Filter dropping message: frame 'odom' at time 1781687608.113 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[competition_master_stage3.py-20] [INFO] [1781687619.011913784] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.36,-2.11) yaw=-19deg cmd=(vx=-0.15 wz=0.80) elapsed=18.8s plan[10pts 1.4m] (-0.30,-2.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=72C cpu=71% mem=18%
[lidar_cone_detector.py-19] [INFO] [1781687619.862500032] [lidar_cone_detector]: [lidar_cone] no_cone→CLEAR
[competition_master_stage3.py-20] [INFO] [1781687620.174755711] [competition_master_stage3]: [状态机] BACKING_UP → CRUISE_CHANNEL
[competition_master_stage3.py-20] [INFO] [1781687620.177730129] [competition_master_stage3]: [CRUISE] 方向: CCW (逆时针, even QR), 路点: (1.73,-1.98), (2.78,-0.95), (2.10,0.92)
[cmd_vel_mux.py-8] [INFO] [1781687620.187759216] [cmd_vel_mux]: [mux→] src=stop vx=0.00 wz=0.00
[competition_master_stage3.py-20] [INFO] [1781687620.188517425] [competition_master_stage3]: [CRUISE] NavigateThroughPoses: (0.38,-1.10), (1.73,-1.98), (2.78,-0.95), (2.10,0.92)
[component_container_isolated-18] [INFO] [1781687620.192895719] [bt_navigator]: Begin navigating from current location through 4 poses to (2.10, 0.92)
[competition_master_stage3.py-20] [INFO] [1781687620.204422932] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[lidar_cone_detector.py-19] [INFO] [1781687620.461424170] [lidar_cone_detector]: [lidar_cone] cone→CONE_DETECTED
[component_container_isolated-18] [WARN] [1781687620.467849214] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1781687620.468087173] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[competition_master_stage3.py-20] [INFO] [1781687620.473711800] [competition_master_stage3]: [CONE] 锥桶! 禁区代价降至101, 车可借道且感知边界
[component_container_isolated-18] [ERROR] [1781687620.478165135] [local_costmap.local_costmap]: KeepoutFilter: For proper use of keepout filter base and multiplier in CostmapFilterInfo message should be set to their default values (0.000000 and 1.000000)
[component_container_isolated-18] [INFO] [1781687620.478502219] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [ERROR] [1781687620.478223010] [global_costmap.global_costmap]: KeepoutFilter: For proper use of keepout filter base and multiplier in CostmapFilterInfo message should be set to their default values (0.000000 and 1.000000)
[component_container_isolated-18] [INFO] [1781687620.478793261] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781687620.494225809] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781687620.495323851] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[cmd_vel_mux.py-8] [INFO] [1781687620.687786811] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.51s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1781687620.697111481] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[competition_master_stage3.py-20] [INFO] [1781687621.013339162] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.70,-2.13) yaw=33deg cmd=(vx=0.00 wz=0.00) elapsed=20.8s plan[10pts 1.4m] (-0.30,-2.05)→(0.40,-3.15) cpuFreq=1500MHz cpuT=72C cpu=33% mem=18%
[component_container_isolated-18] [WARN] [1781687621.101969409] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.1161 Hz
[component_container_isolated-18] [INFO] [1781687621.301249871] [controller_server]: Received a goal, begin computing control effort.
[cmd_vel_mux.py-8] [INFO] [1781687621.355583603] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=0.12
[velocity_pid.py-9] [INFO] [1781687621.387850451] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.09 err=100.0%
[velocity_pid.py-9] [INFO] [1781687622.388885097] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.39 corrected=0.18 err=21.6%
[competition_master_stage3.py-20] [INFO] [1781687623.013555454] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.52,-1.96) yaw=46deg cmd=(vx=0.50 wz=-0.13) elapsed=22.8s plan[66pts 8.5m] (-0.70,-2.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=72C cpu=43% mem=18%
[component_container_isolated-18] [WARN] [1781687623.105938078] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4079 Hz
[component_container_isolated-18] [INFO] [1781687623.301627996] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687624.403684520] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=-0.07 err=22.7%
[cmd_vel_mux.py-8] [INFO] [1781687624.423959696] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.35
[velocity_pid.py-9] [INFO] [1781687624.586985809] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.10 -> current=0.03 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1781687624.653768463] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0334s, resetting
[competition_master_stage3.py-20] [INFO] [1781687625.013525953] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.12,-1.32) yaw=36deg cmd=(vx=-0.30 wz=0.26) elapsed=24.8s plan[63pts 8.1m] (-0.40,-1.85)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=29% mem=18%
[component_container_isolated-18] [WARN] [1781687625.092433571] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4384 Hz
[component_container_isolated-18] [INFO] [1781687625.301635579] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687625.423554383] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.10 corrected=-0.21 err=53.3%
[cmd_vel_mux.py-8] [INFO] [1781687625.424174091] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.02
[velocity_pid.py-9] [INFO] [1781687625.488778869] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.02 -> current=-0.10 dt=0.0336s, resetting
[velocity_pid.py-9] [INFO] [1781687625.553228523] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0331s, resetting
[lidar_cone_detector.py-19] [INFO] [1781687625.849937152] [lidar_cone_detector]: [lidar_cone] no_cone→CLEAR
[component_container_isolated-18] [WARN] [1781687625.857226072] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1781687625.858748531] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1781687625.859744448] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[competition_master_stage3.py-20] [INFO] [1781687625.865928826] [competition_master_stage3]: [CONE] 锥桶已通过, 恢复禁区
[component_container_isolated-18] [INFO] [1781687625.869945119] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781687625.874627121] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781687625.874920122] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-4] [INFO] [1781687626.004462803] [imu_madgwick_filter]: [imu_madgwick ->] msgs=997 q_w=0.9550 angle=34.5deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781687626.174472711] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2604 q_w=0.9966 angle=9.5deg beta=0.0030
[velocity_pid.py-9] [INFO] [1781687626.454180291] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.31 corrected=0.35 err=37.2%
[lidar_cone_detector.py-19] [INFO] [1781687626.737927332] [lidar_cone_detector]: [lidar_cone] cone→CONE_DETECTED
[component_container_isolated-18] [WARN] [1781687626.740494125] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1781687626.740515458] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [ERROR] [1781687626.747769169] [local_costmap.local_costmap]: KeepoutFilter: For proper use of keepout filter base and multiplier in CostmapFilterInfo message should be set to their default values (0.000000 and 1.000000)
[component_container_isolated-18] [INFO] [1781687626.748035378] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [ERROR] [1781687626.749150253] [global_costmap.global_costmap]: KeepoutFilter: For proper use of keepout filter base and multiplier in CostmapFilterInfo message should be set to their default values (0.000000 and 1.000000)
[component_container_isolated-18] [INFO] [1781687626.749396295] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[competition_master_stage3.py-20] [INFO] [1781687626.749598504] [competition_master_stage3]: [CONE] 锥桶! 禁区代价降至101, 车可借道且感知边界
[component_container_isolated-18] [WARN] [1781687626.758635799] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781687626.760703967] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-20] [INFO] [1781687627.011657618] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.44,-1.16) yaw=10deg cmd=(vx=0.50 wz=-0.10) elapsed=26.8s plan[57pts 7.2m] (0.30,-1.25)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=70% mem=18%
[component_container_isolated-18] [WARN] [1781687627.092996570] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4361 Hz
[lidar_cone_detector.py-19] [INFO] [1781687627.239515009] [lidar_cone_detector]: [lidar_cone] no_cone→CLEAR
[component_container_isolated-18] [WARN] [1781687627.242634802] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[competition_master_stage3.py-20] [INFO] [1781687627.246635471] [competition_master_stage3]: [CONE] 锥桶已通过, 恢复禁区
[component_container_isolated-18] [WARN] [1781687627.244810970] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1781687627.253107098] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781687627.258285101] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781687627.267308396] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781687627.267631688] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1781687627.301634786] [controller_server]: Passing new path to controller.
[lidar_cone_detector.py-19] [INFO] [1781687628.135357359] [lidar_cone_detector]: [lidar_cone] cone→CONE_DETECTED
[component_container_isolated-18] [WARN] [1781687628.138568860] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1781687628.139027735] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [ERROR] [1781687628.143462154] [global_costmap.global_costmap]: KeepoutFilter: For proper use of keepout filter base and multiplier in CostmapFilterInfo message should be set to their default values (0.000000 and 1.000000)
[component_container_isolated-18] [INFO] [1781687628.143789154] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [ERROR] [1781687628.145272238] [local_costmap.local_costmap]: KeepoutFilter: For proper use of keepout filter base and multiplier in CostmapFilterInfo message should be set to their default values (0.000000 and 1.000000)
[component_container_isolated-18] [INFO] [1781687628.145531196] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[competition_master_stage3.py-20] [INFO] [1781687628.157318618] [competition_master_stage3]: [CONE] 锥桶! 禁区代价降至101, 车可借道且感知边界
[component_container_isolated-18] [WARN] [1781687628.155445451] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781687628.155953117] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[velocity_pid.py-9] [INFO] [1781687628.492552139] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.04 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1781687628.524164070] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.32
[component_container_isolated-18] Reallocing temp weights 365 - 60
[velocity_pid.py-9] [INFO] [1781687628.756930088] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0336s, resetting
[competition_master_stage3.py-20] [INFO] [1781687629.014022784] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.19,-1.23) yaw=-35deg cmd=(vx=-0.30 wz=0.62) elapsed=28.8s plan[54pts 6.7m] (0.60,-1.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=62% mem=18%
[component_container_isolated-18] [WARN] [1781687629.091713942] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4386 Hz
[component_container_isolated-18] [INFO] [1781687629.201658740] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781687629.320351834] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.74
[velocity_pid.py-9] [INFO] [1781687629.455964518] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0330s, resetting
[velocity_pid.py-9] [INFO] [1781687629.522257964] [velocity_pid]: [vel_pid→] desired=0.14 actual=-0.07 corrected=0.20 err=152.6%
[velocity_pid.py-9] [INFO] [1781687630.653685332] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.10 -> current=-0.02 dt=0.0326s, resetting
[competition_master_stage3.py-20] [INFO] [1781687631.022482618] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.61,-1.57) yaw=-35deg cmd=(vx=0.50 wz=-0.64) elapsed=30.8s plan[47pts 5.9m] (1.40,-1.45)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=20% mem=19%
[component_container_isolated-18] [WARN] [1781687631.097150775] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2470 Hz
[cmd_vel_mux.py-8] [INFO] [1781687631.222316871] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.73
[velocity_pid.py-9] [INFO] [1781687631.257545553] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.48 corrected=-0.06 err=51.2%
[component_container_isolated-18] [INFO] [1781687631.301622156] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687631.788744493] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.07 -> current=-0.02 dt=0.0347s, resetting
[cmd_vel_mux.py-8] [INFO] [1781687631.823899425] [cmd_vel_mux]: [mux→] src=nav vx=-0.10 wz=-0.23
[velocity_pid.py-9] [INFO] [1781687631.955459316] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.11 -> current=0.02 dt=0.0330s, resetting
[velocity_pid.py-9] [INFO] [1781687632.288613377] [velocity_pid]: [vel_pid→] desired=-0.30 actual=0.02 corrected=-0.39 err=106.3%
[competition_master_stage3.py-20] [INFO] [1781687633.013728151] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.89,-1.88) yaw=-86deg cmd=(vx=-0.30 wz=1.41) elapsed=32.8s plan[45pts 5.6m] (1.60,-1.65)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=67% mem=18%
[component_container_isolated-18] [WARN] [1781687633.085542558] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2663 Hz
[component_container_isolated-18] [INFO] [1781687633.201653733] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687633.290445272] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.27 corrected=-0.04 err=30.5%
[cmd_vel_mux.py-8] [INFO] [1781687633.320034868] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=1.20
[velocity_pid.py-9] [INFO] [1781687633.456346261] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0340s, resetting
[velocity_pid.py-9] [INFO] [1781687634.321245887] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.25 corrected=0.39 err=49.0%
[competition_master_stage3.py-20] [INFO] [1781687635.012409854] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.91,-1.84) yaw=-53deg cmd=(vx=0.50 wz=-0.15) elapsed=34.8s plan[38pts 5.1m] (1.90,-1.95)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=80% mem=19%
[velocity_pid.py-9] [INFO] [1781687635.089053929] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.03 -> current=0.10 dt=0.0333s, resetting
[component_container_isolated-18] [WARN] [1781687635.096965099] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2492 Hz
[component_container_isolated-18] [INFO] [1781687635.301624647] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687635.487157102] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.53 corrected=0.04 err=29.3%
[cmd_vel_mux.py-8] [INFO] [1781687635.519650492] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.72
[velocity_pid.py-9] [INFO] [1781687635.753626260] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0332s, resetting
[velocity_pid.py-9] [INFO] [1781687635.856574555] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.10 -> current=-0.03 dt=0.0342s, resetting
[imu_madgwick_filter.py-4] [INFO] [1781687636.004370869] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1197 q_w=0.9331 angle=42.2deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781687636.175607735] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3120 q_w=0.8291 angle=68.0deg beta=0.0030
[velocity_pid.py-9] [INFO] [1781687636.493572373] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.07 corrected=-0.34 err=76.3%
[lidar_cone_detector.py-19] [INFO] [1781687637.001953136] [lidar_cone_detector]: [lidar_cone] no_cone→CLEAR
[competition_master_stage3.py-20] [INFO] [1781687637.012423390] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.18,-2.39) yaw=-54deg cmd=(vx=-0.30 wz=-0.49) elapsed=36.8s plan[38pts 5.0m] (2.00,-1.95)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=75% mem=19%
[component_container_isolated-18] [WARN] [1781687637.023679312] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1781687637.024477687] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[competition_master_stage3.py-20] [INFO] [1781687637.026951105] [competition_master_stage3]: [CONE] 锥桶已通过, 恢复禁区
[component_container_isolated-18] [INFO] [1781687637.033771941] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781687637.033873816] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781687637.043581529] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781687637.043627279] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781687637.094681468] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2568 Hz
[component_container_isolated-18] [INFO] [1781687637.201625139] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781687637.319241857] [cmd_vel_mux]: [mux→] src=nav vx=-0.18 wz=-0.12
[velocity_pid.py-9] [INFO] [1781687637.392648097] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.12 -> current=0.01 dt=0.0383s, resetting
[velocity_pid.py-9] [INFO] [1781687637.522119487] [velocity_pid]: [vel_pid→] desired=-0.18 actual=-0.28 corrected=-0.11 err=56.1%
[velocity_pid.py-9] [INFO] [1781687637.756692672] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.01 -> current=-0.12 dt=0.0324s, resetting
[cmd_vel_mux.py-8] [INFO] [1781687637.821490158] [cmd_vel_mux]: [mux→] src=nav vx=0.30 wz=-0.37
[velocity_pid.py-9] [INFO] [1781687638.522442921] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.27 corrected=0.17 err=46.4%
[cmd_vel_mux.py-8] [INFO] [1781687638.658163188] [cmd_vel_mux]: [mux→] src=nav vx=0.34 wz=-1.57
[velocity_pid.py-9] [INFO] [1781687638.956810193] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.07 -> current=-0.02 dt=0.0323s, resetting
[competition_master_stage3.py-20] [INFO] [1781687639.012963134] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.10,-2.27) yaw=-79deg cmd=(vx=-0.10 wz=-1.04) elapsed=38.8s plan[38pts 4.9m] (2.10,-2.35)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=60% mem=19%
[component_container_isolated-18] [WARN] [1781687639.086907124] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2671 Hz
[component_container_isolated-18] [INFO] [1781687639.201637549] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781687639.256654031] [cmd_vel_mux]: [mux→] src=nav vx=-0.30 wz=-0.29
[lidar_cone_detector.py-19] [INFO] [1781687639.295942173] [lidar_cone_detector]: [lidar_cone] cone→CONE_DETECTED
[competition_master_stage3.py-20] [INFO] [1781687639.312409056] [competition_master_stage3]: [CONE] 锥桶! 禁区代价降至101, 车可借道且感知边界
[component_container_isolated-18] [WARN] [1781687639.308882054] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1781687639.308901762] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [ERROR] [1781687639.318405350] [global_costmap.global_costmap]: KeepoutFilter: For proper use of keepout filter base and multiplier in CostmapFilterInfo message should be set to their default values (0.000000 and 1.000000)
[component_container_isolated-18] [INFO] [1781687639.318660183] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [ERROR] [1781687639.325618061] [local_costmap.local_costmap]: KeepoutFilter: For proper use of keepout filter base and multiplier in CostmapFilterInfo message should be set to their default values (0.000000 and 1.000000)
[component_container_isolated-18] [INFO] [1781687639.325867478] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781687639.332656856] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781687639.333954982] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[velocity_pid.py-9] [INFO] [1781687639.455269034] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.08 dt=0.0341s, resetting
[velocity_pid.py-9] [INFO] [1781687639.523004064] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.01 corrected=-0.37 err=98.0%
[competition_master_stage3.py-20] [INFO] [1781687641.014667377] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.09,-2.29) yaw=-87deg cmd=(vx=-0.30 wz=1.67) elapsed=40.8s plan[39pts 5.1m] (2.10,-2.35)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=43% mem=19%
[component_container_isolated-18] [WARN] [1781687641.087699242] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2663 Hz
[velocity_pid.py-9] [INFO] [1781687641.089086201] [velocity_pid]: [vel_pid→] desired=-0.21 actual=-0.29 corrected=-0.05 err=36.7%
[cmd_vel_mux.py-8] [INFO] [1781687641.122287757] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=1.42
[component_container_isolated-18] [INFO] [1781687641.201638167] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687641.253180814] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1781687641.887896547] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.01 -> current=-0.12 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781687642.124939192] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.27 corrected=0.37 err=45.2%
[competition_master_stage3.py-20] [INFO] [1781687643.014528744] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.21,-2.27) yaw=-38deg cmd=(vx=0.50 wz=1.52) elapsed=42.8s plan[38pts 4.8m] (2.10,-2.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=71% mem=19%
[component_container_isolated-18] [WARN] [1781687643.089387651] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2590 Hz
[component_container_isolated-18] [INFO] [1781687643.401625495] [controller_server]: Passing new path to controller.
[lidar_cone_detector.py-19] [INFO] [1781687643.780175575] [lidar_cone_detector]: [lidar_cone] no_cone→CLEAR
[component_container_isolated-18] [WARN] [1781687643.784792286] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1781687643.784809494] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[competition_master_stage3.py-20] [INFO] [1781687643.789110996] [competition_master_stage3]: [CONE] 锥桶已通过, 恢复禁区
[component_container_isolated-18] [INFO] [1781687643.790743038] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781687643.798005000] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781687643.808935796] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781687643.808947838] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[velocity_pid.py-9] [INFO] [1781687644.487942257] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.07 err=21.2%
[cmd_vel_mux.py-8] [INFO] [1781687644.519729479] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.71
[lidar_cone_detector.py-19] [INFO] [1781687644.677626631] [lidar_cone_detector]: [lidar_cone] cone→CONE_DETECTED
[component_container_isolated-18] [WARN] [1781687644.685520176] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1781687644.685564051] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [ERROR] [1781687644.694795846] [local_costmap.local_costmap]: KeepoutFilter: For proper use of keepout filter base and multiplier in CostmapFilterInfo message should be set to their default values (0.000000 and 1.000000)
[component_container_isolated-18] [INFO] [1781687644.695049305] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[competition_master_stage3.py-20] [INFO] [1781687644.703123808] [competition_master_stage3]: [CONE] 锥桶! 禁区代价降至101, 车可借道且感知边界
[component_container_isolated-18] [WARN] [1781687644.707569810] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [ERROR] [1781687644.709139561] [global_costmap.global_costmap]: KeepoutFilter: For proper use of keepout filter base and multiplier in CostmapFilterInfo message should be set to their default values (0.000000 and 1.000000)
[component_container_isolated-18] [INFO] [1781687644.709441603] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781687644.723867651] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[velocity_pid.py-9] [INFO] [1781687644.756746540] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0323s, resetting
[velocity_pid.py-9] [INFO] [1781687644.856913583] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.09 -> current=-0.04 dt=0.0361s, resetting
[competition_master_stage3.py-20] [INFO] [1781687645.023653405] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.02,-2.06) yaw=58deg cmd=(vx=-0.30 wz=-0.41) elapsed=44.8s plan[35pts 4.6m] (2.30,-2.35)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=86% mem=19%
[component_container_isolated-18] [WARN] [1781687645.084240682] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4519 Hz
[component_container_isolated-18] [INFO] [1781687645.201646566] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781687645.321692826] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.64
[lidar_cone_detector.py-19] [INFO] [1781687645.371009556] [lidar_cone_detector]: [lidar_cone] no_cone→CLEAR
[component_container_isolated-18] [WARN] [1781687645.375423058] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1781687645.375423183] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[competition_master_stage3.py-20] [INFO] [1781687645.378701392] [competition_master_stage3]: [CONE] 锥桶已通过, 恢复禁区
[component_container_isolated-18] [INFO] [1781687645.378311684] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1781687645.386593521] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781687645.389039522] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781687645.399153109] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[velocity_pid.py-9] [INFO] [1781687645.455734801] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0320s, resetting
[velocity_pid.py-9] [INFO] [1781687645.490736232] [velocity_pid]: [vel_pid→] desired=0.14 actual=-0.05 corrected=0.26 err=138.5%
[imu_madgwick_filter.py-4] [INFO] [1781687646.006427789] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1396 q_w=0.6400 angle=100.4deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781687646.174811862] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3622 q_w=0.8303 angle=67.7deg beta=0.0030
[competition_master_stage3.py-20] [INFO] [1781687647.013161724] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.12,-1.67) yaw=81deg cmd=(vx=0.50 wz=0.57) elapsed=46.8s plan[30pts 3.9m] (3.10,-1.85)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=62% mem=19%
[component_container_isolated-18] [WARN] [1781687647.083834755] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2683 Hz
[component_container_isolated-18] [INFO] [1781687647.201633306] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687647.688127474] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.52 corrected=-0.04 err=26.1%
[cmd_vel_mux.py-8] [INFO] [1781687647.719941363] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.26
[lidar_cone_detector.py-19] [INFO] [1781687647.772790136] [lidar_cone_detector]: [lidar_cone] cone→CONE_DETECTED
[component_container_isolated-18] [WARN] [1781687647.775650179] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1781687647.776160887] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[competition_master_stage3.py-20] [INFO] [1781687647.779097763] [competition_master_stage3]: [CONE] 锥桶! 禁区代价降至101, 车可借道且感知边界
[component_container_isolated-18] [ERROR] [1781687647.787977517] [local_costmap.local_costmap]: KeepoutFilter: For proper use of keepout filter base and multiplier in CostmapFilterInfo message should be set to their default values (0.000000 and 1.000000)
[component_container_isolated-18] [INFO] [1781687647.788261392] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [ERROR] [1781687647.795898021] [global_costmap.global_costmap]: KeepoutFilter: For proper use of keepout filter base and multiplier in CostmapFilterInfo message should be set to their default values (0.000000 and 1.000000)
[component_container_isolated-18] [INFO] [1781687647.796187396] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781687647.807315817] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781687647.808144193] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[velocity_pid.py-9] [INFO] [1781687647.895510689] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.01 -> current=-0.12 dt=0.0335s, resetting
[velocity_pid.py-9] [INFO] [1781687647.958991758] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1781687648.690184157] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.09 corrected=-0.33 err=71.7%
[competition_master_stage3.py-20] [INFO] [1781687649.015316547] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.90,-0.83) yaw=117deg cmd=(vx=-0.30 wz=-0.34) elapsed=48.8s plan[27pts 3.4m] (3.10,-1.45)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=57% mem=19%
[component_container_isolated-18] [WARN] [1781687649.080748367] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2745 Hz
[component_container_isolated-18] [INFO] [1781687649.201635045] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781687649.323761264] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.03
[velocity_pid.py-9] [INFO] [1781687649.392138668] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.03 -> current=0.09 dt=0.0332s, resetting
[component_container_isolated-18] Reallocing temp weights 1500 - 60
[velocity_pid.py-9] [INFO] [1781687649.453891237] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0336s, resetting
[velocity_pid.py-9] [INFO] [1781687649.720917310] [velocity_pid]: [vel_pid→] desired=0.44 actual=-0.16 corrected=0.53 err=136.1%
[competition_master_stage3.py-20] [INFO] [1781687651.013320743] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.86,-0.74) yaw=113deg cmd=(vx=0.50 wz=-0.03) elapsed=50.8s plan[15pts 2.0m] (2.90,-0.85)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=43% mem=19%
[component_container_isolated-18] [WARN] [1781687651.079361105] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2759 Hz
[component_container_isolated-18] [INFO] [1781687651.201638574] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687651.293273781] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.09 dt=0.0335s, resetting
[velocity_pid.py-9] [INFO] [1781687652.390531170] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.08 -> current=-0.04 dt=0.0326s, resetting
[velocity_pid.py-9] [INFO] [1781687652.398082007] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.51 corrected=0.03 err=24.4%
[cmd_vel_mux.py-8] [INFO] [1781687652.420894683] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.14
[velocity_pid.py-9] [INFO] [1781687652.656988119] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0264s, resetting
[competition_master_stage3.py-20] [INFO] [1781687653.012800980] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.36,0.05) yaw=123deg cmd=(vx=-0.30 wz=-0.02) elapsed=52.8s plan[13pts 1.8m] (2.80,-0.65)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=89% mem=19%
[component_container_isolated-18] [WARN] [1781687653.080018968] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2748 Hz
[component_container_isolated-18] [INFO] [1781687653.201676312] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687653.287701182] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.01 -> current=-0.12 dt=0.0333s, resetting
[cmd_vel_mux.py-8] [INFO] [1781687653.331566201] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.24
[velocity_pid.py-9] [INFO] [1781687653.453546212] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1781687653.458577214] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.10 corrected=0.37 err=263.3%
[velocity_pid.py-9] [INFO] [1781687654.491350034] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.35 corrected=0.33 err=30.7%
[cmd_vel_mux.py-8] [INFO] [1781687654.862087819] [cmd_vel_mux]: [mux→] src=nav vx=0.35 wz=-1.54
[competition_master_stage3.py-20] [INFO] [1781687655.022022804] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.24,0.34) yaw=77deg cmd=(vx=0.17 wz=-1.29) elapsed=54.8s plan[10pts 1.2m] (2.30,0.15)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=33% mem=19%
[component_container_isolated-18] [WARN] [1781687655.079336079] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2750 Hz
[velocity_pid.py-9] [INFO] [1781687655.088381208] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.08 -> current=-0.01 dt=0.0317s, resetting
[component_container_isolated-18] [INFO] [1781687655.201638465] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687655.389176796] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.06 -> current=0.03 dt=0.0333s, resetting
[cmd_vel_mux.py-8] [INFO] [1781687655.424051019] [cmd_vel_mux]: [mux→] src=nav vx=0.11 wz=-0.17
[velocity_pid.py-9] [INFO] [1781687655.521387352] [velocity_pid]: [vel_pid→] desired=0.11 actual=0.14 corrected=0.03 err=27.1%
[velocity_pid.py-9] [INFO] [1781687655.555890951] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.08 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1781687655.853797912] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.02 -> current=-0.07 dt=0.0336s, resetting
[velocity_pid.py-9] [INFO] [1781687655.988563970] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.08 -> current=-0.04 dt=0.0333s, resetting
[imu_madgwick_filter.py-4] [INFO] [1781687656.003060893] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1594 q_w=0.8726 angle=58.5deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781687656.174512384] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4133 q_w=0.9797 angle=23.1deg beta=0.0030
[lidar_cone_detector.py-19] [INFO] [1781687656.340285247] [lidar_cone_detector]: [lidar_cone] no_cone→CLEAR
[component_container_isolated-18] [WARN] [1781687656.346732874] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1781687656.346772624] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1781687656.353045544] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[competition_master_stage3.py-20] [INFO] [1781687656.355070878] [competition_master_stage3]: [CONE] 锥桶已通过, 恢复禁区
[component_container_isolated-18] [INFO] [1781687656.363550840] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781687656.370785010] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781687656.375798345] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[cmd_vel_mux.py-8] [INFO] [1781687656.423230949] [cmd_vel_mux]: [mux→] src=nav vx=0.06 wz=-0.55
[velocity_pid.py-9] [INFO] [1781687656.456594672] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0345s, resetting
[velocity_pid.py-9] [INFO] [1781687656.521917325] [velocity_pid]: [vel_pid→] desired=0.12 actual=0.00 corrected=0.10 err=100.0%
[competition_master_stage3.py-20] [INFO] [1781687657.025851708] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.34,0.52) yaw=40deg cmd=(vx=0.12 wz=0.82) elapsed=56.8s plan[6pts 0.6m] (2.30,0.55)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=67% mem=19%
[component_container_isolated-18] [WARN] [1781687657.079295856] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2782 Hz
[component_container_isolated-18] [INFO] [1781687657.201630575] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781687657.319382251] [cmd_vel_mux]: [mux→] src=nav vx=-0.06 wz=0.82
[velocity_pid.py-9] [INFO] [1781687657.357889643] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.03 -> current=-0.06 dt=0.0333s, resetting
[velocity_pid.py-9] [INFO] [1781687657.530299425] [velocity_pid]: [vel_pid→] desired=-0.21 actual=0.06 corrected=-0.23 err=127.3%
[velocity_pid.py-9] [INFO] [1781687658.559019367] [velocity_pid]: [vel_pid→] desired=-0.25 actual=-0.20 corrected=-0.15 err=20.5%
[cmd_vel_mux.py-8] [INFO] [1781687658.823717356] [cmd_vel_mux]: [mux→] src=nav vx=-0.04 wz=0.59
[competition_master_stage3.py-20] [INFO] [1781687659.011386937] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.32,0.45) yaw=53deg cmd=(vx=0.12 wz=0.34) elapsed=58.8s plan[7pts 0.8m] (2.40,0.55)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=62% mem=19%
[component_container_isolated-18] [WARN] [1781687659.079719966] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2746 Hz
[velocity_pid.py-9] [INFO] [1781687659.088530428] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.09 -> current=-0.04 dt=0.0340s, resetting
[component_container_isolated-18] [INFO] [1781687659.201637227] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687659.455395461] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.09 dt=0.0284s, resetting
[velocity_pid.py-9] [INFO] [1781687659.589709185] [velocity_pid]: [vel_pid→] desired=0.29 actual=0.03 corrected=0.22 err=91.0%
[velocity_pid.py-9] [INFO] [1781687660.590083907] [velocity_pid]: [vel_pid→] desired=0.19 actual=0.27 corrected=-0.04 err=48.0%
[competition_master_stage3.py-20] [INFO] [1781687661.013888214] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.34,0.65) yaw=92deg cmd=(vx=0.16 wz=0.60) elapsed=60.8s plan[6pts 0.6m] (2.30,0.45)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=70% mem=19%
[component_container_isolated-18] [WARN] [1781687661.079215283] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2760 Hz
[component_container_isolated-18] [INFO] [1781687661.201659211] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687661.795317757] [velocity_pid]: [vel_pid→] desired=0.13 actual=0.16 corrected=-0.03 err=27.8%
[cmd_vel_mux.py-8] [INFO] [1781687661.854210699] [cmd_vel_mux]: [mux→] src=nav vx=0.11 wz=0.06
[cmd_vel_mux.py-8] [INFO] [1781687662.453858623] [cmd_vel_mux]: [mux→] src=nav vx=0.01 wz=-0.08
[velocity_pid.py-9] [INFO] [1781687662.489346138] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.04 -> current=-0.08 dt=0.0357s, resetting
[velocity_pid.py-9] [INFO] [1781687662.555961500] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.01 -> current=-0.08 dt=0.0324s, resetting
[lidar_cone_detector.py-19] [INFO] [1781687662.714171985] [lidar_cone_detector]: [lidar_cone] cone→CONE_DETECTED
[competition_master_stage3.py-20] [INFO] [1781687662.722130905] [competition_master_stage3]: [CONE] 锥桶! 禁区代价降至101, 车可借道且感知边界
[component_container_isolated-18] [WARN] [1781687662.718992529] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1781687662.719218237] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [ERROR] [1781687662.728140574] [global_costmap.global_costmap]: KeepoutFilter: For proper use of keepout filter base and multiplier in CostmapFilterInfo message should be set to their default values (0.000000 and 1.000000)
[component_container_isolated-18] [INFO] [1781687662.728414866] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [ERROR] [1781687662.735941952] [local_costmap.local_costmap]: KeepoutFilter: For proper use of keepout filter base and multiplier in CostmapFilterInfo message should be set to their default values (0.000000 and 1.000000)
[component_container_isolated-18] [INFO] [1781687662.736184494] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781687662.741559163] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781687662.748063333] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[velocity_pid.py-9] [INFO] [1781687662.824035240] [velocity_pid]: [vel_pid→] desired=-0.10 actual=0.06 corrected=-0.15 err=158.0%
[competition_master_stage3.py-20] [INFO] [1781687663.014269447] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.23,0.93) yaw=119deg cmd=(vx=-0.10 wz=-0.19) elapsed=62.8s plan[4pts 0.5m] (2.30,0.75)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=70% mem=19%
[component_container_isolated-18] [WARN] [1781687663.079293100] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.1577 Hz
[component_container_isolated-18] [INFO] [1781687663.202581111] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781687663.323617830] [cmd_vel_mux]: [mux→] src=nav vx=0.08 wz=-0.20
[velocity_pid.py-9] [INFO] [1781687663.357147969] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.01 -> current=0.08 dt=0.0335s, resetting
[velocity_pid.py-9] [INFO] [1781687663.855659058] [velocity_pid]: [vel_pid→] desired=0.10 actual=0.00 corrected=0.11 err=100.0%
[lidar_cone_detector.py-19] [INFO] [1781687664.602948670] [lidar_cone_detector]: [lidar_cone] no_cone→CLEAR
[component_container_isolated-18] [WARN] [1781687664.607470338] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1781687664.608000922] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1781687664.613290549] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[competition_master_stage3.py-20] [INFO] [1781687664.617165259] [competition_master_stage3]: [CONE] 锥桶已通过, 恢复禁区
[component_container_isolated-18] [INFO] [1781687664.624485054] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781687664.627983514] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1781687664.642537270] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-20] [INFO] [1781687665.013506262] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.23,0.93) yaw=119deg cmd=(vx=0.10 wz=-0.55) elapsed=64.8s plan[3pts 0.3m] (2.20,0.95)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=88% mem=19%
[component_container_isolated-18] [WARN] [1781687665.079679707] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2745 Hz
[cmd_vel_mux.py-8] [INFO] [1781687665.122908142] [cmd_vel_mux]: [mux→] src=nav vx=-0.08 wz=-0.30
[velocity_pid.py-9] [INFO] [1781687665.159434033] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.01 -> current=-0.08 dt=0.0354s, resetting
[velocity_pid.py-9] [INFO] [1781687665.163078576] [velocity_pid]: [vel_pid→] desired=-0.08 actual=0.10 corrected=-0.40 err=222.5%
[component_container_isolated-18] [INFO] [1781687665.201636093] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687665.554373869] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.03 -> current=0.10 dt=0.0333s, resetting
[lidar_cone_detector.py-19] [INFO] [1781687665.902929018] [lidar_cone_detector]: [lidar_cone] cone→CONE_DETECTED
[component_container_isolated-18] [WARN] [1781687665.906342186] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[competition_master_stage3.py-20] [INFO] [1781687665.911297063] [competition_master_stage3]: [CONE] 锥桶! 禁区代价降至101, 车可借道且感知边界
[component_container_isolated-18] [WARN] [1781687665.906354228] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [ERROR] [1781687665.914298231] [global_costmap.global_costmap]: KeepoutFilter: For proper use of keepout filter base and multiplier in CostmapFilterInfo message should be set to their default values (0.000000 and 1.000000)
[component_container_isolated-18] [INFO] [1781687665.914922940] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781687665.923606944] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [ERROR] [1781687665.924521944] [local_costmap.local_costmap]: KeepoutFilter: For proper use of keepout filter base and multiplier in CostmapFilterInfo message should be set to their default values (0.000000 and 1.000000)
[component_container_isolated-18] [INFO] [1781687665.924746528] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781687665.937844575] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-4] [INFO] [1781687666.003127603] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1794 q_w=0.4140 angle=131.1deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781687666.174594510] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4640 q_w=0.6987 angle=91.4deg beta=0.0030
[velocity_pid.py-9] [INFO] [1781687666.188180890] [velocity_pid]: [vel_pid→] desired=-0.10 actual=-0.01 corrected=-0.15 err=94.0%
[competition_master_stage3.py-20] [INFO] [1781687667.015081994] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.14,1.09) yaw=105deg cmd=(vx=-0.01 wz=2.67) elapsed=66.8s plan[3pts 0.2m] (2.20,1.05)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=78% mem=19%
[cmd_vel_mux.py-8] [INFO] [1781687667.021479955] [cmd_vel_mux]: [mux→] src=nav vx=0.08 wz=2.55
[velocity_pid.py-9] [INFO] [1781687667.055574970] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.01 -> current=0.08 dt=0.0313s, resetting
[component_container_isolated-18] [WARN] [1781687667.079275189] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2891 Hz
[velocity_pid.py-9] [INFO] [1781687667.191519987] [velocity_pid]: [vel_pid→] desired=0.10 actual=-0.06 corrected=0.15 err=165.0%
[component_container_isolated-18] [INFO] [1781687667.201627783] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [INFO] [1781687667.602284079] [controller_server]: Reached the goal!
[component_container_isolated-18] [INFO] [1781687668.093935164] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-20] [INFO] [1781687668.102533001] [competition_master_stage3]: [结果回调] 巡航完成, 到达VLM路点, 触发VLM推理...
[competition_master_stage3.py-20] [INFO] [1781687668.108937588] [competition_master_stage3]: [VLM] 发布 sign4return=100, 拍照推理中...
[competition_master_stage3.py-20] [INFO] [1781687668.113065131] [competition_master_stage3]: [状态机] CRUISE_CHANNEL → RETURN_P
[vision_ai_node-14] [INFO] [1781687668.113342006] [vision_ai_node]: Received sign4return: 100
[component_container_isolated-18] [WARN] [1781687668.113999006] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1781687668.113999131] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[competition_master_stage3.py-20] [INFO] [1781687668.119272967] [competition_master_stage3]: [RETURN] 强制恢复禁区 LETHAL (防止锥桶检测残留)
[competition_master_stage3.py-20] [INFO] [1781687668.129110096] [competition_master_stage3]: [RETURN] 清除机器人周围1.5m + 直接返航至 P点 (-1.99,-0.01)
[component_container_isolated-18] [INFO] [1781687668.124279761] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781687668.130911972] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[vision_ai_node-14] [INFO] [1781687668.129707930] [vision_ai_node]: Received trigger signal (sign4return=100), subscribing to image topic...
[component_container_isolated-18] [INFO] [1781687668.134061973] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1781687668.156174024] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[vision_ai_node-14] [INFO] [1781687668.186179496] [vision_ai_node]: Subscribed to /aurora/rgb/image_raw topic
[vision_ai_node-14] [INFO] [1781687668.221598844] [vision_ai_node]: Received compressed image, processing with AI model...
[competition_master_stage3.py-20] [INFO] [1781687668.242976061] [competition_master_stage3]: [DIAG] nav目标距离: 4.27m, robot=(2.14,1.09) → target=(-1.99,-0.01)
[competition_master_stage3.py-20] [INFO] [1781687668.246133396] [competition_master_stage3]: >>> 发送导航目标 [P点返航]: (-1.99, -0.01, yaw=1.83)
[component_container_isolated-18] [INFO] [1781687668.251416232] [bt_navigator]: Begin navigating from current location (2.16, 1.03) to (-1.99, -0.01)
[competition_master_stage3.py-20] [INFO] [1781687668.263558737] [competition_master_stage3]: 导航目标已接受，车辆出发...
[competition_master_stage3.py-20] [INFO] [1781687669.011574057] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.14,1.09) yaw=105deg cmd=(vx=0.00 wz=0.00) elapsed=68.8s plan[3pts 0.2m] (2.20,1.05)→(2.10,0.95) cpuFreq=1500MHz cpuT=73C cpu=33% mem=19%
[component_container_isolated-18] [WARN] [1781687669.107495098] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.1731 Hz
[cmd_vel_mux.py-8] [INFO] [1781687669.119256853] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.52s > 0.5s, marked inactive
[cmd_vel_mux.py-8] [INFO] [1781687669.124447355] [cmd_vel_mux]: [mux] IDLE all sources inactive, publishing zero Twist
[component_container_isolated-18] [INFO] [1781687669.254011577] [controller_server]: Received a goal, begin computing control effort.
[cmd_vel_mux.py-8] [INFO] [1781687669.326828483] [cmd_vel_mux]: [mux→] src=nav vx=0.07 wz=0.12
[velocity_pid.py-9] [INFO] [1781687669.355963746] [velocity_pid]: [vel_pid→] desired=0.07 actual=0.00 corrected=0.22 err=100.0%
[competition_master_stage3.py-20] [INFO] [1781687671.025605084] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.91,1.25) yaw=152deg cmd=(vx=0.50 wz=1.32) elapsed=70.8s plan[46pts 6.5m] (2.20,1.05)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=74C cpu=67% mem=19%
[component_container_isolated-18] [WARN] [1781687671.103090784] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3377 Hz
[component_container_isolated-18] [INFO] [1781687671.258018017] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781687672.254964443] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.18
[velocity_pid.py-9] [INFO] [1781687672.254944318] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.02 err=21.2%
[velocity_pid.py-9] [INFO] [1781687672.493569128] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0372s, resetting
[competition_master_stage3.py-20] [INFO] [1781687673.030335565] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.95,0.78) yaw=-121deg cmd=(vx=-0.30 wz=-0.51) elapsed=72.8s plan[44pts 6.5m] (1.80,1.35)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=67% mem=19%
[component_container_isolated-18] [WARN] [1781687673.104197555] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3328 Hz
[component_container_isolated-18] [INFO] [1781687673.257995496] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687673.287228675] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.09 corrected=-0.34 err=71.7%
[cmd_vel_mux.py-8] [INFO] [1781687673.354592996] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.26
[velocity_pid.py-9] [INFO] [1781687673.488646969] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0338s, resetting
[velocity_pid.py-9] [INFO] [1781687673.553227122] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.01 -> current=0.12 dt=0.0332s, resetting
[velocity_pid.py-9] [INFO] [1781687674.288450561] [velocity_pid]: [vel_pid→] desired=0.47 actual=0.21 corrected=0.40 err=55.2%
[competition_master_stage3.py-20] [INFO] [1781687675.022818666] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.89,0.61) yaw=-102deg cmd=(vx=0.50 wz=0.71) elapsed=74.8s plan[36pts 5.0m] (1.00,0.85)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=43% mem=19%
[component_container_isolated-18] [WARN] [1781687675.103925408] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3343 Hz
[component_container_isolated-18] [INFO] [1781687675.258028224] [controller_server]: Passing new path to controller.
[lidar_cone_detector.py-19] [INFO] [1781687675.767148150] [lidar_cone_detector]: [lidar_cone] no_cone→CLEAR
[imu_madgwick_filter.py-4] [INFO] [1781687676.004386292] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1994 q_w=-0.9135 angle=312.0deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781687676.174866490] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5154 q_w=-0.6607 angle=262.7deg beta=0.0030
[cmd_vel_mux.py-8] [INFO] [1781687676.253993107] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.43
[velocity_pid.py-9] [INFO] [1781687676.288619288] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.49 corrected=-0.03 err=53.1%
[velocity_pid.py-9] [INFO] [1781687676.488425540] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0297s, resetting
[lidar_cone_detector.py-19] [INFO] [1781687676.664845324] [lidar_cone_detector]: [lidar_cone] cone→CONE_DETECTED
[competition_master_stage3.py-20] [INFO] [1781687677.018977558] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.08,-0.38) yaw=-99deg cmd=(vx=-0.30 wz=0.23) elapsed=76.8s plan[37pts 5.0m] (0.90,0.55)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=71% mem=19%
[component_container_isolated-18] [WARN] [1781687677.092425923] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3539 Hz
[component_container_isolated-18] [INFO] [1781687677.258011118] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687677.292034383] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.06 corrected=-0.36 err=80.7%
[cmd_vel_mux.py-8] [INFO] [1781687677.360054953] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=-0.02
[velocity_pid.py-9] [INFO] [1781687677.386769923] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.10 -> current=-0.02 dt=0.0329s, resetting
[velocity_pid.py-9] [INFO] [1781687677.489176050] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0332s, resetting
[velocity_pid.py-9] [INFO] [1781687678.322999405] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.25 corrected=0.36 err=50.4%
[competition_master_stage3.py-20] [INFO] [1781687679.018758576] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.93,-0.50) yaw=-128deg cmd=(vx=0.50 wz=-0.44) elapsed=78.8s plan[28pts 3.6m] (1.00,-0.45)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=50% mem=19%
[component_container_isolated-18] [WARN] [1781687679.091078107] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3739 Hz
[component_container_isolated-18] [INFO] [1781687679.258003761] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781687680.453177770] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=-0.17
[velocity_pid.py-9] [INFO] [1781687680.454375895] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.50 corrected=0.03 err=22.7%
[velocity_pid.py-9] [INFO] [1781687680.690182996] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0364s, resetting
[competition_master_stage3.py-20] [INFO] [1781687681.014994800] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(0.32,-0.90) yaw=-171deg cmd=(vx=-0.30 wz=0.28) elapsed=80.8s plan[26pts 3.2m] (0.90,-0.65)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=74C cpu=62% mem=19%
[component_container_isolated-18] [WARN] [1781687681.098019294] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2040 Hz
[component_container_isolated-18] [INFO] [1781687681.258000279] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781687681.353283069] [cmd_vel_mux]: [mux→] src=nav vx=-0.12 wz=0.05
[velocity_pid.py-9] [INFO] [1781687681.493706837] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.03 -> current=0.06 dt=0.0351s, resetting
[velocity_pid.py-9] [INFO] [1781687681.500650507] [velocity_pid]: [vel_pid→] desired=0.06 actual=-0.10 corrected=0.35 err=263.3%
[velocity_pid.py-9] [INFO] [1781687682.525515901] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.36 corrected=0.32 err=28.2%
[competition_master_stage3.py-20] [INFO] [1781687683.014793359] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.00,-0.89) yaw=158deg cmd=(vx=0.50 wz=-0.07) elapsed=82.8s plan[19pts 2.3m] (0.10,-0.85)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=50% mem=19%
[component_container_isolated-18] [WARN] [1781687683.082551721] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3888 Hz
[component_container_isolated-18] [INFO] [1781687683.258001545] [controller_server]: Passing new path to controller.
[cmd_vel_mux.py-8] [INFO] [1781687684.656364222] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.13
[velocity_pid.py-9] [INFO] [1781687684.693898280] [velocity_pid]: [vel_pid→] desired=0.32 actual=0.49 corrected=-0.05 err=53.1%
[velocity_pid.py-9] [INFO] [1781687684.787464236] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.01 -> current=-0.12 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781687684.892007531] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0334s, resetting
[competition_master_stage3.py-20] [INFO] [1781687685.016040583] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.94,-0.43) yaw=174deg cmd=(vx=-0.19 wz=-0.50) elapsed=84.8s plan[16pts 2.0m] (-0.20,-0.75)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=62% mem=19%
[component_container_isolated-18] [WARN] [1781687685.147767306] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2727 Hz
[component_container_isolated-18] [INFO] [1781687685.257994603] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687685.722935175] [velocity_pid]: [vel_pid→] desired=-0.30 actual=-0.11 corrected=-0.29 err=63.0%
[imu_madgwick_filter.py-4] [INFO] [1781687686.006353087] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2192 q_w=-0.1952 angle=202.5deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781687686.179345910] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5671 q_w=0.2684 angle=148.9deg beta=0.0030
[cmd_vel_mux.py-8] [INFO] [1781687686.628264851] [cmd_vel_mux]: [mux→] src=nav vx=-0.16 wz=-1.54
[velocity_pid.py-9] [INFO] [1781687686.759919156] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.07 -> current=0.02 dt=0.0357s, resetting
[velocity_pid.py-9] [INFO] [1781687686.792799670] [velocity_pid]: [vel_pid→] desired=0.09 actual=-0.27 corrected=0.42 err=394.5%
[competition_master_stage3.py-20] [INFO] [1781687687.015566640] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-0.90,-0.48) yaw=152deg cmd=(vx=0.39 wz=-0.67) elapsed=86.8s plan[9pts 1.2m] (-1.00,-0.45)→(-1.80,-0.03) cpuFreq=1500MHz cpuT=73C cpu=67% mem=19%
[component_container_isolated-18] [WARN] [1781687687.083019168] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3781 Hz
[component_container_isolated-18] [INFO] [1781687687.257967701] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687687.288553881] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=-0.04 -> current=0.08 dt=0.0336s, resetting
[velocity_pid.py-9] [INFO] [1781687687.827918151] [velocity_pid]: [vel_pid→] desired=0.50 actual=0.35 corrected=0.37 err=29.4%
[vision_ai_node-14] [INFO] [1781687688.571038424] [vision_ai_node]: AI Analysis Result: 这张图片呈现了一个简洁的室内场景，核心物体是**一只透明塑料饮料瓶**：瓶身贴有**红色标签**（标签含黑、白色文字，疑似“可口可乐”相关标识），瓶盖为**黄色**，瓶内剩余少量液体，瓶底可见残留。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] ### 场景与环境：
[vision_ai_node-14] 背景是一面**浅米色（或米白色）的瓷砖墙**，瓷砖表面光滑带细微纹理，墙面反射出左侧窗户的光影（窗户透入自然光，使场景更明亮）。
[vision_ai_node-14]
[vision_ai_node-14] 地面铺有**浅绿色的塑料防护膜**（或装修保护膜），左下角露出一块**浅黄色的布料**（或另一块防护材料），整体地面整洁，推测是装修中（或临时布置）的室内空间（如新房、工装场地）。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] ### 色彩与氛围：
[vision_ai_node-14] - 瓶子：透明（瓶身）+ 红（标签）+ 黑/白（文字）+ 黄（瓶盖），色彩鲜明；
[vision_ai_node-14] - 墙面：浅米色，柔和干净；
[vision_ai_node-14] - 地面：浅绿色（防护膜）+ 浅黄色（布料），色调清新；
[vision_ai_node-14]
[vision_ai_node-14] 整体光线柔和，场景简洁静谧，背景的浅色调与瓶子的鲜明色彩形成对比，视觉焦点集中在饮料瓶上，给人一种“临时布置、待使用/装修中”的空间感。
[vision_ai_node-14]
[vision_ai_node-14]
[vision_ai_node-14] （注：场景推测为装修期的室内，地面防护、墙面瓷砖、窗户光影共同支撑这一判断。）
[competition_master_stage3.py-20] [INFO] [1781687688.584713347] [competition_master_stage3]: [VLM] 后台收到推理结果: 这张图片呈现了一个简洁的室内场景，核心物体是**一只透明塑料饮料瓶**：瓶身贴有**红色标签**（标签含黑、白色文字，疑似“可口可乐”相关标识），瓶盖为**黄色**，瓶内剩余少量液体，瓶底可见残留。
[competition_master_stage3.py-20]
[competition_master_stage3.py-20]
[competition_master_stage3.py-20] ### 场景与环境：
[competition_master_stage3.py-20] 背景是...
[vision_ai_node-14] [INFO] [1781687688.585220680] [vision_ai_node]: Unsubscribed from image topic
[competition_master_stage3.py-20] [INFO] [1781687689.029992452] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.13,-0.29) yaw=154deg cmd=(vx=0.50 wz=0.87) elapsed=88.8s plan[12pts 1.4m] (-0.80,-0.55)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=93% mem=19%
[cmd_vel_mux.py-8] [INFO] [1781687689.053928879] [cmd_vel_mux]: [mux→] src=nav vx=0.32 wz=0.62
[velocity_pid.py-9] [INFO] [1781687689.060230840] [velocity_pid]: [vel_pid→] desired=0.41 actual=0.51 corrected=0.05 err=24.4%
[component_container_isolated-18] [WARN] [1781687689.110319736] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3362 Hz
[component_container_isolated-18] [INFO] [1781687689.257996257] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687689.289152978] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.05 -> current=-0.04 dt=0.0334s, resetting
[velocity_pid.py-9] [INFO] [1781687689.354252256] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.12 -> current=-0.01 dt=0.0330s, resetting
[cmd_vel_mux.py-8] [INFO] [1781687689.819504995] [cmd_vel_mux]: [mux→] src=nav vx=0.13 wz=-0.69
[velocity_pid.py-9] [INFO] [1781687689.987529857] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=0.04 -> current=-0.05 dt=0.0332s, resetting
[velocity_pid.py-9] [INFO] [1781687690.096646445] [velocity_pid]: [vel_pid→] desired=-0.19 actual=0.19 corrected=-0.43 err=198.0%
[lidar_cone_detector.py-19] [INFO] [1781687690.211590244] [lidar_cone_detector]: [lidar_cone] no_cone→CLEAR
[competition_master_stage3.py-20] [INFO] [1781687691.016122918] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.64,-0.27) yaw=-175deg cmd=(vx=-0.16 wz=0.22) elapsed=90.8s plan[5pts 0.6m] (-1.30,-0.15)→(-1.90,0.01) cpuFreq=1500MHz cpuT=73C cpu=93% mem=19%
[component_container_isolated-18] [WARN] [1781687691.080220695] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3785 Hz
[velocity_pid.py-9] [INFO] [1781687691.123913463] [velocity_pid]: [vel_pid→] desired=-0.16 actual=-0.11 corrected=-0.15 err=29.5%
[component_container_isolated-18] [INFO] [1781687691.258008728] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687691.386944366] [velocity_pid]: [vel_pid] DIR_SWITCH wz prev_desired=0.10 -> current=-0.02 dt=0.0328s, resetting
[cmd_vel_mux.py-8] [INFO] [1781687691.722346133] [cmd_vel_mux]: [mux→] src=nav vx=-0.05 wz=-0.72
[velocity_pid.py-9] [INFO] [1781687691.789443912] [velocity_pid]: [vel_pid] DIR_SWITCH vx prev_desired=-0.05 -> current=0.04 dt=0.0339s, resetting
[velocity_pid.py-9] [INFO] [1781687692.155113441] [velocity_pid]: [vel_pid→] desired=0.20 actual=-0.05 corrected=0.26 err=122.1%
[competition_master_stage3.py-20] [INFO] [1781687693.021146224] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.65,-0.30) yaw=171deg cmd=(vx=0.21 wz=-0.61) elapsed=92.8s plan[7pts 0.8m] (-1.80,-0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=57% mem=19%
[component_container_isolated-18] [WARN] [1781687693.079629207] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3850 Hz
[component_container_isolated-18] [INFO] [1781687693.258012366] [controller_server]: Passing new path to controller.
[velocity_pid.py-9] [INFO] [1781687693.658170369] [velocity_pid]: [vel_pid→] desired=0.15 actual=0.19 corrected=0.08 err=27.3%
[lidar_cone_detector.py-19] [INFO] [1781687693.796638885] [lidar_cone_detector]: [lidar_cone] cone→CONE_DETECTED
[cmd_vel_mux.py-8] [INFO] [1781687694.235181862] [cmd_vel_mux]: [mux→] src=nav vx=0.10 wz=-0.13
[velocity_pid.py-9] [INFO] [1781687694.694466348] [velocity_pid]: [vel_pid→] desired=0.10 actual=0.12 corrected=0.10 err=24.0%
[component_container_isolated-18] [INFO] [1781687694.958754501] [controller_server]: Reached the goal!
[competition_master_stage3.py-20] [INFO] [1781687695.016737193] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(-1.80,-0.25) yaw=140deg cmd=(vx=0.10 wz=-0.02) elapsed=94.8s plan[3pts 0.4m] (-1.70,-0.25)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=80% mem=19%
[component_container_isolated-18] [WARN] [1781687695.083509846] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3854 Hz
[component_container_isolated-18] [INFO] [1781687695.452883335] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-20] [INFO] [1781687695.464162507] [competition_master_stage3]: [结果回调] 已回到P点, 任务完成!
[competition_master_stage3.py-20] [INFO] [1781687695.468872675] [competition_master_stage3]: [状态机] RETURN_P → DONE
[competition_master_stage3.py-20] [INFO] [1781687695.473005052] [competition_master_stage3]:
[competition_master_stage3.py-20] [INFO] [1781687695.476396762] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-20] [INFO] [1781687695.479562055] [competition_master_stage3]: >>> [Stage 3] 任务结束 <<<
[cmd_vel_mux.py-8] [INFO] [1781687695.493790269] [cmd_vel_mux]: [mux→] src=stop vx=0.00 wz=0.00
[competition_master_stage3.py-20] [INFO] [1781687695.495689603] [competition_master_stage3]:   最终状态: DONE
[competition_master_stage3.py-20] [INFO] [1781687695.501556939] [competition_master_stage3]:   总耗时:   95.3s
[competition_master_stage3.py-20] [INFO] [1781687695.505142691] [competition_master_stage3]:   --- 各阶段耗时 ---
[competition_master_stage3.py-20] [INFO] [1781687695.508189317] [competition_master_stage3]:   LAUNCH................ 15.2s
[competition_master_stage3.py-20] [INFO] [1781687695.511360943] [competition_master_stage3]:   NAV_TO_QR............. 14.0s
[competition_master_stage3.py-20] [INFO] [1781687695.516860820] [competition_master_stage3]:   BACKING_UP............ 6.0s
[competition_master_stage3.py-20] [INFO] [1781687695.520647655] [competition_master_stage3]:   CRUISE_CHANNEL........ 47.9s
[competition_master_stage3.py-20] [INFO] [1781687695.524160407] [competition_master_stage3]:   RETURN_P.............. 27.4s
[competition_master_stage3.py-20] [INFO] [1781687695.527532075] [competition_master_stage3]:   (transition/overhead). -15.2s
[competition_master_stage3.py-20] [INFO] [1781687695.530545951] [competition_master_stage3]:   --- ---
[competition_master_stage3.py-20] [INFO] [1781687695.532911952] [competition_master_stage3]:   QR 原始数据: 1584
[competition_master_stage3.py-20] [INFO] [1781687695.535232203] [competition_master_stage3]:   QR 方向:   逆时针 (CW=顺时针/odd, CCW=逆时针/even)
[competition_master_stage3.py-20] [INFO] [1781687695.538170204] [competition_master_stage3]:   VLM 结果:  这张图片呈现了一个简洁的室内场景，核心物体是**一只透明塑料饮料瓶**：瓶身贴有**红色标签**（标签含黑、白色文字，疑似“可口可乐”相关标识），瓶盖为**黄色**，瓶内剩余少量液体，瓶底可见残留。
[competition_master_stage3.py-20]
[competition_master_stage3.py-20]
[competition_master_stage3.py-20] ### 场景与环境：
[competition_master_stage3.py-20] 背景是一面**浅米色（或米白色）的瓷砖墙**，瓷砖表面光滑带细微纹理，墙面反射出左侧窗户的光影（窗户透入自然光，使场景更明亮）。
[competition_master_stage3.py-20]
[competition_master_stage3.py-20] 地面铺有**浅绿色的塑料防护膜
[competition_master_stage3.py-20] [INFO] [1781687695.541523373] [competition_master_stage3]:   超时限制:  180.0s (全局)
[competition_master_stage3.py-20] [INFO] [1781687695.544703166] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-20] [INFO] [1781687695.549800418] [competition_master_stage3]: [TRAJ] 轨迹已保存: /userdata/dev_ws/trajectory.csv (117 点)
[imu_madgwick_filter.py-4] [INFO] [1781687696.004359693] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2392 q_w=0.1627 angle=161.3deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1781687696.174432015] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=6178 q_w=0.5681 angle=110.8deg beta=0.0030
[cmd_vel_mux.py-8] [INFO] [1781687696.452783549] [cmd_vel_mux]: [mux] TIMEOUT src=nav age=0.50s > 0.5s, marked inactive
[competition_master_stage3.py-20] [INFO] [1781687697.012596619] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.90,-0.15) yaw=128deg cmd=(vx=0.00 wz=0.00) elapsed=96.8s plan[2pts 0.1m] (-1.90,-0.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=43% mem=19%
[component_container_isolated-18] [INFO] [1781687697.879342109] [local_costmap.local_costmap]: Message Filter dropping message: frame 'laser_link' at time 1781687697.578 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[competition_master_stage3.py-20] [INFO] [1781687699.012984004] [competition_master_stage3]: [DIAG] state=DONE pos=(-1.90,-0.15) yaw=128deg cmd=(vx=0.00 wz=0.00) elapsed=98.8s plan[2pts 0.1m] (-1.90,-0.15)→(-2.00,-0.05) cpuFreq=1500MHz cpuT=73C cpu=57% mem=19%
^C[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[component_container_isolated-18] [INFO] [1781687700.748975444] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-18] [INFO] [1781687700.749197486] [lifecycle_manager_navigation]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_navigation)
[component_container_isolated-18] [INFO] [1781687700.749498444] [lifecycle_manager_navigation]: Terminating bond timer...
[ERROR] [origincar_base_node-1]: process has died [pid 47888, exit code -6, cmd '/userdata/dev_ws/install/origincar_base/lib/origincar_base/origincar_base_node --ros-args --params-file /tmp/launch_params_lac1cshf --params-file /tmp/launch_params_zajj2esa'].
[ERROR] [lslidar_driver_node-2]: process has died [pid 47890, exit code -6, cmd '/userdata/dev_ws/install/lslidar_driver/lib/lslidar_driver/lslidar_driver_node --ros-args -r __node:=lslidar_driver_node --params-file /userdata/dev_ws/install/lslidar_driver/share/lslidar_driver/params/lsx10.yaml'].
[ERROR] [rviz2-21]: process has died [pid 48260, exit code -11, cmd '/opt/ros/humble/lib/rviz2/rviz2 -d /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/rviz/nav.rviz --ros-args -r __node:=rviz2'].
[INFO] [robot_state_publisher-3]: process has finished cleanly [pid 47892]
[INFO] [imu_madgwick_filter.py-6]: process has finished cleanly [pid 47898]
[INFO] [competition_master_stage3.py-20]: process has finished cleanly [pid 48251]
[INFO] [costmap_filter_info_server-16]: process has finished cleanly [pid 48070]
[INFO] [static_transform_publisher-10]: process has finished cleanly [pid 47944]
[INFO] [cmd_vel_mux.py-8]: process has finished cleanly [pid 47906]
[INFO] [ekf_node-7]: process has finished cleanly [pid 47900]
[ERROR] [lidar_cone_detector.py-19]: process has died [pid 48247, exit code -2, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/lidar_cone_detector.py --ros-args -r __node:=lidar_cone_detector'].
[INFO] [imu_madgwick_filter.py-4]: process has finished cleanly [pid 47894]
[INFO] [map_server-15]: process has finished cleanly [pid 48067]
[INFO] [velocity_pid.py-9]: process has finished cleanly [pid 47916]
[INFO] [lifecycle_manager-17]: process has finished cleanly [pid 48074]
[lifecycle_manager-17] [INFO] [1781687700.749187819] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-17] [INFO] [1781687700.749432069] [lifecycle_manager_keepout]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_keepout)
[lifecycle_manager-17] [INFO] [1781687700.749572903] [lifecycle_manager_keepout]: Terminating bond timer...
[ERROR] [bmi088_iio_bridge.py-5]: process has died [pid 47896, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/bmi088_iio_bridge.py --ros-args -r __node:=bmi088_iio_bridge --params-file /tmp/launch_params_zq7apz6r'].
[map_server-15] [INFO] [1781687700.749301194] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-15] [INFO] [1781687700.749519361] [keepout_mask_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_mask_server)
[map_server-15] [INFO] [1781687700.749768069] [keepout_mask_server]: Deactivating
[map_server-15] [INFO] [1781687700.749855028] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[origincar_base_node-1] [INFO] [1781687700.749376861] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1781687700.749702819] [origincar_base]: Stop command sent to STM32 on shutdown.
[origincar_base_node-1] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[lidar_cone_detector.py-19] Traceback (most recent call last):
[lidar_cone_detector.py-19]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/lidar_cone_detector.py", line 192, in <module>
[static_transform_publisher-10] [INFO] [1781687700.749806445] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[rviz2-21] [INFO] [1781687700.750542695] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[robot_state_publisher-3] [INFO] [1781687700.750633320] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[aurora930_node-11] [INFO] [1781687700.750664612] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-16] [INFO] [1781687700.752255821] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-16] [INFO] [1781687700.752575987] [keepout_filter_info_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_filter_info_server)
[costmap_filter_info_server-16] [INFO] [1781687700.752865279] [keepout_filter_info_server]: Deactivating
[costmap_filter_info_server-16] [INFO] [1781687700.752962779] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[ekf_node-7] [INFO] [1781687700.757983865] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-16] [INFO] [1781687700.764647784] [keepout_filter_info_server]: Cleaning up
[costmap_filter_info_server-16] [INFO] [1781687700.764875409] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-16] [INFO] [1781687701.003559885] [keepout_filter_info_server]: Destroying
[map_server-15] [INFO] [1781687700.770728328] [keepout_mask_server]: Cleaning up
[map_server-15] [INFO] [1781687700.770961078] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[map_server-15] [INFO] [1781687700.913567764] [keepout_mask_server]: Destroying
[aurora930_node-11] I0617 17:15:00.774606 47946 ros2_node.cc:90] process quit succeed
[aurora930_node-11] I0617 17:15:00.774784 47946 aurora900_ros2_device.cc:83] begin stop()
[aurora930_node-11] I0617 17:15:00.812279 47946 aurora900_ros2_device.cc:103] stop stream
[aurora930_node-11] 2026-06-17 17:15:00.825 ( 126.019s) [        B5494020]      aurora900_impl.cc:648   INFO| ir_stream_count_=0, rgb_stream_count_=0, depth_stream_count_=0
[aurora930_node-11] 2026-06-17 17:15:00.825 ( 126.019s) [        B5494020]      aurora900_impl.cc:649   INFO| mask=7
[aurora930_node-11] I0617 17:15:01.130095 47946 aurora900_ros2_device.cc:105] destroy stream
[aurora930_node-11] I0617 17:15:01.130318 47946 aurora900_ros2_device.cc:110] close glog
[aurora930_node-11] WARNING: Logging before InitGoogleLogging() is written to STDERR
[aurora930_node-11] I0617 17:15:01.130436 47946 ros2_device.cc:113] close device...
[aurora930_node-11] 2026-06-17 17:15:01.630 ( 126.823s) [        819E37E0]         cmd_backend.cc:40    INFO| RunBlocking is end!!!
[aurora930_node-11] 2026-06-17 17:15:01.831 ( 127.024s) [        B5494020]deptrum_camera_vendor.c:121   INFO| device is close.
[aurora930_node-11] I0617 17:15:01.834185 47946 ros2_device.cc:116] quit succeed
[lidar_cone_detector.py-19]     main()
[lidar_cone_detector.py-19]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/lidar_cone_detector.py", line 187, in main
[lidar_cone_detector.py-19]     rclpy.spin(LidarConeDetector())
[lidar_cone_detector.py-19]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 229, in spin
[lidar_cone_detector.py-19]     executor.spin_once()
[lidar_cone_detector.py-19]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 808, in spin_once
[lidar_cone_detector.py-19]     self._spin_once_impl(timeout_sec)
[lidar_cone_detector.py-19]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 797, in _spin_once_impl
[lidar_cone_detector.py-19]     handler, entity, node = self.wait_for_ready_callbacks(timeout_sec=timeout_sec)
[lidar_cone_detector.py-19]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 780, in wait_for_ready_callbacks
[lidar_cone_detector.py-19]     return next(self._cb_iter)
[lidar_cone_detector.py-19]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 677, in _wait_for_ready_callbacks
[lidar_cone_detector.py-19]     wait_set.wait(timeout_nsec)
[lidar_cone_detector.py-19] KeyboardInterrupt
[origincar_base_node-1] terminate called after throwing an instance of 'rclcpp::exceptions::RCLError'
[origincar_base_node-1]   what():  failed to create guard condition: the given context is not valid, either rcl_init() was not called or rcl_shutdown() was called., at ./src/rcl/guard_condition.c:67
[component_container_isolated-18] [INFO] [1781687700.972070496] [local_costmap.local_costmap]: Message Filter dropping message: frame 'laser_link' at time 1781687700.670 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-18] [INFO] [1781687701.343072694] [behavior_server]: Running Nav2 LifecycleNode rcl preshutdown (behavior_server)
[component_container_isolated-18] [INFO] [1781687701.343482528] [behavior_server]: Deactivating
[component_container_isolated-18] [INFO] [1781687701.343622653] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687701.354123782] [behavior_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781687701.386366879] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687701.386558463] [lifecycle_manager_localization]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_localization)
[component_container_isolated-18] [INFO] [1781687701.386638671] [lifecycle_manager_localization]: Terminating bond timer...
[component_container_isolated-18] [INFO] [1781687701.452356782] [planner_server]: Running Nav2 LifecycleNode rcl preshutdown (planner_server)
[component_container_isolated-18] [INFO] [1781687701.452834407] [planner_server]: Deactivating
[component_container_isolated-18] [INFO] [1781687701.453559824] [global_costmap.global_costmap]: Deactivating
[component_container_isolated-18] [INFO] [1781687701.671237541] [amcl]: Message Filter dropping message: frame 'laser_link' at time 1781687700.670 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-18] [INFO] [1781687702.072453543] [planner_server]: Deactivating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781687702.072833252] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687702.083360923] [planner_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781687702.129333234] [global_costmap.global_costmap]: Cleaning up
[component_container_isolated-18] [INFO] [1781687702.141994073] [planner_server]: Cleaning up plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781687702.143165823] [planner_server]: Destroying plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1781687702.176499337] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687702.176668129] [amcl]: Running Nav2 LifecycleNode rcl preshutdown (amcl)
[component_container_isolated-18] [INFO] [1781687702.176791337] [amcl]: Deactivating
[component_container_isolated-18] [INFO] [1781687702.176947921] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687702.187406383] [amcl]: Cleaning up
[component_container_isolated-18] [INFO] [1781687702.216419854] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687702.216577979] [smoother_server]: Running Nav2 LifecycleNode rcl preshutdown (smoother_server)
[component_container_isolated-18] [INFO] [1781687702.216710021] [smoother_server]: Deactivating
[component_container_isolated-18] [INFO] [1781687702.216770437] [smoother_server]: Deactivating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781687702.217219354] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687702.227797484] [smoother_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781687702.228010859] [smoother_server]: Cleaning up smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1781687702.263296540] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687702.263594540] [velocity_smoother]: Running Nav2 LifecycleNode rcl preshutdown (velocity_smoother)
[component_container_isolated-18] [INFO] [1781687702.263746290] [velocity_smoother]: Deactivating
[component_container_isolated-18] [INFO] [1781687702.264153332] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687702.274552628] [velocity_smoother]: Cleaning up
[component_container_isolated-18] [INFO] [1781687702.274773045] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687702.274844212] [map_server]: Running Nav2 LifecycleNode rcl preshutdown (map_server)
[component_container_isolated-18] [INFO] [1781687702.274958170] [map_server]: Deactivating
[component_container_isolated-18] [INFO] [1781687702.275119045] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687702.285492175] [map_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781687702.285701675] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687702.285770841] [bt_navigator]: Running Nav2 LifecycleNode rcl preshutdown (bt_navigator)
[component_container_isolated-18] [INFO] [1781687702.285883258] [bt_navigator]: Deactivating
[component_container_isolated-18] [INFO] [1781687702.286042008] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687702.296496096] [bt_navigator]: Cleaning up
[component_container_isolated-18] [INFO] [1781687702.539399406] [bt_navigator]: Completed Cleaning up
[component_container_isolated-18] [INFO] [1781687702.539614615] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687702.539680698] [waypoint_follower]: Running Nav2 LifecycleNode rcl preshutdown (waypoint_follower)
[component_container_isolated-18] [INFO] [1781687702.539788115] [waypoint_follower]: Deactivating
[component_container_isolated-18] [INFO] [1781687702.539932157] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687702.550289494] [waypoint_follower]: Cleaning up
[component_container_isolated-18] [INFO] [1781687702.559614248] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1781687702.559755665] [controller_server]: Running Nav2 LifecycleNode rcl preshutdown (controller_server)
[component_container_isolated-18] [INFO] [1781687702.559869248] [controller_server]: Deactivating
[component_container_isolated-18] [INFO] [1781687702.559928790] [controller_server]: Deactivating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781687702.560124249] [local_costmap.local_costmap]: Deactivating
[component_container_isolated-18] [INFO] [1781687702.711393521] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[lifecycle_manager-17] [INFO] [1781687701.011411221] [lifecycle_manager_keepout]: Destroying lifecycle_manager_keepout
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
[component_container_isolated-18] [INFO] [1781687702.721829692] [controller_server]: Cleaning up
[component_container_isolated-18] [INFO] [1781687702.721969733] [controller_server]: Cleaning up controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1781687702.722236400] [local_costmap.local_costmap]: Cleaning up
[INFO] [aurora930_node-11]: process has finished cleanly [pid 47946]
[ERROR] [vision_ai_node-14]: process has died [pid 47957, exit code 1, cmd '/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node --ros-args -r __node:=vision_ai_node'].
[component_container_isolated-18] [INFO] [1781687703.763020171] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[ERROR] [component_container_isolated-18]: process[component_container_isolated-18] failed to terminate '5' seconds after receiving 'SIGINT', escalating to 'SIGTERM'
[INFO] [component_container_isolated-18]: sending signal 'SIGTERM' to process[component_container_isolated-18]
[component_container_isolated-18] [INFO] [1781687707.730938256] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [component_container_isolated-18]: process[component_container_isolated-18] failed to terminate '10.0' seconds after receiving 'SIGTERM', escalating to 'SIGKILL'
[INFO] [component_container_isolated-18]: sending signal 'SIGKILL' to process[component_container_isolated-18]
[ERROR] [component_container_isolated-18]: process has died [pid 48245, exit code -9, cmd '/opt/ros/humble/lib/rclcpp_components/component_container_isolated --ros-args --log-level info --ros-args -r __node:=nav2_container --params-file /tmp/launch_params_y_nujina --params-file /tmp/launch_params_dj6ayym3 -r /tf:=tf -r /tf_static:=tf_static'].
root@ubuntu:/userdata/dev_ws#
