''' 
desc:You are given N nodes, each having unique value ranging from [1, N],
     how many different binary search tree can be created using all of them.
Created on Sat Jan 04 10:18:09 2020

@author: Moneshs
'''
from bstcount import Bst
if __name__ == '__main__': 
    B=Bst()
    n =int(input("Enter the number of testcases:"))
    for i in range(n):
        count1=0 
	    # find count of BST in n nodes
        N=int(input("Enter Number of nodes "))
        count1 = B.countBst(N)
        # print count of BST
        print("count of BST",count1)
	