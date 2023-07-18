import unittest
from src.Assignment2 import util
'''
The first line contains the integer , the number of students' records. 
The next  lines contain the names and marks obtained by a student, each value separated by a space. 
The final line contains query_name, the name of a student to query.
'''
class MyTestCase(unittest.TestCase):

    def test_something(self):
        n = 2
        marks = {"abc": [10, 20, 30], "bcd": [20, 20, 20]}
        qname = "bcd"
        expected_output = 20.0
        z = util.average(n,marks,qname)
        try:
            self.assertEqual(z,expected_output)  # add assertion here
        except AssertionError:
            print("Assertion Error")
            raise

if __name__ == '__main__':
    unittest.main()
