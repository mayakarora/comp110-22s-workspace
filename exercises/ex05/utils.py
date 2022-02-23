"""First file of Ex05."""

__author__ = "730410153"


def only_evens(xs: list[int]) -> int:
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            return xs[i]
    i += 1


def sub(a_list: list[int], x: int, y: int) -> list:
    i: int = 0
    b_list: list[int] = [a_list[i]]
    c_list: list[int] = []
    while i >= x and i < y:
        if len(a_list) == 0 or x > len(a_list) or y <= 0:
            return c_list
        return b_list
    i += 1


def concat(one: list[int], two: list[int]) -> None:
    return one.extend(two)

# use how you expect fucntion ot be used -use
# edge- catches obscure weird function calls
    # most popular - represented by 0, empty or negative numbers