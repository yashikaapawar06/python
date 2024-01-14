#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
print(logo)
import random
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def easy(number):
  print("You have 10 attempts remaining to guess the number.")
  attempts=10
  while attempts>0:
    guess=int(input("Make a guess:"))
    if guess==number:
      print(f"You got it! The answer was {number}")
      break
    attempts-=1
    if guess<number:
      print("Too low")
      print("Guess again")
      print(f"You have {attempts} attempts remaining to guess the number ")
    else:
      print("Too high")
      print("Guess again")
      print(f"You have {attempts} attempts remaining to guess the number ")
    if attempts==0:
      print("You lose!")
  
def hard(number):
  print("You have 5 attempts remaining to guess the number.")
  attempts=5
  while attempts>0:
    guess=int(input("Make a guess:"))
    if guess==number:
      print(f"You got it! The answer was {number}")
      break
    attempts-=1
    if guess<number:
      print("Too low")
      print("Guess again")
      print(f"You have {attempts} attempts remaining to guess the number ")
    else:
      print("Too high")
      print("Guess again")
      print(f"You have {attempts} attempts remaining to guess the number ")
    if attempts==0:
      print("You lose!")
  

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty_level=input("Choose a difficulty level: Type 'easy' or 'hard'.")
number=random.randint(1,100)
# print(f"Psst, the answer is {number}")
if difficulty_level=="easy":
  easy(number)
elif difficulty_level=="hard":
  hard(number)
else:
  print("Please type 'easy' or 'hard'.")