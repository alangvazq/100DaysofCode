import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

tim.shape("turtle")
colors = ["orange", "yellow", "rosy brown", "navajo white", "dark cyan", "dodger blue", "yellow green"]


# for _ in range(10):
#     tim.down()
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)

# side = 2
# for _ in range(10):
#     side += 1
#     tim.color(random.choice(colors))
#     for _ in range(side):
#         tim.forward(100)
#         tim.right(360 / side)

# tim.speed(0)
# tim.pensize(5)
# direction = [0, 90, 180, 270]
#
# for _ in range(100):
#     tim.color(random.choice(colors))
#     tim.seth(random.choice(direction))
#     tim.forward(25)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_choice = (r, g, b)
    return random_choice


tim.speed(0)

for angle in range(0, 360, 2):
    tim.color(random_color())
    tim.circle(200)
    tim.seth(angle)








screen = Screen()
screen.exitonclick()
