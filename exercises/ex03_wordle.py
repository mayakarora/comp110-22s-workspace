"""The real Wordle!"""

__author__ = 730140153


GREEN_BOX: str = "\U0001F7E9"
WHITE_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"
space = ""

def main() -> None:
    """The entrypoint of the program and main game loop."""
    i: int = 0
    ind: int = 0
    space = ""
    attempt: str = input(f"Enter a {number} character word: ")
    while i < 6:
        input(contains_char)
        input(emojified)
        input(input_guess)
        print(f"=== Turn {i}/6 ===")
        i += 1



def contains_char(first: str, second: str) -> bool:
    assert len(second) == 1
    """Searching the word for the character inputted."""
    i: int = 0
    while i < len(first):
        if first[i] == second:
            return True
        else:
            green: bool = False
            idx: int = 0
            while not green and idx < len(first):
                if first[idx] == second:
                    green: bool = True
                else:
                    idx += 1
            if green is True:
                return True
            else:
                return False
        i += 1


def emojified(guess: str, secret: str) -> str:
    """Printing colored boxes based on guess."""
    assert len(guess) == len(secret)
    ind: int = 0
    space = ""
    if contains_char is True:
        if guess[ind] == secret[ind]:
            space += GREEN_BOX
        else:
            space += YELLOW_BOX
    ind += 1
    if contains_char is False:
        space += WHITE_BOX


def input_guess(number: int) -> str:
    attempt: str = input(f"Enter a {number} character word: ")
    while number != len(attempt):
        input(f"That wasn't {number} characters! Try again: ")
    else:
        print(attempt)
