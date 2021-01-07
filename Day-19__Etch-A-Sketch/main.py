import turtle as t
from turtle import Turtle, Screen
import random
t.colormode(255)

def color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)


tim = Turtle()
tim.pensize(10)
def move_forwards():
    tim.color(color())
    tim.forward(10)

def move_backwards():
    tim.color(color())
    tim.forward(-10)

def left():
    tim.color(color())
    tim.left(5)

def right():
    tim.color(color())
    tim.right(5)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()
screen.listen()
screen.onkeypress(key="space",fun=move_forwards)
screen.onkeypress(key="s",fun=move_backwards)
screen.onkeypress(key="d",fun=right)
screen.onkeypress(key="a",fun=left)
screen.onkeypress(key="c",fun=clear)

screen.exitonclick()