import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_positive(self):
        assert self.calc.multiply(self, 2, 2) == 4
    
    def test_division_calculate_positive(self):
        assert self.calc.division(self, 9, 3) == 3

    def test_subtraction_calculate_positive(self):
        assert self.calc.subtraction(self, 10, 3) == 7

    def test_subtraction_calculate_positive_2(self):
        assert self.calc.subtraction(self, -10, -3) == -7

    def test_subtraction_calculate_positive_3(self):
        assert self.calc.subtraction(self, -10, 3) == -13

    def test_adding_calculate_positive(self):
        assert self.calc.adding(self, 3, 3) == 6

    def test_adding_calculate_positive_2(self):
        assert self.calc.adding(self, -3, 3) == 0

    def test_adding_calculate_positive_3(self):
        assert self.calc.adding(self, -3, -3) == -6
    
