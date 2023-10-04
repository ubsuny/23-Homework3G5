import numpy as np

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
k = 0.1   # Air resistance constant (kg/s)
m = 1.0   # Mass of the projectile (kg)

# Initial conditions
x0, y0 = 0.0, 0.0  # Initial position (m)
v0 = 100.0         # Initial velocity (m/s)
theta = np.radians(45)  # Launch angle in radians

# Calculate initial horizontal and vertical velocities
v0x = v0 * np.cos(theta)
v0y = v0 * np.sin(theta)

# Time values
t_max = 20  # Maximum simulation time (s)
dt = 0.01   # Time step (s)
t_values = np.arange(0, t_max, dt)

# Define functions for horizontal and vertical motion
def horizontal_motion(vx, t):
    return vx - (k/m) * vx * t

def vertical_motion(vy, t):
    return vy - g * t - (k/m) * vy * t

# Use functional programming to update velocities over time
vx_values = np.array(list(map(lambda t: x0 + v0x * t, t_values)))
vy_values = np.array(list(map(lambda t: y0 + v0y * t - 0.5 * g * t**2, t_values)))

# Find the index when the projectile hits the ground (y = 0)
ground_index = np.argmax(vy_values < 0)

# Calculate the horizontal distance traveled
x_final = vx_values[ground_index]

print(f"Horizontal distance traveled: {x_final:.2f} meters")

