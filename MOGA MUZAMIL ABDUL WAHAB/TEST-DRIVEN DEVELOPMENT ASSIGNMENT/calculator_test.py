import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def __init__(self):
        """Initializes the calculator object."""
        pass

    def test_addition(self):#Adding two numbers.
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)

    def test_subtraction(self): #Subtracting two numbers.
        calc = Calculator()
        self.assertEqual(calc.subtract(5, 3), 2)

