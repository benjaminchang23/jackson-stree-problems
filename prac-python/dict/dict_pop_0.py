from copy import deepcopy
from typing import Dict

dict_0 = {}

dict_0["a"] = "a"
dict_0["bs"] = ["b", "c"]

dict_1 = {}

dict_1["a"] = "a"
dict_1["b"] = "b"

def dict_widget(dict: Dict):
    deepcopy_dict = deepcopy(dict)
    if "bs" in deepcopy_dict:
        print(len(deepcopy_dict.get("bs")))
        deepcopy_dict.pop("bs")
    elif "b" in deepcopy_dict:
        deepcopy_dict.pop("b")
    print(deepcopy_dict)

dict_widget(dict_0)
dict_widget(dict_1)
