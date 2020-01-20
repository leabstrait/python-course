import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        # result = calc.add(10, 5)
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(10, -5), 5)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -5), -6)

    def test_subtraction(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(10, -5), 15)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -5), 4)

    def test_multiplication(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(10, -5), -50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -5), 5)

    def test_division(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(10, -5), -2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -5), 1/5)

        # self.assertRaises(ValueError, calc.divide, 5, 0)
        # self.assertRaises(ValueError, calc.divide, 5, 2)

        with self.assertRaises(ValueError):
            calc.divide(5, 0)

# Running with unittest module
# python -m unittest test_calc.py


if __name__ == '__main__':
    unittest.main()
