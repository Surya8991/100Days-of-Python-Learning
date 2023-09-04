from turtle import Turtle,Screen
import time
tim=Turtle()
scr=Screen()
scr.setup(width=600,height=600)
scr.bgcolor("black")
scr.title("Welcome to Snake Game")
scr.tracer(0)
# Create a Snake body
segment_positions=[(0,0),(-20,0),(-40,0)]
all_segments=[]
for position in segment_positions:
    new_segment=Turtle('square')
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    all_segments.append(new_segment)

is_game_over=True

# To move the turtle
while is_game_over:
    # To turn off the animation and update after a delay
    scr.update()
    time.sleep(0.1)
    # To make sure 2nd and 3rd square follow the 1st one
    for seg_num in range(len(all_segments)-1,0,-1):
        new_x=all_segments[seg_num-1].xcor()
        new_y=all_segments[seg_num-1].ycor()
        all_segments[seg_num].goto(new_x,new_y)
    # Forwarding the 1st square by 20
    all_segments[0].forward(20)


        # if segment.xcor() > 290:
        #     print("You lost")
        #     is_game_over=False

scr.exitonclick()