root@ubuntu:/userdata/dev_ws# ros2 launch origincar_bringup stage3_bringup.launch.py
[INFO] [launch]: All log files can be found below /root/.ros/log/2026-07-06-16-43-34-287471-ubuntu-6944
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [origincar_base_node-1]: process started with pid [6957]
[INFO] [lslidar_driver_node-2]: process started with pid [6959]
[INFO] [robot_state_publisher-3]: process started with pid [6961]
[INFO] [imu_madgwick_filter.py-4]: process started with pid [6963]
[INFO] [bmi088_iio_bridge.py-5]: process started with pid [6965]
[INFO] [imu_madgwick_filter.py-6]: process started with pid [6967]
[INFO] [ekf_node-7]: process started with pid [6969]
[INFO] [static_transform_publisher-8]: process started with pid [7017]
[INFO] [aurora930_node-9]: process started with pid [7019]
[INFO] [qr_decoder-10]: process started with pid [7021]
[INFO] [qr_decision.py-11]: process started with pid [7023]
[INFO] [vision_ai_node-12]: process started with pid [7025]
[INFO] [hobot_codec_republish-13]: process started with pid [7027]
[origincar_base_node-1] [INFO] [1783327414.960439586] [origincar_base]: origincar_base serial port opened
[lslidar_driver_node-2] [INFO] [1783327415.008438241] [lslidar_driver_node]: Lidar is N10
[lslidar_driver_node-2] [INFO] [1783327415.019758333] [lslidar_driver_node]: Initialised lslidar without error
[lslidar_driver_node-2] [INFO] [1783327415.019939294] [lslidar_driver_node]: Successfully initialize driver...
[robot_state_publisher-3] [WARN] [1783327414.963283745] [robot_state_publisher]: No robot_description parameter, but command-line argument available.  Assuming argument is name of URDF file.  This backwards compatibility fallback will be removed in the future.
[robot_state_publisher-3] [INFO] [1783327414.986475480] [robot_state_publisher]: got segment base_footprint
[robot_state_publisher-3] [INFO] [1783327414.986680399] [robot_state_publisher]: got segment base_link
[robot_state_publisher-3] [INFO] [1783327414.986772691] [robot_state_publisher]: got segment gyro_link
[robot_state_publisher-3] [INFO] [1783327414.986837317] [robot_state_publisher]: got segment laser_link
[ekf_node-7] Both imu1_differential and imu1_relative were set to true. Using differential mode.
[static_transform_publisher-8] [INFO] [1783327415.171152671] [depth_camera_tf]: Spinning until stopped - publishing transform
[static_transform_publisher-8] translation: ('0.140000', '0.000000', '0.050000')
[static_transform_publisher-8] rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
[static_transform_publisher-8] from 'base_link' to 'depth_camera_link'
[hobot_codec_republish-13] [WARN] [1783327415.281067557] [vlm_jpeg_encoder]: Parameters:
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
[hobot_codec_republish-13] [WARN] [1783327415.320330523] [HobotCodecImpl]: platform x5
[aurora930_node-9] W0706 16:43:35.803680  7019 ros2_node.cc:35] hello aurora 900/930
[qr_decoder-10] [INFO] [1783327415.832061551] [qr_decoder_zbar]: QR decoder (ZBar) started: rgb=/aurora/rgb/image_raw, depth=/aurora/depth/image_raw, filter=on, range=[50, 4000]mm, min_qr_len=1, intrinsics: fx=421.3 fy=422.3 cx=320.3 cy=197.0
[aurora930_node-9] 2026-07-06 16:43:35.897 (   0.254s) [        A8FA4020] device_manager_impl.cc:89    INFO| hotplug has registed by user
[aurora930_node-9] I0706 16:43:35.936731  7019 aurora900_ros2_device.cc:153] BOOT_ORDER_1::Found 1 deptrum device
[aurora930_node-9] I0706 16:43:35.937431  7019 aurora900_ros2_device.cc:162] BOOT_ORDER_1::No serial number provided: picking first device
[aurora930_node-9] 2026-07-06 16:43:35.937 (   0.294s) [        A8FA4020] device_manager_impl.cc:318   INFO| Device information:
[aurora930_node-9]      ir_pid:0x1930, rgb_pid:0x0
[aurora930_node-9]      serial number:HY400529001015314G00248
[aurora930_node-9] I0706 16:43:35.938475  7019 aurora900_ros2_device.cc:206] BOOT_ORDER_1::0:device start opening
[aurora930_node-9] 2026-07-06 16:43:35.941 (   0.297s) [        A8FA4020]   custom_usb_device.cc:101   INFO| bulk in endpoint addr:129
[aurora930_node-9] 2026-07-06 16:43:35.942 (   0.298s) [        A8FA4020]   custom_usb_device.cc:98    INFO| bulk out endpoint addr:2
[aurora930_node-9] 2026-07-06 16:43:35.947 (   0.304s) [        A8FA4020]deptrum_camera_aurora93:53    INFO| doe_broken:0 ito_support:1 crash_count:0 wdt_count:0 hard_reset_count:2 heart_boot_count:0 boot_total:131 last_crash_time:N
[aurora930_node-9] I0706 16:43:35.947548  7019 aurora900_ros2_device.cc:247] device supported frame_mode:
[aurora930_node-9] I0706 16:43:35.947659  7019 aurora900_ros2_device.cc:252] [0]:ir_mode:=13 kRes320x200Ir8Bit rgb_mode:=31 kRes320x200RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0706 16:43:35.947712  7019 aurora900_ros2_device.cc:252] [1]:ir_mode:=17 kRes480x300Depth16Bit rgb_mode:=32 kRes480x300RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0706 16:43:35.947772  7019 aurora900_ros2_device.cc:252] [2]:ir_mode:=20 kRes640x400Ir8Bit rgb_mode:=33 kRes640x400RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0706 16:43:35.947815  7019 aurora900_ros2_device.cc:266] current set mode ir_mode:20:kRes640x400Ir8Bit,rgb_mode:33:kRes640x400RgbYuv
[aurora930_node-9] device_count==========1
[INFO] [map_server-14]: process started with pid [7117]
[INFO] [costmap_filter_info_server-15]: process started with pid [7119]
[INFO] [lifecycle_manager-16]: process started with pid [7127]
[costmap_filter_info_server-15] [INFO] [1783327416.279453763] [costmap_filter_info_server]: This is costmap filter info publisher
[lifecycle_manager-16] [INFO] [1783327416.335639678] [lifecycle_manager_keepout]: Creating
[lifecycle_manager-16] [INFO] [1783327416.363309588] [lifecycle_manager_keepout]: Creating and initializing lifecycle service clients
[costmap_filter_info_server-15] [INFO] [1783327416.464190906] [keepout_filter_info_server]:
[costmap_filter_info_server-15]         keepout_filter_info_server lifecycle node launched.
[costmap_filter_info_server-15]         Waiting on external lifecycle transitions to activate
[costmap_filter_info_server-15]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[aurora930_node-9] I0706 16:43:36.499135  7019 aurora900_ros2_device.cc:387] Switch Auto Exposure
[aurora930_node-9] 2026-07-06 16:43:36.561 (   0.917s) [        A8FA4020]      aurora900_impl.cc:1106  INFO| SetHeartbeat user set heartbeat enable: 0
[map_server-14] [INFO] [1783327416.570595539] [keepout_mask_server]:
[map_server-14]         keepout_mask_server lifecycle node launched.
[map_server-14]         Waiting on external lifecycle transitions to activate
[map_server-14]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[map_server-14] [INFO] [1783327416.571169796] [keepout_mask_server]: Creating
[lifecycle_manager-16] [INFO] [1783327416.654675200] [lifecycle_manager_keepout]: Starting managed nodes bringup...
[lifecycle_manager-16] [INFO] [1783327416.654946786] [lifecycle_manager_keepout]: Configuring keepout_mask_server
[map_server-14] [INFO] [1783327416.656561514] [keepout_mask_server]: Configuring
[map_server-14] [INFO] [1783327416.656854392] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.yaml
[map_server-14] [INFO] [1783327416.658036531] [map_io]: resolution: 0.05
[map_server-14] [INFO] [1783327416.658133782] [map_io]: origin[0]: -2.65
[map_server-14] [INFO] [1783327416.658163908] [map_io]: origin[1]: -4.5
[map_server-14] [INFO] [1783327416.658191158] [map_io]: origin[2]: 0
[map_server-14] [INFO] [1783327416.658219700] [map_io]: free_thresh: 0.5
[map_server-14] [INFO] [1783327416.658247867] [map_io]: occupied_thresh: 0.5
[map_server-14] [INFO] [1783327416.658286368] [map_io]: mode: scale
[map_server-14] [INFO] [1783327416.658315785] [map_io]: negate: 0
[map_server-14] [INFO] [1783327416.658987084] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm
[map_server-14] [INFO] [1783327416.676617168] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm: 163 X 141 map @ 0.05 m/cell
[bmi088_iio_bridge.py-5] [INFO] [1783327416.686674787] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1783327416.693914122] [bmi088_iio_bridge]:   DIAGNOSTIC: Scanning IIO devices under /sys/bus/iio/devices/
[bmi088_iio_bridge.py-5] [INFO] [1783327416.698327008] [bmi088_iio_bridge]:   Equivalent to: ls /sys/bus/iio/devices/*/name
[bmi088_iio_bridge.py-5] [INFO] [1783327416.701049707] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1783327416.707791661] [bmi088_iio_bridge]:   iio:device0/name = "34190000.adc"
[bmi088_iio_bridge.py-5] [INFO] [1783327416.710676862] [bmi088_iio_bridge]:   iio:device1/name = "bmi08x"
[lifecycle_manager-16] [INFO] [1783327416.712346298] [lifecycle_manager_keepout]: Configuring keepout_filter_info_server
[bmi088_iio_bridge.py-5] [INFO] [1783327416.713312268] [bmi088_iio_bridge]:   trigger0/name = "34190000.adc-dev0"
[costmap_filter_info_server-15] [INFO] [1783327416.713644522] [keepout_filter_info_server]: Configuring
[bmi088_iio_bridge.py-5] [INFO] [1783327416.716371513] [bmi088_iio_bridge]:   Total IIO devices found: 3
[bmi088_iio_bridge.py-5] [INFO] [1783327416.719067961] [bmi088_iio_bridge]:   BMI088 kernel module APPEARS LOADED: 1 BMI device(s) detected
[bmi088_iio_bridge.py-5] [INFO] [1783327416.721990246] [bmi088_iio_bridge]:   BMI device names: ['bmi08x']
[bmi088_iio_bridge.py-5] [INFO] [1783327416.727739230] [bmi088_iio_bridge]:   gyro:  /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_anglvel is_si=False scale_override=0.00053
[bmi088_iio_bridge.py-5] [INFO] [1783327416.731721152] [bmi088_iio_bridge]:   accel: /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_accel is_si=False scale_override=0.00341
[lifecycle_manager-16] [INFO] [1783327416.738855612] [lifecycle_manager_keepout]: Activating keepout_mask_server
[map_server-14] [INFO] [1783327416.741421184] [keepout_mask_server]: Activating
[map_server-14] [INFO] [1783327416.741803438] [keepout_mask_server]: Creating bond (keepout_mask_server) to lifecycle manager.
[imu_madgwick_filter.py-4] [INFO] [1783327416.855029235] [imu_madgwick_filter]: [imu_madgwick] init: beta=0.0330, gyro_noise=0.0010, accel_noise=0.050
[bmi088_iio_bridge.py-5] [INFO] [1783327416.861414061] [bmi088_iio_bridge]: BMI088 IIO Bridge 启动 @ 100Hz -> /imu_data  [OK]
[imu_madgwick_filter.py-4] [INFO] [1783327416.862344489] [imu_madgwick_filter]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[lifecycle_manager-16] [INFO] [1783327416.863978925] [lifecycle_manager_keepout]: Server keepout_mask_server connected with bond.
[lifecycle_manager-16] [INFO] [1783327416.864174760] [lifecycle_manager_keepout]: Activating keepout_filter_info_server
[costmap_filter_info_server-15] [INFO] [1783327416.865074896] [keepout_filter_info_server]: Activating
[costmap_filter_info_server-15] [INFO] [1783327416.865322024] [keepout_filter_info_server]: Creating bond (keepout_filter_info_server) to lifecycle manager.
[imu_madgwick_filter.py-4] [INFO] [1783327416.865375941] [imu_madgwick_filter]: [imu_madgwick] accel init: roll=0.3deg, pitch=-0.1deg
[lifecycle_manager-16] [INFO] [1783327416.981430147] [lifecycle_manager_keepout]: Server keepout_filter_info_server connected with bond.
[lifecycle_manager-16] [INFO] [1783327416.981607857] [lifecycle_manager_keepout]: Managed nodes are active
[lifecycle_manager-16] [INFO] [1783327416.981735609] [lifecycle_manager_keepout]: Creating bond timer...
[aurora930_node-9] I0706 16:43:37.002270  7019 aurora900_ros2_device.cc:304] BOOT_ORDER_1::Device information:
[aurora930_node-9] I0706 16:43:37.002434  7019 aurora900_ros2_device.cc:305]     sdk version: 1.1.22
[aurora930_node-9] I0706 16:43:37.002475  7019 aurora900_ros2_device.cc:306]     device name: Aurora 930
[aurora930_node-9] I0706 16:43:37.002502  7019 aurora900_ros2_device.cc:307]     serial number: HY400529001015314G00248
[aurora930_node-9] I0706 16:43:37.002529  7019 aurora900_ros2_device.cc:308]     firmware version: 1.7.2
[aurora930_node-9] I0706 16:43:37.002581  7019 camera_parameters.cc:134] BOOT_ORDER_1::Camera Parameters:
[aurora930_node-9] I0706 16:43:37.002610  7019 camera_parameters.cc:135] BOOT_ORDER_1::  Ir Intrinsics:
[aurora930_node-9] I0706 16:43:37.002637  7019 camera_parameters.cc:146]                 Resolution:
[aurora930_node-9] I0706 16:43:37.002662  7019 camera_parameters.cc:147]                         Rows:400
[aurora930_node-9] I0706 16:43:37.002688  7019 camera_parameters.cc:148]                         Cols:640
[aurora930_node-9] I0706 16:43:37.002713  7019 camera_parameters.cc:149]                 Intrinsics:
[aurora930_node-9] I0706 16:43:37.002738  7019 camera_parameters.cc:150]                         fx: 421.307
[aurora930_node-9] I0706 16:43:37.002841  7019 camera_parameters.cc:151]                         fy: 422.254
[aurora930_node-9] I0706 16:43:37.002876  7019 camera_parameters.cc:152]                         cx: 320.27
[aurora930_node-9] I0706 16:43:37.003146  7019 camera_parameters.cc:153]                         cy: 197.01
[aurora930_node-9] I0706 16:43:37.003187  7019 camera_parameters.cc:154]                         k1: 0.0606853
[aurora930_node-9] I0706 16:43:37.003221  7019 camera_parameters.cc:155]                         k2: -0.10961
[aurora930_node-9] I0706 16:43:37.003252  7019 camera_parameters.cc:156]                         p1: 0.00126689
[aurora930_node-9] I0706 16:43:37.003283  7019 camera_parameters.cc:157]                         p2: -0.00120539
[aurora930_node-9] I0706 16:43:37.003314  7019 camera_parameters.cc:158]                         k3: 0.0522281
[aurora930_node-9] I0706 16:43:37.003345  7019 camera_parameters.cc:138] BOOT_ORDER_1::  Rgb Intrinsics:
[aurora930_node-9] I0706 16:43:37.003373  7019 camera_parameters.cc:146]                 Resolution:
[aurora930_node-9] I0706 16:43:37.003398  7019 camera_parameters.cc:147]                         Rows:400
[aurora930_node-9] I0706 16:43:37.003423  7019 camera_parameters.cc:148]                         Cols:640
[aurora930_node-9] I0706 16:43:37.003448  7019 camera_parameters.cc:149]                 Intrinsics:
[aurora930_node-9] I0706 16:43:37.003473  7019 camera_parameters.cc:150]                         fx: 416.49
[aurora930_node-9] I0706 16:43:37.003504  7019 camera_parameters.cc:151]                         fy: 417.383
[aurora930_node-9] I0706 16:43:37.003536  7019 camera_parameters.cc:152]                         cx: 316.832
[aurora930_node-9] I0706 16:43:37.003568  7019 camera_parameters.cc:153]                         cy: 188.753
[aurora930_node-9] I0706 16:43:37.003599  7019 camera_parameters.cc:154]                         k1: 0.00611878
[aurora930_node-9] I0706 16:43:37.003666  7019 camera_parameters.cc:155]                         k2: -0.0490436
[aurora930_node-9] I0706 16:43:37.003700  7019 camera_parameters.cc:156]                         p1: 0.000399548
[aurora930_node-9] I0706 16:43:37.003732  7019 camera_parameters.cc:157]                         p2: 0.000563892
[aurora930_node-9] I0706 16:43:37.003763  7019 camera_parameters.cc:158]                         k3: 0.0308458
[aurora930_node-9] I0706 16:43:37.003794  7019 camera_parameters.cc:141] BOOT_ORDER_1::  Ir to Rgb Extrinsic:
[aurora930_node-9] I0706 16:43:37.003821  7019 camera_parameters.cc:162]                 Extrinsics:
[aurora930_node-9] I0706 16:43:37.003846  7019 camera_parameters.cc:163]                         Rotation[0]: 0.999973, 0.00724076, -0.00112023
[aurora930_node-9] I0706 16:43:37.003882  7019 camera_parameters.cc:165]                         Rotation[1]: -0.00724006, 0.999973, 0.000633162
[aurora930_node-9] I0706 16:43:37.003918  7019 camera_parameters.cc:167]                         Rotation[2]: 0.00112478, -0.000625033, 0.999999
[aurora930_node-9] I0706 16:43:37.004001  7019 camera_parameters.cc:169]                         Translation: -9.88662, 0.117748, 0.603513
[aurora930_node-9] 2026-07-06 16:43:37.004 (   1.361s) [        A8FA4020]      aurora900_impl.cc:578   INFO| stream_mask_:0, rgb_stream_count_:1
[imu_madgwick_filter.py-6] [INFO] [1783327417.022253212] [imu_madgwick_bmi088]: [imu_madgwick] init: beta=0.0030, gyro_noise=0.0002, accel_noise=0.010
[imu_madgwick_filter.py-6] [INFO] [1783327417.028445993] [imu_madgwick_bmi088]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-6] [INFO] [1783327417.031167942] [imu_madgwick_bmi088]: [imu_madgwick] accel init: roll=-2.0deg, pitch=-3.7deg
[qr_decision.py-11] [INFO] [1783327417.113024032] [qr_decision]: qr_decision started: cooldown=3.0s, awaiting /sign from qr_decoder
[hobot_codec_republish-13] [WARN] [1783327417.289047565] [HobotVenc]: init_pic_w_: 640, init_pic_h_: 400, alined_pic_w_: 640, alined_pic_h_: 400, aline_w_: 16, aline_h_: 16
[hobot_codec_republish-13] [WARN] [1783327420.340945852] [vlm_jpeg_encoder]: Sub imgRaw fps [8.78]
[hobot_codec_republish-13] [WARN] [1783327420.343303130] [vlm_jpeg_encoder]: Pub img fps [8.78]
[aurora930_node-9] 2026-07-06 16:43:37.327 (   1.683s) [        891D37E0]deptrum_camera_aurora93:407    ERR| recv first frame time is 1783327417327
[lslidar_driver_node-2] port = /dev/ttyACM1, baud_rate = 230400
[lslidar_driver_node-2] open_port /dev/ttyACM1 OK !
[INFO] [component_container_isolated-17]: process started with pid [7284]
[vision_ai_node-12] [INFO] [1783327420.078726082] [vision_ai_node]: Loaded config: /userdata/dev_ws/install/racing_vision_ai/share/racing_vision_ai/config/vision_ai_config.yaml
[vision_ai_node-12] [INFO] [1783327420.488705995] [vision_ai_node]: Volcengine Ark client initialized
[vision_ai_node-12] [INFO] [1783327420.506405076] [vision_ai_node]: Vision AI Node initialized (JPU JPEG mode)
[vision_ai_node-12] [INFO] [1783327420.509822075] [vision_ai_node]: Waiting for sign4return=9
[vision_ai_node-12] [INFO] [1783327420.512404397] [vision_ai_node]: Image topic: /aurora/rgb/image_jpeg
[bmi088_iio_bridge.py-5] [INFO] [1783327422.429868933] [bmi088_iio_bridge]:   gyro bias calibrated: (0.002889, 0.001993, -0.002918) rad/s
[INFO] [yolo_costmap_bridge.py-19]: process started with pid [7290]
[INFO] [competition_master_stage3.py-20]: process started with pid [7299]
[INFO] [racing_obstacle_detection_yolo-18]: process started with pid [7288]
[INFO] [speed_profile_node.py-21]: process started with pid [7301]
[INFO] [rviz2-22]: process started with pid [7303]
[component_container_isolated-17] [INFO] [1783327423.107254751] [nav2_container]: Load Library: /opt/ros/humble/lib/libcontroller_server_core.so
[component_container_isolated-17] [INFO] [1783327423.136748676] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-17] [INFO] [1783327423.142573326] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-17] [INFO] [1783327423.331336094] [controller_server]:
[component_container_isolated-17]       controller_server lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783327423.392667595] [controller_server]: Creating controller server
[component_container_isolated-17] [INFO] [1783327423.571974295] [local_costmap.local_costmap]:
[component_container_isolated-17]       local_costmap lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783327423.581768950] [local_costmap.local_costmap]: Creating Costmap
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/controller_server' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783327423.615055419] [nav2_container]: Load Library: /opt/ros/humble/lib/libmap_server_core.so
[component_container_isolated-17] [INFO] [1783327423.686904042] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::CostmapFilterInfoServer>
[component_container_isolated-17] [INFO] [1783327423.687107628] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapSaver>
[component_container_isolated-17] [INFO] [1783327423.687169545] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-17] [INFO] [1783327423.687220087] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-17] [INFO] [1783327423.765396867] [map_server]:
[component_container_isolated-17]       map_server lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783327423.765694787] [map_server]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/map_server' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783327423.773549878] [nav2_container]: Load Library: /opt/ros/humble/lib/libsmoother_server_core.so
[component_container_isolated-17] [INFO] [1783327423.785235888] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-17] [INFO] [1783327423.785447349] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-17] [INFO] [1783327423.910141250] [smoother_server]:
[component_container_isolated-17]       smoother_server lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783327423.940347100] [smoother_server]: Creating smoother server
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/smoother_server' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783327423.979892099] [nav2_container]: Load Library: /opt/ros/humble/lib/libamcl_core.so
[component_container_isolated-17] [INFO] [1783327423.992727998] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-17] [INFO] [1783327423.992935084] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[racing_obstacle_detection_yolo-18] [BPU_PLAT]BPU Platform Version(1.3.6)! soc info(x5)
[racing_obstacle_detection_yolo-18] [HBRT] set log level as 0. version = 3.15.55.0
[racing_obstacle_detection_yolo-18] [DNN] Runtime version = 1.24.5_(3.15.55 HBRT)
[component_container_isolated-17] [INFO] [1783327424.127072715] [amcl]:
[component_container_isolated-17]       amcl lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783327424.131564600] [amcl]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/amcl' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783327424.274465124] [nav2_container]: Load Library: /opt/ros/humble/lib/libplanner_server_core.so
[component_container_isolated-17] [INFO] [1783327424.286353844] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-17] [INFO] [1783327424.286635764] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-17] [INFO] [1783327424.422094535] [planner_server]:
[component_container_isolated-17]       planner_server lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783327424.443454115] [planner_server]: Creating
[racing_obstacle_detection_yolo-18] [A][DNN][packed_model.cpp:247][Model](2026-07-06,16:43:44.310.934) [HorizonRT] The model builder version = 1.24.3
[component_container_isolated-17] [INFO] [1783327424.568052302] [global_costmap.global_costmap]:
[component_container_isolated-17]       global_costmap lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783327424.571147172] [global_costmap.global_costmap]: Creating Costmap
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/planner_server' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783327424.625503965] [nav2_container]: Load Library: /opt/ros/humble/lib/libnav2_lifecycle_manager_core.so
[component_container_isolated-17] [INFO] [1783327424.631671328] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-17] [INFO] [1783327424.631884122] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-17] [INFO] [1783327424.830984336] [lifecycle_manager_localization]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_localization' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783327424.884391369] [lifecycle_manager_localization]: Creating and initializing lifecycle service clients
[component_container_isolated-17] [INFO] [1783327424.926036099] [nav2_container]: Load Library: /opt/ros/humble/lib/libbehavior_server_core.so
[component_container_isolated-17] [INFO] [1783327424.963825285] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-17] [INFO] [1783327424.964009787] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-17] [INFO] [1783327424.981225528] [lifecycle_manager_localization]: Starting managed nodes bringup...
[component_container_isolated-17] [INFO] [1783327424.987073095] [lifecycle_manager_localization]: Configuring map_server
[component_container_isolated-17] [INFO] [1783327424.988178566] [map_server]: Configuring
[component_container_isolated-17] [INFO] [1783327424.990057088] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.yaml
[component_container_isolated-17] [INFO] [1783327424.991236685] [map_io]: resolution: 0.05
[component_container_isolated-17] [INFO] [1783327424.991340019] [map_io]: origin[0]: -2.65
[component_container_isolated-17] [INFO] [1783327424.991375936] [map_io]: origin[1]: -4.5
[component_container_isolated-17] [INFO] [1783327424.991405853] [map_io]: origin[2]: 0
[component_container_isolated-17] [INFO] [1783327424.992852995] [map_io]: free_thresh: 0.25
[component_container_isolated-17] [INFO] [1783327424.992915162] [map_io]: occupied_thresh: 0.65
[component_container_isolated-17] [INFO] [1783327424.993000788] [map_io]: mode: trinary
[component_container_isolated-17] [INFO] [1783327424.993036706] [map_io]: negate: 0
[component_container_isolated-17] [INFO] [1783327424.993731297] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm
[component_container_isolated-17] [INFO] [1783327425.048673846] [behavior_server]:
[component_container_isolated-17]       behavior_server lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783327425.063547975] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm: 163 X 141 map @ 0.05 m/cell
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/behavior_server' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783327425.110061010] [lifecycle_manager_localization]: Configuring amcl
[component_container_isolated-17] [INFO] [1783327425.111528986] [amcl]: Configuring
[component_container_isolated-17] [INFO] [1783327425.112001408] [amcl]: initTransforms
[component_container_isolated-17] [INFO] [1783327425.121763728] [nav2_container]: Load Library: /opt/ros/humble/lib/libbt_navigator_core.so
[component_container_isolated-17] [INFO] [1783327425.193951934] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-17] [INFO] [1783327425.194144477] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-17] [INFO] [1783327425.314300776] [amcl]: initPubSub
[component_container_isolated-17] [INFO] [1783327425.355268872] [amcl]: Subscribed to map topic.
[hobot_codec_republish-13] [WARN] [1783327425.384293539] [vlm_jpeg_encoder]: Sub imgRaw fps [10.91]
[hobot_codec_republish-13] [WARN] [1783327425.388904468] [vlm_jpeg_encoder]: Pub img fps [10.90]
[component_container_isolated-17] [INFO] [1783327425.428863260] [lifecycle_manager_localization]: Activating map_server
[component_container_isolated-17] [INFO] [1783327425.430154692] [map_server]: Activating
[component_container_isolated-17] [INFO] [1783327425.430895325] [map_server]: Creating bond (map_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327425.433324645] [amcl]: Received a 163 X 141 map @ 0.050 m/pix
[component_container_isolated-17] [INFO] [1783327425.502698026] [bt_navigator]:
[component_container_isolated-17]       bt_navigator lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/bt_navigator' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783327425.503125240] [bt_navigator]: Creating
[component_container_isolated-17] [INFO] [1783327425.525027866] [nav2_container]: Load Library: /opt/ros/humble/lib/libwaypoint_follower_core.so
[component_container_isolated-17] [INFO] [1783327425.528910994] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-17] [INFO] [1783327425.529094788] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-17] [INFO] [1783327425.574359101] [lifecycle_manager_localization]: Server map_server connected with bond.
[component_container_isolated-17] [INFO] [1783327425.574553061] [lifecycle_manager_localization]: Activating amcl
[component_container_isolated-17] [INFO] [1783327425.576164288] [amcl]: Activating
[component_container_isolated-17] [INFO] [1783327425.576415083] [amcl]: initialPoseReceived
[component_container_isolated-17] [INFO] [1783327425.576903838] [amcl]: Setting pose (1783327425.576899): -1.985 -0.014 0.262
[component_container_isolated-17] [INFO] [1783327425.578846777] [amcl]: Creating bond (amcl) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327425.652968588] [amcl]: createLaserObject
[component_container_isolated-17] [INFO] [1783327425.680171526] [waypoint_follower]:
[component_container_isolated-17]       waypoint_follower lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783327425.690073056] [waypoint_follower]: Creating
[component_container_isolated-17] [INFO] [1783327425.704099093] [lifecycle_manager_localization]: Server amcl connected with bond.
[component_container_isolated-17] [INFO] [1783327425.704286637] [lifecycle_manager_localization]: Managed nodes are active
[component_container_isolated-17] [INFO] [1783327425.704402221] [lifecycle_manager_localization]: Creating bond timer...
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/waypoint_follower' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783327425.746923627] [nav2_container]: Load Library: /opt/ros/humble/lib/libvelocity_smoother_core.so
[component_container_isolated-17] [INFO] [1783327425.750881923] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-17] [INFO] [1783327425.751049633] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[speed_profile_node.py-21] [INFO] [1783327425.785742407] [speed_profile_node]: speed_profile_node started — v_max=0.50 v_min=0.15 beta=0.47 lambda=1.32 max_accel=1.01 max_decel=-1.57
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/velocity_smoother' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783327425.874579929] [velocity_smoother]:
[component_container_isolated-17]       velocity_smoother lifecycle node launched.
[component_container_isolated-17]       Waiting on external lifecycle transitions to activate
[component_container_isolated-17]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-17] [INFO] [1783327425.925056718] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-17] [INFO] [1783327425.925252261] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[racing_obstacle_detection_yolo-18] [WARN] [1783327425.925299387] [ObstacleDetectionNode]: input fps: 8.76, out fps: 8.80, infer time ms: 10, post process time ms: 14
[component_container_isolated-17] [INFO] [1783327426.052538474] [lifecycle_manager_navigation]: Creating
[component_container_isolated-17] [INFO] [1783327426.093892073] [lifecycle_manager_navigation]: Creating and initializing lifecycle service clients
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_navigation' in container '/nav2_container'
[component_container_isolated-17] [INFO] [1783327426.272271035] [lifecycle_manager_navigation]: Starting managed nodes bringup...
[component_container_isolated-17] [INFO] [1783327426.272506704] [lifecycle_manager_navigation]: Configuring controller_server
[component_container_isolated-17] [INFO] [1783327426.273777469] [controller_server]: Configuring controller interface
[component_container_isolated-17] [INFO] [1783327426.274796564] [controller_server]: getting goal checker plugins..
[component_container_isolated-17] [INFO] [1783327426.278036726] [controller_server]: Controller frequency set to 10.0000Hz
[component_container_isolated-17] [INFO] [1783327426.278400689] [local_costmap.local_costmap]: Configuring
[component_container_isolated-17] [INFO] [1783327426.359851373] [local_costmap.local_costmap]: Using plugin "obstacle_layer"
[yolo_costmap_bridge.py-19] [INFO] [1783327426.369539525] [yolo_costmap_bridge]: YoloCostmapBridge ready
[component_container_isolated-17] [INFO] [1783327426.409092812] [local_costmap.local_costmap]: Subscribed to Topics: scan tracked_obstacles
[component_container_isolated-17] [INFO] [1783327426.569634028] [local_costmap.local_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-17] [INFO] [1783327426.571134379] [local_costmap.local_costmap]: Using plugin "keepout_filter"
[component_container_isolated-17] [INFO] [1783327426.629789593] [local_costmap.local_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-17] [INFO] [1783327426.629987762] [local_costmap.local_costmap]: Using plugin "inflation_layer"
[component_container_isolated-17] [INFO] [1783327426.675686203] [local_costmap.local_costmap]: Initialized plugin "inflation_layer"
[imu_madgwick_filter.py-4] [INFO] [1783327426.703188268] [imu_madgwick_filter]: [imu_madgwick ->] msgs=198 q_w=0.9994 angle=3.8deg beta=0.0330
[component_container_isolated-17] [INFO] [1783327426.749688093] [controller_server]: Created progress_checker : progress_checker of type nav2_controller::SimpleProgressChecker
[component_container_isolated-17] [INFO] [1783327426.758052772] [controller_server]: Created goal checker : goal_checker of type nav2_controller::SimpleGoalChecker
[component_container_isolated-17] [INFO] [1783327426.768221639] [controller_server]: Controller Server has goal_checker  goal checkers available.
[component_container_isolated-17] [INFO] [1783327426.773086111] [controller_server]: Created controller : FollowPath of type nav2_regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-17] [INFO] [1783327426.883497544] [controller_server]: Controller Server has FollowPath  controllers available.
[imu_madgwick_filter.py-6] [INFO] [1783327426.908312662] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=405 q_w=0.9993 angle=4.3deg beta=0.0030
[component_container_isolated-17] [INFO] [1783327426.981291624] [lifecycle_manager_navigation]: Configuring smoother_server
[component_container_isolated-17] [INFO] [1783327426.983110061] [smoother_server]: Configuring smoother server
[racing_obstacle_detection_yolo-18] [WARN] [1783327426.992975258] [ObstacleDetectionNode]: input fps: 11.15, out fps: 11.16, infer time ms: 10, post process time ms: 6
[component_container_isolated-17] [INFO] [1783327427.069721594] [smoother_server]: Created smoother : SmoothPath of type nav2_constrained_smoother/ConstrainedSmoother
[component_container_isolated-17] [INFO] [1783327427.137414118] [smoother_server]: Smoother Server has SmoothPath  smoothers available.
[component_container_isolated-17] [INFO] [1783327427.192747250] [lifecycle_manager_navigation]: Configuring planner_server
[component_container_isolated-17] [INFO] [1783327427.193424924] [planner_server]: Configuring
[component_container_isolated-17] [INFO] [1783327427.193722261] [global_costmap.global_costmap]: Configuring
[component_container_isolated-17] [INFO] [1783327427.243317037] [global_costmap.global_costmap]: Using plugin "static_layer"
[component_container_isolated-17] [INFO] [1783327427.269855715] [global_costmap.global_costmap]: Subscribing to the map topic (/map) with transient local durability
[component_container_isolated-17] [INFO] [1783327427.278326270] [global_costmap.global_costmap]: Initialized plugin "static_layer"
[component_container_isolated-17] [INFO] [1783327427.280014331] [global_costmap.global_costmap]: Using plugin "obstacle_layer"
[component_container_isolated-17] [INFO] [1783327427.303221430] [global_costmap.global_costmap]: Subscribed to Topics: scan tracked_obstacles
[competition_master_stage3.py-20] [INFO] [1783327427.323751289] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-20] [INFO] [1783327427.327277246] [competition_master_stage3]: === [Stage 3] 总控节点初始化 ===
[competition_master_stage3.py-20] [INFO] [1783327427.331040206] [competition_master_stage3]:   QR点:    (0.41, -3.17, yaw=0.00)
[competition_master_stage3.py-20] [INFO] [1783327427.334731373] [competition_master_stage3]:   通道入口: (0.38, -1.10, yaw=0.00)
[competition_master_stage3.py-20] [INFO] [1783327427.339056214] [competition_master_stage3]:   P点:     (-1.99, -0.01, yaw=0.26)
[competition_master_stage3.py-20] [INFO] [1783327427.342094416] [competition_master_stage3]:   cruise_cw: 4路点 (1,2,VLM,post) → VLM=(3.04, -1.58)
[competition_master_stage3.py-20] [INFO] [1783327427.345369453] [competition_master_stage3]:   cruise_ccw: 4路点 (1,2,VLM,post) → VLM=(2.02, 0.94)
[competition_master_stage3.py-20] [INFO] [1783327427.348720033] [competition_master_stage3]:   超时: total=180.0s QR=90.0s entry=60.0s cruise=180.0s vlm=30.0s return=120.0s
[competition_master_stage3.py-20] [INFO] [1783327427.352852705] [competition_master_stage3]:   回退QR方向: 逆时针
[competition_master_stage3.py-20] [INFO] [1783327427.356443496] [competition_master_stage3]:   VLM结果话题: vlm_result
[competition_master_stage3.py-20] [INFO] [1783327427.360016746] [competition_master_stage3]: ============================================================
[component_container_isolated-17] [INFO] [1783327427.423021591] [global_costmap.global_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-17] [INFO] [1783327427.423245843] [global_costmap.global_costmap]: Using plugin "keepout_filter"
[component_container_isolated-17] [INFO] [1783327427.436922875] [global_costmap.global_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-17] [INFO] [1783327427.437104210] [global_costmap.global_costmap]: Using plugin "inflation_layer"
[component_container_isolated-17] [INFO] [1783327427.451763961] [global_costmap.global_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-17] [INFO] [1783327427.512605823] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 163 X 141 at 0.050000 m/pix
[component_container_isolated-17] [INFO] [1783327427.540128805] [planner_server]: Created global planner plugin GridBased of type nav2_smac_planner/SmacPlannerHybrid
[component_container_isolated-17] [INFO] [1783327427.540449975] [planner_server]: Configuring GridBased of type SmacPlannerHybrid
[component_container_isolated-17] [INFO] [1783327427.613293891] [planner_server]: Even sized heuristic lookup table size set 266.000000, increasing size by 1 to make odd
[rviz2-22] [INFO] [1783327427.929933594] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-22] [INFO] [1783327427.930612185] [rviz2]: OpenGl version: 4.5 (GLSL 4.5)
[racing_obstacle_detection_yolo-18] [WARN] [1783327428.058625105] [ObstacleDetectionNode]: input fps: 14.07, out fps: 14.08, infer time ms: 10, post process time ms: 6
[rviz2-22] [INFO] [1783327428.586016491] [rviz2]: Stereo is NOT SUPPORTED
[racing_obstacle_detection_yolo-18] [WARN] [1783327429.076153241] [ObstacleDetectionNode]: input fps: 12.78, out fps: 12.78, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-18] [WARN] [1783327430.120074807] [ObstacleDetectionNode]: input fps: 13.42, out fps: 13.42, infer time ms: 10, post process time ms: 6
[hobot_codec_republish-13] [WARN] [1783327430.412230658] [vlm_jpeg_encoder]: Sub imgRaw fps [12.93]
[hobot_codec_republish-13] [WARN] [1783327430.418777649] [vlm_jpeg_encoder]: Pub img fps [12.93]
[racing_obstacle_detection_yolo-18] [WARN] [1783327431.184039311] [ObstacleDetectionNode]: input fps: 14.12, out fps: 14.12, infer time ms: 10, post process time ms: 7
[rviz2-22] [INFO] [1783327431.582621021] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[rviz2-22] [ERROR] [1783327432.054996604] [rviz2]: Vertex Program:rviz/glsl120/indexed_8bit_image.vert Fragment Program:rviz/glsl120/indexed_8bit_image.frag GLSL link result :
[rviz2-22] active samplers with a different type refer to the same texture image unit
[racing_obstacle_detection_yolo-18] [WARN] [1783327432.216470881] [ObstacleDetectionNode]: input fps: 13.61, out fps: 13.55, infer time ms: 14, post process time ms: 6
[qr_decoder-10] [INFO] [1783327433.039538355] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=200 last_qr_frame=-1 gap=-1 frames rejects=0
[racing_obstacle_detection_yolo-18] [WARN] [1783327433.238063625] [ObstacleDetectionNode]: input fps: 14.62, out fps: 14.69, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-18] [WARN] [1783327434.266065281] [ObstacleDetectionNode]: input fps: 11.68, out fps: 11.68, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-18] [WARN] [1783327435.318495173] [ObstacleDetectionNode]: input fps: 14.25, out fps: 14.25, infer time ms: 10, post process time ms: 6
[hobot_codec_republish-13] [WARN] [1783327435.439326354] [vlm_jpeg_encoder]: Sub imgRaw fps [13.53]
[hobot_codec_republish-13] [WARN] [1783327435.443476484] [vlm_jpeg_encoder]: Pub img fps [13.54]
[racing_obstacle_detection_yolo-18] [WARN] [1783327436.356830038] [ObstacleDetectionNode]: input fps: 14.46, out fps: 14.46, infer time ms: 10, post process time ms: 6
[imu_madgwick_filter.py-4] [INFO] [1783327436.702945471] [imu_madgwick_filter]: [imu_madgwick ->] msgs=396 q_w=0.9978 angle=7.7deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1783327436.897813889] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=900 q_w=0.9993 angle=4.3deg beta=0.0030
[racing_obstacle_detection_yolo-18] [WARN] [1783327437.399567915] [ObstacleDetectionNode]: input fps: 14.38, out fps: 14.38, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-18] [WARN] [1783327438.409665562] [ObstacleDetectionNode]: input fps: 11.89, out fps: 11.89, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-18] [WARN] [1783327439.439679977] [ObstacleDetectionNode]: input fps: 13.59, out fps: 13.59, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-18] [WARN] [1783327440.447509989] [ObstacleDetectionNode]: input fps: 13.90, out fps: 13.92, infer time ms: 10, post process time ms: 7
[hobot_codec_republish-13] [WARN] [1783327440.470664868] [vlm_jpeg_encoder]: Sub imgRaw fps [13.91]
[hobot_codec_republish-13] [WARN] [1783327440.475121709] [vlm_jpeg_encoder]: Pub img fps [13.91]
[racing_obstacle_detection_yolo-18] [WARN] [1783327441.503678121] [ObstacleDetectionNode]: input fps: 13.26, out fps: 13.25, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-18] [WARN] [1783327442.557336481] [ObstacleDetectionNode]: input fps: 14.23, out fps: 14.25, infer time ms: 9, post process time ms: 6
[racing_obstacle_detection_yolo-18] [WARN] [1783327443.567228745] [ObstacleDetectionNode]: input fps: 12.88, out fps: 12.88, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-18] [WARN] [1783327444.590328827] [ObstacleDetectionNode]: input fps: 14.66, out fps: 14.66, infer time ms: 10, post process time ms: 6
[hobot_codec_republish-13] [WARN] [1783327445.508872284] [vlm_jpeg_encoder]: Sub imgRaw fps [13.50]
[hobot_codec_republish-13] [WARN] [1783327445.512600283] [vlm_jpeg_encoder]: Pub img fps [13.50]
[racing_obstacle_detection_yolo-18] [WARN] [1783327445.631951284] [ObstacleDetectionNode]: input fps: 13.45, out fps: 13.45, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-18] [WARN] [1783327446.657022318] [ObstacleDetectionNode]: input fps: 14.63, out fps: 14.63, infer time ms: 10, post process time ms: 6
[imu_madgwick_filter.py-4] [INFO] [1783327446.707666573] [imu_madgwick_filter]: [imu_madgwick ->] msgs=595 q_w=0.9948 angle=11.7deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1783327446.898638093] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1405 q_w=0.9993 angle=4.3deg beta=0.0030
[racing_obstacle_detection_yolo-18] [WARN] [1783327447.664400920] [ObstacleDetectionNode]: input fps: 13.00, out fps: 13.00, infer time ms: 10, post process time ms: 12
[qr_decoder-10] [INFO] [1783327447.931023873] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=400 last_qr_frame=-1 gap=-1 frames rejects=0
[component_container_isolated-17] [INFO] [1783327448.128410118] [planner_server]: Configured plugin GridBased of type SmacPlannerHybrid with maximum iterations 1500, max on approach iterations 300, and not allowing unknown traversal. Tolerance 0.50.Using motion model: Reeds-Shepp.
[component_container_isolated-17] [INFO] [1783327448.128721371] [planner_server]: Planner Server has GridBased  planners available.
[component_container_isolated-17] [INFO] [1783327448.204217806] [lifecycle_manager_navigation]: Configuring behavior_server
[component_container_isolated-17] [INFO] [1783327448.207914512] [behavior_server]: Configuring
[component_container_isolated-17] [INFO] [1783327448.268549871] [behavior_server]: Creating behavior plugin spin of type nav2_behaviors/Spin
[component_container_isolated-17] [INFO] [1783327448.278101515] [behavior_server]: Configuring spin
[component_container_isolated-17] [INFO] [1783327448.331891926] [behavior_server]: Creating behavior plugin backup of type nav2_behaviors/BackUp
[component_container_isolated-17] [INFO] [1783327448.336195597] [behavior_server]: Configuring backup
[component_container_isolated-17] [INFO] [1783327448.395217230] [behavior_server]: Creating behavior plugin drive_on_heading of type nav2_behaviors/DriveOnHeading
[component_container_isolated-17] [INFO] [1783327448.401103293] [behavior_server]: Configuring drive_on_heading
[component_container_isolated-17] [INFO] [1783327448.458251365] [behavior_server]: Creating behavior plugin wait of type nav2_behaviors/Wait
[component_container_isolated-17] [INFO] [1783327448.462277866] [behavior_server]: Configuring wait
[component_container_isolated-17] [INFO] [1783327448.498388921] [lifecycle_manager_navigation]: Configuring bt_navigator
[component_container_isolated-17] [INFO] [1783327448.499862478] [bt_navigator]: Configuring
[racing_obstacle_detection_yolo-18] [WARN] [1783327448.697901686] [ObstacleDetectionNode]: input fps: 11.56, out fps: 11.55, infer time ms: 10, post process time ms: 7
[competition_master_stage3.py-20] [INFO] [1783327448.863698423] [competition_master_stage3]: [CPU] governor → performance
[competition_master_stage3.py-20] [INFO] [1783327448.873771865] [competition_master_stage3]: [LAUNCH] 发车阶段: 21.8s
[competition_master_stage3.py-20] [INFO] [1783327448.880876608] [competition_master_stage3]: >>> 系统就绪, 开始 Stage 3 导航
[competition_master_stage3.py-20] [INFO] [1783327448.930921603] [competition_master_stage3]: [BAG] 录制开始: stage3_20260706_164408
[competition_master_stage3.py-20] [INFO] [1783327448.944511415] [competition_master_stage3]: [状态机] INIT → NAV_TO_QR
[competition_master_stage3.py-20] [INFO] [1783327448.971218660] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[competition_master_stage3.py-20] [INFO] [1783327449.056899370] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.01,-0.02) yaw=13deg cmd=(vx=0.00 wz=0.00) elapsed=0.1s cpuFreq=1500MHz cpuT=69C bpuT=67C cpu=88% mem=18%
[component_container_isolated-17] [INFO] [1783327449.136490638] [lifecycle_manager_navigation]: Configuring waypoint_follower
[component_container_isolated-17] [INFO] [1783327449.138832204] [waypoint_follower]: Configuring
[competition_master_stage3.py-20] [INFO] [1783327449.179918686] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.01,-0.02) yaw=13deg cmd=(vx=0.00 wz=0.00) elapsed=0.2s cpuFreq=1500MHz cpuT=69C bpuT=68C cpu=100% mem=18%
[competition_master_stage3.py-20] [WARN] [1783327449.214493555] [competition_master_stage3]: 导航目标被拒绝, 3s 后重试...
[component_container_isolated-17] [INFO] [1783327449.257010010] [waypoint_follower]: Created waypoint_task_executor : wait_at_waypoint of type nav2_waypoint_follower::WaitAtWaypoint
[component_container_isolated-17] [INFO] [1783327449.274284070] [lifecycle_manager_navigation]: Configuring velocity_smoother
[component_container_isolated-17] [INFO] [1783327449.276140506] [velocity_smoother]: Configuring velocity smoother
[component_container_isolated-17] [INFO] [1783327449.332251023] [lifecycle_manager_navigation]: Activating controller_server
[component_container_isolated-17] [INFO] [1783327449.333624163] [controller_server]: Activating
[component_container_isolated-17] [INFO] [1783327449.333908666] [local_costmap.local_costmap]: Activating
[component_container_isolated-17] [INFO] [1783327449.334014167] [local_costmap.local_costmap]: Checking transform
[component_container_isolated-17] [INFO] [1783327449.334520089] [local_costmap.local_costmap]: start
[component_container_isolated-17] [INFO] [1783327449.354988058] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327449.373474006] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327449.373685175] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [INFO] [1783327449.380700292] [local_costmap.local_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[component_container_isolated-17] [INFO] [1783327449.570777200] [controller_server]: Activating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-17] [INFO] [1783327449.571146620] [controller_server]: Creating bond (controller_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327449.684061870] [lifecycle_manager_navigation]: Server controller_server connected with bond.
[component_container_isolated-17] [INFO] [1783327449.684264664] [lifecycle_manager_navigation]: Activating smoother_server
[component_container_isolated-17] [INFO] [1783327449.689862557] [smoother_server]: Activating
[component_container_isolated-17] [INFO] [1783327449.690122893] [smoother_server]: Activating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-17] [INFO] [1783327449.690306770] [smoother_server]: Creating bond (smoother_server) to lifecycle manager.
[racing_obstacle_detection_yolo-18] [WARN] [1783327449.775922936] [ObstacleDetectionNode]: input fps: 12.09, out fps: 12.08, infer time ms: 10, post process time ms: 9
[component_container_isolated-17] [INFO] [1783327449.819114856] [lifecycle_manager_navigation]: Server smoother_server connected with bond.
[component_container_isolated-17] [INFO] [1783327449.819325150] [lifecycle_manager_navigation]: Activating planner_server
[component_container_isolated-17] [INFO] [1783327449.820832750] [planner_server]: Activating
[component_container_isolated-17] [INFO] [1783327449.821336880] [global_costmap.global_costmap]: Activating
[component_container_isolated-17] [INFO] [1783327449.821475465] [global_costmap.global_costmap]: Checking transform
[component_container_isolated-17] [INFO] [1783327449.821752301] [global_costmap.global_costmap]: start
[component_container_isolated-17] [INFO] [1783327449.841991643] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327449.855643622] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327449.855832207] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [INFO] [1783327449.870548531] [global_costmap.global_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[rviz2-22] [INFO] [1783327450.037996363] [rviz2]: Trying to create a map of size 60 x 60 using 1 swatches
[hobot_codec_republish-13] [WARN] [1783327450.558385622] [vlm_jpeg_encoder]: Sub imgRaw fps [12.87]
[hobot_codec_republish-13] [WARN] [1783327450.563387133] [vlm_jpeg_encoder]: Pub img fps [12.87]
[racing_obstacle_detection_yolo-18] [WARN] [1783327450.788214739] [ObstacleDetectionNode]: input fps: 13.79, out fps: 13.79, infer time ms: 10, post process time ms: 6
[component_container_isolated-17] [INFO] [1783327450.857120266] [planner_server]: Activating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-17] [INFO] [1783327450.868721931] [planner_server]: Creating bond (planner_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327451.024355966] [lifecycle_manager_navigation]: Server planner_server connected with bond.
[component_container_isolated-17] [INFO] [1783327451.024589468] [lifecycle_manager_navigation]: Activating behavior_server
[component_container_isolated-17] [INFO] [1783327451.025799814] [behavior_server]: Activating
[component_container_isolated-17] [INFO] [1783327451.025924982] [behavior_server]: Activating spin
[component_container_isolated-17] [INFO] [1783327451.026077151] [behavior_server]: Activating backup
[component_container_isolated-17] [INFO] [1783327451.026153235] [behavior_server]: Activating drive_on_heading
[component_container_isolated-17] [INFO] [1783327451.026226652] [behavior_server]: Activating wait
[component_container_isolated-17] [INFO] [1783327451.026306986] [behavior_server]: Creating bond (behavior_server) to lifecycle manager.
[competition_master_stage3.py-20] [INFO] [1783327451.040604138] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.01,-0.02) yaw=13deg cmd=(vx=0.00 wz=0.00) elapsed=2.1s cpuFreq=1500MHz cpuT=70C bpuT=68C cpu=100% mem=18%
[component_container_isolated-17] [INFO] [1783327451.144766121] [lifecycle_manager_navigation]: Server behavior_server connected with bond.
[component_container_isolated-17] [INFO] [1783327451.144936206] [lifecycle_manager_navigation]: Activating bt_navigator
[component_container_isolated-17] [INFO] [1783327451.145903841] [bt_navigator]: Activating
[component_container_isolated-17] [WARN] [1783327451.322229800] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-17] [WARN] [1783327451.508324195] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-17] [WARN] [1783327451.624521681] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-17] [WARN] [1783327451.840334684] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[racing_obstacle_detection_yolo-18] [WARN] [1783327451.882861511] [ObstacleDetectionNode]: input fps: 11.00, out fps: 10.98, infer time ms: 10, post process time ms: 7
[component_container_isolated-17] [WARN] [1783327452.084595445] [bt_navigator_navigate_to_pose_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[competition_master_stage3.py-20] [INFO] [1783327452.221078851] [competition_master_stage3]: 重试发送导航目标 (QR点)...
[competition_master_stage3.py-20] [INFO] [1783327452.239527630] [competition_master_stage3]: [DIAG] nav目标距离: 3.97m, robot=(-2.01,-0.02) → target=(0.41,-3.17)
[competition_master_stage3.py-20] [INFO] [1783327452.259818886] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-17] [INFO] [1783327452.286615962] [bt_navigator]: Creating bond (bt_navigator) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327452.316961659] [bt_navigator]: Begin navigating from current location (-2.01, -0.02) to (0.41, -3.17)
[component_container_isolated-17] [INFO] [1783327452.317868127] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[competition_master_stage3.py-20] [INFO] [1783327452.337516793] [competition_master_stage3]: 导航目标已接受，车辆出发...
[component_container_isolated-17] [INFO] [1783327452.338255176] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327452.347572192] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327452.347727610] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327452.363374193] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [INFO] [1783327452.418525944] [lifecycle_manager_navigation]: Server bt_navigator connected with bond.
[component_container_isolated-17] [INFO] [1783327452.418743613] [lifecycle_manager_navigation]: Activating waypoint_follower
[component_container_isolated-17] [INFO] [1783327452.420511048] [waypoint_follower]: Activating
[component_container_isolated-17] [INFO] [1783327452.420813843] [waypoint_follower]: Creating bond (waypoint_follower) to lifecycle manager.
[rviz2-22] [INFO] [1783327452.438857743] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[component_container_isolated-17] [INFO] [1783327452.557994672] [lifecycle_manager_navigation]: Server waypoint_follower connected with bond.
[component_container_isolated-17] [INFO] [1783327452.558290009] [lifecycle_manager_navigation]: Activating velocity_smoother
[component_container_isolated-17] [INFO] [1783327452.561212082] [velocity_smoother]: Activating
[component_container_isolated-17] [INFO] [1783327452.561551794] [velocity_smoother]: Creating bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327452.703546757] [lifecycle_manager_navigation]: Server velocity_smoother connected with bond.
[component_container_isolated-17] [INFO] [1783327452.703747468] [lifecycle_manager_navigation]: Managed nodes are active
[component_container_isolated-17] [INFO] [1783327452.703988845] [lifecycle_manager_navigation]: Creating bond timer...
[component_container_isolated-17] [WARN] [1783327452.833443009] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 2.0625 Hz
[speed_profile_node.py-21] [INFO] [1783327452.856325752] [speed_profile_node]: Plan received: 20 poses, mean|κ|=0.4965 m⁻¹, max|κ|=1.5564 m⁻¹, mean_v=0.425 m/s, min_v=0.271 m/s, max_v=0.500 m/s
[racing_obstacle_detection_yolo-18] [WARN] [1783327452.886722908] [ObstacleDetectionNode]: input fps: 11.94, out fps: 11.95, infer time ms: 10, post process time ms: 7
[component_container_isolated-17] [INFO] [1783327453.018851516] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-17] [WARN] [1783327453.019397439] [controller_server]: No goal checker was specified in parameter 'current_goal_checker'. Server will use only plugin loaded goal_checker . This warning will appear once.
[competition_master_stage3.py-20] [INFO] [1783327453.048559455] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.01,-0.02) yaw=13deg cmd=(vx=0.00 wz=0.00) elapsed=4.1s plan[20pts 4.1m] (-1.98,-0.07)→(0.43,-3.22) cpuFreq=1500MHz cpuT=70C bpuT=68C cpu=87% mem=19%
[racing_obstacle_detection_yolo-18] [WARN] [1783327453.908197292] [ObstacleDetectionNode]: input fps: 12.72, out fps: 12.72, infer time ms: 10, post process time ms: 6
[component_container_isolated-17] [INFO] [1783327454.117945839] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327454.135465982] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327454.161981511] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327454.162796728] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327454.176478372] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783327454.835692569] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.5288 Hz
[speed_profile_node.py-21] [INFO] [1783327454.862043514] [speed_profile_node]: Plan received: 19 poses, mean|κ|=0.3036 m⁻¹, max|κ|=1.2001 m⁻¹, mean_v=0.453 m/s, min_v=0.313 m/s, max_v=0.500 m/s
[racing_obstacle_detection_yolo-18] [WARN] [1783327454.909674516] [ObstacleDetectionNode]: input fps: 12.72, out fps: 10.99, infer time ms: 11, post process time ms: 6
[component_container_isolated-17] Reallocing temp weights 301 - 60
[component_container_isolated-17] [INFO] [1783327455.019805426] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-20] [INFO] [1783327455.051951055] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.77,-0.05) yaw=-23deg cmd=(vx=0.49 wz=-1.22) elapsed=6.1s plan[19pts 3.8m] (-1.68,-0.07)→(0.43,-3.22) cpuFreq=1500MHz cpuT=70C bpuT=68C cpu=62% mem=19%
[component_container_isolated-17] Reallocing temp weights 839 - 60
[hobot_codec_republish-13] [WARN] [1783327455.634483634] [vlm_jpeg_encoder]: Sub imgRaw fps [12.22]
[hobot_codec_republish-13] [WARN] [1783327455.636867618] [vlm_jpeg_encoder]: Pub img fps [12.22]
[racing_obstacle_detection_yolo-18] [WARN] [1783327455.991809514] [ObstacleDetectionNode]: input fps: 12.57, out fps: 12.95, infer time ms: 10, post process time ms: 6
[component_container_isolated-17] [INFO] [1783327456.119582020] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327456.126518967] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327456.162530636] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327456.162697971] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327456.179655816] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-4] [INFO] [1783327456.702063664] [imu_madgwick_filter]: [imu_madgwick ->] msgs=793 q_w=0.8943 angle=53.2deg beta=0.0330
[component_container_isolated-17] [WARN] [1783327456.831982275] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.5083 Hz
[speed_profile_node.py-21] [INFO] [1783327456.847483729] [speed_profile_node]: Plan received: 14 poses, mean|κ|=0.2762 m⁻¹, max|κ|=1.0817 m⁻¹, mean_v=0.457 m/s, min_v=0.329 m/s, max_v=0.500 m/s
[imu_madgwick_filter.py-6] [INFO] [1783327456.893450585] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1771 q_w=0.8105 angle=71.7deg beta=0.0030
[component_container_isolated-17] [INFO] [1783327457.019796783] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-18] [WARN] [1783327457.046133850] [ObstacleDetectionNode]: input fps: 12.33, out fps: 12.35, infer time ms: 10, post process time ms: 6
[competition_master_stage3.py-20] [INFO] [1783327457.050587272] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.34,-0.76) yaw=-58deg cmd=(vx=-0.30 wz=-0.11) elapsed=8.1s plan[14pts 3.0m] (-1.23,-0.82)→(0.43,-3.22) cpuFreq=1500MHz cpuT=71C bpuT=69C cpu=70% mem=19%
[racing_obstacle_detection_yolo-18] [WARN] [1783327458.073257952] [ObstacleDetectionNode]: input fps: 13.63, out fps: 13.62, infer time ms: 10, post process time ms: 5
[component_container_isolated-17] [INFO] [1783327458.117950042] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327458.137366411] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327458.162805801] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327458.163222847] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327458.179944354] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783327458.834607464] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4866 Hz
[speed_profile_node.py-21] [INFO] [1783327458.850892800] [speed_profile_node]: Plan received: 12 poses, mean|κ|=0.3642 m⁻¹, max|κ|=1.1508 m⁻¹, mean_v=0.444 m/s, min_v=0.319 m/s, max_v=0.500 m/s
[component_container_isolated-17] [INFO] [1783327459.019798517] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-20] [INFO] [1783327459.043861892] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.97,-1.22) yaw=-48deg cmd=(vx=0.50 wz=-0.34) elapsed=10.1s plan[12pts 2.4m] (-0.93,-1.27)→(0.43,-3.22) cpuFreq=1500MHz cpuT=71C bpuT=69C cpu=50% mem=19%
[racing_obstacle_detection_yolo-18] [WARN] [1783327459.107860598] [ObstacleDetectionNode]: input fps: 12.57, out fps: 12.57, infer time ms: 10, post process time ms: 6
[component_container_isolated-17] [INFO] [1783327460.117834123] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327460.133362034] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327460.148966279] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327460.149275532] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327460.168175686] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-18] [WARN] [1783327460.212497478] [ObstacleDetectionNode]: input fps: 12.68, out fps: 12.68, infer time ms: 10, post process time ms: 5
[component_container_isolated-17] Reallocing temp weights 1500 - 60
[hobot_codec_republish-13] [WARN] [1783327460.659703275] [vlm_jpeg_encoder]: Sub imgRaw fps [12.94]
[hobot_codec_republish-13] [WARN] [1783327460.666273051] [vlm_jpeg_encoder]: Pub img fps [12.93]
[component_container_isolated-17] [WARN] [1783327460.837369156] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4437 Hz
[speed_profile_node.py-21] [INFO] [1783327460.845814701] [speed_profile_node]: Plan received: 8 poses, mean|κ|=0.5094 m⁻¹, max|κ|=1.1352 m⁻¹, mean_v=0.420 m/s, min_v=0.321 m/s, max_v=0.500 m/s
[component_container_isolated-17] [INFO] [1783327461.019887670] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-20] [INFO] [1783327461.045569518] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.46,-2.00) yaw=-60deg cmd=(vx=-0.30 wz=0.04) elapsed=12.1s plan[8pts 1.5m] (-0.48,-2.02)→(0.43,-3.22) cpuFreq=1500MHz cpuT=71C bpuT=69C cpu=75% mem=19%
[racing_obstacle_detection_yolo-18] [WARN] [1783327461.285855082] [ObstacleDetectionNode]: input fps: 13.08, out fps: 13.07, infer time ms: 10, post process time ms: 8
[component_container_isolated-17] [INFO] [1783327462.118088210] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327462.129223075] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327462.147272219] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327462.147491263] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327462.162782045] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-18] [WARN] [1783327462.290204523] [ObstacleDetectionNode]: input fps: 13.92, out fps: 13.93, infer time ms: 10, post process time ms: 6
[component_container_isolated-17] [WARN] [1783327462.838304081] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4651 Hz
[speed_profile_node.py-21] [INFO] [1783327462.852954732] [speed_profile_node]: Plan received: 6 poses, mean|κ|=0.5677 m⁻¹, max|κ|=0.9597 m⁻¹, mean_v=0.410 m/s, min_v=0.346 m/s, max_v=0.499 m/s
[component_container_isolated-17] [INFO] [1783327463.019815115] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-20] [INFO] [1783327463.072323529] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.32,-2.23) yaw=-63deg cmd=(vx=0.50 wz=0.13) elapsed=14.1s plan[6pts 1.2m] (-0.33,-2.32)→(0.43,-3.22) cpuFreq=1500MHz cpuT=71C bpuT=69C cpu=75% mem=19%
[qr_decoder-10] [INFO] [1783327463.297435797] [qr_decoder_zbar]: [qr_decoder] QR DETECTED frame=593 symbols=1 (gap=-1 frames)
[qr_decoder-10] [INFO] [1783327463.300075574] [qr_decoder_zbar]: [QR] 1584 | 3D:(-0.533, +0.134, 1.384)m | px(158,238) D:1384mm
[qr_decoder-10] [INFO] [1783327463.301173502] [qr_decoder_zbar]: [QR] 1584 | robot_pos: (1.01, -3.08, yaw=-1.47)
[qr_decision.py-11] [INFO] [1783327463.310091969] [qr_decision]: [QR] 1584 CCW @ (x=1.01, y=-3.13, yaw=-1.45) → /qr_event
[competition_master_stage3.py-20] [INFO] [1783327463.323481773] [competition_master_stage3]: [QR检测] 内容: 1584
[qr_decision.py-11] [INFO] [1783327463.322657389] [qr_decision]: [检查点] qr_decision 发布 /qr_event (由 task_manager 决定停车)
[competition_master_stage3.py-20] [INFO] [1783327463.335202060] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decoder_zbar
[competition_master_stage3.py-20] [INFO] [1783327463.341599500] [competition_master_stage3]: >>> QR 解码已关闭, 等待方向判断 (/qr_event)...
[competition_master_stage3.py-20] [INFO] [1783327463.346990764] [competition_master_stage3]: [QR检测] 取消当前导航目标, 等待BT完成 cancel/halt 清理...
[racing_obstacle_detection_yolo-18] [WARN] [1783327463.356780031] [ObstacleDetectionNode]: input fps: 12.21, out fps: 12.21, infer time ms: 11, post process time ms: 7
[component_container_isolated-17] [INFO] [1783327463.419811303] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-17] [INFO] [1783327463.420039347] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[competition_master_stage3.py-20] [INFO] [1783327463.420941815] [competition_master_stage3]: [QR事件] 方向: 逆时针 (通道巡航阶段使用)
[component_container_isolated-17] [INFO] [1783327463.421566946] [bt_navigator]: [navigate_to_pose] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-17] [INFO] [1783327463.422776458] [bt_navigator]: Goal canceled
[competition_master_stage3.py-20] [INFO] [1783327463.435422130] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decision
[competition_master_stage3.py-20] [INFO] [1783327463.448202011] [competition_master_stage3]: [结果回调] BT取消确认完成 (STATUS_CANCELED), 准备发送通道入口目标...
[competition_master_stage3.py-20] [INFO] [1783327463.454732745] [competition_master_stage3]: [状态机] NAV_TO_QR → BACKING_UP
[competition_master_stage3.py-20] [INFO] [1783327463.457726025] [competition_master_stage3]: >>> BT取消完成, 右后退摆正车头→前进进通道...
[competition_master_stage3.py-20] [INFO] [1783327463.463224790] [competition_master_stage3]: [BACKUP] 右后退中: vx=-0.15 wz=0.80, 持续 6.0s...
[qr_decoder-10] [INFO] [1783327463.480222881] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[INFO] [qr_decoder-10]: process has finished cleanly [pid 7021]
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
[qr_decision.py-11]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 681, in _wait_for_ready_callbacks
[qr_decision.py-11]     raise ExternalShutdownException()
[qr_decision.py-11] rclpy.executors.ExternalShutdownException
[racing_obstacle_detection_yolo-18] [WARN] [1783327464.421574403] [ObstacleDetectionNode]: input fps: 10.34, out fps: 10.34, infer time ms: 10, post process time ms: 8
[ERROR] [qr_decision.py-11]: process has died [pid 7023, exit code 1, cmd '/userdata/dev_ws/install/qr_decoder/lib/qr_decoder/qr_decision.py --ros-args -r __node:=qr_decision --params-file /tmp/launch_params_gzdgcvm0'].
[competition_master_stage3.py-20] [INFO] [1783327465.040339316] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.01,-2.72) yaw=-61deg cmd=(vx=-0.15 wz=0.80) elapsed=16.1s plan[6pts 1.2m] (-0.33,-2.32)→(0.43,-3.22) cpuFreq=1500MHz cpuT=71C bpuT=69C cpu=66% mem=18%
[racing_obstacle_detection_yolo-18] [WARN] [1783327465.438852715] [ObstacleDetectionNode]: input fps: 12.78, out fps: 12.78, infer time ms: 10, post process time ms: 8
[hobot_codec_republish-13] [WARN] [1783327465.707419413] [vlm_jpeg_encoder]: Sub imgRaw fps [12.09]
[hobot_codec_republish-13] [WARN] [1783327465.714855655] [vlm_jpeg_encoder]: Pub img fps [12.08]
[racing_obstacle_detection_yolo-18] [WARN] [1783327466.468590330] [ObstacleDetectionNode]: input fps: 13.58, out fps: 13.58, infer time ms: 10, post process time ms: 5
[imu_madgwick_filter.py-4] [INFO] [1783327466.701911370] [imu_madgwick_filter]: [imu_madgwick ->] msgs=991 q_w=0.9825 angle=21.5deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1783327466.899878883] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2099 q_w=0.9518 angle=35.7deg beta=0.0030
[competition_master_stage3.py-20] [INFO] [1783327467.042379707] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.08,-2.68) yaw=-21deg cmd=(vx=-0.15 wz=0.80) elapsed=18.1s plan[6pts 1.2m] (-0.33,-2.32)→(0.43,-3.22) cpuFreq=1500MHz cpuT=71C bpuT=69C cpu=100% mem=18%
[racing_obstacle_detection_yolo-18] [WARN] [1783327467.516760267] [ObstacleDetectionNode]: input fps: 14.42, out fps: 14.40, infer time ms: 12, post process time ms: 11
[racing_obstacle_detection_yolo-18] [WARN] [1783327468.596353615] [ObstacleDetectionNode]: input fps: 14.99, out fps: 14.76, infer time ms: 10, post process time ms: 6
[competition_master_stage3.py-20] [INFO] [1783327469.042102704] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.30,-2.68) yaw=24deg cmd=(vx=-0.15 wz=0.80) elapsed=20.1s plan[6pts 1.2m] (-0.33,-2.32)→(0.43,-3.22) cpuFreq=1500MHz cpuT=71C bpuT=69C cpu=75% mem=18%
[competition_master_stage3.py-20] [INFO] [1783327469.466276814] [competition_master_stage3]: [状态机] BACKING_UP → CRUISE_CHANNEL
[competition_master_stage3.py-20] [INFO] [1783327469.469381429] [competition_master_stage3]: [CRUISE] 方向: CCW (逆时针, even QR), 路点: (1.56,-1.34), (3.02,-1.07), (2.02,0.94) → VLM=(2.02,0.94) → post=(0.94,-0.09)
[competition_master_stage3.py-20] [INFO] [1783327469.478797232] [competition_master_stage3]: [CRUISE] NavigateThroughPoses: (0.38,-1.10), (1.56,-1.34), (3.02,-1.07), (2.02,0.94)
[component_container_isolated-17] [INFO] [1783327469.493293211] [bt_navigator]: Begin navigating from current location through 4 poses to (2.02, 0.94)
[component_container_isolated-17] [INFO] [1783327469.493965260] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327469.511194850] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327469.526658506] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327469.526895134] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[competition_master_stage3.py-20] [INFO] [1783327469.529589744] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[component_container_isolated-17] [WARN] [1783327469.545769740] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-18] [WARN] [1783327469.612029950] [ObstacleDetectionNode]: input fps: 12.66, out fps: 12.81, infer time ms: 11, post process time ms: 6
[component_container_isolated-17] [WARN] [1783327469.849381176] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 3.1058 Hz
[speed_profile_node.py-21] [INFO] [1783327469.887693563] [speed_profile_node]: Plan received: 49 poses, mean|κ|=1.5862 m⁻¹, max|κ|=4.4105 m⁻¹, mean_v=0.313 m/s, min_v=0.150 m/s, max_v=0.500 m/s
[component_container_isolated-17] [INFO] [1783327469.999093769] [controller_server]: Received a goal, begin computing control effort.
[racing_obstacle_detection_yolo-18] [WARN] [1783327470.694101797] [ObstacleDetectionNode]: input fps: 14.29, out fps: 13.86, infer time ms: 10, post process time ms: 6
[hobot_codec_republish-13] [WARN] [1783327470.748028089] [vlm_jpeg_encoder]: Sub imgRaw fps [13.69]
[hobot_codec_republish-13] [WARN] [1783327470.751961129] [vlm_jpeg_encoder]: Pub img fps [13.70]
[competition_master_stage3.py-20] [INFO] [1783327471.049213907] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.41,-2.76) yaw=52deg cmd=(vx=0.50 wz=0.76) elapsed=22.1s plan[49pts 9.8m] (-0.48,-2.77)→(2.08,0.98) cpuFreq=1500MHz cpuT=71C bpuT=70C cpu=70% mem=18%
[component_container_isolated-17] [INFO] [1783327471.096650466] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327471.117519967] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327471.133760088] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327471.134196218] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327471.151457474] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-4] [WARN] [1783327471.507295207] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1502s > 0.15s, capping
[racing_obstacle_detection_yolo-18] [WARN] [1783327471.735856873] [ObstacleDetectionNode]: input fps: 13.85, out fps: 14.41, infer time ms: 10, post process time ms: 6
[component_container_isolated-17] [WARN] [1783327471.845374887] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4139 Hz
[speed_profile_node.py-21] [INFO] [1783327471.898438752] [speed_profile_node]: Plan received: 46 poses, mean|κ|=1.6722 m⁻¹, max|κ|=4.4105 m⁻¹, mean_v=0.303 m/s, min_v=0.150 m/s, max_v=0.499 m/s
[component_container_isolated-17] [INFO] [1783327472.000762028] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-18] [WARN] [1783327472.879364809] [ObstacleDetectionNode]: input fps: 14.37, out fps: 13.13, infer time ms: 10, post process time ms: 6
[competition_master_stage3.py-20] [INFO] [1783327473.040148373] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.24,-1.98) yaw=72deg cmd=(vx=0.41 wz=-0.02) elapsed=24.1s plan[46pts 9.3m] (-0.33,-2.32)→(2.08,0.98) cpuFreq=1500MHz cpuT=71C bpuT=70C cpu=25% mem=18%
[component_container_isolated-17] [INFO] [1783327473.094104119] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327473.116747761] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327473.126863737] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327473.127024197] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327473.150503014] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783327473.844779515] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3927 Hz
[racing_obstacle_detection_yolo-18] [WARN] [1783327473.897829377] [ObstacleDetectionNode]: input fps: 12.83, out fps: 13.74, infer time ms: 11, post process time ms: 6
[speed_profile_node.py-21] [INFO] [1783327473.902475299] [speed_profile_node]: Plan received: 42 poses, mean|κ|=1.8069 m⁻¹, max|κ|=4.4105 m⁻¹, mean_v=0.289 m/s, min_v=0.150 m/s, max_v=0.499 m/s
[component_container_isolated-17] [INFO] [1783327474.000749569] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-18] [WARN] [1783327474.911294783] [ObstacleDetectionNode]: input fps: 14.72, out fps: 14.91, infer time ms: 10, post process time ms: 12
[component_container_isolated-17] [INFO] [1783327474.994467818] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327475.007367446] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327475.024738451] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327475.024912370] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327475.036134231] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-20] [INFO] [1783327475.051577842] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.07,-1.51) yaw=70deg cmd=(vx=0.50 wz=-0.69) elapsed=26.1s plan[42pts 8.4m] (-0.02,-1.42)→(2.08,0.98) cpuFreq=1500MHz cpuT=72C bpuT=70C cpu=87% mem=18%
[hobot_codec_republish-13] [WARN] [1783327475.763086890] [vlm_jpeg_encoder]: Sub imgRaw fps [13.96]
[hobot_codec_republish-13] [WARN] [1783327475.767808604] [vlm_jpeg_encoder]: Pub img fps [13.96]
[component_container_isolated-17] [WARN] [1783327475.850897219] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2242 Hz
[speed_profile_node.py-21] [INFO] [1783327475.892578215] [speed_profile_node]: Plan received: 41 poses, mean|κ|=1.7982 m⁻¹, max|κ|=4.4105 m⁻¹, mean_v=0.291 m/s, min_v=0.150 m/s, max_v=0.500 m/s
[racing_obstacle_detection_yolo-18] [WARN] [1783327475.940755026] [ObstacleDetectionNode]: input fps: 13.12, out fps: 13.53, infer time ms: 10, post process time ms: 6
[component_container_isolated-17] [INFO] [1783327476.000768078] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-4] [INFO] [1783327476.705582790] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1184 q_w=0.9765 angle=24.9deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1783327476.893433688] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2505 q_w=0.9985 angle=6.3deg beta=0.0030
[racing_obstacle_detection_yolo-18] [WARN] [1783327476.952355311] [ObstacleDetectionNode]: input fps: 12.99, out fps: 12.86, infer time ms: 10, post process time ms: 6
[competition_master_stage3.py-20] [INFO] [1783327477.040831018] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.53,-1.06) yaw=16deg cmd=(vx=0.50 wz=-0.63) elapsed=28.1s plan[41pts 8.2m] (0.13,-1.27)→(2.08,0.98) cpuFreq=1500MHz cpuT=71C bpuT=70C cpu=50% mem=18%
[component_container_isolated-17] [INFO] [1783327477.094234127] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327477.111488172] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327477.125713062] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327477.125875897] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327477.140433498] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783327477.843905468] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3909 Hz
[speed_profile_node.py-21] [INFO] [1783327477.883130813] [speed_profile_node]: Plan received: 36 poses, mean|κ|=1.8296 m⁻¹, max|κ|=4.0834 m⁻¹, mean_v=0.276 m/s, min_v=0.150 m/s, max_v=0.500 m/s
[component_container_isolated-17] [INFO] [1783327478.000809014] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-18] [WARN] [1783327478.036071277] [ObstacleDetectionNode]: input fps: 14.08, out fps: 13.85, infer time ms: 10, post process time ms: 6
[competition_master_stage3.py-20] [INFO] [1783327479.040202470] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.90,-1.02) yaw=-11deg cmd=(vx=0.50 wz=-0.09) elapsed=30.1s plan[36pts 6.8m] (1.03,-1.12)→(2.08,0.98) cpuFreq=1500MHz cpuT=71C bpuT=70C cpu=40% mem=18%
[component_container_isolated-17] [INFO] [1783327479.094323833] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327479.109202187] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[racing_obstacle_detection_yolo-18] [WARN] [1783327479.113381895] [ObstacleDetectionNode]: input fps: 13.94, out fps: 13.93, infer time ms: 10, post process time ms: 6
[component_container_isolated-17] [INFO] [1783327479.125982685] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327479.126167395] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327479.136455496] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783327479.847661668] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4031 Hz
[speed_profile_node.py-21] [INFO] [1783327479.869762260] [speed_profile_node]: Plan received: 34 poses, mean|κ|=2.0307 m⁻¹, max|κ|=4.4105 m⁻¹, mean_v=0.272 m/s, min_v=0.150 m/s, max_v=0.500 m/s
[component_container_isolated-17] [INFO] [1783327480.000734542] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-18] [WARN] [1783327480.159443092] [ObstacleDetectionNode]: input fps: 14.11, out fps: 14.38, infer time ms: 10, post process time ms: 9
[hobot_codec_republish-13] [WARN] [1783327480.782413216] [vlm_jpeg_encoder]: Sub imgRaw fps [13.15]
[hobot_codec_republish-13] [WARN] [1783327480.785326869] [vlm_jpeg_encoder]: Pub img fps [13.16]
[competition_master_stage3.py-20] [INFO] [1783327481.040899822] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.65,-1.21) yaw=-19deg cmd=(vx=-0.30 wz=-0.01) elapsed=32.1s plan[34pts 6.9m] (1.33,-1.12)→(2.08,0.98) cpuFreq=1500MHz cpuT=71C bpuT=70C cpu=66% mem=18%
[component_container_isolated-17] [INFO] [1783327481.094617636] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327481.114188160] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327481.126796283] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327481.126968910] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327481.140472083] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-18] [WARN] [1783327481.189104640] [ObstacleDetectionNode]: input fps: 15.00, out fps: 14.55, infer time ms: 10, post process time ms: 6
[component_container_isolated-17] [WARN] [1783327481.843563844] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3959 Hz
[speed_profile_node.py-21] [INFO] [1783327481.897884915] [speed_profile_node]: Plan received: 30 poses, mean|κ|=2.3787 m⁻¹, max|κ|=5.8680 m⁻¹, mean_v=0.266 m/s, min_v=0.150 m/s, max_v=0.499 m/s
[component_container_isolated-17] [INFO] [1783327482.003152356] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-18] [WARN] [1783327482.243709274] [ObstacleDetectionNode]: input fps: 13.61, out fps: 14.23, infer time ms: 10, post process time ms: 6
[competition_master_stage3.py-20] [INFO] [1783327483.045331013] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.50,-1.14) yaw=-11deg cmd=(vx=0.41 wz=-1.22) elapsed=34.1s plan[30pts 6.2m] (1.48,-1.12)→(2.08,0.98) cpuFreq=1500MHz cpuT=72C bpuT=70C cpu=66% mem=18%
[component_container_isolated-17] [INFO] [1783327483.094325279] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327483.113978177] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327483.129961582] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327483.130172918] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327483.142358785] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-18] [WARN] [1783327483.278199267] [ObstacleDetectionNode]: input fps: 12.15, out fps: 11.61, infer time ms: 10, post process time ms: 7
[component_container_isolated-17] [WARN] [1783327483.841564178] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4318 Hz
[speed_profile_node.py-21] [INFO] [1783327483.860254359] [speed_profile_node]: Plan received: 29 poses, mean|κ|=1.6437 m⁻¹, max|κ|=3.6316 m⁻¹, mean_v=0.295 m/s, min_v=0.150 m/s, max_v=0.500 m/s
[component_container_isolated-17] [INFO] [1783327484.000772636] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-18] [WARN] [1783327484.315541215] [ObstacleDetectionNode]: input fps: 14.34, out fps: 14.45, infer time ms: 10, post process time ms: 5
[competition_master_stage3.py-20] [INFO] [1783327485.042662440] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.76,-1.48) yaw=-69deg cmd=(vx=0.50 wz=0.76) elapsed=36.1s plan[29pts 5.6m] (1.63,-1.27)→(2.08,0.98) cpuFreq=1500MHz cpuT=72C bpuT=70C cpu=60% mem=18%
[component_container_isolated-17] [INFO] [1783327485.094248270] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327485.124375935] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327485.154282639] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327485.154459849] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327485.181761945] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-18] [WARN] [1783327485.368147614] [ObstacleDetectionNode]: input fps: 11.96, out fps: 11.42, infer time ms: 10, post process time ms: 6
[hobot_codec_republish-13] [WARN] [1783327485.821565060] [vlm_jpeg_encoder]: Sub imgRaw fps [13.10]
[hobot_codec_republish-13] [WARN] [1783327485.827841787] [vlm_jpeg_encoder]: Pub img fps [13.09]
[component_container_isolated-17] [WARN] [1783327485.842949141] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.5485 Hz
[speed_profile_node.py-21] [INFO] [1783327485.863992177] [speed_profile_node]: Plan received: 26 poses, mean|κ|=2.2921 m⁻¹, max|κ|=4.4105 m⁻¹, mean_v=0.258 m/s, min_v=0.150 m/s, max_v=0.499 m/s
[component_container_isolated-17] [INFO] [1783327486.000732034] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-18] [WARN] [1783327486.371638052] [ObstacleDetectionNode]: input fps: 12.99, out fps: 13.97, infer time ms: 10, post process time ms: 8
[imu_madgwick_filter.py-4] [INFO] [1783327486.702465351] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1383 q_w=0.9738 angle=26.3deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1783327486.894190024] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2926 q_w=0.9018 angle=51.2deg beta=0.0030
[competition_master_stage3.py-20] [INFO] [1783327487.045644685] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.11,-2.01) yaw=-39deg cmd=(vx=0.36 wz=1.22) elapsed=38.1s plan[26pts 5.2m] (2.08,-2.02)→(2.08,0.98) cpuFreq=1500MHz cpuT=72C bpuT=70C cpu=100% mem=18%
[component_container_isolated-17] [INFO] [1783327487.094353359] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327487.110416888] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327487.123994893] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327487.124285271] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327487.138845410] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-18] [WARN] [1783327487.452522994] [ObstacleDetectionNode]: input fps: 13.18, out fps: 12.94, infer time ms: 10, post process time ms: 6
[component_container_isolated-17] [WARN] [1783327487.842140306] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3943 Hz
[speed_profile_node.py-21] [INFO] [1783327487.862696669] [speed_profile_node]: Plan received: 25 poses, mean|κ|=2.2277 m⁻¹, max|κ|=4.4105 m⁻¹, mean_v=0.259 m/s, min_v=0.150 m/s, max_v=0.499 m/s
[component_container_isolated-17] [INFO] [1783327488.000747281] [controller_server]: Passing new path to controller.
[component_container_isolated-17] [WARN] [1783327488.105543240] [controller_server]: Control loop missed its desired rate of 10.0000Hz
[racing_obstacle_detection_yolo-18] [WARN] [1783327488.511248360] [ObstacleDetectionNode]: input fps: 13.99, out fps: 11.36, infer time ms: 11, post process time ms: 8
[component_container_isolated-17] [WARN] [1783327488.902613677] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[competition_master_stage3.py-20] [INFO] [1783327489.046442340] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.98,-1.88) yaw=35deg cmd=(vx=0.23 wz=0.46) elapsed=40.1s plan[25pts 5.0m] (2.38,-2.17)→(2.08,0.98) cpuFreq=1500MHz cpuT=72C bpuT=70C cpu=88% mem=18%
[component_container_isolated-17] [INFO] [1783327489.094307670] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327489.107722381] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327489.127056399] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327489.127232984] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327489.140113106] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-18] [WARN] [1783327489.574570864] [ObstacleDetectionNode]: input fps: 10.63, out fps: 13.15, infer time ms: 11, post process time ms: 5
[component_container_isolated-17] [WARN] [1783327489.835761390] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4098 Hz
[speed_profile_node.py-21] [INFO] [1783327489.863556446] [speed_profile_node]: Plan received: 19 poses, mean|κ|=1.9534 m⁻¹, max|κ|=4.3744 m⁻¹, mean_v=0.278 m/s, min_v=0.150 m/s, max_v=0.500 m/s
[component_container_isolated-17] [INFO] [1783327490.000736835] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-18] [WARN] [1783327490.577924560] [ObstacleDetectionNode]: input fps: 13.40, out fps: 13.97, infer time ms: 10, post process time ms: 7
[hobot_codec_republish-13] [WARN] [1783327490.874595082] [vlm_jpeg_encoder]: Sub imgRaw fps [13.66]
[hobot_codec_republish-13] [WARN] [1783327490.880020384] [vlm_jpeg_encoder]: Pub img fps [13.66]
[competition_master_stage3.py-20] [INFO] [1783327491.065564184] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.10,-1.76) yaw=50deg cmd=(vx=0.44 wz=1.22) elapsed=42.1s plan[19pts 3.6m] (3.13,-1.72)→(2.08,0.98) cpuFreq=1500MHz cpuT=72C bpuT=70C cpu=86% mem=19%
[component_container_isolated-17] [INFO] [1783327491.095291423] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327491.115654574] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327491.126859180] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327491.127035390] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327491.140374141] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-18] [WARN] [1783327491.579198334] [ObstacleDetectionNode]: input fps: 13.97, out fps: 13.97, infer time ms: 11, post process time ms: 6
[component_container_isolated-17] [WARN] [1783327491.601973757] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-17] [WARN] [1783327491.701831368] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-17] [WARN] [1783327491.802405611] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-17] [WARN] [1783327491.835631426] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4401 Hz
[speed_profile_node.py-21] [INFO] [1783327491.858068055] [speed_profile_node]: Plan received: 18 poses, mean|κ|=2.0220 m⁻¹, max|κ|=4.6528 m⁻¹, mean_v=0.277 m/s, min_v=0.150 m/s, max_v=0.500 m/s
[component_container_isolated-17] [WARN] [1783327491.901748259] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-17] [INFO] [1783327492.000737821] [controller_server]: Passing new path to controller.
[component_container_isolated-17] [WARN] [1783327492.005393115] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-17] [WARN] [1783327492.101809566] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-17] [WARN] [1783327492.301748243] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-17] [WARN] [1783327492.401680519] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[racing_obstacle_detection_yolo-18] [WARN] [1783327492.655606830] [ObstacleDetectionNode]: input fps: 15.12, out fps: 14.87, infer time ms: 10, post process time ms: 6
[competition_master_stage3.py-20] [INFO] [1783327493.045355213] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.21,-1.24) yaw=100deg cmd=(vx=-0.29 wz=-1.22) elapsed=44.1s plan[18pts 3.3m] (3.13,-1.42)→(2.08,0.98) cpuFreq=1500MHz cpuT=72C bpuT=71C cpu=75% mem=18%
[component_container_isolated-17] [INFO] [1783327493.094572551] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327493.114136819] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327493.163955120] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327493.164137372] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327493.187245089] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-18] [WARN] [1783327493.709171123] [ObstacleDetectionNode]: input fps: 14.37, out fps: 13.31, infer time ms: 10, post process time ms: 7
[component_container_isolated-17] [WARN] [1783327493.834531218] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.5796 Hz
[speed_profile_node.py-21] [INFO] [1783327493.861754683] [speed_profile_node]: Plan received: 13 poses, mean|κ|=2.0153 m⁻¹, max|κ|=4.4760 m⁻¹, mean_v=0.271 m/s, min_v=0.150 m/s, max_v=0.396 m/s
[component_container_isolated-17] [INFO] [1783327494.000763615] [controller_server]: Passing new path to controller.
[component_container_isolated-17] [WARN] [1783327494.101390517] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[racing_obstacle_detection_yolo-18] [WARN] [1783327494.743721249] [ObstacleDetectionNode]: input fps: 10.21, out fps: 10.62, infer time ms: 10, post process time ms: 5
[competition_master_stage3.py-20] [INFO] [1783327495.048963319] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.16,-1.29) yaw=77deg cmd=(vx=0.37 wz=1.22) elapsed=46.1s plan[13pts 2.7m] (3.13,-1.12)→(2.08,0.98) cpuFreq=1500MHz cpuT=72C bpuT=71C cpu=71% mem=18%
[component_container_isolated-17] [INFO] [1783327495.094108157] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327495.112112367] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327495.131398714] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327495.131563174] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327495.149313424] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-18] [WARN] [1783327495.761146311] [ObstacleDetectionNode]: input fps: 12.51, out fps: 11.82, infer time ms: 10, post process time ms: 8
[component_container_isolated-17] [WARN] [1783327495.840156717] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4086 Hz
[hobot_codec_republish-13] [WARN] [1783327495.925754017] [vlm_jpeg_encoder]: Sub imgRaw fps [12.87]
[hobot_codec_republish-13] [WARN] [1783327495.931162859] [vlm_jpeg_encoder]: Pub img fps [12.87]
[component_container_isolated-17] [INFO] [1783327496.001245806] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-4] [INFO] [1783327496.703417145] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1577 q_w=0.2296 angle=153.5deg beta=0.0330
[racing_obstacle_detection_yolo-18] [WARN] [1783327496.762723365] [ObstacleDetectionNode]: input fps: 12.43, out fps: 12.97, infer time ms: 10, post process time ms: 7
[imu_madgwick_filter.py-6] [INFO] [1783327496.893945755] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3325 q_w=0.5161 angle=117.9deg beta=0.0030
[component_container_isolated-17] [WARN] [1783327497.001634759] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-17] [INFO] [1783327497.007068268] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327497.028765303] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327497.049627414] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327497.049824749] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327497.067265369] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-20] [INFO] [1783327497.069295222] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.78,-0.65) yaw=133deg cmd=(vx=0.41 wz=-0.86) elapsed=48.1s plan[13pts 2.7m] (3.13,-1.12)→(2.08,0.98) cpuFreq=1500MHz cpuT=72C bpuT=70C cpu=100% mem=19%
[component_container_isolated-17] [WARN] [1783327497.101603314] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-17] [WARN] [1783327497.201837746] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-17] [WARN] [1783327497.303076729] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-17] [WARN] [1783327497.401725396] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-17] [WARN] [1783327497.502560000] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-17] [WARN] [1783327497.601679005] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-17] [WARN] [1783327497.701728768] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[racing_obstacle_detection_yolo-18] [WARN] [1783327497.800208934] [ObstacleDetectionNode]: input fps: 11.68, out fps: 12.52, infer time ms: 15, post process time ms: 6
[component_container_isolated-17] [WARN] [1783327497.802833500] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-17] [WARN] [1783327497.831425932] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.2863 Hz
[speed_profile_node.py-21] [INFO] [1783327497.854047809] [speed_profile_node]: Plan received: 9 poses, mean|κ|=2.2539 m⁻¹, max|κ|=4.6657 m⁻¹, mean_v=0.277 m/s, min_v=0.150 m/s, max_v=0.500 m/s
[component_container_isolated-17] [WARN] [1783327497.901705669] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-17] [INFO] [1783327498.000743548] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-18] [WARN] [1783327498.853030117] [ObstacleDetectionNode]: input fps: 13.81, out fps: 13.30, infer time ms: 10, post process time ms: 5
[component_container_isolated-17] [INFO] [1783327499.007285255] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327499.039616304] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327499.062958645] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327499.063206147] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327499.071938770] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-20] [INFO] [1783327499.074920672] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.63,-0.41) yaw=97deg cmd=(vx=0.50 wz=0.26) elapsed=50.1s plan[9pts 1.8m] (2.68,-0.37)→(2.08,0.98) cpuFreq=1500MHz cpuT=73C bpuT=71C cpu=100% mem=19%
[component_container_isolated-17] [WARN] [1783327499.837775558] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.3463 Hz
[speed_profile_node.py-21] [INFO] [1783327499.851637019] [speed_profile_node]: Plan received: 6 poses, mean|κ|=2.8574 m⁻¹, max|κ|=4.4270 m⁻¹, mean_v=0.232 m/s, min_v=0.150 m/s, max_v=0.436 m/s
[racing_obstacle_detection_yolo-18] [WARN] [1783327499.887262099] [ObstacleDetectionNode]: input fps: 13.06, out fps: 13.54, infer time ms: 10, post process time ms: 5
[component_container_isolated-17] [INFO] [1783327500.000738231] [controller_server]: Passing new path to controller.
[component_container_isolated-17] [INFO] [1783327500.801810907] [controller_server]: Reached the goal!
[hobot_codec_republish-13] [WARN] [1783327500.968008814] [vlm_jpeg_encoder]: Sub imgRaw fps [13.09]
[hobot_codec_republish-13] [WARN] [1783327500.970652297] [vlm_jpeg_encoder]: Pub img fps [13.10]
[racing_obstacle_detection_yolo-18] [WARN] [1783327501.009231236] [ObstacleDetectionNode]: input fps: 14.87, out fps: 12.52, infer time ms: 10, post process time ms: 9
[competition_master_stage3.py-20] [INFO] [1783327501.044326309] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.38,0.57) yaw=127deg cmd=(vx=0.05 wz=0.00) elapsed=52.1s plan[6pts 1.1m] (2.53,0.23)→(2.08,0.98) cpuFreq=1500MHz cpuT=72C bpuT=71C cpu=88% mem=19%
[component_container_isolated-17] [INFO] [1783327501.094230476] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-17] [INFO] [1783327501.108435773] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327501.128904461] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327501.129196630] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327501.148336515] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [ERROR] [1783327501.698020984] [bt_navigator_navigate_through_poses_rclcpp_node]: Failed to get result for compute_path_through_poses in node halt!
[component_container_isolated-17] [WARN] [1783327501.699401372] [BehaviorTreeEngine]: Behavior Tree tick rate 10.00 was exceeded!
[component_container_isolated-17] [INFO] [1783327501.700324672] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-20] [INFO] [1783327501.726214410] [competition_master_stage3]: [结果回调] 巡航完成, 触发VLM推理...
[competition_master_stage3.py-20] [INFO] [1783327501.736665423] [competition_master_stage3]: [VLM] 发布 sign4return=100, 拍照推理中...
[vision_ai_node-12] [INFO] [1783327501.742256224] [vision_ai_node]: Received sign4return: 100
[competition_master_stage3.py-20] [INFO] [1783327501.743439652] [competition_master_stage3]: [状态机] CRUISE_CHANNEL → RETURN_P
[competition_master_stage3.py-20] [INFO] [1783327501.754985633] [competition_master_stage3]: [RETURN] NavigateThroughPoses: 7路点 (0.94,-0.09)→(-1.99,-0.01) (共识中心线, std=0.19m)
[component_container_isolated-17] [INFO] [1783327501.767378163] [bt_navigator]: Begin navigating from current location through 7 poses to (-1.99, -0.01)
[component_container_isolated-17] [INFO] [1783327501.768415631] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[competition_master_stage3.py-20] [INFO] [1783327501.781312542] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[component_container_isolated-17] [INFO] [1783327501.781597128] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-17] [INFO] [1783327501.791631636] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-17] [INFO] [1783327501.791783179] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-17] [WARN] [1783327501.825413114] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-17] [WARN] [1783327501.833423062] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 1.4214 Hz
[speed_profile_node.py-21] [INFO] [1783327501.842384353] [speed_profile_node]: Plan received: 3 poses, mean|κ|=6.6328 m⁻¹, max|κ|=6.6328 m⁻¹, mean_v=0.150 m/s, min_v=0.150 m/s, max_v=0.150 m/s
[racing_obstacle_detection_yolo-18] [WARN] [1783327502.032991979] [ObstacleDetectionNode]: input fps: 12.28, out fps: 14.62, infer time ms: 10, post process time ms: 5
[component_container_isolated-17] [INFO] [1783327502.069162061] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-17] [INFO] [1783327502.074068773] [controller_server]: Reached the goal!
[component_container_isolated-17] [INFO] [1783327502.468282219] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-20] [INFO] [1783327502.489572248] [competition_master_stage3]: [结果回调] 返航完成, 已回到P点!
[racing_obstacle_detection_yolo-18] [WARN] [1783327503.039714040] [ObstacleDetectionNode]: input fps: 14.31, out fps: 13.93, infer time ms: 10, post process time ms: 7
[competition_master_stage3.py-20] [INFO] [1783327503.315078015] [competition_master_stage3]: [BAG] 录制已停止
[competition_master_stage3.py-20] [INFO] [1783327503.321753243] [competition_master_stage3]: [状态机] RETURN_P → DONE
[competition_master_stage3.py-20] [INFO] [1783327503.332590133] [competition_master_stage3]:
[competition_master_stage3.py-20] [INFO] [1783327503.338578938] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-20] [INFO] [1783327503.344832454] [competition_master_stage3]: >>> [Stage 3] 任务结束 <<<
[competition_master_stage3.py-20] [INFO] [1783327503.348052400] [competition_master_stage3]:   最终状态: DONE
[competition_master_stage3.py-20] [INFO] [1783327503.351068761] [competition_master_stage3]:   总耗时:   54.4s
[competition_master_stage3.py-20] [INFO] [1783327503.354846962] [competition_master_stage3]:   --- 各阶段耗时 ---
[competition_master_stage3.py-20] [INFO] [1783327503.361601357] [competition_master_stage3]:   LAUNCH................ 21.8s
[competition_master_stage3.py-20] [INFO] [1783327503.364504842] [competition_master_stage3]:   NAV_TO_QR............. 14.5s
[competition_master_stage3.py-20] [INFO] [1783327503.369020300] [competition_master_stage3]:   BACKING_UP............ 6.0s
[competition_master_stage3.py-20] [INFO] [1783327503.371797492] [competition_master_stage3]:   CRUISE_CHANNEL........ 32.3s
[competition_master_stage3.py-20] [INFO] [1783327503.374093929] [competition_master_stage3]:   RETURN_P.............. 1.6s
[competition_master_stage3.py-20] [INFO] [1783327503.377125707] [competition_master_stage3]:   (transition/overhead). -21.8s
[competition_master_stage3.py-20] [INFO] [1783327503.380346862] [competition_master_stage3]:   --- ---
[competition_master_stage3.py-20] [INFO] [1783327503.384861069] [competition_master_stage3]:   QR 原始数据: 1584
[competition_master_stage3.py-20] [INFO] [1783327503.396966138] [competition_master_stage3]:   QR 方向:   逆时针 (CW=顺时针/odd, CCW=逆时针/even)
[competition_master_stage3.py-20] [WARN] [1783327503.404708751] [competition_master_stage3]:   VLM 结果:  未收到
[competition_master_stage3.py-20] [INFO] [1783327503.412181027] [competition_master_stage3]:   超时限制:  180.0s (全局)
[competition_master_stage3.py-20] [INFO] [1783327503.421227735] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-20] [INFO] [1783327503.431112492] [competition_master_stage3]: [TRAJ] CSV已保存: /userdata/dev_ws/trajectory_20260706_164503.csv (69 点)
[competition_master_stage3.py-20] [INFO] [1783327503.869369456] [competition_master_stage3]: [TRAJ] Nav2 params snapshot: 31 keys
[competition_master_stage3.py-20] [INFO] [1783327503.873937915] [competition_master_stage3]: [TRAJ] 摘要JSON已保存: /userdata/dev_ws/trajectory_20260706_164503_summary.json
[competition_master_stage3.py-20] [INFO] [1783327503.878912585] [competition_master_stage3]: [TRAJ] 规划历史已保存: /userdata/dev_ws/trajectory_20260706_164503_plans.csv (23 次规划)
[competition_master_stage3.py-20] [INFO] [1783327503.899817235] [competition_master_stage3]: [TRAJ] costmap PGM已保存: /userdata/dev_ws/trajectory_20260706_164503_costmap.pgm
[competition_master_stage3.py-20] [INFO] [1783327503.931023937] [competition_master_stage3]: [DIAG] state=DONE pos=(2.22,0.77) yaw=117deg cmd=(vx=0.00 wz=0.00) elapsed=55.0s plan[3pts 0.4m] (2.23,0.98)→(2.08,0.98) cpuFreq=1500MHz cpuT=73C bpuT=71C cpu=77% mem=18%
[racing_obstacle_detection_yolo-18] [WARN] [1783327504.056828460] [ObstacleDetectionNode]: input fps: 12.81, out fps: 12.83, infer time ms: 10, post process time ms: 10
[competition_master_stage3.py-20] [INFO] [1783327505.050544808] [competition_master_stage3]: [DIAG] state=DONE pos=(2.22,0.77) yaw=117deg cmd=(vx=0.00 wz=0.00) elapsed=56.1s plan[3pts 0.4m] (2.23,0.98)→(2.08,0.98) cpuFreq=1500MHz cpuT=73C bpuT=71C cpu=66% mem=18%
[racing_obstacle_detection_yolo-18] [WARN] [1783327505.146128218] [ObstacleDetectionNode]: input fps: 13.35, out fps: 12.81, infer time ms: 10, post process time ms: 5
[hobot_codec_republish-13] [WARN] [1783327506.011858711] [vlm_jpeg_encoder]: Sub imgRaw fps [13.68]
[hobot_codec_republish-13] [WARN] [1783327506.014409068] [vlm_jpeg_encoder]: Pub img fps [13.68]
[racing_obstacle_detection_yolo-18] [WARN] [1783327506.184432817] [ObstacleDetectionNode]: input fps: 12.60, out fps: 13.49, infer time ms: 10, post process time ms: 5
[imu_madgwick_filter.py-4] [INFO] [1783327506.701922049] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1774 q_w=0.3771 angle=135.7deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1783327506.899480839] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3736 q_w=0.6466 angle=99.4deg beta=0.0030
[competition_master_stage3.py-20] [INFO] [1783327507.040540492] [competition_master_stage3]: [DIAG] state=DONE pos=(2.22,0.77) yaw=117deg cmd=(vx=0.00 wz=0.00) elapsed=58.1s plan[3pts 0.4m] (2.23,0.98)→(2.08,0.98) cpuFreq=1500MHz cpuT=72C bpuT=71C cpu=42% mem=18%
[racing_obstacle_detection_yolo-18] [WARN] [1783327507.254767970] [ObstacleDetectionNode]: input fps: 13.00, out fps: 11.23, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-18] [WARN] [1783327508.284607061] [ObstacleDetectionNode]: input fps: 12.71, out fps: 14.56, infer time ms: 10, post process time ms: 5
[competition_master_stage3.py-20] [INFO] [1783327509.046759304] [competition_master_stage3]: [DIAG] state=DONE pos=(2.22,0.77) yaw=117deg cmd=(vx=0.00 wz=0.00) elapsed=60.1s plan[3pts 0.4m] (2.23,0.98)→(2.08,0.98) cpuFreq=1500MHz cpuT=72C bpuT=71C cpu=100% mem=18%
[racing_obstacle_detection_yolo-18] [WARN] [1783327509.327480910] [ObstacleDetectionNode]: input fps: 12.43, out fps: 12.48, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-18] [WARN] [1783327510.366303820] [ObstacleDetectionNode]: input fps: 14.56, out fps: 14.45, infer time ms: 10, post process time ms: 6
[hobot_codec_republish-13] [WARN] [1783327511.035378565] [vlm_jpeg_encoder]: Sub imgRaw fps [13.54]
[hobot_codec_republish-13] [WARN] [1783327511.038610594] [vlm_jpeg_encoder]: Pub img fps [13.54]
[competition_master_stage3.py-20] [INFO] [1783327511.043483013] [competition_master_stage3]: [DIAG] state=DONE pos=(2.22,0.77) yaw=117deg cmd=(vx=0.00 wz=0.00) elapsed=62.1s plan[3pts 0.4m] (2.23,0.98)→(2.08,0.98) cpuFreq=1500MHz cpuT=73C bpuT=71C cpu=80% mem=18%
[racing_obstacle_detection_yolo-18] [WARN] [1783327511.374556930] [ObstacleDetectionNode]: input fps: 14.35, out fps: 13.89, infer time ms: 10, post process time ms: 5
[racing_obstacle_detection_yolo-18] [WARN] [1783327512.469229659] [ObstacleDetectionNode]: input fps: 12.22, out fps: 11.88, infer time ms: 10, post process time ms: 5
[competition_master_stage3.py-20] [INFO] [1783327513.041287631] [competition_master_stage3]: [DIAG] state=DONE pos=(2.22,0.77) yaw=117deg cmd=(vx=0.00 wz=0.00) elapsed=64.1s plan[3pts 0.4m] (2.23,0.98)→(2.08,0.98) cpuFreq=1500MHz cpuT=73C bpuT=71C cpu=57% mem=18%
[racing_obstacle_detection_yolo-18] [WARN] [1783327513.529600220] [ObstacleDetectionNode]: input fps: 13.49, out fps: 14.15, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-18] [WARN] [1783327514.550249985] [ObstacleDetectionNode]: input fps: 13.65, out fps: 13.74, infer time ms: 10, post process time ms: 6
[competition_master_stage3.py-20] [INFO] [1783327515.039868698] [competition_master_stage3]: [DIAG] state=DONE pos=(2.22,0.77) yaw=117deg cmd=(vx=0.00 wz=0.00) elapsed=66.1s plan[3pts 0.4m] (2.23,0.98)→(2.08,0.98) cpuFreq=1500MHz cpuT=73C bpuT=71C cpu=50% mem=18%
[racing_obstacle_detection_yolo-18] [WARN] [1783327515.576283896] [ObstacleDetectionNode]: input fps: 14.58, out fps: 14.63, infer time ms: 10, post process time ms: 7
[hobot_codec_republish-13] [WARN] [1783327516.051953140] [vlm_jpeg_encoder]: Sub imgRaw fps [13.56]
[hobot_codec_republish-13] [WARN] [1783327516.059133828] [vlm_jpeg_encoder]: Pub img fps [13.55]
[racing_obstacle_detection_yolo-18] [WARN] [1783327516.643970774] [ObstacleDetectionNode]: input fps: 13.73, out fps: 13.11, infer time ms: 10, post process time ms: 5
[imu_madgwick_filter.py-4] [INFO] [1783327516.702171162] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1974 q_w=0.3417 angle=140.0deg beta=0.0330
[imu_madgwick_filter.py-6] [INFO] [1783327516.895067653] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4204 q_w=0.6470 angle=99.4deg beta=0.0030
[competition_master_stage3.py-20] [INFO] [1783327517.046866990] [competition_master_stage3]: [DIAG] state=DONE pos=(2.22,0.77) yaw=117deg cmd=(vx=0.00 wz=0.00) elapsed=68.1s plan[3pts 0.4m] (2.23,0.98)→(2.08,0.98) cpuFreq=1500MHz cpuT=73C bpuT=71C cpu=100% mem=18%
[racing_obstacle_detection_yolo-18] [WARN] [1783327517.715525366] [ObstacleDetectionNode]: input fps: 13.73, out fps: 14.01, infer time ms: 10, post process time ms: 5
^C[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[rviz2-22] [INFO] [1783327517.788033503] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [origincar_base_node-1]: process has died [pid 6957, exit code -6, cmd '/userdata/dev_ws/install/origincar_base/lib/origincar_base/origincar_base_node --ros-args --params-file /tmp/launch_params_v_4ol_hi --params-file /tmp/launch_params_mbkcj2ni'].
[ERROR] [lslidar_driver_node-2]: process has died [pid 6959, exit code -6, cmd '/userdata/dev_ws/install/lslidar_driver/lib/lslidar_driver/lslidar_driver_node --ros-args -r __node:=lslidar_driver_node --params-file /userdata/dev_ws/install/lslidar_driver/share/lslidar_driver/params/lsx10.yaml'].
[INFO] [lifecycle_manager-16]: process has finished cleanly [pid 7127]
[INFO] [robot_state_publisher-3]: process has finished cleanly [pid 6961]
[ERROR] [rviz2-22]: process has died [pid 7303, exit code -11, cmd '/opt/ros/humble/lib/rviz2/rviz2 -d /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/rviz/nav.rviz --ros-args -r __node:=rviz2'].
[INFO] [ekf_node-7]: process has finished cleanly [pid 6969]
[INFO] [map_server-14]: process has finished cleanly [pid 7117]
[INFO] [static_transform_publisher-8]: process has finished cleanly [pid 7017]
[INFO] [costmap_filter_info_server-15]: process has finished cleanly [pid 7119]
[INFO] [hobot_codec_republish-13]: process has finished cleanly [pid 7027]
[INFO] [imu_madgwick_filter.py-4]: process has finished cleanly [pid 6963]
[INFO] [bmi088_iio_bridge.py-5]: process has finished cleanly [pid 6965]
[lifecycle_manager-16] [INFO] [1783327517.788103462] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-16] [INFO] [1783327517.788377298] [lifecycle_manager_keepout]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_keepout)
[lifecycle_manager-16] [INFO] [1783327517.788558883] [lifecycle_manager_keepout]: Terminating bond timer...
[static_transform_publisher-8] [INFO] [1783327517.788234421] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[robot_state_publisher-3] [INFO] [1783327517.788243088] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-17] [INFO] [1783327517.788389673] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-17] [INFO] [1783327517.788523216] [lifecycle_manager_navigation]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_navigation)
[component_container_isolated-17] [INFO] [1783327517.788831385] [lifecycle_manager_navigation]: Terminating bond timer...
[aurora930_node-9] [INFO] [1783327517.788825177] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1783327517.789123554] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-14] [INFO] [1783327517.793666761] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-14] [INFO] [1783327517.793993014] [keepout_mask_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_mask_server)
[map_server-14] [INFO] [1783327517.794273599] [keepout_mask_server]: Deactivating
[map_server-14] [INFO] [1783327517.802785341] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[map_server-14] [INFO] [1783327517.816942507] [keepout_mask_server]: Cleaning up
[map_server-14] [INFO] [1783327517.817202759] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[map_server-14] [INFO] [1783327518.040756223] [keepout_mask_server]: Destroying
[competition_master_stage3.py-20] [INFO] [1783327517.864851386] [competition_master_stage3]: [MAIN] 收到 Ctrl+C, 停止录制 + 保存轨迹...
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.868837338] [competition_master_stage3]:
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.872296452] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.875285520] [competition_master_stage3]: >>> [Stage 3] 任务结束 <<<
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.881964578] [competition_master_stage3]:   最终状态: DONE
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.889209100] [competition_master_stage3]:   总耗时:   68.9s
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.895596406] [competition_master_stage3]:   --- 各阶段耗时 ---
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.901612626] [competition_master_stage3]:   LAUNCH................ 21.8s
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.907205883] [competition_master_stage3]:   NAV_TO_QR............. 14.5s
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.916794718] [competition_master_stage3]:   BACKING_UP............ 6.0s
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.922521310] [competition_master_stage3]:   CRUISE_CHANNEL........ 32.3s
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.929141576] [competition_master_stage3]:   RETURN_P.............. 1.6s
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.934398039] [competition_master_stage3]:   (transition/overhead). -7.3s
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.938967038] [competition_master_stage3]:   --- ---
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.944261959] [competition_master_stage3]:   QR 原始数据: 1584
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.949783133] [competition_master_stage3]:   QR 方向:   逆时针 (CW=顺时针/odd, CCW=逆时针/even)
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [WARN] [1783327517.955979895] [competition_master_stage3]:   VLM 结果:  未收到
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.961182858] [competition_master_stage3]:   超时限制:  180.0s (全局)
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.964423845] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327517.968770049] [competition_master_stage3]: [CPU] governor → schedutil
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[origincar_base_node-1] [INFO] [1783327517.796946956] [origincar_base]: Stop command sent to STM32 on shutdown.
[origincar_base_node-1] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[origincar_base_node-1] terminate called after throwing an instance of 'rclcpp::exceptions::RCLError'
[origincar_base_node-1]   what():  failed to create guard condition: the given context is not valid, either rcl_init() was not called or rcl_shutdown() was called., at ./src/rcl/guard_condition.c:67
[costmap_filter_info_server-15] [INFO] [1783327517.797014624] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-15] [INFO] [1783327517.799473562] [keepout_filter_info_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_filter_info_server)
[costmap_filter_info_server-15] [INFO] [1783327517.799875065] [keepout_filter_info_server]: Deactivating
[costmap_filter_info_server-15] [INFO] [1783327517.799997358] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-15] [INFO] [1783327517.845250214] [keepout_filter_info_server]: Cleaning up
[costmap_filter_info_server-15] [INFO] [1783327517.845480216] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-15] [INFO] [1783327517.939489501] [keepout_filter_info_server]: Destroying
[ekf_node-7] [INFO] [1783327517.807071212] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[aurora930_node-9] I0706 16:45:17.857283  7019 ros2_node.cc:90] process quit succeed
[aurora930_node-9] I0706 16:45:17.857532  7019 aurora900_ros2_device.cc:83] begin stop()
[aurora930_node-9] I0706 16:45:17.859107  7019 aurora900_ros2_device.cc:103] stop stream
[aurora930_node-9] 2026-07-06 16:45:17.911 ( 102.268s) [        A8FA4020]      aurora900_impl.cc:648   INFO| ir_stream_count_=0, rgb_stream_count_=0, depth_stream_count_=0
[aurora930_node-9] 2026-07-06 16:45:17.911 ( 102.268s) [        A8FA4020]      aurora900_impl.cc:649   INFO| mask=7
[aurora930_node-9] I0706 16:45:18.066936  7019 aurora900_ros2_device.cc:105] destroy stream
[aurora930_node-9] I0706 16:45:18.067252  7019 aurora900_ros2_device.cc:110] close glog
[aurora930_node-9] WARNING: Logging before InitGoogleLogging() is written to STDERR
[aurora930_node-9] I0706 16:45:18.067426  7019 ros2_device.cc:113] close device...
[aurora930_node-9] 2026-07-06 16:45:18.564 ( 102.921s) [        891D37E0]         cmd_backend.cc:40    INFO| RunBlocking is end!!!
[aurora930_node-9] 2026-07-06 16:45:18.765 ( 103.122s) [        A8FA4020]deptrum_camera_vendor.c:121   INFO| device is close.
[aurora930_node-9] I0706 16:45:18.767623  7019 ros2_device.cc:116] quit succeed
[component_container_isolated-17] [INFO] [1783327518.060233394] [local_costmap.local_costmap]: Message Filter dropping message: frame 'laser_link' at time 1783327517.756 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-17] [INFO] [1783327518.379828986] [waypoint_follower]: Running Nav2 LifecycleNode rcl preshutdown (waypoint_follower)
[component_container_isolated-17] [INFO] [1783327518.380218698] [waypoint_follower]: Deactivating
[component_container_isolated-17] [INFO] [1783327518.380383949] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327518.391435463] [waypoint_follower]: Cleaning up
[component_container_isolated-17] [INFO] [1783327518.451933909] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327518.452116744] [behavior_server]: Running Nav2 LifecycleNode rcl preshutdown (behavior_server)
[component_container_isolated-17] [INFO] [1783327518.452301038] [behavior_server]: Deactivating
[component_container_isolated-17] [INFO] [1783327518.453137503] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327518.463615095] [behavior_server]: Cleaning up
[component_container_isolated-17] [INFO] [1783327518.516844395] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327518.517016188] [lifecycle_manager_localization]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_localization)
[component_container_isolated-17] [INFO] [1783327518.517093064] [lifecycle_manager_localization]: Terminating bond timer...
[component_container_isolated-17] [INFO] [1783327518.599204575] [velocity_smoother]: Running Nav2 LifecycleNode rcl preshutdown (velocity_smoother)
[component_container_isolated-17] [INFO] [1783327518.599632745] [velocity_smoother]: Deactivating
[component_container_isolated-17] [INFO] [1783327518.599900498] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327518.610392798] [velocity_smoother]: Cleaning up
[component_container_isolated-17] [INFO] [1783327518.610712176] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327518.610844135] [amcl]: Running Nav2 LifecycleNode rcl preshutdown (amcl)
[component_container_isolated-17] [INFO] [1783327518.611748643] [amcl]: Deactivating
[component_container_isolated-17] [INFO] [1783327518.611993645] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327518.622604905] [amcl]: Cleaning up
[component_container_isolated-17] [INFO] [1783327518.677586012] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327518.677720138] [bt_navigator]: Running Nav2 LifecycleNode rcl preshutdown (bt_navigator)
[component_container_isolated-17] [INFO] [1783327518.677834222] [bt_navigator]: Deactivating
[component_container_isolated-17] [INFO] [1783327518.677994765] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327518.688597025] [bt_navigator]: Cleaning up
[component_container_isolated-17] [INFO] [1783327519.244344848] [bt_navigator]: Completed Cleaning up
[component_container_isolated-17] [INFO] [1783327519.244803727] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327519.244895727] [planner_server]: Running Nav2 LifecycleNode rcl preshutdown (planner_server)
[component_container_isolated-17] [INFO] [1783327519.245023604] [planner_server]: Deactivating
[component_container_isolated-17] [INFO] [1783327519.245272731] [global_costmap.global_costmap]: Deactivating
[lifecycle_manager-16] [INFO] [1783327518.078367136] [lifecycle_manager_keepout]: Destroying lifecycle_manager_keepout
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
[competition_master_stage3.py-20] [INFO] [1783327517.974299848] [competition_master_stage3]: [TRAJ] CSV已保存: /userdata/dev_ws/trajectory_20260706_164517.csv (70 点)
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327518.435036720] [competition_master_stage3]: [TRAJ] Nav2 params snapshot: 31 keys
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327518.442051698] [competition_master_stage3]: [TRAJ] 摘要JSON已保存: /userdata/dev_ws/trajectory_20260706_164517_summary.json
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327518.447386786] [competition_master_stage3]: [TRAJ] 规划历史已保存: /userdata/dev_ws/trajectory_20260706_164517_plans.csv (23 次规划)
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-20] [INFO] [1783327518.467945425] [competition_master_stage3]: [TRAJ] costmap PGM已保存: /userdata/dev_ws/trajectory_20260706_164517_costmap.pgm
[competition_master_stage3.py-20] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[speed_profile_node.py-21] Traceback (most recent call last):
[speed_profile_node.py-21]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/speed_profile_node.py", line 394, in <module>
[speed_profile_node.py-21]     main()
[speed_profile_node.py-21]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/speed_profile_node.py", line 390, in main
[speed_profile_node.py-21]     rclpy.shutdown()
[speed_profile_node.py-21]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 130, in shutdown
[speed_profile_node.py-21]     _shutdown(context=context)
[speed_profile_node.py-21]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/utilities.py", line 58, in shutdown
[speed_profile_node.py-21]     return context.shutdown()
[speed_profile_node.py-21]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/context.py", line 102, in shutdown
[speed_profile_node.py-21]     self.__context.shutdown()
[speed_profile_node.py-21] rclpy._rclpy_pybind11.RCLError: failed to shutdown: rcl_shutdown already called on the given context, at ./src/rcl/init.c:241
[yolo_costmap_bridge.py-19] Traceback (most recent call last):
[yolo_costmap_bridge.py-19]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/yolo_costmap_bridge.py", line 156, in <module>
[yolo_costmap_bridge.py-19]     main()
[yolo_costmap_bridge.py-19]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/yolo_costmap_bridge.py", line 152, in main
[yolo_costmap_bridge.py-19]     rclpy.shutdown()
[yolo_costmap_bridge.py-19]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 130, in shutdown
[yolo_costmap_bridge.py-19]     _shutdown(context=context)
[yolo_costmap_bridge.py-19]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/utilities.py", line 58, in shutdown
[yolo_costmap_bridge.py-19]     return context.shutdown()
[yolo_costmap_bridge.py-19]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/context.py", line 102, in shutdown
[yolo_costmap_bridge.py-19]     self.__context.shutdown()
[yolo_costmap_bridge.py-19] rclpy._rclpy_pybind11.RCLError: failed to shutdown: rcl_shutdown already called on the given context, at ./src/rcl/init.c:241
[INFO] [imu_madgwick_filter.py-6]: process has finished cleanly [pid 6967]
[ERROR] [speed_profile_node.py-21]: process has died [pid 7301, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/speed_profile_node.py --ros-args -r __node:=speed_profile_node --params-file /tmp/launch_params_8f2l5mcj'].
[ERROR] [yolo_costmap_bridge.py-19]: process has died [pid 7290, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/yolo_costmap_bridge.py --ros-args -r __node:=yolo_costmap_bridge'].
[component_container_isolated-17] [INFO] [1783327519.822239731] [planner_server]: Deactivating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-17] [INFO] [1783327519.822583484] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327519.833043950] [planner_server]: Cleaning up
[component_container_isolated-17] [INFO] [1783327519.852911624] [global_costmap.global_costmap]: Cleaning up
[component_container_isolated-17] [INFO] [1783327519.862873878] [planner_server]: Cleaning up plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-17] [INFO] [1783327519.864369016] [planner_server]: Destroying plugin GridBased of type SmacPlannerHybrid
[INFO] [aurora930_node-9]: process has finished cleanly [pid 7019]
[INFO] [competition_master_stage3.py-20]: process has finished cleanly [pid 7299]
[INFO] [racing_obstacle_detection_yolo-18]: process has finished cleanly [pid 7288]
[ERROR] [vision_ai_node-12]: process has died [pid 7025, exit code 1, cmd '/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node --ros-args -r __node:=vision_ai_node'].
[component_container_isolated-17] [INFO] [1783327520.885719920] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327520.885873880] [smoother_server]: Running Nav2 LifecycleNode rcl preshutdown (smoother_server)
[component_container_isolated-17] [INFO] [1783327520.885985631] [smoother_server]: Deactivating
[component_container_isolated-17] [INFO] [1783327520.886039089] [smoother_server]: Deactivating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-17] [INFO] [1783327520.886174216] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327520.896775475] [smoother_server]: Cleaning up
[component_container_isolated-17] [INFO] [1783327520.897046227] [smoother_server]: Cleaning up smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-17] [INFO] [1783327520.915206552] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327520.915333845] [map_server]: Running Nav2 LifecycleNode rcl preshutdown (map_server)
[component_container_isolated-17] [INFO] [1783327520.915563347] [map_server]: Deactivating
[component_container_isolated-17] [INFO] [1783327520.915718348] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327520.926203856] [map_server]: Cleaning up
[component_container_isolated-17] [INFO] [1783327520.926402733] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327520.926463775] [controller_server]: Running Nav2 LifecycleNode rcl preshutdown (controller_server)
[component_container_isolated-17] [INFO] [1783327520.926565818] [controller_server]: Deactivating
[component_container_isolated-17] [INFO] [1783327520.926626026] [controller_server]: Deactivating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-17] [INFO] [1783327520.926800695] [local_costmap.local_costmap]: Deactivating
[component_container_isolated-17] [INFO] [1783327520.934967807] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[component_container_isolated-17] [INFO] [1783327520.945422023] [controller_server]: Cleaning up
[component_container_isolated-17] [INFO] [1783327520.945575900] [controller_server]: Cleaning up controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-17] [INFO] [1783327520.945923820] [local_costmap.local_costmap]: Cleaning up
[component_container_isolated-17] [INFO] [1783327521.985008893] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[ERROR] [component_container_isolated-17]: process[component_container_isolated-17] failed to terminate '5' seconds after receiving 'SIGINT', escalating to 'SIGTERM'
[INFO] [component_container_isolated-17]: sending signal 'SIGTERM' to process[component_container_isolated-17]
[component_container_isolated-17] [INFO] [1783327524.378120882] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [component_container_isolated-17]: process[component_container_isolated-17] failed to terminate '10.0' seconds after receiving 'SIGTERM', escalating to 'SIGKILL'
[INFO] [component_container_isolated-17]: sending signal 'SIGKILL' to process[component_container_isolated-17]
[ERROR] [component_container_isolated-17]: process has died [pid 7284, exit code -9, cmd '/opt/ros/humble/lib/rclcpp_components/component_container_isolated --ros-args --log-level info --ros-args -r __node:=nav2_container --params-file /tmp/launch_params_dp9klkzk --params-file /tmp/launch_params_tl4592uh -r /tf:=tf -r /tf_static:=tf_static'].
root@ubuntu:/userdata/dev_ws#
