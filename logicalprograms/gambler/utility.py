#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:17:09 2019

@author: Monesh.S
"""
#importing the random function 
import random
#defining the function
def gambler(s,g,n):
    #initializing bets and wins to 0 
    bets=0
    wins=0
    #using looping function to till the number of trails
    for i in range(n):
        #assingning stake money to cash variable
        cash=s
        #using looping conditions till cash is greater than 0 and cash is greater than goal
        while(cash>0 and cash<g):
            #incrementing bets each time if conditions true 
            bets+=1
            #using random function getting a value between the range
            if(random.randrange(0,2)==0):
                #if conditions is true cash will be incremented
                cash+=1
                #if not decrementing the cash
            else:
                cash-=1
        #If cash is equal to goal increment the wins
        if cash==g:
            wins+=1
    #printing no of wins in the given trails
    print("no of wins",wins)
    win=100*wins//n
    #win percentage and lose percentage
    print(str(win)+'%wins')
    print(str(100.0-win)+'%lose')