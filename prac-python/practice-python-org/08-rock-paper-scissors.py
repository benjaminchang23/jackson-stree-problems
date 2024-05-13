# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock


from enum import Enum


class Hand(Enum):
    rock = 1
    paper = 2
    scissors = 3
    waiting = 4


class GameState(Enum):
    START = 1
    PLAYER_ONE_TURN = 2
    PLAYER_TWO_TURN = 3
    PLAYER_VICTORY = 4
    GAMEOVER = 5
    ERROR = 6


class GameContainer:
    def __init__(self):
        self._done = False
        self._game_state = GameState.START
        self._player_one_hand = Hand.waiting
        self._player_two_hand = Hand.waiting
        self._winning_player_num = 0
    
    def computer_winning_player(self):
        if self._player_one_hand == self._player_two_hand:
            print("Looks like the players tied!")
            self._game_state = GameState.PLAYER_ONE_TURN
            return
        if self._player_one_hand == Hand.rock and self._player_two_hand == Hand.paper:
            self._winning_player_num = 2
        elif self._player_one_hand == Hand.rock and self._player_two_hand == Hand.scissors:
            self._winning_player_num = 1
        elif self._player_one_hand == Hand.paper and self._player_two_hand == Hand.rock:
            self._winning_player_num = 1
        elif self._player_one_hand == Hand.paper and self._player_two_hand == Hand.scissors:
            self._winning_player_num = 2
        elif self._player_one_hand == Hand.scissors and self._player_two_hand == Hand.rock:
            self._winning_player_num = 2
        elif self._player_one_hand == Hand.scissors and self._player_two_hand == Hand.paper:
            self._winning_player_num = 1
        else:
            raise RuntimeError("should never reach this")
        self._game_state = GameState.PLAYER_VICTORY


def print_game_start():
    print("Welcome to rock paper scissors! Type exit or quit to exit at any time. Press enter to begin")


def print_hand_options(player_num: int):
    print(f"Player {player_num}, please input a hand from the following list: rock, paper, scissors")


def print_player_win(player_num: int):
    print(f"Player {player_num} is victorious! input y to start a new game input n to exit the program")


def print_game_end():
    print("Thank you for playing rock paper scissors!")


def handle_prompt(game_container: GameContainer):
    if game_container._game_state == GameState.START:
        print_game_start()
    elif game_container._game_state == GameState.PLAYER_ONE_TURN:
        print_hand_options(1)
    elif game_container._game_state == GameState.PLAYER_TWO_TURN:
        print_hand_options(2)
    elif game_container._game_state == GameState.PLAYER_VICTORY:
        print_player_win(game_container._winning_player_num)
    else:
        print("Error unknown game state")


def handle_player_hand_input(game_container: GameContainer, input: str, player_num: int):
    hand: Hand = Hand.waiting
    try:
        hand = Hand[input]
        if player_num == 1:
            game_container._player_one_hand = hand
            game_container._game_state = GameState.PLAYER_TWO_TURN
        else:
            game_container._player_two_hand = hand
            game_container.computer_winning_player()
    except KeyError as e:
        print(f"Could not parse: {e}")
    except ValueError as e:
        print(e)


def handle_gameover_input(game_container: GameContainer, input: str):
    if input == "y":
        game_container._game_state = GameState.PLAYER_ONE_TURN
    elif input == "n":
        print_game_end()
        game_container._done = True


def handle_input(game_container: GameContainer, input: str):
    if input == "exit" or input == "quit":
        game_container._done = True
        return

    if game_container._game_state == GameState.START:
        game_container._game_state = GameState.PLAYER_ONE_TURN
    elif game_container._game_state == GameState.PLAYER_ONE_TURN:
        handle_player_hand_input(game_container, input, 1)
    elif game_container._game_state == GameState.PLAYER_TWO_TURN:
        handle_player_hand_input(game_container, input, 2)
    elif game_container._game_state == GameState.PLAYER_VICTORY:
        handle_gameover_input(game_container, input)
    else:
        print("Error unknown game state")


def main():
    game_container: GameContainer = GameContainer()
    while not game_container._done:
        handle_prompt(game_container)
        try:
            echo: str = input()
        except Exception as e:
            print(f"error: {e}")
            return
        handle_input(game_container, echo)


if __name__ == "__main__":
    main()
