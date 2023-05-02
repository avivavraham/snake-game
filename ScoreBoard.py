from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')


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
