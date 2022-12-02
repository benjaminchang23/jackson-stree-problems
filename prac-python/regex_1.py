import re
from typing import List

log_list = []

log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/some/s3/path/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/some/s3/path/longer/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/some/s3/path/longest/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/some/s3/path/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/some/s3/path/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/some/s3/path/longest/longest/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/short_log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base1/less/short_log.log")

log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base2/some/s3/path/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base2/some/s3/path/longer/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base2/some/s3/path/longest/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base2/some/s3/path/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base2/some/s3/path/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base2/some/s3/path/longest/longest/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base2/short_log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/base2/less/short_log.log")

log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name2/base1/some/s3/path/short_log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name2/base1/some/s3/path/short_log.log")
log_list.append("s3://foo-bar/Unpacked1/TestCustom/TestLoc/2022.07/2022.07.18/Name2/base1/some/s3/path/short_log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom1/TestLoc/2022.07/2022.07.18/Name2/base2/some/s3/path/short_log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc1/2022.07/2022.07.18/Name2/base2/some/s3/path/short_log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.08/2022.07.18/Name2/base2/some/s3/path/short_log.log")

base_name_set = set()
dict_0 = {}

for log_path in log_list:
    print("Processing: {}".format(log_path))
    try:
        # 
        # https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html
        # https://linuxhint.com/extract-substring-regex-python/
        # https://stackoverflow.com/questions/14909777/what-does-the-1-in-match-group1-mean
        search_res = re.search("[a-zA-Z0-9_.%\-~/:]+/[0-9]{4}\.[0-9]{2}/[0-9]{4}\.[0-9]{2}\.[0-9]{2}/[a-zA-Z0-9_.%\-~]+/([a-zA-Z0-9_.%\-~]+)", log_path)
        found = None
        if search_res is None:
            print("could not match: {}".format(log_path))
            continue
        else:
            found = search_res.group(0)
            print(found)
        if not found:
            continue
        if found not in dict_0:
            dict_0[found] = [log_path]
        else:
            dict_0[found].append(log_path)
    except AttributeError:
        pass
    
# for element in dict_0:
#     print("element: {}".format(element))
#     print(dict_0[element])
