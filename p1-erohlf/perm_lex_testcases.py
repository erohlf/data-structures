import unittest
from perm_lex import *

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        '''test on 2 character string'''
        self.assertEqual(perm_gen_lex('ab'),['ab','ba'])
   
    def test2_perm_gen_lex(self):
        '''test on 3 character string'''
        self.assertEqual(perm_gen_lex('abc'),['abc','acb','bac','bca','cab','cba'])
    
    def test3_perm_gen_lex(self):
        '''test on 1 character string'''
        self.assertEqual(perm_gen_lex('k'),['k'])

    def test4_perm_gen_lex(self):
        '''test on empty string'''
        self.assertEqual(perm_gen_lex(''),[])

if __name__ == "__main__":
        unittest.main()
