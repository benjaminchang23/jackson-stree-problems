import json

array_str = "[{\"start\": 0, \"end\": 30},{\"start\": 0, \"end\": 30},{\"start\": 0, \"end\": 30}]"

print(array_str)

json_str = json.dumps(array_str)

print(json_str)