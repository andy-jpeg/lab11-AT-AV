# https://github.com/andy-jpeg/lab11-AT-AV
# Partner 1: Andy Tran
# Partner 2: Augusto Valero

from calculator import *
import unittest

class CalculatorProgramTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 6), 9)
        self.assertEqual(add(-4, -7), -11)
        self.assertEqual(add(-2, 5), 3)
        self.assertEqual(add(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(5, 10), 50)
        self.assertEqual(mul(10, 2.5), 25)
        self.assertEqual(mul(5, 1000), 5000)

    def test_divide(self):
        self.assertEqual(div(4, 12), 3)
        self.assertEqual(div(5, 5), 1)
        self.assertAlmostEqual(div(4, 30), 7.5)
        self.assertEqual(div(10, 500), 50)

    def test_subtract(self):
        self.assertEqual(subtract(9, 3), 6)
        self.assertEqual(subtract(5, -3), 8)
        self.assertEqual(subtract(4, -6), 10)
        self.assertEqual(subtract(-1, -1), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self):
        self.assertEqual(logarithm(100, 10), 2)
        self.assertEqual(logarithm(8, 2), 3)
        self.assertEqual(logarithm(256, 4), 4)
        self.assertEqual(logarithm(25, 5), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ZeroDivisionError):
            logarithm(10, 1)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(10, 0)

    def test_sqrt(self):
        self.assertEqual(square_root(256), 16)
        self.assertAlmostEqual(square_root(24), 4.89897949)
        self.assertAlmostEqual(square_root(5), 2.23606797749979)
        self.assertAlmostEqual(square_root(729), 27)

    def test_hypotenuse(self):
        self.assertEqual(math.hypot(3, 4), 5)
        self.assertEqual(math.hypot(6, 8), 10)
        self.assertEqual(math.hypot(20, 21), 29)
        self.assertEqual(math.hypot(8, 15), 17)

if __name__ == '__main__':
    unittest.main()