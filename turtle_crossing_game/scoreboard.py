from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-220, 260)
        self.display()
    def add_score(self):
        self.score += 1
    def display(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)
