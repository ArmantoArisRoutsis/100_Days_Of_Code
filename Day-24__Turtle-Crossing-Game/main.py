import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")



game_is_on = True
player.go_up()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    for i in car.all_cars:
        if i.distance(player)<20:
            game_is_on = False
            score.game_over()
    if player.ycor()>280:
        player.restart()
        car.level_up()
        score.next_level()






screen.exitonclick()