# "a": Append mode.
#       If the file does not exist, it will be created.
#       If it exists, new content will be added to the end without deleting the old content.

# "r+": Both Read and Write mode.
#       The file must already exist, otherwise it will raise an error.
#       You can both read and overwrite from the beginning of the file.

with open("file2.txt", "r+", encoding="utf-8") as file:
    # file.seek(20) → this line is commented out. If it were active, the cursor would move to the 20th byte.
    # Reads the file content from the current cursor position to the end
    print(file.read())  

    # Since the cursor is now at the end of the file, writing will look like appending
    # This line adds "new line" to the file
    file.write("new line\n")

# NOTE: If the seek() line above had been active, the writing would start from that exact position.
# In that case, "new line" could overwrite the middle part of the previous content.

with open("file2.txt", "a", encoding="utf-8") as file:
    file.write("This line was added using append.\n")
    file.write("Data is being appended to the end of the file.\n")
