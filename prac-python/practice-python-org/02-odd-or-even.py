# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:

#     If the number is a multiple of 4, print out a different message.
#     Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#     If check divides evenly into num, tell that to the user. 
#     If not, print a different appropriate message.


def main():
    print("Please input an odd or even integer. Alternatively, input two integers x and y to check if x divides evenly into y. ")
    try:
        echo = input()
    except Exception as e:
        print(f"error: {e}")
        return
    split_str: str = echo.split(" ")
    if len(split_str) == 1:
        try:
            num: int = int(split_str[0])
            # zero is even
            if num % 2 == 1:
                print("odd")
            elif num % 4 == 0:
                print("divisible by 4")
            else:
                print("even")
        except ValueError as e:
            print(f"could not process: {split_str[0]} {e}")
            return
    elif len(split_str) == 2:
        x_str = split_str[0]
        y_str = split_str[1]
        try:
            x = int(x_str)
            y = int(y_str)
            xy_modulo = x % y
            if xy_modulo == 0:
                print(f"{x} divides evenly into {y}")
            else:
                print(f"{x} does not divide evenly into {y} there is {xy_modulo} remainder")
        except ValueError as e:
            print(f"could not process: {x_str} or {y_str} {e}")
            return
    else:
        print("Too many arguments!")


if __name__ == "__main__":
    main()
