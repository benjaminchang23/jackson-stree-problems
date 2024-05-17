# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

from typing import List

def first_and_last(input_list: List):
    if len(input_list) <= 2:
        return input_list
    return [input_list[0], input_list[-1:][0]]

list_0 = [0, 1, 2, 3, 4, 5]

assert first_and_last(list_0) == [0, 5]
assert first_and_last([0]) == [0]
assert first_and_last([]) == []
