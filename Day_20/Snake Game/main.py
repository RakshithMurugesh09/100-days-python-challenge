import time
from turtle import Screen
from snake import Snake
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Ball()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    snake.move()

    # Food Collision
    if snake.head.distance(food.ball) < 15:
        food.create_ball()
        snake.extend()
        score.increase_score()

    # Wall Collision
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_is_on = False

    # Tail Collision
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

score.game_over()

screen.exitonclick()