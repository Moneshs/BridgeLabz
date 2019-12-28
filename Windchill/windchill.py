#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 00:02:31 2019

@author: Monesh.S
"""
#importing the sys module
import sys
from utility import windchill
#getting the temeperture value from the user
t=int(input("Enter the temperature:"))
#checking the temperature should be less than 50
if(t>50):
    print("temperature should be lessthan 50")
    sys.exit()
#getting the speed values from the user   
v=int(input("Enter the speed:"))
#checking the user value which speed should not exceed more than 120 and less than 3
if(t>120 and t<3):
    print("speed should be lessthan 120 and greater than 3")
    sys.exit()
 #calling the function   
windchill(t,v)