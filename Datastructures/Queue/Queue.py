"""
Desc:Create a Program which creates Banking Cash Counter where people
     come in to deposit Cash and withdraw Cash. Have an input panel to
     add people to Queue to either deposit or withdraw money and dequeue
     the people. Maintain the Cash Balance.
Created on Tue Dec 31 10:04:09 2019

@author: Moneshs
"""
#from cashcounter import queue
#Creating a Class queue
class queue:

    
      # Function to initialize the queue object
    def __init__(self,balance):
        #Initialize queue as empty
        self.queue=[]
        #Assinging Total balance for cash counter 
        self.balance=10000
    
    #Function to initialize the withdraw function
    def withdraw(self,data):
        """
        Desc:Function to withdraw money from Cash counter
        params: int
             data
        return: int
            withdraw amount
        """
        self.queue.append(data)

        # withdraw amount
        withdraw=int(input("enter the amount to withdraw:"))

        #checking whether the amount is less than the total balance
        if self.balance>=withdraw:
            self.balance-=withdraw
            print("user and amount withdraw",self.queue,withdraw)

            #removing from queue after withdraw
            self.queue.pop(0)
        else:
            print("Not sufficient balance in cashing counter and enter lesser amount")
            #calling the same function again
            self.withdraw(int(data))

    #function for the deposit money in cash counter
    def deposit(self,data):
        """
        Desc:Function to deposit money from Cash counter
        params: int
             data
        return: int
            deposit amount
        """
        self.queue.append(data)

        #deposit amount
        deposit=int(input("enter the amount to deposit"))

        #checking whether amount is greater than 0
        if deposit >0:
            self.balance+=deposit
            print("user and amount withdraw",self.queue,self.balance)
            #removing from queue after deposit
            self.queue.pop(0)
        else:
            print("Enter more than 0 ")
            #calling the same function again
            self.deposit(int(data))

    def dequeue(self):
        '''
        desc:function is to remove the members in the queue after
             withdrawing or despositing
        '''
        self.queue.pop(0)        
    
    #Function to display total balance in the cash counter
    def display(self):
        ''' 
        return: display the total balance
         '''
        print(self.balance)

    #Function to return the size of the queue
    def size(self):
        ''' 
         return: Size of the queue
        '''
        s=len(self.queue)
        if s==0:
            print("queue is empty")
        else:
            print("queue length is",s)
