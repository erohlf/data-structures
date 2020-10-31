
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.front = None
        self.back = None
        self.num_items = 0


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        return self.num_items == 0

   
    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        return self.num_items == self.capacity


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if self.is_full() == True:
            raise IndexError('full queue')
        elif self.is_empty() == True:
            new = Node(item)
            self.rear = new
            self.front = new
            self.num_items += 1
        else:
            new = Node(item)
            self.rear.next = new
            self.rear = new
            self.num_items += 1


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.is_empty() == True:
            raise IndexError('empty queue')
        else:
            top = self.front
            self.front = self.front.next
            self.num_items -= 1
            return top.data


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items
