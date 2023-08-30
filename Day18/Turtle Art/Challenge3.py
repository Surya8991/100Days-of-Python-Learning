# Draw different type of shape

from turtle import Turtle, Screen,colormode
import random

tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_of_sides):
    angle = 360/num_of_sides
    for _ in range(num_of_sides):
        tim.forward(10)
        tim.right(angle)
    for _ in range(num_of_sides):
        tim.forward(10)
        tim.left(angle)


for shape_side_n in range(3, 150):
    draw_shape(shape_side_n)
    tim.color(random.choices(colours))

scr = Screen()
scr.exitonclick()
