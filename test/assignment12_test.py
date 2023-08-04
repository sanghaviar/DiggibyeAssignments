import unittest
from src.Assignment12 import util
import numpy

"""
Given a 2-D array with dimensions N x M The task is to perform the min function over 
axis and then find the max of that.
"""
class MyTestCase(unittest.TestCase):
    def test_case1(self):
        array1 = numpy.array([[2, 5],
                                [3, 7],
                                [1, 3],
                                [4, 0]])
        expected_output = 3
        x = util.min_max(array1)
        self.assertEqual(x,expected_output)
    def test_case2(self):
        array1 = numpy.array([[9, 0],
                                [6, 7],
                                [10, 13],
                                [14, 8]])
        expected_output = 10
        x = util.min_max(array1)
        self.assertEqual(x,expected_output)

    def test_case3(self):
        array1 = numpy.array([[12, 15],
                                [13, 70],
                                [1, 78],
                                [92, 90]])
        expected_output = 90
        x = util.min_max(array1)
        self.assertEqual(x,expected_output)

if __name__ == '__main__':
    unittest.main()
