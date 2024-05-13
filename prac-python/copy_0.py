from typing import Dict
from copy import deepcopy

def modify_dict(my_dict: Dict):
    if len(my_dict.get("foo")) > 1:
        my_dict["bar"] = "plural"
    else:
        my_dict["bar"] = "singular"


def main():
    dict_0: Dict = {"foo": [1]}
    dict_1: Dict = {"foo": [1, 2]}
    print(f"{dict_0} - {dict_1}")
    deepcopy_dict_0 = deepcopy(dict_0)
    modify_dict(deepcopy_dict_0)
    modify_dict(dict_1)
    print(f"{dict_0} - {dict_1}")


if __name__ == "__main__":
    main()
