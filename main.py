from turtle import Screen
from Snake_ import Snake
from SnakeFood import SnakeFood
from ScoreBoard import ScoreBoard
import time


game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("black")
game_screen.title("My Snake Game")
game_screen.tracer(0)

snake = Snake()
food = SnakeFood()
score_board = ScoreBoard()
score_board.score_update()
game_screen.listen()
game_screen.onkey(snake.up, "Up")
game_screen.onkey(snake.left, "Left")
game_screen.onkey(snake.right, "Right")
game_screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collisions with food
    if snake.head.distance(food) < 16:
        food.relocate()
        score_board.score += 1
        score_board.clear()
        score_board.score_update()

game_screen.exitonclick()
