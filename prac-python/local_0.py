from typing import Optional

def widget_func(
    foo: Optional[str] = None,
    bar: Optional[int] = None,
):
    local = locals()
    print(f"local: {local}")
    print(f"foo: {foo}")
    print(f"bar: {bar}")
    foo += "goo"
    bar += 1
    print(f"local: {local}")
    print(f"foo: {foo}")
    print(f"bar: {bar}")
    print()

a = "foo"
b = 2
widget_func("foo", 2)

print(f"{a} - {b}")

widget_func(a, b)

print(f"{a} - {b}")
