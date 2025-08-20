# break → completely exits the loop
# continue → skips the current loop iteration and continues with the next one

# name = 'Emirhan Uysal'

# for letter in name:
#     if letter == 'i':
#         continue  # try replacing with break to see the difference
#     print(letter)

# x = 0

# while x < 5:
#     x += 1  # if this was placed at the end, it would get stuck at 2
#     if x == 2:
#         continue
#     print(x)

# 1 - Sum of odd numbers up to 100
x = 0
result = 0

while x <= 100:
    x += 1
    if x % 2 == 0:  # skip even numbers
        continue
    result += x

print(f'Total sum: {result}')
