from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()






screen.listen()
screen.onkeypress(paddle.move_up, "Up")
screen.onkeypress(paddle.move_down, "Down")

game_on = True
while game_on:
    screen.update()




screen.exitonclick()
