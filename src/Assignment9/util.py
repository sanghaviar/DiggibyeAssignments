from collections import namedtuple
def student_marks(data):
    n = len(data)
    fields = ['MARKS', 'CLASS', 'NAME', 'ID']

    total_marks = 0
    for i in range(n):
        students = namedtuple('student', fields)
        student = students(*data[i])
        total_marks += int(student.MARKS)
    result = ('{:.2f}'.format(total_marks / n))
    print(result)
    return result


# def student_marks():
#     n = 2
#     fields = input().split()
#     total_marks = 0
#     for _ in range(n):
#         students = namedtuple('student', fields)
#         MARKS, CLASS, NAME, ID = input().split()
#         student = students(MARKS, CLASS, NAME, ID)
#         total_marks += int(student.MARKS)
#
#     print('{:.2f}'.format(total_marks / n))