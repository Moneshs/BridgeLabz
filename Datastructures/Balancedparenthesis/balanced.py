"""
Desc: Take an Arithmetic Expression such as (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) where
 parentheses are used to order the performance of operations. Ensure parentheses must
 appear in a balanced fashion.

Created on MON Dec 30 04:20:35 2019
@author: MONESH.s
"""
class Node:
    ''' 
    desc:Class node is takes the arguments data
    params: str
          data
     '''
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    ''' 
    desc:Class stack creates two variable top and count
    params:int
         top,count    
     '''
    # creating the variables top and a count variable
    def __init__(self):
        self.top = -1
        self.count = 0

    def push(self, data):
        ''' 
        desc:Function push elements in the stack
        params: str
              data
        returns:
              values in the stack
        '''
        # inserting the element at the top
        # creating the node object and passing the given data to it and assigning the given data to it.
        node = Node(data)
        node.data = data
        node.next = None
        # if in top there are no elements then given data will be assigned as top
        if self.top is None:
            self.top = node
            self.count += 1
        # else the next of the top element is assigned as node and the  top is assigned as node
        else:
            node.next = self.top
            self.top = node
            self.count += 1
        #self.show()

    def pop(self):
        ''' 
        desc:Function popping the element from the stack
        params:str
            stack[data]
        return:
            top-1
         '''
        # removes the top element
        # if stack is empty it will prints the below context
        if not Stack.isEmpty(self):
            self.top=self.top.next
            self.count-=1
        else:
            print("empty")
    
    def isEmpty(self):
        ''' 
        desc:Function find the stack is empty or not
        params:str
             top
        return:
            true
         '''
        # returns weather the stack is empty or not
        if self.top is -1:
            return True
        else:
            return False

    def peek(self):
        ''' 
        returns:top element in the stack
         '''
        # Prints the top element
        print(self.top.data)

    def size(self):
        ''' 
        returns: Size of the stack
        '''
        # returns the count value if it is not equals to 0
        if self.count < 0:
            print("Out of index")
        # else returning the count
        else:
            return self.count