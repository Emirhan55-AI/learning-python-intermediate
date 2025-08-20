# Identity Operator: is

# x = y = [1, 2, 3]
# z = y

# print(x == y)  # True → checks if the values are the same
# print(x == z)  # True
# print(x is y)  # True → because both point to the same object
# print(x is z)  # True

x = [1, 2, 3]
y = [2, 4]

del x[2]       # removes the element at index 2 from list x → x becomes [1, 2]
y[1] = 1       # changes index 1 of list y → y becomes [2, 1]
y.reverse()    # reverses list y → y becomes [1, 2]

print(x == y)       # True → lists have the same values in the same order
print(x is y)       # False → they are different objects in memory
print(x is not y)   # True → they are not the same object

# Membership Operator: in

x = ['apple', 'banana']
print('banana' in x)  # True → 'banana' is in the list

name = 'Ahmet'
print('a' in name)        # False → lowercase 'a' is not in 'Ahmet'
print('a' not in name)    # True → lowercase 'a' is indeed not in 'Ahmet'
