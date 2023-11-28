from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
X_DISTANCE = 330



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.goto(x = X_DISTANCE, y= random.randint(-250, 250))


    def car_move(self, speed):
        self.forward(speed)
        
    def remove_turtle(self):
        self.hideturtle()
    
    def increase_speed(self, speed):
        speed += MOVE_INCREMENT
        return speed
        
    

        