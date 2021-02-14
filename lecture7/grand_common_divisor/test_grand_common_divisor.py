import unittest
from .grand_common_divisor2 import grand_common_divisor


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(grand_common_divisor(25, 5), 5)
        self.assertEqual(grand_common_divisor(5, 25), 5)
        self.assertEqual(grand_common_divisor(6,8),2)
        self.assertEqual(grand_common_divisor(8,6),2)
        self.assertEqual(grand_common_divisor(25, 35), 5)
        self.assertEqual(grand_common_divisor(35, 25), 5)
        self.assertEqual(grand_common_divisor(35, 35), 35)
        self.assertEqual(grand_common_divisor(18, 12), 6)
        self.assertEqual(grand_common_divisor(12, 18), 6)
        self.assertRaises(ArithmeticError, grand_common_divisor, -10, 5)
        self.assertRaises(ArithmeticError, grand_common_divisor, 10, -5)
        self.assertRaises(ArithmeticError, grand_common_divisor, -10, -5)
        self.assertRaises(ArithmeticError, grand_common_divisor, -10, 0)
        self.assertRaises(ArithmeticError, grand_common_divisor, 0, 5)
        self.assertRaises(ArithmeticError, grand_common_divisor, 0, 0)
        self.assertRaises(TypeError, grand_common_divisor, 0.9, 1)
        self.assertRaises(TypeError, grand_common_divisor, 9, 0.1)
        self.assertRaises(TypeError, grand_common_divisor, 0.9, 0.1)
        self.assertRaises(TypeError, grand_common_divisor, 9, "asd")
        self.assertRaises(TypeError, grand_common_divisor, "asd", 5)
        self.assertRaises(TypeError, grand_common_divisor, "asd", 'a')
        self.assertRaises(TypeError, grand_common_divisor, 'a', 'a')


if __name__ == '__main__':
    unittest.main()
