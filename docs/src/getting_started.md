# Install and Verify

## Your Computer

Running the Robotics World for Marine Energy requires 25 GB of free disk space. For the best experience, use a modern processor, a supported GPU, and at least 16 GB of RAM. The software may run on a less capable computer with reduced simulation performance.

## Setting up your computer

If you already have Windows on your computer, we recommend dual booting Ubuntu alongside it to run the Robotics World for Marine Energy. This allows you to use Ubuntu for the software while still keeping your Windows installation for other tasks.

If you do not have Windows, you can install Ubuntu as your primary operating system. Make sure to back up any important data before proceeding with the installation.

## Installing Ubuntu

Ubuntu is a popular open-source Linux distribution that is widely used for development and research purposes. It is available for free to download and install.

For instructions on dual booting Ubuntu alongside Windows, please refer to the official Ubuntu documentation: [Ubuntu Dual Boot Guide](https://help.ubuntu.com/community/WindowsDualBoot).

For instructions on installing Ubuntu as your primary operating system, please refer to the official Ubuntu documentation: [Ubuntu Installation Guide](https://ubuntu.com/tutorials/install-ubuntu-desktop).


!!!note
    Make sure you select Ubuntu 24.04 LTS as the version to install.

    Ensure that your computer meets the minimum system requirements before proceeding with the installation.

The process of installing Ubuntu involves creating a bootable USB drive, booting from it, and following the on-screen instructions to complete the installation. Make sure to carefully follow each step to avoid data loss and ensure a successful installation.

## Installing ROS2 and Gazebo

!!! note
    Make sure you install ROS2 Jazzy and Gazebo Harmonic and not any other versions. Using different versions may lead to compatibility issues and unexpected behavior in the Robotics World for Marine Energy.

To install ROS2 and Gazebo on Ubuntu, follow the official installation guides:

- [ROS2 Installation Guide](https://docs.ros.org/en/jazzy/Installation.html)
- [Gazebo Installation Guide](https://gazebosim.org/docs/harmonic/ros_installation/)


## Install Project Dependencies

In addition to ROS 2 Jazzy and Gazebo Harmonic, the tidal scenario requires:

- A supported NVIDIA or AMD GPU driver.
- ROS-Gazebo integration packages, including `ros_gz_sim`.
- ArduSub and `ardupilot_gazebo` for the simulated vehicle control stack.
- The Linux joystick driver and a PS4 controller for the physical-controller scenario.

The repository provides ArduSub installers in `extras/ardusub-ubuntu-install.sh` and `extras/ardusub-ubuntu-install-local.sh`. The standard installer uses `/opt/ardusub_ws`; the local installer uses `/home/<user>/ardusub_ws`.

!!! warning
    The checked-in PS4 launch file currently expects `/home/comet/ardusub_ws`, while the virtual joystick launch expects `/opt/ardusub_ws`. Confirm the path in the launch file matches your ArduSub installation before launching. This is a local configuration requirement, not an automatic discovery step.

## Build And Verify The Workspace

From the root of a workspace containing this repository, build and source the overlay:

```bash
colcon build
source install/setup.bash
```

Before moving on, confirm the build completes and ROS 2 can locate the main launch package:

```bash
ros2 pkg prefix dave_demos
```

For the physical-controller path, connect the controller before starting the scenario. For a controller-free option, see [Virtual Joystick](virtual_joystick.md).

## Launching the Robotics World for Marine Energy

After the build and package check succeed, continue with [First Marine Energy Simulation](first_simulation.md).

## Troubleshooting

See [Troubleshooting First Launch](troubleshooting.md) for package, resource-path, controller, camera, and performance issues.

