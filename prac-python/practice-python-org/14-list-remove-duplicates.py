# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# Extras:
#     Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#     Go back and do Exercise 5 using sets, and write the solution for that in a different function.


from typing import List


def deduplicate_list_manual(my_list: List):
    new_list = []
    for ele in my_list:
        if ele not in new_list:
            new_list.append(ele)
    return new_list

def deduplicate_list_set(my_list: List):
    return list(set(my_list))


def main():
    lists = [
        [],
        [1, 2, 3, 4, 5, 6, 7, 8, 8],
        [1, 1, 1, 1, 1, 1],
        [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    ]
    for list in lists:
        print(f"checking {list}")
        print(f"deduplicate_list_manual: {deduplicate_list_manual(list)}")
        print(f"deduplicate_list_set: {deduplicate_list_set(list)}")


if __name__ == "__main__":
    main()
