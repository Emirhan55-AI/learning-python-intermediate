x, y, z = 2, 5, 10

# 1 - What is the difference between the product of 2 numbers entered by the user 

#     and the sum of x, y, z?

# a = int(input('First number: '))
# b = int(input('Second number: '))
# result = (a * b) - (x + y + z)

# 2 - Calculate y divided by x without remainder (integer division).

result = y // x

# 3 - What is the sum of (x, y, z) mod 3?

total = (x + y + z)
result = total % 3

# 4 - Calculate y to the power of x.

result = y ** x

# 5 - According to x, *y, z = numbers, what is the cube of z?

numbers = 1, 5, 7, 10, 6
x, *y, z = numbers  # y corresponds to [5, 7, 10] and z corresponds to 6
result = z ** 3

# 6 - According to x, *y, z = numbers, what is the sum of the values of y?

numbers = 1, 5, 7, 10, 6
x, *y, z = numbers

result = y[0] + y[1] + y[2]

print(result)
