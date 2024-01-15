from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.teleport(0,280)
        self.color("white")
        self.score_count()


    def score_count(self):
        self.clear()
        self.teleport(0, 280)
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.write(f"Score : {self.count} High Score : {self.high_score} ", True, ALIGNMENT, FONT)


    def increase_score(self):
        self.count += 1
        self.score_count()
    def reset_score(self):
        if self.count > self.high_score:
            self.high_score = self.score_count()
            with open("data.txt", mode="w") as data:
                self.count = str(self.count)
                data.write(self.count)
        self.count = 0
        self.score_count()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!", True, ALIGNMENT, FONT)