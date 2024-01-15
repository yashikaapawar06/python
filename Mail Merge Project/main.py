list_of_names = []

#enter the names in a list
with open("./Input/Names/invited_names.txt") as names_list:
    names = names_list.read()
    list_of_names = names.split("\n")
    print(list_of_names)
#read the letter contents and store it in a variable
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()


#replacing the names in the letter
for list_item in list_of_names:
    with open(f"./Output/ReadyToSend/letter_to_{list_item}.txt",mode="w") as letter:
        letter.write(letter_content.replace("[name]", list_item))

