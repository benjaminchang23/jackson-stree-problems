# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.

from random import randrange


def print_game_start():
    print("Welcome to the guessing game! please input a number between 1 and 9 (inclusive)")


def main():
    guess_count: int = 0
    lower_limit: int = 1
    upper_limit: int = 9
    random_num: int = randrange(lower_limit, upper_limit)
    done: bool = False
    print_game_start()
    while not done:
        try:
            echo = input()
        except Exception as e:
            print(f"error: {e}")
            return
        print(f"recieved: {echo}")
        if echo == "exit" or echo == "quit":
            return
        try:
            guess: int = int(echo)
            if guess < lower_limit or guess > upper_limit:
                print(f"input a number between 1 and 9 (inclusive)")
                continue
            guess_count += 1
            if guess == random_num:
                plural_str = "try" if guess_count == 1 else "tries"
                print(f"Congradulations! you won in {guess_count} {plural_str}")
                done = True
            elif guess > random_num:
                print("Too high")
            else:
                print("Too Low")
        except ValueError as e:
            print(f"could not process: {echo} {e}")
            continue


if __name__ == "__main__":
    main()
