#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 04:45:35 2019

@author: MONESH.s
"""
from utility import leapyear

year=int(input("enter the year"))
count=0
while(year!=0):
    year//=10
    count+=1
print(count)
leapyear(year,count) 

if(leapyear(year,count)):
    print("Its a Leap year")
else:
    print("its a not leapyear")