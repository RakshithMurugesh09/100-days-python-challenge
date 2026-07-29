import random
from turtle import Turtle, Screen

DOT_COLOR = ["red", "green", "blue"]
DOT_SIZE = 20
MOMENT = 50

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Spot paint")
screen.tracer(0)

turtle = Turtle()
turtle.hideturtle()
turtle.speed("fastest")
turtle.penup()
turtle.goto(-300, 200)

for row in range(10):
    for col in range(10):
        turtle.dot(DOT_SIZE, random.choice(DOT_COLOR))
        turtle.forward(MOMENT)

    turtle.setx(-300)
    turtle.sety(turtle.ycor() - MOMENT)

screen.update()
screen.exitonclick()