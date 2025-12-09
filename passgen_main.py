import random

#Library of possible characters
LETTER_LIBRARY = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGIT_LIBRARY = '1234567890'
SYMBOL_LIBRARY = '-/:;$&@.,?!'

#Combined library of possible characters
combined_library = LETTER_LIBRARY + DIGIT_LIBRARY

length = int(input('How many characters should be in your password?'))

#password init
password = ""

symbols_true = input('Should your password use special characters? [Y] or [N]').upper()

if symbols_true == 'Y' or symbols_true == 'YES':
    combined_library += SYMBOL_LIBRARY

#inital for loop to generate
for i in range(length):
    character = random.choice(combined_library)
    password += character

#display
print(password)