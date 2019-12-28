"""
Created on Sat Dec 28 6:17:24 2019

@author: Moneshs
"""
def prime(n):
    for i in range(2,n+1):
         # Corner case
        if i>1:
            for j in range(2,i):
                # check from 2 to n-1 
                if(i%j==0):
                    break
            else:
                #return i
                #calling the function palindrome
                palindrome(i)

#creating a empty list                           
l=[]             
print("The palindrome numbers are:")
def palindrome(i):
    temp=i
    #storing the prime no's in the list
    l.append(i)
    rev=0
    # Iterative function to reverse 
    # digits of i 
    while(i>0):
        dig=i%10
        rev=rev*10+dig
        i=i//10
    # Check if temp and rev are same or not.
    if(temp==rev):
        print(temp)