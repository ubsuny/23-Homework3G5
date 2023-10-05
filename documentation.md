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

1. **Conversion of angles:**
```python
angle = [math.radians(degrees) for degrees in angle_degree]
```
Each launch angle in degrees is converted to radians.

2. **Main Trajectory Calculation Loop:**
Iterates over each launch angle to calculate the corresponding trajectory. Inside this loop:

- Initial velocity components are determined based on the launch angle.
- A nested loop calculates the trajectory until the projectile hits the ground.
- Projectile's positions are updated at each time step.
- Velocities are adjusted at each step considering gravity and air drag.
- Interpolation is performed to determine the exact landing position of the projectile.

**Looping Over Launch Angles:**
```python
for j in range(len(angle)):
```
This loop serves as a mechanism to study the trajectory of a projectile for various launch angles. By iterating over each launch angle, the code computes trajectories that help in visualizing how different angles affect the projectile's path.

**Initial Velocity Components:**
```python
vx = v_initial*math.cos(angle[j])
vy = v_initial*math.sin(angle[j])
```
Given the initial speed of the projectile and the launch angle, these lines determine the horizontal (vx) and vertical (vy) components of the velocity using trigonometric functions. Essentially, this breaks down the launch speed into how much of it pushes the projectile forward and how much lifts it upward.

**Nested Loop for Trajectory Calculation:**
```python
while y[-1]>=0:
```
This loop's condition ensures that the calculations continue as long as the projectile is above the ground (y[-1] being the latest y-position). Within this loop, we compute the projectile's path over time.

- Position Update:
```python
x.append(x[i]+vx*dt)
y.append(y[i]+vy*dt)
```
These lines update the projectile's horizontal (x) and vertical (y) positions based on their respective velocities. The dt represents the time step, which in essence is a measure of how much time we "move forward" with each iteration.

- Velocity Update (Including Air Drag):
```python
vx = vx - const*dt*vx*math.sqrt((vx**2)+(vy**2))
vy = vy - dt*(g + const*vy*math.sqrt((vx**2)+(vy**2)))
```
This part of the code updates the velocities considering two forces: gravitational acceleration and air drag. The gravitational force acts downward, which is why we subtract g from the vertical velocity vy. The air drag acts against the direction of motion and is dependent on the projectile's speed, hence the use of sqrt((vx**2)+(vy**2)) which calculates the resultant speed. The const value represents the drag coefficient.

**Interpolation for Accurate Landing Position:**
```python
r = -y[-2]/y[-1]
x[-1] = (x[-2]+r*x[-1])/(r+1)
y[-1] = 0.0
```
When the projectile is close to the ground, the time step might be too large to accurately determine the exact landing position. The lines above use linear interpolation between the last two known points to pinpoint a more accurate landing position on the x-axis.

# Visualization:
The code visualizes the trajectories using a scatter plot. Different trajectories are distinguished using unique colors. 

![Projectile_motion_with_air_drag](projectile_motion_with_air_drag.png)



