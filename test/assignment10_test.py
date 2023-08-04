import unittest
from src.Assignment10 import util
"""

When users post an update on social media,such as a URL, image, status update etc.,
other users in their network are able to view this new post on their news feed. 
Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
Since sometimes posts are published and viewed in different time zones,
this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them
"""


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        t = 1
        t1= "Sat 02 May 2015 19:54:36 +0530"
        t2=  "Fri 01 May 2015 13:54:36 -0000"
        expected_output = 88200
        x = util.time_delta(t1,t2)
        try :
            self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion Error")

    def test_case2(self):
        t = 1
        t1= "Sun 10 May 2015 13:54:36 -0700"
        t2=  "Sun 10 May 2015 13:54:36 -0000"
        expected_output = 25200
        x = util.time_delta(t1,t2)
        try :
            self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion Error")

    def test_case3(self):
        t = 1
        t1= "Sun 10 May 2015 13:54:36 -0700"
        t2=  "Fri 01 May 2015 13:54:36 -0000"
        expected_output = 802800
        x = util.time_delta(t1,t2)
        try :
            self.assertEqual(x, expected_output)
        except AssertionError:
            print("Assertion Error")

if __name__ == '__main__':
    unittest.main()
