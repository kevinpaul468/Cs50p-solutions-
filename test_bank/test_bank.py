from bank import value
def test_hello():
    assert value("hello")==0
    assert value("Hello")==0
def test_h():
    assert value("hey")==20
    assert value("Hey")==20
def test_other():
    assert value("good morning")==100
    assert value("Good morning")==100