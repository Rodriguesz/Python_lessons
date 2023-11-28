from turtle import Screen
import time

from scoreboard_class import Score
from snake_class import Snake
from food_class import Food

# Screen config
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0) # set it to 0 turn off the animation 
screen.title("My Snake Game")


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key="Up", fun= snake.move_up)
screen.onkey(key="Down", fun= snake.move_down)
screen.onkey(key="Left", fun= snake.move_left)
screen.onkey(key="Right", fun= snake.move_right)

game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(0.1)          
    snake.move()
    
    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.reset()
        snake.reset()
    
    #Detect collision with tail
    for segment in snake.segments[1:]:
     
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()