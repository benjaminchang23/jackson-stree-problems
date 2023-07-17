dict_0 = {
    "key1": [
        "aa",
        "a",
        "aaa"
    ],
    "key3": [
        "c",
        "cc",
        "ccc"
    ],
    "key2": [
        "bbb",
        "bb",
        "b"
    ]
}

for key in dict_0:
    curr_list = dict_0.get(key)
    curr_list.sort()
    print(f"{key} - {curr_list}")