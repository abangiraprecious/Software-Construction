class Calculator_Refactored:
   
    @staticmethod
    def add(number_one, number_two ):
        return number_one + number_two 

    @staticmethod
    def subtract(number_one, number_two):
        return number_one - number_two

    @staticmethod
    def multiply(number_one, number_two):
        return number_one * number_two

    @staticmethod
    def divide(number_one, number_two):
        if number_two == 0:
            raise ValueError("Cannot divide by zero.")
        return number_one / number_two
