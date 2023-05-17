from working import convert
import pytest
def test_format1():
    assert convert("9 AM to 5 PM") =="09:00 to 17:00"
    assert convert("8 AM to 6 PM") =="08:00 to 18:00"

def test_format2():
    assert convert("8:00 AM to 6:00 PM") =="08:00 to 18:00"
    assert convert("5:00 AM to 6:00 PM") =="05:00 to 18:00"

def test_valerr():
    with pytest.raises(ValueError):
        convert("12:60 AM to 6:00 PM")
    with pytest.raises(ValueError):
        convert("12:30 AM - 6:00 PM")