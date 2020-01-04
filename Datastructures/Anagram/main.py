"""
Desc:Take a range of 0 - 1000 Numbers and find the Prime numbers in that range.
     In a 2D Array the numbers that are Anagram and numbers that are not Anagram.

Created on Thu Jan 02 12:20:09 2020

@author: Moneshs
"""

from anagram import prime,prime1
from Anagramchecker import A,B
#starting with the empty list
s=prime()
s.primenumber(1,1000)
merge=A+B
Anagram=set(merge)
prime2=set(prime1)
NotAna=prime2.difference(Anagram)
C=sorted(NotAna)
D=(sorted(Anagram))
#Creating a empty list to store anagram and not anagram
elements=[]
elements.append([])
elements.append([])
elements[0].append(C)
elements[1].append(D)
#printing the list
print(elements)
