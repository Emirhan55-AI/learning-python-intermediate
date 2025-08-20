username = "Emirhan"
password = 12345
password = str(password)

username2 = input("Enter your username: \n")
password2 = input("Enter your password: \n")

'''
# First Example
if username == username2 and password == password2: 
    print(f'Welcome Mr. {username} -> Your password: {password}')
else: 
    print("Incorrect information!")
'''

# Second Example (nested if)

if username == username2:
    if password == password2:
        print("Welcome!")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# elif usage example

# x = int(input('x: '))
# y = int(input('y: '))

# if x > y:
#     print('x is greater than y')
# elif x == y:
#     print('x is equal to y')
# else:
#     print('y is greater than x')

num = int(input('Number: '))

if num > 0:
    print('The number is positive')
elif num < 0:
    print('The number is negative')
else:
    print('The number is zero')
