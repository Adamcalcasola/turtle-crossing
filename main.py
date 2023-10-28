import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")
screen.onkey(fun=player.backup, key="Down")
screen.onkey(fun=player.move_right, key="Right")
screen.onkey(fun=player.move_left, key="Left")

car_speed = 0.1
game_is_on = True
while game_is_on:
    car_manager.create_car()
    car_manager.move_cars()
    time.sleep(car_speed)
    screen.update()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() == 280:
        player.reset()
        scoreboard.level_up()
        car_speed *= 0.5

screen.exitonclick()