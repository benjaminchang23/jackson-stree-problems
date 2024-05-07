from typing import List

def first_and_last(input_list: List):
    if len(input_list) <= 2:
        return input_list
    return [input_list[0], input_list[-1:][0]]

list_0 = [0, 1, 2, 3, 4, 5]

assert first_and_last(list_0) == [0, 5]
assert first_and_last([0]) == [0]
assert first_and_last([]) == []
