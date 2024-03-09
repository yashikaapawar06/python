from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

#----------------------------------CHOOSING A RANDOM WORD--------------------#
data_list = {}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    data_list = original_data.to_dict(orient="records")
else:
    data_list = data.to_dict(orient="records")
choice = {}
def random_word():
    global choice, flip_timer
    window.after_cancel(flip_timer)
    choice = random.choice(data_list)
    canvas.itemconfig(heading, text="French", fill="black")
    canvas.itemconfig(content, text=choice['French'], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip_card)

def is_known():
    data_list.remove(choice)
    data1 = pd.DataFrame(data_list)
    data1.to_csv("data/words_to_learn.csv", index=False)
    random_word()
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(heading, text="English", fill="white")
    canvas.itemconfig(content, text=choice['English'], fill="white")



#-----------------------------------UI SETUP---------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, random_word)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

heading = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
content = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=0)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_word)
wrong_button.grid(row=1, column=1)

window.mainloop()
