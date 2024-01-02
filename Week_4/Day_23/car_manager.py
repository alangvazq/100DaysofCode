from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
cars = []

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.seth(180)
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.goto(random.randint(280, 1000), random.randint(-240, 240))



    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def more_cars(self):
        CarManager()
        self.move()

