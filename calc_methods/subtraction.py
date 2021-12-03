
from calc_methods.calculation import Calculation



class Subtraction(Calculation):
    """  it Performs subtraction between two values coming from super class or parent class
    and returns the results """

    def getresult(self):
        return self.value_a - self.value_b
