import colorgram

rgb_colors = []
colors = colorgram.extract("image.jpg",10)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))

import turtle as t
from turtle import Turtle, Screen
import random
t.colormode(255)


brush = Turtle()
brush.hideturtle()
brush.pensize(10)
# ** USE THIS LINE IF YOU CANNOT USE THE "colorgram" LIBRARY
# colors = [(217, 226, 220), (195, 172, 122), (221, 226, 232), (159, 100, 58), (186, 161, 51), (126, 37, 25), (8, 54, 78)]
brush.penup()
brush.setheading(180)
brush.forward(200)
brush.setheading(270)
brush.forward(100)
brush.setheading(0)

for i in range(11):
    for j in range (11):
        brush.color(random.choice(rgb_colors))
        brush.forward(30)
        brush.dot()
    brush.left(90)
    brush.forward(30)
    brush.left(90)
    brush.forward(330)
    brush.left(180)



screen = Screen()
screen.exitonclick()