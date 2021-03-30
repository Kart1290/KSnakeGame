from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.title('SNAKE by Kart')
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.update()

screen.listen()
screen.onkey(snake.down, 'Down')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    if snake.turtles_[0].distance(food) < 18:
        food.refresh()
        score.score_counter()
        snake.grow()

    if snake.turtles_[0].xcor() > 280 or snake.turtles_[0].xcor() < -280 or snake.turtles_[0].ycor() > 280 or \
            snake.turtles_[0].ycor() < -280:
        score.reset_score()
        snake.reset_snake()

    for seg in snake.turtles_[1:]:
        if snake.turtles_[0].distance(seg) < 10:
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()
