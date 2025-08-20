# ===============================================
#               GRADE APPLICATION
# ===============================================

# Function to calculate the letter grade and average
def calculate_grade(line):
    line = line[:-1]  # Remove the newline character (\n) at the end
    parts = line.split(":")  # "name surname:90,80,70" -> ['name surname', '90,80,70']

    student_name = parts[0]  # Student's full name
    grades = parts[1].split(",")  # Split the grades by commas -> ['90', '80', '70']

    # Convert grades to integers
    grade1 = int(grades[0])
    grade2 = int(grades[1])
    grade3 = int(grades[2])

    # Calculate the average
    average = (grade1 + grade2 + grade3) / 3

    # Determine the letter grade based on the average
    if average >= 90 and average <= 100:
        letter = "AA"
    elif average >= 80:
        letter = "BA"
    elif average >= 75:
        letter = "BB"
    elif average >= 70:
        letter = "CB"
    elif average >= 65:
        letter = "CC"
    elif average >= 60:
        letter = "DC"
    elif average >= 50:
        letter = "DD"
    elif average >= 40:
        letter = "FD"
    else:
        letter = "FF"

    # Return the student name, letter grade, and average as a string
    return f"{student_name} : {letter} - ({average})\n"


# Function to take student information and grades from the user and append them to a file
def enter_grade():
    first_name = input("Student first name: ")
    last_name = input("Student last name: ")
    grade1 = input("Grade 1: ")
    grade2 = input("Grade 2: ")
    grade3 = input("Grade 3: ")

    # Write the data to the file in the format "name surname:grade1,grade2,grade3"
    with open("exam_grades.txt", "a", encoding="utf-8") as file:
        file.write(first_name + ' ' + last_name + ':' + grade1 + ',' + grade2 + ',' + grade3 + '\n')


# Function to read all grades from the file and print their letter equivalents
def read_grades():
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(calculate_grade(line))


# Function to save the letter grades into a separate file
def save_grades():
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        results = []

        for line in file:
            # Get the grade evaluation for each line and add it to the list
            results.append(calculate_grade(line))

    # Write the letter grades into a new file
    with open("results.txt", "w", encoding="utf-8") as file2:
        file2.writelines(results)


# Main loop: shows a menu and performs operations based on user choice
while True:
    choice = input(
        "\n--- MENU ---\n"
        "1 - Enter Grade\n"
        "2 - Show Averages\n"
        "3 - Save Grades\n"
        "4 - Exit\n"
        "Your choice: "
    )

    if choice == "1":
        enter_grade()
    elif choice == "2":
        read_grades()
    elif choice == "3":
        save_grades()
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
