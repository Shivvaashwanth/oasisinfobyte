import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters for security.")

    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("At least one character type must be selected.")

    password = "".join(random.choice(char_pool) for _ in range(length))
    return password

# User Input
length = int(input("Enter password length: "))
use_letters = input("Include letters? (y/n): ").lower() == "y"
use_digits = input("Include digits? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

try:
    password = generate_password(length, use_letters, use_digits, use_symbols)
    print(f"Generated Password: {password}")
except ValueError as e:
    print(f"Error: {e}")
