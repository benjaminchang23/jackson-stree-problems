dict_0 = {}

dict_0["top"] = {}
dict_0["top"]["entry1"] = ["e", "d"]
dict_0["top"]["entry2"] = ["c", "b"]

dict_0["bottom"] = {}
dict_0["bottom"]["entry1"] = ["z", "b"]
dict_0["bottom"]["entry2"] = ["y", "a"]

list_0 = ["e", "d"]
list_0.sort()

print(list_0)

print(dict_0)

dict_0 = {}

print(dict_0)

for top_or_bot in dict_0:
    for name in dict_0[top_or_bot]:
        unsorted = dict_0[top_or_bot][name]
        print("unsorted: {} - {}".format(name, unsorted))
        unsorted.sort()
        print("sorted: {} - {}".format(name, unsorted))

dict_1 = {"a": "b",
          "f": "g"}
dict_2 = {"a": "c",
          "d": "e"}
dict_1.update(dict_2)
print(dict_1)

