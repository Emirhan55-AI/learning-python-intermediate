# username, password => database values

# Example: 'emirhanuysl' , '123456'

a, b, c, d = 5, 5, 10, 4

password = '1234'
username = 'emirhanuysl'

result = (a == b) # True
result = (a == c) # False
result = ('emirhan' == username) # False
result = ('emirhanuysl' == username) # True
result = (password == input("Password: ")) # Check if input matches stored password
result = (a != b) # False
result = (a != c) # True
result = (a > c) # False
result = (a < c) # True
result = (a >= b) # True
result = (c <= b) # False
result = (True == 1) # True (in Python, True is 1)
result = (False == 0) # True (in Python, False is 0)
result = False + True + 40 # 0 + 1 + 40 = 41

print(result)
