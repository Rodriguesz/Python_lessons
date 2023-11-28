from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()

def move_foward():
    turtle.forward(10)

#allow tutle "listen" to keys on keyboard 
screen.listen()
screen.onkey(key="space", fun= move_foward)

screen.exitonclick()

