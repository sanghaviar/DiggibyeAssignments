import unittest
from src.Assignment6 import util

def convert_number(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        result1 = deci.rjust(width)
        result2 = octa.rjust(width)
        result3 = hexa.rjust(width)
        result4 = bina.rjust(width)


class MyTestCase(unittest.TestCase):

    def test_case1(self):
        number = 3  # any integer
        expected_output = convert_number(number)
        x = util.print_formatted(number)

        try:
            self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion Error")
            raise

    def test_case2(self):
        number = 6 # any integer
        expected_output = convert_number(number)
        x = util.print_formatted(number)

        try:
            self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion Error")
            raise

    def test_case3(self):
        number = 3  # any integer
        expected_output = convert_number(number)
        x = util.print_formatted(number)

        try:
            self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion Error")
            raise

if __name__ == '__main__':
    unittest.main()
