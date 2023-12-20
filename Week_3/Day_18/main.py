import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

tim.shape("turtle")
colors = ["orange", "yellow", "rosy brown", "navajo white", "dark cyan", "dodger blue", "yellow green"]


# for _ in range(10):
#     new_turtle.down()
#     new_turtle.forward(10)
#     new_turtle.up()
#     new_turtle.forward(10)

# side = 2
# for _ in range(10):
#     side += 1
#     new_turtle.color(random.choice(colors))
#     for _ in range(side):
#         new_turtle.forward(100)
#         new_turtle.right(360 / side)

# new_turtle.speed(0)
# new_turtle.pensize(5)
# direction = [0, 90, 180, 270]
#
# for _ in range(100):
#     new_turtle.color(random.choice(colors))
#     new_turtle.seth(random.choice(direction))
#     new_turtle.forward(25)

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
