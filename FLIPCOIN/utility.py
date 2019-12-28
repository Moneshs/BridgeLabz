#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 05:03:03 2019

@author: MoneshS
"""
#importing the random function
import random
#defining the function
def flipcoin(n):
    #initializing the value of head,tails,hpercent,tpercent to 0
    heads=0
    tails=0
    hpercent=0
    tpercent=0
    #using looping till the n value
    for i in range(n):
        #getting random value between 1 and 2 and storing into the coin
        coin=random.randint(1,2)
        #print(coin)
        #using conditional statement whether coin is equal to 1 or not
        if coin==1:
            #print("heads")
            #condition is true head is incremented by 1
            heads+=1
        else:
            #condtion fails tails is incremented by 1
            #print("tails")
            tails+=1

    hpercent=(heads/10)
    tpercent=100.0-hpercent
    #returning the percentage of heads and tails
    return hpercent,tpercent
    #print("Heads percent: " + str(hpercent)) 
    #print("Tails percent: " + str(tpercent)) 

    
