"""
Created on Sat Dec 28 6:17:24 2019

@author: Moneshs
"""
def tostring(list):
    return ''.join(list)

# Function to print permutations of string 
# This function takes three parameters: 
# 1. String 
# 2. Starting index of the string 
# 3. Ending index of the string.
def permute(a,l,r):
    if(l==r):
        print(tostring(a))
    else:
        #recursive function
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            permute(a,l+1,r)
            #backtrack
            a[l],a[i]=a[i],a[l]
            