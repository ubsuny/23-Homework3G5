# Projectile Motion with Air Drag:

## Objective:
The program aims to replicate projectile motion with air drag. It calculates and then illustrates the trajectories for various launch angles.

## Dependencies:
1. math: This standard Python library offers a set of mathematical functions.
1. matplotlib.pyplot: A plotting library to visualize the trajectories.

## Constants and Initial Values:

- g: Acceleration due to gravity. Default is 9.81 m/s^2.
- dt: Time interval for each calculation step. Default is 0.5 seconds.
- x_start, y_start: Initial positions of the projectile. Both are set to 0 as the starting point.
- const: Quadratic drag coefficient for the air drag. Default value is 4*(10**-5) 1/m.
- v_initial: Initial launch velocity of the projectile. Default value is 700 m/s.
- angle_degree: A list of desired launch angles in degrees.
- angle: Converted list of launch angles in radians.

# Computations:

1. Conversion of angles:
```python
angle = [math.radians(degrees) for degrees in angle_degree]
```
Each launch angle in degrees is converted to radians.

2. Main Trajectory Calculation Loop:
Iterates over each launch angle to calculate the corresponding trajectory. Inside this loop:

- Initial velocity components are determined based on the launch angle.
- A nested loop calculates the trajectory until the projectile hits the ground.
- Projectile's positions are updated at each time step.
- Velocities are adjusted at each step considering gravity and air drag.
- Interpolation is performed to determine the exact landing position of the projectile.
