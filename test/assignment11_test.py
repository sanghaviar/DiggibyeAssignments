import unittest
import numpy
from src.Assignment11 import util


def test_case(elem):
    # rounds down to the nearest
    floor1 = numpy.floor(elem)
    # rounds up to the nearest
    ceil1 = numpy.ceil(elem)
    # rounds to the nearest integer
    rint1 = numpy.rint(elem)



class MyTestCase(unittest.TestCase):
    def test_something(self):
        global elem
        elem= list(map(float, input("Enter all elements: ").strip().split()))
        expected_output = test_case(elem)
        x = util.elements(elem)
        self.assertEqual(x,expected_output)


if __name__ == '__main__':
    unittest.main()
