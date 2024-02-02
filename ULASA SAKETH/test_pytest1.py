import math_functions


def test_add_positive_numbers():
    assert math_functions.add(1, 2) == 3

def test_add_negative_numbers():
    assert math_functions.add(-1, -2) == -3

def test_add_mixed_numbers():
    assert math_functions.add(5, -3) == 2
