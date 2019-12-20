#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 05:03:03 2019

@author: MoneshS
"""
def harmonic(N):
    harmonic=1.00
    for i in range(2,N+1):
        harmonic+=1/i
    harmonic=round(harmonic,2)
    return harmonic



