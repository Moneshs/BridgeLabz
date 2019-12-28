#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 23:51:35 2019

@author: Monesh.S
"""
#importing the cmath
import cmath
#defining the function
def quadratic(a,b,c):
    #using quadratic equation formula to find the roots value of given value of a,b,c
    delta=(b**2) -(4*a*c)
    #print(delta)
    root1=(-b+cmath.sqrt(delta))/(2*a)
    #print(root1)
    root2=(-b-cmath.sqrt(delta))/(2*a)
    #print(root2)
    #returning the values of delta,root1 and root2 value
    return delta,root1,root2