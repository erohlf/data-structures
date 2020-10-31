import unittest
from queue_array import Queue
#from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test1(self):
        '''check if queue is empty'''
        q = Queue(3)
        self.assertEqual(q.is_empty(), True)
        q.enqueue(3)
        self.assertEqual(q.is_empty(), False)

    def test2(self):
        '''check if queue is full'''
        q = Queue(2)
        q.enqueue(6)
        self.assertEqual(q.is_full(), False)
        q.enqueue(7)
        self.assertEqual(q.is_full(), True)
       
    def test3(self):
        '''test size of queue'''
        q = Queue(3)
        self.assertEqual(q.size(), 0)
        q.enqueue(4)
        self.assertEqual(q.size(), 1)
        q.enqueue(2)
        self.assertEqual(q.size(), 2)
        q.enqueue(7)
        self.assertEqual(q.size(), 3)

    def test4(self):
        '''test enqueue'''
        q = Queue(2)
        q.enqueue(8)
        q.enqueue(6)
        with self.assertRaises(IndexError):
            q.enqueue(5)

    def test5(self):
        '''test dequeue'''
        q = Queue(2)
        q.enqueue(8)
        q.enqueue(9)
        q.dequeue()
        q.dequeue()
        self.assertEqual(q.size(), 0)

    def test6(self):
        '''test dequeue on empty queue'''
        q = Queue(6)
        self.assertEqual(q.is_empty(), True)
        with self.assertRaises(IndexError):
            q.dequeue()

        
if __name__ == '__main__': 
    unittest.main()
