# In Python, file operations are performed using the open() function.
# General usage: open(file_name, access_mode, encoding)

# "r" mode: read mode. The file must already exist.
f = open("log.txt", encoding='utf-8')

# Reads the entire file and returns it as a string
print(f.read())

# If you try to read again, it returns an empty string because the cursor has reached the end
print(f.read())

# Reset the cursor position to 0, meaning go back to the beginning
f.seek(0)

# Read the entire content again
print(f.read())

# Again, returns empty because the cursor is at the end
print(f.read())

# Move the cursor to the 10th character in the file
f.seek(10)

# Reads from that position until the end
print(f.read())

# Reset the cursor back to the beginning
f.seek(0)

# Use readline() to read line by line
print(f.readline())  # 1st line
print(f.readline())  # 2nd line
print(f.readline())  # 3rd line
print(f.readline())  # No more lines, returns empty string

# Reset the cursor again
f.seek(0)

# readlines() returns all lines as a list
lines = f.readlines()
print(lines)  # ['1.line\n', '2.line\n', '3.line']

# You can access list elements by index
print(lines[0])  # '1.line\n'
print(lines[1])  # '2.line\n'
print(lines[2])  # '3.line'

# Check if the file is open
print(f.closed)  # False → still open

# Close the file
f.close()

# Now the file is closed
print(f.closed)  # True

# If you try to perform operations on a closed file, you get an error.
# We close files to free up memory.
# f.read()  # ValueError: I/O operation on closed file.

# Reopen the file
f = open("log.txt", encoding='utf-8')
print(f.read())
f.close()


# Using 'with' block to open files: This ensures the file closes automatically after use
with open("log.txt", encoding="utf-8") as f:
    # Read the entire file
    content = f.read()
    print("Content:", content)

    # After reaching the end of the file, the cursor will be at the end.
    # tell() function gives the exact byte position of the cursor
    position = f.tell()
    print("Cursor is now at byte {}.".format(position))

# At this point, the file has closed automatically

# New example: Demonstrating cursor movement and tell() together
with open("log.txt", encoding="utf-8") as f:
    print("First 10 characters:", f.read(10))  # Read first 10 characters
    print("Cursor position:", f.tell())        # Where is the cursor now?

    f.seek(0)  # Move cursor back to start
    print("Cursor position (after reset):", f.tell())

    line = f.readline()  # Read one line
    print("Read line:", line)
    print("Cursor position (after reading one line):", f.tell())


# Example with Exception Handling
try:
    with open("log2.txt", encoding="utf-8") as f:
        for i in f:
            print(i, end="")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
