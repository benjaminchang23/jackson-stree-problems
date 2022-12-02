file_list = []

file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel/123456789.00_2022-09-22.first_first.png")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel/123456789.00_2022-09-22.second_second.jpg")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel/123456789.00_2022-09-22.third_third.json")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel/123456789.00_2022-09-22.fourth_fourth.pcd")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted//123456789.00_2022-09-22.fourth_fourth.pcd")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel/-09-22.fourth_fourth.pcd")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel/123456789.00.png")

for file in file_list:
    print("Processing: {}".format(file))
    rfind_slash_res = file.rfind("/")
    find_under_res = file[rfind_slash_res + 1:].find("_")
    rfind_period_res = file.rfind(".")
    if rfind_slash_res == -1 or find_under_res == -1 or rfind_period_res == -1:
        print("error: {}".format(file))
    print("final: {}".format(file[rfind_slash_res + 1 + find_under_res + 1:rfind_period_res]))
