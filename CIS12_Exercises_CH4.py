from turtle import *
import math
import time
shape("turtle")
bgcolor("light blue")
color("red")

def polyline(n, length, angle):
    for _ in range(n):
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
    arc(radius, 360)

print ("CIS-12 Chapter 4 Exercises")

def pause(amount=2.0):
    time.sleep(amount) # pause python for 2 seconds
    clear()

def parallelogram0(length, height, int_angle):
    out_angle = 180 - int_angle
    for _ in range(2):
        forward(length)
        left(int_angle)
        forward(height)
        left(out_angle)

def parallelogram(length, height, int_angle):
    out_angle = 180 - int_angle
    for _ in range(2):
        for side, angle in {(length, int_angle), (height, out_angle)}:
            forward(side)
            left(angle)

print ("Exercise 1")

def rectangle(length, height, int_angle=90):
    parallelogram(length, height, int_angle)

rectangle(80, 40)
pause()

print ("Exercise 2")

def rhombus(length, height, int_angle):
    parallelogram(length, height, int_angle)

rhombus(50, 80, 60)
pause()

print ("Exercise 3")

def iso_tri(base, side):
    """
    Draws an isosceles triangle with given base and side values.
    Does not accept certain values due to correction method used.
    (The calculated angle is subtracted from 180 to create the correct angle,
    but this creates a negative number for calculated angles less than 180.)
    """
    angle_base = 180 - math.degrees(math.acos((base**2)/(2*side*base)))
    angle_vertex = 180 - math.degrees(math.acos((2*(side**2)-(base**2))/(2*(side**2))))
    print(f"{angle_base}")
    print(f"{angle_vertex}")
    polyline(1, length=base, angle=angle_base) # base
    polyline(1, length=side, angle=angle_vertex) # right side
    polyline(1, length=side, angle=angle_base) # left side


iso_tri(75, 130)
pause()
#iso_tri(175, 65) # these values are not acceptable, see documentation
#pause()

def draw_pie(n, base, side):
    for _ in range(n):
        iso_tri(base, side)
        polyline(1, length=base, angle=0)  # base
        left(360 / n)

draw_pie(5, 75, 80) # not quite right, but it'll do
pause()

print ("Exercise 4")

def petal(radius, angle=90):
    speed(0)
    reverse_angle = 180 - angle
    for _ in range (2):
        arc(radius, angle)
        left(reverse_angle)

def flower(n, radius, p_angle=None):
    rotate_offset = 360 / n
    p_angle = rotate_offset
    for _ in range(n):
        petal(radius, p_angle)
        left(rotate_offset)

petal(30, 60)
pause()
flower(8, 90)


time.sleep(10) # pause python for 10 seconds before exiting the program