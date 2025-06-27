# #You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.
# Note that:
#The valid operators are '+', '-', '*', and '/'.
#Each operand may be an integer or another expression.
#The division between two integers always truncates toward zero.
#There will not be any division by zero.
#The input represents a valid arithmetic expression in a reverse polish notation.
#The answer and all the intermediate calculations can be represented in a 32-bit integer.


class Solution(object):
    def evalRPN(self, tokens):

      # MY LOGIC + REASONING :
        # stack + dict that has operators + functionality to be used
        # a, b
        # if operator in dict -- > pop last two in stack + operate
        # append to stack

        #  *NB******8 lambda arguments: expression  --> how lambda is used    *NB******
        stack = []
        operators = ['+', '-', '*', '/']

        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(float(a) / float(b)) if b != 0 else 0,        # initially does floating point division and then 'ints' it after as per Q 
        }

        for token in tokens:
            if token in operators:
                a = stack.pop()
                b = stack.pop()
                result = ops[token](b, a)
                stack.append(result)
            else:
                stack.append(int(token))

        # when it all works out, there should only be one element left in the stack -- >> this should be thr final total
        return stack[0]
        
