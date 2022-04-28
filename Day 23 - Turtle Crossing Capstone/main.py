from turtle import Turtle, Screen
from car import Car
from player import Player
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.colormode(255)
screen.tracer(0)

car = Car()
player = Player()
score = Scoreboard()

speed = 0.1

screen.listen()
screen.onkeypress(player.move_up, "Up")


game_on = True
while game_on:
    time.sleep(speed)
    screen.update()
    car.create_car()
    car.drive()

    #Check for crashes
    for vehicle in car.cars:
        if player.distance(vehicle) <= 20:
            print("Collision!")
            game_on = False
            break

    #Detects a successful crossing
    if player.ycor() > 280:
        score.levelup()
        player.restart()
        speed *= 0.6

score.gameover()

screen.exitonclick()
