#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 05:03:03 2019

@author: MoneshS
"""

def leapyear(year,count):
    
    if(count==4):
        if(((year%4==0)and(year%100!=0))or(year%400==0)):
            return True
        else:
            return False
    else:
        print("enter four digit number")

    
