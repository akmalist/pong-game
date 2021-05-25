from turtle import Screen, Turtle, reset
from paddle import Paddle
from ball import Ball
from  scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

scoreboard = ScoreBoard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    # detect collision with wall
    if ball.ycor() > 279 or ball.ycor() < -279:
        ball.bounce_y()
    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

    # detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()

    screen.update()

screen.exitonclick()
