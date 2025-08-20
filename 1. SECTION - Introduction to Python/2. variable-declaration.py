# What is a variable?
# - A variable is a named container that holds a value in RAM while a program runs.
# - When the program ends, RAM is cleared; variables are not persistent storage.

# Memory and addressing
# - Every piece of data in RAM lives at a memory address.
# - In high-level languages, we rarely work with raw addresses; the runtime manages them.
# - In many languages, variables may hold a reference to a value rather than the value itself.

# Data types (examples)
# - Numeric: int (integer), float/double (floating point)
# - Text: string
# - Boolean: bool (true/false)
# - Collections: array, list, dictionary/map, set
# - Others: date/time, enum, class/object (instance)
# - Type checking: static languages check at compile time; dynamic languages check at runtime.

# Assignment and reassignment
# - Assignment (=) binds a value to a variable name.
# - You can later assign a new value to the same variable; unreachable old values may be cleaned up by the garbage collector (GC).

# Naming rules (general)
# - Start with a letter or an underscore (_); cannot start with a digit.
# - No spaces or special characters.
# - Use meaningful names; include units when helpful (e.g., productPriceTRY).
# - Reserved keywords cannot be used as names (e.g., class, if, for).

# Naming styles (language-dependent)
# - camelCase: productPrice → common for variables/functions in JavaScript, Java, C#.
# - PascalCase: ProductPrice → common for class/type names.
# - snake_case: product_price → preferred for variables/functions in Python (PEP 8).
# - Whatever style you choose, keep it consistent across the project.



# Variable declaration and assignment in Python:

x = 1
y = 2.1
student = False
print(x, y, student)

name = "Emirhan"
lastname = " Uysal"
name2 = name + " " + lastname
print(name + lastname)
print(name2)

a, b, c, d = 2, 3, 5, False
print(a, b, c, d)