big_list = ["a", "b", "c", "d", "e", "f"]

filter_list_0 = ["a", "c", "e"]
filter_list_1 = ["b", "d", "f"]
filter_list_2 = ["a", "z"]

if all(element in big_list for element in filter_list_0):
    print(0)
if all(element in big_list for element in filter_list_1):
    print(1)
if all(element in big_list for element in filter_list_2):
    print(2)