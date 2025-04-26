import pytest
from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(3, 5) == 8
    assert calc.add(-1, 1) == 0
    assert calc.add(-1, -1) == -2

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(1, 5) == -4
    assert calc.subtract(-5, -3) == -2
