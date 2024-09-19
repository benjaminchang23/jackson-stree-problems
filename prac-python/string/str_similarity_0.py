from typing import List

def find_closest_needle(needle, haystack: List[str]):
    split_needle_list = needle.split("/")
    search_str = needle
    for x in range(len(split_needle_list)):
        rfind_needle = search_str.rfind("/")
        check_str = needle[:rfind_needle + 1]
        search_str = needle[:rfind_needle]
        for hay in haystack:
            rfind_hay = hay.rfind("/")
            check_hay = hay[:rfind_hay + 1]
            print(f"check_str: {check_str} check_hay: {check_hay} full_hay: {hay}")
            if check_str == check_hay:
                return hay
    return None

haystack_contents = [
    "one/two/three/four/five/six/seven/some-uuid-0.json",
    "one/two/three/four/five/six/seven/id-1/some-uuid-1.json",
    "one/two/three/four/five/six/seven/id-2/some-uuid-2.json",
    "one/two/three/four/five/six/seven/id-3/some-uuid-3.json",
    "one/two/three/four/five/six/seven/id-4/some-uuid-4.json",
    "one/two/three/four/five/six/seven/some-uuid-5.json",
    "one/two/three/four/five/six/seven/some-uuid-6.json",
    "one/two/three/four/five/six/some-uuid-7.json",
]

needle_list = [
    "one/two/three/four/five/six/seven/id-1/obj.txt",
    "one/two/three/four/five/six/seven/id-1/obj.png",
    "one/two/three/four/five/six/seven/id-2/obj.txt",
    "one/two/three/four/five/six/seven/id-2/obj.png",
    "one/two/three/four/five/six/seven/id-3/obj.txt",
    "one/two/three/four/five/six/seven/id-3/obj.png",
    "one/two/three/four/five/six/seven/id-5/obj.png",
    "one/two/three/four/five/six/foo/id-5/obj.png",
    "foo",
]

hay_0 = haystack_contents[0]
hay_id_1 = haystack_contents[1]
hay_id_2 = haystack_contents[2]
hay_id_3 = haystack_contents[3]
hay_foo = haystack_contents[7]

haystack_contents.sort()

assert find_closest_needle(needle=needle_list[0], haystack=haystack_contents) == hay_id_1, f"{find_closest_needle(needle=needle_list[0], haystack=haystack_contents)} {hay_id_1}"
assert find_closest_needle(needle=needle_list[1], haystack=haystack_contents) == hay_id_1, f"{find_closest_needle(needle=needle_list[0], haystack=haystack_contents)} {hay_id_1}"

assert find_closest_needle(needle=needle_list[2], haystack=haystack_contents) == hay_id_2
assert find_closest_needle(needle=needle_list[3], haystack=haystack_contents) == hay_id_2

assert find_closest_needle(needle=needle_list[4], haystack=haystack_contents) == hay_id_3
assert find_closest_needle(needle=needle_list[5], haystack=haystack_contents) == hay_id_3

assert find_closest_needle(needle=needle_list[6], haystack=haystack_contents) == hay_0
assert find_closest_needle(needle=needle_list[7], haystack=haystack_contents) == hay_foo
assert find_closest_needle(needle=needle_list[8], haystack=haystack_contents) == None
