import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertFalse(bst.is_empty())
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_empty(self):
        b = BinarySearchTree()
        self.assertTrue(b.is_empty())
     
    def test_search(self):
        b = BinarySearchTree()
        b.insert(12, 'a')
        b.insert(13, 'b')
        self.assertTrue(b.search(13))
        self.assertFalse(b.search(8))

    def test_insert(self):
        b = BinarySearchTree()
        b.insert(6, 'a')
        b.insert(5, 'b')
        b.insert(5, 'e')
        b.insert(7, 'u')
        b.insert(7, 'l')
        
    def test_max_min(self):
        b = BinarySearchTree()
        self.assertEqual(b.find_min(), None)
        self.assertEqual(b.find_max(), None)
        b.insert(7, 'w')
        b.insert(4, 'r')
        b.insert(8, 'g')
        self.assertEqual(b.find_min(), (4, 'r'))
        self.assertEqual(b.find_max(), (8, 'g'))

    def test_norder(self):
        b = BinarySearchTree()
        b.insert(9, 'f')
        b.insert(6, 'd') 
        b.insert(14, 'g')
        b.insert(3, 'r')
        b.insert(11, 'y')
        b.insert(14, 't')
        b.insert(6, 'x')
        self.assertEqual(b.inorder_list(), [3,6,9,11,14])
        self.assertEqual(b.preorder_list(), [9,6,3,14,11])
        self.assertEqual(b.level_order_list(),[9,6,14,3,11]) 
        self.assertEqual(b.tree_height(), 2)
        self.assertEqual(b.search(3), True)
        self.assertEqual(b.search(4), False)
        self.assertEqual(b.search(11), True)

    def test_height(self):
        b = BinarySearchTree()
        self.assertEqual(b.tree_height(), None)
        b.insert(5, 'k')
        self.assertEqual(b.tree_height(), 0)
        b.insert(6, 'l')
        self.assertEqual(b.tree_height(), 1)
        b.insert(4, 'p')
        self.assertEqual(b.tree_height(), 1)

    def test_oroder(self):
        b = BinarySearchTree()
        self.assertEqual(b.inorder_list(), [])
        self.assertEqual(b.preorder_list(), [])
        self.assertEqual(b.level_order_list(), None)

if __name__ == '__main__': 
    unittest.main()
