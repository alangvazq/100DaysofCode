from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.count = 0
        self.goto(x=-200, y=250)

    def score(self):
        self.clear()
        self.write(f"Score: {self.count}", align="center", font=FONT)

    def point(self):
        self.count += 1
        self.score()
