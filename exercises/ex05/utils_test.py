"""Second file of Ex05."""

__author__ = "730410153"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_edge() -> None:
    assert only_evens([17, 19, 43, 27, 90]) == []


def test_only_evens_use1() -> None:
    assert only_evens([1, 2, 5, 6, 7]) == [2, 6]


def test_only_evens_use2() -> None:
    assert only_evens([4, 14, 24, 35, 65]) == [4, 14, 24]


def test_sub_edge() -> None:
    assert sub([4, 13, 28, 45], -1, 5) == [4, 13, 28, 45]


def test_sub_use1() -> None:
    assert sub([4, 13, 28, 45], 1, 3) == [4, 13]


def test_sub_use2() -> None:
    assert sub([4, 13, 28, 45, 58, 67, 69, 78], 2, 5) == [13, 28, 45, 58]


def test_concat_edge() -> None:
    assert concat([], []) == []


def test_concat_use1() -> None:
    assert concat([3, 4, 5], [25, 35, 45]) == [3, 4, 5, 25, 35, 45]


def test_concat_use2() -> None:
    assert concat([2, 5, 9, 10, 13], [6]) == [2, 5, 9, 10, 13, 6]

    