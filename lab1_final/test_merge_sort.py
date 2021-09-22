import unittest
from merge_sort import merge_sort, Sort

arr = [2, 8, 1, 3, 6, 7, 5, 4]
sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8]
desc_arr =  [8, 7, 6, 5, 4, 3, 2, 1]

class testMergeSort(unittest.TestCase):
    def testSortingInputArray(self):
        merge_sort(arr)
        self.assertEqual(arr, sorted(arr))

    def testSortingByASC(self):
        merge_sort(arr)
        self.assertEqual(arr, sorted(arr))

    def testSortingByDESC(self):
        merge_sort(arr, Sort.DESC)
        self.assertEqual(arr, sorted(arr, reverse= True))



