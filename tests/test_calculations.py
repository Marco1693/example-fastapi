import sys
sys.path.append(".")

from app.calculations import add
import pytest

@pytest.mark.parametrize("num1, num2, expected",[
    (3, 2, 5), 
    (4,3,7), 
    (5,5,10)
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected
