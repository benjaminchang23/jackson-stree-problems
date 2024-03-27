import enum

class MyEnum(enum.Enum):
    first = 1
    second = 2
    third = 3

tuple_0 = ("one", 1, MyEnum.first)

print(tuple_0)
print(tuple_0[0])