#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 00:02:49 2019

@author: Monesh.S
"""
#importing the math module
import math
#defining the function
def windchill(t,v):
    #storing the speed power of 0.16 into the value
    value=math.pow(v,0.16)
    #calculating the windchill and storing into w
    w=35.74+(0.6215*t)+((0.4275*t)-35.75)*value
    #returning w
    return w