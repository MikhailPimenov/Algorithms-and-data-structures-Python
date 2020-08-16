import unittest
from .generate_numbers import generate_numbers as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        algorithm(2, 3)
        self.assertRaises(TypeError, algorithm, 8, 'a')
        self.assertRaises(TypeError, algorithm, "asd", 9)
        self.assertRaises(TypeError, algorithm, 'a', "asd")
        self.assertRaises(ArithmeticError, algorithm, -3, 4)
        self.assertRaises(ArithmeticError, algorithm, 19, 5)



if __name__ == '__main__':
    unittest.main()
