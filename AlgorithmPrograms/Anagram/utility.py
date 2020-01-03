"""
Created on Sat Dec 28 2:17:24 2019

@author: Moneshs
"""
#defining the function
def anagram(str1,str2):
    #Finding the length of string1 and string2
    n1=len(str1)
    n2=len(str2)
    #checking the length of n1 and n2 if fails print false
    if(n1!=n2):
        return False
    else:
        count=0
        for i in str1:
            for j in str2:
                if i==j:
                   count+=1

        if count==len(str1):
            return True
        else:
           return False