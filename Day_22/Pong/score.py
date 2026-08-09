from turtle import Turtle


class GameScore(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(self.score,align="center",font=("Courier", 36, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

