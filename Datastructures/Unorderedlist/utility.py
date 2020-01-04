"""
Desc: Read the Text from a file, split it into words and arrange it
      as Linked List. Take a user input to search a Word in the List.
      If the Word is not found then add it to the list, and if it
      found then remove the word from the List. In the end save the list into a file

Created on Mon Dec 30 11:03:09 2019

@author: Moneshs
"""

from linkedlist import Linkedlist

#Starting with the empty list
new_linked_list = Linkedlist()

#Reading the file for the input
with open('file.txt','r') as f:
    for line in f:
        for word in line.split():
            #calling the insert function to insert into linkedlist
            new_linked_list.insert_end(word)

#calling search function
new_linked_list.search_item('linear')

new_linked_list.search_item('linear')
print("\nAfter searching item in linkedlist:")
new_linked_list.traverse_list()

