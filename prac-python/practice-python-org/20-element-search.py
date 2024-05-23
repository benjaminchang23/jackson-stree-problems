# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:
#     Use binary search.


from typing import Any, List


def find_element_binary(my_list: List, ele: Any):
    found: bool = False
    start_index: int = 0
    end_index: int = len(my_list) - 1

    if not ele or not my_list:
        print(f"Found: {found}")
        return found

    while not found:
        check_index: int = int((end_index - start_index)/2) + start_index
        check = my_list[check_index]

        # print(f"check_index: {check_index} val: {check} ele: {ele} start: {start_index} end: {end_index}")

        if check_index < start_index or check_index > end_index:
            print(f"Found: {found} {check_index}")
            return found

        if end_index - start_index == 1:
            found = my_list[start_index] == ele or my_list[end_index] == ele
            return found

        if check < ele:
            start_index = check_index
        elif check > ele:
            end_index = check_index
        elif check == ele:
            found = True
        else:
            raise ValueError(f"Could not eval: {check} - {my_list[check_index]}")

    print(f"Found: {found}")
    return found


def find_element_simple(my_list: List, ele: Any):
    "assuming that the element is the same type as the list contents"
    found: bool = ele in my_list
    print(f"Found: {found}")
    return found


def main():
    list_0 = []
    list_1 = [1]
    list_2 = [1, 2]
    list_3 = [1, 2, 3]
    list_4 = [1, 2, 3]
    list_5 = [1, 2, 3, 4, 5]
    list_6 = [1, 2, 3, 4, 5, 6]
    list_7 = ["a", "b", "c"]
    list_8 = ["a", "b", "c", "d"]
    list_9 = ["a", "b", "c", "d", "e"]

    assert find_element_simple(list_0, None) == False
    assert find_element_simple(list_1, 1) == True
    assert find_element_simple(list_2, 2) == True
    assert find_element_simple(list_3, 2) == True
    assert find_element_simple(list_4, 4) == False
    assert find_element_simple(list_5, 4) == True
    assert find_element_simple(list_6, 4) == True
    assert find_element_simple(list_7, "a") == True
    assert find_element_simple(list_8, "b") == True
    assert find_element_simple(list_9, "c") == True

    print("------")

    assert find_element_binary(list_0, None) == False
    assert find_element_binary(list_1, 1) == True
    assert find_element_binary(list_2, 2) == True
    assert find_element_binary(list_3, 2) == True
    assert find_element_binary(list_4, 4) == False
    assert find_element_binary(list_5, 4) == True
    assert find_element_binary(list_6, 4) == True
    assert find_element_binary(list_7, "a") == True
    assert find_element_binary(list_8, "b") == True
    assert find_element_binary(list_9, "c") == True

if __name__ == "__main__":
    main()
