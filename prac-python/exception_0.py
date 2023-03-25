# python exception list
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
# https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python

def value_error_func():
    raise ValueError("wrong value foo", "val1", "val2")

try:
    value_error_func()
except ValueError as err:
    print(err.args)
