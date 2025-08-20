# Data Input (input):

x = input("Enter the first number: \n")
y = input("Enter the second number:")
print(x + y)
print(type(x + y))

# All data received from the user is str. Don't forget to convert them when necessary.


# Data Conversion:

total = int(x) + int(y)
print(total)
print(type(total))

# This conversion can be done for str, float, int and bool.

a = 2.5
a = int(a)
print(a)

k = float(input("Enter a number: "))
print("NUMBER : ", int(k))


# CIRCLE CALCULATIONS:

pi = 3.14
r = float(input("Enter the radius: \n"))
area = pi * (r ** 2)
circumference = 2 * pi * r
print("Before rounding: ", circumference)
circumference = round(circumference, 3) # number round
print("Area \n " + str(area) +"\n" + "Circumference \n" +str(circumference))


# Escape Characters:

"""
\n (New Line) → Moves to the next line.

\t (Tab) → Leaves a space, indents by one tab.

\\ (Backslash) → Allows us to write the \ character as a normal character.

\' (Single Quote) → Allows us to use a single quote (') inside a string with single quotes.

\" (Double Quote) → Allows us to use double quotes (") inside a string with double quotes.

\b (Backspace) → Deletes the previous character.

"""


