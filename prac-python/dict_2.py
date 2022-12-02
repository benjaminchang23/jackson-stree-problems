from typing import Dict

def add_to_dict(dict: Dict, input: str):
    dict[input] = input

dict_0 = {}

add_to_dict(dict_0, "1")
add_to_dict(dict_0, "2")
add_to_dict(dict_0, "3")


for element in dict_0:
    print(element)
