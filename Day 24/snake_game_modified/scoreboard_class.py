from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 15, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_score()
    
    def add_score(self):
        self.score += 1
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font= FONT, align= ALIGNMENT)
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", font= FONT, align= ALIGNMENT)          
    
    def reset(self):
        if self.score > self.high_score:
            with open("Day_24/snake_game_modified/high_score.txt", mode="w") as arquivo:
                arquivo.write(str(self.score))
            self.high_score = self.read_high_score()
        self.score = 0
        self.update_score()
    
    def read_high_score(self):
        with open("Day_24/snake_game_modified/high_score.txt") as arquivo:
            high_score = arquivo.read()
            return int(high_score)
