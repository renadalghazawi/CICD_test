from newmath.add import add
from newmath.mul import mul

import sys

BIGMAX=sys.maxsize



def test_add_bigmax():
    assert add(BIGMAX, 2) > BIGMAX
    assert add(5, BIGMAX) > BIGMAX
    assert add(BIGMAX, BIGMAX) > BIGMAX
    # Subtraction
    assert add(-1, BIGMAX) < BIGMAX


def test_mul_bigmax():
    assert mul(BIGMAX, 2) > BIGMAX
    assert mul(5, BIGMAX) > BIGMAX
    assert mul(BIGMAX, BIGMAX) > BIGMAX

    assert mul(BIGMAX, 0) == 0