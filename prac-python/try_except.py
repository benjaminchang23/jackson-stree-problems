def force_except():
    assert( 0 == 1)
    return "passed force except"

def except_test():
    try:
        task = force_except()
        print("Success")
        return task
    except Exception as e:
        # we don't raise exception here because we want other tasks to be uploaded as well
        print("reached exception")
        print("error", e)
        return None

if __name__ == "__main__":
    print("start try except test")
    result = except_test()
    print(result)