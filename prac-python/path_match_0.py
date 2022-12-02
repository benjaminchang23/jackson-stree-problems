def get_close_path(needle, haystack):
    # print("closet to {} in {}".format(needle, haystack))
    match = None
    match_len = 0
    needle_split = needle.split('/')
    for hay in haystack:
        hay_split = hay.split('/')
        hay_match_len = 0
        for i in range(len(hay_split) - 1):
            # needle_split not long enough for compare
            if i > len(needle_split) - 1:
                break
            if hay_split[i] == needle_split[i]:
                hay_match_len += 1
            else:
                break
        if hay_match_len > match_len:
            # print("{}, {}".format(hay_match_len, match_len))
            match = hay
            match_len = hay_match_len
                
    return match


list_0 = []

list_0.append("s3://bucket/some/s3/path/file.json")
list_0.append("s3://bucket/some/s3/path/longer/file.json")
list_0.append("s3://bucket/some/s3/path/longest/file.json")

list_1 = []

list_1.append("s3://bucket/some/s3/path/log.log")
list_1.append("s3://bucket/some/s3/path/longer/log.log")
list_1.append("s3://bucket/some/s3/path/longest/log.log")
list_1.append("s3://bucket/some/s3/path/log.log")
list_1.append("s3://bucket/some/s3/path/log.log")
list_1.append("s3://bucket/some/s3/path/longest/longest/log.log")
list_1.append("s3://bucket/short_log.log")
list_1.append("s3://bucket/less/short_log.log")

combined = []
for list_1_rep in list_1:
    # print(list_1_rep.split('/'))
    match = get_close_path(list_1_rep, list_0)
    print(match)