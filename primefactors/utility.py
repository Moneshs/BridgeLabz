#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 05:03:03 2019

@author: MoneshS
"""
import math 
def primeFactors(n): 
    while n % 2 == 0: 
        print(2 ), 
        n = n / 2

    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            print(i), 
            n = n / i 

    if n > 2: 
        return n 



