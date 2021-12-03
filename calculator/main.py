class Calculator:
    def __init__(self):
        pass

    result=0

    def addition(self,value_a,value_b):
        self.result=value_a+value_b
        return self.result

    def subtraction(self,value_a,value_b):
        self.result=value_a-value_b
        return self.result

    def multiplication(self,value_a,value_b):
        self.result=value_a * value_b
        return self.result

    def division(self,value_a,value_b):
        try:
            self.result=value_a / value_b
            return self.result
        except ZeroDivisionError:
            return 0