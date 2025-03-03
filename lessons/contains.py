"""Example of a function that searches through a list."""


def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Pete Davidson"]))



# Define a function named contains
# Two parameters
# 1. needle - the string we're seraching for
# 2. haystack- the list we're searching through
def contains(needle: str, haystack: list[str]) -> bool:
    # Algorithm:
    #   For each item in the haystack
    #       Test if it is equal to needle
    #       if so, return True
    for item in haystack:
        if item == needle:
            return True    
#   After testing all items, return False, because not found
# Returns true if need in haystack, false otherwise
    return False


if __name__ == "__main__":
    main()
else:
    print(__name__)