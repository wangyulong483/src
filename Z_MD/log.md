root@ubuntu:/userdata/dev_ws# ros2 launch origincar_bringup stage2_bringup.launch.py
[INFO] [launch]: All log files can be found below /root/.ros/log/2026-07-11-18-13-43-986340-ubuntu-11734
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [origincar_base_node-1]: process started with pid [11755]
[INFO] [lslidar_driver_node-2]: process started with pid [11757]
[INFO] [robot_state_publisher-3]: process started with pid [11759]
[INFO] [imu_madgwick_filter.py-4]: process started with pid [11761]
[INFO] [bmi088_iio_bridge.py-5]: process started with pid [11763]
[INFO] [imu_madgwick_filter.py-6]: process started with pid [11765]
[INFO] [ekf_node-7]: process started with pid [11767]
[INFO] [static_transform_publisher-8]: process started with pid [11807]
[INFO] [aurora930_node-9]: process started with pid [11809]
[INFO] [qr_decoder-10]: process started with pid [11811]
[INFO] [qr_decision.py-11]: process started with pid [11813]
[INFO] [vision_ai_node-12]: process started with pid [11815]
[origincar_base_node-1] [INFO] [1783764824.675539816] [origincar_base]: origincar_base serial port opened
[lslidar_driver_node-2] [INFO] [1783764824.674265939] [lslidar_driver_node]: Lidar is N10
[lslidar_driver_node-2] [INFO] [1783764824.685675913] [lslidar_driver_node]: Initialised lslidar without error
[lslidar_driver_node-2] [INFO] [1783764824.685914997] [lslidar_driver_node]: Successfully initialize driver...
[robot_state_publisher-3] [WARN] [1783764824.658417875] [robot_state_publisher]: No robot_description parameter, but command-line argument available.  Assuming argument is name of URDF file.  This backwards compatibility fallback will be removed in the future.
[robot_state_publisher-3] [INFO] [1783764824.673925564] [robot_state_publisher]: got segment base_footprint
[robot_state_publisher-3] [INFO] [1783764824.674606856] [robot_state_publisher]: got segment base_link
[robot_state_publisher-3] [INFO] [1783764824.674678940] [robot_state_publisher]: got segment gyro_link
[robot_state_publisher-3] [INFO] [1783764824.674724482] [robot_state_publisher]: got segment laser_link
[ekf_node-7] Both imu1_differential and imu1_relative were set to true. Using differential mode.
[static_transform_publisher-8] [INFO] [1783764824.890893491] [depth_camera_tf]: Spinning until stopped - publishing transform
[static_transform_publisher-8] translation: ('0.140000', '0.000000', '0.050000')
[static_transform_publisher-8] rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
[static_transform_publisher-8] from 'base_link' to 'depth_camera_link'
[aurora930_node-9] W0711 18:13:45.348527 11809 ros2_node.cc:35] hello aurora 900/930
[qr_decoder-10] [INFO] [1783764825.436866212] [qr_decoder_zbar]: QR decoder (ZBar) started: rgb=/aurora/rgb/image_raw, depth=/aurora/depth/image_raw, filter=on, range=[50, 4000]mm, min_qr_len=1, intrinsics: fx=421.3 fy=422.3 cx=320.3 cy=197.0
[aurora930_node-9] 2026-07-11 18:13:45.554 (   0.356s) [        83974020] device_manager_impl.cc:89    INFO| hotplug has registed by user
[aurora930_node-9] device_count==========1
[aurora930_node-9] I0711 18:13:45.586444 11809 aurora900_ros2_device.cc:153] BOOT_ORDER_1::Found 1 deptrum device
[aurora930_node-9] I0711 18:13:45.588678 11809 aurora900_ros2_device.cc:162] BOOT_ORDER_1::No serial number provided: picking first device
[aurora930_node-9] 2026-07-11 18:13:45.589 (   0.392s) [        83974020] device_manager_impl.cc:318   INFO| Device information:
[aurora930_node-9]      ir_pid:0x1930, rgb_pid:0x0
[aurora930_node-9]      serial number:HY400529001015314G00248
[aurora930_node-9] I0711 18:13:45.589303 11809 aurora900_ros2_device.cc:206] BOOT_ORDER_1::0:device start opening
[aurora930_node-9] 2026-07-11 18:13:45.594 (   0.397s) [        83974020]   custom_usb_device.cc:101   INFO| bulk in endpoint addr:129
[aurora930_node-9] 2026-07-11 18:13:45.594 (   0.397s) [        83974020]   custom_usb_device.cc:98    INFO| bulk out endpoint addr:2
[aurora930_node-9] 2026-07-11 18:13:45.603 (   0.406s) [        83974020]deptrum_camera_aurora93:53    INFO| doe_broken:0 ito_support:1 crash_count:0 wdt_count:0 hard_reset_count:2 heart_boot_count:0 boot_total:139 last_crash_time:N
[aurora930_node-9] I0711 18:13:45.603497 11809 aurora900_ros2_device.cc:247] device supported frame_mode:
[aurora930_node-9] I0711 18:13:45.603617 11809 aurora900_ros2_device.cc:252] [0]:ir_mode:=13 kRes320x200Ir8Bit rgb_mode:=31 kRes320x200RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0711 18:13:45.603667 11809 aurora900_ros2_device.cc:252] [1]:ir_mode:=17 kRes480x300Depth16Bit rgb_mode:=32 kRes480x300RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0711 18:13:45.603703 11809 aurora900_ros2_device.cc:252] [2]:ir_mode:=20 kRes640x400Ir8Bit rgb_mode:=33 kRes640x400RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0711 18:13:45.603735 11809 aurora900_ros2_device.cc:266] current set mode ir_mode:20:kRes640x400Ir8Bit,rgb_mode:33:kRes640x400RgbYuv
[INFO] [map_server-13]: process started with pid [11894]
[INFO] [costmap_filter_info_server-14]: process started with pid [11896]
[INFO] [lifecycle_manager-15]: process started with pid [11898]
[costmap_filter_info_server-14] [INFO] [1783764825.928029398] [costmap_filter_info_server]: This is costmap filter info publisher
[costmap_filter_info_server-14] [INFO] [1783764825.987019731] [keepout_filter_info_server]:
[costmap_filter_info_server-14]         keepout_filter_info_server lifecycle node launched.
[costmap_filter_info_server-14]         Waiting on external lifecycle transitions to activate
[costmap_filter_info_server-14]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[lifecycle_manager-15] [INFO] [1783764826.006932008] [lifecycle_manager_keepout]: Creating
[lifecycle_manager-15] [INFO] [1783764826.081840947] [lifecycle_manager_keepout]: Creating and initializing lifecycle service clients
[aurora930_node-9] I0711 18:13:46.169313 11809 aurora900_ros2_device.cc:387] Switch Auto Exposure
[map_server-13] [INFO] [1783764826.209437875] [keepout_mask_server]:
[map_server-13]         keepout_mask_server lifecycle node launched.
[map_server-13]         Waiting on external lifecycle transitions to activate
[map_server-13]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[lifecycle_manager-15] [INFO] [1783764826.213191422] [lifecycle_manager_keepout]: Starting managed nodes bringup...
[lifecycle_manager-15] [INFO] [1783764826.213429214] [lifecycle_manager_keepout]: Configuring keepout_mask_server
[map_server-13] [INFO] [1783764826.224408813] [keepout_mask_server]: Creating
[aurora930_node-9] 2026-07-11 18:13:46.231 (   1.034s) [        83974020]      aurora900_impl.cc:1106  INFO| SetHeartbeat user set heartbeat enable: 0
[map_server-13] [INFO] [1783764826.241021461] [keepout_mask_server]: Configuring
[map_server-13] [INFO] [1783764826.241463337] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.yaml
[map_server-13] [INFO] [1783764826.242838380] [map_io]: resolution: 0.05
[map_server-13] [INFO] [1783764826.242926339] [map_io]: origin[0]: -2.65
[map_server-13] [INFO] [1783764826.242957714] [map_io]: origin[1]: -4.5
[map_server-13] [INFO] [1783764826.242984714] [map_io]: origin[2]: 0
[map_server-13] [INFO] [1783764826.243013464] [map_io]: free_thresh: 0.01
[map_server-13] [INFO] [1783764826.243042547] [map_io]: occupied_thresh: 0.99
[map_server-13] [INFO] [1783764826.243080839] [map_io]: mode: scale
[map_server-13] [INFO] [1783764826.243112256] [map_io]: negate: 0
[map_server-13] [INFO] [1783764826.247857221] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm
[map_server-13] [INFO] [1783764826.281701560] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm: 163 X 141 map @ 0.05 m/cell
[lifecycle_manager-15] [INFO] [1783764826.325853955] [lifecycle_manager_keepout]: Configuring keepout_filter_info_server
[costmap_filter_info_server-14] [INFO] [1783764826.327065165] [keepout_filter_info_server]: Configuring
[lifecycle_manager-15] [INFO] [1783764826.353541119] [lifecycle_manager_keepout]: Activating keepout_mask_server
[map_server-13] [INFO] [1783764826.356188414] [keepout_mask_server]: Activating
[map_server-13] [INFO] [1783764826.356679040] [keepout_mask_server]: Creating bond (keepout_mask_server) to lifecycle manager.
[lifecycle_manager-15] [INFO] [1783764826.474459247] [lifecycle_manager_keepout]: Server keepout_mask_server connected with bond.
[lifecycle_manager-15] [INFO] [1783764826.474658288] [lifecycle_manager_keepout]: Activating keepout_filter_info_server
[costmap_filter_info_server-14] [INFO] [1783764826.478089168] [keepout_filter_info_server]: Activating
[costmap_filter_info_server-14] [INFO] [1783764826.478338835] [keepout_filter_info_server]: Creating bond (keepout_filter_info_server) to lifecycle manager.
[bmi088_iio_bridge.py-5] [INFO] [1783764826.510978006] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1783764826.514191677] [bmi088_iio_bridge]:   DIAGNOSTIC: Scanning IIO devices under /sys/bus/iio/devices/
[bmi088_iio_bridge.py-5] [INFO] [1783764826.517383057] [bmi088_iio_bridge]:   Equivalent to: ls /sys/bus/iio/devices/*/name
[bmi088_iio_bridge.py-5] [INFO] [1783764826.520804478] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1783764826.523448399] [bmi088_iio_bridge]:   iio:device0/name = "34190000.adc"
[bmi088_iio_bridge.py-5] [INFO] [1783764826.526011902] [bmi088_iio_bridge]:   iio:device1/name = "bmi08x"
[bmi088_iio_bridge.py-5] [INFO] [1783764826.528505697] [bmi088_iio_bridge]:   trigger0/name = "34190000.adc-dev0"
[bmi088_iio_bridge.py-5] [INFO] [1783764826.531016867] [bmi088_iio_bridge]:   Total IIO devices found: 3
[bmi088_iio_bridge.py-5] [INFO] [1783764826.533571163] [bmi088_iio_bridge]:   BMI088 kernel module APPEARS LOADED: 1 BMI device(s) detected
[bmi088_iio_bridge.py-5] [INFO] [1783764826.536049999] [bmi088_iio_bridge]:   BMI device names: ['bmi08x']
[bmi088_iio_bridge.py-5] [INFO] [1783764826.539489296] [bmi088_iio_bridge]:   gyro:  /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_anglvel is_si=False scale_override=0.00053
[bmi088_iio_bridge.py-5] [INFO] [1783764826.542807509] [bmi088_iio_bridge]:   accel: /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_accel is_si=False scale_override=0.00341
[lifecycle_manager-15] [INFO] [1783764826.591272577] [lifecycle_manager_keepout]: Server keepout_filter_info_server connected with bond.
[lifecycle_manager-15] [INFO] [1783764826.591598244] [lifecycle_manager_keepout]: Managed nodes are active
[lifecycle_manager-15] [INFO] [1783764826.591705994] [lifecycle_manager_keepout]: Creating bond timer...
[aurora930_node-9] I0711 18:13:46.653708 11809 aurora900_ros2_device.cc:304] BOOT_ORDER_1::Device information:
[aurora930_node-9] I0711 18:13:46.653867 11809 aurora900_ros2_device.cc:305]     sdk version: 1.1.22
[aurora930_node-9] I0711 18:13:46.653910 11809 aurora900_ros2_device.cc:306]     device name: Aurora 930
[aurora930_node-9] I0711 18:13:46.653940 11809 aurora900_ros2_device.cc:307]     serial number: HY400529001015314G00248
[aurora930_node-9] I0711 18:13:46.653967 11809 aurora900_ros2_device.cc:308]     firmware version: 1.7.2
[aurora930_node-9] I0711 18:13:46.654021 11809 camera_parameters.cc:134] BOOT_ORDER_1::Camera Parameters:
[aurora930_node-9] I0711 18:13:46.654052 11809 camera_parameters.cc:135] BOOT_ORDER_1::  Ir Intrinsics:
[aurora930_node-9] I0711 18:13:46.654078 11809 camera_parameters.cc:146]                 Resolution:
[aurora930_node-9] I0711 18:13:46.654105 11809 camera_parameters.cc:147]                         Rows:400
[aurora930_node-9] I0711 18:13:46.654132 11809 camera_parameters.cc:148]                         Cols:640
[aurora930_node-9] I0711 18:13:46.654158 11809 camera_parameters.cc:149]                 Intrinsics:
[aurora930_node-9] I0711 18:13:46.654186 11809 camera_parameters.cc:150]                         fx: 421.307
[aurora930_node-9] I0711 18:13:46.654282 11809 camera_parameters.cc:151]                         fy: 422.254
[aurora930_node-9] I0711 18:13:46.654318 11809 camera_parameters.cc:152]                         cx: 320.27
[aurora930_node-9] I0711 18:13:46.654351 11809 camera_parameters.cc:153]                         cy: 197.01
[aurora930_node-9] I0711 18:13:46.654384 11809 camera_parameters.cc:154]                         k1: 0.0606853
[aurora930_node-9] I0711 18:13:46.654417 11809 camera_parameters.cc:155]                         k2: -0.10961
[aurora930_node-9] I0711 18:13:46.654450 11809 camera_parameters.cc:156]                         p1: 0.00126689
[aurora930_node-9] I0711 18:13:46.654484 11809 camera_parameters.cc:157]                         p2: -0.00120539
[aurora930_node-9] I0711 18:13:46.654515 11809 camera_parameters.cc:158]                         k3: 0.0522281
[aurora930_node-9] I0711 18:13:46.654547 11809 camera_parameters.cc:138] BOOT_ORDER_1::  Rgb Intrinsics:
[aurora930_node-9] I0711 18:13:46.654575 11809 camera_parameters.cc:146]                 Resolution:
[aurora930_node-9] I0711 18:13:46.654601 11809 camera_parameters.cc:147]                         Rows:400
[aurora930_node-9] I0711 18:13:46.654628 11809 camera_parameters.cc:148]                         Cols:640
[aurora930_node-9] I0711 18:13:46.654654 11809 camera_parameters.cc:149]                 Intrinsics:
[aurora930_node-9] I0711 18:13:46.654680 11809 camera_parameters.cc:150]                         fx: 416.49
[aurora930_node-9] I0711 18:13:46.654713 11809 camera_parameters.cc:151]                         fy: 417.383
[aurora930_node-9] I0711 18:13:46.654747 11809 camera_parameters.cc:152]                         cx: 316.832
[aurora930_node-9] I0711 18:13:46.654779 11809 camera_parameters.cc:153]                         cy: 188.753
[aurora930_node-9] I0711 18:13:46.654811 11809 camera_parameters.cc:154]                         k1: 0.00611878
[aurora930_node-9] I0711 18:13:46.654843 11809 camera_parameters.cc:155]                         k2: -0.0490436
[aurora930_node-9] I0711 18:13:46.654875 11809 camera_parameters.cc:156]                         p1: 0.000399548
[aurora930_node-9] I0711 18:13:46.654907 11809 camera_parameters.cc:157]                         p2: 0.000563892
[aurora930_node-9] I0711 18:13:46.654939 11809 camera_parameters.cc:158]                         k3: 0.0308458
[aurora930_node-9] I0711 18:13:46.654971 11809 camera_parameters.cc:141] BOOT_ORDER_1::  Ir to Rgb Extrinsic:
[aurora930_node-9] I0711 18:13:46.654999 11809 camera_parameters.cc:162]                 Extrinsics:
[aurora930_node-9] I0711 18:13:46.655025 11809 camera_parameters.cc:163]                         Rotation[0]: 0.999973, 0.00724076, -0.00112023
[aurora930_node-9] I0711 18:13:46.655062 11809 camera_parameters.cc:165]                         Rotation[1]: -0.00724006, 0.999973, 0.000633162
[aurora930_node-9] I0711 18:13:46.655100 11809 camera_parameters.cc:167]                         Rotation[2]: 0.00112478, -0.000625033, 0.999999
[aurora930_node-9] I0711 18:13:46.655190 11809 camera_parameters.cc:169]                         Translation: -9.88662, 0.117748, 0.603513
[aurora930_node-9] 2026-07-11 18:13:46.655 (   1.458s) [        83974020]      aurora900_impl.cc:578   INFO| stream_mask_:0, rgb_stream_count_:1
[bmi088_iio_bridge.py-5] [INFO] [1783764826.661577425] [bmi088_iio_bridge]: BMI088 IIO Bridge 启动 @ 50Hz -> /imu_data  [OK]
[imu_madgwick_filter.py-6] [INFO] [1783764826.663921762] [imu_madgwick_bmi088]: [imu_madgwick] init: beta=0.0030, gyro_noise=0.0002, accel_noise=0.010
[imu_madgwick_filter.py-6] [INFO] [1783764826.699358187] [imu_madgwick_bmi088]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-6] [INFO] [1783764826.701806565] [imu_madgwick_bmi088]: [imu_madgwick] accel init: roll=-2.1deg, pitch=-3.1deg
[imu_madgwick_filter.py-4] [INFO] [1783764826.725780932] [imu_madgwick_filter]: [imu_madgwick] init: beta=0.0330, gyro_noise=0.0010, accel_noise=0.050
[imu_madgwick_filter.py-4] [INFO] [1783764826.731300440] [imu_madgwick_filter]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[qr_decision.py-11] [INFO] [1783764826.732842442] [qr_decision]: qr_decision started: cooldown=3.0s, awaiting /sign from qr_decoder
[imu_madgwick_filter.py-4] [INFO] [1783764826.733978235] [imu_madgwick_filter]: [imu_madgwick] accel init: roll=-0.0deg, pitch=0.2deg
[aurora930_node-9] 2026-07-11 18:13:46.970 (   1.773s) [        4F7E57E0]deptrum_camera_aurora93:407    ERR| recv first frame time is 1783764826970
[lslidar_driver_node-2] port = /dev/ttyACM1, baud_rate = 230400
[lslidar_driver_node-2] open_port /dev/ttyACM1 OK !
[vision_ai_node-12] [INFO] [1783764829.963517404] [vision_ai_node]: Loaded config: /userdata/dev_ws/install/racing_vision_ai/share/racing_vision_ai/config/vision_ai_config.yaml
[vision_ai_node-12] [INFO] [1783764830.357792170] [vision_ai_node]: Volcengine Ark client initialized
[vision_ai_node-12] [INFO] [1783764830.371436356] [vision_ai_node]: Vision AI Node initialized (JPU JPEG mode)
[vision_ai_node-12] [INFO] [1783764830.374127568] [vision_ai_node]: Waiting for sign4return=100
[vision_ai_node-12] [INFO] [1783764830.376460321] [vision_ai_node]: Image topic: /aurora/rgb/image_jpeg
[INFO] [component_container_isolated-16]: process started with pid [12060]
[bmi088_iio_bridge.py-5] [INFO] [1783764832.331429634] [bmi088_iio_bridge]:   gyro bias calibrated: (0.002767, 0.001206, -0.002727) rad/s
[INFO] [competition_master_stage2.py-17]: process started with pid [12062]
[INFO] [rviz2-18]: process started with pid [12064]
[component_container_isolated-16] [INFO] [1783764833.173975290] [nav2_container]: Load Library: /opt/ros/humble/lib/libcontroller_server_core.so
[component_container_isolated-16] [INFO] [1783764833.211999053] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-16] [INFO] [1783764833.212192511] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-16] [INFO] [1783764833.296128214] [controller_server]:
[component_container_isolated-16]       controller_server lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1783764833.324652422] [controller_server]: Creating controller server
[component_container_isolated-16] [INFO] [1783764833.409968460] [local_costmap.local_costmap]:
[component_container_isolated-16]       local_costmap lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1783764833.413589507] [local_costmap.local_costmap]: Creating Costmap
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/controller_server' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1783764833.433690869] [nav2_container]: Load Library: /opt/ros/humble/lib/libmap_server_core.so
[component_container_isolated-16] [INFO] [1783764833.504528220] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::CostmapFilterInfoServer>
[component_container_isolated-16] [INFO] [1783764833.504723887] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapSaver>
[component_container_isolated-16] [INFO] [1783764833.504802553] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-16] [INFO] [1783764833.504861970] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-16] [INFO] [1783764833.564108096] [map_server]:
[component_container_isolated-16]       map_server lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1783764833.564397930] [map_server]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/map_server' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1783764833.569412770] [nav2_container]: Load Library: /opt/ros/humble/lib/libsmoother_server_core.so
[component_container_isolated-16] [INFO] [1783764833.578508492] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-16] [INFO] [1783764833.578681742] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-16] [INFO] [1783764833.644908711] [smoother_server]:
[component_container_isolated-16]       smoother_server lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1783764833.657116187] [smoother_server]: Creating smoother server
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/smoother_server' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1783764833.665948783] [nav2_container]: Load Library: /opt/ros/humble/lib/libamcl_core.so
[component_container_isolated-16] [INFO] [1783764833.675283421] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-16] [INFO] [1783764833.675450088] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-16] [INFO] [1783764833.760992335] [amcl]:
[component_container_isolated-16]       amcl lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1783764833.763830797] [amcl]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/amcl' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1783764833.867794779] [nav2_container]: Load Library: /opt/ros/humble/lib/libplanner_server_core.so
[component_container_isolated-16] [INFO] [1783764833.872335619] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-16] [INFO] [1783764833.872514119] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-16] [INFO] [1783764833.945249556] [planner_server]:
[component_container_isolated-16]       planner_server lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1783764833.959563535] [planner_server]: Creating
[component_container_isolated-16] [INFO] [1783764834.053250085] [global_costmap.global_costmap]:
[component_container_isolated-16]       global_costmap lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1783764834.056883340] [global_costmap.global_costmap]: Creating Costmap
[component_container_isolated-16] [INFO] [1783764834.100722986] [nav2_container]: Load Library: /opt/ros/humble/lib/libnav2_lifecycle_manager_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/planner_server' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1783764834.104404158] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-16] [INFO] [1783764834.104596575] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-16] [INFO] [1783764834.186655192] [lifecycle_manager_localization]: Creating
[component_container_isolated-16] [INFO] [1783764834.215010066] [nav2_container]: Load Library: /opt/ros/humble/lib/libbehavior_server_core.so
[component_container_isolated-16] [INFO] [1783764834.215942234] [lifecycle_manager_localization]: Creating and initializing lifecycle service clients
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_localization' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1783764834.239500226] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-16] [INFO] [1783764834.239746726] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-16] [INFO] [1783764834.299586395] [lifecycle_manager_localization]: Starting managed nodes bringup...
[component_container_isolated-16] [INFO] [1783764834.299872021] [lifecycle_manager_localization]: Configuring map_server
[component_container_isolated-16] [INFO] [1783764834.301047814] [map_server]: Configuring
[component_container_isolated-16] [INFO] [1783764834.301382481] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.yaml
[component_container_isolated-16] [INFO] [1783764834.304698611] [map_io]: resolution: 0.05
[component_container_isolated-16] [INFO] [1783764834.304832444] [map_io]: origin[0]: -2.65
[component_container_isolated-16] [INFO] [1783764834.304885069] [map_io]: origin[1]: -4.5
[component_container_isolated-16] [INFO] [1783764834.304916944] [map_io]: origin[2]: 0
[component_container_isolated-16] [INFO] [1783764834.304951069] [map_io]: free_thresh: 0.25
[component_container_isolated-16] [INFO] [1783764834.304980986] [map_io]: occupied_thresh: 0.65
[component_container_isolated-16] [INFO] [1783764834.305042778] [map_io]: mode: trinary
[component_container_isolated-16] [INFO] [1783764834.305078611] [map_io]: negate: 0
[component_container_isolated-16] [INFO] [1783764834.305863737] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm
[component_container_isolated-16] [INFO] [1783764834.358373646] [behavior_server]:
[component_container_isolated-16]       behavior_server lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1783764834.373552501] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm: 163 X 141 map @ 0.05 m/cell
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/behavior_server' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1783764834.419034482] [lifecycle_manager_localization]: Configuring amcl
[component_container_isolated-16] [INFO] [1783764834.419935900] [amcl]: Configuring
[component_container_isolated-16] [INFO] [1783764834.420349193] [amcl]: initTransforms
[component_container_isolated-16] [INFO] [1783764834.424969741] [nav2_container]: Load Library: /opt/ros/humble/lib/libbt_navigator_core.so
[component_container_isolated-16] [INFO] [1783764834.441355014] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-16] [INFO] [1783764834.441524765] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-16] [INFO] [1783764834.523612423] [amcl]: initPubSub
[component_container_isolated-16] [INFO] [1783764834.560118559] [amcl]: Subscribed to map topic.
[component_container_isolated-16] [INFO] [1783764834.601032117] [lifecycle_manager_localization]: Activating map_server
[component_container_isolated-16] [INFO] [1783764834.601960910] [map_server]: Activating
[component_container_isolated-16] [INFO] [1783764834.602585911] [map_server]: Creating bond (map_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764834.605389332] [amcl]: Received a 163 X 141 map @ 0.050 m/pix
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/bt_navigator' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1783764834.606250000] [bt_navigator]:
[component_container_isolated-16]       bt_navigator lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1783764834.608971629] [bt_navigator]: Creating
[component_container_isolated-16] [INFO] [1783764834.630011450] [nav2_container]: Load Library: /opt/ros/humble/lib/libwaypoint_follower_core.so
[component_container_isolated-16] [INFO] [1783764834.634749249] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-16] [INFO] [1783764834.635280041] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-16] [INFO] [1783764834.718251118] [lifecycle_manager_localization]: Server map_server connected with bond.
[component_container_isolated-16] [INFO] [1783764834.718515660] [lifecycle_manager_localization]: Activating amcl
[component_container_isolated-16] [INFO] [1783764834.719802870] [amcl]: Activating
[component_container_isolated-16] [INFO] [1783764834.720044204] [amcl]: initialPoseReceived
[component_container_isolated-16] [INFO] [1783764834.720566413] [amcl]: Setting pose (1783764834.720560): -1.985 -0.014 0.262
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/waypoint_follower' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1783764834.720790622] [waypoint_follower]:
[component_container_isolated-16]       waypoint_follower lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1783764834.722899833] [amcl]: Creating bond (amcl) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764834.724176585] [waypoint_follower]: Creating
[component_container_isolated-16] [INFO] [1783764834.754424961] [nav2_container]: Load Library: /opt/ros/humble/lib/libvelocity_smoother_core.so
[component_container_isolated-16] [INFO] [1783764834.758406550] [amcl]: createLaserObject
[component_container_isolated-16] [INFO] [1783764834.759262843] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-16] [INFO] [1783764834.759411094] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-16] [INFO] [1783764834.844144465] [lifecycle_manager_localization]: Server amcl connected with bond.
[component_container_isolated-16] [INFO] [1783764834.844321506] [lifecycle_manager_localization]: Managed nodes are active
[component_container_isolated-16] [INFO] [1783764834.844441090] [lifecycle_manager_localization]: Creating bond timer...
[component_container_isolated-16] [INFO] [1783764834.870124710] [velocity_smoother]:
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/velocity_smoother' in container '/nav2_container'
[component_container_isolated-16]       velocity_smoother lifecycle node launched.
[component_container_isolated-16]       Waiting on external lifecycle transitions to activate
[component_container_isolated-16]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-16] [INFO] [1783764834.900964879] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-16] [INFO] [1783764834.901178171] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-16] [INFO] [1783764834.978186948] [lifecycle_manager_navigation]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_navigation' in container '/nav2_container'
[component_container_isolated-16] [INFO] [1783764835.012431247] [lifecycle_manager_navigation]: Creating and initializing lifecycle service clients
[component_container_isolated-16] [INFO] [1783764835.134719255] [lifecycle_manager_navigation]: Starting managed nodes bringup...
[component_container_isolated-16] [INFO] [1783764835.134952255] [lifecycle_manager_navigation]: Configuring controller_server
[component_container_isolated-16] [INFO] [1783764835.136473924] [controller_server]: Configuring controller interface
[component_container_isolated-16] [INFO] [1783764835.137656759] [controller_server]: getting goal checker plugins..
[component_container_isolated-16] [INFO] [1783764835.146458397] [controller_server]: Controller frequency set to 10.0000Hz
[component_container_isolated-16] [INFO] [1783764835.146799981] [local_costmap.local_costmap]: Configuring
[component_container_isolated-16] [INFO] [1783764835.201982101] [local_costmap.local_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-16] [INFO] [1783764835.245857622] [local_costmap.local_costmap]: Subscribed to Topics: scan
[component_container_isolated-16] [INFO] [1783764835.300123450] [local_costmap.local_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-16] [INFO] [1783764835.300322825] [local_costmap.local_costmap]: Using plugin "voxel_layer"
[component_container_isolated-16] [INFO] [1783764835.319123644] [local_costmap.local_costmap]: Subscribed to Topics: depth_points
[component_container_isolated-16] [INFO] [1783764835.404769892] [local_costmap.local_costmap]: Initialized plugin "voxel_layer"
[component_container_isolated-16] [INFO] [1783764835.406532311] [local_costmap.local_costmap]: Using plugin "keepout_filter"
[component_container_isolated-16] [INFO] [1783764835.434023975] [local_costmap.local_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-16] [INFO] [1783764835.434274017] [local_costmap.local_costmap]: Using plugin "inflation_layer"
[component_container_isolated-16] [INFO] [1783764835.452833502] [local_costmap.local_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-16] [INFO] [1783764835.517719803] [controller_server]: Created progress_checker : progress_checker of type nav2_controller::SimpleProgressChecker
[component_container_isolated-16] [INFO] [1783764835.525031980] [controller_server]: Created goal checker : goal_checker of type nav2_controller::SimpleGoalChecker
[component_container_isolated-16] [INFO] [1783764835.532775241] [controller_server]: Controller Server has goal_checker  goal checkers available.
[component_container_isolated-16] [INFO] [1783764835.536335455] [controller_server]: Created controller : FollowPath of type nav2_regulated_pure_pursuit_controller::RegulatedPurePursuitController
[competition_master_stage2.py-17] [INFO] [1783764835.589038155] [competition_master_stage2]: === [Stage 2] 总控节点初始化 ===
[competition_master_stage2.py-17] [INFO] [1783764835.595120497] [competition_master_stage2]:   参数: nav_timeout=180.0s, qr_point=(0.41, -3.17, yaw=0.00), entry_point=(0.38, -1.10, yaw=0.00)
[component_container_isolated-16] [INFO] [1783764835.619717074] [controller_server]: Controller Server has FollowPath  controllers available.
[component_container_isolated-16] [INFO] [1783764835.667250351] [lifecycle_manager_navigation]: Configuring smoother_server
[component_container_isolated-16] [INFO] [1783764835.667882560] [smoother_server]: Configuring smoother server
[component_container_isolated-16] [INFO] [1783764835.719954468] [smoother_server]: Created smoother : SmoothPath of type nav2_constrained_smoother/ConstrainedSmoother
[component_container_isolated-16] [INFO] [1783764835.758128272] [smoother_server]: Smoother Server has SmoothPath  smoothers available.
[component_container_isolated-16] [INFO] [1783764835.790791611] [lifecycle_manager_navigation]: Configuring planner_server
[component_container_isolated-16] [INFO] [1783764835.791634945] [planner_server]: Configuring
[component_container_isolated-16] [INFO] [1783764835.792005029] [global_costmap.global_costmap]: Configuring
[component_container_isolated-16] [INFO] [1783764835.835048882] [global_costmap.global_costmap]: Using plugin "static_layer"
[component_container_isolated-16] [INFO] [1783764835.853539992] [global_costmap.global_costmap]: Subscribing to the map topic (/map) with transient local durability
[component_container_isolated-16] [INFO] [1783764835.859251459] [global_costmap.global_costmap]: Initialized plugin "static_layer"
[component_container_isolated-16] [INFO] [1783764835.859420084] [global_costmap.global_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-16] [INFO] [1783764835.873531063] [global_costmap.global_costmap]: Subscribed to Topics: scan
[component_container_isolated-16] [INFO] [1783764835.920438463] [global_costmap.global_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-16] [INFO] [1783764835.920766089] [global_costmap.global_costmap]: Using plugin "voxel_layer"
[component_container_isolated-16] [INFO] [1783764835.933067648] [global_costmap.global_costmap]: Subscribed to Topics: depth_points
[component_container_isolated-16] [INFO] [1783764835.988901936] [global_costmap.global_costmap]: Initialized plugin "voxel_layer"
[component_container_isolated-16] [INFO] [1783764835.989119936] [global_costmap.global_costmap]: Using plugin "keepout_filter"
[component_container_isolated-16] [INFO] [1783764836.003440540] [global_costmap.global_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-16] [INFO] [1783764836.004030041] [global_costmap.global_costmap]: Using plugin "inflation_layer"
[component_container_isolated-16] [INFO] [1783764836.013771555] [global_costmap.global_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-16] [INFO] [1783764836.063322418] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 163 X 141 at 0.050000 m/pix
[component_container_isolated-16] [INFO] [1783764836.087102994] [planner_server]: Created global planner plugin GridBased of type nav2_smac_planner/SmacPlannerHybrid
[component_container_isolated-16] [INFO] [1783764836.087348161] [planner_server]: Configuring GridBased of type SmacPlannerHybrid
[component_container_isolated-16] [INFO] [1783764836.135236688] [planner_server]: Even sized heuristic lookup table size set 266.000000, increasing size by 1 to make odd
[imu_madgwick_filter.py-6] [INFO] [1783764836.527630876] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=428 q_w=0.9994 angle=4.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783764836.587810712] [imu_madgwick_filter]: [imu_madgwick ->] msgs=200 q_w=0.9984 angle=6.5deg beta=0.0330
[rviz2-18] [INFO] [1783764836.711337306] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-18] [INFO] [1783764836.712120140] [rviz2]: OpenGl version: 4.5 (GLSL 4.5)
[rviz2-18] [INFO] [1783764836.953830529] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-18] [INFO] [1783764839.239081779] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[rviz2-18] [ERROR] [1783764839.731938991] [rviz2]: Vertex Program:rviz/glsl120/indexed_8bit_image.vert Fragment Program:rviz/glsl120/indexed_8bit_image.frag GLSL link result :
[rviz2-18] active samplers with a different type refer to the same texture image unit
[qr_decoder-10] [INFO] [1783764842.807006160] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=200 last_qr_frame=-1 gap=-1 frames rejects=0
[competition_master_stage2.py-17] [INFO] [1783764843.600005899] [competition_master_stage2]: >>> 系统就绪, 开始 Stage 2 导航
[imu_madgwick_filter.py-6] [INFO] [1783764846.526202056] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=925 q_w=0.9994 angle=4.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783764846.592250611] [imu_madgwick_filter]: [imu_madgwick ->] msgs=400 q_w=0.9935 angle=13.0deg beta=0.0330
[competition_master_stage2.py-17] [WARN] [1783764846.614180726] [competition_master_stage2]: navigate_to_pose action server 未就绪 (3s 超时), 跳过导航目标 [任务发布点]. 3s 后重试.
[competition_master_stage2.py-17] [INFO] [1783764849.618386110] [competition_master_stage2]: 重试发送导航目标 (QR点)...
[competition_master_stage2.py-17] [WARN] [1783764852.632164245] [competition_master_stage2]: navigate_to_pose action server 未就绪 (3s 超时), 跳过导航目标 [任务发布点]. 3s 后重试.
[competition_master_stage2.py-17] [INFO] [1783764855.637445979] [competition_master_stage2]: 重试发送导航目标 (QR点)...
[imu_madgwick_filter.py-6] [INFO] [1783764856.525108267] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1422 q_w=0.9994 angle=4.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783764856.594796038] [imu_madgwick_filter]: [imu_madgwick ->] msgs=600 q_w=0.9853 angle=19.6deg beta=0.0330
[component_container_isolated-16] [INFO] [1783764856.603617593] [planner_server]: Configured plugin GridBased of type SmacPlannerHybrid with maximum iterations 1500, max on approach iterations 300, and not allowing unknown traversal. Tolerance 0.50.Using motion model: Reeds-Shepp.
[component_container_isolated-16] [INFO] [1783764856.603866718] [planner_server]: Planner Server has GridBased  planners available.
[component_container_isolated-16] [INFO] [1783764856.665307102] [lifecycle_manager_navigation]: Configuring behavior_server
[component_container_isolated-16] [INFO] [1783764856.666225854] [behavior_server]: Configuring
[component_container_isolated-16] [INFO] [1783764856.706632997] [behavior_server]: Creating behavior plugin spin of type nav2_behaviors/Spin
[component_container_isolated-16] [INFO] [1783764856.711425463] [behavior_server]: Configuring spin
[component_container_isolated-16] [INFO] [1783764856.755065612] [behavior_server]: Creating behavior plugin backup of type nav2_behaviors/BackUp
[component_container_isolated-16] [INFO] [1783764856.759634869] [behavior_server]: Configuring backup
[component_container_isolated-16] [INFO] [1783764856.796408632] [behavior_server]: Creating behavior plugin drive_on_heading of type nav2_behaviors/DriveOnHeading
[component_container_isolated-16] [INFO] [1783764856.800412096] [behavior_server]: Configuring drive_on_heading
[component_container_isolated-16] [INFO] [1783764856.844429579] [behavior_server]: Creating behavior plugin wait of type nav2_behaviors/Wait
[component_container_isolated-16] [INFO] [1783764856.850308588] [behavior_server]: Configuring wait
[component_container_isolated-16] [INFO] [1783764856.881992469] [lifecycle_manager_navigation]: Configuring bt_navigator
[component_container_isolated-16] [INFO] [1783764856.883177221] [bt_navigator]: Configuring
[competition_master_stage2.py-17] [INFO] [1783764857.166012520] [competition_master_stage2]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-16] [INFO] [1783764857.343926621] [lifecycle_manager_navigation]: Configuring waypoint_follower
[competition_master_stage2.py-17] [WARN] [1783764857.348277002] [competition_master_stage2]: 导航目标被拒绝, 3s 后重试...
[component_container_isolated-16] [INFO] [1783764857.349137754] [waypoint_follower]: Configuring
[component_container_isolated-16] [INFO] [1783764857.442104310] [waypoint_follower]: Created waypoint_task_executor : wait_at_waypoint of type nav2_waypoint_follower::WaitAtWaypoint
[component_container_isolated-16] [INFO] [1783764857.451456616] [lifecycle_manager_navigation]: Configuring velocity_smoother
[component_container_isolated-16] [INFO] [1783764857.452721159] [velocity_smoother]: Configuring velocity smoother
[component_container_isolated-16] [INFO] [1783764857.485165916] [lifecycle_manager_navigation]: Activating controller_server
[component_container_isolated-16] [INFO] [1783764857.486874336] [controller_server]: Activating
[component_container_isolated-16] [INFO] [1783764857.487310878] [local_costmap.local_costmap]: Activating
[component_container_isolated-16] [INFO] [1783764857.487502587] [local_costmap.local_costmap]: Checking transform
[component_container_isolated-16] [INFO] [1783764857.487937296] [local_costmap.local_costmap]: start
[component_container_isolated-16] [INFO] [1783764857.504868904] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1783764857.519010509] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1783764857.519204343] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1783764857.532100904] [local_costmap.local_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[component_container_isolated-16] [INFO] [1783764857.719152518] [controller_server]: Activating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-16] [INFO] [1783764857.719556185] [controller_server]: Creating bond (controller_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764857.831728937] [lifecycle_manager_navigation]: Server controller_server connected with bond.
[component_container_isolated-16] [INFO] [1783764857.832025479] [lifecycle_manager_navigation]: Activating smoother_server
[component_container_isolated-16] [INFO] [1783764857.833528731] [smoother_server]: Activating
[component_container_isolated-16] [INFO] [1783764857.833764982] [smoother_server]: Activating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-16] [INFO] [1783764857.833844774] [smoother_server]: Creating bond (smoother_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764857.947827778] [lifecycle_manager_navigation]: Server smoother_server connected with bond.
[component_container_isolated-16] [INFO] [1783764857.948006237] [lifecycle_manager_navigation]: Activating planner_server
[component_container_isolated-16] [INFO] [1783764857.948999655] [planner_server]: Activating
[component_container_isolated-16] [INFO] [1783764857.949259114] [global_costmap.global_costmap]: Activating
[component_container_isolated-16] [INFO] [1783764857.949386281] [global_costmap.global_costmap]: Checking transform
[component_container_isolated-16] [INFO] [1783764857.949651489] [global_costmap.global_costmap]: start
[component_container_isolated-16] [INFO] [1783764857.960879048] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-16] [INFO] [1783764857.967784600] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-16] [INFO] [1783764857.968074934] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-16] [INFO] [1783764857.979069742] [global_costmap.global_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[qr_decoder-10] [INFO] [1783764858.008168036] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=400 last_qr_frame=-1 gap=-1 frames rejects=0
[rviz2-18] [INFO] [1783764858.169219570] [rviz2]: Trying to create a map of size 60 x 60 using 1 swatches
[component_container_isolated-16] [INFO] [1783764859.068041590] [planner_server]: Activating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-16] [INFO] [1783764859.075281059] [planner_server]: Creating bond (planner_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764859.211879099] [lifecycle_manager_navigation]: Server planner_server connected with bond.
[component_container_isolated-16] [INFO] [1783764859.212072474] [lifecycle_manager_navigation]: Activating behavior_server
[component_container_isolated-16] [INFO] [1783764859.213281767] [behavior_server]: Activating
[component_container_isolated-16] [INFO] [1783764859.213406726] [behavior_server]: Activating spin
[component_container_isolated-16] [INFO] [1783764859.213565476] [behavior_server]: Activating backup
[component_container_isolated-16] [INFO] [1783764859.213656476] [behavior_server]: Activating drive_on_heading
[component_container_isolated-16] [INFO] [1783764859.213732851] [behavior_server]: Activating wait
[component_container_isolated-16] [INFO] [1783764859.213818060] [behavior_server]: Creating bond (behavior_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764859.335279368] [lifecycle_manager_navigation]: Server behavior_server connected with bond.
[component_container_isolated-16] [INFO] [1783764859.335456993] [lifecycle_manager_navigation]: Activating bt_navigator
[component_container_isolated-16] [INFO] [1783764859.336578620] [bt_navigator]: Activating
[rviz2-18] [INFO] [1783764859.398039754] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[component_container_isolated-16] [WARN] [1783764859.473539868] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-16] [WARN] [1783764859.544491642] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-16] [WARN] [1783764859.573194727] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-16] [WARN] [1783764859.685737063] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-16] [WARN] [1783764859.879807231] [bt_navigator_navigate_to_pose_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-16] [INFO] [1783764860.098968521] [bt_navigator]: Creating bond (bt_navigator) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764860.220846913] [lifecycle_manager_navigation]: Server bt_navigator connected with bond.
[component_container_isolated-16] [INFO] [1783764860.221043288] [lifecycle_manager_navigation]: Activating waypoint_follower
[component_container_isolated-16] [INFO] [1783764860.222328499] [waypoint_follower]: Activating
[component_container_isolated-16] [INFO] [1783764860.222573666] [waypoint_follower]: Creating bond (waypoint_follower) to lifecycle manager.
[competition_master_stage2.py-17] [INFO] [1783764860.352566446] [competition_master_stage2]: 重试发送导航目标 (QR点)...
[competition_master_stage2.py-17] [INFO] [1783764860.366252841] [competition_master_stage2]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-16] [INFO] [1783764860.368806637] [lifecycle_manager_navigation]: Server waypoint_follower connected with bond.
[component_container_isolated-16] [INFO] [1783764860.368987137] [lifecycle_manager_navigation]: Activating velocity_smoother
[component_container_isolated-16] [INFO] [1783764860.371564516] [velocity_smoother]: Activating
[component_container_isolated-16] [INFO] [1783764860.373384935] [velocity_smoother]: Creating bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764860.383720909] [bt_navigator]: Begin navigating from current location (-1.98, -0.01) to (0.41, -3.17)
[competition_master_stage2.py-17] [INFO] [1783764860.394717593] [competition_master_stage2]: 导航目标已接受，车辆出发...
[component_container_isolated-16] [INFO] [1783764860.511629228] [lifecycle_manager_navigation]: Server velocity_smoother connected with bond.
[component_container_isolated-16] [INFO] [1783764860.511817728] [lifecycle_manager_navigation]: Managed nodes are active
[component_container_isolated-16] [INFO] [1783764860.511900853] [lifecycle_manager_navigation]: Creating bond timer...
[component_container_isolated-16] [INFO] [1783764860.586079965] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-16] [WARN] [1783764860.588648552] [controller_server]: No goal checker was specified in parameter 'current_goal_checker'. Server will use only plugin loaded goal_checker . This warning will appear once.
[component_container_isolated-16] [INFO] [1783764861.889060604] [controller_server]: Passing new path to controller.
[component_container_isolated-16] Reallocing temp weights 301 - 60
[component_container_isolated-16] Reallocing temp weights 1500 - 60
[component_container_isolated-16] [INFO] [1783764863.189050828] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [INFO] [1783764864.488988890] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [INFO] [1783764865.789054498] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-6] [INFO] [1783764866.525572624] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1861 q_w=0.7125 angle=89.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783764866.589334305] [imu_madgwick_filter]: [imu_madgwick ->] msgs=800 q_w=0.8562 angle=62.2deg beta=0.0330
[component_container_isolated-16] [INFO] [1783764867.089058445] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764868.291639039] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.20, -2.95, 0.00) to (3.18, 0.03, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764868.389051897] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764868.491948222] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.25, -3.05, 0.00) to (3.23, -0.07, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764868.691449362] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.30, -3.10, 0.00) to (3.28, -0.12, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764868.893085463] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.35, -3.20, 0.00) to (3.33, -0.22, 0.75). The costmap cannot raytrace for it.
[qr_decoder-10] [INFO] [1783764869.020532784] [qr_decoder_zbar]: [qr_decoder] QR DETECTED frame=539 symbols=1 (gap=-1 frames)
[qr_decoder-10] [INFO] [1783764869.020787576] [qr_decoder_zbar]: [QR] 11 | depth=0mm (advisory, publishing anyway)
[qr_decoder-10] [INFO] [1783764869.021261993] [qr_decoder_zbar]: [QR] 11 | robot_pos: (0.99, -2.54, yaw=-1.36)
[competition_master_stage2.py-17] [INFO] [1783764869.029764340] [competition_master_stage2]: [QR检测] 内容: 11
[qr_decision.py-11] [INFO] [1783764869.027498128] [qr_decision]: [QR] 11 CW @ (x=0.99, y=-2.56, yaw=-1.35) → /qr_event
[qr_decision.py-11] [INFO] [1783764869.036509559] [qr_decision]: [检查点] qr_decision 发布 /qr_event (由 task_manager 决定停车)
[component_container_isolated-16] [WARN] [1783764869.095316316] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.40, -3.25, 0.00) to (3.38, -0.27, 0.75). The costmap cannot raytrace for it.
[qr_decoder-10] [INFO] [1783764869.103030494] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[competition_master_stage2.py-17] [INFO] [1783764869.107188959] [competition_master_stage2]: 已终止进程: qr_decoder_zbar
[competition_master_stage2.py-17] [INFO] [1783764869.115901181] [competition_master_stage2]: >>> QR 解码已关闭, 等待方向判断 (/qr_event)...
[competition_master_stage2.py-17] [INFO] [1783764869.120282104] [competition_master_stage2]: [QR检测] 取消当前导航目标, 等待BT完成 cancel/halt 清理...
[competition_master_stage2.py-17] [INFO] [1783764869.136569879] [competition_master_stage2]: [QR事件] 方向: 顺时针 (通道巡航阶段使用)
[component_container_isolated-16] [INFO] [1783764869.189062293] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-16] [INFO] [1783764869.189276127] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-16] [INFO] [1783764869.190954296] [bt_navigator]: [navigate_to_pose] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-16] [INFO] [1783764869.191861798] [bt_navigator]: Goal canceled
[competition_master_stage2.py-17] [INFO] [1783764869.222796429] [competition_master_stage2]: 已终止进程: qr_decision
[competition_master_stage2.py-17] [INFO] [1783764869.234360446] [competition_master_stage2]: [结果回调] BT取消确认完成 (STATUS_CANCELED), 准备发送通道入口目标...
[competition_master_stage2.py-17] [INFO] [1783764869.245879339] [competition_master_stage2]: >>> BT取消确认完成, 先后退 22cm 远离 keepout 边界再发送通道入口目标...
[competition_master_stage2.py-17] [INFO] [1783764869.249820595] [competition_master_stage2]: [BACKUP] 右后退中: vx=-0.15 wz=-2.80, 6.0s
[component_container_isolated-16] [WARN] [1783764869.291204825] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.45, -3.30, 0.00) to (3.43, -0.32, 0.75). The costmap cannot raytrace for it.
[INFO] [qr_decoder-10]: process has finished cleanly [pid 11811]
[component_container_isolated-16] [WARN] [1783764869.491416509] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.50, -3.40, 0.00) to (3.48, -0.42, 0.75). The costmap cannot raytrace for it.
[qr_decision.py-11] Traceback (most recent call last):
[qr_decision.py-11]   File "/userdata/dev_ws/install/qr_decoder/lib/qr_decoder/qr_decision.py", line 107, in <module>
[qr_decision.py-11]     main()
[qr_decision.py-11]   File "/userdata/dev_ws/install/qr_decoder/lib/qr_decoder/qr_decision.py", line 97, in main
[qr_decision.py-11]     rclpy.spin(node)
[qr_decision.py-11]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 229, in spin
[qr_decision.py-11]     executor.spin_once()
[qr_decision.py-11]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 808, in spin_once
[qr_decision.py-11]     self._spin_once_impl(timeout_sec)
[qr_decision.py-11]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 797, in _spin_once_impl
[qr_decision.py-11]     handler, entity, node = self.wait_for_ready_callbacks(timeout_sec=timeout_sec)
[qr_decision.py-11]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 780, in wait_for_ready_callbacks
[qr_decision.py-11]     return next(self._cb_iter)
[qr_decision.py-11]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 653, in _wait_for_ready_callbacks
[qr_decision.py-11]     wait_set = _rclpy.WaitSet(
[qr_decision.py-11] rclpy._rclpy_pybind11.RCLError: failed to initialize wait set: the given context is not valid, either rcl_init() was not called or rcl_shutdown() was called., at ./src/rcl/wait.c:130
[component_container_isolated-16] [WARN] [1783764869.691249108] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.55, -3.45, 0.00) to (3.53, -0.47, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764869.891157290] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.60, -3.50, 0.00) to (3.58, -0.52, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764870.098408026] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.65, -3.55, 0.00) to (3.63, -0.57, 0.75). The costmap cannot raytrace for it.
[ERROR] [qr_decision.py-11]: process has died [pid 11813, exit code 1, cmd '/userdata/dev_ws/install/qr_decoder/lib/qr_decoder/qr_decision.py --ros-args -r __node:=qr_decision --params-file /tmp/launch_params_tvlwwm3p'].
[component_container_isolated-16] [WARN] [1783764870.290986615] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.65, -3.55, 0.00) to (3.63, -0.57, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764870.491025590] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.65, -3.55, 0.00) to (3.63, -0.57, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764870.690948648] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.65, -3.55, 0.00) to (3.63, -0.57, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764870.890966748] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.65, -3.55, 0.00) to (3.63, -0.57, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764871.091157515] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.65, -3.55, 0.00) to (3.63, -0.57, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764871.291219241] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.65, -3.55, 0.00) to (3.63, -0.57, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764871.491331175] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.65, -3.55, 0.00) to (3.63, -0.57, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764871.691187067] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.65, -3.55, 0.00) to (3.63, -0.57, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764871.890989001] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.65, -3.55, 0.00) to (3.63, -0.57, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764872.091115310] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.60, -3.55, 0.00) to (3.58, -0.57, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764872.291162828] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.60, -3.50, 0.00) to (3.58, -0.52, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764872.490933221] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.55, -3.50, 0.00) to (3.53, -0.52, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764872.690911489] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.55, -3.50, 0.00) to (3.53, -0.52, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764872.890952131] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.50, -3.50, 0.00) to (3.48, -0.52, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764873.090995025] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.50, -3.50, 0.00) to (3.48, -0.52, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764873.291154627] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.45, -3.50, 0.00) to (3.43, -0.52, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764873.491205395] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.40, -3.50, 0.00) to (3.38, -0.52, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764873.691623123] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.40, -3.50, 0.00) to (3.38, -0.52, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764873.891226015] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.35, -3.50, 0.00) to (3.33, -0.52, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764874.091191034] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.30, -3.50, 0.00) to (3.28, -0.52, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764874.291502720] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.30, -3.50, 0.00) to (3.28, -0.52, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764874.491081114] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.25, -3.50, 0.00) to (3.23, -0.52, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764874.691709092] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.25, -3.50, 0.00) to (3.23, -0.52, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764874.891295360] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.20, -3.55, 0.00) to (3.18, -0.57, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764875.091197421] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.20, -3.55, 0.00) to (3.18, -0.57, 0.75). The costmap cannot raytrace for it.
[competition_master_stage2.py-17] [INFO] [1783764875.252939548] [competition_master_stage2]: [BACKUP] 后退完成, 机器人已远离 keepout 边界, 发送通道入口导航目标...
[competition_master_stage2.py-17] [INFO] [1783764875.260503351] [competition_master_stage2]: >>> 发送导航目标 [通道入口]: (0.38, -1.10, yaw=0.00)
[component_container_isolated-16] [INFO] [1783764875.264072607] [bt_navigator]: Begin navigating from current location (-0.62, -2.19) to (0.38, -1.10)
[competition_master_stage2.py-17] [INFO] [1783764875.274898374] [competition_master_stage2]: 导航目标已接受，车辆出发...
[component_container_isolated-16] [WARN] [1783764875.291142566] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.15, -3.60, 0.00) to (3.13, -0.62, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764875.477183188] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-16] [WARN] [1783764875.491233252] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.15, -3.60, 0.00) to (3.13, -0.62, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764875.691327438] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.15, -3.65, 0.00) to (3.13, -0.67, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764875.891224041] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.15, -3.65, 0.00) to (3.13, -0.67, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764876.093351689] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.15, -3.65, 0.00) to (3.13, -0.67, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764876.291488457] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.15, -3.65, 0.00) to (3.13, -0.67, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764876.491692102] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.15, -3.60, 0.00) to (3.13, -0.62, 0.75). The costmap cannot raytrace for it.
[imu_madgwick_filter.py-6] [INFO] [1783764876.525727447] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2342 q_w=0.9646 angle=30.6deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783764876.588160794] [imu_madgwick_filter]: [imu_madgwick ->] msgs=999 q_w=0.8420 angle=65.3deg beta=0.0330
[component_container_isolated-16] [WARN] [1783764876.691763206] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.15, -3.55, 0.00) to (3.13, -0.57, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764876.777570256] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764876.891320142] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.20, -3.45, 0.00) to (3.18, -0.47, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764877.091003245] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.25, -3.35, 0.00) to (3.23, -0.37, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764877.291071558] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.30, -3.25, 0.00) to (3.28, -0.27, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764877.491403954] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.30, -3.20, 0.00) to (3.28, -0.22, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764877.691187766] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.40, -3.10, 0.00) to (3.38, -0.12, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764877.890942078] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.40, -3.00, 0.00) to (3.38, -0.02, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764878.077565911] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764878.091405058] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.45, -2.90, 0.00) to (3.43, 0.08, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764878.291441454] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.50, -2.80, 0.00) to (3.48, 0.18, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764878.491168475] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.55, -2.75, 0.00) to (3.53, 0.23, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764878.692443082] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.55, -2.70, 0.00) to (3.53, 0.28, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764878.778372800] [controller_server]: Reached the goal!
[component_container_isolated-16] [WARN] [1783764878.891290102] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.60, -2.65, 0.00) to (3.58, 0.33, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764879.091154040] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.65, -2.60, 0.00) to (3.63, 0.38, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764879.265303438] [bt_navigator]: Goal succeeded
[competition_master_stage2.py-17] [INFO] [1783764879.270448321] [competition_master_stage2]:
[competition_master_stage2.py-17] [INFO] [1783764879.273713701] [competition_master_stage2]: ============================================================
[competition_master_stage2.py-17] [INFO] [1783764879.276271830] [competition_master_stage2]: >>> [Stage 2] 任务完成！
[competition_master_stage2.py-17] [INFO] [1783764879.279197543] [competition_master_stage2]: >>> QR 原始数据: 11
[competition_master_stage2.py-17] [INFO] [1783764879.282853423] [competition_master_stage2]: >>> QR 方向: 顺时针 (通道巡航: CW=顺时针 奇数, CCW=逆时针 偶数)
[competition_master_stage2.py-17] [INFO] [1783764879.285850470] [competition_master_stage2]: >>> 已抵达通道入口，等待下阶段扩展
[component_container_isolated-16] [WARN] [1783764879.295294151] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.65, -2.50, 0.00) to (3.63, 0.48, 0.75). The costmap cannot raytrace for it.
[competition_master_stage2.py-17] [INFO] [1783764879.305987501] [competition_master_stage2]: ============================================================
[component_container_isolated-16] [WARN] [1783764879.491220875] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.45, 0.00) to (3.68, 0.53, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764879.691238564] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764879.891277336] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764880.091481191] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764880.291310089] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764880.492053862] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764880.691581217] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764880.891877157] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764881.091142970] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764881.291190493] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764881.491190974] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764881.691147747] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764881.891609438] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764882.091050169] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764882.291095234] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764882.491194758] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764882.691079323] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764882.891241763] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764883.091233037] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764883.291032811] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764883.492453837] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764883.691134776] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764883.891301550] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764884.091102283] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764884.291036974] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764884.491052707] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764884.691210232] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764884.891650632] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764885.091150615] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764885.291209640] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764885.491353207] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764885.691031065] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764885.891424633] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764886.091063241] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764886.291104059] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764886.492018919] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[imu_madgwick_filter.py-6] [INFO] [1783764886.524851221] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2833 q_w=0.9558 angle=34.2deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783764886.590638617] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1199 q_w=0.7910 angle=75.4deg beta=0.0330
[component_container_isolated-16] [WARN] [1783764886.691188610] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764886.891200178] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764887.091181829] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764887.291102105] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764887.491238840] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764887.691498200] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764887.891131768] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764888.091115002] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764888.291414863] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764888.491307390] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764888.691332209] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764888.891351069] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764889.091333596] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764889.294745379] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764889.491071859] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764889.691037469] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764889.891783623] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764890.091312817] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764890.291181136] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764890.491351873] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764890.691451443] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764890.891309929] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764891.091262915] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764891.291074193] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764891.493504059] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764891.691172251] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764891.891199529] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764892.091619559] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764892.291167837] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764892.491415116] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764892.691368062] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764892.891315008] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764893.091310620] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764893.291965151] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764893.490999429] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764893.691383126] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764893.891164239] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764894.091631311] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764894.291331757] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764894.491045829] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764894.691032234] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764894.892010682] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764895.091093336] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764895.291555951] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764895.491174564] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764895.691101886] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764895.891087875] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764896.091589449] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764896.292557690] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764896.491185261] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[imu_madgwick_filter.py-6] [INFO] [1783764896.525137815] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3329 q_w=0.9560 angle=34.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783764896.592012090] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1399 q_w=0.7546 angle=82.0deg beta=0.0330
[component_container_isolated-16] [WARN] [1783764896.691294500] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764896.891173406] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764897.092679274] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764897.291487220] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764897.491363293] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764897.691348158] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764897.892110150] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764898.091197638] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764898.291544338] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764898.491194703] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764898.691676569] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764898.892644770] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764899.091841426] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764899.291927126] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764899.492114825] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764899.691628941] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764899.891176056] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764900.091579090] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764900.290974330] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764900.490924905] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764900.691206772] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764900.891179681] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764901.091865424] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764901.291008540] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764901.491086574] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764901.693204527] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764901.891286267] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764902.091448634] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764902.291053585] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764902.491089494] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764902.691510654] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764902.892463815] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764903.091520223] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764903.291386008] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764903.491265417] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764903.691909078] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764903.891402571] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764904.091177230] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764904.291399391] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764904.491329468] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764904.692299088] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764904.893025750] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764905.091303950] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764905.291106985] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764905.491115188] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764905.691670016] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764905.891081009] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764906.091021920] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764906.291115915] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764906.491641786] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[imu_madgwick_filter.py-6] [INFO] [1783764906.524586673] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3823 q_w=0.9561 angle=34.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783764906.588488237] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1599 q_w=0.7158 angle=88.6deg beta=0.0330
[component_container_isolated-16] [WARN] [1783764906.691203655] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764906.891378817] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764907.091252187] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764907.291282932] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764907.491193969] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764907.691158630] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764907.891139501] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764908.091469705] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764908.291346242] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764908.496025829] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764908.691071400] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764908.891324063] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764909.091821185] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764909.291133055] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764909.491157635] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764909.691131089] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764909.891006918] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764910.091243582] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764910.291092954] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764910.491092784] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764910.691309114] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764910.891216319] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764911.091090399] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764911.291481897] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764911.491372561] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764911.691124183] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764911.891238097] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764912.090968136] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764912.291853177] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764912.491364882] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764912.691199546] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764912.891233169] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764913.091077000] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764913.293841669] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764913.491188372] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764913.691566996] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764913.891386035] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764914.091526201] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764914.291286824] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764914.491118198] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764914.691287947] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764914.891385404] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764915.093831782] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764915.291141568] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764915.491201484] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764915.691377276] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764915.891036733] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764916.091288108] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764916.291180232] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764916.491037190] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[imu_madgwick_filter.py-6] [INFO] [1783764916.527251875] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4316 q_w=0.9562 angle=34.0deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783764916.587993810] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1799 q_w=0.6740 angle=95.2deg beta=0.0330
[component_container_isolated-16] [WARN] [1783764916.691271482] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764916.891008314] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764917.091416273] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764917.291214940] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764917.491314065] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764917.691089774] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764917.891088274] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764918.091187275] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764918.291013192] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764918.491002942] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764918.691077652] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764918.891997029] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764919.091625612] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764919.291039363] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764919.491426823] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764919.691071782] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764919.891265450] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764920.091176368] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764920.291352453] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764920.492558290] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764920.691072831] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764920.891142916] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764921.091061210] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764921.291053504] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764921.491142464] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764921.691181592] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764921.891047760] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764922.091102554] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764922.292371976] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764922.491064560] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764922.691263813] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764922.891498108] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764923.091039318] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764923.291151821] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764923.491182074] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764923.691002202] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764923.891056831] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764924.092587253] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764924.291076046] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764924.491116716] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764924.691054845] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764924.891177640] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764925.091034769] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764925.291144773] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764925.491101402] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764925.691601157] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764925.891134327] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764926.091269748] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764926.291797462] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764926.491161591] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[imu_madgwick_filter.py-6] [INFO] [1783764926.525592940] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4807 q_w=0.9564 angle=34.0deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783764926.589075089] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1999 q_w=0.6295 angle=102.0deg beta=0.0330
[component_container_isolated-16] [WARN] [1783764926.691143178] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764926.891156641] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764927.091120438] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764927.291051693] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764927.491246073] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764927.691899621] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764927.891426667] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764928.091550839] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764928.291373844] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764928.491155224] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764928.691337480] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764928.891692736] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764929.093623954] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764929.291126580] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764929.491302795] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764929.691410884] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764929.892143017] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764930.091363355] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764930.291062444] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764930.491125076] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764930.692980002] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764930.890940838] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764931.091107512] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764931.291192227] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764931.499673249] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764931.691282075] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764931.892888751] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764932.091769756] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764932.291326346] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764932.491395853] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764932.691089569] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764932.891201576] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764933.091261251] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764933.292353927] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764933.491033016] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764933.691279232] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764933.891094115] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764934.091207165] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764934.291425257] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764934.491300057] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764934.691082814] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764934.891532615] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764935.091069081] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764935.291369799] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764935.491311141] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764935.693845779] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764935.891248325] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764936.091240417] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764936.291632677] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764936.491569311] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[imu_madgwick_filter.py-6] [INFO] [1783764936.524905285] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5300 q_w=0.9566 angle=33.9deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783764936.588951895] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2199 q_w=0.5825 angle=108.7deg beta=0.0330
[component_container_isolated-16] [WARN] [1783764936.691214903] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764936.891546246] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764937.090920213] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764937.291064389] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764937.491474775] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764937.694892832] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764937.891388586] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764938.091230553] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764938.291097313] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764938.491589324] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764938.691179917] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764938.891192302] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764939.091883939] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764939.291145448] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764939.491242709] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764939.691542678] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764939.891127396] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764940.091274032] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764940.291154960] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764940.491181304] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764940.691202898] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764940.891487660] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764941.091457046] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764941.291083599] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764941.491380652] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764941.691333830] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764941.891073508] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764942.091563729] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764942.291347324] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764942.491161085] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764942.692017307] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764942.891267276] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764943.091648663] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764943.291532134] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764943.491103479] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764943.691614367] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764943.891054087] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764944.091103016] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764944.291023279] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764944.491232959] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764944.691079471] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764944.891114651] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764945.091302872] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764945.291215927] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764945.491501107] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764945.691173120] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764945.891288592] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764946.091157397] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764946.291549536] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764946.492280134] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[imu_madgwick_filter.py-6] [INFO] [1783764946.525393233] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5796 q_w=0.9567 angle=33.8deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783764946.588284217] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2399 q_w=0.5335 angle=115.5deg beta=0.0330
[component_container_isolated-16] [WARN] [1783764946.691049146] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764946.891008701] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764947.091017090] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764947.291456813] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764947.491194702] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764947.692954344] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764947.891129230] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764948.091185577] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764948.290988758] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764948.491202523] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764948.690991829] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764948.893371348] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764949.091098983] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764949.291107623] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764949.491339805] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[rviz2-18] Start navigate through poses
[rviz2-18] [INFO] [1783764949.513074218] [rviz_navigation_dialog_action_client]: NavigateThroughPoses will be called using the BT Navigator's default behavior tree.
[component_container_isolated-16] [INFO] [1783764949.514946430] [bt_navigator]: Begin navigating from current location through 7 poses to (1.15, 0.11)
[component_container_isolated-16] [WARN] [1783764949.691545029] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764949.716999990] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-16] [WARN] [1783764949.891975461] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764950.091972935] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764950.291545366] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.40, 0.00) to (3.68, 0.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764950.491384090] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.35, 0.00) to (3.68, 0.63, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764950.691117521] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.30, 0.00) to (3.68, 0.68, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764950.891322495] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.30, 0.00) to (3.68, 0.68, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764951.017378673] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764951.091484219] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.25, 0.00) to (3.68, 0.73, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764951.290990818] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.20, 0.00) to (3.68, 0.77, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764951.491116334] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.15, 0.00) to (3.68, 0.82, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764951.691274766] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.05, 0.00) to (3.68, 0.92, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764951.891272824] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -2.00, 0.00) to (3.68, 0.97, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764952.091704924] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, -1.95, 0.00) to (3.68, 1.02, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764952.291325690] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.75, -1.90, 0.00) to (3.73, 1.07, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764952.317365193] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764952.491647748] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.85, -1.85, 0.00) to (3.83, 1.12, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764952.691170013] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.90, -1.75, 0.00) to (3.88, 1.22, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764952.891330947] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.00, -1.70, 0.00) to (3.98, 1.27, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764953.091254380] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.10, -1.65, 0.00) to (4.08, 1.32, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764953.291477438] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.15, -1.60, 0.00) to (4.13, 1.38, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764953.491004454] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.25, -1.50, 0.00) to (4.23, 1.48, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764953.617370592] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764953.691179763] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.35, -1.45, 0.00) to (4.33, 1.53, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764953.892256115] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.40, -1.40, 0.00) to (4.38, 1.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764954.091180671] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.50, -1.35, 0.00) to (4.48, 1.63, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764954.291872523] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.55, -1.25, 0.00) to (4.53, 1.73, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764954.491402206] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.65, -1.20, 0.00) to (4.63, 1.78, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764954.691346723] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.75, -1.15, 0.00) to (4.73, 1.83, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764954.891325865] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.80, -1.10, 0.00) to (4.78, 1.88, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764954.917355119] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764955.091440216] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.90, -1.05, 0.00) to (4.88, 1.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764955.293027611] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.00, -1.00, 0.00) to (4.98, 1.98, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764955.491302709] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.05, -0.95, 0.00) to (5.03, 2.03, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764955.693966856] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.15, -0.95, 0.00) to (5.13, 2.03, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764955.892549496] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.25, -0.90, 0.00) to (5.23, 2.08, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764956.091654846] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.30, -0.85, 0.00) to (5.28, 2.13, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764956.217378441] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764956.291071737] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.40, -0.80, 0.00) to (5.38, 2.18, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764956.491024880] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.50, -0.75, 0.00) to (5.48, 2.23, 0.75). The costmap cannot raytrace for it.
[imu_madgwick_filter.py-6] [INFO] [1783764956.524624898] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=6289 q_w=0.9274 angle=43.9deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783764956.587576467] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2599 q_w=0.9315 angle=42.7deg beta=0.0330
[component_container_isolated-16] [WARN] [1783764956.691768608] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.55, -0.70, 0.00) to (5.53, 2.28, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764956.891333750] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.65, -0.65, 0.00) to (5.63, 2.33, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764957.091117601] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.65, -0.55, 0.00) to (5.63, 2.43, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764957.291194828] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.70, -0.50, 0.00) to (5.68, 2.48, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764957.491163680] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.70, -0.40, 0.00) to (5.68, 2.58, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764957.517380059] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764957.691060156] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.70, -0.35, 0.00) to (5.68, 2.63, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764957.891133883] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.70, -0.25, 0.00) to (5.68, 2.73, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764958.091811736] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.70, -0.20, 0.00) to (5.68, 2.78, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764958.291769963] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.70, -0.15, 0.00) to (5.68, 2.83, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764958.490981939] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.70, -0.15, 0.00) to (5.68, 2.83, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764958.691198749] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.70, -0.10, 0.00) to (5.68, 2.88, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764958.817383972] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764958.891546852] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.70, -0.10, 0.00) to (5.68, 2.88, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764959.091342162] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.70, -0.10, 0.00) to (5.68, 2.88, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764959.291212806] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.70, -0.15, 0.00) to (5.68, 2.83, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764959.491340659] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.70, -0.15, 0.00) to (5.68, 2.83, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764959.691226345] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.70, -0.15, 0.00) to (5.68, 2.83, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764959.891056697] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.70, -0.15, 0.00) to (5.68, 2.83, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764960.091151425] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.70, -0.15, 0.00) to (5.68, 2.83, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764960.117363263] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764960.291094861] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.70, -0.10, 0.00) to (5.68, 2.88, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764960.491012297] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.65, -0.05, 0.00) to (5.63, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764960.690989025] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.60, 0.00, 0.00) to (5.58, 2.98, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764960.891058336] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.50, 0.05, 0.00) to (5.48, 3.03, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764961.092875068] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.45, 0.10, 0.00) to (5.43, 3.08, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764961.291004376] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.35, 0.10, 0.00) to (5.33, 3.08, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764961.417364808] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764961.491213855] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.25, 0.10, 0.00) to (5.23, 3.08, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764961.692009918] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.15, 0.10, 0.00) to (5.13, 3.08, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764961.891030686] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (2.05, 0.10, 0.00) to (5.03, 3.08, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764962.091139207] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.95, 0.10, 0.00) to (4.93, 3.08, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764962.291216060] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.85, 0.05, 0.00) to (4.83, 3.03, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764962.491089372] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.75, 0.00, 0.00) to (4.73, 2.98, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764962.691130560] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.65, -0.05, 0.00) to (4.63, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764962.717362439] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764962.891040246] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.60, -0.05, 0.00) to (4.58, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764963.092078311] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.55, -0.05, 0.00) to (4.53, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764963.291063205] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.55, -0.05, 0.00) to (4.53, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764963.491213226] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.55, -0.05, 0.00) to (4.53, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764963.691145413] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.55, -0.05, 0.00) to (4.53, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764963.891077809] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.60, -0.05, 0.00) to (4.58, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764964.090959038] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.65, -0.05, 0.00) to (4.63, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764964.117358126] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764964.291034643] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.70, -0.05, 0.00) to (4.68, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764964.491013122] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.75, -0.05, 0.00) to (4.73, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764964.691335477] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.80, -0.05, 0.00) to (4.78, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764964.890985748] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.80, -0.05, 0.00) to (4.78, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764965.090974728] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.80, -0.05, 0.00) to (4.78, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764965.291105041] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.80, -0.05, 0.00) to (4.78, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764965.317385963] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764965.491219063] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.75, -0.05, 0.00) to (4.73, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764965.691123876] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.70, -0.05, 0.00) to (4.68, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764965.891187023] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.60, 0.00, 0.00) to (4.58, 2.98, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764966.090995211] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.50, 0.00, 0.00) to (4.48, 2.98, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764966.295273366] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.40, 0.05, 0.00) to (4.38, 3.03, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764966.491102755] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.30, 0.10, 0.00) to (4.28, 3.08, 0.75). The costmap cannot raytrace for it.
[imu_madgwick_filter.py-6] [INFO] [1783764966.525297774] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=6783 q_w=0.7956 angle=74.6deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783764966.588697262] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2797 q_w=0.1058 angle=167.9deg beta=0.0330
[component_container_isolated-16] [WARN] [1783764966.691832695] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.20, 0.15, 0.00) to (4.18, 3.13, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764966.717370491] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764966.891196425] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.10, 0.15, 0.00) to (4.08, 3.13, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764967.091112822] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (1.00, 0.15, 0.00) to (3.98, 3.13, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764967.291055469] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.90, 0.15, 0.00) to (3.88, 3.13, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764967.491082033] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.80, 0.15, 0.00) to (3.78, 3.13, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764967.691089347] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.70, 0.10, 0.00) to (3.68, 3.08, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764967.891329870] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.60, 0.10, 0.00) to (3.58, 3.08, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764967.917359125] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [WARN] [1783764968.091334059] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.50, 0.05, 0.00) to (3.48, 3.03, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764968.291783791] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.40, 0.00, 0.00) to (3.38, 2.98, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764968.491401147] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.30, 0.00, 0.00) to (3.28, 2.98, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764968.690901794] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.25, 0.00, 0.00) to (3.23, 2.98, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [WARN] [1783764968.891137109] [local_costmap.local_costmap]: Sensor origin at (0.13, 0.05 0.12) is out of map bounds (0.15, -0.05, 0.00) to (3.13, 2.93, 0.75). The costmap cannot raytrace for it.
[component_container_isolated-16] [INFO] [1783764969.217349315] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [INFO] [1783764970.517382259] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [INFO] [1783764971.817362456] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [INFO] [1783764973.117398573] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [INFO] [1783764974.417362277] [controller_server]: Passing new path to controller.
[component_container_isolated-16] [INFO] [1783764974.973037940] [controller_server]: Reached the goal!
[component_container_isolated-16] [INFO] [1783764975.416160319] [bt_navigator]: Goal succeeded
[imu_madgwick_filter.py-6] [INFO] [1783764976.526145645] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=7277 q_w=-0.7962 angle=285.5deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783764976.588307798] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2995 q_w=-0.9722 angle=332.9deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1783764986.529237339] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=7770 q_w=-0.7963 angle=285.6deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783764986.588392113] [imu_madgwick_filter]: [imu_madgwick ->] msgs=3195 q_w=-0.9562 angle=325.9deg beta=0.0330
^C[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[rviz2-18] [INFO] [1783764989.978474113] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [lslidar_driver_node-2]: process has died [pid 11757, exit code -6, cmd '/userdata/dev_ws/install/lslidar_driver/lib/lslidar_driver/lslidar_driver_node --ros-args -r __node:=lslidar_driver_node --params-file /userdata/dev_ws/install/lslidar_driver/share/lslidar_driver/params/lsx10.yaml'].
[ERROR] [origincar_base_node-1]: process has died [pid 11755, exit code -6, cmd '/userdata/dev_ws/install/origincar_base/lib/origincar_base/origincar_base_node --ros-args --params-file /tmp/launch_params_yqvui107 --params-file /tmp/launch_params_s4geb8qa'].
[INFO] [robot_state_publisher-3]: process has finished cleanly [pid 11759]
[INFO] [costmap_filter_info_server-14]: process has finished cleanly [pid 11896]
[ERROR] [rviz2-18]: process has died [pid 12064, exit code -11, cmd '/opt/ros/humble/lib/rviz2/rviz2 -d /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/rviz/nav.rviz --ros-args -r __node:=rviz2'].
[INFO] [static_transform_publisher-8]: process has finished cleanly [pid 11807]
[INFO] [map_server-13]: process has finished cleanly [pid 11894]
[INFO] [lifecycle_manager-15]: process has finished cleanly [pid 11898]
[aurora930_node-9] [INFO] [1783764989.978584280] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[INFO] [ekf_node-7]: process has finished cleanly [pid 11767]
[ekf_node-7] [INFO] [1783764989.978545988] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-13] [INFO] [1783764989.978707780] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-13] [INFO] [1783764989.978925738] [keepout_mask_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_mask_server)
[map_server-13] [INFO] [1783764989.979211364] [keepout_mask_server]: Deactivating
[map_server-13] [INFO] [1783764989.979300322] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[static_transform_publisher-8] [INFO] [1783764989.978718988] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-14] [INFO] [1783764989.979055197] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-14] [INFO] [1783764989.979233072] [keepout_filter_info_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_filter_info_server)
[costmap_filter_info_server-14] [INFO] [1783764989.979461614] [keepout_filter_info_server]: Deactivating
[costmap_filter_info_server-14] [INFO] [1783764989.979545073] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-14] [INFO] [1783764990.010448338] [keepout_filter_info_server]: Cleaning up
[costmap_filter_info_server-14] [INFO] [1783764990.010694171] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-14] [INFO] [1783764990.102054463] [keepout_filter_info_server]: Destroying
[robot_state_publisher-3] [INFO] [1783764989.979719282] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-16] [INFO] [1783764989.980024490] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-16] [INFO] [1783764989.980193657] [lifecycle_manager_navigation]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_navigation)
[component_container_isolated-16] [INFO] [1783764989.980453575] [lifecycle_manager_navigation]: Terminating bond timer...
[component_container_isolated-16] [INFO] [1783764990.434027068] [local_costmap.local_costmap]: Message Filter dropping message: frame 'laser_link' at time 1783764989.932 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-16] [INFO] [1783764990.467910505] [velocity_smoother]: Running Nav2 LifecycleNode rcl preshutdown (velocity_smoother)
[component_container_isolated-16] [INFO] [1783764990.468310756] [velocity_smoother]: Deactivating
[component_container_isolated-16] [INFO] [1783764990.468435798] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764990.478964067] [velocity_smoother]: Cleaning up
[component_container_isolated-16] [INFO] [1783764990.479283901] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764990.479415943] [bt_navigator]: Running Nav2 LifecycleNode rcl preshutdown (bt_navigator)
[component_container_isolated-16] [INFO] [1783764990.479564860] [bt_navigator]: Deactivating
[component_container_isolated-16] [INFO] [1783764990.479721068] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764990.490353838] [bt_navigator]: Cleaning up
[component_container_isolated-16] [INFO] [1783764991.053463948] [bt_navigator]: Completed Cleaning up
[component_container_isolated-16] [INFO] [1783764991.053773615] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764991.053865740] [behavior_server]: Running Nav2 LifecycleNode rcl preshutdown (behavior_server)
[component_container_isolated-16] [INFO] [1783764991.053991240] [behavior_server]: Deactivating
[component_container_isolated-16] [INFO] [1783764991.054146365] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764991.064765218] [behavior_server]: Cleaning up
[component_container_isolated-16] [INFO] [1783764991.100428575] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764991.100666200] [lifecycle_manager_localization]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_localization)
[component_container_isolated-16] [INFO] [1783764991.100739992] [lifecycle_manager_localization]: Terminating bond timer...
[component_container_isolated-16] [INFO] [1783764991.159911142] [planner_server]: Running Nav2 LifecycleNode rcl preshutdown (planner_server)
[component_container_isolated-16] [INFO] [1783764991.160170726] [planner_server]: Deactivating
[component_container_isolated-16] [INFO] [1783764991.160435726] [global_costmap.global_costmap]: Deactivating
[origincar_base_node-1] [INFO] [1783764989.980883409] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1783764989.983015871] [origincar_base]: Stop command sent to STM32 on shutdown.
[origincar_base_node-1] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[origincar_base_node-1] terminate called after throwing an instance of 'rclcpp::exceptions::RCLError'
[origincar_base_node-1]   what():  failed to create guard condition: the given context is not valid, either rcl_init() was not called or rcl_shutdown() was called., at ./src/rcl/guard_condition.c:67
[lifecycle_manager-15] [INFO] [1783764989.993655515] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-15] [INFO] [1783764989.993958558] [lifecycle_manager_keepout]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_keepout)
[lifecycle_manager-15] [INFO] [1783764989.994129766] [lifecycle_manager_keepout]: Terminating bond timer...
[lifecycle_manager-15] [INFO] [1783764990.234996330] [lifecycle_manager_keepout]: Destroying lifecycle_manager_keepout
[map_server-13] [INFO] [1783764990.000645695] [keepout_mask_server]: Cleaning up
[map_server-13] [INFO] [1783764990.000956029] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[map_server-13] [INFO] [1783764990.086488435] [keepout_mask_server]: Destroying
[aurora930_node-9] I0711 18:16:30.022284 11809 ros2_node.cc:90] process quit succeed
[aurora930_node-9] I0711 18:16:30.022466 11809 aurora900_ros2_device.cc:83] begin stop()
[aurora930_node-9] I0711 18:16:30.057304 11809 aurora900_ros2_device.cc:103] stop stream
[aurora930_node-9] 2026-07-11 18:16:30.134 ( 164.937s) [        83974020]      aurora900_impl.cc:648   INFO| ir_stream_count_=0, rgb_stream_count_=0, depth_stream_count_=0
[aurora930_node-9] 2026-07-11 18:16:30.135 ( 164.937s) [        83974020]      aurora900_impl.cc:649   INFO| mask=7
[aurora930_node-9] I0711 18:16:30.352296 11809 aurora900_ros2_device.cc:105] destroy stream
[aurora930_node-9] I0711 18:16:30.352612 11809 aurora900_ros2_device.cc:110] close glog
[aurora930_node-9] WARNING: Logging before InitGoogleLogging() is written to STDERR
[aurora930_node-9] I0711 18:16:30.354707 11809 ros2_device.cc:113] close device...
[aurora930_node-9] 2026-07-11 18:16:30.852 ( 165.655s) [        4F7E57E0]         cmd_backend.cc:40    INFO| RunBlocking is end!!!
[aurora930_node-9] 2026-07-11 18:16:31.053 ( 165.856s) [        83974020]deptrum_camera_vendor.c:121   INFO| device is close.
[aurora930_node-9] I0711 18:16:31.055336 11809 ros2_device.cc:116] quit succeed
[bmi088_iio_bridge.py-5] Traceback (most recent call last):
[bmi088_iio_bridge.py-5]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/bmi088_iio_bridge.py", line 487, in <module>
[bmi088_iio_bridge.py-5]     main()
[bmi088_iio_bridge.py-5]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/bmi088_iio_bridge.py", line 483, in main
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
[vision_ai_node-12]   File "/userdata/dev_ws/install/racing_vision_ai/lib/python3.10/site-packages/racing_vision_ai/vision_ai_node.py", line 226, in main
[vision_ai_node-12]     rclpy.shutdown()
[vision_ai_node-12]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 130, in shutdown
[vision_ai_node-12]     _shutdown(context=context)
[vision_ai_node-12]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/utilities.py", line 58, in shutdown
[vision_ai_node-12]     return context.shutdown()
[vision_ai_node-12]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/context.py", line 102, in shutdown
[vision_ai_node-12]     self.__context.shutdown()
[vision_ai_node-12] rclpy._rclpy_pybind11.RCLError: failed to shutdown: rcl_shutdown already called on the given context, at ./src/rcl/init.c:241
[INFO] [imu_madgwick_filter.py-4]: process has finished cleanly [pid 11761]
[INFO] [imu_madgwick_filter.py-6]: process has finished cleanly [pid 11765]
[INFO] [competition_master_stage2.py-17]: process has finished cleanly [pid 12062]
[component_container_isolated-16] [INFO] [1783764991.950159042] [planner_server]: Deactivating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-16] [INFO] [1783764991.950475543] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[ERROR] [bmi088_iio_bridge.py-5]: process has died [pid 11763, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/bmi088_iio_bridge.py --ros-args -r __node:=bmi088_iio_bridge --params-file /tmp/launch_params_ut6g8eru'].
[component_container_isolated-16] [INFO] [1783764991.960954687] [planner_server]: Cleaning up
[component_container_isolated-16] [INFO] [1783764991.981206516] [global_costmap.global_costmap]: Cleaning up
[component_container_isolated-16] [INFO] [1783764991.994583540] [planner_server]: Cleaning up plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-16] [INFO] [1783764991.995717375] [planner_server]: Destroying plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-16] [INFO] [1783764992.019123127] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764992.019304544] [amcl]: Running Nav2 LifecycleNode rcl preshutdown (amcl)
[component_container_isolated-16] [INFO] [1783764992.019455210] [amcl]: Deactivating
[component_container_isolated-16] [INFO] [1783764992.019617002] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764992.030023896] [amcl]: Cleaning up
[component_container_isolated-16] [INFO] [1783764992.040979041] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764992.041145000] [map_server]: Running Nav2 LifecycleNode rcl preshutdown (map_server)
[component_container_isolated-16] [INFO] [1783764992.041311917] [map_server]: Deactivating
[component_container_isolated-16] [INFO] [1783764992.041489209] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764992.051891395] [map_server]: Cleaning up
[component_container_isolated-16] [INFO] [1783764992.052120270] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764992.052189979] [waypoint_follower]: Running Nav2 LifecycleNode rcl preshutdown (waypoint_follower)
[component_container_isolated-16] [INFO] [1783764992.052303062] [waypoint_follower]: Deactivating
[component_container_isolated-16] [INFO] [1783764992.052455854] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764992.062935873] [waypoint_follower]: Cleaning up
[ERROR] [vision_ai_node-12]: process has died [pid 11815, exit code 1, cmd '/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node --ros-args -r __node:=vision_ai_node'].
[component_container_isolated-16] [INFO] [1783764992.073729643] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764992.073884685] [smoother_server]: Running Nav2 LifecycleNode rcl preshutdown (smoother_server)
[component_container_isolated-16] [INFO] [1783764992.074013143] [smoother_server]: Deactivating
[component_container_isolated-16] [INFO] [1783764992.074077894] [smoother_server]: Deactivating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-16] [INFO] [1783764992.074228061] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764992.084591746] [smoother_server]: Cleaning up
[component_container_isolated-16] [INFO] [1783764992.084714830] [smoother_server]: Cleaning up smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-16] [INFO] [1783764992.100587067] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764992.100746401] [controller_server]: Running Nav2 LifecycleNode rcl preshutdown (controller_server)
[component_container_isolated-16] [INFO] [1783764992.100954318] [controller_server]: Deactivating
[component_container_isolated-16] [INFO] [1783764992.101054693] [controller_server]: Deactivating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-16] [INFO] [1783764992.101321527] [local_costmap.local_costmap]: Deactivating
[INFO] [aurora930_node-9]: process has finished cleanly [pid 11809]
[component_container_isolated-16] [INFO] [1783764992.289348329] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[component_container_isolated-16] [INFO] [1783764992.300122723] [controller_server]: Cleaning up
[component_container_isolated-16] [INFO] [1783764992.300429849] [controller_server]: Cleaning up controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-16] [INFO] [1783764992.301018933] [local_costmap.local_costmap]: Cleaning up
[component_container_isolated-16] [INFO] [1783764993.349294099] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[ERROR] [component_container_isolated-16]: process[component_container_isolated-16] failed to terminate '5' seconds after receiving 'SIGINT', escalating to 'SIGTERM'
[INFO] [component_container_isolated-16]: sending signal 'SIGTERM' to process[component_container_isolated-16]
[component_container_isolated-16] [INFO] [1783764996.339365657] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [component_container_isolated-16]: process[component_container_isolated-16] failed to terminate '10.0' seconds after receiving 'SIGTERM', escalating to 'SIGKILL'
[INFO] [component_container_isolated-16]: sending signal 'SIGKILL' to process[component_container_isolated-16]
[ERROR] [component_container_isolated-16]: process has died [pid 12060, exit code -9, cmd '/opt/ros/humble/lib/rclcpp_components/component_container_isolated --ros-args --log-level info --ros-args -r __node:=nav2_container --params-file /tmp/launch_params_rgf5euqx --params-file /tmp/launch_params_188perpl -r /tf:=tf -r /tf_static:=tf_static'].
root@ubuntu:/userdata/dev_ws#
