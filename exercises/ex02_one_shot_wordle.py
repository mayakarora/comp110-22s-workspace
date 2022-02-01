"""EX02 - One Shot Wordle!"""

__author__ = "730410153"

word: str = "python"
star: int = len(word)
secret: str = input(f"What is your {star}-letter guess? ")
GREEN_BOX: str = "\U0001F789"
WHITE_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
mart: bool = False
list: int = len(word)

if len(secret) != len(word):
    while len(secret) != len(word):
        secret: str = input(f"That was not {star} letters! Try again: ")
if len(secret) == len(word):
    while i != len(secret):
        if secret[i] == word[i]:
            print(GREEN_BOX, end = " ")
            while mart and i < len(secret):
                for secret[i] in str(word):
                    mart == True
                    print(YELLOW_BOX, end = " ") 
            i = i + 1         
        else:
            print(WHITE_BOX, end = " ")
        i = i + 1
print(sep = " ")
if secret == word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")