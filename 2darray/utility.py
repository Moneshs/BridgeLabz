#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 05:03:03 2019

@author: MoneshS
"""
def matrix(rows,columns):
    matrix1=[]
    for i in range(rows):
        a=[]
        for j in range(columns):
            a.append(int(input()))
            matrix1.append(a)

    for i in range(rows):
        for j in range(columns):
            print(matrix1[i][j], end=" ")
        print()



