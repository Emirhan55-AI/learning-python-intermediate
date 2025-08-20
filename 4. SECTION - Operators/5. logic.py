x = 5

right = 0
go_on = 'e'

result = 5 < x < 10

# and

# True, True => True
# True, False => False


result = (x > 5) and (x < 10)  
result = (right > 0) and (go_on == 'e') 

# or

result = (x > 0) or (x % 2 == 0)

# True, False => True
# True, True => True
# False, False => False

# not

result = not(x > 0)

# Is x an even number between 5 and 10?

result = ((x>5) and (x<10)) and (x%2==0)

print(result)

