from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.shapesize(stretch_wid=40, stretch_len=40)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.count} High Score: {self.high_score}", align="center",
                   font=("Arial", 15, "normal"))

    def reset(self):
        if self.count > self.high_score:
            self.high_score = self.count
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.count = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align="center", font=("Arial", 15, "normal"))

    def print(self):
        self.count += 1
        self.update_score()
