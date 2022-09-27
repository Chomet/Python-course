import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

score = Scoreboard()
player = Player()
car_manager = CarManager()

screen.onkey(player.move, "Up")
screen.update()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_move()
    car_manager.spawn_cars()
    for cars in car_manager.carlist:
        if player.distance(cars) < 20:
            game_is_on = False
            score.end_screen()
    if player.ycor() >= FINISH_LINE_Y:
        player.reset()
        car_manager.reset()
        score.update_score()

screen.exitonclick()
