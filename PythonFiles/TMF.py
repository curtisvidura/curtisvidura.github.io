#C:\Users\User\OneDrive - Chulalongkorn University\Documents\GitHub\curtisvidura.github.io\PythonFiles

import numpy as np
import matplotlib.pyplot as plt
import turtle

wn = turtle.Screen()
wn.title("electron in a magnetic field")
turtle.screensize(canvwidth=1000, canvheight=1000)


e = turtle.Turtle()
e.shape("circle")
e.color("yellow")
e.penup()
e.speed(0)
e.goto(0,200)

steps = 10

m = 1
q = 1
r0 = 0
v0 = 0

dt = 1e-1       # Time step
num_steps = 100 # Number of time steps to simulate


# Initial conditions
r = np.zeros((num_steps, 3))
v = np.zeros((num_steps, 3))
a = np.zeros((num_steps, 3))

# Set initial position and velocity
r[0] = r0
v[0] = v0

# Electric field function (in V/m)
E = 0

# Magnetic field function (in T)
def B(x, y, z):
    return np.array([0, 0, 1])

# Run simulation

for i in range(1, num_steps):
    a[i] = (q/m) * (E + np.cross(v[i-1], B(*r[i-1])))

    # Update position using Taylor series expansion
    r[i] = r[i-1] + v[i-1]*dt + 0.5*a[i-1]*dt**2

    # Update velocity using central difference approximation
    v[i] = v[i-1] + 0.5*(a[i] + a[i-1])*dt

    if np.isnan(r[i]).any() or np.isinf(r[i]).any() or np.isnan(v[i]).any() or np.isinf(v[i]).any() or np.isnan(a[i]).any() or np.isinf(a[i]).any():
        print("Particle's position, velocity, or acceleration is NaN or Inf. Stopping simulation.")
        break

    print(i)
    print(a)

    # e.setx(r[0])
    # e.sety(r[1])


    # if ball.ycor() < -300 or ball.ycor() > 300:
    #     ball.dy *= -1 
    # if ball.xcor() < -300 or ball.xcor() > 300:
    #     ball.dx *= -1