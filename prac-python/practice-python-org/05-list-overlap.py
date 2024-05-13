# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

# Extras:

#     Randomly generate two lists to test this
#     Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)


from random import randrange
from typing import List


def get_random_num(limit: int) -> int:
    random_num = randrange(limit)
    if random_num < 1:
        return 1
    return random_num


def list_comp_sol(list_0: List, list_1: List) -> List:
    return [ele for ele in list_0 if ele in list_1]


def main():
    print("enter a max value as an integer for the random list generator and an integer for the max random list size")
    try:
        echo: str = input()
    except Exception as e:
        print(f"error: {e}")
        return
    split_str: str = echo.split(" ")
    if len(split_str) != 2:
        print(f"got len {len(split_str)}, required, 2")
        return
    try:
        max_value_limit: int = int(split_str[0])
        max_size_limit: int = int(split_str[1])
        if max_value_limit <= 1 or max_size_limit <= 1:
            print(f"limits must be greater than 1")
            return
        max_size: int = get_random_num(max_size_limit)
        print(f"max_value_limit: {max_value_limit} max_size: {max_size}")

        size_0: int = get_random_num(max_size)
        size_1: int = get_random_num(max_size)
        print(f"size_0: {size_0} size_1: {size_1}")

        list_0: List = []
        list_1: List = []
        for x in range(size_0):
            list_0.append(get_random_num(max_value_limit))
        for x in range(size_1):
            list_1.append(get_random_num(max_value_limit))
        print(f"list_0: {list_0} list_1: {list_1}")
        overlap_list = list_comp_sol(list_0, list_1)
        print(overlap_list)
    except ValueError as e:
        print(f"could not process: {split_str[0]} or {split_str[1]} {e}")
        return


if __name__ == "__main__":
    main()
