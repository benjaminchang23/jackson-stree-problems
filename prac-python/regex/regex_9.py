import re

file_list = [
        "s3://ics-1ahs-dev/Unpacked/23101TestCustomer/23101TestSite/2022.07/2022.07.18/Name5/base5/Snippets/snippetname2/extracted/channel5/123456789.00_2022-09-25.fifth_fifth.png",
        "s3://ics-1ahs-dev/Unpacked/23101TestCustomer/23101TestSite/2022.07/2022.07.188/Name6/base6/Snippets/snippetname3/ErrorData/channel6/123456789.00_2022-09-26.sixth_sixth.png",
        "s3://ics-sam-dev/Staging/customer1/test1/2022-00-00t00-00-00.123456_hash.bag",
        "s3://ics-sam-dev/Staging/test1/2022-00-00t00-00-00.123456_hash.bag",
      ]

for file_path in file_list:
    try:
        if "Staging" in file_path:
            search_res = re.search("([a-zA-Z0-9_.%\-~/:']+/"
                                    "Staging/"
                                    "[a-zA-Z0-9_.%\-~:']+/"
                                    "[a-zA-Z0-9_.%\-~']+)/", file_path)
        else:
            search_res = re.search("([a-zA-Z0-9_.%\-~/:']+/"
                                    "[0-9]{4}\.[0-9]{2}/"
                                    "[0-9]{4}\.[0-9]{2}\.[0-9]{2}/"
                                    "[a-zA-Z0-9_.%\-~']+/"
                                    "[a-zA-Z0-9_.%\-~']+)", file_path)
        if search_res is not None:
            print("found: {}".format(search_res.group(1)))
        else:
            print("could not find in: {}".format(file_path))
    except AttributeError:
        pass