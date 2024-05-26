from typing import List, Optional

list_0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
list_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
list_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]


def chop(input_list: List, divider: int):
    print("========")
    lists = []
    total: Optional[int] = None 
    modulo = len(input_list) % divider
    integer_divide = len(input_list) // divider
    ten_per_divider = max(int(divider / 10), 1)
    print(f"modulo: {modulo}")
    print(f"integer_div: {integer_divide}")
    print(f"ten_per_divider: {ten_per_divider}")
    total = integer_divide
    if modulo != 0:
        if modulo > ten_per_divider:
            total = integer_divide + 1
    print(f"total: {total}")
    early_exit = False
    for x in range(total):
        if early_exit:
            break
        end_index = (x + 1) * divider
        print(f"end_index: {end_index} {len(input_list)}")
        compare = abs(len(input_list) - end_index)
        if compare <= ten_per_divider and compare != 0:
            end_index = len(input_list)
            early_exit = True
        lists.append(input_list[x * divider : end_index])
    print(f"lists: {lists}")
    print("")
    return total, lists

result, lists = chop([], 10)
assert result == 0
assert lists == []

result, lists = chop(list_0, 10)
assert result == 1
assert lists == [[1, 2, 3, 4, 5, 6, 7, 8, 9]]

result, lists = chop(list_1, 10)
assert result == 1
assert lists == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

result, lists = chop(list_2, 10)
assert result == 1
assert lists == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]

result, lists = chop(list_3, 10)
assert result == 2
assert lists == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13]]

result, lists = chop(list_4, 10)
assert result == 2
assert lists == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]

result, lists = chop(list_5, 10)
assert result == 2
assert lists == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]]

result, lists = chop(list_6, 10)
assert result == 3
assert lists == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22]]

result, lists = chop(list_7, 7)
assert result == 4
assert lists == [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23]]
