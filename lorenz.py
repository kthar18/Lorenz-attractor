import numpy as np
import matplotlib.pyplot as plt

#lorenz perameters
sigma = 10
rho = 30
beta = 8/3

#initial conditions
x,y,z = 1,1,1
dt=0.01

#secondary conditions
x2,y2,z2 = 1,1,1.5
dt = 0.01


#storage lists
xs, ys, zs = [], [], []

#storage lists
xs2, ys2, zs2 = [], [], []

#Euler's method for the lorenz system
for i in range(10000):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z

    x = x + dx * dt
    y = y + dy * dt
    z = z + dz * dt

    xs.append(x)
    ys.append(y)
    zs.append(z)

for i in range(10000):
    dx2 = sigma * (y2 - x2)
    dy2 = x2 * (rho - z2) - y2
    dz2 = x2 * y2 - beta * z2

    x2 = x2 + dx2 * dt
    y2 = y2 + dy2 * dt
    z2 = z2 + dz2 * dt

    xs2.append(x2)
    ys2.append(y2)
    zs2.append(z2)

#plotting the lorenz attractor
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, ys, zs, lw=0.5, color='blue')
ax.plot(xs2, ys2, zs2, lw=0.5, color='green')
ax.set_title("Lorenz Attractor")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
