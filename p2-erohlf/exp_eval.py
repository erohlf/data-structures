
from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ^ or numbers
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    op_stack = Stack(30)
    tokens = input_str.split()
    op_list = ['+', '-', '/', '*', '**', '<<', '>>']

    if check_expression(input_str) == True:
        for i in tokens:
            if i not in op_list:
                try:
                    int(i)
                    op_stack.push(int(i))
                except ValueError:
                    float(i)
                    op_stack.push(float(i))
            else:
                num1 = op_stack.pop()
                num2 = op_stack.pop()
                solution = calculate(i, num1, num2)
                try:
                    int(solution)
                    op_stack.push(solution)
                except ValueError:
                    float(solution)
                    op_stack.push(solution)
  
        return float(op_stack.pop())
    else:
        return check_expression(input_str)


def calculate(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num2 - num1
    if operator == '*':
        return num2 * num1
    if operator == '/':
        if num1 == 0:
            raise ValueError('division by zero')
        return num2 / num1
    if operator == '**':
        return num2 ** num1
    if operator == '>>':
        try:
            int(str(num1))
            int(str(num2))
        except ValueError:
            raise PostfixFormatException('Illegal bit shift operand')    
        else:
            return num1 // 2**num2
    if operator == '<<':
        try:
            int(str(num1))
            int(str(num2))
        except ValueError:
            raise PostfixFormatException('Illegal bit shift operand')
        else:
            return num1 * 2**num2
 

def check_expression(pf_string):
    op_stack = Stack(30)
    op_stack_num = Stack(30)
    op_list = ['+', '-', '/', '*', '**', '>>', '<<']
    tokens = pf_string.split()

    for i in tokens:
        if i not in op_list:
            dummy = None
            try:
                int(i)
                dummy = True
                op_stack_num.push(i)
            except ValueError:
                try:
                    float(i)
                    dummy = False
                    op_stack_num.push(i)
                except ValueError:
                    pass
        if i in op_list:
            op_stack.push(i) 
        if i not in op_list and dummy == None:
            raise PostfixFormatException('Invalid token')

    if op_stack_num.size() <= op_stack.size():
        raise PostfixFormatException('Insufficient operands')

    if op_stack_num.size() > (op_stack.size() + 1):
        raise PostfixFormatException('Too many operands')

    return True
 
             
def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    op_stack = Stack(30)
    pf_list = []
    infix = input_str.split()
    op_list = ['+', '-', '/', '*', '**', '>>', '<<', '(', ')']

    for i in infix:
        if i not in op_list:
            pf_list.append(i)
        elif i == '(':
            op_stack.push(i)
        elif i == ')':
            top = op_stack.pop()
            while top != '(':
                pf_list.append(top)
                top = op_stack.pop()
        else:
            if i == '**':
                while (op_stack.is_empty() == False) and (op_precedence(op_stack.peek()) > op_precedence(i)):
                    pf_list.append(op_stack.pop())
                op_stack.push(i)
            else:
                while (op_stack.is_empty() == False) and (op_precedence(op_stack.peek()) >= op_precedence(i)):
                    pf_list.append(op_stack.pop())
                op_stack.push(i)
    
    while op_stack.is_empty() == False:
        pf_list.append(op_stack.pop())
    return " ".join(pf_list)


def op_precedence(op):
    if op == '(':
        return 1
    if op == '+' or op == '-':
        return 2
    if op == '*' or op == '/':
        return 3
    if op == '**':
        return 4
    if op == '>>' or op == '<<':
        return 5

def revers(str):
    return str[::-1]


def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    op_stack = Stack(30)
    prefix = revers(input_str)
    prefix = prefix.split()
    op_list = ['+', '-', '*', '/', '**', '>>', '<<', '(', ')']
    
    for i in prefix:
        if i not in op_list:
            op_stack.push(i)
        else:
            op1 = op_stack.pop()
            op2 = op_stack.pop()
            string = op1 + " " + op2 + " " + i
            op_stack.push(string)
  
    return op_stack.pop()


