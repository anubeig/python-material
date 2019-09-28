def sum(a, b):
    return a+b


def test_sum01():
    assert sum(10, 5) == 15

@pytest.mark.sanity
def test_sum02():
    assert sum(10, 5) == 15
