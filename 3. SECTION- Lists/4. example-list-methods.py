names = ['Ali', 'Ahmet', 'Hakan', 'Kerem']
years = [1998, 2000, 1998, 1987]

# 1- Add the name “Cenk” to the end of the list.

# names.append('Cenk')

# 2- Add the value “Fenasi” to the top of the list.

# names.insert(0, 'Fenasi')
# names.insert(-1, 'Mehmet')
# names.insert(len(names), 'Mehmet')

# 3- Remove the name "Ahmet" from the list.

# names.remove('Ahmet')
# names.pop()
# names.pop(1)

# 4- What is the index of the name "Ahmet"?

# index  = names.index('Ahmet')
# names.pop(index)

# 5- Is "Ali" an element of the list?

# result = 'Ali' in names
# result = names.index('Ali')

# 6- Reverse the elements of the list.

# names.reverse()

# 7- Sort the elements of the list alphabetically.

# names.sort()

# 8- Sort the years list by numerical value.

# years.sort()

# 9- str = “Chevrolet,Dacia” Convert the character string to a list.

# str = "Chevrolet, Dacia"
# result = str.split(',')

# 10- What are the largest and smallest elements in the years list?

# min = min(years)
# max = max(years)
# print(min, max)

# 11- How many 1998 values are there in the years list?

# result = years.count(1998)

# 12- Clear all elements of the years list.

# years.clear()

# 13- Store 3 brand names obtained from the user in a list.

markalar = [] # empty list

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)