import json

dict_0 = {
    "clear": True,
}

print(dict_0)

print('{"clear": true}')

loaded_json = json.loads('{"clear": true}')

print(loaded_json)
