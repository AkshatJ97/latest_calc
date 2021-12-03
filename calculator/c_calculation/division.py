from calculator.calculator_calculations.calculation import Calculation

class Division(Calculation):
    """it performs division of values coming from the parent class i.e calculation
     and returns the result to the parent class """

    def getresult(self):
        division_of_values = 1.0
        for value in self.values:
            division_of_values = value / division_of_values
        return division_of_values
