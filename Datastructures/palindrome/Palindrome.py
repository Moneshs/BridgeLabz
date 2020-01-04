''' 
desc: A palindrome is a string that reads the same forward and backward,
      for example, radar, toot, and madam. We would like to construct an
      algorithm to input a string of characters and check whether it is a palindrome.
Created on Fri Jan 03 13:37:09 2020

@author: Moneshs
 '''
class Node:
    ''' 
    Desc: class Node gets the argument data and initialize the next as None
    '''
    def __init__(self,data):
        self.data=data
        self.next=None

class Dequeue:
    ''' 
    Desc:class Dequeue initializing the front,rear and count varible
     '''
    def __init__(self):
        # creating the variables front and rear and a count variable
        self.front = None
        self.rear = None
        self.count = 0

    def insertFront(self, data):
        ''' 
        Desc: Function inserts the elements in the front
        input: str
            data
        return: None
         '''
        # inserting the element from the front
        # creating the node object and passing the given data to it and assigning the given data to it.
        node = Node(data)
        node.data = data
        node.next = None
        # if the queue is empty it means front is none then the given data is the front data
        if self.front is None:
            self.front = self.rear = node
        # else given data will assigned to the next to the front and assigning the given node as front of the queue
        node.next = self.front
        self.front = node
        self.count += 1

    def insertRear(self, data):
        ''' 
        Desc: Function inserts the elements in the end
        input: str
            data
        return: None
         '''
        # Inserting the data at the last of the queue
        # creating the node object and passing the given data to it and
        # assigning the given data to it.
        node = Node(data)
        node.data = data
        node.next = None
        # if the queue is empty it means front is none then the given data is the rear data
        if self.rear is None:
            self.front = self.rear = node
        # else given data will assigned to the next to the rear and assigning
        # the given node as rear of the queue
        self.rear.next = node
        self.rear = node
        self.count += 1

    def isEmpty(self):
        ''' 
        Desc:whether the deque is empty or not
        return:
            boolean
         '''
        # if the front element is none means there is noo element in the queue then the list is empty
        if self.front is None:
            return True
        else:
            return False

    def removeFront(self):
        ''' 
        Desc:Removes the element from Front
        Return:
             None
         '''
        # removing the front element in the queue
        #  if size is zero then queue is empty
        if Dequeue.size(self) == 0:
            return None
        # if the there are one element in the queue then deleting by referring it to the none
        else:
            if self.front.next is None:
                n = self.front.data
                self.front = None
                return n
            # removing the front data and assigning the next to the front element as the front
            else:
                n = self.front.data
                self.front = self.front.next
                self.count -= 1
                return n

    def removeRear(self):
        ''' 
        Desc:Removes the element from end
        Return:
             None
         '''
        # removing the rear element in the queue
        #  if size is zero then queue is empty
        if Dequeue.size(self) == 0:
            return None
        else:
            # taking the size of the queue and traversing before to the last element
            #  And referring the last as None
            itr = Dequeue.size(self)
            temp = self.front
            for i in range(0, itr - 1):
                temp = temp.next
            n = temp.data
            temp = self.rear
            self.rear = temp
            self.count -= 1
            return n
            temp.data = None

    def size(self):
        ''' 
        Desc:Function find the size of the deque

        return: int
            size of the deque
         '''
        # returns the count value if it is not equals to 0
        if self.count < 0:
            print("Out of index")
        # else returning the count
        else:
            return self.count

    def show(self):
        ''' 
        Desc: Displays the deque
        returns:
             deque
         '''
        # traversing from front element to the last element
        # printing the data at each node
        temp = self.front
        itr = Dequeue.size(self)
        for i in range(0, itr):
            print(temp.data, end=" ")
            temp = temp.next

