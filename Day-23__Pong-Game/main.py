from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player1 = Paddle(350)
player2 = Paddle(-350)
ball = Ball()
score = Scoreboard()

game_is_on = True


screen.listen()
screen.onkeypress(player1.go_up,"Up")
screen.onkeypress(player1.go_down,"Down")
screen.onkeypress(player2.go_up,"w")
screen.onkeypress(player2.go_down,"s")

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    if ball.distance(player1)<50 and ball.xcor()>320 or ball.distance(player2)<50 and ball.xcor()>-330:
        ball.deflect()

    if ball.xcor() > 380:
        ball.reset_position()
        score.add_left()

    if ball.xcor() < -380:
        ball.reset_position()
        score.add_rigth()





screen.exitonclick()