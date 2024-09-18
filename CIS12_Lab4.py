import math
import time
from turtle import *
speed(10) # speed is set to fast
#hideturtle() # hide the turtle object
screen = Screen() # create a window to draw in
screen.bgcolor("light blue") # set the background color of the screen
screen.setup(width=600, height=600) # set the dimensions of the screen
color("red")
shape("turtle")

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
draw_circle(50)

print(math.pi*2)