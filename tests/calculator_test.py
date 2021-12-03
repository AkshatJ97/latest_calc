
from calculator.main import Calculator


def test_calculator_result():
    calc = Calculator()
    assert calc.get_result() == 0

def test_calculator_add():
    calc = Calculator()
    calc.addition(10, 10)
    assert calc.get_result() == 20

def test_calculator_subtract():
    calc = Calculator()
    calc.subtraction(10, 10)
    assert calc.get_result() == 0

def test_calculator_multiply():
    calc = Calculator()
    calc.multiplication(10, 10)
    assert calc.get_result() == 100

def test_calculator_divide():
    calc = Calculator()
    calc.division(10, 0)
    assert calc.get_result() == 0
