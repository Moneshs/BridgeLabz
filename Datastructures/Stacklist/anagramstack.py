"""
Desc:Add the Prime Numbers that are Anagram in the Range of 0 - 1000
     in a Stack using the Linked List and Print the Anagrams in the 
     Reverse Order

Created on Thu Jan 02 14:36:09 2020
@author: Moneshs
"""

from primes import prime
from Anagramchecker import A,B
from stack import Stack

#starting with the empty list
s=prime()
s.primenumber(1,1000)

merge=A+B
Anagram=set(merge)
list1=sorted(Anagram)
'''
return : None type
     returns the anagram list in reverse order 
     from the stack using linked list
'''
#Starting with the empty stack
MyStack = Stack()

#Traversing each value from till end of the list
for i in range(len(list1)):
    MyStack.push(list1[i])

#calling the reverse list from the class
MyStack.reverseList()
# Display stack elements 
MyStack.display()