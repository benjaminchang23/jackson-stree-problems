list_0 = []
dict_0 = {"one": "one1", "two": "two2"}
dict_1 = {"one": "three3", "two": "four4"}
list_0.append(dict_0)
list_0.append(dict_1)

print(list_0)

list_1 = [["one1", "two2"], ["three4", "four3"]]

for ele in list_0:
    if [ele["one"], ele["two"]] in list_1:
        print(ele)

print("adding a dict rep to a list of str")

unknown_values = ["unknown0", "unknown1"]

dict_2 = {"known-key": unknown_values}

print(dict_2.__str__())