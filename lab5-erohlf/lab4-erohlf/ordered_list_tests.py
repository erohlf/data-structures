import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)


    def test_add(self):
        o = OrderedList()
        o.add(10)
        self.assertEqual(o.head.item, 10)
        o.add(12)
        self.assertEqual(o.tail.item, 12)
        self.assertFalse(o.add(12))

    def test_index(self):
        o = OrderedList()
        o.add(4) 
        o.add(5)
        o.add(7)
        self.assertEqual(o.index(4), 0)
        self.assertEqual(o.index(5), 1)
        self.assertEqual(o.index(7), 2)
        self.assertEqual(o.index(6), None)

    def test_pop(self): 
        o = OrderedList()
        o.add(2)
        o.add(3)
        o.add(4)
        o.add(5)
        o.add(6)
        o.add(7)
        self.assertEqual(o.pop(0), 2)
        self.assertEqual(o.pop(3), 6)

    def test_remove(self):
        o = OrderedList()
        o.add(1)
        o.remove(1)
        self.assertEqual(o.head, None)
        self.assertEqual(o.tail, None)
        self.assertEqual(o.size(), 0)
        o.add(2)
        o.add(3)
        o.add(4)
        o.remove(4)
        self.assertEqual(o.tail.item, 3)


if __name__ == '__main__': 
    unittest.main()


