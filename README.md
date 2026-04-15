# DAVE

[![Publish a Docker image (AMD64; Common X86_64 Linux Machine)](https://github.com/IOES-Lab/dave/actions/workflows/docker-amd64.yml/badge.svg)](https://github.com/IOES-Lab/dave/actions/workflows/docker-amd64.yml)
[![Publish a Docker image (ARM64; Apple Silicon)](https://github.com/IOES-Lab/dave/actions/workflows/docker-arm64v8.yml/badge.svg?branch=ros2)](https://github.com/IOES-Lab/dave/actions/workflows/docker-arm64v8.yml)

Documentation is currently at [http://dave-ros2.notion.site](http://dave-ros2.notion.site)

For contribution, do `pip3 install pre-commit && pre-commit install && pre-commit run --all-files` before commit.


## Casey Nichols edits:

- Must run extras/ardusub-ubuntu-install.sh

One line start

```bash
colcon build && source install/setup.bash && ros2 launch dave_demos ps4_dave_robot.launch.py 
```


## References

Marine Energy models were designed by IKM 3D [https://www.ikm3d.com/] for ReDi Island [https://www.nlr.gov/water/redi-island].

DAVE Simulation:
Mabel M. Zhang, Woen-Sug Choi, Jessica Herman, Duane Davis, Carson Vogt, Michael McCarrin, Yadunund Vijay, Dharini Dutia, William Lew, Steven Peters, and Brian Bingham, "DAVE Aquatic Virtual Environment: Toward a General Underwater Robotics Simulator," in IEEE/OES Autonomous Underwater Vehicle (AUV) Symposium, 2022. doi: https://doi.org/10.1109/AUV53081.2022.9965808