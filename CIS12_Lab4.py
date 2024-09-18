from turtle import *
import time
import random
shape("turtle")
bgcolor("light blue")
color("red")
speed(0)

def pause(amount=2.0):
    time.sleep(amount) # pause python for 2 seconds
    clear()

def jump(x, y):
    """Moves the turtle cursor."""
    penup()
    goto(x, y)
    pendown()

def draw_square(length):
    """Draws a square with the given side length."""
    for _ in range(4):
        forward(length)
        left(90)

def draw_circle(radius):
    """Draws a circle with the given radius."""
    circle(radius)

def draw_polygon(side, length):
    """Draws any regular polygon with given number of sides."""
    angle = 360 / side
    for _ in range(side):
        forward(length)
        left(angle)

def draw_pumpkin(x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    jump(x,y)
    fillcolor("orange")
    begin_fill()
    circle(radius)
    end_fill()
    jump(x+radius*0.5, y+radius*2)
    fillcolor("green")
    begin_fill()
    for _ in range(4):
        left(90)
        for x in range(2, 5):
            forward(radius // x)
    end_fill()

def draw_eye(x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    jump(x-15, y+10)
    fillcolor("yellow")
    begin_fill()
    draw_polygon(3, size)
    end_fill()

def draw_mouth(x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    jump(x, y+20)
    fillcolor("yellow")
    begin_fill()
    right(60)
    for _ in range(5):
        forward(width // 5)
        left(120)
        forward(width // 5)
        right(120)
    left(240)
    forward(width)
    end_fill()

#draw_pumpkin(0,-100, 100)
#draw_eye(40, 0, 30)
#draw_eye(-40, 0, 30)
#draw_mouth(-50, -50, 100)
#pause()

def draw_star(x, y, size):
    """Draws a star at the given (x, y) position."""
    jump(x, y)
    fillcolor("white")
    begin_fill()
    for _ in range(5):
        forward(size)
        right(144)
    end_fill()

#draw_star(-100, 150, 30)
#draw_star(100, 150, 20)
#pause()

def draw_sky(n):
    """Draws a starry sky with the given number of stars."""
    for _ in range(n):
        x = random.randint(-300, -220)
        y = random.randint(0, 300)
        size = random.randint(10, 30)
        draw_star(x, y, size)

#draw_sky(30)
#pause()

draw_pumpkin(-180, -250, 100)
draw_eye(-220, -160, 30)
draw_eye(-140, -160, 30)
draw_mouth(-220, -200, 80)

draw_pumpkin(0, -150, 40)
draw_eye(0, -190, 7)
draw_eye(35, -190, 7)
draw_mouth(20, -220, 25)

draw_pumpkin(170, -250, 100)
draw_eye(130, -160, 30)
draw_eye(210, -160, 30)
draw_mouth(130, -200, 80)

draw_sky(30)
pause(30)