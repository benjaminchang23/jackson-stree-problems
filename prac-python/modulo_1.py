from typing import List


def check_list(locs: List):
    total = len(locs) // 50000
    if total == 0 and len(locs) != 0:
        total = 1
    print(total)

check_list([])

long_list = []
for x in range(0, 200):
    long_list.append(x)

check_list(long_list)
