class Calculator_Refactored:
    """The calculator refactored class contains methods for basic arithmetic operations."""
    @staticmethod
    def add(num1, num2 ):
        return num1 + num2 

    @staticmethod
    def subtract(num1, num2):
        return num1 - num2

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
