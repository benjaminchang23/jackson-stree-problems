import json
import enum

class MyEnum(enum.Enum):
    first = 1
    second = 2
    third = 3

list_to_read_in = []

dict_0 = {
    "enum": str(MyEnum.second.name),
}
dict_1 = {
    "enum": str(MyEnum.third.name),
}

list_to_read_in.append(dict_0)
list_to_read_in.append(dict_1)

json_dict = {
    "enum_list": list_to_read_in
}

json_dict_str = json.dumps(json_dict)

print(json_dict_str)
