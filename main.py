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

    if loop_count % 4 == 0:
        cm.add_car()

    if player.ycor() >= 280:
        player.next_level_shit()
        sb.next_level_shit()
        cm.next_level_shit()

    for car in cm.car_list:
        if abs(0 - car.xcor()) <= 30 and abs(player.ycor() - car.ycor()) <= 19:
            sb.game_over()
            screen.update()
            get_hoppin = False

screen.exitonclick()