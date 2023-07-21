import unittest
from src.Assignment16 import util

'''
n = 1
k = 6
mylist = [4 3 2 1 3 4]


2
6
4 3 2 1 3 4
3
1 3 2

# num_of_test = 1
# num_of_cubes = 6
# side_length_cubes = [4,3,2,1,3,4]
'''

def test_pilingUp(side_length):
    current_cube_length = float('inf')
    left_runner = 0
    right_runner = len(side_length) - 1

    while left_runner <= right_runner:
        left_value = side_length[left_runner]
        right_value = side_length[right_runner]

        if left_value > current_cube_length and right_value > current_cube_length:
            # print("No")
            return
        else:
            if left_value >= right_value and left_value <= current_cube_length:
                current_cube_length = left_value
                left_runner +=1
            elif right_value > left_value and right_value <= current_cube_length:
                current_cube_length = right_value
                right_runner -=1
            else:
                # print("No")
                return
    # print("Yes")
    return

class MyTestCase(unittest.TestCase):
    def test_something(self):

        global side_lengths
        num_of_tests = int(input())
        for i in range(num_of_tests):
            n = int(input())
            sideLengths_str = input().split()
            side_lengths = []
            for num in sideLengths_str:
                side_lengths.append(int(num))

        x = util.pilingUp(side_lengths)
        expected_output = test_pilingUp(side_lengths)

        try:
            self.assertEqual(x,expected_output)
        except AssertionError:
            print("Assertion Error")

if __name__ == '__main__':
    unittest.main()
