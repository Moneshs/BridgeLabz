#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 05:03:03 2019

@author: MoneshS
"""
#defining  a function
def leapyear(year,count):

    #checking the year count has 4 
    if(count==4):
        #cheking the leapyear or not with the condition statement
        if(((year%4==0)and(year%100!=0))or(year%400==0)):
            return True
        else:
            return False
    #the year count not equal to 4 else condtions works.
    else:
        print("enter four digit number")

    
