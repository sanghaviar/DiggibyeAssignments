import unittest
from src.Assignment13 import util

class MyTestCase(unittest.TestCase):
    def test_something(self):
        array1 = [[2, 3],
                  [4, 5]]
        expected_output = '-2.00'
        x = util.determinant_linalg(array1)
        self.assertEqual(x,expected_output)


if __name__ == '__main__':
    unittest.main()
