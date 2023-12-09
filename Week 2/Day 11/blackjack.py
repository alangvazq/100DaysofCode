############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = True
add_card = True

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

def add_cards(cards, array):
  array.append(random.choice(cards))
  while len(array) < 2:
    array.append(random.choice(cards))

  if array[0] == 11 and array[1] == 11:
    array[1] = 1

  for position in range(0, len(array) - 2):
    if array[position] == 11 and array[len(array -1)] == 11:
      array[len(array -1)] = 1
    

  if array == computer_cards:
    while sum(computer_cards) < 17:
      array.append(random.choice(cards))

  return array

if start == "y":
  while play == True:
    #print(logo)
    user_cards = []
    computer_cards = []

    add_cards(cards, user_cards)
    add_cards(cards, computer_cards)
  
    while add_card == True:
      print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
      print(f"Computer's first card: {computer_cards[0]}")
      
      add = input("Type 'y' to get another card, type 'n' to pass:")
      if add == "y":
        add_cards(cards, user_cards)
        if sum(user_cards) > 21:
          add_card = False
      elif add == "n":
        add_card = False
  
    # user_cards
    # computer_cards
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    
    if sum(user_cards) > 21:
      print("You went over. You lose \U0001F622")
    elif sum(computer_cards) > 21:
      print("Opponent went over. You win \U0001F604")
    elif sum(computer_cards) < sum(user_cards):
      print("You win \U0001F604")
    elif sum(computer_cards) > sum(user_cards):
      print("You lose \U0001F622")
    else:
      print("It's a Draw \U0001F632")

    again = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if again == "y":
      add_card = True
    elif again == "n":
      play = False
      