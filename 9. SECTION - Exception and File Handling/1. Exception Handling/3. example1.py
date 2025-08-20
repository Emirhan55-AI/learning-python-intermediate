# =============================================
# 1. Find numeric values inside list elements
# =============================================

liste = ["1", "3", "5", "20b", "abc", "10a", "60"]

print("Elements that can be converted to numeric values:")
for x in liste:
    try:
        # If x can be converted into a number, print it
        result = int(x)
        print(result)
    except ValueError:
        # Skip elements that cannot be converted
        continue


# =============================================
# 2. Get a valid number from the user
# =============================================

print("\nGetting a number from the user (exit with 'q'):")
while True:
    number = input("Enter a number (or 'q' to quit): ")

    # Exit condition
    if number.lower() == "q":
        break

    try:
        # Try converting the input to a number
        result = float(number)
        print(f"Entered number: {result}")
        break
    except ValueError:
        # Show a warning message for invalid inputs
        print("Invalid number, please try again.")
        continue


# =============================================
# 3. Safe dictionary key access function
# =============================================

product = {"productName": "Samsung S20", "price": 10000}

# Function for safely retrieving data from a dictionary by key
def get(dictionary, key):
    try:
        # If the key exists, return its value
        return dictionary[key]
    except KeyError:
        # If the key does not exist, return None
        return None

# Function tests
print("\nDictionary queries:")
print("price:", get(product, "price"))          # Output: 10000
print("productName:", get(product, "productName"))  # Output: Samsung S20
print("color:", get(product, "color"))          # Output: None
