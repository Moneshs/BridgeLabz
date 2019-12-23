#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 00:02:31 2019

@author: Monesh.S
"""

import sys
from utility import windchill
t=int(input("Enter the temperature:"))
if(t>50):
    print("temperature should be lessthan 50")
    sys.exit()
    
v=int(input("Enter the speed:"))
if(t>120 and t<3):
    print("speed should be lessthan 120 and greater than 3")
    sys.exit()
    
windchill(t,v)