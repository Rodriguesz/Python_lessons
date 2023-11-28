from turtle import Turtle
from scoreboard import Scoreboard
from car_manager import CarManager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def reset_turtle(self):
        self.goto(STARTING_POSITION)
        
        
