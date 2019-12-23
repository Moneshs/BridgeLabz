#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 23:25:14 2019

@author: user
"""

def triplets(arr,n):
    found=True
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if(arr[i]+arr[j]+arr[k]==0):
                    return (arr[i], arr[j], arr[k])
                    found=True
    
    if(found==False):
        print("No triplets")