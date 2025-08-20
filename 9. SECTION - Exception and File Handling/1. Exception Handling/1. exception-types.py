# ======================
# ZeroDivisionError
# ======================
# Division by zero error. It is an undefined mathematical operation.
x = 10
# print(x / 0)  # ZeroDivisionError: division by zero

# ======================
# ValueError
# ======================
# Occurs when an invalid value is used.
# For example, trying to convert a string into a number when it is not numeric.
# int("hello")  # ValueError: invalid literal for int()

# ======================
# SyntaxError
# ======================
# Syntax errors. They occur when there is a mistake in the code’s syntax.
# Example:
# def intro((:      # SyntaxError: invalid syntax
#     pass
# abcdef;;          # SyntaxError: invalid syntax

# ======================
# NameError
# ======================
# Occurs when a variable is used without being defined.
# print(name)  # NameError: name 'name' is not defined

# ======================
# TypeError
# ======================
# Occurs when an operation is applied to an object of inappropriate type.
# len(10)        # TypeError: object of type 'int' has no len()
# 10 + 'a'       # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ======================
# IndexError
# ======================
# Occurs when trying to access an invalid index in a sequence like a list.
my_list = [10]
# print(my_list[1])  # IndexError: list index out of range

# ======================
# KeyError
# ======================
# Occurs when trying to access a dictionary with a key that does not exist.
a = {"name": "Emirhan"}
# print(a["age"])  # KeyError: 'age'

# ======================
# AttributeError
# ======================
# Occurs when trying to call an attribute or method that does not exist in an object.
s = "hello"
# print(s.Upper())  # AttributeError: 'str' object has no attribute 'Upper'
# Correct usage:
print(s.upper())    # "HELLO"

