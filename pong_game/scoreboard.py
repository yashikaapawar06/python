from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.paddle1_score = 0
        self.paddle2_score = 0


    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.paddle1_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.paddle2_score, align="center", font=("Courier", 80, "normal"))

    def add_score_paddle1(self):
        self.paddle1_score += 1
        self.update_score()

    def add_score_paddle2(self):
        self.paddle2_score += 1
        self.update_score()

