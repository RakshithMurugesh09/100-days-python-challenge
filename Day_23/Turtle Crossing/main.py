from turtle import Screen
from player import Player
from car import Car
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = Car()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_manager.move_cars()

    # Collision Detection
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Level Complete
    if player.ycor() > 280:
        player.level_up()
        car_manager.speed_up()
        scoreboard.increase_level()

screen.exitonclick()