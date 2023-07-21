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