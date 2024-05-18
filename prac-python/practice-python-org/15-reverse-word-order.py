# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. 
# For example, say I type the string:

#   My name is Michele

# Then I would see the string:

#   Michele is name My

# shown back to me.

from typing import List


def main():
    print("This is a program to reverses a string separated by spaces! Input a string")
    try:
        echo: str = input()
    except Exception as e:
        print(f"error: {e}")
        return
    print(f"recieved: {echo}")
    split_str: List[str] = echo.split(" ")
    split_str.reverse()
    print(split_str)
    for ele in split_str:
        print(ele, end=" ")
    print()


if __name__ == "__main__":
    main()
