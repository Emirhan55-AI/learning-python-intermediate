import math  # Import the math module
import math as operation  # We gave the math library the alias "operation". Now we can use operation. instead of math.

# METHOD 1

"""
value = dir(math)  # Shows available functions inside the math module.
value2 = help(math)  # Shows how all functions can be used.
value3 = help(math.ceil)  # Shows how only the 'ceil' function can be used.
"""

"""
value = operation.cos(20)
value2 = operation.sqrt(49)
"""

# METHOD 2

"""
from math import *  # Imports all math functions, so you can use them without writing math. before.
value = sqrt(49)
value2 = sinh(35)
"""

"""
from math import factorial, ceil  # Only imports specific functions you choose.
value = factorial(6)
value2 = sin(30)  # You cannot use this because 'sin' was not imported.
"""

def sqrt(x):
    print("x : " + str(x))
    
from math import sqrt
value = sqrt(20)

# Here, the sqrt defined with 'def' is replaced by the sqrt imported from math.
# When two functions have the same name, the one written last will be used.
