from hello import add, fois, moins, div


def test_add():
    assert 2 == add(1, 1)

def test_fois():
    assert 4 == fois(2, 2)

def test_moins():
    assert 0 == moins(1, 1)

def test_div():
    assert 2 == div(4, 2)
