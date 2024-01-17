from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for n in range(nr_letters)]
    password_numbers = [random.choice(numbers) for n in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for n in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.delete(0, 'end')
    pass_entry.insert(0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    new_data = {
        web_entry.get(): {
            "email": email_entry.get(),
            "password": pass_entry.get()
        }
    }
    if web_entry.get() == "" or pass_entry.get() == "":
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:

        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        finally:
            web_entry.delete(0, 'end')
            pass_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Size of cell corresponds to the wider element
# Image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label Web
web_label = ttk.Label(text="Website: ")
web_label.grid(column=0, row=1)

# Entry Web
web_entry = ttk.Entry()
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2, sticky="we")

# Label Email
email_label = ttk.Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

# Entry Email
email_entry = ttk.Entry()
email_entry.insert(0, "python@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="we")

# Label Password
pass_label = ttk.Label(text="Password: ")
pass_label.grid(column=0, row=3)

# Entry Password
pass_entry = ttk.Entry()
pass_entry.grid(column=1, row=3, sticky="we")

# Button
generate = ttk.Button(text="Generate Password", command=generate_password)
generate.grid(column=2, row=3)

# Button
add = ttk.Button(text="Add", command=save)
add.grid(column=1, row=4, columnspan=2, sticky="we")

window.mainloop()
