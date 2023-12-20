import random
import turtle
from turtle import Turtle, Screen
# import colorgram

tim = Turtle()
turtle.colormode(255)

# colors = colorgram.extract('./img/img.jpg', 30)
#
# colors_list = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     colors_list.append(new_color)
# print(colors_list)

colors = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99),
          (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64),
          (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77),
          (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90),
          (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]

tim.color(colors[0])
tim.up()
tim.speed(0)
tim.hideturtle()

y = -200
for _ in range(10):
    y += 50
    tim.teleport(-200, y)
    for position in range(10):
        tim.dot(20, random.choice(colors))
        tim.forward(50)

screen = Screen()
screen.exitonclick()
