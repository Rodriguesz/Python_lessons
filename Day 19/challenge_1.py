from turtle import Screen, Turtle
import random
turtle = Turtle()
screen = Screen()



def move_foward():
    turtle.forward(10)
    
def move_backward():
    turtle.backward(10)

def counter_clockwise():
    turtle.left(10)

def clockwise():
    turtle.right(10)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()
    
screen.listen()
screen.onkey(key="w", fun= move_foward)
screen.onkey(key="s", fun= move_backward)
screen.onkey(key="a", fun= counter_clockwise)
screen.onkey(key="d", fun= clockwise)
screen.onkey(key="c", fun= clear)
screen.exitonclick()