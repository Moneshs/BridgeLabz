"""
Created on Sat Dec 28 6:17:24 2019

@author: Moneshs
"""
from utility import mergesort
numbers=[98,45,65,54,23,12,89,2,24,78]

#Calling the function
mergesort(numbers)

#print the sorted list
for i in range(len(numbers)):
    print(numbers[i],end=' ')
print()