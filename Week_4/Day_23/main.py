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

screen.listen()
screen.onkey(key="w", fun=turtle.move)


scoreboard = Scoreboard()


for item in range(0, 20):
    car = CarManager()
    cars.append(car)


scoreboard.score()


game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()

    for car in cars:
        car.move()
        if car.xcor() < -320:
            car.goto(300, random.randint(-240, 240))
    
    for car in cars:
        if turtle.distance(car) < 20:
            scoreboard.game()
            game_is_on = False

    if turtle.ycor() > 280:
        turtle.goto(0, -280)
        speed /= 2
        scoreboard.point()

screen.exitonclick()
