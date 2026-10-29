from main import add

def test_add():
    assert add(3, 3) == 5
    assert add(-1, 1) == 0