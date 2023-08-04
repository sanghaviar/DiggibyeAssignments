import unittest
from src.Assignment13 import util
"""
Given a square matrix A with dimensions N x N. The task is to find the determinant. 
Note: Round the answer to 2 places after the decimal.
"""
class MyTestCase(unittest.TestCase):
    def test_case1(self):
        array1 = [[2, 3],
                  [4, 5]]
        expected_output = '-2.00'
        x = util.determinant_linalg(array1)
        self.assertEqual(x,expected_output)
    def test_case1(self):
        array1 = [[2, 3],
                  [4, 5]]
        expected_output = '-2.00'
        x = util.determinant_linalg(array1)
        self.assertEqual(x,expected_output)

    def test_case2(self):
        array1 = [[9, 8],
                  [3, 1]]
        expected_output = '-15.00'
        x = util.determinant_linalg(array1)
        self.assertEqual(x,expected_output)

    def test_case3(self):
        array1 = [[10, 18],
                 [30, 25]]
        expected_output = '-290.00'
        x = util.determinant_linalg(array1)
        self.assertEqual(x,expected_output)


if __name__ == '__main__':
    unittest.main()
