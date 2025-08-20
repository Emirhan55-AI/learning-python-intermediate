# Value Type parameter

def changeName(n):
    n = "Ahmet"
    print(n)

name = "Emirhan"
changeName(name)
print(name)

# Reference Type

def change(n):
    n[0] = "Istanbul"

lists = ["Ankara", "Izmir"]
change(lists)
print(lists)

"""
The difference between these two code blocks is whether the parameter is handled
as a value type or a reference type. In Python, variables behave differently
depending on whether their data type is immutable or mutable.

Here, 'name' is a string. In Python, strings are immutable.
Inside changeName, the value of 'name' is copied into 'n'.
The assignment n = "Ahmet" creates a new string for the local variable 'n'.
It does NOT affect the original 'name' outside the function.
Value-type-like behavior: the function works with a copy of the value.

Here, 'lists' is a list. Lists in Python are mutable.
When we pass 'lists' to change, a reference to the same list object is passed.
The statement n[0] = "Istanbul" modifies the first element of the SAME list.
Therefore, the original 'lists' is also changed.
Reference-type-like behavior: the function modifies the original object.
"""

# Example 1

def add(a, b):
    return sum((a, b))

total = add(100, 125)
print(total)


# Example 2

def add(a, b, c=0, d=0, e=0):  # Defaults let you call with only a and b if you want.
    return sum((a, b, c, d, e))

total = add(100, 125)
print(total)
total2 = add(102, 149, 2.5)
print(total2)  # Even without d and e, the sum works thanks to defaults.


# Example 3: When there are many parameters, use *args (tuple via *)

def add(*args):
    return sum(args)

total3 = add(10, 20, -9, 2.89, 149, 100000, 54545754)
print(total3)


# Example 4: For dictionary-like arguments, use ** (keyword args -> dict)

def displayUser(**kwargs):
    for key, value in kwargs.items():
        print('{} is {}'.format(key, value))

displayUser(name="Emirhan", age=21, city="Bursa")
displayUser(name="Mehmet", age=24, city="Kocaeli", phone="2112314234")
displayUser(name="Ahmet", age=49, city="Mardin", phone="241848722", email="ahmetmardinli@gmail.com")


# Example 5

def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(100, 200, 300, 40, 50, key1='value1', key2='value2')
