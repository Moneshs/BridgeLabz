#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 23:51:35 2019

@author: Monesh.S
"""

import cmath
def quadratic(a,b,c):
    delta=(b**2) -(4*a*c)
    #print(delta)
    root1=(-b+cmath.sqrt(delta))/(2*a)
    #print(root1)
    root2=(-b-cmath.sqrt(delta))/(2*a)
    #print(root2)
    return delta,root1,root2