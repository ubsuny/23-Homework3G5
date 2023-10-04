# Projectile Motion Simulation

This Python script simulates the motion of a projectile considering air resistance. It calculates and displays the horizontal distance traveled by the projectile before it hits the ground. The simulation accounts for gravity, air resistance, and user-defined initial conditions.

## Code Structure

### Constants
- `g`: Acceleration due to gravity (m/s^2).
- `k`: Air resistance constant (kg/s). Represents the drag on the projectile.
- `m`: Mass of the projectile (kg).

### Initial Conditions
- `x0, y0`: Initial position (m) of the projectile (default: (0.0, 0.0)).
- `v0`: Initial velocity (m/s) of the projectile.
- `theta`: Launch angle in radians.

### Calculations
- Calculates initial horizontal (`v0x`) and vertical (`v0y`) velocities.
- Defines time values for simulation from `0` to `t_max` seconds with a time step of `dt`.

### Functions
- `horizontal_motion(vx, t)`: Computes the horizontal velocity of the projectile at time `t`.
- `vertical_motion(vy, t)`: Computes the vertical velocity of the projectile at time `t`.

### Simulation
- Utilizes functional programming to update velocities over time.
- Finds the index when the projectile hits the ground (y = 0).
- Calculates the horizontal distance traveled when the projectile hits the ground.

### Output
- Prints the horizontal distance traveled by the projectile.

## Usage

To use this script, modify the initial conditions (e.g., `v0`, `theta`) as needed and run the script. The horizontal distance traveled will be displayed as output.

```python
# Example: Modify initial conditions
v0 = 100.0  # Initial velocity (m/s)
theta = np.radians(45)  # Launch angle in radians

# Run the simulation
# ...

# Output will show the horizontal distance traveled
```
**Output**

![Horizontal_Distance](image-1.png)
