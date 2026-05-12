# Lorenz-attractor and chaos theory 

## What is this?
A Lorenz attractor is a mathematical model that creates a 3D shape in the form of a butterfly. The lines that create the form are made up of 3 differential equations that model atmospheric convection.

## Background
The Lorenz equation is a mathematical model that is used to model the unpredictability of meteorological patterns. The three equations are:
x = rate of convection (how fast warm air rises)
y = horizontal temperature difference
z = vertical temperature difference
The variables don't represent position in space but rather represent the state of a simplified weather system. dx,dy, and dz represent the instantaneous rate of change of each variable, while the parameters sigma, rho, and beta represent how each of the variables influences the others. 

## How it works
A derivative is the instantaneous rate of change at a point. Euler's method says that if you know the rate of change at one point, you can approximate where the system will be a short time in the future. You can do this by multiplying the rate by the time step and adding it. Doing this thousands of times will give you a trace of the full trajectory. It works because for a small enough dt, "instantaneous" and "tiny slice of time" are nearly the same thing.

## Results
The plot shows two lines that start nearly at the same point but trace completely different paths while staying in the same beautiful butterfly shape. The start parameters are the same except for a difference of 0.01 in the z-axis. This proves chaos because this small change produces 2 completely different trajectories, something that wouldn't happen in a non-chaotic system. 

## What I learned
Going into this, I knew nothing about this topic or even how to code. Through online tutorials and help from peers, I was able to create something that I think is really cool and beautiful to look at. I also like learning about chaos theory and plan to try to make a double pendulum simulator. Through this project, I learned the basics of code, how to do research, and what to do when I face challenges. 

## Files
- `lorenz.py` — main Lorenz attractor simulation with butterfly effect visualization
- `week2_day3.py` — Euler's method applied to a falling ball (simpler ODE)
- `week2_day2.py` — numerical vs analytical derivative comparison
- `day6.py` — numerical differentiation from scratch

  

