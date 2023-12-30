if not (True or True):
    print("true true")

if not (True or False):
    print("true true")

if not (False or True):
    print("true true")

if not (False or False):
    print("false false")


list_0 = ["a", "bcd", "def"]

for ele in list_0:
    if not("a" in ele or "b" in ele):
        print("not match: {}".format(ele))
        continue