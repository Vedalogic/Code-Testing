import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(5, 5), 10)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 3), 7)

    def test_divide(self):
        self.assertEqual(calc.divide(10,2), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 10), 100)


if __name__ == "__main__":
    unittest.main()
