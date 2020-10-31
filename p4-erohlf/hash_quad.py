class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value=None):
        ''' Inserts an e ntry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1).'''
        hash = self.horner_hash(key)
        if self.hash_table[hash] == None:
            self.hash_table[hash] = Entry(key,value)
            self.num_items += 1
        else:
            self.hash_table[hash].value = value

        if self.get_load_factor() > 0.5:
            self.table_size = (2*self.table_size) + 1
            lst = []
            for i in self.hash_table:
                if i is not None:
                    lst.append(i)
            self.num_items = 0
            self.hash_table = [None] * self.table_size
            for j in lst:
                self.insert(j.key, j.value)

    def horner_hash(self, key):
        ''' Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification.'''
        return self.horner_hash_helper(key, 0)

    def horner_hash_helper(self, key, idx):
        hash_val = (self.compute_horner(key) + idx**2) % self.table_size
        spot = self.hash_table[hash_val]
        if spot is None or spot.key == key:
            return hash_val
        return self.horner_hash_helper(key, idx+1)
    
    def compute_horner(self, key):
        hash = 0
        if len(key) < 8:
            n = len(key)
            for i in range(len(key)):
                hash += ord(key[i]) * 31 ** (n-1-i)
        else:
            n = 8
            for i in range(8):
                hash += ord(key[i]) * 31 ** (n-1-i)

        return hash

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        hash = self.horner_hash(key)
        if self.hash_table[hash] == None:
            return False
        return True

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''
        hash = self.horner_hash(key)
        if self.in_table(key):
            return self.horner_hash(key)
        return None
        
    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        keys = []
        for i in self.hash_table:
            if i is not None:
                keys.append(i.key)
        return keys

    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        if self.in_table(key):
            hash = self.horner_hash(key)
            return self.hash_table[hash].value
        return None
        
    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.num_items/self.table_size
 
