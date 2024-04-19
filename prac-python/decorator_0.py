def inner_dec(func):
    def inner_func(*args, **kwargs):
        print("inner dec before")
        func(*args, **kwargs)
        print("inner dec after")
    return inner_func(func)


def outer_dec(func):
    def inner_func(*args, **kwargs):
        print("outer dec before")
        func(*args, **kwargs)
        print("outer dec after")
    return inner_func(func)

@inner_dec
@outer_dec
def print_hello(print_str: str):
    print(print_str)

