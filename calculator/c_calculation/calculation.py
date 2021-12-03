class Calculation:

    def __init__(self, values: tuple):
        """converts the values to float"""
        self.values = Calculation.convert_args_to_list_float(values)

    # Class Method
    @staticmethod
    def convert_args_to_list_float(values):
        """ Returns the float values in a list """
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return list_values_float
