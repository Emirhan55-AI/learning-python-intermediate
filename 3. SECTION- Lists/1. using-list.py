"""
String data types are a collection of characters, and we can access each character using its index number.

Similarly, with the list data type, we can group different data types together instead of just a single character.

In Python, there are 4 different list types: List, Tuple, Set, and Dictionary:

--> List elements are ordered, mutable, and can contain duplicate values.
--> Tuple elements are ordered but immutable and can also contain duplicate values.
--> Set elements are unordered and unindexed, and each element can only appear once.
--> Dictionary elements are key-value pairs, and there cannot be multiple elements with the same key.

Lists can be printed using a for loop.
"""


"""
message = "Selamun Aleyküm Mübarek".split() # Converts the string into a list. 
print(message)
print(message[1])
"""


my_list = [1, 2, 3]
my_list2 = ['one', 2, True, 5.6]
print(my_list)
print(my_list2)
print(my_list + my_list2)
print(my_list[0] + my_list[2] + my_list2[3])



list1 =['one', 'two', 'three']
list2 =['four', 'five', 'six']
list3 = [['one', 'two', 'three'], ['four', 'five', 'six']]
numbers = list1 + list2
print(numbers)
print(list3[0][1] + " " + list3[1][2])


# list within a list

userA = ["Emirhan", 21]
userB = ["Uysal", 5.3]
users = [userA, userB]
print(users)
print(users[0][1])


# for loop to print list

my_List = ["one", "two", "three"]

for i in my_List:
    print(i)