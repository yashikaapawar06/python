from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.newx = 10
        self.newy = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.newx
        new_y = self.ycor() + self.newy
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.newy = self.newy * -1

    def bounce_x(self):
        self.newx = self.newx * -1
        self.move_speed *= 0.9


    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
