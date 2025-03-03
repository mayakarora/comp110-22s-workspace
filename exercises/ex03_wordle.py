"""The real Wordle!"""

__author__ = "730410153"

GREEN_BOX: str = "\U0001F7E9"
WHITE_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"
space = ""


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    i: int = 1
    result: bool = False
    while i <= 6 and result is False:
        print(f"=== Turn {i}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            result = True
        else:
            i += 1
    if result is True:
        print(f"You won in {i}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(number: int) -> str:
    """Hello, world."""
    attempt: str = input(f"Enter a {number} character word: ")
    while number != len(attempt):
        attempt = input(f"That wasn't {number} chars! Try again: ")
    else:
        return attempt


def contains_char(first: str, second: str) -> bool:
    """Searching the word for the character inputted."""
    assert len(second) == 1
    i: int = 0
    boolean: bool = False
    while i < len(first):
        if first[i] == second:
            return True
            boolean = True
        else:
            green: bool = False
            idx: int = 0
            while not green and idx < len(first):
                if first[idx] == second:
                    green = True
                else:
                    idx += 1
            if green is True:
                return True
                boolean = True
            else:
                return False
        i += 1
    return boolean


def emojified(guess: str, secret: str) -> str:
    """Printing colored boxes based on guess."""
    color: str = ""
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
    return color