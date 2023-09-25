from main import calculate

import pytest

@pytest.fixture
def data():
    return [15, 23, 43, 11, 5, 30, 8, 19, 7, 50, 28, 37, 14, 21, 9, 63, 31, 2, 45, 12]

def test(data):
    mean, median, std_dev = calculate(data)

    assert mean == 23.65
    assert median == 20.0
    assert std_dev == 16.875004873293644
