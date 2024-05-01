def inner_dec(func):
    def inner_func(*args, **kwargs):
        print(f"inner dec before {args} {kwargs}")
        func(*args, **kwargs)
        print(f"inner dec after {args} {kwargs}")
    return inner_func


def outer_dec(func):
    def inner_func(*args, **kwargs):
        print(f"outer dec before {args} {kwargs}")
        func(*args, **kwargs)
        print(f"outer dec after {args} {kwargs}")
    return inner_func

@inner_dec
@outer_dec
def print_hello(print_str: str):
    print(print_str)

print_hello("foo")
