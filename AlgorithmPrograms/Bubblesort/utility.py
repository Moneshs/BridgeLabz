"""
Created on Sat Dec 28 6:17:24 2019

@author: Moneshs
"""
#defining the function
def bubblesort(numbers):
    #finding the length of the list
    n=len(numbers)
    #looping condition till n
    for i in range(n):
        #looping condition till 0 to n-i-1
        for j in range(0,n-i-1):
            #traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element
            if numbers[j]>numbers[j+1]:
                numbers[j+1],numbers[j]=numbers[j],numbers[j+1]
    
    return numbers