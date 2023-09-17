import re
from typing import List

file_list = []

file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/ExtractedData/channel1/123456789.00_2022-09-22.first_first.png")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/ExtractedData/channel1/123456789.00_2022-09-22.second_second.jpg")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/ExtractedData/channel1/123456789.00_2022-09-22.third_third.json")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/ExtractedData/channel1/123456789.00_2022-09-22.fourth_fourth.pcd")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/ExtractedData//123456789.00_2022-09-22.fourth_fourth.pcd")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/ExtractedData/channel2/-09-22.fourth_fourth.pcd")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/ExtractedData/channel2/123456789.00.png")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/ExtractedData/channel2/123456789.00.jpg")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/ExtractedData/channel2/123456789.00.json")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/ExtractedData/channel2/123456789.00.pcd")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/ExtractedData/channel2/123456789.00_2022.png")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2021.06/2021.06.09/RDR00377/_2021-06-18-16-59-21_4.bag/Annotations/Fcam1/12345678.2345678.jpg")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel2/123456789.00_2022.png")
file_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel2/123456789.00_2022.png")
file_list.append("s3://foo-bar/grob/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/extracted/channel2/123456789.00_2022.png")
file_list.append("s3://foo-bar/grob/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/ExtractedData/channel2/123456789.00_2022.png")
file_list.append("s3://foo-bar/grob/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/Snippets/snippetname1/ExtractedData/channel2/123456789.00_2022.png")
file_list.append("s3://foo-bar/grob/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/Snippets/snippetname1/extracted/channel2/123456789.00_2022.png")


for file_path in file_list:
    print("Channel extract: {}".format(file_path))
    try:
        # https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html
        # https://linuxhint.com/extract-substring-regex-python/
        # https://stackoverflow.com/questions/14909777/what-does-the-1-in-match-group1-mean
        search_res = re.search("Unpacked/"
                               "[a-zA-Z0-9_.%\-~/:]+/"
                               "[0-9]{4}\.[0-9]{2}/"
                               "[0-9]{4}\.[0-9]{2}\.[0-9]{2}/"
                               "[a-zA-Z0-9_.%\-~/]+/"
                               "(ExtractedData|extracted)/"
                               "([a-zA-Z0-9_.%\-~]+)", file_path)
        found = None
        if search_res is None:
            print("could not match: {}".format(file_path))
            continue
        else:
            found = search_res.group(2)
            print(found)
        if not found:
            continue
    except AttributeError:
        pass
