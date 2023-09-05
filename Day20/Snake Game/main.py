from turtle import Turtle,Screen
from snake import Snake
import time
scr=Screen()
scr.setup(width=600,height=600)
scr.bgcolor("black")
scr.title("Welcome to Snake Game")
scr.tracer(0)

snake=Snake()

is_game_over=False

# To control the snake
scr.listen()
scr.onkey(key="Up",fun=snake.up)
scr.onkey(key="Down",fun=snake.down)
scr.onkey(key="Left",fun=snake.left)
scr.onkey(key="Right",fun=snake.right)
# To move the turtle
while not is_game_over:
    # To turn off the animation and update after a delay
    scr.update()
    time.sleep(0.1)
    snake.move()

        # if segment.xcor() > 290:
        #     print("You lost")
        #     is_game_over=False

scr.exitonclick()