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

def str_to_enum(enum_str: str):
    return MyEnum[enum_str]

def str_to_enum_name(enum_str: str):
    return MyEnum[enum_str].name

def str_to_enum_value(enum_str: str):
    return MyEnum[enum_str].value

tuple_0 = ("one", 1, MyEnum.first)

print(tuple_0)
print(tuple_0[0])

print(MyEnum.second.value)

print(f"enum_to_str_name: {enum_to_str_name(MyEnum.first)}")
print(f"enum_to_str_value: {enum_to_str_value(MyEnum.first)}")

print()

print(f"str_to_enum: {str_to_enum('first')}")
print(f"str_to_enum_name: {str_to_enum_name('first')}")
print(f"str_to_enum_value: {str_to_enum_value('first')}")

print()

try:
    print(str_to_enum("First"))
except KeyError as e:
    print(f"KeyError: {e}")

try:
    print(str_to_enum_name("First"))
except KeyError as e:
    print(f"KeyError: {e}")

try:
    print(str_to_enum_value("First"))
except KeyError as e:
    print(f"KeyError: {e}")
