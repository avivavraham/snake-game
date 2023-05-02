from turtle import Turtle
import random


class SnakeFood(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")
        self.relocate()

    def relocate(self):
        self.goto((random.randint(-280, 280), random.randint(-280, 280)))
