from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)  # turning turtles animation off

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # refreshing the screen
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:  # distance method returns the distance between 2 turtles (snake's head and food)
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with wall
    if abs(snake.head.xcor()) > 285 or abs(snake.head.ycor()) > 290:
        game_is_on = False
        scoreboard.write_game_over()

    # detect collision with its tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.write_game_over()

screen.exitonclick()
