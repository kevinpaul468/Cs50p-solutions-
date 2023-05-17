from fuel import convert,gauge
import pytest
def test_convert():
    assert convert('7/10')==70
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ZeroDivisionError):
        convert("9/0")
def test_gauge():
    assert gauge(1)=="E"
    assert gauge(99)=="F"
    assert gauge(56)=="56%"
