import random
import os
from cryptography.fernet import Fernet

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

key = load_create_key()
cipher = Fernet(key)

def add_password():

    LETTER_LIBRARY = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    DIGIT_LIBRARY = '1234567890'
    SYMBOL_LIBRARY = '-/:;$&@.,?!'

    combined_library = LETTER_LIBRARY + DIGIT_LIBRARY

    length = int(input('How many characters should be in your password?\n'))

    symbols_true = input('Use special characters? [Y] or [N]\n').upper()

    if symbols_true == 'Y' or symbols_true == 'YES':
        combined_library += SYMBOL_LIBRARY

    password = ""

    for i in range(length):
        character = random.choice(combined_library)
        password += character

    token = cipher.encrypt(password.encode())
    encrypted_password = token.decode()

    website = input('What website is this password for?\n')
    username = input(f'What is your username for {website}?\n')

    with open("passwords.txt", "a") as file:
        file.write(f"{website} | {username} | {encrypted_password}\n")

    print(f"Your password for {website} has been saved securely!")

def view_passwords():
    if not os.path.exists("secret.key"):
        print("Error: Key file not found!")
        exit()

    key = open("secret.key", "rb").read()
    cipher = Fernet(key)

    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet!")
        exit()

    target = input("Search for a site or user (or press Enter to see all): ").lower()

    print(f"\n--- SEARCH RESULTS ({target}) ---" if target else "\n--- ALL PASSWORDS ---")

    found = False

    with open("passwords.txt", "r") as file:
        for line in file:
            parts = line.strip().split(" | ")
        
            if len(parts) == 3:
                website = parts[0]
                username = parts[1]
                encrypted_pass = parts[2]
            
                if target in website.lower() or target in username.lower():
                
                    try:
                        decrypted_pass = cipher.decrypt(encrypted_pass.encode()).decode()
                        print(f"Site: {website}")
                        print(f"User: {username}")
                        print(f"Pass: {decrypted_pass}")
                        print("-" * 30)
                        found = True
                    except:
                        print(f"Error decrypting {website}. Key mismatch?")

    if not found:
        print("No matches found.")

    print("--- SAVED PASSWORDS ---")

    with open("passwords.txt", "r") as file:
        for line in file:
            parts = line.strip().split(" | ")
        
            if len(parts) == 3:
                website = parts[0]
                username = parts[1]

                encrypted_pass = parts[2]
                decrypted_pass = cipher.decrypt(encrypted_pass.encode()).decode()
            
                print(f"Site: {website}")
                print(f"User: {username}")
                print(f"Pass: {decrypted_pass}")
                print("-" * 30)

while True:
    print("\n" + "="*30)
    print(" PASSWORD MANAGER v2.0")
    print("="*30)
    print("1. Add a new password")
    print("2. Find a password")
    print("3. Exit")
    
    choice = input("\nChoose an option (1-3): ")

    if choice == '1':
        add_password()
    elif choice == '2':
        view_passwords()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")