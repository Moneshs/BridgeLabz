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
        #sorting the str1 and str2
        str1=sorted(str1)
        str2=sorted(str2)

        for i in range (n1):
            #check each character of both strings are equal together are not
            if str1[i]!=str2[i]:
                return False
            else:
                return True