from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_score()
        
        
    def update_score(self): 
        self.clear()
        self.goto(-220, 260)
        self.level += 1
        self.write(f"LEVEL: {self.level}", align='center', font=FONT)
        
    def game_over(self): 
        self.goto(0,0)
        self.write('GAME OVER', align='center', font=FONT)
