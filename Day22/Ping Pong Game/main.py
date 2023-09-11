from turtle import Turtle, Screen
from paddle import Paddle

scr = Screen()
scr.setup(width=800, height=600)
scr.bgcolor("black")
scr.title("Ping Pong Game")
scr.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

scr.listen()
scr.onkey(r_paddle.go_up, "Up")
scr.onkey(r_paddle.go_down, "Down")
scr.onkey(l_paddle.go_up, "w")
scr.onkey(l_paddle.go_down, "s")
is_game_on = True
while is_game_on:
    scr.update()



scr.exitonclick()
