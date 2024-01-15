from turtle import Turtle, Screen
import random
color = ["red", "yellow", "purple", "orange", "blue", "green"]
turtles = []
i = 0
y = -150
for _ in range(6):
    turt = Turtle(shape = "turtle")
    turt.penup()
    turt.color(color[i])
    turt.goto(x = -200, y = y)
    i = i+1
    y += 50
    turtles.append((turt))


screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make a bet", prompt= "Which turtle will win three race? Enter a color?:")
if user_bet:
    is_race_on = True

while is_race_on:

    for turt in turtles:
        if turt.xcor() > 230:
            is_race_on = False
            winning_color = turt.pencolor()
            if winning_color == user_bet:
                print("You won! you guessed it right!")
            else:
                print(f"Oops! You lost {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turt.forward(random_distance)


screen.exitonclick()