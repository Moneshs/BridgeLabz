from utility import binarysearch
list1=[]
with open('file1.txt','r') as f:
    for line in f:
        for word in line.split():
            list1.append(word)
L=sorted(list1)
target=input("Enter the word to search:")
print("targetfound:",binarysearch(L,target))
