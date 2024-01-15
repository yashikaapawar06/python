from turtle import Turtle
positions = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.new_segment = []
        self.create()
        self.head = self.new_segment[0]
    def create(self):
        for position in positions:
            self.add_segment(position)

    def add_segment(self,position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.new_segment.append(new_turtle)

    def extend(self):
        self.add_segment(self.new_segment[-1].position())


    def move(self):
        for segment in range(len(self.new_segment) - 1, 0, -1):
            new_x = self.new_segment[segment - 1].xcor()
            new_y = self.new_segment[segment - 1].ycor()
            self.new_segment[segment].goto(new_x, new_y)
        self.head.forward(20)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        for seg in self.new_segment:
            seg.goto(1000,1000)

        self.new_segment.clear()
        self.create()
        self.head = self.new_segment[0]
