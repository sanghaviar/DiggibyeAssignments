import unittest
from src.Assignment8 import util

class MyTestCase(unittest.TestCase):
    def test_something(self):
        '''
        Input: 05 28 2023
        output: Sunday
        '''
        y = 2023 #year
        m = 5    # Month
        d = 28   #date
        expected_output = "SUNDAY"
        x = util.calender_program(y, m, d)
        try:
           self.assertEqual(x,expected_output)
        except AssertionError:
            print("Assertion Error")
            raise


if __name__ == '__main__':
    unittest.main()
