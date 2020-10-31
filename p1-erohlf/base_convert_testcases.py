import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base162(self):
        self.assertEqual(convert(316,16),"13C")
    
    def test_base17(self):
        self.assertEqual(convert(412,17),None)

    def test_base8(self):
        self.assertEqual(convert(87,8),'127')

    def test_base11(self):
        self.assertEqual(convert(168,11),'143')

    def test_base13(self):
        self.assertEqual(convert(452,13),'28A')

    def test_base10(self):
        self.assertEqual(convert(143,10),'143')

    def test_base12(self):
        self.assertEqual(convert(553,12),'3A1')
    
    def test_base14(self):
        self.assertEqual(convert(553,14),'2B7')
 
    def test_base15(self):
        self.assertEqual(convert(553,15),'26D')

    def test_base152(self):
        self.assertEqual(convert(404,15),'1BE')

    def test_base16(self):
        self.assertEqual(convert(447,16),'1BF') 
if __name__ == "__main__":
        unittest.main()
