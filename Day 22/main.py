from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball



# Screen config
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

player_1 = Paddle((350, 0))
player_2 = Paddle((-350, 0))

player1_score = Scoreboard((100, 180))
player2_score = Scoreboard((-100, 180))

ball = Ball()



screen.listen()
screen.onkey(key="Up", fun= player_1.move_up)
screen.onkey(key="Down", fun= player_1.move_down)
screen.onkey(key="w", fun= player_2.move_up)
screen.onkey(key="s", fun= player_2.move_down)

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    
    #Detect collision with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()
        
    #detec collision with paddle
    if ball.distance(player_1) < 50 and ball.xcor() > 320 or ball.distance(player_2) < 50  and  ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() >380:
        ball.reset_position()
        player2_score.add_score()
    elif ball.xcor() < -380:
        ball.reset_position()
        player1_score.add_score()
        
screen.exitonclick()