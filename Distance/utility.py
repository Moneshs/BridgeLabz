#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 23:38:20 2019

@author: Monesh.S
"""
#importing the math function 
import math
#defining the function
def distance(x,y):
    #assingning the distance to 0
    distance=0
    #adding the value to distance and using euclidean distance formula
    distance+=math.sqrt((x*x)+(y*y))
    #returning the distance value
    return distance