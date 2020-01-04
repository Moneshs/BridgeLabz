"""
Created on Tue Dec 31 12:30:09 2019

@author: Moneshs
"""

#creating a class prime
class prime:

    #Function to initialize the arr object
    def __init__(self):
        #Initialized list as empty
        self.arr=[]
    
    #Function to find the prime numbers
    def primenumber(self,f,n):
        #cornor case
        for i in range(f,n+1):
            if n!=1:
                #check from 2 to n-1
                for j in range(2,i):
                    if i%j==0:
                        break
                else:
                    #append prime numbers into the list
                    self.arr.append(i)
        #print([f,n],self.arr)
        elements=[]
        elements.append([])
        elements.append([])
        elements[0].append([f,n])
        elements[1].append(self.arr)
        #printing the list
        print(elements)
        elements.clear()
        self.arr.clear()
