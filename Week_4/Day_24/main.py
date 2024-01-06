# TODO: Create a letter using starting_letter.txt

with open("./Input/Letters/starting_letter.txt", "r") as letter_lines:
    lines = letter_lines.readlines()

with open("./Input/Names/invited_names.txt", "r") as name_lines:
    names = name_lines.readlines()

first_line = lines[0]

for item in range(0, len(names)):
    name = names[item].strip("\n")
    replace = first_line.replace("[name]", f"{name}")
    lines[0] = replace
    names_string = ''.join(lines)

    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as new_file:
        new_file.write(f"{names_string}")
