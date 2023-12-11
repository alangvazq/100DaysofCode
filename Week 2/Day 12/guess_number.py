#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

number = list(range(1, 100))
random = random.choice(number)
print(random)
game = True

print(logo)
print("Welcome to the Number Guessing Game!")
print("\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
  attempt = 10
elif difficulty == "hard":
  attempt = 5

while game:
  print(f"\nYou have {attempt} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))

  if guess > random:
    print("\nToo high.")
    
  elif guess < random:
    print("\nToo low.")
    
  elif guess == random:
    print(f"\nYou got it! The answer was {guess} \U0001F604")
    break
    
  
  attempt -= 1

  if attempt == 0:
    print("You've run out of guesses, you lose \U0001F622")
    break

  print("Guess again.")