'''
1- Check if the entered number is between 0 and 100.

number = float(input('Number: '))

if (number > 0) and (number <= 100):
    print('The number is between 0 and 100.')
else:
    print('The number is NOT between 0 and 100.')
'''

'''
2- Check if the entered number is a positive even number.

number = int(input('Number: '))

if (number > 0):
    if (number % 2 == 0):
        print('The entered number is a positive even number.')
    else:
        print('The entered number is positive but odd.')
else:
    print('The entered number is negative.')
'''

'''
3- Login control with email and password.

email = 'email@sadikturan.com'
password = 'abc123'

enteredEmail = input('Email: ')
enteredPassword = input('Password: ')

if (enteredEmail == email):
    if (enteredPassword == password): 
        print('Login successful.')
    else:
        print('Incorrect password.')
else:
    print('Incorrect email address.')
'''

'''
4- Compare 3 entered numbers to find which is the largest.

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if (a > b) and (a > c):
    print('a is the largest number.')
elif (b > a) and (b > c):
    print('b is the largest number.')
elif (c > a) and (c > b):
    print('c is the largest number.')
'''

'''
5- Get 2 midterm grades (60%) and a final grade (40%) from the user, 
   then calculate the average. 
   If the average is 50 or above → pass, otherwise → fail.
   a) Even if the average is 50, the final grade must be at least 50.
   b) If the final grade is 70 or above, pass regardless of the average.

midterm1 = float(input('Midterm 1: '))
midterm2 = float(input('Midterm 2: '))
final = float(input('Final: '))

average = ((midterm1 + midterm2) / 2) * 0.6 + (final * 0.4)

result = (average >= 50) and (final >= 50)
result = (average >= 50) or (final >= 70)

# Case 1
if (average >= 50):
    if (final >= 50):  
        print(f'Student average: {average} → Passed')
    else:
        print(f'Student average: {average} → Failed. You must score at least 50 in the final.')
else:
    print(f'Student average: {average} → Failed')

# Case 2
if (average >= 50):
    print(f'Student average: {average} → Passed')
else:
    if (final >= 70):
        print(f'Student average: {average} → Passed (Final score 70+ overrides average).')
    else:
        print(f'Student average: {average} → Failed')
'''

'''
6- Get the person's name, weight, and height, then calculate their BMI.
   Formula: (Weight / height squared)
   According to the table, determine the BMI category:
   0-18.4    => Underweight 
   18.5-24.9 => Normal  
   25.0-29.9 => Overweight
   30.0-34.9 => Obese

name = input('Your name: ')
weight = float(input('Your weight (kg): '))
height = float(input('Your height (m): '))

bmi = weight / (height ** 2)

if (bmi >= 0) and (bmi <= 18.4):
    print(f'{name}, your BMI is: {bmi} → Underweight')
elif (bmi > 18.4) and (bmi <= 24.9):
    print(f'{name}, your BMI is: {bmi} → Normal')
elif (bmi > 24.9) and (bmi <= 29.9):
    print(f'{name}, your BMI is: {bmi} → Overweight')
elif (bmi >= 29.9) and (bmi <= 45.9):
    print(f'{name}, your BMI is: {bmi} → Obese')
else:
    print('Invalid data entered.')
'''
