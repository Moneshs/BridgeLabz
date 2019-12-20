#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 05:03:03 2019

@author: MoneshS
"""

import random
def flipcoin(n):
    heads=0
    tails=0
    hpercent=0
    tpercent=0
    for i in range(n):
        coin=random.randint(1,2)
        if coin==1:
            #print("heads")
            heads+=1
        else:
            #print("tails")
            tails+=1
    hpercent=(heads/10)
    tpercent=100.0-hpercent
    print("Heads percent: " + str(hpercent)) 
    print("Tails percent: " + str(tpercent)) 

    
