dict_0 = {
    "1st": [1, 2, 3],
    "2nd": [4, 6, 5],
    "3rd": [7, 8, 9],
}

for key, value in dict_0.items():
    if key == "2nd":
        value.sort()
    print(f"{key} - {value}")