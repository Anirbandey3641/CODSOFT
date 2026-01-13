import random
import string
def generate_password(length, use_uppercase=True, use_numbers=True, use_special_chars=True):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    password_chars = []
    char_pool = string.ascii_lowercase
    if use_uppercase:
        password_chars.append(random.choice(string.ascii_uppercase))
        char_pool += string.ascii_uppercase
    if use_numbers:
        password_chars.append(random.choice(string.digits))
        char_pool += string.digits
    if use_special_chars:
        password_chars.append(random.choice(string.punctuation))
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(char_pool) 
       for _ in range(length))
    
    return password
def main():
    print("I can help you to generate a password")
    l=int(input("Enter the length of the password (minimum 4): "))
    u=input("Include uppercase letters? (y/n): ").lower() == 'y'
    n=input("Include numbers? (y/n): ").lower() == 'y'
    s=input("Include special characters? (y/n): ").lower() == 'y'
    try:
        password = generate_password(l, u, n, s)
        print("Generated password:",password)
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main() 