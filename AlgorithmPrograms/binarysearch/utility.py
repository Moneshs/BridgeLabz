"""
Created on Sat Dec 28 6:17:24 2019

@author: Moneshs
"""
#defining the function
def binarysearch(arr, start, end, x):
    # check condition
    if end >= start:
        mid = start + (end- start)//2
        # If element is present at the middle
        if arr[mid] == x:
           return mid
        # If element is smaller than mid
        elif arr[mid] > x:
           return binarysearch(arr, start, mid-1, x)
        # Else the element greator than mid
        else:
           return binarysearch(arr, mid+1, end, x)
    else:
   # Element is not found in the array
      return -1