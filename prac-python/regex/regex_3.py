import re

file_list = []

file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel/123456789.00_2022-09-22.first_first.png")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel/123456789.00_2022-09-22.second_second.jpg")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel/123456789.00_2022-09-22.third_third.json")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel/123456789.00_2022-09-22.fourth_fourth.pcd")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted//123456789.00_2022-09-22.fourth_fourth.pcd")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel/-09-22.fourth_fourth.pcd")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel/123456789.00.png")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel/123456789.00.jpg")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel/123456789.00.json")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel/123456789.00.pcd")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel/123456789.00_2022.png")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2021.06/2021.06.09/RDR00377/_2021-06-18-16-59-21_4.bag/Annotations/Fcam1/12345678.2345678.jpg")

for file in file_list:
    print("Processing: {}".format(file))
    # https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html
    search_res = re.search("[a-zA-Z0-9_.%\-~/:]+/"
                "[0-9]{4}\.[0-9]{2}/"
                "[0-9]{4}\.[0-9]{2}\.[0-9]{2}/"
                "[a-zA-Z0-9_.%\-~/:]+/"
                "extracted/"
                "[a-zA-Z0-9_.%\-~/:]+/"
                "[0-9.]+_(.+?).[a-zA-Z0-9]+$", file)
    found = None
    if search_res is None:
        continue
    else:
        found = search_res.group(1)
        print("regex found: {}".format(found))
    if not found:
        print("regex fail")
        continue
        