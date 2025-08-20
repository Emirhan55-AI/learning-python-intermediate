'''
    students = {
        '120': {
            'name': 'Ali',
            'surname': 'Yılmaz',
            'phone': '532 000 00 01'
        },
        '125': {
            'name': 'Can',
            'surname': 'Korkmaz',
            'phone': '532 000 00 02'
        },
        '128': {
            'name': 'Volkan',
            'surname': 'Yükselen',
            'phone': '532 000 00 03'
        },
    }

    1- Store the information provided by the user about the students in the dictionary.

    2- Show the relevant student information by getting the student number from the user.
    
'''

students = {}

number = input("students no: ")
name = input("students name: ")
surname = input("students surname: ")
phone = input("students phone: ")

# students[number] = {
#     'name': name,
#     'surname': surname,
#     'phone': phone
# }

students.update({
    number: {
        'name': name,
        'surname': surname,
        'phone': phone
    }
})

number = input("students no: ")
name = input("students name: ")
surname = input("students surname: ")
phone = input("students phone: ")

students.update({
    number: {
        'name': name,
        'surname': surname,
        'phone': phone
    }
})

number = input("students no: ")
name = input("students name: ")
surname = input("students surname: ")
phone = input("students phone: ")

students.update({
    number: {
        'name': name,
        'surname': surname,
        'phone': phone
    }
})

print('*' * 50)

studentsNo = input('students no: ')
student = students[studentsNo]
print(student)

print(f"Search {studentsNo} numbers of student: {student['name']} surname: {student['surname']} and phone is {student['phone']}")