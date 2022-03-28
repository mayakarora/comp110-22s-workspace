"""First file of Ex05."""

__author__ = "730410153"


def only_evens(xs: list[int]) -> list[int]:
    """Returns only even values of a given list."""
    i: int = 0
    index: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            index.append(xs[i])
        i += 1
    return index


def sub(a_list: list[int], x: int, y: int) -> list[int]:
    """Returns indices of a list between the values of given integers."""
    i: int = 0
    c_list: list[int] = []
    if len(a_list) == 0 or x >= len(a_list) or y <= 0:
        return c_list
    if x < 0:
        newx: int = 0
        if y > len(a_list):
            newy: int = len(a_list)
            while i >= newx and i <= newy:
                c_list.append(a_list[i])
                i += 1
            return c_list
        while i >= newx and i < y:
            c_list.append(a_list[i])
            i += 1
        return c_list
    if i <= x:
        newi: int = x
        if y > len(a_list):
            againy: int = len(a_list) - 1
            while newi >= x and newi <= againy:
                c_list.append(a_list[newi])
                newi += 1
            return c_list
        while newi >= x and newi < y:
            c_list.append(a_list[newi])
            newi += 1
    return c_list


def concat(one: list[int], two: list[int]) -> list[int]:
    """Combines lists."""
    i: int = 0
    if len(two) < 0:
        return one
    while i < len(two):
        one.append(two[i])
        i += 1
    return one
# use how you expect function to be used -use
# edge- catches obscure weird function calls
    # most popular - represented by 0, empty or negative numbers