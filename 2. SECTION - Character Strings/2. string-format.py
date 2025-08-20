name = "Emirhan"
surname = "Uysal"

print("My name is {} and surname is {}".format(name, surname))
print("My name is {1} and surname is {0}".format(name, surname))
print("My name is {s} and surname is {n}".format(n=name, s=surname))
print("My name is {} and surname is {} I'm {} years old".format(name, surname, 36))
print("My name is {} and surname is {} and is {}".format(name, name, name))


# fstring

print(f"My name is {name} {name} {name}")


# Another Example

s = '12345' * 10
print(s)
print(s[::5]) # Takes only the 1's



# Another Example

result = 200/700
print("Result is : {}".format(result))
print("Result is : {k:10.4}".format(k=result)) # Takes 10 spaces and 4 digits after the decimal point.