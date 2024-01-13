import tkinter
from tkinter import *


def button_clicked():
    mile = float(mile_entry.get())
    km = round(mile * 1.609344, 4)
    km_entry.delete(0, END)
    return km_entry.insert(END, string=str(km))


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=40, pady=40)

# Entry
mile_entry = Entry(width=15)
mile_entry.grid(column=0, row=0)

# label
equal_label = Label(text="=", font=("Arial", 24, "bold"))
equal_label.grid(column=1, row=0)

# Entry
km_entry = Entry(width=15)
km_entry.grid(column=2, row=0)

# label
mile_label = Label(text="Mile", font=("Arial", 12))
mile_label.grid(column=0, row=1)
mile_label.config(padx=10, pady=10)

# label
km_label = Label(text="Kilometre", font=("Arial", 12))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)


tkinter.mainloop()
