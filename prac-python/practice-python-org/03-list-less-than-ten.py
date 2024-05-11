# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# Take a list, say for example this one:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

#     Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#     Write this in one line of Python.
#     Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


from typing import List


def oneline_solution(input_list: List, limit: int):
    return [
        ele for ele in input_list if ele < limit
    ]


def main():
    limit = 5
    list_0 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print(oneline_solution(list_0, limit))

if __name__ == "__main__":
    main()
