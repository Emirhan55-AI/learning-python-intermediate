# 1 - Check if the entered number is between 0 and 100.

# number = float(input('Number: '))
# result = (number > 0) and (number <= 100)
# print(f'Is the number between 0 and 100: {result}')

# 2 - Check if the entered number is a positive even number.

# number = int(input('Number: '))
# result = (number > 0) and (number % 2 == 0)
# print(f'Is the entered number a positive even number: {result}')

# 3 - Login control using email and password.

# email = 'email@sadikturan.com'
# password = 'abc123'

# enteredEmail = input('Email: ')
# enteredPassword = input('Password: ')

# result = (enteredEmail == email) and (enteredPassword == password)
# print(f'Is login successful: {result}')

# 4 - Compare 3 entered numbers to determine which is the largest.

# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# result = (a > b) and (a > c)
# print(f'a is the largest number: {result}')

# result = (b > a) and (b > c)
# print(f'b is the largest number: {result}')

# result = (c > a) and (c > b)
# print(f'c is the largest number: {result}')

# 5 - Get 2 midterm grades (60%) and a final grade (40%) from the user, then calculate the average.

# If the average is 50 or above → Pass, otherwise → Fail.
# a) Even if the average is 50, the final grade must be at least 50.
# b) If the final grade is 70 or above, pass regardless of the average.

# midterm1 = float(input('Midterm 1: '))
# midterm2 = float(input('Midterm 2: '))
# final = float(input('Final exam: '))

# average = ((midterm1 + midterm2) / 2) * 0.6 + (final * 0.4)
# result = (average >= 50) and (final >= 50)
# result = (average >= 50) or (final >= 70)

# print(f'Student average: {average} → Pass status: {result}')

# 6 - Get a person’s name, weight, and height, then calculate their BMI (Body Mass Index).
#     Formula: (Weight / height squared)
#     Classify the BMI according to the table:
#     0 - 18.4   => Underweight
#     18.5-24.9  => Normal
#     25.0-29.9  => Overweight
#     30.0-34.9  => Obese

name = input('Your name: ')
weight = float(input('Your weight (kg): '))
height = float(input('Your height (meters): '))

bmi = weight / (height ** 2)

underweight = (bmi >= 0) and (bmi <= 18.4)
normal = (bmi > 18.4) and (bmi <= 24.9)
overweight = (bmi > 24.9) and (bmi <= 29.9)
obese = (bmi >= 29.9) and (bmi <= 34.9)

print(f'{name}, your BMI is: {bmi} → Underweight: {underweight}')
print(f'{name}, your BMI is: {bmi} → Normal: {normal}')
print(f'{name}, your BMI is: {bmi} → Overweight: {overweight}')
print(f'{name}, your BMI is: {bmi} → Obese: {obese}')
