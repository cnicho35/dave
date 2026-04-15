import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

_ARDUSUB_WS = "/opt/ardusub_ws"

# Turbine components: model name → (x, y, z, roll, pitch, yaw)
_TURBINE_COMPONENTS = {
    "Base": ("15", "0", "-15", "1.5708", "0", "1.5708"),
    "Blades": ("15", "0", "-15", "1.5708", "0", "1.5708"),
    "Nacelle": ("15", "0", "-15", "1.5708", "0", "1.5708"),
}


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
            "world_name": "marine_energy_tidal",
            "paused": "false",
            "open_virtual_joystick": "false",
            "open_qgc": "false",
            "use_teleop": "true",
            "use_web_joystick": "false",
        }.items(),
    )

    turbine_launches = [
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution(
                    [FindPackageShare("marine_energy_models"), "launch", "upload_object.launch.py"]
                )
            ),
            launch_arguments={
                "model_name": model,
                "x": pose[0],
                "y": pose[1],
                "z": pose[2],
                "roll": pose[3],
                "pitch": pose[4],
                "yaw": pose[5],
            }.items(),
        )
        for model, pose in _TURBINE_COMPONENTS.items()
    ]

    return LaunchDescription(env_vars + [joy_node, dave_robot_launch] + turbine_launches)

