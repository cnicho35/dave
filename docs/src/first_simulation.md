# First Marine Energy Simulation

This tutorial starts the tidal-energy scenario, places a BlueROV2 near a tidal energy converter (TEC), and opens an RViz view configured for the simulated underwater camera.

## Before You Start

Complete [Install and Verify](getting_started.md) before running this tutorial. You need a DAVE workspace that builds successfully, an ArduSub installation that matches the launch file you choose, and either a connected PS4 controller or the virtual joystick option.

## Build And Source The Workspace

Open a terminal in the root of your DAVE workspace, then build and source the overlay:

```bash
colcon build
source install/setup.bash
```

Run the `source` command again in each new terminal that will use packages from this workspace.

## Start The PS4 Controller Scenario

Connect the controller before launching. Then run:

```bash
ros2 launch dave_demos tidal_ps4_dave_robot.launch.py
```

This launch starts the `joy` controller node, a BlueROV2 in the `bluerov2` namespace, the `marine_energy_tidal` Gazebo world, three TEC model components, and RViz with `underwater_camera.rviz`.

## Confirm A Successful Launch

The first launch can take longer while Gazebo downloads Fuel-hosted world assets. A successful launch gives you:

- A Gazebo window showing an underwater world, the BlueROV2, and the TEC assembly.
- An RViz window using the underwater-camera configuration.
- Terminal output from ROS 2 launch processes without an immediate missing-package, plugin, or resource error.
- A controller recognized by the `joy` node when using the PS4 path.

Use the Gazebo camera to orient yourself, then use the configured RViz view to inspect the ROV camera output.

## End The Session

Press `Ctrl+C` in the terminal that started the launch. This stops the ROS 2 processes and closes the simulation components they started.

## Next Steps

Follow [Operate the BlueROV](marine_energy_world.md) for a guided inspection activity, or use [Troubleshooting First Launch](troubleshooting.md) if the scenario does not start as expected.

!!! note
    This scenario supports training and familiarization. It does not replace equipment manuals, site procedures, or offshore safety requirements.