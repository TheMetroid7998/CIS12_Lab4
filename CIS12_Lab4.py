from turtle import *
import math
import time
shape("turtle")
bgcolor("light blue")
color("red")
speed(0)

def pause(amount=2.0):
    time.sleep(amount) # pause python for 2 seconds
    clear()

def draw_square(length):
    """Draws a square with the given side length."""
    for _ in range(4):
        forward(length)
        left(90)

def draw_circle(radius):
    """Draws a circle with the given radius."""
    circle(radius)

draw_square(100)
pause()
draw_circle(50)
pause()

print(math.pi*2)