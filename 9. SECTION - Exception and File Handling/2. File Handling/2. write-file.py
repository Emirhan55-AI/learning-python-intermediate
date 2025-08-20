# "w": Write mode
# In this mode:
#  - If the file does not exist, it will be created.
#  - If the file already exists, its content will be completely deleted and replaced.

# Open the file in write mode
with open("file.txt", "w", encoding="utf-8") as file:
    # The write() function writes text into the file
    file.write("AI\n")
    file.write("Emirhan Uysal\n")
    # When the 'with' block ends, the file is automatically closed


# Now open the file in read mode
with open("file.txt", "r", encoding="utf-8") as file:
    # Loop through each line in the file
    for i in file:
        # Print each line to the screen
        # end="" → prevents print() from adding an extra newline at the end
        print(i, end="")
