import enum

class MyEnum(enum.Enum):
    first = 1
    second = 2
    third = 3

_map = {
    "first": 1,
    "second": 2,
    "third": 3,
}

def enum_to_str_name(enum: enum.Enum):
    return str(enum.name)

def enum_to_str_value(enum: enum.Enum):
    return str(enum.value)

def str_to_enum_name(enum_str: str):
    return MyEnum[enum_str].name

def str_to_enum_value(enum_str: str):
    return MyEnum[enum_str].value

tuple_0 = ("one", 1, MyEnum.first)

print(tuple_0)
print(tuple_0[0])

print(enum_to_str_name(MyEnum.first))
print(enum_to_str_value(MyEnum.first))

print(str_to_enum_name("first"))
print(str_to_enum_value("first"))