#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 12:17:09 2019

@author: Monesh.S
"""
#importing time function
import time
#calling a sub-modules from the directory
from utility import stopwatch

#storing the epoch starting time 
print("Enter the Start_time:")
start_time=time.time()

#storing the epoch stopped time
print("Enter the Stop_time:")
stop_time=time.time()

#subtracting the stop time and start_time it will be stored in secs
time_elapsed=stop_time-start_time
#calling the function
stopwatch(time_elapsed)
