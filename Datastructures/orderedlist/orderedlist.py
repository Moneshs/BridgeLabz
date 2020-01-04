"""
Desc:Read a List of Numbers from a file and arrange it ascending Order
     in a Linked List. Take user input for a number, if found then pop
     the number out of the list else insert the number in appropriate position

Created on Mon Dec 30 12:07:24 2019

@author: Moneshs
"""

# Node class 
class Node: 
    ''' 
    desc: Class node gets the arguments data and initialize next has None
     '''
    # Function to initialize the node object 
    def __init__(self, data):
        # Assign data 
        # Initialize  
        # next as null 
        self.data = int(data)
        self.next = None
        
        
list1=[]
#Linkedlist class
class LinkedList:
    ''' 
    desc:class linkedlist initilize the head as None
     '''
    # Function to initialize the Linked  
    # List object 
    def __init__(self):
        self.head = None    
    
    #Function sorts into ascending order
    def asc_ordered_list(self, data):
        ''' 
        desc:Function inserts the elements in the ascending order
        params:int
             data
        return: returns the list in the ascending order
         '''
        #print(type(data))
        new_node = Node(data)
        #checks the head is none or not
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        if temp.data > data:
            new_node.next = temp
            self.head = new_node
            return

        while temp.next:
            if temp.next.data > data:
                break
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    # This function prints contents of linked list 
    # starting from head
    def display_list(self):
        ''' 
        desc: displays the list in the linkedlist
        params: int
             data
        return: returns the list
         '''
        #check head node is None or not
        if self.head is None:
           print("List has no elements")
           return
       
        temp = self.head
        #Traverse till None  
        while temp is not None:
            print(temp.data)
            list1.append(temp.data)
            temp = temp.next

    #This function search contents of linked list
    # starting from head        
    def search_item(self,data):
        ''' 
        desc: Function searches the element in the list or not
        input: int
              data
        return: data
         '''
        print(type(data))
        if self.head is None:
            print("List is empty")
            return
        n=self.head
        #traversing till end of the Node
        while n is not None:
            if n.data==data:
                
                #calling a delete function 
                self.delete_item(data)
                return
            n=n.next
            
        else:
            #calling the ordered list function to insert a item
            self.asc_ordered_list(data)
            return

    #This function delete contents of linked list
    # starting from head to specific number to delete     
    def delete_item(self,data):
        ''' 
        desc:Functions deletes the element from the list
        return:
            list
         '''
        if self.head is None:
            print("no element to delete")
            return

        #checks the head is equal to specific number
        if self.head.data==data:
            self.head=self.head.next
            return
        n=self.head
        #checks till last node, stops when the items found
        while n.next is not None:
            if n.next.data==data:
                break
            n=n.next
            
        if n.next is None:
            print("item not found in the list")
            self.asc_ordered_list(data)
        else:
            n.next=n.next.next

#writing the elements into a new file
with open("numbers1.txt", 'w') as f:
    for listitem1 in list1:
        f.write('%s '%listitem1)
