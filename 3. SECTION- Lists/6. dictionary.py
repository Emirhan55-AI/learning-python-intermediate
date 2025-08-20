# key - value: A key-value pair is required to access information. It is sortable, updatable, and non-repeatable.

# plates = { 'kocaeli' : 41, 'istanbul': 34 }
# print(plates['kocaeli']) --> 41
# print(plates['istanbul']) --> 34


# plates['ankara'] = 6 --> add data
# plates['kocaeli'] = 19 --> update data


# print(plates)



users = {
    'emirhanuysal': {
        'age': 36,        
        'roles': ['user'],
        'email': 'emirhan@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    },
    'ahmetyilmaz': {
        'age': 2,
        'roles': ['admin','user'],
        'email': 'ahmet@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    }
}

print(users['ahmetyilmaz']['roles'][0])

