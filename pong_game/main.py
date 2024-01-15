from turtle import Screen
from pong import Pong
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
game_is_on = True
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
paddle1 = Pong((350, 0))
paddle2 = Pong((-350, 0))
ball = Ball()
score = Scoreboard()
score.update_score()
screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")


while game_is_on:
    time.sleep(0.1)
    ball.move()
    #detect collision  with top and bottom walls
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce_y()
    #detect the collision with paddle1
    if ball.distance(paddle1)< 50 and ball.xcor() > 320:
        ball.bounce_x()

    #detect the collision with paddle2
    if ball.distance(paddle2)< 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect paddle missing the ball
    if ball.xcor() > 400 :
        ball.reset_position()
        score.add_score_paddle1()

    if ball.xcor() < -400 :
        ball.reset_position()
        score.add_score_paddle2()
    screen.update()

screen.exitonclick()