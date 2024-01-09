from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

background = Turtle()
text = Turtle()
background.shape(image)


# Get coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor())
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
states = data["state"]
game_is_on = True
guessed_list = []

# TODO Use a loop to allow the user to keep guessing
while game_is_on:
    # TODO Keep track of the score
    answer_state = screen.textinput(title=f"{len(guessed_list)}/50 States Correct", prompt="What's another state's")
    # TODO Convert the guess to Title case
    titlecase_state = answer_state.title()

    # TODO Record the correct guesses in a list
    guessed_list.append(titlecase_state)

    # TODO Check if the guess is among the 50 states
    for state in states:
        # TODO Write correct guesses onto the map
        if state.title() == titlecase_state:
            state_row = data[data["state"] == f"{state}"]
            text.hideturtle()
            text.teleport(int(state_row["x"].iloc[0]), int(state_row["y"].iloc[0]))
            text.write(f"{state}")
        elif len(guessed_list) == 50:
            game_is_on = False


screen.exitonclick()
