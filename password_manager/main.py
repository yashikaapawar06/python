from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert("1.0", password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_txt = website_input.get("1.0", END)
    email_txt = email_input.get("1.0", END)
    password_txt = password_input.get("1.0", END)
    if len(website_txt)==0 or len(email_txt)==0 or len(password_txt) == 0:
        messagebox.showinfo(title="Oops",message="Please dont leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website_txt, message=f"These are the details entered\nEmail:{email_txt}\nPassword:{password_txt}\n is it ok to save this? ")
        if is_ok:
            with open("data.txt","a") as file:
                file.write(f" {website_txt} {email_txt} {password_txt}\n")
            website_input.delete("1.0",END)
            email_input.delete("1.0", END)
            password_input.delete("1.0", END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100,pady=20)
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,94, image=lock_img)
canvas.grid(row=1,column=1)

website = Label(text="Website:")
website.grid(row=2,column=0)
website_input = Text(height=1,width=35)
website_input.focus()
website_input.grid(row=2, column=1, columnspan=2)

email = Label(text="Username/Email:")
email.grid(row=3,column=0)
email_input = Text(height=1,width=35)
email_input.grid(row=3,column=1,columnspan=2)

password = Label(text="Password:")
password.grid(row=4,column=0)
password_input = Text(height=1,width=21)
password_input.grid(row=4, column=1)

generate_pass = Button(text="Generate Password",highlightthickness=0, command=password_generator)
generate_pass.grid(row=4,column=2)

add_button = Button(text="Add",width=39,highlightthickness=0,command=save)
add_button.grid(row=5,column=1,columnspan=2)



window.mainloop()