# =============================================
# 1- Factorial function: Handles invalid inputs 
# and calculates the result for valid ones
# =============================================

def factorial(x):
    # Try to convert input to an integer
    x = int(x)

    # Raise an error if the number is negative
    if x < 0:
        raise ValueError("Negative value is not allowed")

    # Factorial calculation
    result = 1
    for i in range(1, x + 1):
        result *= i

    return result


# Testing the factorial function
# Every element in the list will be tested
for i in [3, 6, 7, '2a', -1, -7, 9]:
    try:
        x = factorial(i)  # Calculate factorial
    except ValueError as e:
        # Handle negative numbers or invalid inputs
        print(f"Error: {e}")
        continue
    except Exception as e:
        # Handle all other possible errors (like '2a')
        print(f"General error: {e}")
        continue
    else:
        # If no error, print the result
        print(f"Factorial of {i} is: {x}")


# =============================================
# 2- Password check: Ensures no Turkish characters are used
# =============================================

def passwordCheck(password):
    # Define Turkish-specific characters
    turkish_chars = "şçğüöıİ"

    # Check each character in the password
    for i in password:
        if i in turkish_chars:
            # Raise an error if a Turkish character is found
            raise TypeError("Password cannot contain Turkish characters")
    
    # If no errors, the password is valid
    print("Valid password")


# Get password from user
password = input("Enter password: ")

# Try password validation with error handling
try:
    passwordCheck(password)
except TypeError as e:
    # If the password contains Turkish characters, show error message
    print(f"Error: {e}")
