import random

value = random.random()
print(value)        # A value between 0 and 1

value = random.uniform(1, 10)
print(value)        # A floating point bvalue between 1 and 10

value = random.randint(1, 6)
print(value)        # A random integer between 1 and 6, In this case simulate a roll of a dice

value = random.randint(0, 1)
print(value)        # A random integer between 1 and 0, In this case simulate a flip of a coin

people = ['a','b','c'] #A list of students in the class
choice = random.choice(people)
print(choice, "will answer the next question")        # Choose one person from the list randomly

# Choose from a list of foods to pack for an outing
foods = ['WaiWai', 'Can of Coke', 'Biscuit', 'Water', 'A Fruit', 'Snickers']
outing_choices = random.choices(foods, k=10)
print(outing_choices)

# Choose from the list of foods to pack for an outing, proritize healthier options
healthy_outing_choices = random.choices(foods, weights=[4, 2, 8, 10, 10, 9], k=10)
print(healthy_outing_choices)

# Simulate shuffling a deck of cards
deck = list(range(1,53))
print(deck)
random.shuffle(deck)
print(deck)

# Pick a sample of random cards(k=5) from the deck
haat = random.sample(deck, k=5)
print(haat)


# Simulate a game of cards and distribute cards to a group of players, 
# include rank and suits


