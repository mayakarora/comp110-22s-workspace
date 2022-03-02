"""Second file of Ex05."""

__author__ = "730410153"

from utils import only_evens, sub, concat


def test_only_evens_edge() -> None:
    """Edge case test of only evens function."""
    xs: list[int] = [17, 19, 43, 27]
    assert only_evens(xs) == []


def test_only_evens_use1() -> None:
    """Use case test 1 of only evens function."""
    xs: list[int] = [1, 2, 5, 6, 7]
    assert only_evens(xs) == [2, 6]


def test_only_evens_use2() -> None:
    """Use case test 2 of only evens function."""
    xs: list[int] = [4, 14, 24, 35, 65]
    assert only_evens(xs) == [4, 14, 24]


def test_sub_edge() -> None:
    """Edge case test of sub function."""
    xs: list[int] = [4, 13, 28, 45]
    assert sub(xs, -1, 3) == [4, 13, 28]


def test_sub_use1() -> None:
    """Use case test 1 of sub function."""
    xs: list[int] = [4, 14, 28, 45]
    assert sub(xs, 1, 3) == [14, 28]


def test_sub_use2() -> None:
    """Use case test 2 of sub function."""
    xs: list[int] = [4, 13, 28, 45, 58, 67, 69, 78]
    assert sub(xs, 2, 5) == [28, 45, 58]


def test_concat_edge() -> None:
    """Edge case test of concat function."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_use1() -> None:
    """Use case test 1 of concat function."""
    xs: list[int] = [3, 4, 5]
    ys: list[int] = [25, 35, 45]
    assert concat(xs, ys) == [3, 4, 5, 25, 35, 45]


def test_concat_use2() -> None:
    """Use case test 2 of concat function."""
    xs: list[int] = [2, 5, 9, 10, 13]
    ys: list[int] = [6]
    assert concat(xs, ys) == [2, 5, 9, 10, 13, 6]