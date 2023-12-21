from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.shapesize(stretch_wid=40, stretch_len=40)
        self.count = 0
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.count}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Arial", 15, "normal"))

    def print(self):
        self.count += 1
        self.clear()
        self.update_score()



