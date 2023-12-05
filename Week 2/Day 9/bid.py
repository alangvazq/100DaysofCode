from replit import clear
import art

print(art.logo)
print("Welcome to the secret auction program.\n")
total_bidders = {}
restart = 'yes'

while restart == 'yes':
  name = input("What is your name?: ")
  bid = int(input("What's your bid?" ))
  total_bidders[name] = bid
  restart = input("Are there any other bidders? Type 'yes' or 'no'. ")
  clear()
  if restart == 'no':
    sum = 0
    name = ''
    for key in total_bidders:
      if total_bidders[key] > sum:
        sum = total_bidders[key]
        name = key
    print(f"The winner is {name} with a bid of ${total_bidders[name]}.")
    restart = False