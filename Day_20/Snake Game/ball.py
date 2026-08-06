import random
from turtle import Turtle


class Ball:

    def __init__(self):
        self.ball = Turtle("circle")
        self.ball.color("pink")
        self.ball.penup()
        self.ball.shapesize(0.8, 0.8)
        self.create_ball()

    def create_ball(self):
        x = random.randrange(-280, 281, 20)
        y = random.randrange(-280, 281, 20)

        self.ball.goto(x, y)