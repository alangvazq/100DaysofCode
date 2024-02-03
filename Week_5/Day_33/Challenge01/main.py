from tkinter import *
import requests
import json

quote = ''

def get_quote():
    global quote
    response = requests.get(url='https://api.kanye.rest')
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote_text, text=data['quote'])


window = Tk()
window.title("Robot Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Robot Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

robot_img = PhotoImage(file="Robot.png")
robot_button = Button(image=robot_img, highlightthickness=0, command=get_quote)
robot_button.grid(row=1, column=0)

window.mainloop()
