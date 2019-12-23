#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 00:02:49 2019

@author: Monesh.S
"""
import math
def windchill(t,v):
    value=math.pow(v,0.16)
    w=35.74+(0.6215*t)+((0.4275*t)-35.75)*value
    return w