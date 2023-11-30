rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

options = ["rock", "paper", "scissors"]

computer_choice = random.randint(0, 2)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if user_choice == 0:
    print("You chose Rock.")
elif user_choice == 1:
    print("You chose Paper.")
elif user_choice == 2:
    print("You chose Scissors.")
else:
    print("Invalid choice. Please choose 0 for Rock, 1 for Paper, or 2 for Scissors.")

print("Computer's choice:")
print(options[computer_choice])

if user_choice == computer_choice:
    print("It's a draw!")
elif (
    (user_choice == 0 and computer_choice == 2)
    or (user_choice == 1 and computer_choice == 0)
    or (user_choice == 2 and computer_choice == 1)
):
    print("You win!")
else:
    print("You lose!")
