# while is used for conditional loops.

# Infinite loop example
# x = 0
# while True:
#     print(x)

# Numbers from 0 to 99
x = 0
while x < 100:
    print(x)  # printing before increment includes 0
    x += 1

# Print even and odd numbers from 0 to 100
t = 0
while t <= 100:
    if t % 2 == 0:
        print(f'{t} is even.')
    else:
        print(f'{t} is odd.')
    t += 1

# Keep asking for the user's name until they enter it
name = ''  # This is equivalent to a False value
while not name.strip():  # not name means True if it's empty
    name = input("Enter your name: ")
    print(f'Welcome {name}')
