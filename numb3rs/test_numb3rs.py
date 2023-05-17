from numb3rs import validate

def test_ip():
    assert validate("22.33.44.55") == True
    assert validate("255.0.33.33")== True
    assert validate("275.0.33.33")== False
    assert validate("215.0.33.330")== False

def test_ivalid_ip():
    assert validate("cat")== False
    assert validate("44.33.22")== False