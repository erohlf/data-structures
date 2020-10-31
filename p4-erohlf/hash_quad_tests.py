import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_02(self):
        ht = HashTable(5)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 2)
        ht.insert("f", 0)
        self.assertEqual(ht.get_index("f"), 3)
        ht.insert("k", 0) #causes rehash
        self.assertEqual(ht.get_index("a"), 9)
        self.assertEqual(ht.get_index("f"), 3)
        self.assertEqual(ht.get_index("k"), 8)

    def test_03(self): 
        ht = HashTable(191)
        ht.insert('cat',4)
        self.assertFalse(ht.in_table("dog"))
        ht.insert('cat',8)
        self.assertEqual(ht.get_value('dog'), None)
        self.assertEqual(ht.get_index('dog'), None)
        self.assertEqual(ht.get_num_items(), 1)
        self.assertEqual(ht.get_value('cat'),8)
        ht.insert('dog',4)
        self.assertEqual(ht.get_num_items(), 2)
        self.assertEqual(ht.get_all_keys(), ['cat','dog'])
        self.assertTrue(ht.in_table("dog"))
        ht.insert('bird',4)
        ht.insert('horse',15)
        ht.insert('horse',11)
        self.assertEqual(ht.get_value('horse'),11)
        self.assertEqual(ht.get_num_items(), 4)
        self.assertEqual(ht.get_load_factor(), 4/191)
        ht.insert('salamander')

if __name__ == '__main__':
   unittest.main()
