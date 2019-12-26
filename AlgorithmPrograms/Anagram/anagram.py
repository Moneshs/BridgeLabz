from utility import anagram
str1=input("Enter the string1:")
str2=input("Enter the string2:")
if(anagram(str1,str2)):
    print("Its an Anagram")
else:
    print("Its not an Anagram")