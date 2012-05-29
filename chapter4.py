from TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()


def square(t, x):
    for i in range(4):
        fd(t, x)
	lt(t)

def polygon(t, x, n):
    theta = 360.0 / n
    for i in range(n):
        fd(t, x)
	lt(t, theta)

def circle(t, r):
    x = 2*math.pi*r
    x = x / 360
    pu(t)
    fd(t,r)
    lt(t)
    pd(t)
    for i in range(360):
        fd(t, x)
	lt(t, 1)

john = Turtle()
tom = Turtle()


bob.delay = 0.1
john.delay = 0.1
tom.delay = 0.01


square(bob, 100)
polygon(john, 50, 5)
circle(tom, 150)

wait_for_user()
