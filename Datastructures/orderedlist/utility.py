"""
Desc:Read a List of Numbers from a file and arrange it ascending Order
     in a Linked List. Take user input for a number, if found then pop
     the number out of the list else insert the number in appropriate position

Created on Mon Dec 30 02:01:44 2019

@author: Moneshs
"""
from orderedlist import LinkedList
#start with the empty list
new_list=LinkedList()

#Reading the input from the file
with open("numbers.txt", 'r') as num:
    for line in num:
        for word in line.split():
            a=int(word)
            #calling the function
            new_list.asc_ordered_list(a)

#calling a search function of given data
new_list.search_item(122)

new_list.search_item(1)
new_list.display_list()