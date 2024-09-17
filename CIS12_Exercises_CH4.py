from turtle import *
import math

# make_turtle() not required

def polyline(n, length, angle):
    for x in range(n):
        forward(length)
        left(angle)

def polygon(n, length):
    angle = 360.0 / n
    polyline(n, length, angle)

def arc(radius, angle):
    arc_length = 2 * math.pi * radius * angle/360
    n = 30
    length =  arc_length / n
    step_angle = angle / n
    polyline(n, length, step_angle)

def circle(radius):
    turtle_delay = 0
    arc(radius, 360)

print ("CIS-12 Chapter 4 Exercises")

def cont_conf(message):
    confirm = input(f"""{message}
""").strip().upper()
    return

def cont():
    if cont_conf("Press any key to continue: "):
        return

print ("Exercise 1")




cont()



input("Press any key to exit the program: ") # this prevents the program from immediately exiting