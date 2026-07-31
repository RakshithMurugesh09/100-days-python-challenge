from turtle import Turtle, Screen

MOVE_DISTANCE = 10
TURN_ANGLE = 10

tim = Turtle()
screen = Screen()

screen.title("Etch-A-Sketch")


def move_forward():
    tim.forward(MOVE_DISTANCE)


def move_backward():
    tim.backward(MOVE_DISTANCE)


def turn_left():
    tim.left(TURN_ANGLE)


def turn_right():
    tim.right(TURN_ANGLE)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear_screen, "c")

screen.exitonclick()