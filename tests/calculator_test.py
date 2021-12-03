import pprint
import pytest
from calculator.main import Calculator

@pytest.fixture
def clear_history():
    Calculator.clear_history()


def test_calculator_add(clear_history):
    """ To check if calculator addition result is correct """
    assert Calculator.add_nums(10, 10) == 20
    assert Calculator.add_nums(20, 20) == 40
    assert Calculator.add_nums(30, 30) == 60
    assert Calculator.add_nums(40, 40) == 40
    assert Calculator.get_calculation_count() == 4
    assert Calculator.get_first_calculation_history() == 20
    pprint.pprint(Calculator.history)


def test_calculator_subtract(clear_history):
    """ To check if calculator subtraction result is correct """
    assert Calculator.subtract_nums(10, 20) == -10
    assert Calculator.get_calculation_count() == 1
    pprint.pprint(Calculator.history)


def test_calculator_multiply(clear_history):
    """ To check if calculator multiplication result is correct """
    assert Calculator.multiply_nums(10, 10) == 100
    assert Calculator.get_calculation_count() == 1
    pprint.pprint(Calculator.history)


def test_calculator_divide(clear_history):
    """ To check if calculator division result is correct """
    assert Calculator.divide_nums(20, 20) == 1
    assert Calculator.get_calculation_count() == 1
    pprint.pprint(Calculator.history)
