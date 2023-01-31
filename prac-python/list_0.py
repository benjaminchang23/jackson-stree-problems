list_0 = []
list_0.append([1, "one"])
list_0.append([2, "two"])
list_0.append([3, "three"])
list_0.append([4, "four"])

list_str = str(list_0)

list_str_encode = list_str.encode()

print(list_str)

print(list_str_encode)

print(list_0)

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

list_1 = list_1 + list_2

print(list_1)

list_3 = []

if list_3:
    print("stuff in list")
else:
    print("nothing in list")