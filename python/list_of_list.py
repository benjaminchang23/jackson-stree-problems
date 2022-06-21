from typing import List

def process_list(
    base_logs: List[List[str]]
) -> List[List[str]]:

    results: List[List[str]] = []
    
    for base in base_logs:
        print("process: {}".format(base))
        print("{}".format(base[0]))
        print("{}".format(base[1]))

    return results

list1 = []
list1.append(["abc", "def"])
list1.append(["def", "ghi"])
print(list1)
print(list1[0][1])

list2 = [["abc", "def"], ["def", "ghi"]]

for element in list1:
    if element in list2:
        print("{} in list2".format(element))

process_list(list1)

print(list1[0])