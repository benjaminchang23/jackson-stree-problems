from posixpath import split


f = open("/home/changb/Documents/CAT/elt-pipeline-project/1_1632233373.600/1_1632233373.600/lidar_smash/1632233374.950.pcd", "r")
contents = f.read()

split_contents = contents.split("\n")

print(split_contents[11])

points = split_contents[11:-1]

for point_str in points:
    point_dict = {}
    point = point_str.split(" ")
    point_dict["x"] = point[0]
    point_dict["y"] = point[1]
    point_dict["z"] = point[2]
    point_dict["i"] = 0.0
    print(point_dict)
