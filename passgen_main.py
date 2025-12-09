import random
import os
from cryptography.fernet import Fernet

#Key logic
def load_create_key():
    filename = "secret.key"
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        key = open(filename, "rb").read()
        return key
    else:
        key = Fernet.generate_key()
        with open(filename, "wb") as key_file:
            key_file.write(key)
        return key

#Key variables
key = load_create_key()
cipher = Fernet(key)

#Library of possible characters
LETTER_LIBRARY = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGIT_LIBRARY = '1234567890'
SYMBOL_LIBRARY = '-/:;$&@.,?!'

#Combined library of possible characters
combined_library = LETTER_LIBRARY + DIGIT_LIBRARY

length = int(input('How many characters should be in your password?\n'))

#password init
password = ""

symbols_true = input('Should your password use special characters? [Y] or [N]\n').upper()

if symbols_true == 'Y' or symbols_true == 'YES':
    combined_library += SYMBOL_LIBRARY

#inital for loop to generate
for i in range(length):
    character = random.choice(combined_library)
    password += character

#Encrypt password file
token = cipher.encrypt(password.encode())
encrypted_password = token.decode()

#Gather further user info
website = input('What website is this password for?\n')
username = input(f'What is your username for {website}?\n')

#save password to file
with open("passwords.txt", "a") as file:
    file.write(f"{website} | {username} | {encrypted_password}\n")

#display
print(f"Your password for {website} has been saved securely!")