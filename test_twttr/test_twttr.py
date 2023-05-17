from twttr import shorten
import pytest
def test_shorten():
    assert shorten("kevin paul")=="kvn pl"
    assert shorten("kevinpaul468")=="kvnpl468"
    assert shorten("kevin,paul")=="kvn,pl"
    assert shorten("EVEN")=="VN"

