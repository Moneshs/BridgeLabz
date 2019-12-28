#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 04:45:35 2019

@author: MONESH.s
"""
from utility import leapyear
#Getting the userinput as a year
year=int(input("enter the year"))
#initializing a count value as 0
count=0
#counting the digits entered by user 
while(year!=0):
    year//=10
    count+=1
print(count)
#calling the function
leapyear(year,count) 

#if conditions is true prints leap year
if(leapyear(year,count)):
    print("Its a Leap year")
else:
    print("its a not leapyear")