from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('white')
        self.speed(0)
        self.seth(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(10)

    def next_level_shit(self):
        self.goto(STARTING_POSITION)
