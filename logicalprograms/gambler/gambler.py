#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 12:17:09 2019

@author: Monesh.S
"""
from utility import gambler
#getting userinput for the stake,goal and no of trails
s= int(input("enter the stake value:"))
g= int(input("enter the goal value:"))
n= int(input("enter the trails:"))
#calling the function
gambler(s,g,n)