from turtle import Turtle, Screen
import time

from snake_class import Snake

# Screen config
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0) # set it to 0 turn off the animation 
screen.title("My Snake Game")


snake = Snake()

screen.listen()
screen.onkey(key="Up", fun= snake.move_up)
screen.onkey(key="Down", fun= snake.move_down)
screen.onkey(key="Left", fun= snake.move_left)
screen.onkey(key="Right", fun= snake.move_right)

game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(0.1)          #start       stop step
    snake.move()

screen.exitonclick()