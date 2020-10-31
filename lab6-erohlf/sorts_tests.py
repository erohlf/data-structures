import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])
        n = [11,23,25,12,26]
        selection_sort(n)
        self.assertEqual(n, [11,12,23,25,26])

    def test_2(self):
        n = [34,6]
        c = insertion_sort(n)
        self.assertEqual(c,1)
        self.assertEqual(n, [6,34])

if __name__ == '__main__': 
    unittest.main()
