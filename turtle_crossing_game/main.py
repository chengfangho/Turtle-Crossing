from turtle import Screen
from player import Player
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkeypress(player.move, "Up")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()