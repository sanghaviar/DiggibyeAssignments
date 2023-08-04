import unittest
from src.Assignment14 import util
"""
There is an array of integers. 
There are also disjoint sets, A and B , each containing m integers. 
You like all the integers in set A and dislike all the integers in set B.
Initial Happiness is 0.For each integer i in the array, if i belong to A, ass 1 to your hapiness. 
If i belong to B, you add -1 to your happiness Otherwise your happiness does not change.
"""
class MyTestCase(unittest.TestCase):
    def test_case1(self):
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

    def test_case2(self):
        array1 = [12,18,23,90,34,78,100]
        a = [29,78,12,90,100,34,79,60]
        b = [67,68,18]
        expected_output = 4
        x = util.no_idea(array1,a,b)
        try:
            self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion Error")
            raise

    def test_case3(self):
        array1 = [12,19,90,78]
        a = [87,78,90,67,56]
        b = [13,17,22,25]
        expected_output = 2
        x = util.no_idea(array1,a,b)
        try:
            self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion Error")
            raise

if __name__ == '__main__':
    unittest.main()
