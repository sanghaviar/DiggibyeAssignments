import unittest
from src.Assignment1 import util

class MyTestCase(unittest.TestCase):
    def test1(self):
        '''
        append 5
        append 6
        insert 0 2
        print
        '''
        N = 4
        output = [2,5,6]
        x = util.list_operations(N)
        try:
            self.assertEqual(x, output)  # add assertion here
        except AssertionError:
            print("Assertion Error")
            raise
    def test2(self):
        '''
            append 2
            append 2
            pop
            insert 1 10
            print
        '''
        N = 5
        output = [2,10]
        x = util.list_operations(N)
        try:
            self.assertEqual(x, output)  # add assertion here
        except AssertionError:
            print("Assertion Error")
            raise
    def test3(self):
        """
            append 1
            insert 1 10
            append 5
            sort
            reverse
            print
        """
        N = 6
        output = [10,5,1]
        x = util.list_operations(N)
        try:
            self.assertEqual(x, output)  # add assertion here
        except AssertionError:
            print("Assertion Error")
            raise


if __name__ == '__main__':
    unittest.main()
