import numpy as np

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
k = 0.1   # Air resistance constant (kg/s). Represents the drag on the projectile.
m = 1.0   # Mass of the projectile (kg)

# Initial conditions
x0, y0 = 0.0, 0.0  # Initial position (m). Projectile starts at the origin.
v0 = 100.0         # Initial velocity (m/s). Initial speed of the projectile upon launch.
theta = np.radians(45)  # Launch angle in radians. Converts 45 degrees to radians.

# Calculate initial horizontal and vertical velocities
v0x = v0 * np.cos(theta)  # Horizontal component of velocity
v0y = v0 * np.sin(theta)  # Vertical component of velocity

# Time values
t_max = 20  # Maximum simulation time (s). This is the upper limit for the simulation.
dt = 0.01   # Time step (s). Increment for each step in the simulation.
t_values = np.arange(0, t_max, dt)  # Array of time values for the simulation.

def horizontal_motion(vx, t):
    """Compute the horizontal velocity of the projectile at time t.
    
    Args:
    - vx (float): Initial horizontal velocity.
    - t (float): Time elapsed since launch.
    
    Returns:
    - float: Horizontal velocity at time t considering air resistance.
    """
    return vx - (k/m) * vx * t

def vertical_motion(vy, t):
    """Compute the vertical velocity of the projectile at time t.
    
    Args:
    - vy (float): Initial vertical velocity.
    - t (float): Time elapsed since launch.
    
    Returns:
    - float: Vertical velocity at time t considering gravity and air resistance.
    """
    return vy - g * t - (k/m) * vy * t

# Use functional programming to update velocities over time
# Note: These formulas are approximations as they don't account for the changing velocities due to air resistance.
vx_values = np.array(list(map(lambda t: x0 + v0x * t, t_values)))  # Horizontal displacements over time.
vy_values = np.array(list(map(lambda t: y0 + v0y * t - 0.5 * g * t**2, t_values)))  # Vertical displacements over time.

# Find the index when the projectile hits the ground (y = 0)
ground_index = np.argmax(vy_values < 0)

# Calculate the horizontal distance traveled when the projectile hits the ground
x_final = vx_values[ground_index]

print(f"Horizontal distance traveled: {x_final:.2f} meters")

