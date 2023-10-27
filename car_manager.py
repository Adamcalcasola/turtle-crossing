from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        random_y = random.randrange(-250, 250, 10)
        if random_y % 50 == 0:
            new_car = Turtle("square")
            new_car.turtlesize(1, 3)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, random_y)
            new_car.forward(STARTING_MOVE_DISTANCE)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)



