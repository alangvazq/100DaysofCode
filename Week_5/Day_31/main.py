from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/french_words.csv")
data_dict = data.to_dict(orient="records")
r_num = 0


def select_random():
    return random.randint(0, len(data_dict))


def random_word():
    global flip_timer
    global r_num
    window.after_cancel(flip_timer)
    r_num = select_random()
    r_word = data_dict[r_num]["French"]
    canvas.itemconfig(word, text="French", fill="black")
    canvas.itemconfig(translation, text=r_word, fill="black")

    flip_timer = window.after(3000, flip)


def flip():
    global r_num
    canvas.itemconfig(image, image=card_back)
    canvas.itemconfig(word, text="English", fill="white")
    canvas.itemconfig(translation, fill="white")
    r_word = data_dict[r_num]["English"]
    canvas.itemconfig(translation, text=r_word)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
image = canvas.create_image(400, 263, image=card)
word = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
translation = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(column=1, row=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, command=random_word)
wrong_button.grid(column=1, row=1)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, command=flip)
right_button.grid(column=2, row=1)

random_word()

window.mainloop()
