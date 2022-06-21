import json
from re import search as reg_search

if __name__ == "__main__":
    print("start extract task id test")
    response_raw = '{"status_code": 409, "error": "The unique_id (\'some-unique-id\') is already used for a different task (some-task_id)."}'
    response = json.loads(response_raw)

    # print(response)

    print("status code is: {}".format(response["status_code"]))
    print("error is: {}".format(response["error"]))
    print(response.status_code)

    split_error = response["error"].split(" ")[-1]
    task_id_substr = reg_search('\(([^)]+)', split_error).group(1)
    
    print(task_id_substr)

