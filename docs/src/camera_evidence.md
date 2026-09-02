# Camera Evidence

Use the simulated underwater camera to collect reproducible visual evidence during an inspection exercise.

## Confirm The Baseline View

Start the scenario using [First Marine Energy Simulation](first_simulation.md). The launch opens RViz with `underwater_camera.rviz`. Confirm that this configured display receives an image before changing RViz settings or recording data.

## Discover The Image Topic

Topic names can differ with launch configuration and package versions. Query the running system rather than assuming a topic name:

```bash
ros2 topic list
ros2 topic list --types | grep -i image
```

Inspect a candidate image topic before using it:

```bash
ros2 topic info <image-topic> -v
```

Replace `<image-topic>` with a topic returned by your running simulation. The detailed information shows its message type and publishers so you can confirm it belongs to the intended camera.

## Collect Evidence

For each screenshot, still image, or locally tested video capture, record:

- The date and time of capture.
- The scenario and launch file used.
- The ROV viewpoint and TEC component shown.
- The image topic or RViz display used.
- Any limitation, such as obscured geometry, poor lighting, or motion.

Do not treat a simulation image as a real inspection record. It is evidence of a training activity and a basis for discussing inspection planning.

Use this workflow in [Challenge 2](challenges.md).