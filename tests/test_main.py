from test_game import Game
from test_snake import Snake
from test_food import Food
from test_scoreboard import Scoreboard
import time

game = Game()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

game.screen.listen()
game.screen.onkey(snake.up, "w")
game.screen.onkey(snake.down, "s")
game.screen.onkey(snake.left, "a")
game.screen.onkey(snake.right, "d")

game_on = True
while game_on:
    game.screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    wall_collision = (
        snake.head.xcor() > 280 or snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or snake.head.ycor() < -280
    )

    tail_collision = False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            tail_collision = True
            break

    if wall_collision or tail_collision:
        game_on = False
        scoreboard.game_over()

game.screen.exitonclick()
