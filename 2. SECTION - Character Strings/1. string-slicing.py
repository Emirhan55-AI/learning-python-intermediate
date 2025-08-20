selam = "Selamun Aleyküm"

print(selam[0]) # S
print(selam[-1]) # m
print(selam[1]) # e
print(selam[2]+selam[6]) # ln

# Find Character String Length

print(len(selam)) # 14 

print(selam[2:5]) # Starting from 2 up to 4, not including 5
print(selam[3:])
print(selam[:9])
print(selam[4:len(selam)])
print(selam[2:14:3]) # Takes one character every 3 characters.
print(selam[::])
print(selam[::2]) # Takes one character, skips one.
print(selam[::-1]) # Prints in reverse. If you write 1, it prints normally.