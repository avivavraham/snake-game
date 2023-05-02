from turtle import Turtle
MOVE_QUANTITY = 20


class Snake:
    def __init__(self):
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]

    def create_snake(self):
        for i in range(3):
            turtle = Turtle("square")
            turtle.penup()
            turtle.speed("fastest")
            turtle.goto((-20 * i, 0))
            turtle.color("white")
            self.body_parts.append(turtle)

    def move(self):
        for body_num in range(len(self.body_parts) - 1, 0, -1):
            new_x = self.body_parts[body_num - 1].xcor()
            new_y = self.body_parts[body_num - 1].ycor()
            self.body_parts[body_num].goto(new_x, new_y)
        self.head.forward(MOVE_QUANTITY)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
