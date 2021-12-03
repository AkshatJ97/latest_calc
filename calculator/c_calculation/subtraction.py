from calculator.calculator_calculations.calculation import Calculation

class Subtraction(Calculation):
    """ it performs subtraction of values coming from the parent class i.e calculation
     and returns the result to the parent class"""

    def getresult(self):
        subtraction_of_values = 0.0
        for value in self.values:
            subtraction_of_values = subtraction_of_values - value
        return subtraction_of_values
