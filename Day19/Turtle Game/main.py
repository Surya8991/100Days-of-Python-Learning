from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500,height=600)

user_bet=screen.textinput(title="Make your bet",prompt="Enter the color of turtle who will win ?")
print("User Turtle color bet",user_bet)
colors=["red","orange","yellow","green","blue","Indigo","violet"]
is_race_on=False
all_turtles=[]

if user_bet:
    is_race_on=True

y_positions=[-70,-40,-10,20,50,80]
for turtle_index in range(0,6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >230:
            winner_color=turtle.pencolor()
            is_race_on=False
            if winner_color == user_bet:
                print("You have won")
            else:
                print(f"You have lost the winning color of Turtle is {winner_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()

# Alertnative method to create turtle and position them
# def create_turtle():
#     turtles=[]
#     y_position=-100
#     for colour in colors:
#         tim = Turtle(shape="turtle")
#         tim.color(colour)
#         tim.penup()
#         tim.goto(x=-230,y=y_position)
#         turtles.append(tim)
#         y_position+=30
#     return turtles
#
# turtles=create_turtle()
# print(turtles)


