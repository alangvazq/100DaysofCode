import random
from game_data import data
from art import logo,vs

data_copy = data
data_a_b = []
strike = 1
count = 0

def higher(data):
    if data[0]['follower_count'] > data[1]['follower_count']:
        return data[0]
    elif data[0]['follower_count'] < data[1]['follower_count']:
        return data[1]
    
print(logo)

data_a = random.choice(data_copy)
data_copy.pop(data_copy.index(data_a))

data_a_b.append(data_a)

while strike == 1:
    if count > 0:
        print(f"You're right! Current score: {count}.")

    data_b = random.choice(data_copy)
    data_copy.pop(data_copy.index(data_b))
    data_a_b.append(data_b)

    higher_data = higher(data_a_b)

    print(f"\nHint: {higher_data['name']}")

    print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}.")
    print(vs)
    print(f"Against B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}.")
    choice = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    if choice == "a":
        if data_a_b[0] == higher_data:
            data_a = higher_data
            data_a_b.pop(1)
            count += 1
        elif data_a_b[0] != higher_data:
            print(f"Sorry, that's wrong. Final score: {count}")
            strike -= 1
    elif choice == "b":
        if data_a_b[1] == higher_data:
            data_a = higher_data
            data_a_b.pop(0)
            count += 1
        elif data_a_b[1] != higher_data:
            print(f"Sorry, that's wrong. Final score: {count}")
            strike -= 1