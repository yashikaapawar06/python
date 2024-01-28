import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(500,300)
window.config(padx=20,pady=20)

#label
my_label = tkinter.Label(text="I am label!", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)
my_label.config(padx=100,pady=20)
# my_label["text"] = "Yashika"

##or

# my_label.config(text="Yashika")
#button
def on_clicked():
    user_input = input.get()
    my_label["text"] = user_input


button = tkinter.Button(text="Click me!", command=on_clicked)
button.grid(row=2, column=3)

#entry

input = tkinter.Entry(width= 20)
input.grid(row=1, column=1)

button2 = tkinter.Button(text="button2")
button2.grid(row=0, column=2)




window.mainloop()