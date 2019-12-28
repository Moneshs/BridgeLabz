#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 23:25:14 2019

@author: Monesh
"""
#defining the function
def triplets(arr,n):
    #initializing the found variable to true
    found=True
    #using looping conditions
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                #checking which 3 variables is added and equal to 0
                if(arr[i]+arr[j]+arr[k]==0):
                    #return the 3 variables which are equal to 0
                    return (arr[i], arr[j], arr[k])
                    found=True
                    
    #if found is equal to false then there is no element in the array is equal to zero.
    if(found==False):
        print("No triplets")