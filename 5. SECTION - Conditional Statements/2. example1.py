# 1 - Ask the user for their name, age, and education level, 
#     then check if they are eligible for a driving license.
#     Conditions: at least 18 years old AND education level must be "high school" or "university".

# name = input('Your name: ')
# age = int(input('Your age: '))
# education = input('Your education level: ')

# if age >= 18:
#     if education == 'high school' or education == 'university':
#         print(f'{name}, you are eligible for a driving license.')
#     else:
#         print(f'{name}, you cannot get a driving license. Education level is insufficient.')
# else:
#     print(f'{name}, you cannot get a driving license. You are underage.')

# 2 - Get a student's 2 written exam grades and 1 oral grade,
#     then calculate the average and print the corresponding grade:
#     0 - 24  => 0
#     25 - 44 => 1
#     45 - 54 => 2
#     55 - 69 => 3
#     70 - 84 => 4
#     85 -100 => 5

# written1 = float(input('1st written exam: '))
# written2 = float(input('2nd written exam: '))
# oral = float(input('Oral exam: '))

# average = (written1 + written2 + oral) / 3

# if 0 <= average < 25:
#     print(f'Your average: {average} → Grade: 0')
# elif 25 <= average < 45:
#     print(f'Your average: {average} → Grade: 1')
# elif 45 <= average < 55:
#     print(f'Your average: {average} → Grade: 2')
# elif 55 <= average < 70:
#     print(f'Your average: {average} → Grade: 3')
# elif 70 <= average < 85:
#     print(f'Your average: {average} → Grade: 4')
# elif 85 <= average <= 100:
#     print(f'Your average: {average} → Grade: 5')
# else:
#     print('Invalid input.')

# 3 - Based on the date a vehicle was first registered,
#     calculate its service schedule:
#     1st Service => within 1 year
#     2nd Service => within 2 years
#     3rd Service => within 3 years
#     ** Calculate based on days using datetime module.

import datetime

date_input = input('Enter the date your vehicle was registered (YYYY/MM/DD): ')
date_parts = date_input.split('/')
registration_date = datetime.datetime(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
now = datetime.datetime.now()
difference = now - registration_date
days = difference.days

if days <= 365:
    print('1st service period')
elif 365 < days <= 365 * 2:
    print('2nd service period')
elif 365 * 2 < days <= 365 * 3:
    print('3rd service period')
else:
    print('Invalid time period.')
# Note: The datetime module is used to handle date and time operations.