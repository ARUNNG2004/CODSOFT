import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the  length of the password: "))
        if length < 1:
            print("enter a positive integer number")
            return
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid input")

if __name__ == "__main__":
    main()
