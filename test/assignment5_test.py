import unittest
from src.Assignment5 import util
'''
There are three substrings of length  to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, 
The second substring has all distinct characters, 
The third substring has  different characters,
 Note that a subsequence maintains the original order of characters encountered.
 The order of characters in each subsequence shown is important.
 s = "AAABCADDE"
 k = 3
 u1 = "A"
 u2 = "BCA"
 u3 = "DE"
'''

def merge_string(string,k):
    temp = []
    len_temp = 0
    for item in string:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == k:
            result = ''.join(temp)
            temp = []
            len_temp = 0


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        string = "AAABCADDE"
        k = 3
        expected_output = merge_string(string,k)
        x = util.merge_the_tools(string,k)
        try:
           self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion error")
            raise
    def test_case2(self):
        string = "AJYUINKOUY"
        k = 3
        expected_output = merge_string(string,k)
        x = util.merge_the_tools(string,k)
        try:
           self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion error")
            raise

    def test_case3(self):
        string = "AAOHJLTYU"
        k = 4
        expected_output = merge_string(string, k)
        x = util.merge_the_tools(string, k)
        try:
            self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion error")
            raise


if __name__ == '__main__':
    unittest.main()
