class Calculator:
    def add(self, number_one , number_two ):
        return number_one  + number_two 

    def subtract(self, number_one , number_two ):
        return number_one  - number_two 

    def multiply(self, number_one , number_two ):
        return number_one  * number_two 

    def divide(self, number_one , number_two ):
        if number_two  == 0:
            raise ValueError("Cannot divide by zero.")
        return number_one / number_two 
