""" Import Calculation Parent Class Constructor """

from calc_methods.calculation import Calculation


class Addition(Calculation):
    """ it performs addition coming from the super class or parent class and returns
     the result """

    def getresult(self):
        return self.value_a + self.value_b
