#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 12:17:09 2019

@author: Monesh.S
"""
import time
from utility import stopwatch


print("Enter the Start_time:")
start_time=time.time()


print("Enter the Stop_time:")
stop_time=time.time()

time_elapsed=stop_time-start_time
stopwatch(time_elapsed)
