"""
desc:Take a range of 0 - 1000 Numbers and find the Prime numbers in that range. 
Created on Tue Dec 31 14:20:09 2019

@author: Moneshs
"""

from primenumber import prime
#starting with the empty list
s=prime()
n=1000

for i in range(10):
    #calling the prime function
    s.primenumber(n-99,n)
    n=n-100
    #checking whether the n is less than 100
    if n<=100:
        #calling the prime function
        s.primenumber(n-98,n)
        break