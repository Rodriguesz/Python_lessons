# import colorgram

# colors = colorgram.extract('image.jpg', 118)
# color_list = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     color_list.append(color_tuple)

# print(color_list)

from turtle import *
from color_list import color_list
import random
turtle = Turtle()
screen = Screen()
colormode(255)
# turtle.hideturtle()
turtle.speed("fastest")


def random_color():
    color = random.choice(color_list)
    return turtle.pencolor(color)
start_x = -275
start_y = -250

for _ in range(10):
    turtle.penup()  # Levanta o lápis da tartaruga
    turtle.goto(start_x, start_y)  # Defina a posição inicial
    for _ in range(10):
        random_color()
        turtle.penup()
        turtle.forward(50)
        turtle.dot(20)
        
    start_y += 50
turtle.hideturtle()    

screen.exitonclick()