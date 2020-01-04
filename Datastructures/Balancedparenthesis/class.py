"""
Desc: Take an Arithmetic Expression such as (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) where
      parentheses are used to order the performance of operations. Ensure parentheses 
      must appear in a balanced fashion.

Created on MON Dec 30 05:36:35 2019
@author: MONESH.s
"""
from balanced import Stack

class BalancingParenthesis:
    '''
    Desc:Class for balancedparenthesis or not
    '''
    if __name__ == '__main__':
        # taking the expression in the form of String
        String = str(input("Enter the Expression : "))
        # creating the stack object
        s = Stack()
        length = len(String)
        # Traversing the loop in the range of length of String
        # And taking each character
        for i in range(length):
            c = String[i]
            # if the character c is equals to '(' then it will push to the stack 
            # else it will continue the loop
            if c == "(":
                s.push("(")
                #s.show()
            # if the character c is equals to ')' then it will pop the data from the queue
            elif c == ")":
                
                s.pop()
                #s.show()
    
        # After the loop finished then the checking the stack is empty or not
        check = s.isEmpty()
        size=s.size()
        print(size)
        # if the stack is empty then the given expression is balanced
        if check==True:
            print("Balanced parenthesis ")
        # else the given expression is balanced
        else:
            print("not balanced parenthesis")