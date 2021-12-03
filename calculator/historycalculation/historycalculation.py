class History:
    history = []

    @staticmethod
    def clear_history():
        """ Clearing history """
        History.history.clear()

    @staticmethod
    def add_calculation_to_history(calculation):
        """ Appending calculation to history """
        History.history.append(calculation)

    @staticmethod
    def get_first_calculation_history():
        return History.history[0]

    @staticmethod
    def get_last_calculation_added():
        return History.history[-1]

    @staticmethod
    def get_calculation_count():
        return len(History.history)
