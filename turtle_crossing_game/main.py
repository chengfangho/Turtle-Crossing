from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()
screen.listen()
screen.onkeypress(player.move, "Up")
game_is_on = True

while game_is_on:
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    time.sleep(0.1)
    for car in car_manager.all_cars:
        if car.distance(player) < 20 or car.distance(player) < 30 and abs(car.ycor() - player.ycor()) < 10:
            game_is_on = False
    if player.ycor() > 290:
        scoreboard.add_score()
        scoreboard.display()
        car_manager.speed_up()
        player.reset()

screen.exitonclick()