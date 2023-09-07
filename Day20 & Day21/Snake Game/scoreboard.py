from turtle import Turtle
ALLIGN="center"
FONT=("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        # Hide turtle is used to hide arrow or turtle slector
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)  # Use goto() instead of position()

    def update_score(self):
        self.clear()
        self.write("Score : {}".format(self.score), align=ALLIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(x=0,y=0)
        self.color("red")
        self.write("Game Over", align=ALLIGN, font=("Arial", 30, "normal"))