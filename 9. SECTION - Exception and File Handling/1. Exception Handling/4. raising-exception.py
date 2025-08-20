# Define a function to print text in a given color
def colorize(text, color):
    # List of valid colors
    valid_colors = ("blue", "red", "white", "black", "orange")

    # If 'text' is not a string, raise a TypeError
    if type(text) is not str:
        raise TypeError("text must be of type str.")

    # If 'color' is not a string, raise a TypeError
    if type(color) is not str:
        raise TypeError("color must be of type str.")

    # If 'color' is not in the list of valid colors, raise a ValueError
    if color not in valid_colors:
        raise ValueError("invalid color")

    # If all checks pass, print the text with the color
    print(f'"{text}" has been written in {color}.')


# Use a try-except block to catch possible errors when testing the function
try:
    # First call is valid, no error will be raised
    colorize("hello", "red")

    # Second call uses an invalid color, this will raise a ValueError
    colorize("hi", "green")

# Catch either TypeError or ValueError
except (TypeError, ValueError) as ex:
    # Print the error message
    print(ex)
