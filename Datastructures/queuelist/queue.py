"""
Desc:Add the Prime Numbers that are Anagram in the Range of 0 - 1000
     in a Queue using the Linked List and Print the Anagrams from the Queue

Created on Thu Jan 02 14:36:09 2020
@author: Moneshs
"""

class Node:
    # Class to create nodes of linked list 
	# constucter initializes node automatically 
    def __init__(self,data):
        self.data=data
        self.next=None


class Queue:
    """
    desc:This class is for Queue using linkedlist 
    """

    def __init__(self):
        """ 
        desc:Constructor for Queue class
        """
        self.head =None
    
    def enqueue(self,data):
        """ 
        desc:function to enqueue the data into the queue
        params:int 
            data
        return:Node
           NoneType
         """
        
        new_item = Node(data)
        current = self.head
        if current is None:
            self.head = new_item
        else:
            while current.next:
                current = current.next
            current.next=new_item
        
    
    def display(self):
        """ 
        desc:Function to display the queue
        params:Node
        return:int
            data
         """
        temp=self.head
        
        while temp.next is not None:
            print(temp.data, end=" ")
            print(type(temp.data))
            temp=temp.next
        print(temp.data)