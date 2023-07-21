import unittest

from src.Assignment18 import util

import re
class MyTestCase(unittest.TestCase):
    def test_something(self):
        n = int(input("For test case:"))
        emails = []
        output = ['abc10@gmail.com', 'abc12@gmail.com', 'abc44@gmail.com']
        for i in range(n):
            email = input().strip()
            if util.email_validation(email):
                emails.append(email)
        result = sorted(emails)
        return result

        self.assertEqual(result,output)


if __name__ == '__main__':
    unittest.main()
