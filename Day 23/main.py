STARTING_MOVE_DISTANCE = 5

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

score = Scoreboard()

screen.listen()
screen.onkey(key = "Up", fun=player.move)

count = 8
game_is_on = True
car_list = []
speed = STARTING_MOVE_DISTANCE

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    #spawn cars
    count -= 1
    if count == 0:
        car = CarManager()
        car_list.append(car) 
        count = 8
    
    #move cars
    for car in car_list:
        if car.xcor() > -350:
            car.car_move(speed)
            #if the player collides with a car
            if player.distance(car) < 20:
                score.game_over()
                game_is_on = False
        else:
            car.remove_turtle()

    #if the player reaches the top
    if player.ycor() > 280:
        score.level_up()
        speed = car.increase_speed(speed)
        player.reset_turtle()
    
    
screen.exitonclick()
    
    
    
