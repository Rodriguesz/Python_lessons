# import another_module

# print(another_module.another_variable)


# # from turtle module import Turtle class
# from turtle import Turtle, Screen

# leo = Turtle()
# leo.shape("turtle")
# leo.color("DarkMagenta")
# leo.forward(100)

# my_screen = Screen()
# # ?     object    attribute (canva height)
# print(my_screen.canvheight)

# # ?           method()
# my_screen.exitonclick()

# # input("Press any key to exit ...")

#TODO: to install packages, go to project console and type "pip install name-of-package"

# pip install PrettyTable
from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])
table.align = 'l'

print(table)