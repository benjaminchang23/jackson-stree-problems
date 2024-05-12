# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


from typing import List, Set

# memoize from https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator
from functools import lru_cache, wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.10f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap


@timing
def brute_force_with_decorator(my_int: int) -> List[int]:
    return brute_force(my_int)


def brute_force(my_int: int) -> List[int]:
    output_list = [1, my_int]
    half = int(my_int/2)
    for x in range(2, half + 1):
        if my_int % x == 0:
            output_list.append(x)
    return output_list


def brute_force_rev(my_int: int) -> List[int]:
    output_list = [1, my_int]
    half = int(my_int/2)
    for x in range(half, 1, -1):
        if my_int % x == 0:
            output_list.append(x)
    return output_list


@lru_cache
@timing
def memoize(my_int: int) -> List[int]:
    return brute_force_rev(my_int)


@lru_cache
def recursive(my_int: int, check: int) -> Set[int]:
    my_set = set()
    if check <= 1 or my_int <= 1:
        my_set.add(1)
        return my_set
    if my_int % check == 0:
        my_set.add(my_int)
        my_set.add(check)
        recursive_set = recursive(check, int(check/2))
        my_set.update(recursive_set)
    recursive_set = recursive(my_int, check - 1)
    my_set.update(recursive_set)
    return my_set


@timing
def recursive_helper(my_int: int):
    return recursive(my_int, int(my_int/2))


def main():
    print("Please input an integer for divisor listing.")
    try:
        echo: str = input()
        num: int = int(echo)
        brute_force_list = brute_force_with_decorator(num)
        print(brute_force_list)
        memoize_list = memoize(num)
        print(memoize_list)
        # can easily exceed the recursion depth for a python object
        recursive_set = recursive_helper(num)
        print(list(recursive_set))
    except ValueError as e:
        print(f"ValueError: {e}")
        return
    except Exception as e:
        print(f"error: {e}")
        return

if __name__ == "__main__":
    main()
