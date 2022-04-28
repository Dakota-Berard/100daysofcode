from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car():
    def __init__(self):
        self.cars = []
        self.create_car()

    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-240, 280)
            new_car.goto(300, random_y)
            new_car.color(random.choice(COLORS))
            self.cars.append(new_car)

    def drive(self):
        for vehicle in self.cars:
            vehicle.backward(STARTING_MOVE_DISTANCE)

