from calculator.calculator_calculations.calculation import Calculation

class Multiplication(Calculation):
    """ it performs multiplication of values coming from the parent class i.e calculation
     and returns the result to the parent class"""
    def getresult(self):
        """ Using self to reference the data contained in the object instance """
        multiplication_of_values = 1.0
        for value in self.values:
            multiplication_of_values = multiplication_of_values * value
        return multiplication_of_values
