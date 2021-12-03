
from calculator.calculator_calculations.calculation import Calculation

class Addition(Calculation):
    '''inheritance concept of oops is used here.
    calculation is the parent class and addition is the child class'''
    def getresult(self):
        """ Using self to reference the data contained in the object instance """
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = sum_of_values + value
        return sum_of_values
