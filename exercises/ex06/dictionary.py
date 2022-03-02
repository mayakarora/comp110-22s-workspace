"""Docstring"""


__author__ = "730410153"


def invert(x: dict[str, str]) -> dict[str, str]:
    """This function swaps the keys and value of a dictionary."""
    result: dict = {}
    for key in x:
        if x[key] in result:
            raise KeyError("Error, duplicate keys are present.")
        else:
            result[x[key]] = key 
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """This function returns the most frequent color."""
    my_dict: dict = {}
    for key in colors:
        if colors[key] in my_dict:
            my_dict[colors[key]] += 1
        else:
            my_dict[colors[key]] = 1
    counter: int = 0
    color: str = ""
    for key in my_dict:
        if my_dict[key] > counter:
            counter = my_dict[key]
            color = key
    return color


def count(values: list[str]) -> dict[str, int]:
    """This function produces a dictionary of the frequency of the items in the given list."""
    i: int = 0
    counts: dict = {}
    while i < len(values):
        if values[i] in counts:
            counts[values[i]] += 1
        else:
            counts[values[i]] = 1
        i += 1
    return counts