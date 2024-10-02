import random as rm
from random import random

print("Enter the desired length of the password, should be greater than 3 and press enter")
passwordLength = int(input())

def password_generator(passwordLength):
    if passwordLength < 4:
        print("The length should be greater than three")
        return ""

    #initialize password as an empty string
    password =  ""

    numbers = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while passwordLength > 0:
        letterIndex = rm.randint(0, 51)
        password = password + letters[letterIndex]
        passwordLength -= 1

        if passwordLength > 0:
            numberIndex = rm.randint(0, 9)
            password = password + numbers[numberIndex]
            passwordLength -= 1

    return password

print(password_generator(passwordLength))