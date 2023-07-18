from util import *
n = int(input())
name, *line = input().split()
scores = list(map(float, line))
student_marks = {}
student_marks[name] = scores
query_name = input()
average(n,student_marks,query_name)



