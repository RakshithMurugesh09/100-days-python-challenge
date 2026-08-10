from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car:

    def __init__(self):
        self.cars = []
        self.car_speed = 5

    def add_car(self):
        if random.randint(1, 20) in (1, 5):
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(400, random.randint(-250, 250))
            self.cars.append(new_car)

    def move_cars(self):
        self.add_car()
        for car in self.cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += 2