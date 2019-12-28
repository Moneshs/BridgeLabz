"""
Created on Sat Dec 28 6:17:24 2019

@author: Moneshs
"""
from utility import permute
#getting a string from user 
string=input("enter the string:")
#finding the length of the string
n=len(string)
a=list(string)
#calling the function
permute(a,0,n-1)