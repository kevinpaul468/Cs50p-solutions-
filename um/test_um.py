from um import count

def test_um():
    assert count("um")==1
    assert count("um?")==1
    assert count("um,")==1

def test_Um():
    assert count("Um")==1
    assert count("uM")==1
    assert count("UM...")==1

def test_not_um():
    assert count("plum")==0
    assert count("tumor")==0