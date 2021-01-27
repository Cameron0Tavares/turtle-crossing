from turtle import Turtle
import random as r
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    x_start = 300
    move_start = STARTING_MOVE_DISTANCE

    def __init__(self):
        super().__init__()
        self.car_list = []
        self.hideturtle()

    def add_car(self):
        random_chance = r.randint(1, 5)
        if random_chance == 1:
            car = Turtle(shape='square')
            car.speed(0)
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(r.choice(COLORS))
            car.goto(self.x_start, r.randrange(-250, 250))
            self.car_list.append(car)

    def drive_car(self):
        for car in range(len(self.car_list)):
            self.car_list[car].backward(self.move_start)

    def next_level_shit(self):
        self.move_start += MOVE_INCREMENT

