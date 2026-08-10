from turtle import Turtle

START_POS = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("red")
        self.setheading(90)
        self.goto(START_POS)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        self.goto(START_POS)