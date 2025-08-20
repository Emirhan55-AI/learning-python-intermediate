# The for loop is used in lists.

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

for a in numbers: # The loop will run as many times as there are elements in numbers.
    print("Hello")



names = ['Emirhan', 'Ömer', 'Zeyd']
for name in names:
    print(f'My name is {name}')


namess = 'Emirhan Uysal'
for n in namess:
    print(n)  # String expressions are lists. Therefore, write each one individually.


tuple = [(1, 2, 3, 4), (1, 2, 3), (1, 2), (5, 6, 7, 8, 9)]
for t in tuple:
    print(t)


tuple2 = [(1, 2, 3), (1, 2, 3), (1, 2, 4), (5, 6, 7)]
for a, b, c in tuple2:
    print(a, b, c)
    print(a, b)
    print(a)


d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print(item)  # only keys are printed
for item in d.items():
    print(item)
for key, value in d.items():
    print(key)
    print(value)
    print(key, value)


for item in d.values():
    print(item)
for item in d.keys():
    print(item)