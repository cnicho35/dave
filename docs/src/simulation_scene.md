# Understand the Simulation Scene

The tidal-energy scenario is named `marine_energy_tidal`. It combines a simulated underwater setting with a BlueROV2 and a TEC assembly to support navigation and inspection practice.

## Main Elements

- **BlueROV2:** The remotely operated vehicle spawned in the `bluerov2` ROS 2 namespace.
- **TEC assembly:** Three marine-energy models named `Base`, `Blades`, and `Nacelle` are placed together to form the turbine.
- **Gazebo:** The physics and visual simulation environment.
- **RViz:** A ROS 2 visualization application launched with the underwater-camera configuration.
- **Doppler Velocity Log (DVL):** The world loads a Gazebo DVL system for velocity-related sensing support.
- **Buoyancy:** The world loads Gazebo buoyancy with a seawater-density default of 1025 kg/m3.

## Frame And Environment Context

The world includes a North-East-Down (NED) frame model. NED is a common navigation convention in which the axes describe north, east, and down rather than the usual up-positive vertical direction. The scene also includes a coastal-water model and a sand heightmap positioned near 15 m below the world origin.

The world references models hosted on Gazebo Fuel. An internet connection may therefore be needed when assets are first downloaded; later launches can reuse cached assets.

## Use The Scene Deliberately

Use Gazebo to understand the ROV and turbine position in the overall environment. Use RViz to work from the simulated camera view. Before changing poses or models, complete the baseline activity so changes can be compared with a known working scenario.

Continue with [Operate the BlueROV](marine_energy_world.md) or learn to [Customize a Scenario](customize_scenario.md).