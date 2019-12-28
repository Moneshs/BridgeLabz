"""
Created on Sat Dec 28 6:17:24 2019

@author: Moneshs
"""
#function for insertion sort
def insertionsort(words):

    # Traverse through 1 to len(arr)
    for i in range(1,len(words)):
        tmp=words[i]
        j=i-1
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position
        while j>=0 and words[j]>tmp:
            words[j+1]=words[j]
            j=j-1
        words[j+1]=tmp
    #returning the words
    return words