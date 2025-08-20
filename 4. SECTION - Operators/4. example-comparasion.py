# 1 - Which of the 2 entered numbers is greater?

# a = int(input('a: '))
# b = int(input('b: '))

# result = (a > b)
# print(f'a: {a} is greater than b: {b} → {result}')

# 2 - Get 2 midterm exam grades (60%) and 1 final exam grade (40%) from the user, 
# calculate the average. If the average is 50 or above, print "Passed", otherwise "Failed".

# midterm1 = float(input('1st midterm: '))
# midterm2 = float(input('2nd midterm: '))
# final = float(input('Final exam: '))

# average = (((midterm1 + midterm2) / 2) * 0.6) + (final * 0.4)

# print(f'Your average: {average} → Passed: {average >= 50}')

# 3 - Check whether an entered number is even or odd.

# number = int(input('Number: '))
# isEven = (number % 2 == 0)
# print(f'The entered number is even: {isEven}')

# 4 - Check whether an entered number is positive or negative.

# number = int(input('Number: '))
# isPositive = (number > 0)
# print(f'The entered number is positive: {isPositive}')

# 5 - Ask for email and password, then verify their correctness.

#     (email: email@emirhan.com, password: abc123)

email = 'email@emirhan.com'
password = 'abc123'

enteredEmail = input('Email: ')
enteredPassword = input('Password: ')

isEmail = (email == enteredEmail.lower().strip())
isPassword = (password == enteredPassword.lower())

print(f'Is email correct: {isEmail} and is password correct: {isPassword}')
