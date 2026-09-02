# Troubleshooting First Launch

Use this page when the first tidal-energy simulation does not build, start, or respond as expected.

## A ROS 2 Package Is Not Found

Build and source the workspace from its root:

```bash
colcon build
source install/setup.bash
```

Then retry the launch. If `dave_demos` or `marine_energy_models` is still not found, confirm that both packages are present in the workspace source tree and that the build completed without errors.

## Gazebo Cannot Find A Model Or Plugin

The tidal launch configures ArduSub executable, system-plugin, model, and world paths. Confirm that the ArduSub workspace exists at the location expected by the launch file:

- `tidal_ps4_dave_robot.launch.py` expects `/home/comet/ardusub_ws`.
- `tidal_virt_js_dave_robot.launch.py` expects `/opt/ardusub_ws`.

The repository includes installation scripts under `extras/` for these layouts. Choose the launch path that matches your installation, or update the launch configuration as part of a locally tested setup. See [Install and Verify](getting_started.md).

## The Controller Does Not Respond

The PS4 launch starts `joy_node` with `device_id` set to `0`. Connect the controller before launching, confirm Linux can see it, and verify that it is the first joystick device. If it is not, use the [Virtual Joystick](virtual_joystick.md) path or adjust the launch configuration for your local device order.

## RViz Does Not Show The Camera View

The launch opens RViz with the repository's `underwater_camera.rviz` configuration. Wait for the simulation to finish starting, then check terminal output for missing packages or resource errors. Use [Camera Evidence](camera_evidence.md) to inspect available ROS 2 topics after the baseline launch is working.

## Simulation Performance Is Poor

Close other graphics-intensive applications and confirm that the system is using its supported GPU driver. The documentation recommends 16 GB RAM, a modern processor, and a GPU for the best experience. Lower-performance computers can run the software with reduced responsiveness.

## Still Blocked

Record the complete command you ran and the first relevant error from the terminal. Include your Ubuntu, ROS 2, and Gazebo versions, whether you use a physical controller or the virtual joystick, and the ArduSub workspace path when requesting support.