# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

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
