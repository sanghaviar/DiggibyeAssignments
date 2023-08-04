from util import *
n = int(input())
name, *line = input().split()
scores = list(map(float, line))
student_marks = {}
student_marks[name] = scores
query_name = input()

average(n, student_marks, query_name)
# """
# Input:
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# """





