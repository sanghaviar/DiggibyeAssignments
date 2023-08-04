import numpy as np
def average(n,student_marks,query_name):
    for _ in range(n):
        ls = student_marks[query_name]
        avg = np.average(ls)
        print(avg)
        return avg




