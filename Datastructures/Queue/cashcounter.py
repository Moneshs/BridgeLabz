"""
Desc:--> queue means it will add the elements at rear and removes the first element
     --> it follows FIFO First In Last Out
     --> it consists front ad rear
         1. front --> front of the queue
         2.rear --> last of the queue
     --> enqueue adds the element at the rear
     --> deque remove the element at first


Created on Tue Dec 31 10:40:09 2019.
  
@author: Moneshs
"""
from Queue import queue
#Starting with the empty queue
queue=queue('3')
#looping till the wrong input
while(1):
    options=int(input("enter 1 for withdraw or enter 2 for deposit:"))

    #checking condition statement whether it is deposit or withdraw
    if options==1:
        id=input("enter the passbook id for withdraw:")
        #calling the withdraw function
        queue.withdraw(id)
    elif options==2:
        id=input("enter the passbook id for deposit:")
        #calling the deposit function
        queue.deposit(id)
    else:
        print("enter the valid option")
        break
#calling display and size of queue function
queue.display()
queue.size()