class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.head = None
        self.tail = None


    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        return self.head == None

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''
        
        new = Node(item)
        current = self.head
        insert = False

        while (not insert):

            if self.is_empty() == True:
                self.tail = new
                self.head = new
                insert = True
            
            elif current.prev == None and new.item < current.item:
                new.next = current
                current.prev = new
                self.head = new
                insert = True
            
            elif new.item < current.item:
                new.next = current
                new.prev = current.prev
                current.prev.next = new
                current.prev = new
                insert = True
 
            elif current.item == new.item:
                 return False
            
            elif self.tail.item < new.item:
                self.tail.next = new
                new.prev = self.tail
                self.tail = new
                insert = True

            else:
                current = current.next

        if insert == True:
            return True
        return False

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        delete = False
        current = self.head
        while not delete:
            if self.head.next == None:
                if self.head.item == item:
                    self.tail = None
                    self.head = None
                    delete = True

            elif self.head.item == item:
                 self.head = self.head.next
                 self.head.prev = None
                 delete = True

            elif self.tail.item == item:
                self.tail = self.tail.prev
                self.tail.next = None
                delete = True

            elif current.item == item:
                nexts = current.next
                prevs = current.prev
                prevs.next = nexts
                nexts.prev = prevs
                delete == True
 
            else:
                current = current.next

        if delete == True:
            return True

        return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        idx = 0
        current = self.head
        while current.item != item:
              current = current.next
              if current == None:
                 return None
              else:
                  idx += 1

        return idx

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        
        if index < 0 or index > self.size():
            raise IndexError('- or bigger than list')

        elif index == 0 and self.size() > 1:
            temp = self.head
            self.head.next.prev = None
            self.head = self.head.next
            return temp.item

        elif index == 0 and self.size() == 1:
            temp = self.head
            self.head = None
            return temp.item

        elif index == self.size() - 1:
            temp = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return temp.item

        elif index <= self.size()//2 - 1 and index <= self.size():
            current = self.head
            idx = 0
            while idx != index:
                current = current.next
                idx += 1
            prevs = current.prev
            nexts = current.next
            prevs.next = nexts
            nexts.prev = prevs
            return current.item

        elif index >= self.size()//2 + 1 and index <= self.size():
            current = self.tail
            idx = self.size() - 1
            while idx != index:
                current = current.prev
                idx -= 1
            prevs = current.prev
            nexts = current.next
            prevs.next = nexts
            nexts.prev = prevs
            return current.item
         

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
       
        if self.head == None:
            return False 
        elif self.head.item == item:
            return True 
        else:
            return self.search(self.head.next, item)
        

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        return self.python_list2(self.head)

    def python_list2(self, node):    
        if node == None:
            return []
        else:
           lst = []
           lst.append(node.item)
           return lst + self.python_list2(node.next)

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.python_list_reversed2(self.tail)

    def python_list_reversed2(self, node):
        if node == None:
            return []
        else:
            lst = []
            lst.append(node.item)
            return lst + self.python_list_reversed2(node.prev)            

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_helper(self.head)

    def size_helper(self, node):
        if node == None:
            return 0
        return 1 + self.size_helper(node.next)
        
