# x = 5
# y = 10
# z = 20

# x, y, z = 5, 16, 20

# a, b, c = 10, 20, (30, 40)   # c is a tuple containing 30 and 40

# d = 10, 20   # d is also a tuple

# x, y = y, x  # swap values
# x += 5       # x = x + 5
# x -= 5       # x = x - 5
# x *= 5       # x = x * 5
# x /= 5       # x = x / 5
# x %= 5       # x = x % 5
# y //= 5      # y = y // 5 (floor division)
# y **= z      # y = y ** z (exponentiation)


values = 1, 2, 3, 4, 5  
# If we did not put * in front of z below, 
# it would give an error because there would be extra values.
# The * collects the remaining values into a list.

print(values)
print(type(values))

x, y, *z = values  # Unpack the first two values into x and y, rest into list z

print(x, y, z)
print(x, y, z[1])

