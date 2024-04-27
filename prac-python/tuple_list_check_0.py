list_0 = [1, 2]
set_0 = set()

set_0.add(("a", 1))
set_0.add(("a", 2))
set_0.add(("b", 3))

for ele in list_0:
    if ("a", ele) in set_0:
        print("found")