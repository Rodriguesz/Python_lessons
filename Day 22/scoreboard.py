from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(position)
        self.color("white")
        self.update_score()
    
    def add_score(self):
        self.score += 1
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"{self.score}", font= FONT, align= ALIGNMENT)
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", font= FONT, align= ALIGNMENT)  