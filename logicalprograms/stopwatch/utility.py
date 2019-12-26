#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 12:17:24 2019

@author: Moneshs
"""
def stopwatch(secs):
    mins=secs//60
    secs=secs%60
    hours=mins//60
    mins=mins%60
    
    print("Time lapsed={0}:{1}:{2}".format(int(hours),int(mins),secs))
