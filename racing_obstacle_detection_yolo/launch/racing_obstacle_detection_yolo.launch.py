import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.substitutions import TextSubstitution
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory


def generate_launch_description():

    image_width_launch_arg = DeclareLaunchArgument(
        "dnn_sample_image_width", default_value=TextSubstitution(text="640")
    )
    image_height_launch_arg = DeclareLaunchArgument(
        "dnn_sample_image_height", default_value=TextSubstitution(text="480")
    )

    usb_node = IncludeLaunchDescription(PythonLaunchDescriptionSource(get_package_share_directory('hobot_usb_cam') + '/launch/hobot_usb_cam.launch.py'),
                                    launch_arguments={'usb_image_width': '640', 'usb_image_height': '480',
                                                'usb_video_device': '/dev/video0'}.items())

    web_show = "TRUE"
    print("web_show is ", web_show)
    print(get_package_share_directory('hobot_codec'))

    nv12_codec_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(get_package_share_directory('hobot_codec') + '/launch/hobot_codec_decode.launch.py'),
                                               launch_arguments={'codec_in_mode': 'ros', 'codec_out_mode': 'shared_mem',
                                                                 'codec_sub_topic': '/image', 'codec_pub_topic': '/hbmem_img'}.items())

    # jpeg图片编码&发布pkg
    jpeg_codec_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('hobot_codec'),
                'launch/hobot_codec_encode.launch.py')),
        launch_arguments={
            'codec_in_mode': 'shared_mem',
            'codec_out_mode': 'ros',
            'codec_sub_topic': '/hbmem_img',
            'codec_pub_topic': '/image_jpeg'
        }.items()
    )

    web_node = IncludeLaunchDescription(PythonLaunchDescriptionSource(get_package_share_directory('websocket') + '/launch/websocket.launch.py'),
                    launch_arguments={'websocket_image_topic': '/image', 'websocket_image_type': 'mjpeg',
                    'websocket_smart_topic': '/racing_obstacle_detection'}.items())

    image_transport_node = Node(
        package='utils',
        executable='image_transport_node',
        output='screen',
        arguments=['--ros-args', '--log-level', 'info']
    )


    # 障碍物检测pkg
    racing_obstacle_detection_yolov5_node = Node(
        package='racing_obstacle_detection_yolo',
        executable='racing_obstacle_detection_yolo',
        output='screen',
        parameters=[
            {"is_shared_mem_sub": True}, #True
            {"sub_img_topic": "/hbmem_img"},
            {"config_file": "/userdata/dev_ws/src/origincar/origincar_bringup/config/yolov5workconfig.json"},
        ],
        arguments=['--ros-args', '--log-level', 'warn']
    )

    return LaunchDescription([
        usb_node,
        racing_obstacle_detection_yolov5_node,
        nv12_codec_node,
        web_node,
    ])
