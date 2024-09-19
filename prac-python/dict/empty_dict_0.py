dict_0 = {}

dict_0["foo"] = 1

list_0 = dict_0.get("list")

if list_0 is None:
    print("list_0 none")
else:
    for element in list_0:
        print(element)
assert list_0 is None

if dict_0.get("list"):
    print("exist")
else:
    print("not exist")

print("")

if not dict_0.get("list"):
    print("not exist")
else:
    print("exist")

assert not dict_0.get("list")

print(dict_0.get("foo"))
assert dict_0.get("foo")
