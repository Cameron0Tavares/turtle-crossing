import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
sb = ScoreBoard()
cm = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

get_hoppin = True
loop_count = 0
while get_hoppin:
    time.sleep(.1)
    loop_count += 1
    screen.update()
    cm.drive_car()
    cm.add_car()

    if player.is_at_finish():
        player.go_to_start()
        sb.next_level_shit()
        cm.next_level_shit()

    for car in cm.car_list:
        if car.distance(player) < 20:
            sb.game_over()
            get_hoppin = False

screen.exitonclick()