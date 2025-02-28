from app import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert sub(4 - 2) == 2