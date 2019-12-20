#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 05:03:03 2019

@author: MoneshS
"""
def factors(n):
    N=1
    if n>0 and n<32:
        for i in range(1,n+1):
            N=2*N
        return N
    else:
        print("enter less than 32")


