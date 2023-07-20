import unittest
from collections import namedtuple
from src.Assignment9 import util

'''
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4   
'''
def marks():
    n = 2
    fields = input("INPUT for test case: ")

    total_marks = 0
    for _ in range(n):
        students = namedtuple('student', fields)
        MARKS, CLASS, NAME, ID = input().split()
        student = students(MARKS, CLASS, NAME, ID)
        total_marks += int(student.MARKS)
    res = ('{:.2f}'.format(total_marks / n))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected_result = marks()
        x = util.student_marks()
        self.assertEqual(x,expected_result)


if __name__ == '__main__':
    unittest.main()
