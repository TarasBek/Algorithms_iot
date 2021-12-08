from RabinKarp import *

import unittest


class TestRabinKarp(unittest.TestCase):

    def setUp(self):
        self.prime_num = 101
        self.pattern = "THIS IS A TEST TEXT"
        self.text = "TE"
        self.pattern_2 = "AABAACAADAABAABA"
        self.text_1 = "TARAS"

    def test_1(self):
        self.assertEqual(rabin_carp(self.pattern, self.text, self.prime_num), (8))

    def test_2(self):
        self.assertEqual(rabin_carp(self.pattern_2, self.text_1, self.prime_num), ())


if __name__ == '__main__':
    unittest.main()
