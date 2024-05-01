def make_pretty(func):

    def inner():
        print("before func")
        func()
        print("after func")
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()