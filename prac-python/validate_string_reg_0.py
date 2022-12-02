import re

file_list = []

file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/0123456789.json")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/20221.07/2022.07.18/Name/0123456789.json")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.071/2022.07.18/Name/0123456789.json")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/20221.07.18/Name/0123456789.json")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.071.18/Name/0123456789.json")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.181/Name/0123456789.json")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name1/0123456789.json")

file_list.append("s3://foo-bar1/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/0123456789.json")
file_list.append("s3://foo-bar/Unpacked1/TestCustom/TestLoc/2022.07/2022.07.18/Name/0123456789.json")
file_list.append("s3://foo-bar/Unpacked/TestCustom1/TestLoc/2022.07/2022.07.18/Name/0123456789.json")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc1/2022.07/2022.07.18/Name/0123456789.json")
file_list.append("2022.07/2022.07.18/Name/0123456789.json")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/a0123456789.json")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/01234b56789.json")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/0123456789c.json")

for file in file_list:
    print("Processing: {}".format(file))
    if re.match("^.+/[0-9]{4}\.[0-9]{2}/[0-9]{4}\.[0-9]{2}\.[0-9]{2}/\w+/[a-z-0-9]*.json$", file):
        print("Matched: {}".format(file))