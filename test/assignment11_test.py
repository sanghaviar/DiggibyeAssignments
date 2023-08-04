import unittest
import numpy
from src.Assignment11 import util

"""
write a code to find floor,ceil,rint
"""
def numbers(elem):
    # rounds down to the nearest
    floor1 = numpy.floor(elem)
    # rounds up to the nearest
    ceil1 = numpy.ceil(elem)
    # rounds to the nearest integer
    rint1 = numpy.rint(elem)



class MyTestCase(unittest.TestCase):
    def test_case1(self):
        global elem
        # elem= list(map(float, input("Enter all elements: ").strip().split()))
        elem = [1.0,1.2,1.3,1.5]
        expected_output = numbers(elem)
        x = util.elements(elem)
        self.assertEqual(x,expected_output)

    def test_case2(self):
        global elem
        elem = [1.9,4.2,9.3,9.5,9.0]
        expected_output = numbers(elem)
        x = util.elements(elem)
        self.assertEqual(x,expected_output)

    def test_case3(self):
        global elem
        elem = [6.9,9.2,8.9,10.5,12.8]
        expected_output = numbers(elem)
        x = util.elements(elem)
        self.assertEqual(x,expected_output)


if __name__ == '__main__':
    unittest.main()
