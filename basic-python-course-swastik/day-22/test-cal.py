import cal
import unittest

class TestCal(unittest.TestCase):

    def test_add(self):
        self.assertEqual(cal.add(10,5), 15)
        self.assertEqual(cal.add(10, -5), 5)
        self.assertEqual(cal.add(-1, 1), 0)
        self.assertEqual(cal.add(-1, -5), -6)

    def test_subtraction(self):
        self.assertEqual(cal.subtract(10, 5), 5)
        self.assertEqual(cal.subtract(10, -5), 15)
        self.assertEqual(cal.subtract(-1, 1), -2)
        self.assertEqual(cal.subtract(-1, -5), 4)

    def test_multiplication(self):
        self.assertEqual(cal.multiply(10, 5), 50)
        self.assertEqual(cal.multiply(10, -5), -50)
        self.assertEqual(cal.multiply(-1, 1), -1)
        self.assertEqual(cal.multiply(-1, -5), 5)

    def test_division(self):
        self.assertEqual(cal.divide(10, 5), 2)
        self.assertEqual(cal.divide(10, -5), -2)
        self.assertEqual(cal.divide(-1, 1), -1)
        self.assertEqual(cal.divide(-1, -5), 1/5)

        # self.assertRaises(ZeroDivisionError, cal.divide, 4, 0)
        # self.assertRaises(ZeroDivisionError, cal.divide, 4, 2)

        with self.assertRaises(ZeroDivisionError):
            cal.divide(5,0)

unittest.main()