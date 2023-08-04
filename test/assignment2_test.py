import unittest
from src.Assignment2 import util
'''
The first line contains the integer , the number of students' records. 
The next  lines contain the names and marks obtained by a student, each value separated by a space. 
The final line contains query_name, the name of a student to query.
'''
class MyTestCase(unittest.TestCase):

    def test_case1(self):
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
    def test_case2(self):
        n = 3
        marks = {"abc": [10, 20, 30], "bcd": [20, 20, 20],"xyz": [40, 40, 40] }
        qname = "xyz"
        expected_output = 40.0
        z = util.average(n,marks,qname)
        try:
            self.assertEqual(z,expected_output)
        except AssertionError:
            print("Assertion Error")
            raise
    def test_case3(self):
        n = 2
        marks = {"anu": [10, 20, 30], "john": [90, 60, 90]}
        qname = "john"
        expected_output = 80.0
        z = util.average(n,marks,qname)
        try:
            self.assertEqual(z,expected_output)
        except AssertionError:
            print("Assertion Error")
            raise
if __name__ == '__main__':
    unittest.main()
