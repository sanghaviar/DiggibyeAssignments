import unittest
from src.Assignment17 import util
'''
4
a a c d
2
output = 0.833
'''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        n = 4
        mlist = ['a','a','c','d']
        k = 2
        expected_output = "0.833"
        x= util.iters(mlist,k)
        try:
            self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion Error")

if __name__ == '__main__':
    unittest.main()
