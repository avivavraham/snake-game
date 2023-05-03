from turtle import Turtle
MOVE_QUANTITY = 20
'''
Snake class-
responsible for creating and extending snake.
responsible for moving the snake around.
'''


class Snake:
    def __init__(self):
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]

    def create_snake(self):
        for i in range(3):
            self.add_body_part((-20 * i, 0))

    def add_body_part(self, position):
        turtle = Turtle("square")
        turtle.penup()
        turtle.speed("fastest")
        turtle.goto(position)
        turtle.color("white")
        self.body_parts.append(turtle)

    def extend_snake(self):
        self.add_body_part(self.body_parts[-1].position())

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

    def reset(self):
        for body_part in self.body_parts:
            body_part.goto((1000, 1000))
        self.body_parts.clear()
        self.create_snake()
        self.head = self.body_parts[0]
