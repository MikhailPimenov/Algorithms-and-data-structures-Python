import unittest
from .horse import horse as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        v1 = 'e2'
        v2 = 'e4'
        result = algorithm(v1, v2)
        print(v1, "->")
        print(*result)
        print("->", v2)

        v1 = 'a1'
        v2 = 'h8'
        result = algorithm(v1, v2)
        print(v1, "->")
        print(*result)
        print("->", v2)

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
