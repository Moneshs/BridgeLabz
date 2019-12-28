"""
Created on Sat Dec 28 6:17:24 2019

@author: Moneshs
"""
from utility import insertionsort
#creating a empty list
words=[]
#reading a file for an input
with open('file1.txt','r') as f:
    for line in f:
        for word in line.split():
            #appending the word in to the list
            words.append(word)
#calling the function
sort=insertionsort(words)
#print("hello")
print(sort)