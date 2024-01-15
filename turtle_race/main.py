from turtle import Turtle, Screen

tim = Turtle()

#Etch a sketch application
def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def clockwise():
    new_dir = tim.right(10) + 10
    tim.setheading(new_dir)

def anti_clockwise():
    new_dir = tim.left(10) - 10
    tim.setheading(new_dir)

def clear_screen():
    tim.clear()
    tim.reset()


screen = Screen()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(anti_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()