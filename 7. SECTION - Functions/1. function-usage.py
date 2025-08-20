# Function Usage 1

def sayHello():
    print("Hello")
    
sayHello()
sayHello()

for i in range(10):
    sayHello()  # If you define this loop inside the function, it will be even easier to reuse.


# Function Usage 2: Returning a value from a function

# If a function does not use 'return', it can only display output,
# but you cannot assign that result to a variable or use it elsewhere.
# The moment Python reaches 'return', the function stops running — nothing after it will run.
# If you don’t use return (or just write return without a value),
# the function returns 'None'.
# If you want to use the result somewhere else, you must use 'return'.

def sum_numbers():
    return 10 + 20

result = sum_numbers()  # Just calling it without assigning does nothing here.
print(result)


# Function Usage 3: Sending parameters to a function

def sayHello2(name):
    print("Hello " + name)
    
sayHello2("Emirhan")


# Function Usage 4

def total(num1, num2):
    return num1 + num2

total_sum = total(20, 30)
print(total_sum)


# Function Usage 5

def calculate_age(birth_year):
    return 2026 - birth_year

age_emir = calculate_age(1999)
print(age_emir)


# Function Usage 6: Using one function inside another

def years_until_retirement(birth_year, name):
    age = calculate_age(birth_year)
    retirement = 65 - age
    
    if retirement > 0:
        print(f"{name}, you have {retirement} years until retirement.")
    else:
        print(f"{name}, you are already retired.")

ret1 = years_until_retirement(1999, "Emirhan")
ret2 = years_until_retirement(1920, "Ali")
print(ret1)
print(ret2)


# Function Usage 7: Giving information about the function to the user (docstring)

def years_until_retirement(birth_year):
    '''
    Description: Calculates how many years until retirement based on birth year.
    Input: Birth year
    Output: Years left until retirement
    '''
    age = calculate_age(birth_year)
    retirement = 65 - age
    
    if retirement > 0:
        print(f"You have {retirement} years until retirement.")
    else:
        print("You are already retired.")

print(help(years_until_retirement))


# Function Usage 8: Default parameter

def sayHello3(name= "User"):
    print("Hello " + name)

sayHello3()  # If no parameter is given, it will use 'User' by default.

def greeting(name= "User", greetings= "Welcome"):
    return name + " " + greetings

result = greeting()
print(result)
result2 = greeting("Emirhan")
print(result2)
result3 = greeting("Emirhan", "Hello")
print(result3)


# Function Usage 9

def power(base, exponent=2):  # Default parameters cannot be on the left.
    return base ** exponent

result = power(2, 3)
result = power(5)


# Function Usage 10: Passing a function as a reference (function as argument)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def operation(a, b, fn=add):
    return fn(a, b)

result = operation(10, 20)
print(result)

# Here, 'fn' is a reference to a function.
# Without the default, we would have to write operation(10,20,add) or operation(10,20,subtract).
# By setting a default to 'add', we can just call operation(10,20).


# Function Usage 11: Keyword arguments

def full_name(firstname: str, lastname: str, age: int = 0) -> str:
    return f"Your name is {firstname} {lastname}"

result = full_name("Emirhan", "Uysal")
result = full_name(lastname="Uysal", firstname="Emirhan")
result = full_name(firstname="Emirhan", lastname="Uysal")

print(result)

"""
Keyword arguments let you pass parameters to a function using their names.

Advantages:
1. Removes the need to follow the exact order of parameters.
   Example: full_name(lastname="Uysal", firstname="Emirhan")
2. Improves code readability.
   Example: full_name(firstname="Emirhan", lastname="Uysal") is clearer than full_name("Emirhan", "Uysal").
3. Works well with optional parameters that have default values.
   You can pass only the ones you need.
"""
