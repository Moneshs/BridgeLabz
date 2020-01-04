''' 
Desc:Create a Slot of 10 to store Chain of Numbers that belong to each Slot to efficiently
     search a number from a given set of number

Created on Sat Jan 04 17:28:09 2020
@author: Moneshs
 '''
from Hashing import ChainedHashTable

cht = ChainedHashTable(11)
cht.insert(1)
cht.insert(4)
cht.insert(36)
cht.insert(3) 
cht.insert(44)
cht.insert(91)
cht.insert(54)
cht.insert(18)
#print(cht)
