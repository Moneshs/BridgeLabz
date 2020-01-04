"""
Desc:Take a range of 0 - 1000 Numbers and find the Prime numbers in that range.
     In a 2D Array the numbers that are Anagram and numbers that are not Anagram.

Created on Thu Jan 02 12:03:09 2020
@author: Moneshs
"""

#creating empty list
from Anagramchecker import areAnagrams
prime1=[]
#creating a class prime
class prime:
    #Function to initialize the arr object
    '''
    prime class prints the prime and Anagram  
    '''
    def __init__(self):
        #Initialized list as empty
        self.arr=[]
        
    
    #Function to find the prime numbers
    def primenumber(self,f,n):
        '''
        parameters:int
        f-starting number of start the prime number
        n=Ending number to find prime number till n
        
        return:
          list
             A list returns the prime number
        '''

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
                    prime1.append(i)
                    
        #print(self.prime)
        #print([f,n],self.arr)
        #self.arr.clear()
        self.Anagram(prime)    

    #having a function to call the Anagram checker
    def Anagram(self,prime):
        '''
        parameter:list
          prime1: List of prime numbers
        return:
          None
        '''
        for i in range(0,len(prime1)):
            for j in range(i+1,len(prime1)):
                areAnagrams(prime1[i],prime1[j])

