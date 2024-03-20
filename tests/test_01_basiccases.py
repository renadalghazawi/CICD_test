from newmath.add import add
from newmath.mul import mul

def test_add():
    assert add(1, 2) == 3
    assert add(5, 7) == 12
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    
def test_mul():
    assert mul(1, 2) == 2
    assert mul(5, 7) == 35
    assert mul(-1, 1) == -1
    assert mul(0, 0) == 0