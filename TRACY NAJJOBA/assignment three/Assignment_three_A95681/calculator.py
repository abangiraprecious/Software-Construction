class Calculator:
    """The calculator class contains methods for basic arithmetic operations."""
    def add(self, num1 , num2 ):
        return num1  + num2 

    def subtract(self, num1 , num2 ):
        return num1  - num2 

    def multiply(self, num1 , num2 ):
        return num1  * num2 

    def divide(self, num1 , num2 ):
        if num2  == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2 
