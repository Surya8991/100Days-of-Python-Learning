from turtle import Turtle,Screen

tim=Turtle()
scr=Screen()
def move_turtle():
    tim.forward(10)



scr.listen()
scr.onkey(key="space",fun=move_turtle)
scr.exitonclick()