import random
from turtle import *

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Enter a color: ")
color_list = ["red", "orange", "green", "blue", "yellow", "purple"]


turtle_list = []

x = -230
y = -100

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_list[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= x, y= y)
    y += 45
    turtle_list.append(new_turtle)
    
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 220:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print("Your turtle won the race")
            else: 
                print("Your turtle lost the race")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    
screen.exitonclick()
