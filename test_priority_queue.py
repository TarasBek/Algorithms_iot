import unittest
from priority_queue import PriorityQueue



class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.priority = PriorityQueue()
        self.priority.add(45, 0)
        self.priority.add(31, 1)
        self.priority.add(20, 2)
        self.priority.add(14, 3)
        self.priority.add(7, 4)
        self.priority.add(12, 5)
        self.priority.add(18, 6)
        self.priority.add(11, 7)
        self.priority.add(7, 8)

    def test_add(self):
        self.priority.add(50, 9)
        self.assertEqual(self.priority.peek(), 50)




if __name__ == '__main__':
    unittest.main()






