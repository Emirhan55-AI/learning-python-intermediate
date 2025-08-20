# ======================
# Program that takes two numbers from the user and performs division
# Provides appropriate error messages for invalid inputs.
# ======================

try:
    # Get two integer inputs from the user
    x = int(input("x: "))
    y = int(input("y: "))

    # Perform division with the given numbers
    print(x / y)

# This block executes if y is entered as zero
except ZeroDivisionError:
    print("Error: y cannot be zero")

# This block executes if the user enters letters or symbols instead of valid integers
except ValueError:
    print("Error: x and y must be integers")

# Any other unexpected error will be caught here
except:
    print("An unknown error occurred")


# ======================
# Handling multiple exceptions in the same block
# ======================

try:
    x = int(input("x: "))
    y = int(input("y: "))

    print(x / y)

# Both ZeroDivisionError and ValueError are handled in the same block
except (ZeroDivisionError, ValueError) as e:
    print("Error: x and y must be numbers. Also, y cannot be zero.")
    print("Detailed error message:", e)

# If another type of error occurs, it will be caught here
except:
    print("An unknown error occurred")


# ======================
# Using the base Exception class
# ======================

try:
    x = int(input("x: "))
    y = int(input("y: "))

    print(x / y)

# The Exception class is the parent of all built-in exceptions.
# No matter what type of error occurs, this block will catch it and assign it to variable `e`.
except Exception as e:
    print("An unknown error occurred")
    print("Details:", e)  # Provides the system-generated description of the error.


# ======================
# Loop until valid input is provided
# ======================

# This program keeps asking for input until the user enters valid numbers.
# Errors are handled specifically, and the finally block always runs.

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))

        print(x / y)

    # Catch ZeroDivisionError or ValueError
    except (ZeroDivisionError, ValueError) as e:
        print("x and y must be valid numbers. Also, y cannot be zero.")
        print("Details:", e)

    # Catch any other unknown errors
    except Exception as e:
        print("An unknown error occurred.")
        print("Details:", e)

    # This block runs if no exception was raised in try
    # Means valid input was provided, so the loop will break
    else:
        break

    # This block always runs regardless of error or not
    # Typically used for cleanup, releasing resources, etc.
    finally:
        print("Finally block executed.\n")
