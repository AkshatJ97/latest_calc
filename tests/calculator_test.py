import pprint
import pytest
from calculator.main import Calculator
from calculator.history_calculations.history_calculations import History



'''pytest fixtures are functions attached to
the tests which run before the test function is executed@pytest.fixture'''
def clear_history():
    """ Clears history """
    History.clear_history()


def test_calculator_add(clear_history):
    assert Calculator.add_nums(10.0, 20.0, 40.0) == 70.0
    assert Calculator.add_nums(10.0, 50.0) == 60.0
    assert History.get_calculation_count() == 2
    assert History.get_first_calculation_history() == 70.0
    assert History.get_last_calculation_added() == 60.0
    pprint.pprint(History.history)


def test_calculator_subtract(clear_history):
    """ To check if calculator subtraction result is correct """
    assert Calculator.subtract_nums(10.0, 20.0) == -30.0


def test_calculator_multiply(clear_history):
    """ To check if calculator multiplication result is correct """
    assert Calculator.multiply_nums(10.0, 10.0) == 100.0


def test_calculator_divide(clear_history):
    """ To check if calculator division result is correct """
    assert Calculator.divide_nums(20.0, 10.0) == 2.0
