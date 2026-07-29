from turtle import Turtle, Screen
import time

MOMENT = 10

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

turtle = Turtle(shape="turtle")
turtle.penup()


def move_up():
    if turtle.heading() != DOWN:
        turtle.setheading(UP)


def move_down():
    if turtle.heading() != UP:
        turtle.setheading(DOWN)


def move_right():
    if turtle.heading() != LEFT:
        turtle.setheading(RIGHT)


def move_left():
    if turtle.heading() != RIGHT:
        turtle.setheading(LEFT)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Etch A Sketch")

screen.listen()

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")

screen.tracer(0)

while True:
    screen.update()
    turtle.forward(MOMENT)
    time.sleep(0.1)

screen.exitonclick()