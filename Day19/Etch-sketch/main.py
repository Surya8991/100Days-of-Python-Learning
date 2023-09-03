from turtle import Turtle, Screen

tim = Turtle()
scr = Screen()

def move_turtle():
    tim.forward(100)

def move_backward():
    tim.backward(100)
def turn_turtle_right():
    tim.right(45)
    tim.heading()

def turn_turtle_left():
    tim.left(45)
    tim.heading()

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

scr.listen()
scr.onkeypress(move_turtle,"w")
scr.onkeypress(move_backward,"s")
scr.onkeypress(turn_turtle_right,"d")
scr.onkeypress(turn_turtle_left,"a")
scr.onkey(clear,"c")
scr.exitonclick()
