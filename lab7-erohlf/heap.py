
class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.size = 0
        self.capacity = capacity
        self.list = [None]*capacity

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        if self.is_full():
            return False
        self.size += 1
        self.capacity = self.size
        self.list.append(item)
        self.perc_up(self.size)
        return True

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.is_empty():
            return None
        return self.list[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        if self.is_empty():
            return None
        max = self.list[1]
        self.list[1] = self.list[self.size]
        self.list.pop()
        self.size -= 1
        self.perc_down(1)
        return max

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return self.list[1:self.size+1]

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate 
        exactly the number of items in alist'''
        if len(alist) > self.capacity:
            self.capacity = len(alist)
        self.size = len(alist) 
        self.list = [None] + alist[:]
        j = self.size//2     
        while j > 0:
            self.perc_down(j)
            j -= 1
        return True
 

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        return self.size == 0

    def is_full(self):
        '''returns True if the heap is full, false otherwise'''
        return self.size == self.capacity
     
    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return self.capacity
    
    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        return self.size 
        
    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while (2*i) <= self.size:
            greater = 2*i 
            if not 2*i+1 > self.size:
                if self.list[2*i] < self.list[2*i+1]:
                    greater = 2*i+1 
            if self.list[i] < self.list[greater]:
                temp = self.list[greater]  
                self.list[greater] = self.list[i] 
                self.list[i] = temp 
            i = greater
    
        
    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while i//2 > 0:
           if self.list[i] > self.list[i//2]:
               temp = self.list[i//2]
               self.list[i//2] = self.list[i]
               self.list[i] = temp
           i = i//2 

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.build_heap(alist)
        for index in range(1,len(alist)):
            value = alist[index]
            i = index-1
            while i>=0:
                if value < alist[i]:
                    alist[i+1] = alist[i]
                    alist[i] = value
                    i -= 1
                else:
                    break

