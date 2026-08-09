import time
from turtle import Screen, Turtle
from ball import Ball
from pad import Paddle
from score import GameScore


def center_line():
    line = Turtle()
    line.hideturtle()
    line.color("red")
    line.penup()
    line.goto(0, -250)
    line.setheading(90)

    for _ in range(25):
        line.pendown()
        line.forward(10)
        line.penup()
        line.forward(10)


screen = Screen()
screen.setup(width=700, height=500)
screen.bgcolor("white")
screen.title("Pong")
screen.tracer(0)

center_line()

left_paddle = Paddle((-320, 0))
right_paddle = Paddle((320, 0))

left_score = GameScore((-100, 200))
right_score = GameScore((100, 200))

ball = Ball()

screen.listen()
screen.onkeypress(left_paddle.paddle_up, "w")
screen.onkeypress(left_paddle.paddle_down, "s")
screen.onkeypress(right_paddle.paddle_up, "Up")
screen.onkeypress(right_paddle.paddle_down, "Down")

game_is_on = True

while game_is_on:

    time.sleep(ball.move_speed)

    screen.update()
    ball.move()

    # Top and bottom wall collision
    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.bounce_y()

    # Right paddle collision
    if ball.xcor() > 300 and ball.distance(right_paddle) < 50:
        ball.bounce_x()

    # Left paddle collision
    if ball.xcor() < -300 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    # Right side missed
    if ball.xcor() > 340:
        left_score.increase_score()
        ball.reset_ball()

    # Left side missed
    if ball.xcor() < -340:
        right_score.increase_score()
        ball.reset_ball()

screen.exitonclick()