import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(check_expression('3 4 +'))
        self.assertTrue(check_expression('4 5 -'))
        self.assertTrue(check_expression('34 06 *'))
        self.assertTrue(check_expression('27 8 /'))
        self.assertTrue(check_expression('5 4 **'))
        self.assertTrue(check_expression('6'))
        self.assertTrue(check_expression('1 2 3 4 5 6 - - - - -'))

    def test_invalid(self):
        try:
            check_expression('7h34')
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Invalid token')

    def test_invalid2(self):
        try:
            check_expression('1 - 4 5')
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Too many operands')

    def test_invalid3(self):
        try:
            check_expression('5 + -')
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Insufficient operands')

    def test_postfix1(self):
        try:
            postfix_eval('5 + -')
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Insufficient operands')
    
    def test_postfix2(self):
        try:
            postfix_eval('1 - 4 5')
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Too many operands')

    def test_postfix3(self):
        try:
            check_expression('14k6')
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Invalid token')

    def test_postfix4(self):
        with self.assertRaises(ValueError):
            postfix_eval('6 0 /')
 
    def test_precendence(self):
        self.assertEqual(op_precedence('('), 1)
        self.assertEqual(op_precedence('+'), 2)
        self.assertEqual(op_precedence('-'), 2)
        self.assertEqual(op_precedence('*'), 3)
        self.assertEqual(op_precedence('/'), 3)
        self.assertEqual(op_precedence('**'), 4)
        self.assertEqual(op_precedence('>>'), 5)
        self.assertEqual(op_precedence('<<'), 5)

    def test_reverse(self):
        self.assertEqual(revers('123'), '321')

    def test_calculate(self):
        self.assertEqual(calculate('-', 5, 2), -3)
        self.assertEqual(calculate('+', 6, 7), 13)
        self.assertEqual(calculate('/', 2, 8), 4)
        self.assertEqual(calculate('*', 5, 4), 20)
        self.assertEqual(calculate('**', 3, 2), 8)
        self.assertEqual(calculate('<<', 3, 2), 12)
        self.assertEqual(calculate('>>', 27, 4), 1)

    def test_calculate2(self):
        with self.assertRaises(ValueError):
            calculate('/', 0, 6)
        with self.assertRaises(PostfixFormatException):
            calculate('>>', 1.5, 8)
        with self.assertRaises(PostfixFormatException):
            calculate('<<', 5, 2.3) 

    def test_postfix_eval1(self):
        try:
            postfix_eval('3 3 / 1 >>')
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Illegal bit shift operand')

    def test_postfix_eval11(self):
        try:
            postfix_eval('3 3 / 1 <<')
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), 'Illegal bit shift operand')

    def test_postfix_eval2(self):
        self.assertAlmostEqual(postfix_eval('3 4 *'), 12)
        self.assertAlmostEqual(postfix_eval('12 3 /'), 4)
        self.assertAlmostEqual(postfix_eval('1 2 3 * + 4 -'), 3)
        self.assertAlmostEqual(postfix_eval('3 3 2 ** **'), 19683)
        self.assertAlmostEqual(postfix_eval('3 2 9 + *'), 33)
        self.assertAlmostEqual(postfix_eval('3 3 + 1 <<'), 64)
        self.assertAlmostEqual(postfix_eval('3 3 + 1 >>'), 0)

    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix('6 - 3'), '6 3 -')
        self.assertEqual(infix_to_postfix('6'), '6')
        self.assertEqual(infix_to_postfix('4 + 6'), '4 6 +')
        self.assertEqual(infix_to_postfix('2 * 3 / 9'), '2 3 * 9 /')
        self.assertEqual(infix_to_postfix('( 2 - 8 ) * 4'), '2 8 - 4 *')
        self.assertEqual(infix_to_postfix('2 ** 3 ** 2'), '2 3 2 ** **')

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix('* - 3 / 2 1 - / 4 5 6'), '3 2 1 / - 4 5 / 6 - *')
        self.assertEqual(prefix_to_postfix('- * + 1 2 3 * - 4 5 + 6 7'), '1 2 + 3 * 4 5 - 6 7 + * -')


    

if __name__ == '__main__':
    unittest.main()

