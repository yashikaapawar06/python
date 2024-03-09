############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from replit import clear
from art import logo
import random
card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
while(1):
  if input("Do you want to play a game of Blackjack? Type 'y' or 'n':")=='y':
    clear()
    print(logo)
    user_card=[]
    computer_choice=[]
    while len(user_card)<2:
      user_card.append(random.choice(card))
    print(f"Your cards: {user_card}, current score: {sum(user_card)}")
    computer_choice.append(random.choice(card))
    print("Computer's first card: ",computer_choice)
    while input("Type 'y' to get another card, type 'n' to pass:") == 'y':
      user_card.append(random.choice(card))
      print(f"Your cards: {user_card}, current score: {sum(user_card)}")
      computer_choice.append(random.choice(card))
      print("Computer's first card: ",int(computer_choice[0]))
      if sum(user_card)>21:
        print(f"Your final hand: {user_card}, final score: {sum(user_card)}")
        print(f"Computer's final hand: {computer_choice}, final score: {sum(computer_choice)}")
        print("You went over!! you lose😭")
        break
    print(f"Your cards: {user_card}, current score: {sum(user_card)}")
    print(f"Computer's final hand: {computer_choice}, final score: {sum(computer_choice)}")
    if (user_card[0]==11 and user_card[1]==10) or (user_card[0]==10 and user_card[1]==11):
      print("Win with a Blackjack 😎")
    elif sum(user_card)<sum(computer_choice) and not sum(computer_choice)>21:
      print("You lose 😤")
    elif sum(user_card)==sum(computer_choice) and sum(user_card)<=21:
      print("Draw 🙃")
    elif sum(user_card)==21 or (sum(user_card)>sum(computer_choice) and not sum(user_card)>21):
      print("You win 😃")
    elif sum(user_card)<21 and sum(computer_choice)>21:
      print("Opponent went over. You win 😃")
  else:
    break
  
  
