'''
Random password generator by Anton Hristov
'''

import sys
import string
import random

def password_generator():
    '''Generate random password'''

    special_chars = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    while True:
        try:
            include_special_chars = input("Include special characters? (y/n) ")
            if (include_special_chars == "y") or (include_special_chars == "Y"):
                chars = string.ascii_letters + string.digits + special_chars
                break
            elif (include_special_chars == "n") or (include_special_chars == "N"):
                chars = string.ascii_letters + string.digits
                break
            else:
                print("Oops! Wront input provided. Try again...")
                continue
        except RuntimeError:
            raise

    while True:
        try:
            password_length = int(input("Enter password lenght (8 to 128 chars recommended): "))
            if password_length < 4:
                print("The password must be at least four characters. Try again...")
                continue
            else: break
        except ValueError:
            print("Oops! Not a valid number. Try again...")
        except KeyboardInterrupt:
            sys.exit("")

    #Generate random numbers from sources provided by the operating system.
    random.SystemRandom()

    print("\n### Generating Five Random Passwords ### \n")
    for _ in range(5):
        password = ''
        for _ in range(password_length):
            password += random.choice(chars)
        print(password + "\n")
