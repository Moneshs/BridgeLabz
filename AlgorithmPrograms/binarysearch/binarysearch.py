"""
Created on Sat Dec 28 6:17:24 2019

@author: Moneshs
"""
from utility import binarysearch
#creating a empty list
list1=[]
#opening and reading a text file for input
with open('file1.txt','r') as f:
    for line in f:
        for word in line.split():
            #appending the words into the list
            list1.append(word)

#sorting the words
L=sorted(list1)
print(L)
#getting the target word from the user
target=input("Enter the word to search:")
#calling the function
print("targetfound:",binarysearch(L,0,len(L)-1,target))
