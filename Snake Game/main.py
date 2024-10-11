from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600),
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "up")
screen.onkey(snake.down, "down")
screen.onkey(snake.left, "left")
screen.onkey(snake.right, "right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # DETECT COLLISION WITH FOOD.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.inc_score()

    # DETECT COLLISION WITH WALL.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # DETECT COLLISION WITH TAIL.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
