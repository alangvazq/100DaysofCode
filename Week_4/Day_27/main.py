import tkinter
from tkinter import *


def button_clicked():
    my_label.config(text=input_entry.get())


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="I Am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


# Button
button = Button(text="Click", command=button_clicked)
button.grid(column=1, row=1)


# Entry
input_entry = Entry(width=10)
input_entry.grid(column=3, row=2)

tkinter.mainloop()
