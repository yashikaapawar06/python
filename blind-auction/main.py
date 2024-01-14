from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to Blind Auction Program")
def blind_auction(bidders_info):
  max_value=0
  name=""
  for key in bidders_info:
    if bidders_info[key]>max_value:
      max_value=bidders_info[key]
      name=key
  print(f"The winner is {name} and the bid value is {max_value}")
    
    
  
bidding_finished=False
bidders_info={}
while bidding_finished==False:
  clear()
  name=input("What is your name?")
  bid_amount=int(input("what is your bid amount? $"))
  more_bidders=input("Are there any other bidders? Type 'yes or 'no'.")
  bidders_info[name]=bid_amount
  if more_bidders=="no":
    bidding_finished=True
blind_auction(bidders_info)  
  
  