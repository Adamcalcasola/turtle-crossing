from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        if random.randint(1, 6) == 1:
            random_y = random.randrange(-250, 250, 50)
            new_car = Turtle("square")
            new_car.turtlesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(MOVE_INCREMENT)



