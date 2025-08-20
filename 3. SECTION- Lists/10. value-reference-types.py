# -------------------------------
# VALUE TYPES
# int, float, string, bool → store the value directly inside the variable.
# -------------------------------

x = 5      # x stores the value 5 directly in memory
y = 25     # y stores the value 25 directly in memory

x = y      # copies the value of y into x (x is now 25)
y = 10     # changes y only; x is not affected

print(x, y)  # OUTPUT: 25 10
# In value types, each variable has its own independent memory address and value.


# -------------------------------
# REFERENCE TYPES
# list, dict, class → store the memory address of the actual object.
# -------------------------------

A = ["orange", "apple", "banana"]  # Creates a list in memory; A stores its address
B = ["orange", "apple", "banana"]  # Creates another list at a different address

A = B      # Now A and B point to the SAME address (address is copied)
B[0] = "grape"  # Changing B also changes A because they share the same list in memory

print(A, B)  # OUTPUT: ['grape', 'apple', 'banana'] ['grape', 'apple', 'banana']
# Both variables point to the same list; any change via one affects the other.


# -------------------------------
# VALUE TYPES EXAMPLE AGAIN
# -------------------------------
x = 10
y = 20
x = y   # Copies the value (20) into x
y = 30  # Changing y does not affect x
print(x, y)  # OUTPUT: 20 30


# -------------------------------
# REFERENCE TYPES EXAMPLE AGAIN
# -------------------------------
a = ["apple", "pear"]  # Creates a list in memory
b = ["apple", "pear"]  # Creates another list at a different memory location

a = b  # Address is copied → a and b now point to the same list
a[0] = "grape"  # Changing a also changes b
print(a, b)  # OUTPUT: ['grape', 'pear'] ['grape', 'pear']


# -------------------------------
# COPYING A LIST (Independent Address)
# -------------------------------
listeA = [10, 20]          # A list in memory
# listeB = listeA.copy()   # Method 1: copy() method
listeB = list(listeA)      # Method 2: list() constructor

listeB[0] = 30  # Change in listeB will NOT affect listeA

print(listeA, listeB)  # OUTPUT: [10, 20] [30, 20]
# Now they are completely independent lists (different addresses).


# -------------------------------
# CHECKING MEMORY ADDRESSES (id() function)
# id() → returns the memory address of a variable's object
# -------------------------------
print("A address:", id(A))
print("B address:", id(B))
print("listeA address:", id(listeA))
print("listeB address:", id(listeB))
