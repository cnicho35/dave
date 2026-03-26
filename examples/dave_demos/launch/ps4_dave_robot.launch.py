from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    OpaqueFunction,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def launch_setup(context, *args, **kwargs):
    # PS4 controller joy node – reads the gamepad and publishes sensor_msgs/Joy
    # to /joy, which is the topic consumed by ardusub_manual_control.py to drive
    # the bluerov2 via MAVROS ManualControl messages.
    joy_node = Node(
        package="joy",
        executable="joy_node",
        name="ps4_controller",
        parameters=[
            {
                "device_id": 0,
                "deadzone": 0.05,
                "autorepeat_rate": 20.0,
            }
        ],
        output="screen",
    )

    # Include the main dave_robot launch file with PS4-specific defaults.
    # use_web_joystick is disabled because the real PS4 controller is used instead.
    dave_robot_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                PathJoinSubstitution(
                    [
                        FindPackageShare("dave_demos"),
                        "launch",
                        "dave_robot.launch.py",
                    ]
                )
            ]
        ),
        launch_arguments={
            "z": LaunchConfiguration("z"),
            "namespace": LaunchConfiguration("namespace"),
            "world_name": LaunchConfiguration("world_name"),
            "paused": LaunchConfiguration("paused"),
            "open_virtual_joystick": LaunchConfiguration("open_virtual_joystick"),
            "open_qgc": LaunchConfiguration("open_qgc"),
            "use_web_joystick": "false",
        }.items(),
    )

    return [joy_node, dave_robot_launch]


def generate_launch_description():
    args = [
        DeclareLaunchArgument(
            "z",
            default_value="-0.5",
            description="Initial z position of the bluerov2",
        ),
        DeclareLaunchArgument(
            "namespace",
            default_value="bluerov2",
            description="Robot namespace",
        ),
        DeclareLaunchArgument(
            "world_name",
            default_value="dave_ocean_waves",
            description="Gazebo world file to launch",
        ),
        DeclareLaunchArgument(
            "paused",
            default_value="false",
            description="Start the simulation paused",
        ),
        DeclareLaunchArgument(
            "open_virtual_joystick",
            default_value="false",
            description="Open the virtual joystick page in Firefox",
        ),
        DeclareLaunchArgument(
            "open_qgc",
            default_value="false",
            description="Launch QGroundControl",
        ),
    ]

    return LaunchDescription(args + [OpaqueFunction(function=launch_setup)])
