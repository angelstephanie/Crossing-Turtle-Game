import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
description = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(turtle.move_fd, "Up")

game_is_on = True

scoreboard.level()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if turtle.ycor() == 280.0:
        turtle.go_to_start()
        car.level_up()
        scoreboard.level_up()
    car.create_car()
    car.move()
    for stuff in car.all_cars:
        if turtle.distance(stuff) <= 20:
            game_is_on = False
            description.game_over()

screen.exitonclick()
