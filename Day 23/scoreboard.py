from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-220, 260)
        self.write(arg=f"Level: {self.score}", align= "center", font= FONT, move= False)
    
    def level_up(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Level: {self.score}", align= "center", font= FONT, move= False)
        
    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align= "center", font= FONT, move= False)
