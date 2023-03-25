# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
gen_0 = (x+x for x in range(5))

for i in gen_0:
    print(i)

print("---")

def create_generator_0():
    list_0 = range(5)
    print("generating with list", list_0)
    for x in list_0:
        yield x+x

gen_1 = create_generator_0()

for i in gen_1:
    print(i)

def create_generator_1():
    print("create generator with values")
    yield 1
    yield 2
    yield 3

for i in create_generator_1():
    print(i)