import unittest
from src.Assignment14 import util

class MyTestCase(unittest.TestCase):
    def test_something(self):
        array1 = [1,2,3,4,5,6,7,8]
        a = [1,2,3,4,5,6]
        b = [7,8,9,10]
        expected_output = 4
        x = util.no_idea(array1,a,b)
        try:
            self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion Error")
            raise

if __name__ == '__main__':
    unittest.main()
