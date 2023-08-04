import unittest
from collections import namedtuple
from src.Assignment9 import util

'''
Using namedtuples calculate the average marks of the student spreadsheets
MARKS    CLASS        NAME       ID   
97         1         Raymond    7         
50         2         Steven     4   
'''



class MyTestCase(unittest.TestCase):

    def test_case1(self):
        data = [
            ('85', '10', 'John Doe', '101'),
            ('92', '12', 'Jane Smith', '102')
        ]
        output = '88.50'
        x = util.student_marks(data)
        try:
            self.assertEqual(x,output)
        except AssertionError:
            print("Assertion error")

    def test_case2(self):
        data = [
            ('97', '1', 'Raymond', '7'),
            ('50', '2', 'Steven', '4')
        ]
        output = '73.50'
        x = util.student_marks(data)
        try:
            self.assertEqual(x, output)
        except AssertionError:
            print("Assertion error")

    def test_case3(self):
        data = [
            ('50', '1', 'John', '4'),
            ('50', '2', 'Ram', '9')
        ]
        output = '50.00'
        x = util.student_marks(data)
        try:
            self.assertEqual(x, output)
        except AssertionError:
            print("Assertion error")

if __name__ == '__main__':
    unittest.main()
