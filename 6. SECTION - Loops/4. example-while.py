numbers = [1, 3, 5, 7, 9, 12, 19, 21]

# 1: Print the numbers list using while.
# i = 0
# while (i < len(numbers)):
#     print(numbers[i])
#     i += 1

# 2: Get start and end values from the user, then print all odd numbers in between.
# start = int(input('Start: '))
# end = int(input('End: '))
# i = start
# while i < end:
#     i += 1
#     if (i % 2 == 1):
#         print(i)

# 3: Print numbers from 100 to 1 in descending order.
# i = 100
# while i > 0:
#     print(i)
#     i -= 1

# 4: Get 5 numbers from the user, then print them in sorted order.
# nums = []
# i = 0
# while i < 5:
#     num = int(input('Number: '))
#     nums.append(num)
#     i += 1
# nums.sort()
# print(nums)

# 5: Get an unlimited number of product details from the user and store them in a list.
#    ** Ask the user how many products they want to enter.
#    ** Use a dictionary structure with (name, price).
#    ** When done, list the products using while.

products = []
count = int(input('How many products do you want to add: '))
i = 0

while i < count:
    name = input('Product name: ')
    price = input('Product price: ')
    products.append({
        'name': name,
        'price': price
    })
    i += 1

for product in products:
    print(f'Product name: {product["name"]} | Product price: {product["price"]}')
