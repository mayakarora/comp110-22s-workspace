"""EX02 - One Shot Wordle!"""

__author__ = "730410153"

secret: str = "python"
star: int = len(secret)
word: str = input(f"What is your {star}-letter guess? ")
GREEN_BOX: str = "\U0001F7E9"
WHITE_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
final_string = ""

while len(word) != len(secret):
    word: str = input(f"That was not {star} letters! Try again: ")
while i < len(word):
    if word[i] == secret[i]:
        final_string += GREEN_BOX
    else:
        yellow: bool = False
        idx: int = 0
        while not yellow and idx < len(word):
            if secret[idx] == word[i]:
                yellow: bool = True
            else:  
                idx += 1
        if yellow is True:
            final_string += YELLOW_BOX
        else:
            final_string += WHITE_BOX
    i += 1
print(final_string)   
if word == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")