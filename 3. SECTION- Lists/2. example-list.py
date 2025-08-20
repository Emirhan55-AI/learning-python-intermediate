# 1-  Create a list containing the elements “BMW, Mercedes, Opel, Mazda.”

cars = ['BMW', 'Mercedes', 'Opel', 'Mazda']

# 2-  How many elements are in the list?

result = len(cars)

# 3-  What are the first and last elements of the list?

result = cars[0]
result = cars[3]
result = cars[-1]

# 4-  Change the value of Mazda to Toyota.

cars[-1]= 'Toyota'
result = cars
print(result)
result = cars + ["Ferrari", "Dacia"]
print(result)

# 5-  Is Mercedes an element of the list?

result = 'Mercedes' in cars
result = "Mercedes" not in cars

# 6-  What is the value at index -2 of the list?

result = cars[-2]

# 7-  Get the first 3 elements of the list.

result = cars[0:3]
result = cars[:3]
result = cars[-2:]

# 8-  Replace the last 2 elements of the list with "Toyota" and "Renault".

cars[-2:] = ['Toyota', 'Renault']
result = cars

# 9-  Add "Audi" and "Nissan" to the list.

result = cars + ['Audi', 'Nissan']

# 10- Remove the last element of the list.

del cars[-1]
result = cars

# 11- Print the elements of the list in reverse order.

result = cars[::-1]

# 12- Store the following data in a list.

      # studentA: Yiğit Mehmet 2010, (70,60,70)
      # studentB: Muhammed Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90) 

studentA = ['Yiğit', 'Mehmet', 2010, [70, 60, 70]]
studentB = ['Muhammed', 'Turan', 1999, [80, 80, 70]]
studentC = ['Ahmet', 'Turan', 1998, [80, 70, 90]]

# 13- Print the elements of the list.

result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} {2019 - studentA[2]} years old and note average {(studentA[3][0] + studentA[3][1] + studentA[3][2]) / 3}"

print(result)