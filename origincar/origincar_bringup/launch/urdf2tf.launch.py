import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    urdf_tutorial_path = get_package_share_directory('origincar_description')
    origincar_model_path = urdf_tutorial_path + '/urdf/laser_slam_only.urdf'
    action_declare_arg_mode_path = launch.actions.DeclareLaunchArgument(
        'model',
        default_value=str(origincar_model_path),
        description='urdf的绝对路径')
    robot_description = launch_ros.parameter_descriptions.ParameterValue(
        launch.substitutions.Command(
            ['cat ', launch.substitutions.LaunchConfiguration('model')]),  # 注意这里添加了空格
            value_type=str)
    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}])
    # 由于URDF全是固定关节，不需要joint_state_publisher
    # joint_state_publisher_node = launch_ros.actions.Node(
    #         package='joint_state_publisher', 
    #         executable='joint_state_publisher', 
    #         name='joint_state_publisher',
    # )

    return launch.LaunchDescription([
        action_declare_arg_mode_path,
        robot_state_publisher_node,
        # joint_state_publisher_node
    ])