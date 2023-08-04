import unittest
from src.Assignment7 import util
def allignment(thickness,c):

    for i in range(thickness):
        output = ((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
    for i in range(thickness + 1):
        output = ((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    for i in range((thickness + 1) // 2):
        output = ((c * thickness * 5).center(thickness * 6))

    for i in range(thickness + 1):
        output = ((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))


    for i in range(thickness):
        output = (((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
            thickness * 6))

class MyTestCase(unittest.TestCase):
    def test_case1(self):
        c = 'H'
        thickness = 3
        x = util.allign(thickness,c)
        expected_result = allignment(thickness,c)
        try:
            self.assertEqual(x,expected_result)
        except AssertionError:
            print("Assertion Error")
            raise

    def test_case2(self):
        c = 'M'
        thickness = 2
        x = util.allign(thickness,c)
        expected_result = allignment(thickness,c)
        try:
            self.assertEqual(x,expected_result)
        except AssertionError:
            print("Assertion Error")
            raise

    def test_case3(self):
        c = 'S'
        thickness = 9
        x = util.allign(thickness,c)
        expected_result = allignment(thickness,c)
        try:
            self.assertEqual(x,expected_result)
        except AssertionError:
            print("Assertion Error")
            raise



if __name__ == '__main__':
    unittest.main()
