from turtle import *
import math
import time
shape("turtle")
bgcolor("light blue")
color("red")
speed(0)

def polyline(n, length, angle):
    """Draws a line for a given length and turns for a given angle for a given number of times."""
    for _ in range(n):
        forward(length)
        left(angle)

def polygon(n, length):
    """Generalizes `polyline` to work for polygons."""
    angle = 360.0 / n
    polyline(n, length, angle)

def arc(radius, angle):
    """Uses `polyline` to draw rough approximations of circular sections."""
    arc_length = 2 * math.pi * radius * angle/360
    n = 30
    length =  arc_length / n
    step_angle = angle / n
    polyline(n, length, step_angle)

def circle(radius):
    """Uses `arc` to draw an approximate circle."""
    arc(radius, 360)

print ("CIS-12 Chapter 4 Exercises")

def pause(amount=2.0):
    """Pauses Python for a given number of seconds and then clears the Turtle screen."""
    time.sleep(amount) # pause python for 2 seconds
    clear()

def parallelogram0(length, height, int_angle):
    """
    Draws a quadrilateral with given length, height, and internal angles.
    This is the original version, which is unoptimized.
    """
    out_angle = 180 - int_angle
    for _ in range(2):
        forward(length)
        left(int_angle)
        forward(height)
        left(out_angle)

def parallelogram(length, height, int_angle):
    """Draws a quadrilateral with given length, height, and internal angles."""
    out_angle = 180 - int_angle
    for _ in range(2):
        for side, angle in {(length, int_angle), (height, out_angle)}:
            forward(side)
            left(angle)

print ("Exercise 1")

def rectangle(length, height, int_angle=90):
    """Uses `parallelogram` to draw a rectangle with fixed angles."""
    parallelogram(length, height, int_angle)

rectangle(80, 40)
pause()

print ("Exercise 2")

def rhombus(length, height, int_angle):
    """Uses `parallelogram` to draw a rhombus with given dimensions."""
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
    #print(f"{angle_base}")
    #print(f"{angle_vertex}")
    polyline(1, length=base, angle=angle_base) # base
    polyline(1, length=side, angle=angle_vertex) # right side
    polyline(1, length=side, angle=angle_base) # left side


iso_tri(75, 130)
pause()
#iso_tri(175, 65) # these values are not acceptable, see documentation
#pause()

def draw_pie(n, base, side):
    """Uses `iso_tri` to draw a 'pie' made of triangle segments."""
    for _ in range(n):
        iso_tri(base, side)
        polyline(1, length=base, angle=0)  # base
        left(360 / n)

draw_pie(5, 75, 80) # not quite right, but it'll do
draw_pie(7, 75, 80) # definitely not right
pause()

print ("Exercise 4")

def petal(radius, angle=90):
    """Uses `arc` to draw a pair of circular segments."""
    reverse_angle = 180 - angle
    for _ in range (2):
        arc(radius, angle)
        left(reverse_angle)

def flower(n, radius, p_angle=None):
    """Uses `petal` to draw a series of segment pairs."""
    rotate_offset = 360 / n
    p_angle = rotate_offset
    for _ in range(n):
        petal(radius, p_angle)
        left(rotate_offset)

petal(30, 60)
pause()
flower(8, 90)


time.sleep(10) # pause python for 10 seconds before exiting the program