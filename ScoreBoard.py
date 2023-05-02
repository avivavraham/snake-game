from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')

'''
score board class-
responsible for keep tracking of the score, and displaying it constantly.
responsible to displaying GAME OVER when the user loses.
'''


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0
        self.penup()
        self.goto((0, 280))
        self.color("white")
        self.hideturtle()

    def score_update(self):
        self.write(f"score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto((0, 0))
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
