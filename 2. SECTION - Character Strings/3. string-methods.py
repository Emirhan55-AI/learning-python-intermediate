message = "    Bismillah. Rahman! rahim"

# This method does not change the original string, it creates a new one.



# 1.PART: 

'''
message = message.upper()
message = message.lower()
message = message.title() # Every word's first letter is capitalized
message = message.capitalize() # The first letter is capitalized
sonuc = "abc".islower() # Is the written text lowercase = True (if you say .isupper() it asks if it's uppercase.)
sonuc= message.count('.') # Counts how many . are in the sentence.
sonuc = message.isalpha() # Are the characters in the sentence made up of letters.
'''

# 2.PART: 

'''
message = message.strip() # Removes the leading whitespace.
message = message.split() # Converts the message into a list.
message = message.split('.')  # Splits the words from the period.
message = message.split('!') # Splits the word after the exclamation mark.
sonuc = message.index("Rahman") # Gives the index where this word starts.
'''

# 3.PART: 

'''
message = ' '.join(message) # Adds a space between elements
message = '*'.join(message) # Adds a * between elements
message = '---'.join(message)

index = message.find("Bismillah") # searches for Bismillah in a sentence
print(index) # If the word is not in the sentence, it returns -1.

isFound = message.startswith(' ') # Is the sentence starting with a space?
isFound2 = message.startswith('B') # Is the sentence starting with a capital B?
isFound3 = message.endswith("m") # Is the sentence ending with a lowercase m?
print(isFound)
print(isFound2)
print(isFound3)
'''

# 4.PART: 

'''
message = message.replace('Bismillah','ALLAH') # Write ALLAH instead of Bismillah
message = message.replace(' ','*') # Replace space with *
message = message.replace('Bismillah','Rahman').replace('rahim','Rahim')
'''

# 5.PART: 

'''
message = message.center(100) # Leaves 100 characters of space on the right and left sides.
message = message.center(50,'!') #Puts exclamation marks in those spaces.
'''


'''
print(message)
print(message[2])
'''

# You can find string methods on GOOGLE.