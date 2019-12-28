
"""
Created on Fri Dec 20 05:03:03 2019

@author: MoneshS
"""
#importing the math functions
import math 
#defining the function
def primeFactors(n): 
    #checking the n modulo of 2 is equal to 0.
    while n % 2 == 0: 
        #if true printing 2
        print(2 ), 
        n = n / 2
    #using looping condtions 
    for i in range(3,int(math.sqrt(n))+1,2):
        print(i) 
        while n % i== 0: 
            #if n modulo to i is equal to 0
            print(i), 
            n = n / i 
    #if n is less than 2 return n
    if n > 2: 
        return n 



