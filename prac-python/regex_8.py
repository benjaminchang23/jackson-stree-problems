import re
from typing import List

file_list = ["s3://ics-1ahs-dev/Unpacked/23101TestCustomer/23101TestSite/2022.07/2022.07.18/Name7/base7/Snippets/snippetname4/3DSceneFrames/channel7/1234567890.json"]

for file_path in file_list:
    print("Processing: {}".format(file_path))
    try:
        # https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html
        # https://linuxhint.com/extract-substring-regex-python/
        # https://stackoverflow.com/questions/14909777/what-does-the-1-in-match-group1-mean
        search_res = re.search("([a-zA-Z0-9_.%\-~/:']+/"
                                "[0-9]{4}\.[0-9]{2}/"
                                "[0-9]{4}\.[0-9]{2}\.[0-9]{2}/"
                                "[a-zA-Z0-9_.%\-~']+/"
                                "[a-zA-Z0-9_.%\-~']+/"
                                "[Snippets|snippets]+/"
                                "[a-zA-Z0-9_.%\-~']+/"
                                "[3DSceneFrames]+/"
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
