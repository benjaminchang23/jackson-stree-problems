list_0 = [1, 2, 3, 4, 5]
list_1 = []


for ele in list_0:
    print(ele)
    if ele % 2 == 0:
        list_1.append(ele)
    if ele == 3:
        break