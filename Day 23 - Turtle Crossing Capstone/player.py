from turtle import Turtle

STARTING_CORDS = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.restart()

    def move_up(self):
        self.forward(10)

    def restart(self):
        self.goto(STARTING_CORDS)
