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
        with open('data.txt', "r") as data:
            self.high_score = int(data.read())

    def score_update(self):
        self.write(f"score : {self.score}, high score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', "w") as data:
                data.write(f"{self.high_score}")
        self.goto((0, 0))
        self.write("GAME OVER\n press space to play again", align=ALIGNMENT, font=FONT)
        self.score = 0

    def reset(self):
        self.clear()
        self.goto((0, 280))
        self.score_update()
