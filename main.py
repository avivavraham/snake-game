from turtle import Screen
from Snake import Snake
from SnakeFood import SnakeFood
from ScoreBoard import ScoreBoard
import time

global SPEED_OF_GAME
# settings of screen
game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("black")
game_screen.title("My Snake Game")
game_screen.tracer(0)

snake = Snake()
food = SnakeFood()
score_board = ScoreBoard()
score_board.score_update()
# interacting with computer keys
game_screen.listen()
game_screen.onkey(snake.up, "Up")
game_screen.onkey(snake.left, "Left")
game_screen.onkey(snake.right, "Right")
game_screen.onkey(snake.down, "Down")


def reset_game():
    global SPEED_OF_GAME
    snake.reset()
    score_board.reset()
    game()


game_screen.onkey(reset_game, "space")


def game():
    global SPEED_OF_GAME
    SPEED_OF_GAME = 0.1
    game_is_on = True
    while game_is_on:
        game_screen.update()
        time.sleep(SPEED_OF_GAME)
        snake.move()
        # detect collisions with food
        if snake.head.distance(food) < 16:
            food.relocate()
            snake.extend_snake()
            score_board.score += 1
            score_board.clear()
            score_board.score_update()
            # increasing difficulty of game for every score achieved
            SPEED_OF_GAME /= 1.05
        # detect collisions with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            score_board.game_over()
        # detect collisions with tail
        for body_part in snake.body_parts[1:]:
            if snake.head.distance(body_part) < 10:
                game_is_on = False
                score_board.game_over()


game()
game_screen.exitonclick()
