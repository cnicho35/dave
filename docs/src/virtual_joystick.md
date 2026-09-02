# Virtual Joystick

Use the virtual-joystick launch when a PS4 controller is unavailable. It starts the same BlueROV2 and tidal-energy scenario but enables the virtual and web joystick options instead of starting `joy_node`.

## Launch

From a built and sourced DAVE workspace, run:

```bash
ros2 launch dave_demos tidal_virt_js_dave_robot.launch.py
```

The checked-in launch config uses `/opt/ardusub_ws` for its ArduSub and Gazebo environment paths. Install ArduSub at that location or update the launch configuration as part of a tested local setup.

## Confirm The Scenario

The launch starts the `marine_energy_tidal` world, the BlueROV2 in the `bluerov2` namespace, the `Base`, `Blades`, and `Nacelle` turbine models, and RViz with the underwater-camera configuration. It also requests both `open_virtual_joystick` and `use_web_joystick`.

The exact control interface and mappings depend on the installed DAVE and ArduSub components. Verify the available interface in your running simulation before using it for a training activity.

Return to [Operate the BlueROV](marine_energy_world.md) when the vehicle is ready.