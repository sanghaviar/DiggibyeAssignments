import unittest
from src.Assignment8 import util

class MyTestCase(unittest.TestCase):
    def test_case1(self):
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

    def test_case2(self):
        '''
        Input: 08 03 2023
        output: Thursday
        '''
        y = 2023 #year
        m = 8    # Month
        d = 3   #date
        expected_output = "THURSDAY"
        x = util.calender_program(y, m, d)
        try:
           self.assertEqual(x,expected_output)
        except AssertionError:
            print("Assertion Error")
            raise
    def test_case3(self):
        '''
        Input: 05 27 2023
        output: Saturday
        '''
        y = 2023 #year
        m = 5    # Month
        d = 27   #date
        expected_output = "SATURDAY"
        x = util.calender_program(y, m, d)
        try:
           self.assertEqual(x,expected_output)
        except AssertionError:
            print("Assertion Error")
            raise

if __name__ == '__main__':
    unittest.main()
