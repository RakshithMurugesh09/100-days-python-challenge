from turtle import Turtle, Screen
from random import randint
import time

POSITIONS = [(-270, 0), (-270, 100), (-270, -100), (-270, -200), (-270, 200)]
COLORS = ["red", "green", "blue", "yellow", "purple"]

screen = Screen()
screen.title("Turtle Race")
screen.bgcolor("black")
screen.setup(width=600, height=600)

user_bet = screen.textinput(
    title="Make Your Bet",
    prompt="Which turtle will win the race? Enter a color: "
)

screen.tracer(0)

all_turtles = []

for i in range(len(POSITIONS)):
    turtle = Turtle(shape="turtle")
    turtle.color(COLORS[i])
    turtle.penup()
    turtle.goto(POSITIONS[i])
    turtle.speed("fastest")
    all_turtles.append(turtle)

is_race_on = False

if user_bet:
    is_race_on = True

winner = ""

while is_race_on:
    screen.update()

    for turtle in all_turtles:
        turtle.forward(randint(0, 30))

        if turtle.xcor() > 250:
            winner = turtle.pencolor()
            is_race_on = False
            break

    time.sleep(0.1)

if user_bet:
    if user_bet.lower() == winner:
        print(f"🎉 Congratulations! You won! The {winner} turtle is the winner.")
    else:
        print(f"😢 You lost. The winner is the {winner} turtle.")

screen.exitonclick()
