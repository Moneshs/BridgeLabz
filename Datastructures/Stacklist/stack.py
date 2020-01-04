"""
Desc:Add the Prime Numbers that are Anagram in the Range of 0 - 1000
     in a Stack using the Linked List and Print the Anagrams in the 
     Reverse Order

Created on Thu Jan 02 14:36:09 2020
@author: Moneshs
"""

class Node: 
	
	# Class to create nodes of linked list 
	# constucter initializes node automatically 
	def __init__(self,data): 
		self.data = data 
		self.next = None
	
class Stack: 
    """
    desc:This a class for stack using linkedlist
    """
	# head is default NULL 
    def __init__(self):
        """
        desc:Constructor for stack class
        """
        self.head = None

	# Method to add data to the stack 
	# adds to the start of the stack 
    def push(self,data):
        '''
        desc:function to push  the data in to stack using linked list
        params:int
        data
        return :None type
        None
        '''
		
        if self.head == None:
            self.head=Node(data)
        else: 
            newnode = Node(data) 
            newnode.next = self.head 
            self.head = newnode
    
    def reverseList(self): 
        '''
        desc:this function to reverse the stack
        params:data

        return:object
            
        '''
		# Stack to store elements of list 
        stk = [] 
	
		# Push the elements of list to stack 
        ptr = self.head 
        print(ptr)
        while ptr.next != None: 
            stk.append(ptr) 
            ptr = ptr.next
	
		# Pop from stack and replace 
		# current nodes value' 
        self.head = ptr 
        while len(stk) != 0: 
            ptr.next = stk.pop() 
            ptr = ptr.next
		
        ptr.next = None
	
	# Prints out the stack	 
    def display(self):
        curr = self.head
        while curr: 
            print(curr.data, end = " ") 
            curr = curr.next