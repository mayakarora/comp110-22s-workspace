"""Tests for dictionary functions."""

__author__ = "730410153"


from dictionary import invert, favorite_color, count


def test_invert_edge() -> None:
    """Edge case test of invert function."""
    y: dict[str, str] = {}
    assert invert(y) == {}


def test_invert_use1() -> None:
    """Use case test 1 of invert function."""
    colors: dict[str, str] = {"blue": "green", "purple": "yellow"}
    assert invert(colors) == {"green": "blue", "yellow": "purple"}


def test_invert_use2() -> None:
    """Use case test 2 of invert function."""
    names: dict[str, str] = {"Maya": "Vidya", "Maria": "Giana"}
    assert invert(names) == {"Vidya": "Maya", "Giana": "Maria"}


def test_favorite_color_edge() -> None:
    """Edge case test of favorite color function."""
    empty: dict[str, str] = {}
    assert favorite_color(empty) == ""


def test_favorite_color_use1() -> None:
    """Use case test 1 of favorite color dictionary."""
    dict_1: dict[str, str] = {"Maya": "green", "Andrea": "purple", "Maria": "green", "Mary Lacey": "purple"}
    assert favorite_color(dict_1) == "green"


def test_favorite_color_use2() -> None:
    """Use case test 1 of favorite color dictionary."""
    dict_2: dict[str, str] = {"Maya": "purple", "Andrea": "green", "Maria": "purple", "Mary Lacey": "purple"}
    assert favorite_color(dict_2) == "purple"


def test_count_edge() -> None:
    """Edge case test of count function."""
    empty: list[str] = []
    assert count(empty) == {}


def test_count_use1() -> None:
    """Use case test 1 of count function."""
    animals: list[str] = ["dog", "cat", "cat", "cat"]
    assert count(animals) == {"dog": 1, "cat": 3}


def test_count_use2() -> None:
    """Use case test 2 of count function."""
    foods: list[str] = ["popcorn", "bagel", "goldfish", "bagel"]
    assert count(foods) == {"bagel": 2, "goldfish": 1, "popcorn": 1}
