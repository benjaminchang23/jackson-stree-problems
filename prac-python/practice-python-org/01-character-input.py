# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 
# Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). 
# If you want to do this in a generic way, see exercise 39.

# Extras:

#     Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
#       (Hint: order of operations exists in Python)
#     Print out that many copies of the previous message on separate lines. 
#       (Hint: the string "\n is the same as pressing the ENTER button)

from datetime import datetime
from typing import List


def print_help():
    print("please input your first name and birthday (YYYY-MM-DD)")
    print("enter exit or quit to stop the application")


def main():
    done: bool = False
    while not done:
        print_help()
        try:
            echo: str = input()
        except Exception as e:
            print(f"error: {e}")
            return
        print(f"recieved {echo}")
        if echo == "exit" or echo == "quit":
            return
        split_str: List[str] = echo.split(" ")
        if len(split_str) != 2:
            continue
        name = split_str[0]
        try:
            date: datetime = datetime.strptime(split_str[1], "%Y-%m-%d")
        except ValueError as e:
            print(f"could not convert time format: {e}")
            continue
        hundred_date = date.replace(year=date.year + 100)
        print(f"Hello {name}, you will turn 100 on {hundred_date}")
        done = True


if __name__ == "__main__":
    main()
