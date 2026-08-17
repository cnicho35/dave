import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

_ARDUSUB_WS = "/home/comet/ardusub_ws"


def generate_launch_description():
    env_vars = [
        SetEnvironmentVariable("PATH", f"{_ARDUSUB_WS}/ardupilot/build/sitl/bin:{os.getenv('PATH', '')}"),
        SetEnvironmentVariable("GZ_SIM_SYSTEM_PLUGIN_PATH", f"{_ARDUSUB_WS}/ardupilot_gazebo/build:{os.getenv('GZ_SIM_SYSTEM_PLUGIN_PATH', '')}"),
        SetEnvironmentVariable("GZ_SIM_RESOURCE_PATH", f"{_ARDUSUB_WS}/ardupilot_gazebo/models:{_ARDUSUB_WS}/ardupilot_gazebo/worlds:{os.getenv('GZ_SIM_RESOURCE_PATH', '')}"),
    ]

    joy_node = Node(
        package="joy",
        executable="joy_node",
        name="ps4_controller",
        parameters=[{"device_id": 0, "deadzone": 0.05, "autorepeat_rate": 20.0}],
        output="screen",
    )

    dave_robot_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare("dave_demos"), "launch", "dave_robot.launch.py"])
        ),
        launch_arguments={
            "z": "-0.5",
            "namespace": "bluerov2",
            "world_name": "dave_ocean_waves",
            "paused": "false",
            "open_virtual_joystick": "false",
            "open_qgc": "false",
            "use_teleop": "true",
            "use_web_joystick": "false",
        }.items(),
    )

    return LaunchDescription(env_vars + [joy_node, dave_robot_launch])

