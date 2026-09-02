# Customize a Scenario

After completing the baseline scenario, you can explore controlled changes to the placement of marine-energy models.

## How Model Placement Works

The `marine_energy_models` package provides `upload_object.launch.py`. It creates a model from a matching subdirectory in `description/` and accepts these launch arguments:

- `model_name`: A model directory such as `Base`, `Blades`, or `Nacelle`.
- `x`, `y`, `z`: Initial position.
- `roll`, `pitch`, `yaw`: Initial orientation.
- `use_ned_frame`: Whether to create the `world` to `world_ned` static transform.

The baseline tidal launch places each TEC component at `x=15`, `y=0`, `z=-15`, `roll=1.5708`, `pitch=0`, and `yaw=1.5708`.

## Start With A Bounded Change

1. Copy the tidal launch file to a clearly named local variant.
2. Change one position or orientation value for one component.
3. Build and source the workspace.
4. Launch the variant and compare the result with the baseline in Gazebo.
5. Record the changed value and the visible effect.

Do not overwrite the baseline launch while learning. A small, documented change makes it easy to reset to a known scenario and understand which parameter caused an effect.

Use [Understand the Simulation Scene](simulation_scene.md) to review frame and environment context before making changes.