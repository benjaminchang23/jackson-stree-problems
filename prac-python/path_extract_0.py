import re
from typing import List

image_list = []

image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base_name1/s3/path/log.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base_name1/s3/path/longer/log.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base_name1/s3/path/longest/log.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base.name2/s3/path/log.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base.name2/s3/path/log.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base.name2/s3/path/longest/longest/log.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base.name2/some_image.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base_name3/less/some_image.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name2/base_name1/some_image.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name2/base_name1/some_image.image")
image_list.append("s3://foo-bar/Unpacked1/TestCustom/TestLoc/2022.07/2022.07.18/Name2/base_name1/some_image.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom1/TestLoc/2022.07/2022.07.18/Name2/base.name2/some_image.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc1/2022.07/2022.07.18/Name2/base.name2/some_image.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.08/2022.07.18/Name2/base_name3/some_image.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.08/2022.07.18/Name2/base_name3/funky path/some_image.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.08/2022.07.18/Name2/base_name3/funky°path/some_image.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.08/2022.07.18/Name2/base_name3/funkyÂpath/some_image.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.08/2022.07.18/Name2/base_name3/funky%20path/some_image.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.08/2022.07.18/Name2/base_name3/funky%C2%B0path/some_image.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.08/2022.07.18/Name2/base_name3/funky%C3%82path/some_image.image")
image_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.08/2022.07.18/Name2/base_name4/funky%C3%82path/some_image.image")
image_list.append("funky%C3%82path/some_image.image")

base_name_set = set()
dict_0 = {}

for image_path in image_list:
    print("Processing: {}".format(image_path))
    try:
        # https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html
        # https://linuxhint.com/extract-substring-regex-python/
        # https://stackoverflow.com/questions/14909777/what-does-the-1-in-match-group1-mean
        search_res = re.search("/[0-9]{4}\.[0-9]{2}/[0-9]{4}\.[0-9]{2}\.[0-9]{2}/(\w+/[a-zA-Z0-9_.]+/)", image_path)
        if search_res is None:
            print("could not match: {}".format(image_path))
            continue
        else:
            found = search_res.group(1)
        if not found:
            continue
        if found not in dict_0:
            dict_0[found] = [image_path]
        else:
            dict_0[found].append(image_path)
    except AttributeError:
        pass
    
for element in dict_0:
    print("element: {}".format(element))
    print(dict_0[element])
