from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"


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


def delete_word():
    global r_num
    french_data_list.remove(data_dict[r_num]["French"])
    english_data_list.remove(data_dict[r_num]["English"])
    new_data_dict = {
        "French": french_data_list,
        "English": english_data_list
    }
    data_frame = pandas.DataFrame(new_data_dict)
    data_frame.to_csv("./data/words_to_learn.csv", index=False)
    random_word()


try:
    with open("data/words_to_learn.csv", "r") as words_to_learn:
        data = pandas.read_csv("./data/words_to_learn.csv")
        data_dict = data.to_dict(orient="records")
        french_data_list = data["French"].to_list()
        english_data_list = data["English"].to_list()
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    data_dict = data.to_dict(orient="records")
    french_data_list = data["French"].to_list()
    english_data_list = data["English"].to_list()
finally:
    r_num = 0

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
    right_button = Button(image=right_img, command=delete_word)
    right_button.grid(column=2, row=1)

    random_word()
    window.mainloop()
