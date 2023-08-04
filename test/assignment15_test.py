import unittest
from src.Assignment15 import util

"""
Given n words. Some words may repeat. 
For each word, output its number of occurrences.
The output order should correspond with the input order of apperance of the word.
"""


def test_word_order(n, words_list):
    counter = {}
    words = []
    for word in words_list:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
            words.append(word)

class MyTestCase(unittest.TestCase):
    def test_case1(self):
        n = 3
        words_list = ["cat", "rat", "bat", "cat"]
        expected_output = test_word_order(n, words_list)
        x = util.word_order(n, words_list)
        self.assertEqual(x, expected_output)
    def test_case2(self):
        n = 4
        words_list = ["python", "java", "pyspark", "spark"]
        expected_output = test_word_order(n, words_list)
        x = util.word_order(n, words_list)
        self.assertEqual(x, expected_output)

    def test_case3(self):
        n = 3
        words_list = ["map", "globe", "earth", "sky"]
        expected_output = test_word_order(n, words_list)
        x = util.word_order(n, words_list)
        self.assertEqual(x, expected_output)


if __name__ == '__main__':
    unittest.main()
