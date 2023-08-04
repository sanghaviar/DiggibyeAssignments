import unittest
import re
from src.Assignment18 import util

"""
Given an integer N followed by N email addresses.
The task is to print a list containing only valid email addresses in lexicographical order.
"""


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        emails = ['abc@gmail.com', 'xyyz12@gmail.com', 'ab123@gmail.in']
        output = ['ab123@gmail.in', 'abc@gmail.com', 'xyyz12@gmail.com']
        x = util.email_validation(emails)
        try:
            self.assertEqual(x, output)
        except AssertionError:
            print("Assertion Error")

    def test_case2(self):
        emails = ['anu@gmail.com', 'zara12@gmail.com', 'ab123@gmail.in']
        output = ['ab123@gmail.in', 'anu@gmail.com', 'zara12@gmail.com']
        x = util.email_validation(emails)
        try:
            self.assertEqual(x, output)
        except AssertionError:
            print("Assertion Error")

    def test_case3(self):
        emails = ['abc@gmail.in', 'xy12@gmail.com', 'ab123@gmail.in','john@gmail.com']
        output = ['ab123@gmail.in', 'abc@gmail.in', 'john@gmail.com','xy12@gmail.com']
        x = util.email_validation(emails)
        try:
            self.assertEqual(x, output)
        except AssertionError:
            print("Assertion Error")




if __name__ == '__main__':
    unittest.main()
