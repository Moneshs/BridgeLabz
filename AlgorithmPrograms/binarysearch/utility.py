"""
Created on Sat Dec 28 6:17:24 2019

@author: Moneshs
"""
#defining the function
def binarysearch(L,target):
    #initializing the value 0 to variable first
    first=0
    #getting length of the list
    r=len(L)-1
    #using loop till first is less than the length of list 
    while(first<=r):
        #finding the median of the list
        middle=(first+r)//2

        mid=L[middle]
        #checking condition where target greater than the median
        if (mid > target): 
            end= middle-1
            return end
        #checking condition where target less than the median
        elif(mid < target): 
            first= middle + 1
        #other wise print the median value
        else:
            return mid
