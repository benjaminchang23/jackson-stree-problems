import re
from typing import List

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
file_list.append("s3://foo-bar/Unpacked/Test's%20Custom/TestLoc/2021.06/2021.06.09/RDR00377/_2021-06-18-16-59-21_4.bag/Annotations/Fcam1/12345678.2345678.jpg")
file_list.append("s3://ics-vision-dev-de-eu1-bucket/ICS-MSC/Unpacked/Dan's%20Excavating/Site036/2020.12/2020.12.09/SGJ20014/2020.12.09_Wed_18.33.53_450_451_Site036/extracted/emos_rear/2020.12.09_Wed_18.33.53_450_451_Site036_BoxY_950M_Front_Cam57_Rear_Cam58_EMOS180%C3%82%C2%B00186000_H264_Front_Ht3.437mRear_Ht1.984m_FrontAndRear_Pitch30%C3%82%B0down_rear_cam_00005.png")

for file_path in file_list:
    print("Processing: {}".format(file_path))
    try:
        # https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html
        # https://linuxhint.com/extract-substring-regex-python/
        # https://stackoverflow.com/questions/14909777/what-does-the-1-in-match-group1-mean
        search_res = re.search("[a-zA-Z0-9_.%\-~/:']+/"
                                "[0-9]{4}\.[0-9]{2}/"
                                "[0-9]{4}\.[0-9]{2}\.[0-9]{2}/"
                                "([a-zA-Z0-9_.%\-~']+/"
                                "[a-zA-Z0-9_.%\-~']+)", file_path)
        found = None
        if search_res is None:
            print("could not match: {}".format(file_path))
            continue
        else:
            found = search_res.group(0)
            print(found)
        if not found:
            continue
    except AttributeError:
        pass
