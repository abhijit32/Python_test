from unittest import TestCase
import test


class TestFunctions(TestCase):
    def test_divide_result(self):
        num1 = 15
        num2 = 3
        result = 5.0
        self.assertAlmostEqual(test.divide(num1,num2), result)

    def test_divide_byZero(self):
        with self.assertRaises(ValueError):
            test.divide(4,0)