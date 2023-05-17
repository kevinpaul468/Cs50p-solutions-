from plates import is_valid
def test_length():
    assert is_valid("abcdefg")==False
    assert is_valid("abcdef")==True
def test_letter():
    assert is_valid("a1234")==False
    assert is_valid("ab123")==True

def test_num_order():
    assert is_valid("ar1ae")==False
    assert is_valid("aae01")==False

def test_period_pun():
    assert is_valid("ab 123")==False
    assert is_valid("ab,123")==False