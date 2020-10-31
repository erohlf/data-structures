# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self):
        with self.assertRaises(ValueError):
            postfix_eval('6 0 /')

   # def test_postfix_eval_06(self):
    #    try:
     #       postfix_eval("3 3 / 1 >>")
      #      self.fail()
       # except PostfixFormatException as e:
        #    self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_07(self):
        self.assertAlmostEqual(postfix_eval('3 4 *'), 12)
        self.assertAlmostEqual(postfix_eval('12 3 /'), 4)
        self.assertAlmostEqual(postfix_eval('1 2 3 * + 4 -'), 3)
        self.assertAlmostEqual(postfix_eval('3 3 2 ** **'), 19683)  
        self.assertAlmostEqual(postfix_eval('3 2 9 + *'), 33)
        self.assertAlmostEqual(postfix_eval('3 3 + 1 <<'), 64)
        self.assertAlmostEqual(postfix_eval('3 3 + 1 >>'), 0)   
   
    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix('4 + 6'), '4 6 +')
        self.assertEqual(infix_to_postfix('2 * 3 / 9'), '2 3 * 9 /')
        self.assertEqual(infix_to_postfix('( 2 - 8 ) * 4'), '2 8 - 4 *')
        self.assertEqual(infix_to_postfix('5 ** 7 * 2'), '5 7 ** 2 *')
        self.assertEqual(infix_to_postfix('6 ** ( 7 ** 2 )'), '6 7 2 ** **')
        self.assertEqual(infix_to_postfix('4 * ( 3 + 2 )'), '4 3 2 + *')  
    
    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix('- * + 1 2 3 * - 4 5 + 6 7'), '1 2 + 3 * 4 5 - 6 7 + * -')


if __name__ == "__main__":
    unittest.main()
