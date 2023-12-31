from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time
scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Welcome to Snake Game")
scr.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.update_score()
is_game_over = True

# To control the snake
scr.listen()
scr.onkey(key="Up", fun=snake.up)
scr.onkey(key="Down", fun=snake.down)
scr.onkey(key="Left", fun=snake.left)
scr.onkey(key="Right", fun=snake.right)
# To move the turtle
while is_game_over:
    # To turn off the animation and update after a delay
    scr.update()
    time.sleep(0.1)
    snake.move()
    # Detect Food Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        # Increasing the length of the snake by 1
        snake.extend()
    # Detect Collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -295
        or snake.head.ycor() > 295
        or snake.head.ycor() < -280
    ):
        scoreboard.game_over()
        is_game_over = False
 # Detect collision with tail.
    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            is_game_over = False


scr.exitonclick()
