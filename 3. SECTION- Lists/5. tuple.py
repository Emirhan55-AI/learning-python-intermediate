# You can't add or remove stuff from a tuple list. It takes up less space in memory. You can go from a list to a tuple and from a tuple to a list.

my_list = [1, 2, 3]
my_tuple = (1, 'iki', 3) # You don't have to use parentheses.
print(type(my_list))
print(type(my_tuple))
print(my_list[2])
print(my_tuple[2])
print(len(my_tuple))
print(len(my_list))



my_list = ['ali', 'veli']
my_tuple = ('a', 'b', 'b')
names = ('c', 'd', 'f') + my_tuple
print(names)



my_list[0] = 'ahmet'
# my_tuple[0] = 'kerim' This kind of assignment is not possible. The difference with a tuple is that you can't change, add, or remove a single element. You can make a general change.



print(my_tuple.count('b'))
print(my_tuple.index('b')) # No other methods can be used.
print(my_list)
print(my_tuple)



# Type Conversion
my_tuple = tuple([2, 3, 4])
my_list = list((2, 3, 4))