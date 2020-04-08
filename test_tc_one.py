import helloworld_ts

def test_double():
    result = helloworld_ts.double(5)
    assert result == 10


def test_double2():
    result = helloworld_ts.double(3)
    assert result == 6


def test_double3():
    result = helloworld_ts.double(2)
    assert result == 4

