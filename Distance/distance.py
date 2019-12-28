#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 23:36:29 2019

@author: Monesh.S
"""

from utility import distance
#getting the X value from user
x=int(input("enter the X value:"))
#getting the y values from user
y=int(input("enter the y value:"))

print("Euclidean distance of x and y is:")
#calling the function
distance(x,y)
