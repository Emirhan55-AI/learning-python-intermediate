numbers = [1, 3, 5, 7, 9, 12, 21]

# 1. Example → Print numbers divisible by 3
'''
for num in numbers:
    if num % 3 == 0:
        print(num)
'''

# 2. Example → Sum all numbers
'''
total = 0
for num in numbers:
    total += num
print(total)
'''

# 3. Example → Square numbers divisible by 3
'''
for num in numbers:
    if num % 3 == 0:
        num = num ** 2
        print(num)
'''

# 4. Example → Print city names with 5 or fewer characters
'''
cities = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']
for city in cities:
    if len(city) <= 5:
        print(city)
'''

# 5. Example → List of products with prices
products = [
    {'name': 'Samsung S6', 'price': '3000'},
    {'name': 'Samsung S7', 'price': '4000'},
    {'name': 'Samsung S8', 'price': '5000'},
    {'name': 'Samsung S9', 'price': '6000'},
    {'name': 'Samsung S10', 'price': '7000'}
]

# Calculate the total price of all products
total_price = 0
for product in products:
    price = int(product['price'])
    total_price += price
print('Total price of all products:', total_price)

# Show products with price less than or equal to 5000
for product in products:
    if int(product['price']) <= 5000:
        print(product['name'])
