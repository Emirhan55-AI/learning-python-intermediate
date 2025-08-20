import random

"""
result = dir(random)  # Lists all available functions inside the random module.
result = help(random)  # Shows documentation for the random module.
"""

"""
result = random.random()  # Generates a random float between 0 and 1.
result = random.random() * 100  # Generates a random float between 0 and 100.
result = random.randint(1, 100)  # Generates a random integer between 1 and 100.
result = random.uniform(10, 120)  # Generates a random float between 10 and 120.
print(result)
"""

"""
names = ["ahmet", "mehmet", "zübeyir"]
result = names[random.randint(0, len(names) - 1)]  # Picks a random element manually.
result = random.choice(names)  # Easier way to pick a random element from the list.
greetings = "hello there"
result = random.choice(greetings)  # Picks a random character from the string.
print(result)
"""

# Create a list of numbers from 0 to 9
liste = list(range(10))  
shuffles = random.shuffle(liste)  # Shuffles the elements randomly in the list.

# Select random samples
liste = range(100)
result = random.sample(liste, 3)  # Selects 3 random numbers from the list.

names = ["ahmet", "mehmet", "zübeyir"]
result = random.sample(names, 2)  # Selects 2 random names from the list.
print(result)
