import re
from typing import List

def match_path(
    path: str,
    file_list: List[str],
):
    match = None
    for file in file_list:
        rfind_res = file.rfind("/")
        prefix_path = file[:rfind_res + 1]
        if path.startswith(prefix_path):
            print("{} starts with {}".format(path, prefix_path))
            return file
    return match


log_list = []

log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/some/s3/path/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/some/s3/path/longer/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/some/s3/path/longest/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/some/s3/path/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/some/s3/path/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/some/s3/path/longest/longest/log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/short_log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/less/short_log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name2/short_log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name2/short_log.log")
log_list.append("s3://foo-bar/Unpacked1/TestCustom/TestLoc/2022.07/2022.07.18/Name2/short_log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom1/TestLoc/2022.07/2022.07.18/Name2/short_log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc1/2022.07/2022.07.18/Name2/short_log.log")
log_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.08/2022.07.18/Name2/short_log.log")

json_list = []

json_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/0123456789.json")
json_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name2/0123456789.json")
json_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/20221.07/2022.07.18/Name/0123456789.json")
json_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.071/2022.07.18/Name/0123456789.json")
json_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/20221.07.18/Name/0123456789.json")
json_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.071.18/Name/0123456789.json")
json_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.181/Name/0123456789.json")
json_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name1/0123456789.json")

json_list.append("s3://foo-bar1/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/0123456789.json")
json_list.append("s3://foo-bar/Unpacked1/TestCustom/TestLoc/2022.07/2022.07.18/Name/0123456789.json")
json_list.append("s3://foo-bar/Unpacked/TestCustom1/TestLoc/2022.07/2022.07.18/Name/0123456789.json")
json_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc1/2022.07/2022.07.18/Name/0123456789.json")
json_list.append("2022.07/2022.07.18/Name/0123456789.json")
json_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/a0123456789.json")
json_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/01234b56789.json")
json_list.append("s3://foo-bar/Unpacked/TestCustom/TestLoc/2022.07/2022.07.18/Name/0123456789c.json")

filtered_json_list = []

for json_file in json_list:
    print("Processing: {}".format(json_file))
    if re.match("^.+/[0-9]{4}\.[0-9]{2}/[0-9]{4}\.[0-9]{2}\.[0-9]{2}/\w+/[a-z-0-9]*.json$", json_file):
        print("Add json: {}".format(json_file))
        filtered_json_list.append(json_file)

for log in log_list:
    matched_json = match_path(log, filtered_json_list)
    print("Matched json: {}".format(matched_json))