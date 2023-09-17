import json

element_dict = {}
element_dict["first_loc"] = ["first_info_0", "first_info_1"]
element_dict["second_loc"] = ["second_info_0", "second_info_1"]

print(element_dict)

attr_list = ["one", "two"]

data_frames = []

i = 0
for element in element_dict:
    combined = {}
    combined["ele_loc"] = element
    combined["ele_info"] = element_dict[element]
    combined["ele_attr"] = attr_list[i]
    data_frames.append(combined)
    i += 1

print(data_frames)

for data_frame in data_frames:
    data_dict = {}
    data_dict["file"] = data_frame["ele_loc"]
    data_dict["info"] = data_frame["ele_info"]
    data_dict["attr"] = data_frame["ele_attr"]
    json_str = json.dumps(data_dict)
    print(json_str)

simple_list = ["one", "two"]
simple_dict = {}

for element in simple_list:
    simple_dict[element] = {}
    simple_dict[element][2] = 1

print(simple_dict)
