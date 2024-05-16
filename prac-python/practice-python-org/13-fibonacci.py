# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


_simple_memo = [1, 1]


def fibonnaci_helper(count: int):
    for x in range(len(_simple_memo), count):
        _simple_memo.append(_simple_memo[x - 1] + _simple_memo[x - 2])


def fibonnaci(count: int):
    if count == 0:
        return 0
    if count > len(_simple_memo):
        # increase size of memo
        fibonnaci_helper(count)
        return _simple_memo[count - 1]
    else:
        return _simple_memo[count - 1]


def main():
    print("Welcome to a simple Fibonnaci number generator! Input the number of Fibonnaci numbers to generate!")
    try:
        echo: str = input()
    except Exception as e:
        print(f"error: {e}")
        return
    print(f"recieved: {echo}")
    try:
        count: int = int(echo)
        fib_list = []
        # pre-calculate the fibonnaci seq
        fibonnaci(count)
        for x in range(count):
            fib_list.append(fibonnaci(x))
        print(f"{fib_list}")
        print(f"memo len: {len(_simple_memo)}")
    except ValueError as e:
        print(f"could not process: {echo} {e}")


if __name__ == "__main__":
    main()
