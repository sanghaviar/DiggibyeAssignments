import unittest
from src.Assignment17 import util
'''
Given a list of N lowercase English letters. 
For a given integer K, you can select any K indices with a uniform probability from the list.
Find the probability that at least one of the K indices selected will contain the letter: 'a'.

'''
class MyTestCase(unittest.TestCase):
    def test_case1(self):
        n = 4
        mlist = ['a','a','c','d']
        k = 2
        expected_output = "0.833"
        x= util.iters(mlist,k)
        try:
            self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion Error")

    def test_case2(self):
        n = 5
        mlist = ['a', 'c', 'a', 'd','f']
        k = 2
        expected_output = "0.700"
        x = util.iters(mlist, k)
        try:
            self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion Error")

    def test_case3(self):
        n = 6
        mlist = ['a', 'b', 'c', 'd','e', 'a']
        k = 3
        expected_output = "0.800"
        x = util.iters(mlist, k)
        try:
            self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion Error")

if __name__ == '__main__':
    unittest.main()
