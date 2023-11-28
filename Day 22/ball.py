STARTING_POSTION = (0, 0)
TOP_MAX = 300
BOTTOM_MAX =  - 400 
from turtle import Turtle
from time import sleep

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(STARTING_POSTION)
        self.x_move = 0.20
        self.y_move = 0.20
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
         
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        
    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        sleep(1)