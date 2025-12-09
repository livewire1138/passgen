import random

#Library of possible characters
LETTER_LIBRARY = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGIT_LIBRARY = '1234567890'
SYMBOL_LIBRARY = '-/:;$&@.,?!'

#Combined library of possible characters
combined_library = LETTER_LIBRARY + DIGIT_LIBRARY + SYMBOL_LIBRARY

#password init
password = ""

#inital for loop to generate
for i in range(8):
    character = random.choice(combined_library)
    password += character

#display
print(password)