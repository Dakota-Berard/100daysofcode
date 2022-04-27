from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("purple")
        self.speed("fastest")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def moving(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.check_walls()

    def check_walls(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def restart(self):
        self.goto(0, 0)
        self.bounce_x()