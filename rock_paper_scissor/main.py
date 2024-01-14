rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_input=int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors. "))
list=[0,1,2]
computer_choice=random.choice(list)
if user_input==0:
  print(rock)
elif user_input==1:
  print(paper)
else:
  print(scissors)
print("computer chose:")
if computer_choice==0:
  print(rock)
elif computer_choice==1:
  print(paper)
else:
  print(scissors)
if user_input==0 and computer_choice==1:
  print("You lose")
elif user_input==1 and computer_choice==2:
  print("You lose")
elif user_input==2 and computer_choice==0:
  print("You lose")
elif user_input==1 and computer_choice==0:
  print("You win")
elif user_input==2 and computer_choice==1:
  print("You win")
elif user_input==0 and computer_choice==2:
  print("You win")
else:
  print("Its a tie")