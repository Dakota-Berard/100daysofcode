import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)
tim.speed("fastest")


def draw_square():
    for i in range(0, 4):
        tim.forward(100)
        tim.right(90)


def draw_dashed_line():
    for _ in range(15):
        tim.forward(10)
        tim.pu() if tim.isdown() else tim.pd()


def random_color():
    tim.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))


def shape_spam():
    angle = 0
    for i in range(8):
        vectors = i + 3
        angle = 360 / vectors
        random_color()
        while vectors > 0:
            tim.forward(100)
            tim.right(angle)
            vectors -= 1


def random_walk(num):
    for i in range(num):
        random_color()
        tim.pensize(15)
        tim.forward(50)
        tim.right(random.choice([0, 90, 180, 270]))
        #tim.setheading(random.choice([0, 90, 180, 270]))


def spirograph(step):
    for _ in range(int(360/step)):
        random_color()
        tim.circle(100)
        tim.setheading(tim.heading() + step)



#draw_square()
#draw_dashed_line()
#shape_spam()
#random_walk(200)
#spirograph(5)







screen = Screen()
screen.exitonclick()
