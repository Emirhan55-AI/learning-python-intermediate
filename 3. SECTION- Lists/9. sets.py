fruits = {'orange', 'banana', 'mango'} # set definitions are made between {}.
# print(fruits[0]) Unlike lists, sets are unordered and unindexed. They cannot be indexed. Elements cannot be repeated or updated. You can delete or add elements.


# You can access elements with a loop.
for x in fruits:
    print(x)



fruits.add('cherry') # cherry was added to the list.
fruits.update(['mango', 'apple', 'melon']) # if the same element is not found in the list, it will not be visible even if you add it (two at once)
print(fruits)


fruits.remove('mango') # mango was removed. using discard instead of remove also does the same thing.
fruits.pop() # since elements are not ordered, it removes a random word.
fruits.clear() # all elements are deleted.



MY_list = [1, 2, 3, 4, 5, 1, 2]
print(MY_list) # same values appear in this list.
print(set(MY_list)) # if we send mylist to the constructor, the same values do not appear.