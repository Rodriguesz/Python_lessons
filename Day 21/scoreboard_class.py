from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 15, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_score()
    
    def add_score(self):
        self.score += 1
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font= FONT, align= ALIGNMENT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", font= FONT, align= ALIGNMENT)          
              
