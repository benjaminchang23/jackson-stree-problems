# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. 
# Take this opportunity to practice using functions, described below.


# from https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
# modified to remove deprecation warning
import collections.abc
import functools
import sys
sys.setrecursionlimit(100000)


class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
       self.func = func
       self.cache = {}
    def __call__(self, *args):
       if not isinstance(args, collections.abc.Hashable):
          # uncacheable. a list, for instance.
          # better to not cache than blow up.
          return self.func(*args)
       if args in self.cache:
          return self.cache[args]
       else:
          value = self.func(*args)
          self.cache[args] = value
          return value
    def __repr__(self):
       '''Return the function's docstring.'''
       return self.func.__doc__
    def __get__(self, obj, objtype):
       '''Support instance methods.'''
       return functools.partial(self.__call__, obj)


@memoized
def recursive_is_prime_decreasing(num: int, check: int):
    if check == 1:
        return True
    elif num % check == 0:
        return False
    return recursive_is_prime_decreasing(num, check - 1)


@memoized
def recursive_is_prime_increasing(num: int, check: int):
    if num == check:
        return True
    elif num % check == 0:
        return False
    return recursive_is_prime_increasing(num, check + 1)


def main():
    print("Give me an integer to check if it is prime!")
    try:
        echo: str = input()
    except Exception as e:
        print(f"error: {e}")
        return
    print(f"recieved: {echo}")
    try:
        guess: int = int(echo)
        print(f"check for prime with increasing: {recursive_is_prime_increasing(guess, 2)}")
        print(f"check for prime with increasing: {recursive_is_prime_decreasing(guess, guess - 1)}")
    except ValueError as e:
        print(f"could not process: {echo} {e}")

if __name__ == "__main__":
    main()
