start = 10
end = 22

for i in range(10, 22):
    print(i)

list_0 = [0, 1, 2, 3, 4]

print()

for i in range(len(list_0)):
    print(list_0[i])

print()

for i in range(0, len(list_0)):
    print(list_0[i])

print()

for i in range(0, 5):
    print(list_0[i])

print()

str_0 = "FIELDS a b c d e f"
line_0 = "0 1 2 3 4 5"
fields_list = str_0.split(" ")[1:]
fields_dict = {}
print(fields_list)

for i in range(len(fields_list)):
    fields_dict[fields_list[i]] = i

print(fields_dict)

point = line_0.split(" ")

dict_0 = {
    "a": point[fields_dict.get("a")],
    "b": point[fields_dict.get("b")],
    "c": point[fields_dict.get("c")],
}

print(dict_0)
