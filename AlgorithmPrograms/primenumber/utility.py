"""
Created on Sat Dec 28 6:17:24 2019

@author: Moneshs
"""
def prime(n):
    for i in range(2,n+1):
         # Corner case
        if i>1:
            for j in range(2,i):
                # check from 2 to n-1 
                if(i%j==0):
                    break
            else:
                print(i)