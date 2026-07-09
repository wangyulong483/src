root@ubuntu:/userdata/dev_ws# ros2 launch origincar_bringup stage3_bringup.launch.py
[INFO] [launch]: All log files can be found below /root/.ros/log/2026-07-08-19-59-58-181404-ubuntu-5569
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [origincar_base_node-1]: process started with pid [5590]
[INFO] [lslidar_driver_node-2]: process started with pid [5592]
[INFO] [robot_state_publisher-3]: process started with pid [5594]
[INFO] [imu_madgwick_filter.py-4]: process started with pid [5596]
[INFO] [bmi088_iio_bridge.py-5]: process started with pid [5598]
[INFO] [imu_madgwick_filter.py-6]: process started with pid [5600]
[INFO] [ekf_node-7]: process started with pid [5602]
[INFO] [static_transform_publisher-8]: process started with pid [5637]
[INFO] [aurora930_node-9]: process started with pid [5640]
[INFO] [qr_decoder-10]: process started with pid [5642]
[INFO] [qr_decision.py-11]: process started with pid [5644]
[INFO] [vision_ai_node-12]: process started with pid [5648]
[INFO] [hobot_codec_republish-13]: process started with pid [5650]
[lslidar_driver_node-2] [INFO] [1783511999.095612415] [lslidar_driver_node]: Lidar is N10
[lslidar_driver_node-2] [INFO] [1783511999.137485316] [lslidar_driver_node]: Initialised lslidar without error
[lslidar_driver_node-2] [INFO] [1783511999.137989153] [lslidar_driver_node]: Successfully initialize driver...
[robot_state_publisher-3] [WARN] [1783511999.083842922] [robot_state_publisher]: No robot_description parameter, but command-line argument available.  Assuming argument is name of URDF file.  This backwards compatibility fallback will be removed in the future.
[robot_state_publisher-3] [INFO] [1783511999.167036530] [robot_state_publisher]: got segment base_footprint
[robot_state_publisher-3] [INFO] [1783511999.178838665] [robot_state_publisher]: got segment base_link
[robot_state_publisher-3] [INFO] [1783511999.179036389] [robot_state_publisher]: got segment gyro_link
[robot_state_publisher-3] [INFO] [1783511999.179099713] [robot_state_publisher]: got segment laser_link
[origincar_base_node-1] [INFO] [1783511999.206102188] [origincar_base]: origincar_base serial port opened
[static_transform_publisher-8] [INFO] [1783511999.290071228] [depth_camera_tf]: Spinning until stopped - publishing transform
[static_transform_publisher-8] translation: ('0.140000', '0.000000', '0.050000')
[static_transform_publisher-8] rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
[static_transform_publisher-8] from 'base_link' to 'depth_camera_link'
[hobot_codec_republish-13] [WARN] [1783511999.369069563] [vlm_jpeg_encoder]: Parameters:
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
[hobot_codec_republish-13] [WARN] [1783511999.425244021] [HobotCodecImpl]: platform x5
[ekf_node-7] Both imu1_differential and imu1_relative were set to true. Using differential mode.
[INFO] [map_server-14]: process started with pid [5722]
[INFO] [map_server-15]: process started with pid [5724]
[INFO] [costmap_filter_info_server-16]: process started with pid [5726]
[INFO] [lifecycle_manager-17]: process started with pid [5728]
[costmap_filter_info_server-16] [INFO] [1783512000.353403298] [costmap_filter_info_server]: This is costmap filter info publisher
[lifecycle_manager-17] [INFO] [1783512000.362297306] [lifecycle_manager_keepout]: Creating
[lifecycle_manager-17] [INFO] [1783512000.409905212] [lifecycle_manager_keepout]: Creating and initializing lifecycle service clients
[map_server-15] [INFO] [1783512000.451977713] [keepout_mask_soft_server]:
[map_server-15]         keepout_mask_soft_server lifecycle node launched.
[map_server-15]         Waiting on external lifecycle transitions to activate
[map_server-15]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[map_server-15] [INFO] [1783512000.452655261] [keepout_mask_soft_server]: Creating
[costmap_filter_info_server-16] [INFO] [1783512000.498341161] [keepout_filter_info_server]:
[costmap_filter_info_server-16]         keepout_filter_info_server lifecycle node launched.
[costmap_filter_info_server-16]         Waiting on external lifecycle transitions to activate
[costmap_filter_info_server-16]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[qr_decoder-10] [INFO] [1783512000.594308642] [qr_decoder_zbar]: QR decoder (ZBar) started: rgb=/aurora/rgb/image_raw, depth=/aurora/depth/image_raw, filter=on, range=[50, 4000]mm, min_qr_len=1, intrinsics: fx=421.3 fy=422.3 cx=320.3 cy=197.0
[lifecycle_manager-17] [INFO] [1783512000.620361724] [lifecycle_manager_keepout]: Starting managed nodes bringup...
[lifecycle_manager-17] [INFO] [1783512000.620692849] [lifecycle_manager_keepout]: Configuring keepout_mask_server
[map_server-14] [INFO] [1783512000.694033134] [keepout_mask_server]:
[map_server-14]         keepout_mask_server lifecycle node launched.
[map_server-14]         Waiting on external lifecycle transitions to activate
[map_server-14]         See https://design.ros2.org/articles/node_lifecycle.html for more information.
[map_server-14] [INFO] [1783512000.698229200] [keepout_mask_server]: Creating
[aurora930_node-9] W0708 20:00:00.824965  5640 ros2_node.cc:35] hello aurora 900/930
[aurora930_node-9] 2026-07-08 20:00:00.902 (   0.419s) [        B9E24020] device_manager_impl.cc:89    INFO| hotplug has registed by user
[map_server-14] [INFO] [1783512000.939399177] [keepout_mask_server]: Configuring
[map_server-14] [INFO] [1783512000.939722047] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.yaml
[map_server-14] [INFO] [1783512000.948824159] [map_io]: resolution: 0.05
[map_server-14] [INFO] [1783512000.948946846] [map_io]: origin[0]: -2.65
[map_server-14] [INFO] [1783512000.948981071] [map_io]: origin[1]: -4.5
[map_server-14] [INFO] [1783512000.949009002] [map_io]: origin[2]: 0
[map_server-14] [INFO] [1783512000.949038225] [map_io]: free_thresh: 0.5
[map_server-14] [INFO] [1783512000.949066406] [map_io]: occupied_thresh: 0.5
[map_server-14] [INFO] [1783512000.949109261] [map_io]: mode: scale
[map_server-14] [INFO] [1783512000.949142486] [map_io]: negate: 0
[map_server-14] [INFO] [1783512000.967996161] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm
[map_server-14] [INFO] [1783512000.994181810] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask.pgm: 163 X 141 map @ 0.05 m/cell
[lifecycle_manager-17] [INFO] [1783512001.038669066] [lifecycle_manager_keepout]: Configuring keepout_mask_soft_server
[map_server-15] [INFO] [1783512001.042158318] [keepout_mask_soft_server]: Configuring
[map_server-15] [INFO] [1783512001.042549431] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask_soft.yaml
[map_server-15] [INFO] [1783512001.045006873] [map_io]: resolution: 0.05
[map_server-15] [INFO] [1783512001.045116387] [map_io]: origin[0]: -2.65
[map_server-15] [INFO] [1783512001.045161451] [map_io]: origin[1]: -4.5
[map_server-15] [INFO] [1783512001.045196552] [map_io]: origin[2]: 0
[map_server-15] [INFO] [1783512001.045230486] [map_io]: free_thresh: 0.01
[map_server-15] [INFO] [1783512001.045262377] [map_io]: occupied_thresh: 0.99
[map_server-15] [INFO] [1783512001.045314653] [map_io]: mode: scale
[map_server-15] [INFO] [1783512001.045351463] [map_io]: negate: 0
[map_server-15] [INFO] [1783512001.046145153] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask_soft.pgm
[aurora930_node-9] device_count==========1
[aurora930_node-9] I0708 20:00:01.042971  5640 aurora900_ros2_device.cc:153] BOOT_ORDER_1::Found 1 deptrum device
[aurora930_node-9] I0708 20:00:01.043573  5640 aurora900_ros2_device.cc:162] BOOT_ORDER_1::No serial number provided: picking first device
[aurora930_node-9] 2026-07-08 20:00:01.043 (   0.561s) [        B9E24020] device_manager_impl.cc:318   INFO| Device information:
[aurora930_node-9]      ir_pid:0x1930, rgb_pid:0x0
[aurora930_node-9]      serial number:HY400529001015314G00248
[aurora930_node-9] I0708 20:00:01.043779  5640 aurora900_ros2_device.cc:206] BOOT_ORDER_1::0:device start opening
[aurora930_node-9] 2026-07-08 20:00:01.048 (   0.566s) [        B9E24020]   custom_usb_device.cc:101   INFO| bulk in endpoint addr:129
[aurora930_node-9] 2026-07-08 20:00:01.048 (   0.566s) [        B9E24020]   custom_usb_device.cc:98    INFO| bulk out endpoint addr:2
[map_server-15] [INFO] [1783512001.069444686] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/keepout_mask_soft.pgm: 163 X 141 map @ 0.05 m/cell
[aurora930_node-9] 2026-07-08 20:00:01.080 (   0.598s) [        B9E24020]deptrum_camera_aurora93:53    INFO| doe_broken:0 ito_support:1 crash_count:0 wdt_count:0 hard_reset_count:2 heart_boot_count:0 boot_total:134 last_crash_time:N
[aurora930_node-9] I0708 20:00:01.080914  5640 aurora900_ros2_device.cc:247] device supported frame_mode:
[aurora930_node-9] I0708 20:00:01.081039  5640 aurora900_ros2_device.cc:252] [0]:ir_mode:=13 kRes320x200Ir8Bit rgb_mode:=31 kRes320x200RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0708 20:00:01.081091  5640 aurora900_ros2_device.cc:252] [1]:ir_mode:=17 kRes480x300Depth16Bit rgb_mode:=32 kRes480x300RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0708 20:00:01.081130  5640 aurora900_ros2_device.cc:252] [2]:ir_mode:=20 kRes640x400Ir8Bit rgb_mode:=33 kRes640x400RgbYuv depth_mode:=0 kInvalid
[aurora930_node-9] I0708 20:00:01.081164  5640 aurora900_ros2_device.cc:266] current set mode ir_mode:20:kRes640x400Ir8Bit,rgb_mode:33:kRes640x400RgbYuv
[lifecycle_manager-17] [INFO] [1783512001.104668582] [lifecycle_manager_keepout]: Configuring keepout_filter_info_server
[costmap_filter_info_server-16] [INFO] [1783512001.106788313] [keepout_filter_info_server]: Configuring
[lifecycle_manager-17] [INFO] [1783512001.148927223] [lifecycle_manager_keepout]: Activating keepout_mask_server
[map_server-14] [INFO] [1783512001.150321840] [keepout_mask_server]: Activating
[map_server-14] [INFO] [1783512001.150723250] [keepout_mask_server]: Creating bond (keepout_mask_server) to lifecycle manager.
[lifecycle_manager-17] [INFO] [1783512001.283592803] [lifecycle_manager_keepout]: Server keepout_mask_server connected with bond.
[lifecycle_manager-17] [INFO] [1783512001.283779063] [lifecycle_manager_keepout]: Activating keepout_mask_soft_server
[lifecycle_manager-17] [INFO] [1783512001.413272129] [lifecycle_manager_keepout]: Server keepout_mask_soft_server connected with bond.
[lifecycle_manager-17] [INFO] [1783512001.413425331] [lifecycle_manager_keepout]: Activating keepout_filter_info_server
[lifecycle_manager-17] [INFO] [1783512001.529705428] [lifecycle_manager_keepout]: Server keepout_filter_info_server connected with bond.
[lifecycle_manager-17] [INFO] [1783512001.529889771] [lifecycle_manager_keepout]: Managed nodes are active
[lifecycle_manager-17] [INFO] [1783512001.529966809] [lifecycle_manager_keepout]: Creating bond timer...
[map_server-15] [INFO] [1783512001.284605103] [keepout_mask_soft_server]: Activating
[map_server-15] [INFO] [1783512001.285192648] [keepout_mask_soft_server]: Creating bond (keepout_mask_soft_server) to lifecycle manager.
[bmi088_iio_bridge.py-5] [INFO] [1783512001.408641595] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1783512001.411173075] [bmi088_iio_bridge]:   DIAGNOSTIC: Scanning IIO devices under /sys/bus/iio/devices/
[bmi088_iio_bridge.py-5] [INFO] [1783512001.413449134] [bmi088_iio_bridge]:   Equivalent to: ls /sys/bus/iio/devices/*/name
[bmi088_iio_bridge.py-5] [INFO] [1783512001.415934090] [bmi088_iio_bridge]: =================================================================
[bmi088_iio_bridge.py-5] [INFO] [1783512001.418538023] [bmi088_iio_bridge]:   iio:device0/name = "34190000.adc"
[bmi088_iio_bridge.py-5] [INFO] [1783512001.421172513] [bmi088_iio_bridge]:   iio:device1/name = "bmi08x"
[bmi088_iio_bridge.py-5] [INFO] [1783512001.423879705] [bmi088_iio_bridge]:   trigger0/name = "34190000.adc-dev0"
[bmi088_iio_bridge.py-5] [INFO] [1783512001.426534538] [bmi088_iio_bridge]:   Total IIO devices found: 3
[bmi088_iio_bridge.py-5] [INFO] [1783512001.429231351] [bmi088_iio_bridge]:   BMI088 kernel module APPEARS LOADED: 1 BMI device(s) detected
[bmi088_iio_bridge.py-5] [INFO] [1783512001.431775128] [bmi088_iio_bridge]:   BMI device names: ['bmi08x']
[bmi088_iio_bridge.py-5] [INFO] [1783512001.435261295] [bmi088_iio_bridge]:   gyro:  /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_anglvel is_si=False scale_override=0.00053
[bmi088_iio_bridge.py-5] [INFO] [1783512001.440947901] [bmi088_iio_bridge]:   accel: /sys/bus/iio/devices/iio:device1 (name=="bmi08x") attr=in_accel is_si=False scale_override=0.00341
[bmi088_iio_bridge.py-5] [INFO] [1783512001.563200498] [bmi088_iio_bridge]: BMI088 IIO Bridge 启动 @ 50Hz -> /imu_data  [OK]
[INFO] [component_container_isolated-18]: process started with pid [5929]
[costmap_filter_info_server-16] [INFO] [1783512001.414385855] [keepout_filter_info_server]: Activating
[costmap_filter_info_server-16] [INFO] [1783512001.414620139] [keepout_filter_info_server]: Creating bond (keepout_filter_info_server) to lifecycle manager.
[qr_decision.py-11] [INFO] [1783512001.434782222] [qr_decision]: qr_decision started: cooldown=3.0s, awaiting /sign from qr_decoder
[imu_madgwick_filter.py-6] [INFO] [1783512001.526557014] [imu_madgwick_bmi088]: [imu_madgwick] init: beta=0.0030, gyro_noise=0.0002, accel_noise=0.010
[imu_madgwick_filter.py-6] [INFO] [1783512001.603646307] [imu_madgwick_bmi088]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-6] [INFO] [1783512001.607662407] [imu_madgwick_bmi088]: [imu_madgwick] accel init: roll=-2.2deg, pitch=-3.6deg
[imu_madgwick_filter.py-4] [INFO] [1783512001.555119273] [imu_madgwick_filter]: [imu_madgwick] init: beta=0.0330, gyro_noise=0.0010, accel_noise=0.050
[imu_madgwick_filter.py-4] [INFO] [1783512001.561272738] [imu_madgwick_filter]: [imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline
[imu_madgwick_filter.py-4] [INFO] [1783512001.563711087] [imu_madgwick_filter]: [imu_madgwick] accel init: roll=0.0deg, pitch=0.1deg
[aurora930_node-9] I0708 20:00:01.616904  5640 aurora900_ros2_device.cc:387] Switch Auto Exposure
[aurora930_node-9] 2026-07-08 20:00:01.677 (   1.194s) [        B9E24020]      aurora900_impl.cc:1106  INFO| SetHeartbeat user set heartbeat enable: 0
[aurora930_node-9] I0708 20:00:02.089242  5640 aurora900_ros2_device.cc:304] BOOT_ORDER_1::Device information:
[aurora930_node-9] I0708 20:00:02.089408  5640 aurora900_ros2_device.cc:305]     sdk version: 1.1.22
[aurora930_node-9] I0708 20:00:02.089444  5640 aurora900_ros2_device.cc:306]     device name: Aurora 930
[aurora930_node-9] I0708 20:00:02.089474  5640 aurora900_ros2_device.cc:307]     serial number: HY400529001015314G00248
[aurora930_node-9] I0708 20:00:02.089504  5640 aurora900_ros2_device.cc:308]     firmware version: 1.7.2
[aurora930_node-9] I0708 20:00:02.089556  5640 camera_parameters.cc:134] BOOT_ORDER_1::Camera Parameters:
[aurora930_node-9] I0708 20:00:02.089771  5640 camera_parameters.cc:135] BOOT_ORDER_1::  Ir Intrinsics:
[aurora930_node-9] I0708 20:00:02.089803  5640 camera_parameters.cc:146]                 Resolution:
[aurora930_node-9] I0708 20:00:02.089831  5640 camera_parameters.cc:147]                         Rows:400
[aurora930_node-9] I0708 20:00:02.089859  5640 camera_parameters.cc:148]                         Cols:640
[aurora930_node-9] I0708 20:00:02.089886  5640 camera_parameters.cc:149]                 Intrinsics:
[aurora930_node-9] I0708 20:00:02.089913  5640 camera_parameters.cc:150]                         fx: 421.307
[aurora930_node-9] I0708 20:00:02.090003  5640 camera_parameters.cc:151]                         fy: 422.254
[aurora930_node-9] I0708 20:00:02.090039  5640 camera_parameters.cc:152]                         cx: 320.27
[aurora930_node-9] I0708 20:00:02.090072  5640 camera_parameters.cc:153]                         cy: 197.01
[aurora930_node-9] I0708 20:00:02.090106  5640 camera_parameters.cc:154]                         k1: 0.0606853
[aurora930_node-9] I0708 20:00:02.090140  5640 camera_parameters.cc:155]                         k2: -0.10961
[aurora930_node-9] I0708 20:00:02.090173  5640 camera_parameters.cc:156]                         p1: 0.00126689
[aurora930_node-9] I0708 20:00:02.090207  5640 camera_parameters.cc:157]                         p2: -0.00120539
[aurora930_node-9] I0708 20:00:02.090240  5640 camera_parameters.cc:158]                         k3: 0.0522281
[aurora930_node-9] I0708 20:00:02.090274  5640 camera_parameters.cc:138] BOOT_ORDER_1::  Rgb Intrinsics:
[aurora930_node-9] I0708 20:00:02.090303  5640 camera_parameters.cc:146]                 Resolution:
[aurora930_node-9] I0708 20:00:02.090330  5640 camera_parameters.cc:147]                         Rows:400
[aurora930_node-9] I0708 20:00:02.090358  5640 camera_parameters.cc:148]                         Cols:640
[aurora930_node-9] I0708 20:00:02.090385  5640 camera_parameters.cc:149]                 Intrinsics:
[aurora930_node-9] I0708 20:00:02.090412  5640 camera_parameters.cc:150]                         fx: 416.49
[aurora930_node-9] I0708 20:00:02.090446  5640 camera_parameters.cc:151]                         fy: 417.383
[aurora930_node-9] I0708 20:00:02.090479  5640 camera_parameters.cc:152]                         cx: 316.832
[aurora930_node-9] I0708 20:00:02.090513  5640 camera_parameters.cc:153]                         cy: 188.753
[aurora930_node-9] I0708 20:00:02.090546  5640 camera_parameters.cc:154]                         k1: 0.00611878
[aurora930_node-9] I0708 20:00:02.090579  5640 camera_parameters.cc:155]                         k2: -0.0490436
[aurora930_node-9] I0708 20:00:02.090611  5640 camera_parameters.cc:156]                         p1: 0.000399548
[aurora930_node-9] I0708 20:00:02.090644  5640 camera_parameters.cc:157]                         p2: 0.000563892
[aurora930_node-9] I0708 20:00:02.090677  5640 camera_parameters.cc:158]                         k3: 0.0308458
[aurora930_node-9] I0708 20:00:02.090709  5640 camera_parameters.cc:141] BOOT_ORDER_1::  Ir to Rgb Extrinsic:
[aurora930_node-9] I0708 20:00:02.090739  5640 camera_parameters.cc:162]                 Extrinsics:
[aurora930_node-9] I0708 20:00:02.090765  5640 camera_parameters.cc:163]                         Rotation[0]: 0.999973, 0.00724076, -0.00112023
[aurora930_node-9] I0708 20:00:02.090803  5640 camera_parameters.cc:165]                         Rotation[1]: -0.00724006, 0.999973, 0.000633162
[aurora930_node-9] I0708 20:00:02.090842  5640 camera_parameters.cc:167]                         Rotation[2]: 0.00112478, -0.000625033, 0.999999
[aurora930_node-9] I0708 20:00:02.090935  5640 camera_parameters.cc:169]                         Translation: -9.88662, 0.117748, 0.603513
[aurora930_node-9] 2026-07-08 20:00:02.091 (   1.609s) [        B9E24020]      aurora900_impl.cc:578   INFO| stream_mask_:0, rgb_stream_count_:1
[aurora930_node-9] 2026-07-08 20:00:02.382 (   1.900s) [        928E47E0]deptrum_camera_aurora93:407    ERR| recv first frame time is 1783512002382
[hobot_codec_republish-13] [WARN] [1783512002.376334307] [HobotVenc]: init_pic_w_: 640, init_pic_h_: 400, alined_pic_w_: 640, alined_pic_h_: 400, aline_w_: 16, aline_h_: 16
[hobot_codec_republish-13] [WARN] [1783512004.484833784] [vlm_jpeg_encoder]: Sub imgRaw fps [5.95]
[hobot_codec_republish-13] [WARN] [1783512004.487525928] [vlm_jpeg_encoder]: Pub img fps [5.95]
[lslidar_driver_node-2] port = /dev/ttyACM1, baud_rate = 230400
[lslidar_driver_node-2] open_port /dev/ttyACM1 OK !
[vision_ai_node-12] [INFO] [1783512005.804372757] [vision_ai_node]: Loaded config: /userdata/dev_ws/install/racing_vision_ai/share/racing_vision_ai/config/vision_ai_config.yaml
[vision_ai_node-12] [INFO] [1783512006.229283581] [vision_ai_node]: Volcengine Ark client initialized
[vision_ai_node-12] [INFO] [1783512006.247164768] [vision_ai_node]: Vision AI Node initialized (JPU JPEG mode)
[vision_ai_node-12] [INFO] [1783512006.250188620] [vision_ai_node]: Waiting for sign4return=100
[vision_ai_node-12] [INFO] [1783512006.252481980] [vision_ai_node]: Image topic: /aurora/rgb/image_jpeg
[INFO] [yolo_costmap_bridge.py-20]: process started with pid [5942]
[INFO] [competition_master_stage3.py-21]: process started with pid [5944]
[INFO] [racing_obstacle_detection_yolo-19]: process started with pid [5940]
[INFO] [speed_profile_node.py-22]: process started with pid [5950]
[bmi088_iio_bridge.py-5] [INFO] [1783512007.160211165] [bmi088_iio_bridge]:   gyro bias calibrated: (0.002655, 0.000996, -0.002804) rad/s
[INFO] [rviz2-23]: process started with pid [5954]
[component_container_isolated-18] [INFO] [1783512007.286871600] [nav2_container]: Load Library: /opt/ros/humble/lib/libcontroller_server_core.so
[component_container_isolated-18] [INFO] [1783512007.368829004] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-18] [INFO] [1783512007.369142620] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_controller::ControllerServer>
[component_container_isolated-18] [INFO] [1783512007.506647459] [controller_server]:
[component_container_isolated-18]       controller_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1783512007.614625179] [controller_server]: Creating controller server
[component_container_isolated-18] [INFO] [1783512007.823898264] [local_costmap.local_costmap]:
[component_container_isolated-18]       local_costmap lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1783512007.852138153] [local_costmap.local_costmap]: Creating Costmap
[component_container_isolated-18] [INFO] [1783512007.924924494] [nav2_container]: Load Library: /opt/ros/humble/lib/libmap_server_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/controller_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1783512007.980974264] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::CostmapFilterInfoServer>
[component_container_isolated-18] [INFO] [1783512007.981187704] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapSaver>
[component_container_isolated-18] [INFO] [1783512007.981248151] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-18] [INFO] [1783512007.981299594] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_map_server::MapServer>
[component_container_isolated-18] [INFO] [1783512008.087451481] [map_server]:
[component_container_isolated-18]       map_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/map_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1783512008.087819832] [map_server]: Creating
[component_container_isolated-18] [INFO] [1783512008.101296516] [nav2_container]: Load Library: /opt/ros/humble/lib/libsmoother_server_core.so
[component_container_isolated-18] [INFO] [1783512008.162595047] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-18] [INFO] [1783512008.162778639] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_smoother::SmootherServer>
[component_container_isolated-18] [INFO] [1783512008.289417063] [smoother_server]:
[component_container_isolated-18]       smoother_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1783512008.318381774] [smoother_server]: Creating smoother server
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/smoother_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1783512008.333364673] [nav2_container]: Load Library: /opt/ros/humble/lib/libamcl_core.so
[component_container_isolated-18] [INFO] [1783512008.379792069] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[component_container_isolated-18] [INFO] [1783512008.380006302] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_amcl::AmclNode>
[racing_obstacle_detection_yolo-19] [BPU_PLAT]BPU Platform Version(1.3.6)! soc info(x5)
[racing_obstacle_detection_yolo-19] [HBRT] set log level as 0. version = 3.15.55.0
[racing_obstacle_detection_yolo-19] [DNN] Runtime version = 1.24.5_(3.15.55 HBRT)
[component_container_isolated-18] [INFO] [1783512008.491836123] [amcl]:
[component_container_isolated-18]       amcl lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1783512008.503881380] [amcl]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/amcl' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1783512008.590465191] [nav2_container]: Load Library: /opt/ros/humble/lib/libplanner_server_core.so
[component_container_isolated-18] [INFO] [1783512008.617199240] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-18] [INFO] [1783512008.617398423] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_planner::PlannerServer>
[component_container_isolated-18] [INFO] [1783512008.732552789] [planner_server]:
[component_container_isolated-18]       planner_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1783512008.755590274] [planner_server]: Creating
[racing_obstacle_detection_yolo-19] [A][DNN][packed_model.cpp:247][Model](2026-07-08,20:00:08.766.212) [HorizonRT] The model builder version = 1.24.3
[component_container_isolated-18] [INFO] [1783512008.935891811] [global_costmap.global_costmap]:
[component_container_isolated-18]       global_costmap lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1783512008.941445767] [global_costmap.global_costmap]: Creating Costmap
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/planner_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1783512009.023157964] [nav2_container]: Load Library: /opt/ros/humble/lib/libnav2_lifecycle_manager_core.so
[component_container_isolated-18] [INFO] [1783512009.031606165] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1783512009.031891642] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1783512009.103936360] [lifecycle_manager_localization]: Creating
[component_container_isolated-18] [INFO] [1783512009.147557431] [lifecycle_manager_localization]: Creating and initializing lifecycle service clients
[component_container_isolated-18] [INFO] [1783512009.149589910] [nav2_container]: Load Library: /opt/ros/humble/lib/libbehavior_server_core.so
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_localization' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1783512009.237614611] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-18] [INFO] [1783512009.237814461] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<behavior_server::BehaviorServer>
[component_container_isolated-18] [INFO] [1783512009.261126792] [lifecycle_manager_localization]: Starting managed nodes bringup...
[component_container_isolated-18] [INFO] [1783512009.261435239] [lifecycle_manager_localization]: Configuring map_server
[component_container_isolated-18] [INFO] [1783512009.263153727] [map_server]: Configuring
[component_container_isolated-18] [INFO] [1783512009.263493897] [map_io]: Loading yaml file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.yaml
[component_container_isolated-18] [INFO] [1783512009.291743166] [map_io]: resolution: 0.05
[component_container_isolated-18] [INFO] [1783512009.291878359] [map_io]: origin[0]: -2.65
[component_container_isolated-18] [INFO] [1783512009.291913835] [map_io]: origin[1]: -4.5
[component_container_isolated-18] [INFO] [1783512009.291942474] [map_io]: origin[2]: 0
[component_container_isolated-18] [INFO] [1783512009.291972656] [map_io]: free_thresh: 0.25
[component_container_isolated-18] [INFO] [1783512009.292000545] [map_io]: occupied_thresh: 0.65
[component_container_isolated-18] [INFO] [1783512009.292057032] [map_io]: mode: trinary
[component_container_isolated-18] [INFO] [1783512009.292089131] [map_io]: negate: 0
[component_container_isolated-18] [INFO] [1783512009.292883780] [map_io]: Loading image_file: /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm
[component_container_isolated-18] [INFO] [1783512009.333522062] [map_io]: Read map /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/maps/room.pgm: 163 X 141 map @ 0.05 m/cell
[component_container_isolated-18] [INFO] [1783512009.466168044] [lifecycle_manager_localization]: Configuring amcl
[component_container_isolated-18] [INFO] [1783512009.469946274] [amcl]: Configuring
[component_container_isolated-18] [INFO] [1783512009.471115153] [amcl]: initTransforms
[component_container_isolated-18] [INFO] [1783512009.484963649] [behavior_server]:
[component_container_isolated-18]       behavior_server lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[hobot_codec_republish-13] [WARN] [1783512009.507295779] [vlm_jpeg_encoder]: Sub imgRaw fps [12.15]
[hobot_codec_republish-13] [WARN] [1783512009.512024654] [vlm_jpeg_encoder]: Pub img fps [12.14]
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/behavior_server' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1783512009.575920364] [nav2_container]: Load Library: /opt/ros/humble/lib/libbt_navigator_core.so
[component_container_isolated-18] [INFO] [1783512009.617889230] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-18] [INFO] [1783512009.618246451] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_bt_navigator::BtNavigator>
[component_container_isolated-18] [INFO] [1783512009.705587725] [amcl]: initPubSub
[component_container_isolated-18] [INFO] [1783512009.774605132] [amcl]: Subscribed to map topic.
[component_container_isolated-18] [INFO] [1783512009.852391233] [lifecycle_manager_localization]: Activating map_server
[component_container_isolated-18] [INFO] [1783512009.854696432] [map_server]: Activating
[component_container_isolated-18] [INFO] [1783512009.855166960] [map_server]: Creating bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512009.855618520] [amcl]: Received a 163 X 141 map @ 0.050 m/pix
[component_container_isolated-18] [INFO] [1783512009.900476837] [bt_navigator]:
[component_container_isolated-18]       bt_navigator lifecycle node launched.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/bt_navigator' in container '/nav2_container'
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1783512009.901335102] [bt_navigator]: Creating
[component_container_isolated-18] [INFO] [1783512009.924656646] [nav2_container]: Load Library: /opt/ros/humble/lib/libwaypoint_follower_core.so
[component_container_isolated-18] [INFO] [1783512009.940293539] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-18] [INFO] [1783512009.941440991] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_waypoint_follower::WaypointFollower>
[component_container_isolated-18] [INFO] [1783512009.978271693] [lifecycle_manager_localization]: Server map_server connected with bond.
[component_container_isolated-18] [INFO] [1783512009.978486635] [lifecycle_manager_localization]: Activating amcl
[component_container_isolated-18] [INFO] [1783512009.983372296] [amcl]: Activating
[component_container_isolated-18] [INFO] [1783512009.983742524] [amcl]: initialPoseReceived
[component_container_isolated-18] [INFO] [1783512009.984321398] [amcl]: Setting pose (1783512009.984315): -1.985 -0.014 0.262
[component_container_isolated-18] [INFO] [1783512009.988334538] [amcl]: Creating bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512010.106531265] [amcl]: createLaserObject
[component_container_isolated-18] [INFO] [1783512010.195711546] [waypoint_follower]:
[component_container_isolated-18]       waypoint_follower lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[component_container_isolated-18] [INFO] [1783512010.196218384] [lifecycle_manager_localization]: Server amcl connected with bond.
[component_container_isolated-18] [INFO] [1783512010.207314330] [lifecycle_manager_localization]: Managed nodes are active
[component_container_isolated-18] [INFO] [1783512010.207433724] [lifecycle_manager_localization]: Creating bond timer...
[racing_obstacle_detection_yolo-19] [WARN] [1783512010.216561140] [ObstacleDetectionNode]: input fps: -1.00, out fps: 9.69, infer time ms: 73, post process time ms: 25
[component_container_isolated-18] [INFO] [1783512010.229058124] [waypoint_follower]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/waypoint_follower' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1783512010.322737748] [nav2_container]: Load Library: /opt/ros/humble/lib/libvelocity_smoother_core.so
[component_container_isolated-18] [INFO] [1783512010.338306983] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-18] [INFO] [1783512010.338627227] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_velocity_smoother::VelocitySmoother>
[component_container_isolated-18] [INFO] [1783512010.604033749] [velocity_smoother]:
[component_container_isolated-18]       velocity_smoother lifecycle node launched.
[component_container_isolated-18]       Waiting on external lifecycle transitions to activate
[component_container_isolated-18]       See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/velocity_smoother' in container '/nav2_container'
[component_container_isolated-18] [INFO] [1783512010.630145402] [nav2_container]: Found class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[component_container_isolated-18] [INFO] [1783512010.630361052] [nav2_container]: Instantiate class: rclcpp_components::NodeFactoryTemplate<nav2_lifecycle_manager::LifecycleManager>
[speed_profile_node.py-22] [INFO] [1783512010.748895115] [speed_profile_node]: speed_profile_node started — v_max=0.50 v_min=0.20 beta=0.25 lambda=1.20 max_accel=1.01 max_decel=-1.57
[component_container_isolated-18] [INFO] [1783512010.785673416] [lifecycle_manager_navigation]: Creating
[INFO] [launch_ros.actions.load_composable_nodes]: Loaded node '/lifecycle_manager_navigation' in container '/nav2_container'
[yolo_costmap_bridge.py-20] [INFO] [1783512010.823922456] [yolo_costmap_bridge]: YoloCostmapBridge ready
[component_container_isolated-18] [INFO] [1783512010.826042854] [lifecycle_manager_navigation]: Creating and initializing lifecycle service clients
[component_container_isolated-18] [INFO] [1783512011.073458592] [lifecycle_manager_navigation]: Starting managed nodes bringup...
[component_container_isolated-18] [INFO] [1783512011.073833155] [lifecycle_manager_navigation]: Configuring controller_server
[component_container_isolated-18] [INFO] [1783512011.076500787] [controller_server]: Configuring controller interface
[component_container_isolated-18] [INFO] [1783512011.077834706] [controller_server]: getting goal checker plugins..
[component_container_isolated-18] [INFO] [1783512011.082191102] [controller_server]: Controller frequency set to 10.0000Hz
[component_container_isolated-18] [INFO] [1783512011.082532274] [local_costmap.local_costmap]: Configuring
[component_container_isolated-18] [INFO] [1783512011.162097227] [local_costmap.local_costmap]: Using plugin "obstacle_layer"
[racing_obstacle_detection_yolo-19] [WARN] [1783512011.205457291] [ObstacleDetectionNode]: input fps: 9.01, out fps: 7.95, infer time ms: 14, post process time ms: 8
[component_container_isolated-18] [INFO] [1783512011.236182428] [local_costmap.local_costmap]: Subscribed to Topics: scan tracked_obstacles
[imu_madgwick_filter.py-6] [INFO] [1783512011.370734242] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=325 q_w=0.9994 angle=4.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783512011.406652278] [imu_madgwick_filter]: [imu_madgwick ->] msgs=200 q_w=0.9993 angle=4.1deg beta=0.0330
[component_container_isolated-18] [INFO] [1783512011.456218334] [local_costmap.local_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1783512011.460138511] [local_costmap.local_costmap]: Using plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1783512011.511680351] [local_costmap.local_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1783512011.511881327] [local_costmap.local_costmap]: Using plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1783512011.534980301] [local_costmap.local_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1783512011.660982655] [controller_server]: Created progress_checker : progress_checker of type nav2_controller::SimpleProgressChecker
[component_container_isolated-18] [INFO] [1783512011.683877485] [controller_server]: Created goal checker : goal_checker of type nav2_controller::SimpleGoalChecker
[component_container_isolated-18] [INFO] [1783512011.702175090] [controller_server]: Controller Server has goal_checker  goal checkers available.
[component_container_isolated-18] [INFO] [1783512011.723688184] [controller_server]: Created controller : FollowPath of type nav2_regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1783512011.923594315] [controller_server]: Controller Server has FollowPath  controllers available.
[component_container_isolated-18] [INFO] [1783512011.988711222] [lifecycle_manager_navigation]: Configuring smoother_server
[component_container_isolated-18] [INFO] [1783512011.993446600] [smoother_server]: Configuring smoother server
[component_container_isolated-18] [INFO] [1783512012.175563298] [smoother_server]: Created smoother : SmoothPath of type nav2_constrained_smoother/ConstrainedSmoother
[racing_obstacle_detection_yolo-19] [WARN] [1783512012.239242608] [ObstacleDetectionNode]: input fps: 8.70, out fps: 12.56, infer time ms: 10, post process time ms: 6
[component_container_isolated-18] [INFO] [1783512012.240325652] [smoother_server]: Smoother Server has SmoothPath  smoothers available.
[component_container_isolated-18] [INFO] [1783512012.314152973] [lifecycle_manager_navigation]: Configuring planner_server
[component_container_isolated-18] [INFO] [1783512012.318432873] [planner_server]: Configuring
[component_container_isolated-18] [INFO] [1783512012.318824653] [global_costmap.global_costmap]: Configuring
[component_container_isolated-18] [INFO] [1783512012.381155577] [global_costmap.global_costmap]: Using plugin "static_layer"
[component_container_isolated-18] [INFO] [1783512012.409748893] [global_costmap.global_costmap]: Subscribing to the map topic (/map) with transient local durability
[component_container_isolated-18] [INFO] [1783512012.423345470] [global_costmap.global_costmap]: Initialized plugin "static_layer"
[component_container_isolated-18] [INFO] [1783512012.423640660] [global_costmap.global_costmap]: Using plugin "obstacle_layer"
[competition_master_stage3.py-21] [INFO] [1783512012.451483308] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-21] [INFO] [1783512012.455319192] [competition_master_stage3]: === [Stage 3] 总控节点初始化 ===
[competition_master_stage3.py-21] [INFO] [1783512012.460874732] [competition_master_stage3]:   QR点:    (0.41, -3.17, yaw=0.00)
[competition_master_stage3.py-21] [INFO] [1783512012.463989713] [competition_master_stage3]:   通道入口: (0.33, -1.16, yaw=0.00)
[component_container_isolated-18] [INFO] [1783512012.463837220] [global_costmap.global_costmap]: Subscribed to Topics: scan tracked_obstacles
[competition_master_stage3.py-21] [INFO] [1783512012.467055544] [competition_master_stage3]:   P点:     (-1.99, -0.01, yaw=0.26)
[competition_master_stage3.py-21] [INFO] [1783512012.470686326] [competition_master_stage3]:   cruise_cw: 4路点 (1,2,VLM,post) → VLM=(3.02, -1.02)
[competition_master_stage3.py-21] [INFO] [1783512012.473926369] [competition_master_stage3]:   cruise_ccw: 4路点 (1,2,VLM,post) → VLM=(2.02, 0.94)
[competition_master_stage3.py-21] [INFO] [1783512012.478126061] [competition_master_stage3]:   超时: total=180.0s QR=90.0s entry=60.0s cruise=180.0s vlm=30.0s return=120.0s
[competition_master_stage3.py-21] [INFO] [1783512012.482342595] [competition_master_stage3]:   回退QR方向: 逆时针
[competition_master_stage3.py-21] [INFO] [1783512012.486493930] [competition_master_stage3]:   VLM结果话题: vlm_result
[competition_master_stage3.py-21] [INFO] [1783512012.490320268] [competition_master_stage3]: ============================================================
[component_container_isolated-18] [INFO] [1783512012.640149212] [global_costmap.global_costmap]: Initialized plugin "obstacle_layer"
[component_container_isolated-18] [INFO] [1783512012.641529238] [global_costmap.global_costmap]: Using plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1783512012.665390720] [global_costmap.global_costmap]: Initialized plugin "keepout_filter"
[component_container_isolated-18] [INFO] [1783512012.665603035] [global_costmap.global_costmap]: Using plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1783512012.681937195] [global_costmap.global_costmap]: Initialized plugin "inflation_layer"
[component_container_isolated-18] [INFO] [1783512012.752170087] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 163 X 141 at 0.050000 m/pix
[component_container_isolated-18] [INFO] [1783512012.834599812] [planner_server]: Created global planner plugin GridBased of type nav2_smac_planner/SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1783512012.834822591] [planner_server]: Configuring GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1783512012.894831391] [planner_server]: Even sized heuristic lookup table size set 266.000000, increasing size by 1 to make odd
[racing_obstacle_detection_yolo-19] [WARN] [1783512013.257241122] [ObstacleDetectionNode]: input fps: 13.47, out fps: 13.77, infer time ms: 10, post process time ms: 7
[rviz2-23] [INFO] [1783512013.650603688] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-23] [INFO] [1783512013.651423600] [rviz2]: OpenGl version: 4.5 (GLSL 4.5)
[rviz2-23] [INFO] [1783512014.171067119] [rviz2]: Stereo is NOT SUPPORTED
[racing_obstacle_detection_yolo-19] [WARN] [1783512014.302361964] [ObstacleDetectionNode]: input fps: 13.45, out fps: 14.40, infer time ms: 10, post process time ms: 10
[hobot_codec_republish-13] [WARN] [1783512014.559583751] [vlm_jpeg_encoder]: Sub imgRaw fps [11.68]
[hobot_codec_republish-13] [WARN] [1783512014.567863075] [vlm_jpeg_encoder]: Pub img fps [11.67]
[racing_obstacle_detection_yolo-19] [WARN] [1783512015.315523008] [ObstacleDetectionNode]: input fps: 14.61, out fps: 12.82, infer time ms: 10, post process time ms: 8
[racing_obstacle_detection_yolo-19] [WARN] [1783512016.329678842] [ObstacleDetectionNode]: input fps: 13.11, out fps: 14.78, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-19] [WARN] [1783512017.346312255] [ObstacleDetectionNode]: input fps: 14.91, out fps: 14.76, infer time ms: 10, post process time ms: 6
[rviz2-23] [INFO] [1783512018.042127237] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[racing_obstacle_detection_yolo-19] [WARN] [1783512018.349993621] [ObstacleDetectionNode]: input fps: 14.71, out fps: 13.97, infer time ms: 10, post process time ms: 7
[qr_decoder-10] [INFO] [1783512018.606574879] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=200 last_qr_frame=-1 gap=-1 frames rejects=0
[rviz2-23] [ERROR] [1783512018.687212454] [rviz2]: Vertex Program:rviz/glsl120/indexed_8bit_image.vert Fragment Program:rviz/glsl120/indexed_8bit_image.frag GLSL link result :
[rviz2-23] active samplers with a different type refer to the same texture image unit
[racing_obstacle_detection_yolo-19] [WARN] [1783512019.356754826] [ObstacleDetectionNode]: input fps: 13.33, out fps: 13.90, infer time ms: 10, post process time ms: 6
[hobot_codec_republish-13] [WARN] [1783512019.575923756] [vlm_jpeg_encoder]: Sub imgRaw fps [13.36]
[hobot_codec_republish-13] [WARN] [1783512019.579252219] [vlm_jpeg_encoder]: Pub img fps [13.37]
[racing_obstacle_detection_yolo-19] [WARN] [1783512020.431562284] [ObstacleDetectionNode]: input fps: 13.99, out fps: 13.04, infer time ms: 10, post process time ms: 6
[imu_madgwick_filter.py-6] [INFO] [1783512021.356584319] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=754 q_w=0.9993 angle=4.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783512021.413472718] [imu_madgwick_filter]: [imu_madgwick ->] msgs=400 q_w=0.9974 angle=8.3deg beta=0.0330
[racing_obstacle_detection_yolo-19] [WARN] [1783512021.491547506] [ObstacleDetectionNode]: input fps: 13.54, out fps: 13.22, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-19] [WARN] [1783512022.569661249] [ObstacleDetectionNode]: input fps: 12.51, out fps: 13.01, infer time ms: 10, post process time ms: 7
[racing_obstacle_detection_yolo-19] [WARN] [1783512023.615672955] [ObstacleDetectionNode]: input fps: 13.69, out fps: 12.42, infer time ms: 10, post process time ms: 6
[hobot_codec_republish-13] [WARN] [1783512024.614517935] [vlm_jpeg_encoder]: Sub imgRaw fps [13.30]
[hobot_codec_republish-13] [WARN] [1783512024.617053833] [vlm_jpeg_encoder]: Pub img fps [13.30]
[racing_obstacle_detection_yolo-19] [WARN] [1783512024.657947701] [ObstacleDetectionNode]: input fps: 12.21, out fps: 14.44, infer time ms: 10, post process time ms: 9
[racing_obstacle_detection_yolo-19] [WARN] [1783512025.715862342] [ObstacleDetectionNode]: input fps: 14.44, out fps: 13.23, infer time ms: 11, post process time ms: 8
[racing_obstacle_detection_yolo-19] [WARN] [1783512026.778630712] [ObstacleDetectionNode]: input fps: 13.30, out fps: 13.15, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-19] [WARN] [1783512027.793216221] [ObstacleDetectionNode]: input fps: 13.46, out fps: 13.81, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-19] [WARN] [1783512028.820248564] [ObstacleDetectionNode]: input fps: 13.86, out fps: 14.61, infer time ms: 10, post process time ms: 6
[hobot_codec_republish-13] [WARN] [1783512029.646687096] [vlm_jpeg_encoder]: Sub imgRaw fps [13.52]
[hobot_codec_republish-13] [WARN] [1783512029.650141289] [vlm_jpeg_encoder]: Pub img fps [13.51]
[racing_obstacle_detection_yolo-19] [WARN] [1783512029.871135593] [ObstacleDetectionNode]: input fps: 13.95, out fps: 13.33, infer time ms: 10, post process time ms: 6
[racing_obstacle_detection_yolo-19] [WARN] [1783512030.930183095] [ObstacleDetectionNode]: input fps: 13.89, out fps: 14.18, infer time ms: 10, post process time ms: 7
[imu_madgwick_filter.py-6] [INFO] [1783512031.362606525] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1219 q_w=0.9994 angle=4.1deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783512031.407804596] [imu_madgwick_filter]: [imu_madgwick ->] msgs=599 q_w=0.9942 angle=12.3deg beta=0.0330
[racing_obstacle_detection_yolo-19] [WARN] [1783512031.934052431] [ObstacleDetectionNode]: input fps: 13.57, out fps: 12.96, infer time ms: 10, post process time ms: 7
[racing_obstacle_detection_yolo-19] [WARN] [1783512032.981729014] [ObstacleDetectionNode]: input fps: 12.71, out fps: 13.37, infer time ms: 10, post process time ms: 7
[qr_decoder-10] [INFO] [1783512033.422120404] [qr_decoder_zbar]: [qr_decoder] SCAN_STATUS frame=400 last_qr_frame=-1 gap=-1 frames rejects=0
[racing_obstacle_detection_yolo-19] [WARN] [1783512034.011394887] [ObstacleDetectionNode]: input fps: 13.96, out fps: 13.62, infer time ms: 10, post process time ms: 8
[component_container_isolated-18] [INFO] [1783512034.129661066] [planner_server]: Configured plugin GridBased of type SmacPlannerHybrid with maximum iterations 1500, max on approach iterations 300, and not allowing unknown traversal. Tolerance 0.50.Using motion model: Reeds-Shepp.
[component_container_isolated-18] [INFO] [1783512034.130100245] [planner_server]: Planner Server has GridBased  planners available.
[component_container_isolated-18] [INFO] [1783512034.203616327] [lifecycle_manager_navigation]: Configuring behavior_server
[component_container_isolated-18] [INFO] [1783512034.208061059] [behavior_server]: Configuring
[component_container_isolated-18] [INFO] [1783512034.271461103] [behavior_server]: Creating behavior plugin spin of type nav2_behaviors/Spin
[component_container_isolated-18] [INFO] [1783512034.281139004] [behavior_server]: Configuring spin
[component_container_isolated-18] [INFO] [1783512034.356041533] [behavior_server]: Creating behavior plugin backup of type nav2_behaviors/BackUp
[component_container_isolated-18] [INFO] [1783512034.375741883] [behavior_server]: Configuring backup
[component_container_isolated-18] [INFO] [1783512034.438269281] [behavior_server]: Creating behavior plugin drive_on_heading of type nav2_behaviors/DriveOnHeading
[component_container_isolated-18] [INFO] [1783512034.450920134] [behavior_server]: Configuring drive_on_heading
[component_container_isolated-18] [INFO] [1783512034.504603924] [behavior_server]: Creating behavior plugin wait of type nav2_behaviors/Wait
[component_container_isolated-18] [INFO] [1783512034.516785666] [behavior_server]: Configuring wait
[component_container_isolated-18] [INFO] [1783512034.573390506] [lifecycle_manager_navigation]: Configuring bt_navigator
[component_container_isolated-18] [INFO] [1783512034.575154892] [bt_navigator]: Configuring
[hobot_codec_republish-13] [WARN] [1783512034.652320224] [vlm_jpeg_encoder]: Sub imgRaw fps [12.79]
[hobot_codec_republish-13] [WARN] [1783512034.654975724] [vlm_jpeg_encoder]: Pub img fps [12.79]
[racing_obstacle_detection_yolo-19] [WARN] [1783512035.014952275] [ObstacleDetectionNode]: input fps: 12.96, out fps: 11.94, infer time ms: 10, post process time ms: 6
[competition_master_stage3.py-21] [INFO] [1783512035.075467329] [competition_master_stage3]: [CPU] governor → performance
[competition_master_stage3.py-21] [INFO] [1783512035.091375359] [competition_master_stage3]: [LAUNCH] 发车阶段: 22.9s
[competition_master_stage3.py-21] [INFO] [1783512035.096639961] [competition_master_stage3]: >>> 系统就绪, 开始 Stage 3 导航
[competition_master_stage3.py-21] [INFO] [1783512035.106045559] [competition_master_stage3]: [BAG] 录制开始: stage3_20260708_200035
[competition_master_stage3.py-21] [INFO] [1783512035.109845634] [competition_master_stage3]: [状态机] INIT → NAV_TO_QR
[competition_master_stage3.py-21] [INFO] [1783512035.119540835] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[competition_master_stage3.py-21] [INFO] [1783512035.200018372] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.00,-0.02) yaw=16deg cmd=(vx=0.00 wz=0.00) elapsed=0.0s cpuFreq=1500MHz cpuT=80C bpuT=78C cpu=100% mem=18%
[component_container_isolated-18] [INFO] [1783512035.463899002] [lifecycle_manager_navigation]: Configuring waypoint_follower
[component_container_isolated-18] [INFO] [1783512035.465809503] [waypoint_follower]: Configuring
[competition_master_stage3.py-21] [WARN] [1783512035.479526100] [competition_master_stage3]: 导航目标被拒绝, 3s 后重试...
[component_container_isolated-18] [INFO] [1783512035.608890809] [waypoint_follower]: Created waypoint_task_executor : wait_at_waypoint of type nav2_waypoint_follower::WaitAtWaypoint
[component_container_isolated-18] [INFO] [1783512035.618702819] [lifecycle_manager_navigation]: Configuring velocity_smoother
[component_container_isolated-18] [INFO] [1783512035.620487424] [velocity_smoother]: Configuring velocity smoother
[component_container_isolated-18] [INFO] [1783512035.684950419] [lifecycle_manager_navigation]: Activating controller_server
[component_container_isolated-18] [INFO] [1783512035.688305020] [controller_server]: Activating
[component_container_isolated-18] [INFO] [1783512035.688696008] [local_costmap.local_costmap]: Activating
[component_container_isolated-18] [INFO] [1783512035.688812400] [local_costmap.local_costmap]: Checking transform
[component_container_isolated-18] [INFO] [1783512035.689330034] [local_costmap.local_costmap]: start
[component_container_isolated-18] [INFO] [1783512035.713805450] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512035.730146447] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512035.734041444] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512035.757499640] [local_costmap.local_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[component_container_isolated-18] [INFO] [1783512035.930032443] [controller_server]: Activating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1783512035.930454739] [controller_server]: Creating bond (controller_server) to lifecycle manager.
[competition_master_stage3.py-21] [INFO] [1783512036.051915646] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.00,-0.02) yaw=16deg cmd=(vx=0.00 wz=0.00) elapsed=0.9s cpuFreq=1500MHz cpuT=81C bpuT=78C cpu=87% mem=18%
[component_container_isolated-18] [INFO] [1783512036.061708814] [lifecycle_manager_navigation]: Server controller_server connected with bond.
[component_container_isolated-18] [INFO] [1783512036.061933510] [lifecycle_manager_navigation]: Activating smoother_server
[component_container_isolated-18] [INFO] [1783512036.063350346] [smoother_server]: Activating
[component_container_isolated-18] [INFO] [1783512036.063630612] [smoother_server]: Activating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1783512036.063746253] [smoother_server]: Creating bond (smoother_server) to lifecycle manager.
[racing_obstacle_detection_yolo-19] [WARN] [1783512036.064381823] [ObstacleDetectionNode]: input fps: 11.63, out fps: 12.44, infer time ms: 10, post process time ms: 10
[component_container_isolated-18] [INFO] [1783512036.185234091] [lifecycle_manager_navigation]: Server smoother_server connected with bond.
[component_container_isolated-18] [INFO] [1783512036.185449074] [lifecycle_manager_navigation]: Activating planner_server
[component_container_isolated-18] [INFO] [1783512036.189390511] [planner_server]: Activating
[component_container_isolated-18] [INFO] [1783512036.189814683] [global_costmap.global_costmap]: Activating
[component_container_isolated-18] [INFO] [1783512036.189936244] [global_costmap.global_costmap]: Checking transform
[component_container_isolated-18] [INFO] [1783512036.190327565] [global_costmap.global_costmap]: start
[component_container_isolated-18] [INFO] [1783512036.219745296] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512036.231917825] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512036.232118800] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512036.246490517] [global_costmap.global_costmap]: KeepoutFilter: Received filter mask from /keepout_mask topic.
[rviz2-23] [INFO] [1783512036.399084099] [rviz2]: Trying to create a map of size 60 x 60 using 1 swatches
[racing_obstacle_detection_yolo-19] [WARN] [1783512037.124295730] [ObstacleDetectionNode]: input fps: 13.27, out fps: 13.17, infer time ms: 14, post process time ms: 6
[component_container_isolated-18] [INFO] [1783512037.231791258] [planner_server]: Activating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1783512037.236115814] [planner_server]: Creating bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512037.355397977] [lifecycle_manager_navigation]: Server planner_server connected with bond.
[component_container_isolated-18] [INFO] [1783512037.355591946] [lifecycle_manager_navigation]: Activating behavior_server
[component_container_isolated-18] [INFO] [1783512037.356971699] [behavior_server]: Activating
[component_container_isolated-18] [INFO] [1783512037.357166543] [behavior_server]: Activating spin
[component_container_isolated-18] [INFO] [1783512037.357341753] [behavior_server]: Activating backup
[component_container_isolated-18] [INFO] [1783512037.357427003] [behavior_server]: Activating drive_on_heading
[component_container_isolated-18] [INFO] [1783512037.357500789] [behavior_server]: Activating wait
[component_container_isolated-18] [INFO] [1783512037.357583912] [behavior_server]: Creating bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512037.487378550] [lifecycle_manager_navigation]: Server behavior_server connected with bond.
[component_container_isolated-18] [INFO] [1783512037.487806591] [lifecycle_manager_navigation]: Activating bt_navigator
[component_container_isolated-18] [INFO] [1783512037.489650527] [bt_navigator]: Activating
[component_container_isolated-18] [WARN] [1783512037.685746415] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[rviz2-23] [INFO] [1783512037.729836764] [rviz2]: Trying to create a map of size 163 x 141 using 1 swatches
[component_container_isolated-18] [WARN] [1783512037.835743938] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [WARN] [1783512037.948279036] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[competition_master_stage3.py-21] [INFO] [1783512038.059168746] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.00,-0.02) yaw=16deg cmd=(vx=0.00 wz=0.00) elapsed=2.9s cpuFreq=1500MHz cpuT=81C bpuT=79C cpu=85% mem=18%
[component_container_isolated-18] [WARN] [1783512038.238596496] [bt_navigator_navigate_through_poses_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[racing_obstacle_detection_yolo-19] [WARN] [1783512038.378557859] [ObstacleDetectionNode]: input fps: 12.04, out fps: 8.85, infer time ms: 11, post process time ms: 17
[competition_master_stage3.py-21] [INFO] [1783512038.487156819] [competition_master_stage3]: 重试发送导航目标 (QR点)...
[competition_master_stage3.py-21] [INFO] [1783512038.494023430] [competition_master_stage3]: [DIAG] nav目标距离: 3.97m, robot=(-2.00,-0.02) → target=(0.41,-3.17)
[competition_master_stage3.py-21] [INFO] [1783512038.526681234] [competition_master_stage3]: >>> 发送导航目标 [任务发布点]: (0.41, -3.17, yaw=0.00)
[component_container_isolated-18] [WARN] [1783512038.773001668] [bt_navigator_navigate_to_pose_rclcpp_node]: Wait duration is negative or zero (0). Setting to positive.
[component_container_isolated-18] [INFO] [1783512039.162031088] [bt_navigator]: Creating bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512039.225941618] [bt_navigator]: Begin navigating from current location (-2.00, -0.02) to (0.41, -3.17)
[competition_master_stage3.py-21] [INFO] [1783512039.251189302] [competition_master_stage3]: 导航目标已接受，车辆出发...
[speed_profile_node.py-22] [INFO] [1783512039.300003529] [speed_profile_node]: Plan received: 20 poses, mean|κ|=0.4965 m⁻¹, max|κ|=1.5564 m⁻¹, mean_v=0.452 m/s, min_v=0.351 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512039.370834049] [lifecycle_manager_navigation]: Server bt_navigator connected with bond.
[component_container_isolated-18] [INFO] [1783512039.371038601] [lifecycle_manager_navigation]: Activating waypoint_follower
[component_container_isolated-18] [INFO] [1783512039.376993901] [waypoint_follower]: Activating
[component_container_isolated-18] [INFO] [1783512039.377376409] [waypoint_follower]: Creating bond (waypoint_follower) to lifecycle manager.
[racing_obstacle_detection_yolo-19] [WARN] [1783512039.421349594] [ObstacleDetectionNode]: input fps: 8.88, out fps: 8.56, infer time ms: 11, post process time ms: 8
[component_container_isolated-18] [INFO] [1783512039.436591756] [controller_server]: Received a goal, begin computing control effort.
[component_container_isolated-18] [WARN] [1783512039.437011697] [controller_server]: No goal checker was specified in parameter 'current_goal_checker'. Server will use only plugin loaded goal_checker . This warning will appear once.
[component_container_isolated-18] [INFO] [1783512039.527853055] [lifecycle_manager_navigation]: Server waypoint_follower connected with bond.
[component_container_isolated-18] [INFO] [1783512039.528057439] [lifecycle_manager_navigation]: Activating velocity_smoother
[component_container_isolated-18] [INFO] [1783512039.529456911] [velocity_smoother]: Activating
[component_container_isolated-18] [INFO] [1783512039.529812323] [velocity_smoother]: Creating bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512039.661273002] [lifecycle_manager_navigation]: Server velocity_smoother connected with bond.
[component_container_isolated-18] [INFO] [1783512039.662559339] [lifecycle_manager_navigation]: Managed nodes are active
[component_container_isolated-18] [INFO] [1783512039.662658051] [lifecycle_manager_navigation]: Creating bond timer...
[hobot_codec_republish-13] [WARN] [1783512039.715614876] [vlm_jpeg_encoder]: Sub imgRaw fps [10.47]
[hobot_codec_republish-13] [WARN] [1783512039.721124056] [vlm_jpeg_encoder]: Pub img fps [10.46]
[competition_master_stage3.py-21] [INFO] [1783512040.056184302] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-2.00,-0.02) yaw=16deg cmd=(vx=0.24 wz=-1.12) elapsed=4.9s plan[20pts 4.1m] (-1.98,-0.07)→(0.43,-3.22) cpuFreq=1500MHz cpuT=81C bpuT=79C cpu=50% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512040.501470624] [ObstacleDetectionNode]: input fps: 8.49, out fps: 12.04, infer time ms: 10, post process time ms: 7
[speed_profile_node.py-22] [INFO] [1783512040.561780960] [speed_profile_node]: Plan received: 20 poses, mean|κ|=0.4472 m⁻¹, max|κ|=1.3476 m⁻¹, mean_v=0.456 m/s, min_v=0.368 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512040.737449974] [controller_server]: Passing new path to controller.
[component_container_isolated-18] Reallocing temp weights 301 - 60
[imu_madgwick_filter.py-6] [INFO] [1783512041.361449679] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1541 q_w=0.9402 angle=39.8deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783512041.407178640] [imu_madgwick_filter]: [imu_madgwick ->] msgs=799 q_w=0.9793 angle=23.4deg beta=0.0330
[racing_obstacle_detection_yolo-19] [WARN] [1783512041.553205024] [ObstacleDetectionNode]: input fps: 12.88, out fps: 12.36, infer time ms: 10, post process time ms: 7
[speed_profile_node.py-22] [INFO] [1783512041.869337170] [speed_profile_node]: Plan received: 19 poses, mean|κ|=0.2637 m⁻¹, max|κ|=1.1929 m⁻¹, mean_v=0.474 m/s, min_v=0.382 m/s, max_v=0.500 m/s
[component_container_isolated-18] Reallocing temp weights 1035 - 60
[component_container_isolated-18] [INFO] [1783512042.037388970] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783512042.060851189] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.64,-0.10) yaw=-36deg cmd=(vx=-0.11 wz=-0.32) elapsed=6.9s plan[19pts 3.8m] (-1.68,-0.07)→(0.43,-3.22) cpuFreq=1500MHz cpuT=81C bpuT=79C cpu=100% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512042.589551648] [ObstacleDetectionNode]: input fps: 11.86, out fps: 11.62, infer time ms: 10, post process time ms: 9
[speed_profile_node.py-22] [INFO] [1783512043.175716304] [speed_profile_node]: Plan received: 17 poses, mean|κ|=0.2393 m⁻¹, max|κ|=1.1310 m⁻¹, mean_v=0.476 m/s, min_v=0.388 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512043.337408717] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512043.593319695] [ObstacleDetectionNode]: input fps: 11.28, out fps: 11.90, infer time ms: 10, post process time ms: 5
[imu_madgwick_filter.py-4] [WARN] [1783512044.071111361] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1501s > 0.15s, capping
[competition_master_stage3.py-21] [INFO] [1783512044.081802783] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-1.40,-0.54) yaw=-68deg cmd=(vx=0.39 wz=0.13) elapsed=8.9s plan[17pts 3.5m] (-1.53,-0.37)→(0.43,-3.22) cpuFreq=1500MHz cpuT=81C bpuT=79C cpu=100% mem=19%
[speed_profile_node.py-22] [INFO] [1783512044.447808322] [speed_profile_node]: Plan received: 14 poses, mean|κ|=0.2763 m⁻¹, max|κ|=1.0807 m⁻¹, mean_v=0.473 m/s, min_v=0.392 m/s, max_v=0.500 m/s
[racing_obstacle_detection_yolo-19] [WARN] [1783512044.596300479] [ObstacleDetectionNode]: input fps: 12.25, out fps: 12.97, infer time ms: 10, post process time ms: 5
[component_container_isolated-18] [INFO] [1783512044.637374424] [controller_server]: Passing new path to controller.
[hobot_codec_republish-13] [WARN] [1783512044.874228438] [vlm_jpeg_encoder]: Sub imgRaw fps [11.63]
[hobot_codec_republish-13] [WARN] [1783512044.880397137] [vlm_jpeg_encoder]: Pub img fps [11.63]
[racing_obstacle_detection_yolo-19] [WARN] [1783512045.607869932] [ObstacleDetectionNode]: input fps: 12.29, out fps: 10.91, infer time ms: 10, post process time ms: 8
[speed_profile_node.py-22] [INFO] [1783512045.747311287] [speed_profile_node]: Plan received: 13 poses, mean|κ|=0.3087 m⁻¹, max|κ|=1.1212 m⁻¹, mean_v=0.470 m/s, min_v=0.389 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512045.937407376] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783512046.056537150] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.96,-1.21) yaw=-54deg cmd=(vx=0.39 wz=-0.33) elapsed=10.9s plan[13pts 2.6m] (-1.08,-1.12)→(0.43,-3.22) cpuFreq=1500MHz cpuT=81C bpuT=79C cpu=100% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512046.670584301] [ObstacleDetectionNode]: input fps: 11.40, out fps: 11.32, infer time ms: 10, post process time ms: 11
[speed_profile_node.py-22] [INFO] [1783512047.065913348] [speed_profile_node]: Plan received: 10 poses, mean|κ|=0.3739 m⁻¹, max|κ|=1.0457 m⁻¹, mean_v=0.463 m/s, min_v=0.396 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512047.237394057] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512047.737197706] [ObstacleDetectionNode]: input fps: 11.17, out fps: 10.27, infer time ms: 10, post process time ms: 6
[competition_master_stage3.py-21] [INFO] [1783512048.059094714] [competition_master_stage3]: [DIAG] state=NAV_TO_QR pos=(-0.70,-1.64) yaw=-67deg cmd=(vx=0.29 wz=0.04) elapsed=12.9s plan[10pts 2.1m] (-0.78,-1.57)→(0.43,-3.22) cpuFreq=1500MHz cpuT=81C bpuT=79C cpu=90% mem=19%
[speed_profile_node.py-22] [INFO] [1783512048.422488334] [speed_profile_node]: Plan received: 9 poses, mean|κ|=0.4348 m⁻¹, max|κ|=1.0974 m⁻¹, mean_v=0.457 m/s, min_v=0.391 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512048.537377356] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512048.881931050] [ObstacleDetectionNode]: input fps: 10.37, out fps: 11.42, infer time ms: 10, post process time ms: 12
[qr_decoder-10] [INFO] [1783512048.911987951] [qr_decoder_zbar]: [qr_decoder] QR DETECTED frame=575 symbols=1 (gap=-1 frames)
[qr_decoder-10] [INFO] [1783512048.912467074] [qr_decoder_zbar]: [QR] 1584 | 3D:(-0.337, +0.189, 1.992)m | px(249,237) D:1992mm
[qr_decoder-10] [INFO] [1783512048.914052368] [qr_decoder_zbar]: [QR] 1584 | robot_pos: (0.54, -2.45, yaw=-1.51)
[competition_master_stage3.py-21] [INFO] [1783512048.922909284] [competition_master_stage3]: [QR检测] 内容: 1584
[qr_decision.py-11] [INFO] [1783512048.930414277] [qr_decision]: [QR] 1584 CCW @ (x=0.54, y=-2.46, yaw=-1.51) → /qr_event
[qr_decision.py-11] [INFO] [1783512048.933271049] [qr_decision]: [检查点] qr_decision 发布 /qr_event (由 task_manager 决定停车)
[competition_master_stage3.py-21] [INFO] [1783512048.934244800] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decoder_zbar
[competition_master_stage3.py-21] [INFO] [1783512048.937824237] [competition_master_stage3]: >>> QR 解码已关闭, 等待方向判断 (/qr_event)...
[competition_master_stage3.py-21] [INFO] [1783512048.940831728] [competition_master_stage3]: [QR检测] 取消当前导航目标, 等待BT完成 cancel/halt 清理...
[competition_master_stage3.py-21] [INFO] [1783512048.960091214] [competition_master_stage3]: [QR事件] 方向: 逆时针 (通道巡航阶段使用)
[competition_master_stage3.py-21] [INFO] [1783512048.970785343] [competition_master_stage3]: [KILL] 已发送终止信号: qr_decision
[qr_decoder-10] [INFO] [1783512049.030798082] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-18] [INFO] [1783512049.037378275] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-18] [INFO] [1783512049.037602308] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1783512049.038675374] [bt_navigator]: [navigate_to_pose] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1783512049.039419497] [bt_navigator]: Goal canceled
[competition_master_stage3.py-21] [INFO] [1783512049.175321208] [competition_master_stage3]: [结果回调] BT取消确认完成 (STATUS_CANCELED), 准备发送通道入口目标...
[competition_master_stage3.py-21] [INFO] [1783512049.181087671] [competition_master_stage3]: [状态机] NAV_TO_QR → BACKING_UP
[competition_master_stage3.py-21] [INFO] [1783512049.186182953] [competition_master_stage3]: >>> BT取消完成, 右后退摆正车头→前进进通道...
[competition_master_stage3.py-21] [INFO] [1783512049.194288321] [competition_master_stage3]: [BACKUP] 右后退中: vx=-0.15 wz=0.80, 持续 6.0s...
[imu_madgwick_filter.py-6] [WARN] [1783512049.308365258] [imu_madgwick_bmi088]: [imu_madgwick] dt outlier: 0.1818s > 0.15s, capping
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
[INFO] [qr_decoder-10]: process has finished cleanly [pid 5642]
[racing_obstacle_detection_yolo-19] [WARN] [1783512049.898983768] [ObstacleDetectionNode]: input fps: 10.66, out fps: 8.83, infer time ms: 10, post process time ms: 9
[hobot_codec_republish-13] [WARN] [1783512049.966209965] [vlm_jpeg_encoder]: Sub imgRaw fps [10.81]
[hobot_codec_republish-13] [WARN] [1783512049.978059290] [vlm_jpeg_encoder]: Pub img fps [10.79]
[competition_master_stage3.py-21] [INFO] [1783512050.057843322] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.41,-2.06) yaw=-63deg cmd=(vx=-0.15 wz=0.80) elapsed=14.9s plan[9pts 1.7m] (-0.63,-1.87)→(0.43,-3.22) cpuFreq=1500MHz cpuT=81C bpuT=80C cpu=100% mem=19%
[ERROR] [qr_decision.py-11]: process has died [pid 5644, exit code 1, cmd '/userdata/dev_ws/install/qr_decoder/lib/qr_decoder/qr_decision.py --ros-args -r __node:=qr_decision --params-file /tmp/launch_params_gvpfa3bi'].
[racing_obstacle_detection_yolo-19] [WARN] [1783512050.975738027] [ObstacleDetectionNode]: input fps: 9.03, out fps: 12.04, infer time ms: 10, post process time ms: 5
[imu_madgwick_filter.py-6] [INFO] [1783512051.359470239] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=1865 q_w=0.8247 angle=68.9deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783512051.407724899] [imu_madgwick_filter]: [imu_madgwick ->] msgs=992 q_w=0.9039 angle=50.7deg beta=0.0330
[racing_obstacle_detection_yolo-19] [WARN] [1783512052.024710213] [ObstacleDetectionNode]: input fps: 13.49, out fps: 13.35, infer time ms: 11, post process time ms: 5
[competition_master_stage3.py-21] [INFO] [1783512052.074034124] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.45,-2.00) yaw=-51deg cmd=(vx=-0.15 wz=0.80) elapsed=16.9s plan[9pts 1.7m] (-0.63,-1.87)→(0.43,-3.22) cpuFreq=1500MHz cpuT=81C bpuT=80C cpu=100% mem=18%
[racing_obstacle_detection_yolo-19] [WARN] [1783512053.107334677] [ObstacleDetectionNode]: input fps: 12.68, out fps: 12.03, infer time ms: 10, post process time ms: 7
[competition_master_stage3.py-21] [INFO] [1783512054.048472265] [competition_master_stage3]: [DIAG] state=BACKING_UP pos=(-0.72,-1.85) yaw=4deg cmd=(vx=-0.15 wz=0.80) elapsed=18.9s plan[9pts 1.7m] (-0.63,-1.87)→(0.43,-3.22) cpuFreq=1500MHz cpuT=82C bpuT=80C cpu=77% mem=18%
[racing_obstacle_detection_yolo-19] [WARN] [1783512054.134212268] [ObstacleDetectionNode]: input fps: 12.71, out fps: 12.66, infer time ms: 10, post process time ms: 6
[hobot_codec_republish-13] [WARN] [1783512055.041522412] [vlm_jpeg_encoder]: Sub imgRaw fps [12.41]
[hobot_codec_republish-13] [WARN] [1783512055.045767627] [vlm_jpeg_encoder]: Pub img fps [12.43]
[racing_obstacle_detection_yolo-19] [WARN] [1783512055.170296328] [ObstacleDetectionNode]: input fps: 12.17, out fps: 12.57, infer time ms: 10, post process time ms: 7
[competition_master_stage3.py-21] [INFO] [1783512055.201570345] [competition_master_stage3]: [状态机] BACKING_UP → CRUISE_CHANNEL
[competition_master_stage3.py-21] [INFO] [1783512055.204623605] [competition_master_stage3]: [CRUISE] 方向: CCW (逆时针, even QR), 路点: (1.50,-1.45), (3.02,-1.02), (2.02,0.94) → VLM=(2.02,0.94) → post=(0.96,-0.06)
[competition_master_stage3.py-21] [INFO] [1783512055.214521340] [competition_master_stage3]: [CRUISE] NavigateThroughPoses: (0.33,-1.16), (1.50,-1.45), (3.02,-1.02), (2.02,0.94)
[component_container_isolated-18] [INFO] [1783512055.222916076] [bt_navigator]: Begin navigating from current location through 4 poses to (2.02, 0.94)
[competition_master_stage3.py-21] [INFO] [1783512055.244882771] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[speed_profile_node.py-22] [INFO] [1783512055.301843885] [speed_profile_node]: Plan received: 48 poses, mean|κ|=1.7662 m⁻¹, max|κ|=6.1430 m⁻¹, mean_v=0.362 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512055.426332367] [controller_server]: Received a goal, begin computing control effort.
[competition_master_stage3.py-21] [INFO] [1783512056.058503826] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.89,-1.89) yaw=33deg cmd=(vx=0.24 wz=0.08) elapsed=20.9s plan[48pts 9.4m] (-0.93,-1.87)→(2.08,0.98) cpuFreq=1500MHz cpuT=82C bpuT=80C cpu=42% mem=18%
[racing_obstacle_detection_yolo-19] [WARN] [1783512056.201823454] [ObstacleDetectionNode]: input fps: 12.55, out fps: 11.76, infer time ms: 10, post process time ms: 19
[component_container_isolated-18] [INFO] [1783512056.629188813] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [WARN] [1783512057.208997640] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512057.211386423] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512057.222188889] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512057.227571550] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512057.238284429] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512057.239794063] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512057.279524846] [ObstacleDetectionNode]: input fps: 11.76, out fps: 11.02, infer time ms: 10, post process time ms: 6
[speed_profile_node.py-22] [INFO] [1783512057.764454684] [speed_profile_node]: Plan received: 47 poses, mean|κ|=1.8007 m⁻¹, max|κ|=6.1430 m⁻¹, mean_v=0.359 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512057.929213166] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783512058.051640267] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.81,-1.80) yaw=41deg cmd=(vx=0.23 wz=0.02) elapsed=22.9s plan[47pts 9.2m] (-0.78,-1.72)→(2.08,0.98) cpuFreq=1500MHz cpuT=82C bpuT=80C cpu=100% mem=18%
[racing_obstacle_detection_yolo-19] [WARN] [1783512058.306853462] [ObstacleDetectionNode]: input fps: 11.24, out fps: 12.66, infer time ms: 10, post process time ms: 6
[speed_profile_node.py-22] [INFO] [1783512059.069870523] [speed_profile_node]: Plan received: 46 poses, mean|κ|=1.8466 m⁻¹, max|κ|=6.1430 m⁻¹, mean_v=0.356 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[component_container_isolated-18] [WARN] [1783512059.214721926] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512059.214721426] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512059.229205532] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [INFO] [1783512059.230394087] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512059.242616933] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512059.254351534] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512059.255176740] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512059.316654736] [ObstacleDetectionNode]: input fps: 12.57, out fps: 10.92, infer time ms: 14, post process time ms: 9
[hobot_codec_republish-13] [WARN] [1783512060.044011556] [vlm_jpeg_encoder]: Sub imgRaw fps [12.00]
[hobot_codec_republish-13] [WARN] [1783512060.049423524] [vlm_jpeg_encoder]: Pub img fps [11.99]
[competition_master_stage3.py-21] [INFO] [1783512060.057284805] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.62,-1.65) yaw=36deg cmd=(vx=0.20 wz=-0.16) elapsed=24.9s plan[46pts 8.8m] (-0.48,-1.57)→(2.08,0.98) cpuFreq=1500MHz cpuT=82C bpuT=80C cpu=93% mem=18%
[racing_obstacle_detection_yolo-19] [WARN] [1783512060.348650487] [ObstacleDetectionNode]: input fps: 10.97, out fps: 12.57, infer time ms: 10, post process time ms: 6
[component_container_isolated-18] [INFO] [1783512060.529188851] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [WARN] [1783512061.224358896] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512061.224382241] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512061.235723000] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512061.239290843] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512061.252908100] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512061.253442072] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-6] [INFO] [1783512061.363089269] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2257 q_w=0.9910 angle=15.4deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783512061.405810462] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1191 q_w=0.9499 angle=36.4deg beta=0.0330
[racing_obstacle_detection_yolo-19] [WARN] [1783512061.406377742] [ObstacleDetectionNode]: input fps: 12.58, out fps: 12.30, infer time ms: 10, post process time ms: 6
[speed_profile_node.py-22] [INFO] [1783512061.697649425] [speed_profile_node]: Plan received: 44 poses, mean|κ|=1.9368 m⁻¹, max|κ|=6.1430 m⁻¹, mean_v=0.348 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512061.829171035] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783512062.049619021] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(-0.16,-1.36) yaw=31deg cmd=(vx=0.30 wz=-0.13) elapsed=26.9s plan[44pts 8.5m] (-0.17,-1.42)→(2.08,0.98) cpuFreq=1500MHz cpuT=82C bpuT=80C cpu=100% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512062.464913353] [ObstacleDetectionNode]: input fps: 12.48, out fps: 11.34, infer time ms: 10, post process time ms: 6
[speed_profile_node.py-22] [INFO] [1783512063.018304770] [speed_profile_node]: Plan received: 38 poses, mean|κ|=1.4760 m⁻¹, max|κ|=4.4343 m⁻¹, mean_v=0.368 m/s, min_v=0.201 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512063.129198106] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [WARN] [1783512063.216599001] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512063.217312414] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512063.236501950] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512063.236681491] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512063.276848139] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512063.284267943] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512063.525381298] [ObstacleDetectionNode]: input fps: 10.76, out fps: 12.26, infer time ms: 11, post process time ms: 6
[competition_master_stage3.py-21] [INFO] [1783512064.074797588] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.31,-1.07) yaw=19deg cmd=(vx=0.09 wz=0.12) elapsed=28.9s plan[38pts 7.4m] (0.13,-1.27)→(2.08,0.98) cpuFreq=1500MHz cpuT=82C bpuT=80C cpu=90% mem=18%
[speed_profile_node.py-22] [INFO] [1783512064.291203871] [speed_profile_node]: Plan received: 39 poses, mean|κ|=2.0794 m⁻¹, max|κ|=4.8039 m⁻¹, mean_v=0.335 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512064.429188132] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512064.555071260] [ObstacleDetectionNode]: input fps: 12.43, out fps: 11.66, infer time ms: 10, post process time ms: 6
[hobot_codec_republish-13] [WARN] [1783512065.054400020] [vlm_jpeg_encoder]: Sub imgRaw fps [12.38]
[hobot_codec_republish-13] [WARN] [1783512065.057510120] [vlm_jpeg_encoder]: Pub img fps [12.38]
[component_container_isolated-18] [WARN] [1783512065.212550315] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512065.216285853] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512065.225296432] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512065.232743583] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512065.251644373] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512065.254077596] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[speed_profile_node.py-22] [INFO] [1783512065.581762212] [speed_profile_node]: Plan received: 37 poses, mean|κ|=1.6801 m⁻¹, max|κ|=4.4343 m⁻¹, mean_v=0.353 m/s, min_v=0.201 m/s, max_v=0.500 m/s
[racing_obstacle_detection_yolo-19] [WARN] [1783512065.652541987] [ObstacleDetectionNode]: input fps: 11.63, out fps: 11.85, infer time ms: 11, post process time ms: 6
[component_container_isolated-18] [INFO] [1783512065.729181223] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783512066.051645949] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.63,-0.95) yaw=25deg cmd=(vx=0.20 wz=-0.50) elapsed=30.9s plan[37pts 7.2m] (0.58,-0.97)→(2.08,0.98) cpuFreq=1500MHz cpuT=82C bpuT=80C cpu=80% mem=19%
[component_container_isolated-18] Reallocing temp weights 1500 - 60
[racing_obstacle_detection_yolo-19] [WARN] [1783512066.725487068] [ObstacleDetectionNode]: input fps: 13.11, out fps: 13.11, infer time ms: 10, post process time ms: 10
[speed_profile_node.py-22] [INFO] [1783512066.878062349] [speed_profile_node]: Plan received: 37 poses, mean|κ|=2.1459 m⁻¹, max|κ|=4.8039 m⁻¹, mean_v=0.330 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512067.029178814] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [WARN] [1783512067.209803245] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512067.210235296] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512067.220133660] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512067.235186540] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512067.235443728] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512067.249460811] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512067.775145135] [ObstacleDetectionNode]: input fps: 11.43, out fps: 11.43, infer time ms: 10, post process time ms: 9
[competition_master_stage3.py-21] [INFO] [1783512068.052280951] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(0.98,-0.88) yaw=-14deg cmd=(vx=0.20 wz=-0.28) elapsed=32.9s plan[37pts 7.2m] (0.88,-0.82)→(2.08,0.98) cpuFreq=1500MHz cpuT=82C bpuT=80C cpu=85% mem=19%
[speed_profile_node.py-22] [INFO] [1783512068.188173245] [speed_profile_node]: Plan received: 35 poses, mean|κ|=1.8351 m⁻¹, max|κ|=4.8781 m⁻¹, mean_v=0.346 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512068.329202527] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512068.785522132] [ObstacleDetectionNode]: input fps: 10.87, out fps: 10.86, infer time ms: 10, post process time ms: 6
[component_container_isolated-18] [WARN] [1783512069.210215223] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512069.211509718] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512069.220819860] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512069.244445183] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512069.247222995] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512069.281753819] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[speed_profile_node.py-22] [INFO] [1783512069.460721271] [speed_profile_node]: Plan received: 34 poses, mean|κ|=2.2114 m⁻¹, max|κ|=4.8039 m⁻¹, mean_v=0.326 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512069.629345519] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512069.869676594] [ObstacleDetectionNode]: input fps: 12.04, out fps: 12.05, infer time ms: 10, post process time ms: 11
[competition_master_stage3.py-21] [INFO] [1783512070.053100576] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.32,-0.99) yaw=-20deg cmd=(vx=0.20 wz=-0.59) elapsed=34.9s plan[34pts 6.5m] (1.33,-0.97)→(2.08,0.98) cpuFreq=1500MHz cpuT=82C bpuT=80C cpu=81% mem=19%
[hobot_codec_republish-13] [WARN] [1783512070.115856000] [vlm_jpeg_encoder]: Sub imgRaw fps [11.66]
[hobot_codec_republish-13] [WARN] [1783512070.119107540] [vlm_jpeg_encoder]: Pub img fps [11.66]
[speed_profile_node.py-22] [INFO] [1783512070.800066143] [speed_profile_node]: Plan received: 35 poses, mean|κ|=2.2928 m⁻¹, max|κ|=4.8039 m⁻¹, mean_v=0.321 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512070.929203961] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512070.933330285] [ObstacleDetectionNode]: input fps: 12.17, out fps: 12.17, infer time ms: 10, post process time ms: 5
[component_container_isolated-18] [WARN] [1783512071.209066774] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512071.216588851] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512071.222186362] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512071.237133232] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512071.257698537] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512071.281124203] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-6] [INFO] [1783512071.358775726] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=2632 q_w=0.8621 angle=60.9deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783512071.407819429] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1387 q_w=0.9564 angle=34.0deg beta=0.0330
[racing_obstacle_detection_yolo-19] [WARN] [1783512071.977968264] [ObstacleDetectionNode]: input fps: 11.61, out fps: 11.61, infer time ms: 10, post process time ms: 15
[speed_profile_node.py-22] [INFO] [1783512072.052934318] [speed_profile_node]: Plan received: 30 poses, mean|κ|=2.1560 m⁻¹, max|κ|=5.1189 m⁻¹, mean_v=0.335 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[competition_master_stage3.py-21] [INFO] [1783512072.077221110] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.59,-1.16) yaw=-61deg cmd=(vx=0.20 wz=-0.64) elapsed=36.9s plan[35pts 6.7m] (1.48,-0.97)→(2.08,0.98) cpuFreq=1500MHz cpuT=82C bpuT=80C cpu=93% mem=19%
[component_container_isolated-18] [INFO] [1783512072.229190703] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512073.000717990] [ObstacleDetectionNode]: input fps: 11.63, out fps: 11.63, infer time ms: 10, post process time ms: 6
[component_container_isolated-18] [WARN] [1783512073.209703922] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512073.209876522] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512073.216481499] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512073.226178520] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512073.244803343] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512073.252979726] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[speed_profile_node.py-22] [INFO] [1783512073.354299316] [speed_profile_node]: Plan received: 27 poses, mean|κ|=1.4513 m⁻¹, max|κ|=3.7958 m⁻¹, mean_v=0.370 m/s, min_v=0.223 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512073.529265746] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512074.014656334] [ObstacleDetectionNode]: input fps: 11.85, out fps: 11.83, infer time ms: 10, post process time ms: 6
[competition_master_stage3.py-21] [INFO] [1783512074.052906523] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.66,-1.38) yaw=-77deg cmd=(vx=0.33 wz=-0.27) elapsed=38.9s plan[27pts 5.6m] (1.63,-1.42)→(2.08,0.98) cpuFreq=1500MHz cpuT=82C bpuT=80C cpu=70% mem=19%
[speed_profile_node.py-22] [INFO] [1783512074.673719754] [speed_profile_node]: Plan received: 27 poses, mean|κ|=1.4295 m⁻¹, max|κ|=3.6234 m⁻¹, mean_v=0.370 m/s, min_v=0.230 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512074.829201778] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512075.147035126] [ObstacleDetectionNode]: input fps: 11.50, out fps: 11.50, infer time ms: 10, post process time ms: 8
[hobot_codec_republish-13] [WARN] [1783512075.173097578] [vlm_jpeg_encoder]: Sub imgRaw fps [11.87]
[hobot_codec_republish-13] [WARN] [1783512075.182691363] [vlm_jpeg_encoder]: Pub img fps [11.85]
[component_container_isolated-18] [WARN] [1783512075.211456086] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512075.211470840] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512075.236240258] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512075.241254594] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512075.255318918] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512075.267741639] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[speed_profile_node.py-22] [INFO] [1783512075.964807701] [speed_profile_node]: Plan received: 25 poses, mean|κ|=1.5005 m⁻¹, max|κ|=3.8154 m⁻¹, mean_v=0.366 m/s, min_v=0.223 m/s, max_v=0.500 m/s
[competition_master_stage3.py-21] [INFO] [1783512076.052720722] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.94,-1.94) yaw=-50deg cmd=(vx=0.33 wz=0.54) elapsed=40.9s plan[25pts 5.1m] (1.93,-1.87)→(2.08,0.98) cpuFreq=1500MHz cpuT=83C bpuT=81C cpu=66% mem=19%
[component_container_isolated-18] [INFO] [1783512076.229201163] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512076.266321278] [ObstacleDetectionNode]: input fps: 10.72, out fps: 10.71, infer time ms: 10, post process time ms: 7
[component_container_isolated-18] [WARN] [1783512077.216302117] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512077.217230726] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[speed_profile_node.py-22] [INFO] [1783512077.258843473] [speed_profile_node]: Plan received: 23 poses, mean|κ|=1.3346 m⁻¹, max|κ|=3.4891 m⁻¹, mean_v=0.379 m/s, min_v=0.236 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512077.273688678] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512077.288550347] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512077.299862835] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512077.302132593] [ObstacleDetectionNode]: input fps: 11.62, out fps: 11.61, infer time ms: 10, post process time ms: 8
[component_container_isolated-18] [WARN] [1783512077.306565536] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512077.429195453] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783512078.052680826] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.39,-2.15) yaw=-7deg cmd=(vx=0.23 wz=0.81) elapsed=42.9s plan[23pts 4.7m] (2.23,-2.17)→(2.08,0.98) cpuFreq=1500MHz cpuT=83C bpuT=81C cpu=87% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512078.500283417] [ObstacleDetectionNode]: input fps: 10.99, out fps: 10.84, infer time ms: 28, post process time ms: 7
[speed_profile_node.py-22] [INFO] [1783512078.551147207] [speed_profile_node]: Plan received: 22 poses, mean|κ|=1.4150 m⁻¹, max|κ|=3.7498 m⁻¹, mean_v=0.374 m/s, min_v=0.225 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512078.729175285] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [WARN] [1783512079.211091684] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512079.211391726] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512079.215008444] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512079.243969575] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512079.248473875] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512079.268092563] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[speed_profile_node.py-22] [INFO] [1783512079.857245082] [speed_profile_node]: Plan received: 21 poses, mean|κ|=1.4892 m⁻¹, max|κ|=3.7771 m⁻¹, mean_v=0.371 m/s, min_v=0.224 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512080.029201705] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783512080.050465620] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.78,-2.04) yaw=31deg cmd=(vx=0.33 wz=0.45) elapsed=44.9s plan[21pts 4.2m] (2.68,-2.02)→(2.08,0.98) cpuFreq=1500MHz cpuT=82C bpuT=80C cpu=71% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512080.200666098] [ObstacleDetectionNode]: input fps: 12.09, out fps: 0.59, infer time ms: 17, post process time ms: 23
[hobot_codec_republish-13] [WARN] [1783512080.264765550] [vlm_jpeg_encoder]: Sub imgRaw fps [11.99]
[hobot_codec_republish-13] [WARN] [1783512080.270412285] [vlm_jpeg_encoder]: Pub img fps [11.99]
[speed_profile_node.py-22] [INFO] [1783512081.173563471] [speed_profile_node]: Plan received: 19 poses, mean|κ|=1.6135 m⁻¹, max|κ|=4.0138 m⁻¹, mean_v=0.362 m/s, min_v=0.215 m/s, max_v=0.500 m/s
[component_container_isolated-18] [WARN] [1783512081.217461820] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512081.217484242] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[racing_obstacle_detection_yolo-19] [WARN] [1783512081.237335658] [ObstacleDetectionNode]: input fps: 9.91, out fps: 12.48, infer time ms: 10, post process time ms: 17
[component_container_isolated-18] [INFO] [1783512081.243601969] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512081.248148870] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512081.261311239] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512081.270499733] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-6] [INFO] [1783512081.359377256] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3008 q_w=0.9513 angle=35.9deg beta=0.0030
[component_container_isolated-18] [INFO] [1783512081.429197822] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-4] [INFO] [1783512081.431997265] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1584 q_w=0.8354 angle=66.7deg beta=0.0330
[competition_master_stage3.py-21] [INFO] [1783512082.058821450] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.08,-1.73) yaw=47deg cmd=(vx=0.25 wz=1.02) elapsed=46.9s plan[19pts 3.7m] (3.13,-1.72)→(2.08,0.98) cpuFreq=1500MHz cpuT=83C bpuT=81C cpu=88% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512082.251610899] [ObstacleDetectionNode]: input fps: 11.55, out fps: 11.73, infer time ms: 11, post process time ms: 7
[speed_profile_node.py-22] [INFO] [1783512082.475010842] [speed_profile_node]: Plan received: 18 poses, mean|κ|=1.5322 m⁻¹, max|κ|=3.7382 m⁻¹, mean_v=0.367 m/s, min_v=0.226 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512082.629261406] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [WARN] [1783512083.211515231] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512083.211578288] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512083.221856737] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512083.235979633] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512083.247816298] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512083.257496850] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512083.320890049] [ObstacleDetectionNode]: input fps: 11.64, out fps: 10.31, infer time ms: 10, post process time ms: 9
[component_container_isolated-18] [WARN] [1783512083.630441302] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512083.729991158] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512083.738903437] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512083.739788030] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.02, 0.94)
[component_container_isolated-18] [WARN] [1783512083.739956738] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1783512083.830429024] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [INFO] [1783512083.924487819] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [WARN] [1783512083.930166135] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [INFO] [1783512083.947917341] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512083.967800989] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512083.967948525] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512083.968860708] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1783512083.969667740] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1783512083.981953767] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512084.030719049] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[competition_master_stage3.py-21] [INFO] [1783512084.067673565] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.24,-1.18) yaw=100deg cmd=(vx=0.00 wz=0.19) elapsed=48.9s plan[18pts 3.6m] (3.13,-1.57)→(2.08,0.98) cpuFreq=1500MHz cpuT=83C bpuT=81C cpu=100% mem=19%
[component_container_isolated-18] [WARN] [1783512084.130448943] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512084.230158249] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512084.230495413] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512084.241667993] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.02, 0.94)
[component_container_isolated-18] [WARN] [1783512084.245693119] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1783512084.330064728] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[racing_obstacle_detection_yolo-19] [WARN] [1783512084.352756011] [ObstacleDetectionNode]: input fps: 10.92, out fps: 12.57, infer time ms: 10, post process time ms: 6
[component_container_isolated-18] [INFO] [1783512084.429197146] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-18] [INFO] [1783512084.429456083] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1783512084.431589592] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1783512084.457945498] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512084.469425943] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512084.481746504] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512084.482373404] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512084.483197850] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512084.495055135] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512084.495208046] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512084.496284303] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1783512084.496545907] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1783512084.522513971] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512084.544638119] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512084.730641951] [behavior_server]: Running backup
[component_container_isolated-18] [INFO] [1783512084.734128323] [behavior_server]: DriveOnHeading: no acceleration or deceleration limits set
[component_container_isolated-18] [WARN] [1783512084.739635719] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1783512084.739810511] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1783512084.740238863] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1783512085.033215674] [behavior_server]: Running wait
[component_container_isolated-18] [WARN] [1783512085.220835537] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512085.223829146] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512085.242102582] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512085.250506068] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512085.257770540] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512085.262853299] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[hobot_codec_republish-13] [WARN] [1783512085.307044439] [vlm_jpeg_encoder]: Sub imgRaw fps [11.90]
[hobot_codec_republish-13] [WARN] [1783512085.311648838] [vlm_jpeg_encoder]: Pub img fps [11.91]
[racing_obstacle_detection_yolo-19] [WARN] [1783512085.425525682] [ObstacleDetectionNode]: input fps: 11.85, out fps: 10.27, infer time ms: 10, post process time ms: 7
[competition_master_stage3.py-21] [INFO] [1783512086.063777675] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.24,-1.18) yaw=100deg cmd=(vx=0.00 wz=0.00) elapsed=50.9s plan[18pts 3.6m] (3.13,-1.57)→(2.08,0.98) cpuFreq=1500MHz cpuT=83C bpuT=81C cpu=85% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512086.500017857] [ObstacleDetectionNode]: input fps: 9.92, out fps: 11.19, infer time ms: 10, post process time ms: 9
[component_container_isolated-18] [WARN] [1783512087.213476444] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512087.213955298] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512087.239023330] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512087.253655677] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512087.258603752] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512087.291418426] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512087.558096388] [ObstacleDetectionNode]: input fps: 11.45, out fps: 10.38, infer time ms: 10, post process time ms: 7
[component_container_isolated-18] [INFO] [1783512088.034957866] [behavior_server]: wait completed successfully
[competition_master_stage3.py-21] [INFO] [1783512088.057579125] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.24,-1.18) yaw=100deg cmd=(vx=0.00 wz=0.00) elapsed=52.9s plan[18pts 3.6m] (3.13,-1.57)→(2.08,0.98) cpuFreq=1500MHz cpuT=83C bpuT=81C cpu=87% mem=19%
[component_container_isolated-18] [WARN] [1783512088.334339633] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512088.338968440] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.02, 0.94)
[component_container_isolated-18] [WARN] [1783512088.343209707] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1783512088.523992985] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512088.539136837] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512088.548300932] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512088.549576950] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512088.548799953] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1783512088.551863306] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1783512088.563778688] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512088.598693865] [ObstacleDetectionNode]: input fps: 10.91, out fps: 13.45, infer time ms: 10, post process time ms: 6
[component_container_isolated-18] [WARN] [1783512089.210817631] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512089.211156242] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (2.02, 0.94)
[component_container_isolated-18] [WARN] [1783512089.211276433] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1783512089.213385864] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512089.213997489] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[competition_master_stage3.py-21] [WARN] [1783512089.224097678] [competition_master_stage3]: [STUCK] 卡死检测: 4秒位移=0.000m, YOLO检测到锥桶, 软化禁区 clip 绕行!
[competition_master_stage3.py-21] [INFO] [1783512089.228473031] [competition_master_stage3]: [KEEPOUT] 软化禁区 → /keepout_mask_soft (可穿高成本, clip绕锥桶)
[component_container_isolated-18] [INFO] [1783512089.243815333] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512089.250352335] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512089.261636599] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512089.261873856] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512089.285685889] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512089.285920687] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512089.318882631] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512089.334976878] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512089.337669804] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1783512089.362641990] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512089.390554861] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512089.391318809] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512089.402596113] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512089.424206279] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512089.448360132] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512089.461982999] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512089.462144241] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512089.463425461] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1783512089.463683388] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1783512089.476839577] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512089.626290826] [behavior_server]: Running backup
[component_container_isolated-18] [WARN] [1783512089.634870663] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1783512089.639681104] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1783512089.639825842] [behavior_server]: [backup] [ActionServer] Aborting handle.
[racing_obstacle_detection_yolo-19] [WARN] [1783512089.683609915] [ObstacleDetectionNode]: input fps: 13.67, out fps: 11.07, infer time ms: 10, post process time ms: 7
[component_container_isolated-18] [INFO] [1783512089.923958156] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1783512089.943737614] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512089.956034877] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512089.956070968] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512089.957312097] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512089.981515959] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [WARN] [1783512089.988228539] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512090.000818237] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512090.001120757] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512090.009116183] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1783512090.009648250] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1783512090.031806092] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783512090.069842723] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.24,-1.18) yaw=100deg cmd=(vx=0.00 wz=0.00) elapsed=54.9s plan[18pts 3.6m] (3.13,-1.57)→(2.08,0.98) cpuFreq=1500MHz cpuT=83C bpuT=81C cpu=50% mem=19%
[component_container_isolated-18] [INFO] [1783512090.224752379] [behavior_server]: Running backup
[hobot_codec_republish-13] [WARN] [1783512090.385057808] [vlm_jpeg_encoder]: Sub imgRaw fps [11.82]
[hobot_codec_republish-13] [WARN] [1783512090.390800066] [vlm_jpeg_encoder]: Pub img fps [11.82]
[racing_obstacle_detection_yolo-19] [WARN] [1783512090.738839921] [ObstacleDetectionNode]: input fps: 10.89, out fps: 12.39, infer time ms: 11, post process time ms: 12
[component_container_isolated-18] [WARN] [1783512091.219483648] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512091.219803168] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512091.238439568] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512091.243809053] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[competition_master_stage3.py-21] [WARN] [1783512091.249026802] [competition_master_stage3]: [STUCK] 软化后仍卡死 (4秒位移=0.000m) → 直驱倒车脱困
[competition_master_stage3.py-21] [WARN] [1783512091.258153465] [competition_master_stage3]: [ESCAPE] 直驱倒车脱困 #1: vx=-0.12 dist=0.40m dur=3.3s
[component_container_isolated-18] [WARN] [1783512091.263008727] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512091.267747801] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512091.325396708] [behavior_server]: Canceling backup
[component_container_isolated-18] [INFO] [1783512091.325805369] [behavior_server]: [backup] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1783512091.331882032] [bt_navigator]: [navigate_through_poses] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1783512091.332703106] [bt_navigator]: Goal canceled
[competition_master_stage3.py-21] [WARN] [1783512091.353855862] [competition_master_stage3]: NavigateThroughPoses 失败 status=5
[imu_madgwick_filter.py-6] [INFO] [1783512091.358881573] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3353 q_w=0.6871 angle=93.2deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783512091.409215039] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1783 q_w=0.4319 angle=128.8deg beta=0.0330
[racing_obstacle_detection_yolo-19] [WARN] [1783512091.783461237] [ObstacleDetectionNode]: input fps: 11.94, out fps: 11.45, infer time ms: 10, post process time ms: 9
[competition_master_stage3.py-21] [INFO] [1783512092.051093031] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.24,-1.18) yaw=100deg cmd=(vx=-0.12 wz=0.00) elapsed=56.9s plan[18pts 3.6m] (3.13,-1.57)→(2.08,0.98) cpuFreq=1500MHz cpuT=83C bpuT=81C cpu=100% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512092.844800030] [ObstacleDetectionNode]: input fps: 11.68, out fps: 12.43, infer time ms: 10, post process time ms: 23
[component_container_isolated-18] [WARN] [1783512093.219157381] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512093.219233437] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512093.241806694] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512093.248493935] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512093.257629240] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512093.258533652] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512093.908381420] [ObstacleDetectionNode]: input fps: 12.44, out fps: 11.13, infer time ms: 10, post process time ms: 8
[competition_master_stage3.py-21] [INFO] [1783512094.051367436] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.24,-1.15) yaw=107deg cmd=(vx=-0.12 wz=0.00) elapsed=58.9s plan[18pts 3.6m] (3.13,-1.57)→(2.08,0.98) cpuFreq=1500MHz cpuT=83C bpuT=81C cpu=75% mem=19%
[competition_master_stage3.py-21] [WARN] [1783512094.594600032] [competition_master_stage3]: [ESCAPE] 倒车完成, 软禁区保持 → 重发目标 (CRUISE_CHANNEL)
[competition_master_stage3.py-21] [INFO] [1783512094.597642813] [competition_master_stage3]: [CRUISE] 方向: CCW (逆时针, even QR), 路点: (1.50,-1.45), (3.02,-1.02), (2.02,0.94) → VLM=(2.02,0.94) → post=(0.96,-0.06)
[competition_master_stage3.py-21] [INFO] [1783512094.612475857] [competition_master_stage3]: [CRUISE] NavigateThroughPoses: (1.50,-1.45), (3.02,-1.02), (2.02,0.94)
[component_container_isolated-18] [INFO] [1783512094.618387138] [bt_navigator]: Begin navigating from current location through 3 poses to (2.02, 0.94)
[competition_master_stage3.py-21] [INFO] [1783512094.644590457] [competition_master_stage3]: NavigateThroughPoses 已接受, 巡航中...
[speed_profile_node.py-22] [INFO] [1783512094.669501717] [speed_profile_node]: Plan received: 39 poses, mean|κ|=1.1887 m⁻¹, max|κ|=3.8469 m⁻¹, mean_v=0.400 m/s, min_v=0.221 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512094.826068934] [controller_server]: Received a goal, begin computing control effort.
[racing_obstacle_detection_yolo-19] [WARN] [1783512094.917539091] [ObstacleDetectionNode]: input fps: 11.37, out fps: 11.93, infer time ms: 10, post process time ms: 11
[hobot_codec_republish-13] [WARN] [1783512095.482524529] [vlm_jpeg_encoder]: Sub imgRaw fps [12.36]
[hobot_codec_republish-13] [WARN] [1783512095.485548374] [vlm_jpeg_encoder]: Pub img fps [12.37]
[racing_obstacle_detection_yolo-19] [WARN] [1783512095.921420155] [ObstacleDetectionNode]: input fps: 11.99, out fps: 12.91, infer time ms: 10, post process time ms: 7
[speed_profile_node.py-22] [INFO] [1783512095.955066978] [speed_profile_node]: Plan received: 30 poses, mean|κ|=0.6228 m⁻¹, max|κ|=2.0660 m⁻¹, mean_v=0.440 m/s, min_v=0.313 m/s, max_v=0.500 m/s
[competition_master_stage3.py-21] [INFO] [1783512096.057482165] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.31,-1.36) yaw=108deg cmd=(vx=0.20 wz=-0.77) elapsed=60.9s plan[30pts 5.9m] (3.43,-1.57)→(2.08,0.98) cpuFreq=1500MHz cpuT=84C bpuT=82C cpu=75% mem=19%
[component_container_isolated-18] [INFO] [1783512096.126934803] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [WARN] [1783512096.607559405] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512096.608737640] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512096.615895517] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512096.632792486] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512096.644010110] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512096.645223934] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512097.000514935] [ObstacleDetectionNode]: input fps: 10.88, out fps: 11.12, infer time ms: 10, post process time ms: 7
[speed_profile_node.py-22] [INFO] [1783512097.262770964] [speed_profile_node]: Plan received: 29 poses, mean|κ|=0.5798 m⁻¹, max|κ|=1.5813 m⁻¹, mean_v=0.443 m/s, min_v=0.349 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512097.426469844] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783512098.066892526] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.33,-1.71) yaw=79deg cmd=(vx=-0.02 wz=-1.27) elapsed=62.9s plan[29pts 5.8m] (3.28,-1.57)→(2.08,0.98) cpuFreq=1500MHz cpuT=84C bpuT=81C cpu=60% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512098.076086061] [ObstacleDetectionNode]: input fps: 11.20, out fps: 11.20, infer time ms: 10, post process time ms: 11
[speed_profile_node.py-22] [INFO] [1783512098.598678171] [speed_profile_node]: Plan received: 29 poses, mean|κ|=0.5962 m⁻¹, max|κ|=1.7035 m⁻¹, mean_v=0.442 m/s, min_v=0.339 m/s, max_v=0.500 m/s
[component_container_isolated-18] [WARN] [1783512098.606368058] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512098.609034217] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512098.634483204] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512098.644886133] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512098.645851906] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512098.659664691] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512098.826516198] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512099.113620762] [ObstacleDetectionNode]: input fps: 12.50, out fps: 12.49, infer time ms: 10, post process time ms: 7
[speed_profile_node.py-22] [INFO] [1783512099.860706649] [speed_profile_node]: Plan received: 29 poses, mean|κ|=0.6039 m⁻¹, max|κ|=1.7821 m⁻¹, mean_v=0.442 m/s, min_v=0.333 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512100.026490824] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783512100.072811928] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.31,-1.79) yaw=67deg cmd=(vx=-0.30 wz=-0.89) elapsed=64.9s plan[29pts 5.8m] (3.28,-1.72)→(2.08,0.98) cpuFreq=1500MHz cpuT=84C bpuT=81C cpu=100% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512100.182885778] [ObstacleDetectionNode]: input fps: 12.16, out fps: 12.15, infer time ms: 10, post process time ms: 6
[hobot_codec_republish-13] [WARN] [1783512100.496450507] [vlm_jpeg_encoder]: Sub imgRaw fps [11.97]
[hobot_codec_republish-13] [WARN] [1783512100.503392634] [vlm_jpeg_encoder]: Pub img fps [11.96]
[component_container_isolated-18] [WARN] [1783512100.607465660] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512100.607720488] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512100.619913290] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512100.625161756] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512100.634832944] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512100.648914519] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[speed_profile_node.py-22] [INFO] [1783512101.159500999] [speed_profile_node]: Plan received: 28 poses, mean|κ|=0.5186 m⁻¹, max|κ|=1.4848 m⁻¹, mean_v=0.449 m/s, min_v=0.357 m/s, max_v=0.500 m/s
[racing_obstacle_detection_yolo-19] [WARN] [1783512101.249237762] [ObstacleDetectionNode]: input fps: 12.20, out fps: 12.20, infer time ms: 11, post process time ms: 6
[component_container_isolated-18] [INFO] [1783512101.326525403] [controller_server]: Passing new path to controller.
[imu_madgwick_filter.py-6] [INFO] [1783512101.373365812] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=3713 q_w=0.9956 angle=10.8deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783512101.406363944] [imu_madgwick_filter]: [imu_madgwick ->] msgs=1983 q_w=0.9096 angle=49.1deg beta=0.0330
[competition_master_stage3.py-21] [INFO] [1783512102.061554986] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.05,-2.02) yaw=13deg cmd=(vx=-0.30 wz=-1.21) elapsed=66.9s plan[28pts 5.6m] (3.13,-1.87)→(2.08,0.98) cpuFreq=1500MHz cpuT=84C bpuT=82C cpu=71% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512102.313724874] [ObstacleDetectionNode]: input fps: 13.18, out fps: 13.20, infer time ms: 10, post process time ms: 9
[speed_profile_node.py-22] [INFO] [1783512102.458883192] [speed_profile_node]: Plan received: 26 poses, mean|κ|=0.4242 m⁻¹, max|κ|=1.4848 m⁻¹, mean_v=0.459 m/s, min_v=0.357 m/s, max_v=0.500 m/s
[component_container_isolated-18] [WARN] [1783512102.613640392] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512102.613678481] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512102.626497341] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [INFO] [1783512102.632822073] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512102.636913210] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512102.648737644] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512102.659390919] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512103.344876368] [ObstacleDetectionNode]: input fps: 12.63, out fps: 12.62, infer time ms: 10, post process time ms: 10
[speed_profile_node.py-22] [INFO] [1783512103.754886692] [speed_profile_node]: Plan received: 25 poses, mean|κ|=0.4313 m⁻¹, max|κ|=1.4848 m⁻¹, mean_v=0.458 m/s, min_v=0.357 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512103.926504281] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783512104.066157392] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.50,-1.89) yaw=-21deg cmd=(vx=-0.30 wz=-0.21) elapsed=68.9s plan[25pts 5.0m] (2.53,-1.87)→(2.08,0.98) cpuFreq=1500MHz cpuT=84C bpuT=82C cpu=75% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512104.374621642] [ObstacleDetectionNode]: input fps: 12.71, out fps: 12.57, infer time ms: 21, post process time ms: 6
[component_container_isolated-18] [WARN] [1783512104.600362105] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512104.600408028] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512104.614248374] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512104.626464555] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask_soft" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512104.635911342] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512104.646029881] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask_soft topic. Updating old filter mask.
[speed_profile_node.py-22] [INFO] [1783512104.949844414] [speed_profile_node]: Plan received: 23 poses, mean|κ|=0.4664 m⁻¹, max|κ|=1.4848 m⁻¹, mean_v=0.454 m/s, min_v=0.357 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512105.126524019] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512105.403960860] [ObstacleDetectionNode]: input fps: 12.51, out fps: 12.66, infer time ms: 10, post process time ms: 7
[hobot_codec_republish-13] [WARN] [1783512105.547568889] [vlm_jpeg_encoder]: Sub imgRaw fps [12.48]
[hobot_codec_republish-13] [WARN] [1783512105.550961852] [vlm_jpeg_encoder]: Pub img fps [12.48]
[competition_master_stage3.py-21] [INFO] [1783512105.605979612] [competition_master_stage3]: [KEEPOUT] 恢复硬 keepout (/keepout_mask) → 回到环道
[component_container_isolated-18] [WARN] [1783512105.607657446] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512105.608087624] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512105.631039854] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512105.631712979] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512105.655374547] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512105.659707420] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512105.727510186] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512105.828518208] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512105.927972245] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512106.028817554] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[competition_master_stage3.py-21] [INFO] [1783512106.054116574] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.96,-1.66) yaw=-30deg cmd=(vx=0.00 wz=0.00) elapsed=70.9s plan[23pts 4.7m] (2.23,-1.72)→(2.08,0.98) cpuFreq=1500MHz cpuT=84C bpuT=82C cpu=25% mem=19%
[component_container_isolated-18] [WARN] [1783512106.128981720] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512106.227914614] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[speed_profile_node.py-22] [INFO] [1783512106.249838940] [speed_profile_node]: Plan received: 27 poses, mean|κ|=1.3144 m⁻¹, max|κ|=3.6450 m⁻¹, mean_v=0.382 m/s, min_v=0.229 m/s, max_v=0.500 m/s
[component_container_isolated-18] [WARN] [1783512106.327716487] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[racing_obstacle_detection_yolo-19] [WARN] [1783512106.413291703] [ObstacleDetectionNode]: input fps: 11.89, out fps: 11.88, infer time ms: 12, post process time ms: 6
[component_container_isolated-18] [INFO] [1783512106.426499405] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [WARN] [1783512106.602776032] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512106.602780866] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512106.617355023] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512106.617418530] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512106.632307975] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512106.638699613] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512107.474148865] [ObstacleDetectionNode]: input fps: 12.28, out fps: 12.29, infer time ms: 10, post process time ms: 8
[component_container_isolated-18] [WARN] [1783512107.526169711] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512107.526498291] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (3.02, -1.02)
[component_container_isolated-18] [WARN] [1783512107.526646642] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1783512107.723648444] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [WARN] [1783512107.729447119] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [INFO] [1783512107.739112327] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512107.747658614] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1783512107.757203599] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512107.757343199] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512107.758653060] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1783512107.766309284] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512107.828092891] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512107.927575011] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[competition_master_stage3.py-21] [INFO] [1783512108.052755814] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.95,-1.69) yaw=-50deg cmd=(vx=0.00 wz=-0.06) elapsed=72.9s plan[27pts 5.4m] (1.78,-1.57)→(2.08,0.98) cpuFreq=1500MHz cpuT=84C bpuT=82C cpu=50% mem=19%
[component_container_isolated-18] [WARN] [1783512108.128314764] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512108.211478485] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 5.3709 Hz
[component_container_isolated-18] [WARN] [1783512108.233328107] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[speed_profile_node.py-22] [INFO] [1783512108.259806374] [speed_profile_node]: Plan received: 27 poses, mean|κ|=2.4275 m⁻¹, max|κ|=5.1666 m⁻¹, mean_v=0.315 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512108.326511204] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [WARN] [1783512108.329076701] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[racing_obstacle_detection_yolo-19] [WARN] [1783512108.519576068] [ObstacleDetectionNode]: input fps: 13.38, out fps: 13.38, infer time ms: 10, post process time ms: 7
[component_container_isolated-18] [WARN] [1783512108.604136404] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512108.605180897] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512108.617742017] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512108.625575772] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512108.626782366] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512108.648250029] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512108.928256038] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512109.429496435] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512109.430128171] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (3.02, -1.02)
[component_container_isolated-18] [WARN] [1783512109.431267629] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[racing_obstacle_detection_yolo-19] [WARN] [1783512109.571042001] [ObstacleDetectionNode]: input fps: 12.35, out fps: 12.35, infer time ms: 10, post process time ms: 5
[component_container_isolated-18] [INFO] [1783512109.624143393] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512109.651484426] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512109.684629468] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1783512109.685000425] [behavior_server]: wait completed successfully
[component_container_isolated-18] [INFO] [1783512109.689096790] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512109.689266808] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512109.713522170] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783512110.066025218] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(1.99,-1.77) yaw=-66deg cmd=(vx=0.20 wz=0.58) elapsed=74.9s plan[27pts 5.4m] (1.93,-1.72)→(2.08,0.98) cpuFreq=1500MHz cpuT=84C bpuT=82C cpu=100% mem=19%
[component_container_isolated-18] [WARN] [1783512110.214801337] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 3.4531 Hz
[speed_profile_node.py-22] [INFO] [1783512110.233638882] [speed_profile_node]: Plan received: 26 poses, mean|κ|=2.4082 m⁻¹, max|κ|=5.0431 m⁻¹, mean_v=0.317 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512110.326433296] [controller_server]: Passing new path to controller.
[hobot_codec_republish-13] [WARN] [1783512110.584054703] [vlm_jpeg_encoder]: Sub imgRaw fps [12.51]
[hobot_codec_republish-13] [WARN] [1783512110.586791369] [vlm_jpeg_encoder]: Pub img fps [12.51]
[component_container_isolated-18] [WARN] [1783512110.605135279] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512110.605938531] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[racing_obstacle_detection_yolo-19] [WARN] [1783512110.615830083] [ObstacleDetectionNode]: input fps: 12.45, out fps: 12.45, infer time ms: 10, post process time ms: 5
[component_container_isolated-18] [INFO] [1783512110.627022982] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512110.636668592] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512110.640700187] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512110.682871674] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-6] [INFO] [1783512111.357216180] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4070 q_w=0.8486 angle=63.9deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783512111.410804208] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2183 q_w=0.9863 angle=19.0deg beta=0.0330
[component_container_isolated-18] [WARN] [1783512111.426803888] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512111.427408408] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (3.02, -1.02)
[component_container_isolated-18] [WARN] [1783512111.427500751] [planner_server]: [compute_path_through_poses] [ActionServer] Aborting handle.
[racing_obstacle_detection_yolo-19] [WARN] [1783512111.620565643] [ObstacleDetectionNode]: input fps: 11.96, out fps: 11.95, infer time ms: 10, post process time ms: 6
[component_container_isolated-18] [INFO] [1783512111.623739426] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512111.644101677] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512111.659299067] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512111.659439914] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512111.667173748] [behavior_server]: Running wait
[component_container_isolated-18] [INFO] [1783512111.667491114] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1783512111.672721983] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783512112.073121529] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.16,-2.08) yaw=-48deg cmd=(vx=0.20 wz=0.84) elapsed=76.9s plan[26pts 5.3m] (2.08,-2.02)→(2.08,0.98) cpuFreq=1500MHz cpuT=84C bpuT=82C cpu=66% mem=19%
[component_container_isolated-18] [WARN] [1783512112.213669040] [planner_server]: Planner loop missed its desired rate of 10.0000 Hz. Current loop rate is 3.4771 Hz
[speed_profile_node.py-22] [INFO] [1783512112.231769588] [speed_profile_node]: Plan received: 26 poses, mean|κ|=2.3192 m⁻¹, max|κ|=5.0375 m⁻¹, mean_v=0.323 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512112.326499962] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [WARN] [1783512112.605988614] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512112.606663264] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512112.621507323] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512112.623421013] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512112.650605298] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512112.655646299] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512112.662359258] [ObstacleDetectionNode]: input fps: 10.57, out fps: 10.57, infer time ms: 10, post process time ms: 6
[speed_profile_node.py-22] [INFO] [1783512113.467923562] [speed_profile_node]: Plan received: 23 poses, mean|κ|=1.3669 m⁻¹, max|κ|=3.7690 m⁻¹, mean_v=0.377 m/s, min_v=0.224 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512113.626507097] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512113.691837769] [ObstacleDetectionNode]: input fps: 12.62, out fps: 12.62, infer time ms: 10, post process time ms: 5
[competition_master_stage3.py-21] [INFO] [1783512114.058865157] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.46,-2.23) yaw=-10deg cmd=(vx=0.22 wz=0.23) elapsed=78.9s plan[23pts 4.6m] (2.53,-2.32)→(2.08,0.98) cpuFreq=1500MHz cpuT=84C bpuT=82C cpu=75% mem=19%
[component_container_isolated-18] [WARN] [1783512114.604548408] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512114.605283185] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512114.619519973] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512114.620403681] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512114.641130491] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512114.642975622] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512114.718916672] [ObstacleDetectionNode]: input fps: 11.70, out fps: 11.70, infer time ms: 10, post process time ms: 6
[speed_profile_node.py-22] [INFO] [1783512114.745319304] [speed_profile_node]: Plan received: 21 poses, mean|κ|=1.4726 m⁻¹, max|κ|=3.8750 m⁻¹, mean_v=0.370 m/s, min_v=0.220 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512114.926605692] [controller_server]: Passing new path to controller.
[hobot_codec_republish-13] [WARN] [1783512115.599119437] [vlm_jpeg_encoder]: Sub imgRaw fps [10.97]
[hobot_codec_republish-13] [WARN] [1783512115.603138346] [vlm_jpeg_encoder]: Pub img fps [10.96]
[racing_obstacle_detection_yolo-19] [WARN] [1783512115.719248916] [ObstacleDetectionNode]: input fps: 10.99, out fps: 10.99, infer time ms: 10, post process time ms: 5
[competition_master_stage3.py-21] [INFO] [1783512116.062265876] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.92,-2.15) yaw=30deg cmd=(vx=0.20 wz=1.04) elapsed=80.9s plan[21pts 4.1m] (2.68,-2.17)→(2.08,0.98) cpuFreq=1500MHz cpuT=84C bpuT=82C cpu=100% mem=19%
[speed_profile_node.py-22] [INFO] [1783512116.065313350] [speed_profile_node]: Plan received: 21 poses, mean|κ|=1.1198 m⁻¹, max|κ|=3.0908 m⁻¹, mean_v=0.397 m/s, min_v=0.254 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512116.226437139] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [WARN] [1783512116.612914329] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512116.612955374] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512116.636221991] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512116.640373895] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512116.656464468] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512116.657547813] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512116.722748052] [ObstacleDetectionNode]: input fps: 11.98, out fps: 11.96, infer time ms: 10, post process time ms: 6
[speed_profile_node.py-22] [INFO] [1783512117.365870077] [speed_profile_node]: Plan received: 20 poses, mean|κ|=2.4007 m⁻¹, max|κ|=7.9726 m⁻¹, mean_v=0.360 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512117.526551631] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512117.740135118] [ObstacleDetectionNode]: input fps: 11.88, out fps: 11.87, infer time ms: 11, post process time ms: 12
[competition_master_stage3.py-21] [INFO] [1783512118.058764337] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(3.19,-1.72) yaw=84deg cmd=(vx=0.33 wz=0.66) elapsed=82.9s plan[20pts 3.7m] (3.13,-1.87)→(2.08,0.98) cpuFreq=1500MHz cpuT=84C bpuT=82C cpu=88% mem=19%
[component_container_isolated-18] [WARN] [1783512118.614637885] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512118.614688056] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512118.667362895] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512118.672853389] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512118.679397470] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512118.691131645] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[speed_profile_node.py-22] [INFO] [1783512118.692759988] [speed_profile_node]: Plan received: 19 poses, mean|κ|=2.7373 m⁻¹, max|κ|=5.0380 m⁻¹, mean_v=0.302 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[racing_obstacle_detection_yolo-19] [WARN] [1783512118.764024901] [ObstacleDetectionNode]: input fps: 11.64, out fps: 11.66, infer time ms: 10, post process time ms: 6
[component_container_isolated-18] [INFO] [1783512118.826507424] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512119.950130404] [ObstacleDetectionNode]: input fps: 9.28, out fps: 9.28, infer time ms: 10, post process time ms: 6
[speed_profile_node.py-22] [INFO] [1783512119.956056005] [speed_profile_node]: Plan received: 12 poses, mean|κ|=1.9234 m⁻¹, max|κ|=3.6951 m⁻¹, mean_v=0.336 m/s, min_v=0.227 m/s, max_v=0.468 m/s
[competition_master_stage3.py-21] [INFO] [1783512120.063585563] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.91,-1.02) yaw=100deg cmd=(vx=-0.30 wz=0.08) elapsed=84.9s plan[12pts 2.4m] (2.98,-0.97)→(2.08,0.98) cpuFreq=1500MHz cpuT=84C bpuT=82C cpu=90% mem=19%
[component_container_isolated-18] [INFO] [1783512120.126492348] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [WARN] [1783512120.605693058] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512120.606913569] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[hobot_codec_republish-13] [WARN] [1783512120.618229611] [vlm_jpeg_encoder]: Sub imgRaw fps [11.16]
[component_container_isolated-18] [INFO] [1783512120.644238458] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512120.676627964] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512120.685971604] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512120.693060861] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512121.004644516] [ObstacleDetectionNode]: input fps: 12.32, out fps: 12.33, infer time ms: 10, post process time ms: 6
[speed_profile_node.py-22] [INFO] [1783512121.254318052] [speed_profile_node]: Plan received: 12 poses, mean|κ|=1.9795 m⁻¹, max|κ|=4.6707 m⁻¹, mean_v=0.346 m/s, min_v=0.200 m/s, max_v=0.468 m/s
[imu_madgwick_filter.py-6] [INFO] [1783512121.363509242] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4436 q_w=0.8026 angle=73.2deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783512121.425363280] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2381 q_w=0.4921 angle=121.0deg beta=0.0330
[component_container_isolated-18] [INFO] [1783512121.426478448] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512122.065921287] [ObstacleDetectionNode]: input fps: 13.22, out fps: 13.20, infer time ms: 11, post process time ms: 6
[competition_master_stage3.py-21] [INFO] [1783512122.068390635] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.90,-0.92) yaw=88deg cmd=(vx=0.20 wz=0.29) elapsed=86.9s plan[12pts 2.4m] (2.98,-0.97)→(2.08,0.98) cpuFreq=1500MHz cpuT=85C bpuT=82C cpu=88% mem=19%
[speed_profile_node.py-22] [INFO] [1783512122.568025554] [speed_profile_node]: Plan received: 10 poses, mean|κ|=1.8578 m⁻¹, max|κ|=4.3035 m⁻¹, mean_v=0.358 m/s, min_v=0.205 m/s, max_v=0.475 m/s
[component_container_isolated-18] [WARN] [1783512122.609730823] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512122.610243194] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512122.618553304] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512122.633133749] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512122.636619379] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512122.663089155] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512122.726555063] [controller_server]: Passing new path to controller.
[hobot_codec_republish-13] [WARN] [1783512122.998544441] [vlm_jpeg_encoder]: Pub img fps [7.57]
[racing_obstacle_detection_yolo-19] [WARN] [1783512123.091357572] [ObstacleDetectionNode]: input fps: 11.74, out fps: 11.75, infer time ms: 11, post process time ms: 10
[speed_profile_node.py-22] [INFO] [1783512123.854301540] [speed_profile_node]: Plan received: 10 poses, mean|κ|=1.8115 m⁻¹, max|κ|=4.2842 m⁻¹, mean_v=0.363 m/s, min_v=0.206 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512124.026494425] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783512124.062317520] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.89,-0.72) yaw=95deg cmd=(vx=0.22 wz=0.35) elapsed=88.9s plan[10pts 2.0m] (2.83,-0.67)→(2.08,0.98) cpuFreq=1500MHz cpuT=85C bpuT=83C cpu=57% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512124.114707657] [ObstacleDetectionNode]: input fps: 13.66, out fps: 13.65, infer time ms: 12, post process time ms: 7
[component_container_isolated-18] [WARN] [1783512124.605395944] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512124.605483067] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512124.617387072] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512124.619913877] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512124.633515043] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512124.633552000] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[speed_profile_node.py-22] [INFO] [1783512125.055707472] [speed_profile_node]: Plan received: 9 poses, mean|κ|=1.8803 m⁻¹, max|κ|=4.4540 m⁻¹, mean_v=0.364 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[racing_obstacle_detection_yolo-19] [WARN] [1783512125.159625645] [ObstacleDetectionNode]: input fps: 9.59, out fps: 9.61, infer time ms: 10, post process time ms: 10
[component_container_isolated-18] [INFO] [1783512125.226487257] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783512126.061259113] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.82,-0.46) yaw=118deg cmd=(vx=0.21 wz=-0.09) elapsed=90.9s plan[9pts 1.7m] (2.83,-0.37)→(2.08,0.98) cpuFreq=1500MHz cpuT=85C bpuT=82C cpu=87% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512126.167300356] [ObstacleDetectionNode]: input fps: 9.96, out fps: 9.95, infer time ms: 10, post process time ms: 12
[speed_profile_node.py-22] [INFO] [1783512126.360359413] [speed_profile_node]: Plan received: 8 poses, mean|κ|=2.0700 m⁻¹, max|κ|=4.3615 m⁻¹, mean_v=0.349 m/s, min_v=0.203 m/s, max_v=0.499 m/s
[component_container_isolated-18] [INFO] [1783512126.526702820] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [WARN] [1783512126.604970816] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512126.605917667] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512126.620671998] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512126.637133118] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512126.643730407] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512126.645960059] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512127.185309343] [ObstacleDetectionNode]: input fps: 10.78, out fps: 10.78, infer time ms: 10, post process time ms: 10
[speed_profile_node.py-22] [INFO] [1783512127.675669945] [speed_profile_node]: Plan received: 7 poses, mean|κ|=2.6118 m⁻¹, max|κ|=4.7904 m⁻¹, mean_v=0.319 m/s, min_v=0.200 m/s, max_v=0.500 m/s
[component_container_isolated-18] [INFO] [1783512127.826485692] [controller_server]: Passing new path to controller.
[hobot_codec_republish-13] [WARN] [1783512128.021409021] [vlm_jpeg_encoder]: Sub imgRaw fps [12.33]
[hobot_codec_republish-13] [WARN] [1783512128.024931768] [vlm_jpeg_encoder]: Pub img fps [12.34]
[competition_master_stage3.py-21] [INFO] [1783512128.059648038] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.59,-0.07) yaw=120deg cmd=(vx=0.14 wz=-0.18) elapsed=92.9s plan[7pts 1.2m] (2.53,0.08)→(2.08,0.98) cpuFreq=1500MHz cpuT=85C bpuT=82C cpu=87% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512128.248214857] [ObstacleDetectionNode]: input fps: 11.27, out fps: 11.27, infer time ms: 10, post process time ms: 7
[component_container_isolated-18] [WARN] [1783512128.602838923] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512128.603031752] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512128.613570659] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512128.640174296] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512128.648637338] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512128.667598705] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512129.126498491] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512129.298091774] [ObstacleDetectionNode]: input fps: 9.53, out fps: 9.52, infer time ms: 11, post process time ms: 6
[competition_master_stage3.py-21] [INFO] [1783512130.052451471] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.45,0.11) yaw=121deg cmd=(vx=0.20 wz=0.03) elapsed=94.9s plan[7pts 1.2m] (2.53,0.08)→(2.08,0.98) cpuFreq=1500MHz cpuT=84C bpuT=83C cpu=80% mem=19%
[speed_profile_node.py-22] [INFO] [1783512130.267280281] [speed_profile_node]: Plan received: 6 poses, mean|κ|=2.9951 m⁻¹, max|κ|=4.7194 m⁻¹, mean_v=0.290 m/s, min_v=0.200 m/s, max_v=0.472 m/s
[racing_obstacle_detection_yolo-19] [WARN] [1783512130.359987311] [ObstacleDetectionNode]: input fps: 11.43, out fps: 11.44, infer time ms: 10, post process time ms: 19
[component_container_isolated-18] [INFO] [1783512130.426518807] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [WARN] [1783512130.609246218] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512130.609310717] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512130.628341453] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512130.640294183] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512130.646001179] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512130.660340355] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-6] [INFO] [1783512131.359445695] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=4778 q_w=0.5588 angle=112.1deg beta=0.0030
[racing_obstacle_detection_yolo-19] [WARN] [1783512131.375404726] [ObstacleDetectionNode]: input fps: 12.67, out fps: 12.67, infer time ms: 10, post process time ms: 8
[imu_madgwick_filter.py-4] [INFO] [1783512131.408732381] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2579 q_w=0.1460 angle=163.2deg beta=0.0330
[speed_profile_node.py-22] [INFO] [1783512131.549905997] [speed_profile_node]: Plan received: 6 poses, mean|κ|=4.2449 m⁻¹, max|κ|=6.1832 m⁻¹, mean_v=0.239 m/s, min_v=0.200 m/s, max_v=0.347 m/s
[component_container_isolated-18] [INFO] [1783512131.726494849] [controller_server]: Passing new path to controller.
[competition_master_stage3.py-21] [INFO] [1783512132.062889178] [competition_master_stage3]: [DIAG] state=CRUISE_CHANNEL pos=(2.18,0.50) yaw=124deg cmd=(vx=0.20 wz=-0.43) elapsed=96.9s plan[6pts 0.9m] (2.23,0.38)→(2.08,0.98) cpuFreq=1500MHz cpuT=85C bpuT=83C cpu=75% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512132.429402710] [ObstacleDetectionNode]: input fps: 12.31, out fps: 12.32, infer time ms: 10, post process time ms: 6
[component_container_isolated-18] [WARN] [1783512132.607187796] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512132.607689911] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512132.618055614] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512132.625577459] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512132.659990625] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512132.666928065] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512132.727524275] [controller_server]: Reached the goal!
[speed_profile_node.py-22] [INFO] [1783512132.849560011] [speed_profile_node]: Plan received: 8 poses, mean|κ|=3.5698 m⁻¹, max|κ|=4.9783 m⁻¹, mean_v=0.246 m/s, min_v=0.200 m/s, max_v=0.344 m/s
[hobot_codec_republish-13] [WARN] [1783512133.084025013] [vlm_jpeg_encoder]: Sub imgRaw fps [12.05]
[hobot_codec_republish-13] [WARN] [1783512133.087474858] [vlm_jpeg_encoder]: Pub img fps [12.05]
[component_container_isolated-18] [INFO] [1783512133.223737426] [bt_navigator]: Goal succeeded
[competition_master_stage3.py-21] [INFO] [1783512133.239899134] [competition_master_stage3]: [结果回调] 巡航完成, 触发VLM推理...
[competition_master_stage3.py-21] [INFO] [1783512133.246743202] [competition_master_stage3]: [VLM] 发布 sign4return=100, 拍照推理中...
[competition_master_stage3.py-21] [INFO] [1783512133.252431293] [competition_master_stage3]: [状态机] CRUISE_CHANNEL → RETURN_P
[vision_ai_node-12] [INFO] [1783512133.251554144] [vision_ai_node]: Received sign4return: 100
[vision_ai_node-12] [INFO] [1783512133.254749328] [vision_ai_node]: Trigger received (sign4return=100), subscribing to /aurora/rgb/image_jpeg...
[competition_master_stage3.py-21] [INFO] [1783512133.257382608] [competition_master_stage3]: [RETURN] VLM→post(0.96,-0.06)→P
[competition_master_stage3.py-21] [INFO] [1783512133.268878079] [competition_master_stage3]: [DIAG] nav目标距离: 1.33m, robot=(2.11,0.61) → target=(0.96,-0.06)
[competition_master_stage3.py-21] [INFO] [1783512133.273268905] [competition_master_stage3]: >>> 发送导航目标 [路点3(post-VLM)]: (0.96, -0.06, yaw=0.00)
[component_container_isolated-18] [INFO] [1783512133.287026038] [bt_navigator]: Begin navigating from current location (2.09, 0.67) to (0.96, -0.06)
[vision_ai_node-12] [INFO] [1783512133.289233785] [vision_ai_node]: Subscribed to /aurora/rgb/image_jpeg
[competition_master_stage3.py-21] [INFO] [1783512133.297919439] [competition_master_stage3]: 导航目标已接受，车辆出发...
[speed_profile_node.py-22] [INFO] [1783512133.316060024] [speed_profile_node]: Plan received: 13 poses, mean|κ|=1.1318 m⁻¹, max|κ|=1.8161 m⁻¹, mean_v=0.391 m/s, min_v=0.331 m/s, max_v=0.496 m/s
[vision_ai_node-12] [INFO] [1783512133.325544870] [vision_ai_node]: Received JPU-encoded JPEG frame (21536 bytes), sending to VLM...
[component_container_isolated-18] [INFO] [1783512133.490086146] [controller_server]: Received a goal, begin computing control effort.
[racing_obstacle_detection_yolo-19] [WARN] [1783512133.493081668] [ObstacleDetectionNode]: input fps: 12.26, out fps: 12.25, infer time ms: 10, post process time ms: 9
[competition_master_stage3.py-21] [INFO] [1783512134.053306920] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(2.11,0.61) yaw=108deg cmd=(vx=0.29 wz=1.09) elapsed=98.9s plan[13pts 2.3m] (2.08,0.68)→(1.03,-0.07) cpuFreq=1500MHz cpuT=85C bpuT=83C cpu=85% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512134.531453796] [ObstacleDetectionNode]: input fps: 12.51, out fps: 12.51, infer time ms: 10, post process time ms: 7
[speed_profile_node.py-22] [INFO] [1783512134.610771033] [speed_profile_node]: Plan received: 13 poses, mean|κ|=1.2126 m⁻¹, max|κ|=2.0717 m⁻¹, mean_v=0.383 m/s, min_v=0.313 m/s, max_v=0.468 m/s
[component_container_isolated-18] [INFO] [1783512134.890499674] [controller_server]: Passing new path to controller.
[component_container_isolated-18] [WARN] [1783512135.264059149] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512135.264118690] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512135.276533959] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512135.286435608] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512135.336200099] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512135.341175381] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512135.599512950] [ObstacleDetectionNode]: input fps: 12.16, out fps: 12.16, infer time ms: 10, post process time ms: 5
[speed_profile_node.py-22] [INFO] [1783512135.914024848] [speed_profile_node]: Plan received: 10 poses, mean|κ|=1.2076 m⁻¹, max|κ|=2.0131 m⁻¹, mean_v=0.385 m/s, min_v=0.317 m/s, max_v=0.490 m/s
[competition_master_stage3.py-21] [INFO] [1783512136.057730800] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.76,1.06) yaw=131deg cmd=(vx=0.45 wz=0.30) elapsed=100.9s plan[10pts 2.0m] (1.78,1.13)→(1.03,-0.07) cpuFreq=1500MHz cpuT=85C bpuT=83C cpu=57% mem=19%
[component_container_isolated-18] [INFO] [1783512136.090468024] [controller_server]: Passing new path to controller.
[racing_obstacle_detection_yolo-19] [WARN] [1783512136.619644429] [ObstacleDetectionNode]: input fps: 11.81, out fps: 11.78, infer time ms: 13, post process time ms: 6
[imu_madgwick_filter.py-4] [WARN] [1783512136.632766643] [imu_madgwick_filter]: [imu_madgwick] dt outlier: 0.1999s > 0.15s, capping
[component_container_isolated-18] [WARN] [1783512136.997990056] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512137.091991351] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512137.191195521] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512137.194156760] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512137.194383756] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.96, -0.06)
[component_container_isolated-18] [WARN] [1783512137.194484380] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1783512137.260396386] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512137.262013566] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512137.267505761] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512137.279573840] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512137.296313920] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512137.297886184] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [WARN] [1783512137.301994237] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512137.302687600] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512137.335175153] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512137.356896562] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512137.359830885] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512137.377529449] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512137.391113251] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512137.492876626] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512137.591993090] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[racing_obstacle_detection_yolo-19] [WARN] [1783512137.649681533] [ObstacleDetectionNode]: input fps: 11.63, out fps: 11.65, infer time ms: 10, post process time ms: 6
[component_container_isolated-18] [WARN] [1783512137.693109310] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512137.791544410] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512137.893957690] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512137.991288477] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[competition_master_stage3.py-21] [INFO] [1783512138.068935380] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.27,1.41) yaw=168deg cmd=(vx=0.00 wz=0.00) elapsed=102.9s plan[10pts 2.0m] (1.78,1.13)→(1.03,-0.07) cpuFreq=1500MHz cpuT=85C bpuT=83C cpu=71% mem=19%
[component_container_isolated-18] [WARN] [1783512138.092067079] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[hobot_codec_republish-13] [WARN] [1783512138.093663136] [vlm_jpeg_encoder]: Sub imgRaw fps [11.98]
[hobot_codec_republish-13] [WARN] [1783512138.096384216] [vlm_jpeg_encoder]: Pub img fps [11.98]
[component_container_isolated-18] [WARN] [1783512138.191211225] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [WARN] [1783512138.210565195] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512138.210854524] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.96, -0.06)
[component_container_isolated-18] [WARN] [1783512138.210969230] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1783512138.292092133] [controller_server]: RegulatedPurePursuitController detected collision ahead!
[component_container_isolated-18] [INFO] [1783512138.390458833] [controller_server]: Goal was canceled. Stopping the robot.
[component_container_isolated-18] [INFO] [1783512138.390666455] [controller_server]: [follow_path] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [INFO] [1783512138.394073648] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1783512138.416809937] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512138.443768698] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512138.445132008] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512138.445380379] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512138.459121360] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [WARN] [1783512138.474594311] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512138.494302442] [BehaviorTreeEngine]: Behavior Tree tick rate 10.00 was exceeded!
[component_container_isolated-18] [INFO] [1783512138.498691786] [behavior_server]: Running backup
[component_container_isolated-18] [INFO] [1783512138.501422657] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512138.501602154] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512138.502960007] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1783512138.503121087] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1783512138.503586205] [behavior_server]: [backup] [ActionServer] Aborting handle.
[vision_ai_node-12] [INFO] [1783512138.512157896] [vision_ai_node]: VLM Result: 图像中无此人形立牌，仅有一个带白色反光条的蓝色交通锥置于地面，背景为浅色墙面，右侧有黑色大型物体（疑似设备），场景似室内作业区或走廊，未呈现医疗巡检相关的人形立牌及动作。
[component_container_isolated-18] [WARN] [1783512138.514689020] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[vision_ai_node-12] [INFO] [1783512138.542287812] [vision_ai_node]: Unsubscribed from image topic
[competition_master_stage3.py-21] [INFO] [1783512138.552156648] [competition_master_stage3]: [VLM] 后台收到推理结果: 图像中无此人形立牌，仅有一个带白色反光条的蓝色交通锥置于地面，背景为浅色墙面，右侧有黑色大型物体（疑似设备），场景似室内作业区或走廊，未呈现医疗巡检相关的人形立牌及动作。...
[racing_obstacle_detection_yolo-19] [WARN] [1783512138.729285124] [ObstacleDetectionNode]: input fps: 12.06, out fps: 12.06, infer time ms: 11, post process time ms: 7
[component_container_isolated-18] [INFO] [1783512138.790701770] [behavior_server]: Running wait
[component_container_isolated-18] [WARN] [1783512139.260030144] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512139.262977845] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512139.279461071] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512139.279972271] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512139.302181152] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512139.323045431] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512139.778888695] [ObstacleDetectionNode]: input fps: 11.43, out fps: 11.43, infer time ms: 10, post process time ms: 6
[competition_master_stage3.py-21] [INFO] [1783512140.053774719] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.27,1.41) yaw=168deg cmd=(vx=0.00 wz=0.00) elapsed=104.9s plan[10pts 2.0m] (1.78,1.13)→(1.03,-0.07) cpuFreq=1500MHz cpuT=85C bpuT=83C cpu=71% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512140.829303784] [ObstacleDetectionNode]: input fps: 12.37, out fps: 12.37, infer time ms: 10, post process time ms: 6
[component_container_isolated-18] [WARN] [1783512141.255516883] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512141.255533382] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512141.266094634] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512141.277872117] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[imu_madgwick_filter.py-6] [INFO] [1783512141.363017247] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5145 q_w=0.2011 angle=156.8deg beta=0.0030
[component_container_isolated-18] [WARN] [1783512141.388024023] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512141.388042565] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-4] [INFO] [1783512141.406666941] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2774 q_w=-0.2142 angle=204.7deg beta=0.0330
[component_container_isolated-18] [INFO] [1783512141.791148233] [behavior_server]: wait completed successfully
[racing_obstacle_detection_yolo-19] [WARN] [1783512141.877511010] [ObstacleDetectionNode]: input fps: 12.49, out fps: 12.49, infer time ms: 10, post process time ms: 13
[competition_master_stage3.py-21] [INFO] [1783512142.056725888] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.27,1.41) yaw=168deg cmd=(vx=0.00 wz=0.00) elapsed=106.9s plan[10pts 2.0m] (1.78,1.13)→(1.03,-0.07) cpuFreq=1500MHz cpuT=85C bpuT=83C cpu=57% mem=19%
[component_container_isolated-18] [WARN] [1783512142.090544977] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512142.091103803] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.96, -0.06)
[component_container_isolated-18] [WARN] [1783512142.091220176] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1783512142.289026412] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512142.305779626] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512142.323273370] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512142.323436451] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512142.334756286] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512142.884737337] [ObstacleDetectionNode]: input fps: 12.86, out fps: 12.86, infer time ms: 10, post process time ms: 8
[hobot_codec_republish-13] [WARN] [1783512143.098734720] [vlm_jpeg_encoder]: Sub imgRaw fps [12.19]
[hobot_codec_republish-13] [WARN] [1783512143.109245535] [vlm_jpeg_encoder]: Pub img fps [12.17]
[component_container_isolated-18] [WARN] [1783512143.214970138] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512143.215238718] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.96, -0.06)
[component_container_isolated-18] [WARN] [1783512143.216576367] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1783512143.258494213] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512143.258858541] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512143.265460743] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512143.273378010] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[competition_master_stage3.py-21] [WARN] [1783512143.274629202] [competition_master_stage3]: [STUCK] 卡死检测: 4秒位移=0.000m, 但非环道阶段 → 不软化禁区
[component_container_isolated-18] [WARN] [1783512143.288995506] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512143.291680428] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512143.389187310] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1783512143.422436858] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512143.429436554] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512143.440614610] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512143.440780650] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512143.453062816] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512143.479246126] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512143.480370611] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512143.485812245] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512143.498960275] [behavior_server]: Running backup
[component_container_isolated-18] [WARN] [1783512143.501885360] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1783512143.502057899] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1783512143.503005011] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1783512143.504584115] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512143.788650834] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1783512143.802357939] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512143.815216639] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512143.818847423] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512143.819421873] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512143.831419877] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512143.846802292] [behavior_server]: Running backup
[component_container_isolated-18] [INFO] [1783512143.849662795] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512143.849865667] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512143.850174455] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1783512143.850297245] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1783512143.850375911] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1783512143.883377337] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512143.885734346] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512143.919339014] [ObstacleDetectionNode]: input fps: 8.89, out fps: 8.78, infer time ms: 11, post process time ms: 17
[competition_master_stage3.py-21] [INFO] [1783512144.059625647] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.27,1.41) yaw=168deg cmd=(vx=0.00 wz=0.00) elapsed=108.9s plan[10pts 2.0m] (1.78,1.13)→(1.03,-0.07) cpuFreq=1500MHz cpuT=85C bpuT=83C cpu=85% mem=19%
[component_container_isolated-18] [INFO] [1783512144.094853376] [behavior_server]: Running wait
[racing_obstacle_detection_yolo-19] [WARN] [1783512144.930446091] [ObstacleDetectionNode]: input fps: 12.56, out fps: 12.73, infer time ms: 10, post process time ms: 6
[component_container_isolated-18] [WARN] [1783512145.262559407] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512145.262574740] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[competition_master_stage3.py-21] [WARN] [1783512145.276254304] [competition_master_stage3]: [STUCK] 卡死检测: 4秒位移=0.000m, 但非环道阶段 → 不软化禁区
[component_container_isolated-18] [INFO] [1783512145.276523258] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512145.276712006] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512145.292525999] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512145.303396059] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512145.965830880] [ObstacleDetectionNode]: input fps: 11.58, out fps: 11.58, infer time ms: 10, post process time ms: 5
[competition_master_stage3.py-21] [INFO] [1783512146.060487354] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.27,1.41) yaw=168deg cmd=(vx=0.00 wz=0.00) elapsed=110.9s plan[10pts 2.0m] (1.78,1.13)→(1.03,-0.07) cpuFreq=1500MHz cpuT=85C bpuT=83C cpu=57% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512146.975050660] [ObstacleDetectionNode]: input fps: 13.90, out fps: 13.92, infer time ms: 10, post process time ms: 8
[component_container_isolated-18] [INFO] [1783512147.095551021] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1783512147.259302788] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512147.265202927] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[competition_master_stage3.py-21] [WARN] [1783512147.265333593] [competition_master_stage3]: [STUCK] 卡死检测: 4秒位移=0.000m, 但非环道阶段 → 不软化禁区
[component_container_isolated-18] [WARN] [1783512147.267292070] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512147.287627001] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512147.294988665] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512147.305672083] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512147.391933873] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512147.392143621] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.96, -0.06)
[component_container_isolated-18] [WARN] [1783512147.392226620] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1783512147.588533009] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512147.610237548] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512147.652679223] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512147.653234008] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512147.666052734] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512148.012535297] [ObstacleDetectionNode]: input fps: 11.56, out fps: 11.55, infer time ms: 10, post process time ms: 6
[competition_master_stage3.py-21] [INFO] [1783512148.060902610] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.27,1.41) yaw=168deg cmd=(vx=0.00 wz=0.00) elapsed=112.9s plan[10pts 2.0m] (1.78,1.13)→(1.03,-0.07) cpuFreq=1500MHz cpuT=85C bpuT=83C cpu=83% mem=19%
[hobot_codec_republish-13] [WARN] [1783512148.117033001] [vlm_jpeg_encoder]: Sub imgRaw fps [11.96]
[hobot_codec_republish-13] [WARN] [1783512148.121122536] [vlm_jpeg_encoder]: Pub img fps [11.97]
[component_container_isolated-18] [WARN] [1783512148.212880930] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512148.213128927] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.96, -0.06)
[component_container_isolated-18] [WARN] [1783512148.215034030] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1783512148.388458142] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1783512148.401842945] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512148.417232225] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512148.417630512] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512148.417765011] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512148.432727670] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512148.442995301] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512148.458975366] [behavior_server]: Running backup
[component_container_isolated-18] [WARN] [1783512148.460337183] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1783512148.460633513] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1783512148.460764220] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1783512148.470389233] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512148.470563815] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512148.501519747] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512148.688764032] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1783512148.704423434] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512148.723873875] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512148.733152226] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512148.740124395] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512148.740414766] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512148.744133307] [behavior_server]: Running backup
[component_container_isolated-18] [INFO] [1783512148.744585385] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512148.744880506] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512148.745452791] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1783512148.745647289] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1783512148.745716288] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1783512148.761188942] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512148.783796805] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512148.989283295] [behavior_server]: Running wait
[racing_obstacle_detection_yolo-19] [WARN] [1783512149.055564234] [ObstacleDetectionNode]: input fps: 12.48, out fps: 12.46, infer time ms: 10, post process time ms: 6
[component_container_isolated-18] [WARN] [1783512149.261435553] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512149.261435637] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512149.274864564] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512149.276108800] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512149.289542727] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512149.291290832] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [WARN] [1783512149.324768944] [competition_master_stage3]: [STUCK] 卡死检测: 4秒位移=0.000m, 但非环道阶段 → 不软化禁区
[competition_master_stage3.py-21] [INFO] [1783512150.056101714] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.27,1.41) yaw=168deg cmd=(vx=0.00 wz=0.00) elapsed=114.9s plan[10pts 2.0m] (1.78,1.13)→(1.03,-0.07) cpuFreq=1500MHz cpuT=85C bpuT=83C cpu=83% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512150.084030501] [ObstacleDetectionNode]: input fps: 12.66, out fps: 12.68, infer time ms: 10, post process time ms: 8
[racing_obstacle_detection_yolo-19] [WARN] [1783512151.093852834] [ObstacleDetectionNode]: input fps: 11.87, out fps: 11.87, infer time ms: 10, post process time ms: 7
[component_container_isolated-18] [WARN] [1783512151.262334506] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512151.262586670] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512151.267988612] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512151.268736396] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[competition_master_stage3.py-21] [WARN] [1783512151.275004330] [competition_master_stage3]: [STUCK] 卡死检测: 4秒位移=0.000m, 但非环道阶段 → 不软化禁区
[component_container_isolated-18] [WARN] [1783512151.290788621] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512151.292689100] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-6] [INFO] [1783512151.364936626] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5509 q_w=0.2007 angle=156.8deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783512151.410784140] [imu_madgwick_filter]: [imu_madgwick ->] msgs=2974 q_w=-0.2510 angle=209.1deg beta=0.0330
[component_container_isolated-18] [INFO] [1783512151.992767218] [behavior_server]: wait completed successfully
[competition_master_stage3.py-21] [INFO] [1783512152.054048943] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.27,1.41) yaw=168deg cmd=(vx=0.00 wz=0.00) elapsed=116.9s plan[10pts 2.0m] (1.78,1.13)→(1.03,-0.07) cpuFreq=1500MHz cpuT=85C bpuT=83C cpu=80% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512152.125560018] [ObstacleDetectionNode]: input fps: 11.64, out fps: 11.64, infer time ms: 10, post process time ms: 7
[component_container_isolated-18] [WARN] [1783512152.294938805] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512152.295280802] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.96, -0.06)
[component_container_isolated-18] [WARN] [1783512152.295454925] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1783512152.489013622] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512152.520521955] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512152.530219394] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512152.531244883] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512152.544212578] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512153.142520952] [ObstacleDetectionNode]: input fps: 11.82, out fps: 11.82, infer time ms: 10, post process time ms: 8
[hobot_codec_republish-13] [WARN] [1783512153.184193510] [vlm_jpeg_encoder]: Sub imgRaw fps [12.04]
[hobot_codec_republish-13] [WARN] [1783512153.186936651] [vlm_jpeg_encoder]: Pub img fps [12.04]
[component_container_isolated-18] [WARN] [1783512153.210397717] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512153.211408957] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.96, -0.06)
[component_container_isolated-18] [WARN] [1783512153.211571581] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1783512153.259930325] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512153.259944241] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[competition_master_stage3.py-21] [WARN] [1783512153.266192848] [competition_master_stage3]: [STUCK] 卡死检测: 4秒位移=0.000m, 但非环道阶段 → 不软化禁区
[component_container_isolated-18] [INFO] [1783512153.267041298] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512153.301412010] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512153.301503050] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512153.317728811] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512153.388533756] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1783512153.405499677] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512153.420739864] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512153.421547272] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512153.421865769] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512153.439860263] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512153.448879593] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512153.475377755] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512153.476622785] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512153.476473370] [behavior_server]: Running backup
[component_container_isolated-18] [WARN] [1783512153.492131511] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1783512153.492302176] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1783512153.492368717] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1783512153.496370970] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512153.788544248] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1783512153.798711400] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[competition_master_stage3.py-21] [INFO] [1783512154.048182962] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.27,1.41) yaw=168deg cmd=(vx=0.00 wz=0.00) elapsed=118.9s plan[10pts 2.0m] (1.78,1.13)→(1.03,-0.07) cpuFreq=1500MHz cpuT=85C bpuT=83C cpu=77% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512154.191565603] [ObstacleDetectionNode]: input fps: 10.46, out fps: 10.47, infer time ms: 10, post process time ms: 5
[component_container_isolated-18] [WARN] [1783512154.289339470] [bt_navigator_navigate_to_pose_rclcpp_node]: Node timed out while executing service call to local_costmap/clear_entirely_local_costmap.
[component_container_isolated-18] [INFO] [1783512154.920154209] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512154.920888577] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512154.921449948] [behavior_server]: Running wait
[component_container_isolated-18] [WARN] [1783512154.922494730] [BehaviorTreeEngine]: Behavior Tree tick rate 10.00 was exceeded!
[component_container_isolated-18] [WARN] [1783512154.947888178] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512155.216955403] [ObstacleDetectionNode]: input fps: 11.71, out fps: 11.71, infer time ms: 10, post process time ms: 5
[component_container_isolated-18] [WARN] [1783512155.266693676] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512155.266693717] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512155.280408002] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512155.285940032] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[competition_master_stage3.py-21] [WARN] [1783512155.298236164] [competition_master_stage3]: [STUCK] 卡死检测: 4秒位移=0.000m, 但非环道阶段 → 不软化禁区
[component_container_isolated-18] [WARN] [1783512155.297852001] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512155.297945209] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [INFO] [1783512156.052552635] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.27,1.41) yaw=168deg cmd=(vx=0.00 wz=0.00) elapsed=120.9s plan[10pts 2.0m] (1.78,1.13)→(1.03,-0.07) cpuFreq=1500MHz cpuT=86C bpuT=83C cpu=80% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512156.255123886] [ObstacleDetectionNode]: input fps: 12.54, out fps: 12.54, infer time ms: 10, post process time ms: 6
[component_container_isolated-18] [WARN] [1783512157.260704819] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512157.262512054] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[competition_master_stage3.py-21] [WARN] [1783512157.281107602] [competition_master_stage3]: [STUCK] 卡死检测: 4秒位移=0.000m, 但非环道阶段 → 不软化禁区
[component_container_isolated-18] [INFO] [1783512157.269607243] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512157.284852653] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512157.293839576] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512157.310991470] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512157.342243409] [ObstacleDetectionNode]: input fps: 13.80, out fps: 13.80, infer time ms: 10, post process time ms: 5
[component_container_isolated-18] [INFO] [1783512157.921796464] [behavior_server]: wait completed successfully
[competition_master_stage3.py-21] [INFO] [1783512158.087767533] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.27,1.41) yaw=168deg cmd=(vx=0.00 wz=0.00) elapsed=122.9s plan[10pts 2.0m] (1.78,1.13)→(1.03,-0.07) cpuFreq=1500MHz cpuT=86C bpuT=84C cpu=96% mem=19%
[component_container_isolated-18] [WARN] [1783512158.168255255] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512158.175357076] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.96, -0.06)
[component_container_isolated-18] [WARN] [1783512158.175559074] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[hobot_codec_republish-13] [WARN] [1783512158.224635867] [vlm_jpeg_encoder]: Sub imgRaw fps [12.70]
[component_container_isolated-18] [INFO] [1783512158.370215885] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[racing_obstacle_detection_yolo-19] [WARN] [1783512158.387243548] [ObstacleDetectionNode]: input fps: 14.44, out fps: 14.44, infer time ms: 11, post process time ms: 11
[component_container_isolated-18] [INFO] [1783512158.395035655] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512158.411450155] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512158.411670278] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512158.425861004] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512159.211475780] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512159.211744069] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.96, -0.06)
[component_container_isolated-18] [WARN] [1783512159.211862693] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1783512159.255996524] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512159.257192932] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512159.262429684] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512159.278198064] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512159.282423573] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512159.286493084] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[competition_master_stage3.py-21] [WARN] [1783512159.305221733] [competition_master_stage3]: [STUCK] 卡死检测: 4秒位移=0.000m, 但非环道阶段 → 不软化禁区
[component_container_isolated-18] [INFO] [1783512159.319428834] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1783512159.346350129] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512159.358735743] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512159.359004866] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512159.359100032] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512159.433440300] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[racing_obstacle_detection_yolo-19] [WARN] [1783512159.434124461] [ObstacleDetectionNode]: input fps: 13.35, out fps: 13.35, infer time ms: 11, post process time ms: 8
[component_container_isolated-18] [INFO] [1783512159.458329319] [behavior_server]: Running backup
[component_container_isolated-18] [INFO] [1783512159.461754876] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [WARN] [1783512159.579642272] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512159.954803335] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512159.958624473] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1783512159.959060095] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1783512159.959178469] [behavior_server]: [backup] [ActionServer] Aborting handle.
[hobot_codec_republish-13] [WARN] [1783512159.957617897] [vlm_jpeg_encoder]: Pub img fps [9.45]
[competition_master_stage3.py-21] [INFO] [1783512160.065648242] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.27,1.41) yaw=168deg cmd=(vx=0.00 wz=0.00) elapsed=124.9s plan[10pts 2.0m] (1.78,1.13)→(1.03,-0.07) cpuFreq=1500MHz cpuT=86C bpuT=84C cpu=77% mem=19%
[component_container_isolated-18] [WARN] [1783512160.176873563] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512160.223024879] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1783512160.240343289] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512160.256152460] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512160.256350792] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512160.271154721] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [WARN] [1783512160.273612036] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512160.303598474] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512160.336746222] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512160.336928513] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512160.338511042] [behavior_server]: Running backup
[component_container_isolated-18] [WARN] [1783512160.343459671] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1783512160.343659836] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1783512160.343763211] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1783512160.357671022] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-6] [WARN] [1783512160.465846741] [imu_madgwick_bmi088]: [imu_madgwick] dt outlier: 0.1505s > 0.15s, capping
[racing_obstacle_detection_yolo-19] [WARN] [1783512160.497682207] [ObstacleDetectionNode]: input fps: 11.41, out fps: 11.41, infer time ms: 11, post process time ms: 19
[component_container_isolated-18] [INFO] [1783512160.624024829] [behavior_server]: Running wait
[component_container_isolated-18] [WARN] [1783512161.260496868] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512161.260499284] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512161.270288928] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[competition_master_stage3.py-21] [WARN] [1783512161.275434352] [competition_master_stage3]: [STUCK] 卡死检测: 4秒位移=0.000m, 但非环道阶段 → 不软化禁区
[component_container_isolated-18] [INFO] [1783512161.286480738] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512161.299643526] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512161.299996315] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[imu_madgwick_filter.py-6] [INFO] [1783512161.359055550] [imu_madgwick_bmi088]: [imu_madgwick ->] msgs=5843 q_w=0.2009 angle=156.8deg beta=0.0030
[imu_madgwick_filter.py-4] [INFO] [1783512161.406218030] [imu_madgwick_filter]: [imu_madgwick ->] msgs=3174 q_w=-0.2889 angle=213.6deg beta=0.0330
[racing_obstacle_detection_yolo-19] [WARN] [1783512161.549998206] [ObstacleDetectionNode]: input fps: 12.00, out fps: 12.20, infer time ms: 10, post process time ms: 5
[competition_master_stage3.py-21] [INFO] [1783512162.067527246] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.27,1.41) yaw=168deg cmd=(vx=0.00 wz=0.00) elapsed=126.9s plan[10pts 2.0m] (1.78,1.13)→(1.03,-0.07) cpuFreq=1500MHz cpuT=86C bpuT=84C cpu=71% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512162.574910312] [ObstacleDetectionNode]: input fps: 11.01, out fps: 10.76, infer time ms: 10, post process time ms: 7
[component_container_isolated-18] [WARN] [1783512163.259050335] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512163.259050376] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[competition_master_stage3.py-21] [WARN] [1783512163.265449334] [competition_master_stage3]: [STUCK] 卡死检测: 4秒位移=0.000m, 但非环道阶段 → 不软化禁区
[component_container_isolated-18] [INFO] [1783512163.280673234] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512163.301776553] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512163.318301277] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512163.319572893] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512163.587765205] [ObstacleDetectionNode]: input fps: 11.87, out fps: 11.87, infer time ms: 10, post process time ms: 8
[component_container_isolated-18] [INFO] [1783512163.626100369] [behavior_server]: wait completed successfully
[component_container_isolated-18] [WARN] [1783512163.930932231] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512163.937583020] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.96, -0.06)
[component_container_isolated-18] [WARN] [1783512163.943215275] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[competition_master_stage3.py-21] [INFO] [1783512164.060803968] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.27,1.41) yaw=168deg cmd=(vx=0.00 wz=0.00) elapsed=128.9s plan[10pts 2.0m] (1.78,1.13)→(1.03,-0.07) cpuFreq=1500MHz cpuT=86C bpuT=84C cpu=91% mem=19%
[component_container_isolated-18] [INFO] [1783512164.123154411] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512164.146959360] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512164.163307352] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512164.163477060] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512164.190225285] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512164.206253486] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512164.206534777] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.96, -0.06)
[component_container_isolated-18] [WARN] [1783512164.206647526] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1783512164.323301497] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1783512164.348693980] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512164.373545091] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512164.374199337] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512164.374361586] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512164.402794968] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512164.407473317] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [WARN] [1783512164.424193473] [BehaviorTreeEngine]: Behavior Tree tick rate 10.00 was exceeded!
[component_container_isolated-18] [INFO] [1783512164.425708048] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512164.425857006] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512164.440502632] [behavior_server]: Running backup
[component_container_isolated-18] [WARN] [1783512164.442212622] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1783512164.442374455] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1783512164.443519032] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1783512164.458513739] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512164.640844426] [ObstacleDetectionNode]: input fps: 12.35, out fps: 12.35, infer time ms: 10, post process time ms: 8
[component_container_isolated-18] [INFO] [1783512164.723112006] [local_costmap.local_costmap]: Received request to clear entirely the local_costmap
[component_container_isolated-18] [INFO] [1783512164.737286094] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512164.752285760] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512164.753400170] [local_costmap.local_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512164.754100958] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512164.780807433] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [INFO] [1783512164.790362463] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512164.799579078] [behavior_server]: Running backup
[component_container_isolated-18] [INFO] [1783512164.801838398] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512164.811600760] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512164.823086238] [behavior_server]: Collision Ahead - Exiting DriveOnHeading
[component_container_isolated-18] [WARN] [1783512164.823243862] [behavior_server]: backup failed
[component_container_isolated-18] [WARN] [1783512164.823312861] [behavior_server]: [backup] [ActionServer] Aborting handle.
[component_container_isolated-18] [WARN] [1783512164.827305547] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[hobot_codec_republish-13] [WARN] [1783512164.980867312] [vlm_jpeg_encoder]: Sub imgRaw fps [12.73]
[hobot_codec_republish-13] [WARN] [1783512164.983565838] [vlm_jpeg_encoder]: Pub img fps [12.74]
[component_container_isolated-18] [INFO] [1783512165.024033636] [behavior_server]: Running wait
[component_container_isolated-18] [WARN] [1783512165.259313916] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512165.259338624] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[competition_master_stage3.py-21] [WARN] [1783512165.277469212] [competition_master_stage3]: [STUCK] 卡死检测: 4秒位移=0.000m, 但非环道阶段 → 不软化禁区
[component_container_isolated-18] [INFO] [1783512165.285971698] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512165.288554722] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512165.302536172] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512165.307223266] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512165.652625276] [ObstacleDetectionNode]: input fps: 10.85, out fps: 10.85, infer time ms: 10, post process time ms: 5
[competition_master_stage3.py-21] [INFO] [1783512166.073455897] [competition_master_stage3]: [DIAG] state=RETURN_P pos=(1.27,1.41) yaw=168deg cmd=(vx=0.00 wz=0.00) elapsed=130.9s plan[10pts 2.0m] (1.78,1.13)→(1.03,-0.07) cpuFreq=1500MHz cpuT=86C bpuT=84C cpu=85% mem=19%
[racing_obstacle_detection_yolo-19] [WARN] [1783512166.658503576] [ObstacleDetectionNode]: input fps: 12.95, out fps: 12.95, infer time ms: 10, post process time ms: 7
[component_container_isolated-18] [WARN] [1783512167.261607075] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [WARN] [1783512167.261607159] [local_costmap.local_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512167.271504530] [local_costmap.local_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512167.276161883] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512167.287808413] [local_costmap.local_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[component_container_isolated-18] [WARN] [1783512167.290292402] [global_costmap.global_costmap]: KeepoutFilter: New filter mask arrived from /keepout_mask topic. Updating old filter mask.
[racing_obstacle_detection_yolo-19] [WARN] [1783512167.713229621] [ObstacleDetectionNode]: input fps: 10.45, out fps: 10.44, infer time ms: 11, post process time ms: 7
[component_container_isolated-18] [INFO] [1783512168.024803877] [behavior_server]: wait completed successfully
^C[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[static_transform_publisher-8] [INFO] [1783512168.031015175] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [lslidar_driver_node-2]: process has died [pid 5592, exit code -6, cmd '/userdata/dev_ws/install/lslidar_driver/lib/lslidar_driver/lslidar_driver_node --ros-args -r __node:=lslidar_driver_node --params-file /userdata/dev_ws/install/lslidar_driver/share/lslidar_driver/params/lsx10.yaml'].
[ERROR] [origincar_base_node-1]: process has died [pid 5590, exit code -6, cmd '/userdata/dev_ws/install/origincar_base/lib/origincar_base/origincar_base_node --ros-args --params-file /tmp/launch_params_cwvm3mli --params-file /tmp/launch_params_rgwd49i3'].
[ERROR] [rviz2-23]: process has died [pid 5954, exit code -11, cmd '/opt/ros/humble/lib/rviz2/rviz2 -d /userdata/dev_ws/install/originbot_navigation/share/originbot_navigation/rviz/nav.rviz --ros-args -r __node:=rviz2'].
[INFO] [robot_state_publisher-3]: process has finished cleanly [pid 5594]
[INFO] [hobot_codec_republish-13]: process has finished cleanly [pid 5650]
[INFO] [static_transform_publisher-8]: process has finished cleanly [pid 5637]
[rviz2-23] [INFO] [1783512168.031138091] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[aurora930_node-9] [INFO] [1783512168.031459090] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[INFO] [map_server-14]: process has finished cleanly [pid 5722]
[INFO] [costmap_filter_info_server-16]: process has finished cleanly [pid 5726]
[component_container_isolated-18] [INFO] [1783512168.031358798] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[component_container_isolated-18] [INFO] [1783512168.036189438] [lifecycle_manager_navigation]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_navigation)
[component_container_isolated-18] [INFO] [1783512168.039284171] [lifecycle_manager_navigation]: Terminating bond timer...
[INFO] [ekf_node-7]: process has finished cleanly [pid 5602]
[ekf_node-7] [INFO] [1783512168.031640255] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-16] [INFO] [1783512168.031858796] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[costmap_filter_info_server-16] [INFO] [1783512168.032085586] [keepout_filter_info_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_filter_info_server)
[costmap_filter_info_server-16] [INFO] [1783512168.032377334] [keepout_filter_info_server]: Deactivating
[costmap_filter_info_server-16] [INFO] [1783512168.032486417] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[costmap_filter_info_server-16] [INFO] [1783512168.050575524] [keepout_filter_info_server]: Cleaning up
[costmap_filter_info_server-16] [INFO] [1783512168.050828814] [keepout_filter_info_server]: Destroying bond (keepout_filter_info_server) to lifecycle manager.
[robot_state_publisher-3] [INFO] [1783512168.031829046] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-15] [INFO] [1783512168.034541781] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-15] [INFO] [1783512168.034932362] [keepout_mask_soft_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_mask_soft_server)
[map_server-15] [INFO] [1783512168.036776393] [keepout_mask_soft_server]: Deactivating
[map_server-15] [INFO] [1783512168.037360723] [keepout_mask_soft_server]: Destroying bond (keepout_mask_soft_server) to lifecycle manager.
[map_server-15] [INFO] [1783512168.070209414] [keepout_mask_soft_server]: Cleaning up
[map_server-15] [INFO] [1783512168.070477162] [keepout_mask_soft_server]: Destroying bond (keepout_mask_soft_server) to lifecycle manager.
[origincar_base_node-1] [INFO] [1783512168.035033194] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[origincar_base_node-1] [INFO] [1783512168.035545358] [origincar_base]: Stop command sent to STM32 on shutdown.
[origincar_base_node-1] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[origincar_base_node-1] terminate called after throwing an instance of 'rclcpp::exceptions::RCLError'
[origincar_base_node-1]   what():  failed to create guard condition: the given context is not valid, either rcl_init() was not called or rcl_shutdown() was called., at ./src/rcl/guard_condition.c:67
[map_server-14] [INFO] [1783512168.042503736] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[map_server-14] [INFO] [1783512168.042802609] [keepout_mask_server]: Running Nav2 LifecycleNode rcl preshutdown (keepout_mask_server)
[map_server-14] [INFO] [1783512168.043133066] [keepout_mask_server]: Deactivating
[map_server-14] [INFO] [1783512168.043276232] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[lifecycle_manager-17] [INFO] [1783512168.043970019] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-17] [INFO] [1783512168.044282059] [lifecycle_manager_keepout]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_keepout)
[lifecycle_manager-17] [INFO] [1783512168.044455975] [lifecycle_manager_keepout]: Terminating bond timer...
[competition_master_stage3.py-21] [INFO] [1783512168.113235131] [competition_master_stage3]: [MAIN] 收到 Ctrl+C, 停止录制 + 保存轨迹...
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[aurora930_node-9] I0708 20:02:48.098558  5640 ros2_node.cc:90] process quit succeed
[aurora930_node-9] I0708 20:02:48.098738  5640 aurora900_ros2_device.cc:83] begin stop()
[aurora930_node-9] I0708 20:02:48.098793  5640 aurora900_ros2_device.cc:103] stop stream
[map_server-14] [INFO] [1783512168.095592605] [keepout_mask_server]: Cleaning up
[map_server-14] [INFO] [1783512168.095873687] [keepout_mask_server]: Destroying bond (keepout_mask_server) to lifecycle manager.
[aurora930_node-9] 2026-07-08 20:02:48.131 ( 167.649s) [        B9E24020]      aurora900_impl.cc:648   INFO| ir_stream_count_=0, rgb_stream_count_=0, depth_stream_count_=0
[aurora930_node-9] 2026-07-08 20:02:48.131 ( 167.649s) [        B9E24020]      aurora900_impl.cc:649   INFO| mask=7
[aurora930_node-9] I0708 20:02:48.380801  5640 aurora900_ros2_device.cc:105] destroy stream
[aurora930_node-9] I0708 20:02:48.381209  5640 aurora900_ros2_device.cc:110] close glog
[aurora930_node-9] WARNING: Logging before InitGoogleLogging() is written to STDERR
[aurora930_node-9] I0708 20:02:48.381474  5640 ros2_device.cc:113] close device...
[aurora930_node-9] 2026-07-08 20:02:48.880 ( 168.398s) [        928E47E0]         cmd_backend.cc:40    INFO| RunBlocking is end!!!
[aurora930_node-9] 2026-07-08 20:02:49.081 ( 168.599s) [        B9E24020]deptrum_camera_vendor.c:121   INFO| device is close.
[aurora930_node-9] I0708 20:02:49.083544  5640 ros2_device.cc:116] quit succeed
[map_server-14] [INFO] [1783512168.229949769] [keepout_mask_server]: Destroying
[costmap_filter_info_server-16] [INFO] [1783512168.301325202] [keepout_filter_info_server]: Destroying
[component_container_isolated-18] [WARN] [1783512168.330434997] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512168.330671038] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.96, -0.06)
[component_container_isolated-18] [WARN] [1783512168.330782245] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1783512168.423016562] [local_costmap.local_costmap]: Message Filter dropping message: frame 'laser_link' at time 1783512167.910 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-18] [INFO] [1783512168.523175917] [global_costmap.global_costmap]: Received request to clear entirely the global_costmap
[component_container_isolated-18] [INFO] [1783512168.664817165] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/costmap_ctrl" topic for filter info...
[component_container_isolated-18] [INFO] [1783512168.682440024] [global_costmap.global_costmap]: KeepoutFilter: Received filter info from /costmap_ctrl topic.
[component_container_isolated-18] [INFO] [1783512168.682631898] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [WARN] [1783512168.690324855] [global_costmap.global_costmap]: KeepoutFilter: New costmap filter info arrived from /costmap_ctrl topic. Updating old filter info.
[component_container_isolated-18] [INFO] [1783512168.700787713] [global_costmap.global_costmap]: KeepoutFilter: Subscribing to "/keepout_mask" topic for filter mask...
[component_container_isolated-18] [INFO] [1783512168.959532305] [waypoint_follower]: Running Nav2 LifecycleNode rcl preshutdown (waypoint_follower)
[component_container_isolated-18] [INFO] [1783512168.959950386] [waypoint_follower]: Deactivating
[component_container_isolated-18] [INFO] [1783512168.960165843] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512168.970887574] [waypoint_follower]: Cleaning up
[component_container_isolated-18] [INFO] [1783512169.003699057] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512169.005155299] [bt_navigator]: Running Nav2 LifecycleNode rcl preshutdown (bt_navigator)
[component_container_isolated-18] [INFO] [1783512169.005487339] [bt_navigator]: Deactivating
[component_container_isolated-18] [WARN] [1783512169.005606588] [bt_navigator]: [navigate_to_pose] [ActionServer] Requested to deactivate server but goal is still executing. Should check if action server is running before deactivating.
[component_container_isolated-18] [INFO] [1783512169.019448023] [amcl]: Message Filter dropping message: frame 'laser_link' at time 1783512168.009 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[component_container_isolated-18] [INFO] [1783512169.105795750] [bt_navigator]: [navigate_to_pose] [ActionServer] Waiting for async process to finish.
[component_container_isolated-18] [INFO] [1783512169.206480828] [bt_navigator]: [navigate_to_pose] [ActionServer] Waiting for async process to finish.
[component_container_isolated-18] [WARN] [1783512169.218483023] [planner_server]: GridBased: failed to create plan, invalid use: Starting point in lethal space! Cannot create feasible plan..
[component_container_isolated-18] [WARN] [1783512169.218796605] [planner_server]: Planning algorithm GridBased failed to generate a valid path to (0.96, -0.06)
[component_container_isolated-18] [INFO] [1783512169.218890230] [planner_server]: [compute_path_to_pose] [ActionServer] Client requested to cancel the goal. Cancelling.
[component_container_isolated-18] [WARN] [1783512169.219366186] [bt_navigator]: [navigate_to_pose] [ActionServer] Aborting handle.
[component_container_isolated-18] [INFO] [1783512169.219875850] [bt_navigator]: Goal canceled
[component_container_isolated-18] [WARN] [1783512169.219939808] [bt_navigator]: [navigate_to_pose] [ActionServer] Stopping the thread per request.
[component_container_isolated-18] [INFO] [1783512169.220318598] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512169.230681217] [bt_navigator]: Cleaning up
[map_server-15] [INFO] [1783512168.522847710] [keepout_mask_soft_server]: Destroying
[INFO] [map_server-15]: process has finished cleanly [pid 5724]
[lifecycle_manager-17] [INFO] [1783512168.660567730] [lifecycle_manager_keepout]: Destroying lifecycle_manager_keepout
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
[speed_profile_node.py-22] Traceback (most recent call last):
[speed_profile_node.py-22]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/speed_profile_node.py", line 390, in main
[speed_profile_node.py-22]     rclpy.spin(node)
[speed_profile_node.py-22]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 229, in spin
[speed_profile_node.py-22]     executor.spin_once()
[speed_profile_node.py-22]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 808, in spin_once
[speed_profile_node.py-22]     self._spin_once_impl(timeout_sec)
[speed_profile_node.py-22]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 805, in _spin_once_impl
[speed_profile_node.py-22]     raise handler.exception()
[speed_profile_node.py-22]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/task.py", line 272, in _execute_coroutine_step
[speed_profile_node.py-22]     result = coro.send(None)
[speed_profile_node.py-22]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 478, in handler
[speed_profile_node.py-22]     arg = take_from_wait_list(entity)
[speed_profile_node.py-22]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 400, in _take_subscription
[speed_profile_node.py-22]     msg_info = sub.handle.take_message(sub.msg_type, sub.raw)
[speed_profile_node.py-22] RuntimeError: Unable to convert call argument to Python object (compile in debug mode for details)
[speed_profile_node.py-22]
[speed_profile_node.py-22] During handling of the above exception, another exception occurred:
[speed_profile_node.py-22]
[speed_profile_node.py-22] Traceback (most recent call last):
[speed_profile_node.py-22]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/speed_profile_node.py", line 399, in <module>
[speed_profile_node.py-22]     main()
[speed_profile_node.py-22]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/speed_profile_node.py", line 395, in main
[speed_profile_node.py-22]     rclpy.shutdown()
[speed_profile_node.py-22]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 130, in shutdown
[speed_profile_node.py-22]     _shutdown(context=context)
[speed_profile_node.py-22]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/utilities.py", line 58, in shutdown
[speed_profile_node.py-22]     return context.shutdown()
[speed_profile_node.py-22]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/context.py", line 102, in shutdown
[speed_profile_node.py-22]     self.__context.shutdown()
[speed_profile_node.py-22] rclpy._rclpy_pybind11.RCLError: failed to shutdown: rcl_shutdown already called on the given context, at ./src/rcl/init.c:241
[competition_master_stage3.py-21] [INFO] [1783512169.842440358] [competition_master_stage3]: [BAG] 录制已停止
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512169.846057425] [competition_master_stage3]:
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512169.849514451] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512169.852776853] [competition_master_stage3]: >>> [Stage 3] 任务结束 <<<
[INFO] [lifecycle_manager-17]: process has finished cleanly [pid 5728]
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512169.859627321] [competition_master_stage3]:   最终状态: RETURN_P
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512169.876434202] [competition_master_stage3]:   总耗时:   134.7s
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512169.886675488] [competition_master_stage3]:   --- 各阶段耗时 ---
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512169.896278694] [competition_master_stage3]:   LAUNCH................ 22.9s
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512169.906380981] [competition_master_stage3]:   NAV_TO_QR............. 14.1s
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[component_container_isolated-18] [INFO] [1783512169.915552147] [bt_navigator]: Completed Cleaning up
[component_container_isolated-18] [INFO] [1783512169.915835771] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512169.915914603] [lifecycle_manager_localization]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_localization)
[component_container_isolated-18] [INFO] [1783512169.915983978] [lifecycle_manager_localization]: Terminating bond timer...
[competition_master_stage3.py-21] [INFO] [1783512169.921126704] [competition_master_stage3]:   BACKING_UP............ 6.0s
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512169.931998779] [competition_master_stage3]:   CRUISE_CHANNEL........ 78.0s
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512169.938591874] [competition_master_stage3]:   (transition/overhead). 13.7s
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512169.941894442] [competition_master_stage3]:   --- ---
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512169.946479879] [competition_master_stage3]:   QR 原始数据: 1584
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512169.953512847] [competition_master_stage3]:   QR 方向:   逆时针 (CW=顺时针/odd, CCW=逆时针/even)
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[component_container_isolated-18] [INFO] [1783512169.956333917] [planner_server]: Running Nav2 LifecycleNode rcl preshutdown (planner_server)
[component_container_isolated-18] [INFO] [1783512169.956613041] [planner_server]: Deactivating
[component_container_isolated-18] [INFO] [1783512169.956893415] [global_costmap.global_costmap]: Deactivating
[INFO] [imu_madgwick_filter.py-6]: process has finished cleanly [pid 5600]
[competition_master_stage3.py-21] [INFO] [1783512169.957301330] [competition_master_stage3]:   VLM 结果:  图像中无此人形立牌，仅有一个带白色反光条的蓝色交通锥置于地面，背景为浅色墙面，右侧有黑色大型物体（疑似设备），场景似室内作业区或走廊，未呈现医疗巡检相关的人形立牌及动作。
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[yolo_costmap_bridge.py-20] Traceback (most recent call last):
[yolo_costmap_bridge.py-20]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/yolo_costmap_bridge.py", line 178, in <module>
[yolo_costmap_bridge.py-20]     main()
[yolo_costmap_bridge.py-20]   File "/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/yolo_costmap_bridge.py", line 174, in main
[yolo_costmap_bridge.py-20]     rclpy.shutdown()
[yolo_costmap_bridge.py-20]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 130, in shutdown
[yolo_costmap_bridge.py-20]     _shutdown(context=context)
[yolo_costmap_bridge.py-20]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/utilities.py", line 58, in shutdown
[yolo_costmap_bridge.py-20]     return context.shutdown()
[yolo_costmap_bridge.py-20]   File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/context.py", line 102, in shutdown
[yolo_costmap_bridge.py-20]     self.__context.shutdown()
[yolo_costmap_bridge.py-20] rclpy._rclpy_pybind11.RCLError: failed to shutdown: rcl_shutdown already called on the given context, at ./src/rcl/init.c:241
[competition_master_stage3.py-21] [INFO] [1783512169.960875271] [competition_master_stage3]:   超时限制:  180.0s (全局)
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[INFO] [imu_madgwick_filter.py-4]: process has finished cleanly [pid 5596]
[competition_master_stage3.py-21] [INFO] [1783512169.964273881] [competition_master_stage3]: ============================================================
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512169.968519528] [competition_master_stage3]: [CPU] governor → schedutil
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512169.975279747] [competition_master_stage3]: [TRAJ] CSV已保存: /userdata/dev_ws/trajectory_20260708_200249.csv (109 点)
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[component_container_isolated-18] [INFO] [1783512170.195626441] [planner_server]: Deactivating plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1783512170.196007022] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512170.206513932] [planner_server]: Cleaning up
[INFO] [aurora930_node-9]: process has finished cleanly [pid 5640]
[component_container_isolated-18] [INFO] [1783512170.277711396] [global_costmap.global_costmap]: Cleaning up
[component_container_isolated-18] [INFO] [1783512170.295247857] [planner_server]: Cleaning up plugin GridBased of type SmacPlannerHybrid
[component_container_isolated-18] [INFO] [1783512170.296506809] [planner_server]: Destroying plugin GridBased of type SmacPlannerHybrid
[ERROR] [speed_profile_node.py-22]: process has died [pid 5950, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/speed_profile_node.py --ros-args -r __node:=speed_profile_node --params-file /tmp/launch_params_gm7sdw5t'].
[ERROR] [bmi088_iio_bridge.py-5]: process has died [pid 5598, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/bmi088_iio_bridge.py --ros-args -r __node:=bmi088_iio_bridge --params-file /tmp/launch_params_w4ae0e7r'].
[ERROR] [yolo_costmap_bridge.py-20]: process has died [pid 5942, exit code 1, cmd '/userdata/dev_ws/install/origincar_bringup/lib/origincar_bringup/yolo_costmap_bridge.py --ros-args -r __node:=yolo_costmap_bridge'].
[INFO] [racing_obstacle_detection_yolo-19]: process has finished cleanly [pid 5940]
[competition_master_stage3.py-21] [INFO] [1783512170.437840242] [competition_master_stage3]: [TRAJ] Nav2 params snapshot: 31 keys
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512170.442119681] [competition_master_stage3]: [TRAJ] 摘要JSON已保存: /userdata/dev_ws/trajectory_20260708_200249_summary.json
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512170.446125495] [competition_master_stage3]: [TRAJ] 规划历史已保存: /userdata/dev_ws/trajectory_20260708_200249_plans.csv (62 次规划)
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[competition_master_stage3.py-21] [INFO] [1783512170.464883992] [competition_master_stage3]: [TRAJ] costmap PGM已保存: /userdata/dev_ws/trajectory_20260708_200249_costmap.pgm
[competition_master_stage3.py-21] Failed to publish log message to rosout: publisher's context is invalid, at ./src/rcl/publisher.c:389
[ERROR] [vision_ai_node-12]: process has died [pid 5648, exit code 1, cmd '/userdata/dev_ws/install/racing_vision_ai/lib/racing_vision_ai/vision_ai_node --ros-args -r __node:=vision_ai_node'].
[component_container_isolated-18] [INFO] [1783512171.326721691] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512171.326885190] [amcl]: Running Nav2 LifecycleNode rcl preshutdown (amcl)
[component_container_isolated-18] [INFO] [1783512171.326996106] [amcl]: Deactivating
[component_container_isolated-18] [INFO] [1783512171.327181647] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512171.337851473] [amcl]: Cleaning up
[component_container_isolated-18] [INFO] [1783512171.351532743] [amcl]: Destroying bond (amcl) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512171.351679451] [smoother_server]: Running Nav2 LifecycleNode rcl preshutdown (smoother_server)
[component_container_isolated-18] [INFO] [1783512171.351895658] [smoother_server]: Deactivating
[component_container_isolated-18] [INFO] [1783512171.351960074] [smoother_server]: Deactivating smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1783512171.352094282] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512171.362552651] [smoother_server]: Cleaning up
[component_container_isolated-18] [INFO] [1783512171.362760150] [smoother_server]: Cleaning up smoother: SmoothPath of type nav2_constrained_smoother::ConstrainedSmoother
[component_container_isolated-18] [INFO] [1783512171.380022862] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512171.380173695] [map_server]: Running Nav2 LifecycleNode rcl preshutdown (map_server)
[component_container_isolated-18] [INFO] [1783512171.380303152] [map_server]: Deactivating
[component_container_isolated-18] [INFO] [1783512171.380448568] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512171.390861854] [map_server]: Cleaning up
[component_container_isolated-18] [INFO] [1783512171.391096561] [map_server]: Destroying bond (map_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512171.391168394] [behavior_server]: Running Nav2 LifecycleNode rcl preshutdown (behavior_server)
[component_container_isolated-18] [INFO] [1783512171.391278893] [behavior_server]: Deactivating
[component_container_isolated-18] [INFO] [1783512171.391505101] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512171.401974011] [behavior_server]: Cleaning up
[component_container_isolated-18] [INFO] [1783512171.409607559] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512171.409752725] [velocity_smoother]: Running Nav2 LifecycleNode rcl preshutdown (velocity_smoother)
[component_container_isolated-18] [INFO] [1783512171.409884224] [velocity_smoother]: Deactivating
[component_container_isolated-18] [INFO] [1783512171.410226556] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512171.420621342] [velocity_smoother]: Cleaning up
[component_container_isolated-18] [INFO] [1783512171.420836382] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512171.420908674] [controller_server]: Running Nav2 LifecycleNode rcl preshutdown (controller_server)
[component_container_isolated-18] [INFO] [1783512171.421029506] [controller_server]: Deactivating
[component_container_isolated-18] [INFO] [1783512171.421098714] [controller_server]: Deactivating controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1783512171.421304505] [local_costmap.local_costmap]: Deactivating
[component_container_isolated-18] [INFO] [1783512171.519439095] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[component_container_isolated-18] [INFO] [1783512171.530205920] [controller_server]: Cleaning up
[component_container_isolated-18] [INFO] [1783512171.530333211] [controller_server]: Cleaning up controller: FollowPath of type regulated_pure_pursuit_controller::RegulatedPurePursuitController
[component_container_isolated-18] [INFO] [1783512171.530573627] [local_costmap.local_costmap]: Cleaning up
[INFO] [competition_master_stage3.py-21]: process has finished cleanly [pid 5944]
[component_container_isolated-18] [INFO] [1783512172.574442763] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[ERROR] [component_container_isolated-18]: process[component_container_isolated-18] failed to terminate '5' seconds after receiving 'SIGINT', escalating to 'SIGTERM'
[INFO] [component_container_isolated-18]: sending signal 'SIGTERM' to process[component_container_isolated-18]
[component_container_isolated-18] [INFO] [1783512174.535723860] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[ERROR] [component_container_isolated-18]: process[component_container_isolated-18] failed to terminate '10.0' seconds after receiving 'SIGTERM', escalating to 'SIGKILL'
[INFO] [component_container_isolated-18]: sending signal 'SIGKILL' to process[component_container_isolated-18]
[ERROR] [component_container_isolated-18]: process has died [pid 5929, exit code -9, cmd '/opt/ros/humble/lib/rclcpp_components/component_container_isolated --ros-args --log-level info --ros-args -r __node:=nav2_container --params-file /tmp/launch_params_obl7siez --params-file /tmp/launch_params_xmosiznn -r /tf:=tf -r /tf_static:=tf_static'].
root@ubuntu:/userdata/dev_ws#
