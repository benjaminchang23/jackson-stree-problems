paths = []
result = {}

try:
    contents = result.get("contents")
    if not contents:
        # AssertionError would be best prac
        raise Exception("no contents", contents)
except ValueError as error:
    print(error.args)
    raise
except AssertionError as error:
    print(error.args)
    raise
except Exception as error:
    print(error.args)
    raise
