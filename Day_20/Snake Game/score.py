from turtle import Turtle


class Score:

    def __init__(self):
        self.score = 0

        self.score_label = Turtle()
        self.score_label.hideturtle()
        self.score_label.penup()
        self.score_label.color("red")

        self.score_label.goto(0, 260)

        self.update_score()

    def update_score(self):
        self.score_label.clear()

        self.score_label.write(
            f"Current Score: {self.score}",
            align="center",
            font=("Courier", 18, "normal")
        )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.score_label.goto(0, 0)

        self.score_label.write(
            "GAME OVER",
            align="center",
            font=("Courier", 24, "bold")
        )