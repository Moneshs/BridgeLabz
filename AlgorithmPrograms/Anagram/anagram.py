"""
Created on Sat Dec 28 2:17:24 2019

@author: Moneshs
"""
from utility import anagram
#Getting the string1 from the user
str1=input("Enter the string1:")
#getting the string2 from the uset
str2=input("Enter the string2:")
#calling the function and checks the condition
if(anagram(str1,str2)):
    print("Its an Anagram")
else:
    print("Its not an Anagram")