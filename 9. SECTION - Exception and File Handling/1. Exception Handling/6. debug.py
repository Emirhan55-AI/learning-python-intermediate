# ===============================================
#            PDB (Python Debugger) EXAMPLE
# ===============================================

# In Python, the 'pdb' module is used for step-by-step debugging.
# In this example, we will analyze the sum of numbers in a list step by step.

import pdb  # Import the debugger module

def calculate_sum(numbers):
    """
    Function that returns the sum of the given list of numbers.
    """
    total = 0

    # Start the debugger here
    pdb.set_trace()  # From this line, the program will pause, and you can debug step by step

    for num in numbers:
        total += num  # Add each number to the total

    return total

# Define a list for testing
my_list = [2, 4, 6, 8]

# Call the function — the debugger will activate here
result = calculate_sum(my_list)

# Print the result
print(f"Sum: {result}")


# ===============================================
#          PDB COMMANDS (FOR DEBUGGER)
# ===============================================

# l => "list": Shows the current line and surrounding code
# n => "next": Executes the current line and goes to the next
# p <variable> => "print": Prints the value of a variable
# s => "step": Steps into a function call
# c => "continue": Resumes the program until the next breakpoint (or exits debugger)
# q => "quit": Exits the debugger and stops the program

# ===============================================
#      EXAMPLE TERMINAL USAGE (AFTER set_trace)
# ===============================================

# (Pdb) p numbers
# [2, 4, 6, 8]

# (Pdb) p total
# 0

# (Pdb) n
# (Pdb) p num
# 2

# (Pdb) n
# (Pdb) p total
# 2

# (Pdb) c
# Sum: 20
