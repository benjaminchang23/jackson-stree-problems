# python exception list
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
# https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python

def value_error_func():
    raise ValueError("wrong value foo", "val1", "val2")

def internal_func():
    try:
        value_error_func()
    except ValueError as error:
        print(error.args)
        raise

try:
    internal_func()
except AssertionError as error:
    print(error.args)
    raise
except ValueError as error:
    print(error.args)
    raise