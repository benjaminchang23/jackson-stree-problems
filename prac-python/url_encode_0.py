import urllib.parse

target = "Hellö Wörld@Python"

encoded = urllib.parse.quote(target)

print(encoded)

target_1 = "s3://where/am/i"

encoded_1 = urllib.parse.quote(target_1, safe="/:")

print(encoded_1)