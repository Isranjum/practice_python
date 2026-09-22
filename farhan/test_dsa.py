import pytest
from dsa import two_sum

def test_two_sum():
    assert two_sum([1, 2, 3, 4, 5], 9) == [4, 5]


def test_two_sum_no_solution():
    assert two_sum([1, 2, 3], 10) == []

def test_two_sum_empty_inp():
    with pytest.raises(ValueError):
        two_sum([], 9)


def test_two_sum_with_negatives():
    assert two_sum([-5, -4, -3, -2, -1], -5) == [-4, -1]


