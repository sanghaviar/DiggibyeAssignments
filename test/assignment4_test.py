import unittest
from src.Assignment4 import util

class MyTestCase(unittest.TestCase):
    def test_something(self):
        '''
        Read a given string, change the character at a given index and then print the modified string.
        Test_case 1:
        Input: "abcd"
        Replacing: z
        Position: 2
        Expected output: "abzd"
        '''
        st1 = "abcd"
        rep = "z"
        pos = 2
        x = util.mutation(st1,rep,pos)
        expected_output = "abzd"
        try:
            self.assertEqual(x,expected_output)  # add assertion here
        except AssertionError:
            print("Assertion Error")
            raise






if __name__ == '__main__':
    unittest.main()
