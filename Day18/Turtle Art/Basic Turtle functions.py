# Importing functions from turtle module
from turtle import Turtle,Screen

tim_turtle=Turtle()
# setting tim_turtle to Turtle function

# Changing shape,color, and move the turtle using below commands
tim_turtle.shape("circle")
tim_turtle.color("red")
tim_turtle.forward(150)
tim_turtle.right(90)




# To make the screen to exit only click
screen=Screen()
screen.exitonclick()