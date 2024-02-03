import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_unsucces(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_divizion(self):
        with pytest.raises(ZeroDivisionError):
             self.calc.division(self, 1, 0)

    def test_division(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_subtraction(self):
        assert self.calc.subtraction(self, 4, 2) == 2


    def teardown(self):
        print('Выполнение метода Teardown')

