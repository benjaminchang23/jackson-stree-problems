import json

dict_0 = {
    "clear": True,
}
print(dict_0)
print('{"clear": true}')
loaded_json_0 = json.loads('{"clear": true}')
print(loaded_json_0)
print(f"dumps: {json.dumps(loaded_json_0)}")

dict_1 = {
    "clear": None,
}
print(dict_1)
print('{"clear": null}')
loaded_json_1 = json.loads('{"clear": null}')
print(loaded_json_1)
print(f"dumps: {json.dumps(loaded_json_1)}")
