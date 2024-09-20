import random
import string

def generate_password(length):
    if length <= 0:
        print("Length should be greater than 0")
        return ""
    
    letters = string.ascii_letters  # A-Z, a-z
    numbers = string.digits  # 0-9
    password = []

    for i in range(length):
        if i % 2 == 0:  # Even index, add a letter
            password.append(random.choice(letters))
        else:  # Odd index, add a number
            password.append(random.choice(numbers))

    return ''.join(password)

# Get input from user
length = int(input("Enter the desired length of the password: "))

# Generate and print the password
generated_password = generate_password(length)
print("Generated Password:", generated_password)

