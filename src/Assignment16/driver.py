from util import *
num_of_tests = int(input())
for i in range(num_of_tests):
    n = int(input())
    # sideLengths = [int(num) for num in input().split()]
    sideLengths_str = input().split()
    side_lengths = []
    for num in sideLengths_str:
        side_lengths.append(int(num))
    pilingUp(side_lengths)
"""
n = 1
k = 6
mylist = [4 3 2 1 3 4]


2
6
4 3 2 1 3 4
3
1 3 2

num_of_test = 1
num_of_cubes = 6
side_length_cubes = [4,3,2,1,3,4]
"""