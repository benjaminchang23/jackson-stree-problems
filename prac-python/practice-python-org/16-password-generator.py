# https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
# Note: this is a 4-chili exercise, not because it introduces a concept, but because this exercise is more like a project. 
# Feel free to skip this and come back when you’re more ready!

# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.

# Extra:

#     Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


import random
import string


_password_word_list = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "apple",
    "avacado",
    "bannana",
    "cherry",
    "grape",
    "lemon",
    "orange",
    "peach",
    "pear",
    "pineapple",
]


def main():
    input_length = 0
    print("This is a password generator. ", end="")
    while input_length <= 0:
        print("How many elements should the password have?")
        try:
            echo: str = input()
        except Exception as e:
            print(f"error: {e}")
            return
        print(f"recieved: {echo}")
        try:
            input_length: int = int(echo)
        except ValueError as e:
            print(f"could not process: {echo} {e}")
            continue

        print("Should the password be generated from a simple list? y/n")
        simple_password: bool = True
        try:
            simple: str = input()
        except Exception as e:
            print(f"error: {e}")
            return
        print(f"recieved: {simple}")
        try:
            if simple == "n" or simple == "no":
                simple_password = False
            elif simple == "y" or simple == "yes":
                simple_password = True
            else:
                raise ValueError
        except ValueError as e:
            print(f"could not process: {echo} {e}")
            continue

        password_str: str = ""

        if simple_password:
            character_options = _password_word_list
        else:
            character_options = string.ascii_letters + string.digits

        password_character_list = random.choices(character_options, k=input_length)
        for character in password_character_list:
            password_str += character

        print(password_str)


if __name__ == "__main__":
    main()
