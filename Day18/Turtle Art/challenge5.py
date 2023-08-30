
import turtle as t
from turtle import Screen,colormode
import random

tim = t.Turtle()
tim.speed(speed=100)

# To generate Random colors
t.colormode(255)
def rand_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color

# To draw cirlce
def draw_spirograpph(num_sides):
    for _ in range(num_sides):
        tim.circle(100)
        tim.right(5)

# To specify no. of circles
for shape_no in range(13):
    draw_spirograpph(shape_no)
    tim.color(rand_color())


scr=Screen()
scr.exitonclick()