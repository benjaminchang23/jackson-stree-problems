class SimpleClass:
    def __init__(self, x):
        self.val = x

list_0 = []

for x in range(0, 20):
    list_0.append(SimpleClass(x))

set_0 = set()

step = 6

print("{} elements with step: {}".format(len(list_0), step))

for x in range(0, len(list_0), step):
    nums = list_0[x:x+step]
    # nums_vals = []
    # for num in nums:
    #     nums_vals.append(num.val)
    nums_vals = [n.val for n in nums]
    print("step: {}".format(nums_vals))
    set_0.update(nums_vals)

print("end set: {}".format(set_0))