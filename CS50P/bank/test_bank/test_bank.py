from bank import value

def test_two_wrong():
    assert value("good day") == 100
    assert value("  labas dienas   ") == 100

def test_one_wrong():
    assert value("GOOD") == 100

def test_hello():
    assert value("hello") == 0
    assert value("HELLO bro") == 0

def test_h():
    assert value("hi") == 20
    assert value("hi bro") == 20