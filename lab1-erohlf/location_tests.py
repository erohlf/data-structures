import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    # Add more tests!

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc==loc2)

    def test2_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("San Clemente", 35.3, -120.7)
        self.assertNotEqual(loc,loc2)

if __name__ == "__main__":
        unittest.main()
