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

#rectangle(80, 40)
#pause()

print ("Exercise 2")

def rhombus(length, height, int_angle):
    """Uses `parallelogram` to draw a rhombus with given dimensions."""
    parallelogram(length, height, int_angle)

#rhombus(50, 80, 60)
#pause()

print ("Exercise 3")

def iso_tri(side, int_angle):
    """Draws an isosceles triangle with given base and side values."""
    ext_angle = 180 - int_angle
    vtx_angle = 180 - 2 * int_angle
    fin_angle = 180
    base = 2*side*math.sin(math.radians(vtx_angle/2))
    polyline(n=1, length=side, angle=ext_angle) # line out
    polyline(n=1, length=base, angle=ext_angle)  # base
    polyline(n=1, length=side, angle=fin_angle)  # line in, around

#iso_tri(75, 66)
#pause()

def draw_pie(n, side):
    """Uses `iso_tri` to draw a 'pie' made of triangle segments. Moves counter-clockwise."""
    int_angle = (180 - (360 / n)) / 2
    for _ in range(n):
        iso_tri(side, int_angle)

draw_pie(5, 75)
pause()
draw_pie(6, 75)
pause()
draw_pie(7, 75)
pause()
draw_pie(9, 75)
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