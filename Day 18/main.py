from turtle import Turtle, Screen, colormode
import random
torugo = Turtle()
screen = Screen()
# torugo.shape("turtle")
torugo.color("black")
#change the color mode to 255
colormode(255)


#? Challange 1: Draw a square
# for _ in range(4):
#     torugo.forward(100)
#     torugo.right(90)


#? Challange 2: Draw a dashad line    
# for _ in range(7):
#     torugo.forward(10)
#     torugo.penup()
#     torugo.forward(10)
#     torugo.pendown()

#? Challange 3: Draw different shapes
# sides = 3
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return torugo.pencolor(r, g, b)

# for _ in range(10):
    
#     torugo.pencolor(random_color())
#     for _ in range (sides):
#         torugo.forward(100)
#         torugo.right(360/sides)
#     sides +=1

#? Challenge 4: Random walk
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def random_direction():
#     direction = [0, 180, 90, 270]
#     return torugo.setheading(random.choice(direction))

# def false(bool_value):
#     bool_value = False
#     return bool_value

# torugo.speed(5)
# torugo.pensize(10)
# for _ in range(200):
#     random_direction()
#     random_color()
#     torugo.forward(30)
 
#? Challenge 5: Draw a Spirograph
torugo.speed(30)
for _ in range(int(360 / 5)):
    random_color()
    torugo.circle(100)
    torugo.right(5)
screen.exitonclick()
