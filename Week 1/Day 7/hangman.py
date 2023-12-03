# from replit import clear
import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

print(f'Pssst, the solution is {chosen_word}.')

display = []
check = []

for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # clear()
    
    check += guess
    double_check = guess
    if check.count(double_check) > 1:
    print(f"You've already introduced the letter {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word.")
        if lives == 0:
            end_of_game = True
            print("You lost.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won.")

    print(hangman_art.stages[lives])