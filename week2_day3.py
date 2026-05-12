import numpy as np
import matplotlib.pyplot as plt

# Initial conditions
t = 0
y = 0      # position (meters)
v = 0      # velocity (m/s)
dt = 0.01  # time step
g = 9.8    # gravity

# Storage lists
times = []
positions = []

# Euler's method
while t < 3:
    v = v + g * dt
    y = y + v * dt
    t = t + dt
    times.append(t)
    positions.append(y)

plt.plot(times, positions)
plt.title("Falling ball - Euler's method")
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.grid(True)
plt.show()