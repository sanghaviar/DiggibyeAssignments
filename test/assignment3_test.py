import unittest
from src.Assignment3 import util
'''
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given  scores.
 Store them in a list and find the score of the runner-up.
'''
class MyTestCase(unittest.TestCase):
    def test_case1(self):
        score = [1,5,88,20,7]
        y = util.runner_up(score)
        expected_output = 20
        try:
            self.assertEqual(y,expected_output)
        except AssertionError:
            print(" Assertion Error")
            raise

    def test_case2(self):
        score = [5, 6, 88, 10, 7]
        y = util.runner_up(score)
        expected_output = 10
        try:
            self.assertEqual(y, expected_output)
        except AssertionError:
            print(" Assertion Error")
            raise

    def test_case3(self):
        score = [100, 60, 88, 70, 97]
        y = util.runner_up(score)
        expected_output = 97
        try:
            self.assertEqual(y, expected_output)
        except AssertionError:
            print(" Assertion Error")
            raise



if __name__ == '__main__':
    unittest.main()
