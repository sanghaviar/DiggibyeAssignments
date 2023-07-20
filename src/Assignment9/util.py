
from collections import namedtuple

def student_marks():
    n = 2
    fields = input().split()
    total_marks = 0
    for _ in range(n):
        students = namedtuple('student', fields)
        MARKS, CLASS, NAME, ID = input().split()
        student = students(MARKS, CLASS, NAME, ID)
        total_marks += int(student.MARKS)

    print('{:.2f}'.format(total_marks / n))

