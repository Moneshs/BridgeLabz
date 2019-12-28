"""
Created on Sat Dec 28 6:17:24 2019

@author: Moneshs
"""
def mergesort(arr):
    if len(arr)>1:
        #Finding the mid of the array 
        mid=len(arr)//2
        # Dividing the array elements 
        #into 2 halves
        L=arr[mid:]      
        R=arr[:mid]
        
        mergesort(L)
        mergesort(R)
        
        i=j=k=0
        #Copy data to temp arrays L[]and R[]
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        #checking if any element was right
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1