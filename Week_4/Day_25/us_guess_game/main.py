from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

background = Turtle()
background.shape(image)

# Get coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor())
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_list = []

# TODO Use a loop to allow the user to keep guessing
while len(guessed_list) < 50:
    # TODO Keep track of the score
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 States Correct", prompt="What's another state's")
    # TODO Convert the guess to Title case
    titlecase_state = answer_state.title()

    # TODO Check if the guess is among the 50 states
    # TODO Write correct guesses onto the map
    if titlecase_state == "Exit":
        break
    if titlecase_state in states:
        text = Turtle()
        text.hideturtle()
        state_row = data[data["state"] == f"{titlecase_state}"]
        text.teleport(int(state_row["x"].iloc[0]), int(state_row["y"].iloc[0]))
        text.write(f"{titlecase_state}")
        # TODO Record the correct guesses in a list
        guessed_list.append(titlecase_state)
        states.remove(titlecase_state)


states_to_learn = pandas.DataFrame(states)
states_to_learn.to_csv("states_to_learn.csv")



