#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 05:03:03 2019

@author: MoneshS
"""
#defining a function
def factors(n):
    #initializing the N as 1
    N=1
    #using condition statement where n value  lies between the range 
    if n>0 and n<32:
        #using looping condition till the n value
        for i in range(1,n+1):
            #multiplying by 2 and storing into N
            N=2*N
        #returning the N value
        return N
    #conditions fails
    else:
        print("enter less than 32")


