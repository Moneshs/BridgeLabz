#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 05:03:03 2019

@author: MoneshS
"""
#defining a function
def harmonic(N):
    #Assining a harmanic value as float 1.00
    harmonic=1.00
    #using looping conditions from 2 to n+1
    for i in range(2,N+1):
        #incrementing a harmonic variable by 1/i
        harmonic+=1/i
    #using round function for 2 decimal values
    harmonic=round(harmonic,2)
    #returning the result
    return harmonic



