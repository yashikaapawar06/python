alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

special_characters=['!','@','#','$','%','^','&','*','1','2','3','4','5','6','7','8','9','0',' ']

def caesar(text, shift, direction):
  end_text = ""
  for i in range(len(text)):
    if text[i] in special_characters:
        end_text+=text[i]
    else:
      index=alphabet.index(text[i])
      if direction=="decode":
        shift_position=index-shift
        if shift_position<0:
          shift_position+=26
        end_text+=alphabet[shift_position]
      else:
        shift_position=index+shift
        if shift_position>26:
          shift_position=shift_position-26
        end_text+=alphabet[shift_position]
        
        
      
  
    
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
      
   
        
        
    
  print(f"Here's the {direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caesar(text,shift, direction)
while(1):
  user_input=input("Type 'yes' if you want to go again. Otherwise type 'no'.")
  if user_input=='yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
  else:
    print("Thank you! \n Goodbye")
    break
  

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

  caesar(text, shift, direction)