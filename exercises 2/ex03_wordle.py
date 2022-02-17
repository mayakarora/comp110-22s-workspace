"""The real Wordle!"""

__author__ = "730140153"

GREEN_BOX: str = "\U0001F7E9"
WHITE_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"
space = ""


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
    color: str = " "
    assert len(guess) == len(secret)
    ind: int = 0
    while ind < len(secret):
        if guess[ind] == secret[ind]:
            color += GREEN_BOX
        else:
            if contains_char(secret, guess[ind]) is True:
                color += YELLOW_BOX
            else:
                color += WHITE_BOX
        ind += 1


def input_guess(number: int) -> str:
    attempt: str = input(f"Enter a {number} character word: ")
    while number != len(attempt):
        input(f"That wasn't {number} characters! Try again: ")
    else:
        print(attempt)

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    length: int = len(secret)
    if input_guess(number) 
