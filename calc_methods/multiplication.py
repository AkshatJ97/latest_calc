from calc_methods.calculation import Calculation

class Multiplication(Calculation):
    """it performs multiply between two values coming from super class or
     Parent Class and returns the results """

    def getresult(self):
        return self.value_a * self.value_b
