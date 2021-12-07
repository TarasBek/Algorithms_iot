import unittest
from main import find_ways_count


class FindWaysCountTest(unittest.TestCase):

    def test_find_ways_count(self):
        matrix = [
            ["a", "a", "a"],
            ["c", "a", "b"],
            ["d", "e", "f"]
        ]
        output = 5
        ways_count = find_ways_count(matrix, 3, 3)
        self.assertEqual(ways_count[0][2]+ways_count[2][2], output)

        matrix = [['a', 'b', 'c', 'd', 'e', 'f', 'a', 'g', 'h', 'i']]
        output = 2
        ways_count = find_ways_count(matrix, 10, 1)
        self.assertEqual(ways_count[0][9] + ways_count[0][9], output)

        matrix = [['a', 'a', 'a', 'a', 'a', 'a', 'a'],
                  ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
                  ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
                  ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
                  ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
                  ['a', 'a', 'a', 'a', 'a', 'a', 'a']]

        output = 201684
        ways_count = find_ways_count(matrix, 7, 6)
        self.assertEqual(ways_count[0][6] + ways_count[5][6], output)