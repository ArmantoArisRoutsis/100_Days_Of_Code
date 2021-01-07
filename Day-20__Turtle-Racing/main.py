from turtle import Turtle, Screen
import random

is_race_on = False


screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet:",prompt="Which turtle will win the race? Enter a color:")


colors = ["red","orange","yellow","green","blue","purple"]
positions = [-150,-90,-30,30,90,150]
all_turtles = []
winner = ""

for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230,positions[i])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            print(winner)
        random_distance = random.randint(1,10)
        turtle.forward(random_distance)


print(f"The winner is the {winner} turtle!")
if winner == user_bet:
    print("Your bet was right!")
else:
    print("Your bet was wrong:(")


screen.exitonclick()