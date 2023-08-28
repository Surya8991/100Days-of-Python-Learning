# Create a dotted line
from turtle import Turtle,Screen

tim=Turtle()
# setting tim to Turtle function

# Using loops

for _ in range(4):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    tim.right(90)



# To make the screen to exit only click
screen=Screen()
screen.exitonclick()