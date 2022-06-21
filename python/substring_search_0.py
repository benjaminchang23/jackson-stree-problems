def split_s3url_to_bucket_key(
    s3url: str,
):
    path_parts = s3url.replace("s3://", "").split("/")
    bucket = path_parts.pop(0)
    key = "/".join(path_parts)
    return bucket, key

word = "s3://ics-v-d3/project/unpacked/pg/site-pg/2022.05/2022.05.04/dummysn/name/extracted/findme/calibration/some-file.json"

bucket, key = split_s3url_to_bucket_key(word)

print("bucket: {}, key: {}".format(bucket, key))

result_0 = key.find("calibration")
print("calibration index: {}".format(result_0))
print("trunc: {}".format(key[:result_0 - 1]))

combine = "s3://" + bucket + "/" + key[:result_0] + "new-file.txt"

print(combine)

result_1 = word.rfind("/")
print("/ index: {}".format(result_1))
print("trunc: {}".format(word[:result_1]))