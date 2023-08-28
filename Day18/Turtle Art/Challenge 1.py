# Draw a square from turle module

# Importing functions from turtle module
from turtle import Turtle,Screen

tim_turtle=Turtle()
# setting tim_turtle to Turtle function

# Changing shape,color, and move the turtle using below commands
tim_turtle.shape("turtle")
tim_turtle.color("red")

# easy version without loops

# tim_turtle.forward(100)
# tim_turtle.right(90)
# tim_turtle.forward(100)
# tim_turtle.right(90)
# tim_turtle.forward(100)
# tim_turtle.right(90)
# tim_turtle.forward(100)
# tim_turtle.right(90)


# Using loops
i=0
while i <4:
    tim_turtle.forward(100)
    tim_turtle.right(90)
    i+=1



# To make the screen to exit only click
screen=Screen()
screen.exitonclick()