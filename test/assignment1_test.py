import unittest
from src.Assignment1 import util

class MyTestCase(unittest.TestCase):
    def test_something(self):
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




if __name__ == '__main__':
    unittest.main()
