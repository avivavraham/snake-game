from turtle import Screen
from Snake_ import Snake
import time


game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("black")
game_screen.title("My Snake Game")
game_screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(0.1)
    snake.move()

game_screen.exitonclick()
