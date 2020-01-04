"""
Desc: Read the Text from a file, split it into words and arrange it
      as Linked List. Take a user input to search a Word in the List.
      If the Word is not found then add it to the list, and if it
      found then remove the word from the List. In the end save the list into a file
Created on Mon Dec 30 09:48:51 2019

@author: Moneshs
"""
#from utility import new_linked_list
# Node class 
class Node:
    ''' 
    desc: Class node gets the arguments data and initialize next has None
    '''
    # Function to initialize the node object 
    def __init__(self,data):
        # Assign data 
        # Initialize  
        # next as null
        self.item=data
        self.next=None
lis=[]

#Linkedlist class
class Linkedlist:
    ''' 
    desc:class linkedlist initilize the head as None
     '''
    # Function to initialize the Linked  
    # List object 
    def __init__(self):
        self.start_node=None

    # This function prints contents of linked list 
    # starting from head    
    def traverse_list(self):
        ''' 
        desc: displays the list in the linkedlist
        params: int
             data
        return: returns the list
        '''
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n=self.start_node
            #Traverse till the n is none
            while n is not None:
                print(n.item, end=" "),
                lis.append(n.item)
                n=n.next

    #This function inserts contents of linked list        
    def insert_end(self,data):
        ''' 
        desc:Function inserts the elements end of linkedlist
        params:str
             data
        return: returns the list
         '''
        new_node=Node(data)
        #checks whether the head is None or not
        if self.start_node is None:
            self.start_node=new_node
            return
        n=self.start_node
        #Traverse till n.next is none
        while n.next is not None:
            n=n.next
        n.next=new_node
    
    #This function searchs words in the linked list 
    #starting from head
    def search_item(self,data):
        ''' 
        desc: Function searches the element in the list or not
        input: int
              data
        return: data
         '''
        #checks whether the head is none or not
        if self.start_node is None:
            print("List is empty")
            return
        n=self.start_node
        #Traverse till n is not none
        while n is not None:
            #check whether the data is present in the linkedlist
            if n.item==data:
                #calling the delete function
                self.delete_item(data)
                return
            n=n.next

        else:
            #calling the insert function
            self.insert_end(data)
            return
    
    #This functions deletes data from the linked list
    def delete_item(self,data):
        ''' 
        desc:Functions deletes the element from the list
        return:
            list
        '''
        #checks whether head node is none or not
        if self.start_node is None:
            print("no element to delete")
            return
        #checks whether is head node is equal
        if self.start_node.item==data:
            self.start_node=self.start_node.ref
            return
        n=self.start_node
        #traverse till n.next is not none
        while n.next is not None:
            if n.next.item==data:
                break
            n=n.next
            
        if n.next is None:
            print("item not found in the list")
            self.insert_end(data)
        else:
            n.next=n.next.next

#Writing the linkedlist into the file       
with open("file1.txt", 'w') as output:
    for listitem in lis:
        output.write('%s '%listitem)