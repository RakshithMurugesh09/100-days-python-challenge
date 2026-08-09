from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=0.5)
        self.goto(position)

    def paddle_up(self):
        if self.ycor() < 200:
            self.goto(self.xcor(),self.ycor() + 20)

    def paddle_down(self):
        if self.ycor() > -200:
            self.goto(self.xcor(),self.ycor() - 20)