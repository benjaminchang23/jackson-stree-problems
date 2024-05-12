# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)


def main():
    print("input a string for palandrome checking")
    try:
        echo = input()
    except Exception as e:
        print(f"error: {e}")
        return
    if len(echo) == 1:
        print(f"the string of {echo}, a single character is a palindrome")
        return
    check_count = int(len(echo)/2)
    is_palindrome = True
    for x in range(check_count):
        if echo[x] != echo[len(echo) - 1 - x]:
            is_palindrome = False
            break
    if is_palindrome:
        print(f"{echo} is a palindrome")
    else:
        print(f"{echo} is not a palindrome")


if __name__ == "__main__":
    main()
