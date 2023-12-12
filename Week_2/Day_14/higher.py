import random
from game_data import data

data_c = []

data_a = random.choice(data)
data_b = random.choice(data)

data_c.append(data_a)

print(data_c)