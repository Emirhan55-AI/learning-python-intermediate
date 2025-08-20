# Open the file marks.txt in append mode
# This adds the line "6-Bmw\n" to the end of the file
with open("marks.txt", "a") as file:
    file.write("6-Bmw\n")

# Open the file marks.txt in read+write mode
# This block is commented out, but to explain:
# 1. Reads the entire content of the file
# 2. Adds "1-Toyota\n" to the beginning
# 3. Moves the cursor back to the start
# 4. Writes the updated data into the file
# with open("marks.txt", "r+", encoding="utf-8") as file:
#     marks = file.read()
#     marks = "1-Toyota\n" + marks
#     file.seek(0)
#     file.write(marks)

# Open marks.txt in read+write mode
# This time, read line by line and insert new data in between
with open("marks.txt", "r+", encoding="utf-8") as file:
    marks = file.readlines()                 # Reads all lines as a list
    marks.insert(2, "3-Renault\n")           # Inserts "3-Renault\n" as the 3rd line (index 2)
    file.seek(0)                             # Moves the cursor back to the beginning
    # The following loop was meant to write line by line, but it is commented out
    # for brand in marks:
    #     file.write(brand)
    file.writelines(marks)                   # Writes the entire list back into the file

# Open marks.txt in read-only mode and print its content
with open("marks.txt", "r", encoding="utf-8") as file:
    print(file.read())                       # Prints the entire content of the file
