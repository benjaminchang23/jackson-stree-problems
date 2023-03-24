import time

def force_except():
    assert( 0 == 1)
    return "passed force except"

def except_test():
    retry_num = 0
    while retry_num < 3:
        retry_num = retry_num + 1
        try:
            task = force_except()
            print("Success")
            return task
        except Exception as e:
            print("reached exception retry num: {}".format(retry_num))
            print(retry_num)
            time.sleep(retry_num)
            if retry_num >= 3:
                raise Exception("Error occured: {}".format(e))

if __name__ == "__main__":
    print("start try except test")
    result = except_test()
    print(result)