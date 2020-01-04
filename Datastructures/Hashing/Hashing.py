''' 
Desc:Create a Slot of 10 to store Chain of Numbers that belong to each Slot to efficiently
     search a number from a given set of number

Created on Sat Jan 04 17:28:09 2020
@author: Moneshs
 '''
class Node:
    ''' 
    Desc:: Class node gets the arguments data and initialize next has None
     '''
    def __init__(self, data):
        self.data = data
        self.next = None
    ''' 
    Desc:String conversion
     '''
    def __repr__(self):
        return str(self.data)

class LinkedList:
    ''' 
    desc:class linkedlist initilize the head as None
     '''
    def __init__(self):
        self.head = None
    ''' 
    Desc:String conversion
    '''
    def __repr__(self):
        return str(self)
    
    ''' 
    desc:Function inserts the elements into the list
    params:int
        data
    return: None
    '''
    def add(self, data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
    ''' 
    Desc:Method returns the string representation of the object. 
     '''
    def __str__(self):
        str_list = []
        current = self.head
        while current:
            str_list.append(str(current.data))
            current = current.next
        return "[" + "->".join(str_list) + "]"


class ChainedHashTable:
    ''' 
    Desc: Class Hashtable is to store values in the hashtable
     '''
    def __init__(self, size):
        self.links = [None] * size
        self.size = size
    ''' 
    Desc:String conversion
    '''
    def __repr__(self):
        return str(self.links)
     
    ''' 
    Desc:Insert the key in the hash table and if the key has the same value it calls the linkedlist
    params:str
         key
    return: str
        hashmap
     '''
    def insert(self, key):
        lst = self.links[self.hash(key)]
        if lst == None:
            lst = LinkedList()
            node = Node(key)
            lst.add(node)
            self.links[self.hash(key)] = lst
            return

        node = Node(key)
        lst.add(node)
        return

    ''' 
    Desc: Function to find the key value for the hash value
    params: str
          key
    return :
          hash_code
    '''
    def hash(self, key):
        hash_code = (key) % self.size
        #print(hash_code)
        return hash_code