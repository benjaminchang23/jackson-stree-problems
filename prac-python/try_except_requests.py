from urllib import response
import requests

def do_get_request(url, headers):
    response = requests.request(
        "GET", url, headers=headers
    )
    print(response.status_code)
    print(response.json()["error"])
    return response.json()

def do_post_request(url, params, headers):
    response = requests.request(
        "POST", url, json=params, headers=headers
    )
    print(response.status_code)
    print(response)
    return response.json()

def except_test_0():
    url = "https://google.com"
    params = ["test-0"]
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    try:
        task = do_post_request(url, params, headers)
        print("Success")
        return task
    except Exception as e:
        print("reached exception")
        print("error", e)
        return None

def except_test_1():
    url = "https://api.scale.com/v1/task/576ba74eec471ff9b01557cc"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    try:
        task = do_get_request(url, headers)
        print("Success")
        return task
    except Exception as e:
        print("reached exception")
        print("error", e)
        return None

if __name__ == "__main__":
    print("start try except test 0")
    result_0 = except_test_0()
    print(result_0)

    print("start try except test 1")
    result_1 = except_test_1()
    print(result_1)