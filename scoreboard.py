from turtle import Turtle
FONT = ('Courier', 18, 'bold')


class ScoreBoard(Turtle):
    score = 1

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-225, 275)
        self.write('Level: ' + str(self.score), align='center', font=FONT)

    def next_level_shit(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        go_turt = Turtle()
        go_turt.hideturtle()
        go_turt.penup()
        go_turt.color('white')
        go_turt.write('GAME OVER', align='center', font=FONT)