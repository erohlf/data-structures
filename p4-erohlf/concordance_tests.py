import unittest
import subprocess
from concordance import *


class TestList(unittest.TestCase):


    def test_01(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        err = subprocess.call("diff -wb file1_con.txt file1_sol.txt", shell = True)
        self.assertEqual(err, 0)

        
    def test_02(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        err = subprocess.call("diff -wb file2_con.txt file2_sol.txt", shell = True)
        self.assertEqual(err, 0)

        
    def test_03(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        err = subprocess.call("diff -wb declaration_con.txt declaration_sol.txt", shell = True)
        self.assertEqual(err, 0)

    def test_04(self):
        conc = Concordance()
        with self.assertRaises(FileNotFoundError):
            conc.load_stop_table("kc.txt")
        with self.assertRaises(FileNotFoundError):
            conc.load_concordance_table("kc.txt")

    def test_05(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("dictionary_a-c.txt")
        conc.write_concordance("dictionary_a-c_con.txt")

    #def test_06(self):
    #    conc = Concordance()
    #    conc.load_stop_table("stop_words.txt")
    #    conc.load_concordance_table("War_And_Peace.txt")
    #    conc.write_concordance("War_And_Peace_con.txt")

    #def test_07(self):
    #    conc = Concordance()
    #    conc.load_stop_table("stop_words.txt")
    #    conc.load_concordance_table("file_the.txt")
    #    conc.write_concordance("file_the_con.txt")



        
if __name__ == '__main__':
    unittest.main()
