from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        return self.root == None

    def search(self, key): # returns True if key is in a node of the tree, else False
        top = self.root
        while top != None and top.key != key:
            if key < top.key:
               top = top.left
            else:
               top = top.right
        return top != None

    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        if self.root == None:
            self.root = TreeNode(key, data)
            
        else:
            top = self.root
            pos = None
            while top != None:
                pos = top
                if key < top.key:
                    top = top.left
                elif key > top.key:
                    top = top.right  
                elif key == top.key:
                    pos.data = data
                    break
            if key < pos.key:
                pos.left = TreeNode(key, data)
            elif key > pos.key:
                pos.right = TreeNode(key, data)

    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty() == True:
            return None
        else:
            top = self.root
            while top.left != None:
                top = top.left
            return top.key, top.data

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty() == True:
            return None
        else:
            top = self.root
            while top.right != None:
                top = top.right
            return top.key, top.data

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.is_empty():
            return None
        return self.tree_height_helper(self.root) - 1
 
    def tree_height_helper(self, node):
        if node == None:
            return 0    
        left = self.tree_height_helper(node.left)
        right = self.tree_height_helper(node.right)
        if left > right:
            return left + 1
        else:
            return right + 1
 

    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        return self.inorder_list_helper(self.root)

    def inorder_list_helper(self, node): 
       if node == None:
           return []
       return self.inorder_list_helper(node.left) + [node.key] + self.inorder_list_helper(node.right)

           

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        return self.preorder_list_helper(self.root)

    def preorder_list_helper(self, node):
        if node != None:
            return [node.key] + self.preorder_list_helper(node.left) + self.preorder_list_helper(node.right)
        return []

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this!
        if self.root == None:
            return None 
        else:
            lst = []
            root = q.enqueue(self.root)
        while q.is_empty() == False:
            item = q.dequeue()
            lst.append(item.key)
            if item.left != None:
                q.enqueue(item.left)
            if item.right != None:
                q.enqueue(item.right)
        return lst
        

