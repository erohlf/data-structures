import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test2_max_list_iter(self):
        '''test where max is first index'''
        tlist = [18,4,5,3,6]
        self.assertEqual(max_list_iter(tlist),18)

    def test3_max_list_iter(self):
        '''test where max is last index'''
        tlist = [1,3,2,4,8]
        self.assertEqual(max_list_iter(tlist),8)

    def test3_max_list_iter(self):
        '''test where two indicies are the max value'''
        tlist = [-1,-4,-5,-1,-2]
        self.assertEqual(max_list_iter(tlist),-1)

    def test4_max_list_iter(self):
        '''test where max is in the middle'''
        tlist = [1,2,9,3,4]
        self.assertEqual(max_list_iter(tlist),9)
    
    def test_reverse_rec(self):
        '''test where list is not empty and has lengh greater than 1'''
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
    
    def test2_reverse_rec(self):
        '''test where list is empty'''
        self.assertEqual(reverse_rec([]),[])

    def test3_reverse_rec(self):
        '''test where list is of length 1'''
        self.assertEqual(reverse_rec([1]),[1])

    def test4_reverse_rec(self):
        '''test where list is None'''
        int_list = None
        with self.assertRaises(ValueError):
            reverse_rec(int_list)

    def test_bin_search(self):
        '''test where target is in middle of list'''
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

    def test2_bin_search(self):
        '''tests empty list'''
        list_val = []
        self.assertEqual(bin_search(0,0,len(list_val)-1,list_val),None)

    def test3_bin_search(self):
        '''tests case when target is higher than list range'''
        list_val = [1,2,3,4]
        self.assertEqual(bin_search(5,0,len(list_val)-1,list_val),None)
    
    def test4_bin_search(self):
        '''tests case when target is lower than list range'''
        list_val = [3,4,5,6,7]
        self.assertEqual(bin_search(2,0,len(list_val)-1,list_val),None)

    def test5_bin_search(self):
        '''tests case when target is within the range but not in the list'''
        list_val = [1,2,6,7,8]
        self.assertEqual(bin_search(4,0,len(list_val)-1,list_val),None)

    def test6_bin_search(self):
        '''tests case when target is first index'''
        list_val = [1,2,3,4,5]
        self.assertEqual(bin_search(1,0,len(list_val)-1,list_val),0)
    
    def test7_bin_search(self):
        '''tests case when target is last index'''
        list_val = [3,4,5,6,7,8,9]
        self.assertEqual(bin_search(9,0,len(list_val)-1,list_val),6)
    
    def test8_bin_search(self):
        ''' tests case when list is none'''
        list_val = None
        with self.assertRaises(ValueError):
            bin_search(1,0,0,list_val)
if __name__ == "__main__":
        unittest.main()

    
