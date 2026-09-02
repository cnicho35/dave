# Operate the BlueROV

The Robotics World for Marine Energy was built using the DAVE Aquatic Virtual Environment (DAVE) software package, which leverages ROS2 and Gazebo to create a realistic simulation environment for marine energy robotics research and development. We enabled Marine Energy-specific scenarios and models to facilitate the study and development of robotic systems in this domain.

The baseline scenario includes a Tidal Energy Converter (TEC) model developed by IKM3D for simulation and training.

## Learning Objective

Use the BlueROV2 to approach a TEC, establish a useful camera viewpoint, and perform a visual inspection in simulation.

## Start The Scenario

Complete [First Marine Energy Simulation](first_simulation.md) before starting this exercise. The PS4-controller launch is:

```bash
ros2 launch dave_demos tidal_ps4_dave_robot.launch.py
```

The launch starts the BlueROV2 in the `bluerov2` namespace, the `marine_energy_tidal` world, the TEC `Base`, `Blades`, and `Nacelle`, the `joy` node, and RViz. It expects a controller at `device_id` `0`; use [Virtual Joystick](virtual_joystick.md) when a physical controller is unavailable.

![](images/gazebo_view.png#center)

## Inspection Activity

1. Wait for the ROV, turbine components, Gazebo, and RViz to appear.
2. Use the controller to move the BlueROV2 from its initial position toward the TEC.
3. Establish a stable viewing angle where the turbine base, nacelle, or blades are visible in the camera view.
4. Inspect the visible surfaces and note any simulated condition that would require follow-up in a training discussion.
5. Return to a clear, stable viewpoint and capture evidence following [Camera Evidence](camera_evidence.md).

Do not infer real equipment condition or operating clearance from this simulation. Use its observations to practice communication, situational awareness, and inspection planning.

## Camera View

The BlueROV2 has a simulated onboard camera. The launch opens RViz with the repository's underwater-camera configuration so you can use the image feed while navigating. Continue to [Camera Evidence](camera_evidence.md) for a verified discovery workflow before recording data.

![](images/camera_view.png#center)