import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
#from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)

    def test_push(self):
       '''test peek on non empty stack'''
       s = Stack(3)
       s.push(1)
       s.push(2)
       self.assertEqual(s.peek(), 2)

    def test_pop_e(self):
       '''tests pop on empty stack'''
       s = Stack(4)
       with self.assertRaises(IndexError):
           s.pop()

    def test_peek_e(self):
       '''tests peek on empty stack'''
       s = Stack(4)
       with self.assertRaises(IndexError):
           s.peek()

    def test_peek_f(self):
       '''tests peek on full stack'''
       s = Stack(1)
       s.push(2)
       self.assertEqual(s.peek(), 2)

    def test_pop(self):
       '''tests pop on stack'''
       s = Stack(2)
       s.push(1)
       s.push(2)
       s.pop()
       self.assertEqual(s.num_items, 1)

    def test_peek(self):
       '''tests peek on stack'''
       s = Stack(3)
       s.push(1)
       s.push(3)
       self.assertEqual(s.peek(), 3)

    def test_full(self):
       '''test if stack is full'''
       s = Stack(3)
       s.push(1)
       s.push(2)
       s.push(2)
       self.assertEqual(s.is_full(), True)
       s.pop()
       self.assertEqual(s.is_full(), False)

    def test_empty(self):
       '''tests is stack is empty'''
       s = Stack(6)
       self.assertEqual(s.is_empty(), True)
       s.push(6)
       self.assertEqual(s.is_empty(), False)

    def test_numitems(self):
       ''' number of items'''
       s = Stack(2)
       s.push(1)
       s.push(2)
       s.pop()
       self.assertEqual(s.num_items, 1)

    def test_size(self):
       '''tests size of stack'''
       s = Stack(3)
       self.assertEqual(s.size(), 0)
       s.push(1)
       self.assertEqual(s.size(), 1)
       s.pop()
       self.assertEqual(s.size(), 0)

if __name__ == '__main__': 
    unittest.main()
