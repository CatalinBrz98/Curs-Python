import unittest
from unittest import TestCase
from calculator import Calculator
from math import isclose


def is_almost_equal(a, b):
    return isclose(a, b, rel_tol=1e-9, abs_tol=0.0)


class TestCalculator(TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_adunare_simpla(self):
        self.assertTrue(is_almost_equal(self.calculator.adunare(29, 5), 34))

    def test_adunare_complexa(self):
        self.assertTrue(is_almost_equal(self.calculator.adunare(-13, 4), -9))

    def test_scadere_simpla(self):
        self.assertTrue(is_almost_equal(self.calculator.scadere(15, 9), 6))

    def test_scadere_complexa(self):
        self.assertTrue(is_almost_equal(self.calculator.scadere(-20, -100), 80))

    def test_inmultire_simpla(self):
        self.assertTrue(is_almost_equal(self.calculator.inmultire(5, 7), 35))

    def test_inmultire_complexa(self):
        self.assertTrue(is_almost_equal(self.calculator.inmultire(-4.5, 3.7), -16.65))

    def test_impartire_simpla(self):
        self.assertTrue(is_almost_equal(self.calculator.impartire(20, 4), 5))

    def test_impartire_cu_virgula(self):
        self.assertTrue(is_almost_equal(self.calculator.impartire(-100, 125), -0.8))

    def test_impartire_la_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.impartire(10, 0)

    def tearDown(self):
        del self.calculator


if __name__ == '__main__':
    unittest.main()
