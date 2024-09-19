from turtle import *
import time
import random
shape("turtle")
bgcolor("dark blue")
color("red")
hideturtle()
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
    jump(x,y) # draws pumpkin
    print(f"Pumpkin Coordinates: x:{x}, y:{y}, radius:{radius}.")
    fillcolor("orange")
    begin_fill()
    circle(radius)
    end_fill()
    jump(x+radius*0.1, y+radius*2) # draws stem
    print(f"Stem Coordinates: x:{x+radius*0.1}, y:{y+radius*2}")
    fillcolor("green")
    begin_fill()
    for _ in range(2):
        for s in (2, 5):
            left(90)
            forward(radius // s)
    end_fill()

def draw_eye(x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    jump(x-size//2, y+size//3)
    print(f"Eye Coordinates: x:{x-size//2}, y:{y+size//3}, size:{size}.")
    fillcolor("yellow")
    begin_fill()
    draw_polygon(3, size)
    end_fill()

def draw_mouth(x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    jump(x-(width*0.05), y+(width*0.2))
    print(f"Mouth Coordinates: x:{x-(width*0.05)}, y: {y+(width*0.2)}, width:{width}.")
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
    right(180)
    end_fill()

def draw_jack(x, y, radius):
    draw_pumpkin(x, y, radius)
    draw_eye(x-radius*0.365, y+radius*1.07, radius // 3)
    draw_eye(x+radius*0.365, y+radius*1.07, radius // 3)
    draw_mouth(x-radius*0.365, y+radius*0.5, radius*0.8)
    jump(x, y)
    print("""
""")

def draw_star(x, y, size):
    """Draws a star at the given (x, y) position."""
    jump(x, y)
    fillcolor("white")
    begin_fill()
    for _ in range(5):
        forward(size)
        right(144)
    end_fill()

def draw_section(n, xx, yx, xy, yy):
    """Draws a section of a starry sky with the given number of stars."""
    for _ in range(n):
        x = random.randint(xx, yx)
        y = random.randint(xy, yy)
        size = random.randint(10, 30)
        draw_star(x, y, size)

def draw_sky(n):
    """Draws a starry sky in sections with the given number of stars as reference."""
    draw_section(n // 5, -300, -220, 0, 300)
    draw_section(n // 6, -220, -120, 70, 300)
    draw_section(n // 3, -120, 120, -30, 300)
    draw_section(n // 6, 120, 220, 70, 300)
    draw_section(n // 5, 220, 300, 0, 300)

draw_jack(x=-180, y=-250, radius=100)

draw_jack(x=0, y=-150, radius=50)

draw_jack(x=170, y=-250, radius=100)

draw_sky(30)
pause(20)