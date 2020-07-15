# In terminal
# python -m unittest
# python -m unittest -v
# pip install -U pytest
# pytest
# pytest -v

from simple_calc import SimpleCalc
import unittest


class Calctests(unittest.TestCase):
    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(12, 5), 17)
        self.assertEqual(self.calc.add(-3, 7), 4)
        self.assertEqual(self.calc.add(67, 8), 75)
        self.assertIsNotNone(self.calc.add(0, 0))

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 1), 2)
        self.assertEqual(self.calc.subtract(65, 9), 56)
        self.assertEqual(self.calc.subtract(2, 17), -15)
        self.assertEqual(self.calc.subtract(-9, -41), 32)
        self.assertIsNotNone(self.calc.subtract(0, 0))

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 6), 30)
        self.assertEqual(self.calc.multiply(34, 2), 68)
        self.assertEqual(self.calc.multiply(-65, 3), -195)
        self.assertEqual(self.calc.multiply(-14, -8), 112)
        self.assertIsNotNone(self.calc.multiply(0, 0))

    def test_divide(self):
        self.assertEqual(self.calc.divide(16, 8), 2)
        self.assertEqual(self.calc.divide(100, 10), 10)
        self.assertEqual(self.calc.divide(-81, -9), 9)
        self.assertEqual(self.calc.divide(-24, 6), -4)
        self.assertIsNotNone(self.calc.divide(0, 1))
