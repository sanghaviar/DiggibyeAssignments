import unittest
from src.Assignment16 import util

'''
There is a Horizontal row of n cubes. 
The length of each cube is given. We need create a new vertical pile of cubes.
The New pile should follow the specified directions.
when stacking cube should pick only either leftmost or rightmost cube each time. 
Print "YES" if it is possible to stack the cubes.Otherwise print "NO"

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
    def test_case1(self):
        side = [1,2,3,4]
        x = util.pilingUp(side)
        output = test_pilingUp(side)
        try:
            self.assertEqual(x,output)
        except AssertionError:
            print("Assertion Error")
    def test_case2(self):
        side = [5,2,3,4,1]
        x = util.pilingUp(side)
        output = test_pilingUp(side)
        try:
            self.assertEqual(x, output)
        except AssertionError:
            print("Assertion Error")
    def test_case3(self):
        side = [5,4,3,2,1,3,4,5]
        x = util.pilingUp(side)
        output = test_pilingUp(side)
        try:
            self.assertEqual(x, output)
        except AssertionError:
            print("Assertion Error")

if __name__ == '__main__':
    unittest.main()
