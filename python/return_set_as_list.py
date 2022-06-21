def get_list():
    l = []
    l.append("list one")
    l.append("list two")
    l.append("list one")

    return l

def get_transformed_set():
    s = set()
    s.add("one")
    s.add("one")
    s.add("two")

    return list(s)

if __name__ == "__main__":
    combine = {
        "list": get_list(),
        "set": get_transformed_set()
    }

    print(combine)