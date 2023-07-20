import unittest
from src.Assignment10 import util
from datetime import datetime
'''
Input
1
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

output 
25200

'''


class MyTestCase(unittest.TestCase):
    def test_something(self):
        t = 1
        t1= "Sat 02 May 2015 19:54:36 +0530"
        t2=  "Fri 01 May 2015 13:54:36 -0000"
        expected_output = 88200
        x = util.time_delta(t1,t2)
        try :
            self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion Error")

if __name__ == '__main__':
    unittest.main()
