# Draw different type of shape

from turtle import Turtle, Screen,colormode
import random

tim = Turtle()

tim.speed(speed=100)
tim.pensize(15)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction=[0,90,180,270,360]

def random_walk(num_walks):
    for _ in range(num_walks):
        tim.forward(30)
        tim.right(random.choice(direction))

for walk_tim in range(3, 200):
    random_walk(walk_tim)
    tim.color(random.choices(colours))

scr = Screen()
scr.exitonclick()
