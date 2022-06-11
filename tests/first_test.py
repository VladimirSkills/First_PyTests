import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    # Позитивный Тест *:
    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    # Негативный Тест *:
    def test_multiply_calculate_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    # Позитивный Тест /:
    def test_multiply_calculate_division(self):
        assert self.calc.division(self, 10, 2) == 5

    # Позитивный Тест -:
    def test_multiply_calculate_subtraction(self):
        assert self.calc.subtraction(self, 8, 1) == 7

    # Позитивный Тест +:
    def test_multiply_calculate_adding(self):
        assert self.calc.adding(self, 2, 1) == 3


# Другой вариант теста
# Тестируемая функция:
def multiply(x, y):
    return x * y

# Позитивный Тест:
def test_multiply_correctly():
    assert multiply(2, 2) == 4

