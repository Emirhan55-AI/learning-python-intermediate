numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

# 1. PART: Min/Max

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers[4] = 40

# 2. PART: Additions

numbers.append(49)
numbers.append(59)
letters.append("emirhan")
numbers.insert(3, 78) # 3. Add the number 78 to the index. 3. The index shifts to the right by one position.
numbers.insert(-1, 52)
letters.insert(0, "ahmet")

#3. PART: Deletions

# numbers.pop()
# numbers.pop(0)
# numbers.pop(-1)
# numbers.remove(59)

#4. PART: Sorting

numbers.sort()
numbers.reverse()
letters.sort()
letters.reverse()
print(numbers)
print(letters)

print(len(numbers))
print(len(letters))

#5. PART: Counting

print(numbers.count(10))
print(letters.count('a'))
print(numbers.index(10))

numbers.clear()
print(numbers)