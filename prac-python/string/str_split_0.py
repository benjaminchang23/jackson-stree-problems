foo = "0,1,2,3,4,5,6,7,8,9,"

split_contents = foo.split(",")[:-1]
print(split_contents)

bar = "s3://home/of/the/brave/loc.json"
split_contents = bar.split("/")[:-1]
split_contents.remove("")
print(split_contents)

last_slash_index = bar.rfind("/")
print(bar[:last_slash_index])