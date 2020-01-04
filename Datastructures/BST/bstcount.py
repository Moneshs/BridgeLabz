''' 
desc:You are given N nodes, each having unique value ranging from [1, N],
     how many different binary search tree can be created using all of them.
Created on Sat Jan 04 10:18:09 2020

@author: Moneshs
 '''

class Bst:
    ''' 
    Desc: Class Bst is to find how many differsnt bst using all of them
    '''
    def countBst(self,n):
        '''
        Desc: Function is to find the total no. of different binary search tree
        input: int
             n
        return: list
            countbst[n]
        ''' 
        if (n == 0 or n == 1): 
            return 1
  
        # Table to store results of subproblems 
        countBst = [0 for i in range(n + 1)] 
  
        # Initialize first two values in table 
        countBst[0] = 1
        countBst[1] = 1
  
        # Fill entries in countBst[] using recursive formula 
        for i in range(2, n + 1): 
            countBst[i] = 0
            for j in range(i): 
                countBst[i] = countBst[i] + countBst[j] * countBst[i-j-1] 
  
        # Return last entry 
        return countBst[n]