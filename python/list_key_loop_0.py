base_dict_0 = {}
base_dict_0["one"] = 1
base_dict_0["two"] = 2
base_dict_0["three"] = 3

base_dict_1 = {}
base_dict_1["one"] = 2
base_dict_1["two"] = 3
base_dict_1["three"] = 4

base_list = []
base_list.append(base_dict_0)
base_list.append(base_dict_1)

some_list = []
some_list.append([1, 2])

for base in base_list:
    if [base["one"], base["two"]] in some_list:
        print("in some list")
    print(base)