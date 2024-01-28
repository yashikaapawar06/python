import tkinter


window = tkinter.Tk()
window.title("Miles to km converter")
window.minsize(300,100)
#mile_input
input = tkinter.Entry(width= 20)
input.grid(row=1, column=2)
mile_label = tkinter.Label(text="miles", font=("Arial", 15, "normal"))
mile_label.grid(row=1, column=3)
is_equal_to = tkinter.Label(text="is equal to", font=("Arial", 15, "normal"))
is_equal_to.grid(row=2, column= 0)

km = tkinter.Label(text="km", font=("Arial", 15, "normal"))
km.grid(row=2, column=3)

def onclicked():
    result = float(input.get()) * 1.6
    km_output = tkinter.Label(text=result, font=("Arial", 15, "normal"))
    km_output.grid(row=2, column=2)

calculate = tkinter.Button(text="Calculate", command=onclicked)
calculate.grid(row=3, column=2)

window.mainloop()