from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=("Courier", 18, "normal"))

    def levelup(self):
        self.level += 1
        self.update_score()

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 18, "normal"))