import unittest
from src.Assignment15 import util
def test_word_order():
    n = int(input().strip())
    counter = {}
    words = []
    for i in range(n):
        word = input().strip()
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
            words.append(word)
    # print(len(words))
    # print(' '.join([str(counter[word]) for word in words]))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected_output = test_word_order()
        x = util.word_order()
        self.assertEqual(x,expected_output)


if __name__ == '__main__':
    unittest.main()
