import unittest
from src.Assignment12 import util
import numpy
class MyTestCase(unittest.TestCase):
    def test_something(self):
        array1 = numpy.array([[2, 5],
                                [3, 7],
                                [1, 3],
                                [4, 0]])
        expected_output = 3
        x = util.min_max(array1)
        self.assertEqual(x,expected_output)


if __name__ == '__main__':
    unittest.main()
