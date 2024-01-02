import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

cars = []
speed = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()

for item in range(0, 20):
    car = CarManager()
    cars.append(car)


scoreboard.score()
screen.listen()
screen.onkey(key="w", fun=turtle.move)

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()

    for car in cars:
        car.move()
        if car.xcor() < -280:
            car.goto(280, random.randint(-240, 240))
        elif turtle.distance(car) < 10:
            game_is_on = False

    if turtle.ycor() > 280:
        turtle.goto(0, -280)
        speed /= 2
        scoreboard.point()


