dict_0 = {}

dict_0["one"] = 1
dict_0["two"] = 2

list_0 = [key for key in dict_0]

print(list_0)

list_1 = [key for key in dict_0 if key == "one"]

print(list_1)

list_2 = [
        key
        for key in dict_0
    ]

print(list_2)

list_3 = [
    key for key in dict_0
    if key == "two"
    if key != "one"
]

print(list_3)

list_4 = [key for key in dict_0 if (key == "one" or key == "two")]

print(list_4)
