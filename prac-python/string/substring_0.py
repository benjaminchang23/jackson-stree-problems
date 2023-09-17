str_0 = "hi.my.name.is"

str_1 = "hi"

final = str_1 + "." + str_0

print(final)

if str_0.startswith("hi"):
    res = str_0.find(".")
    print(final[res + 1:])