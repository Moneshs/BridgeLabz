#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 05:03:03 2019

@author: MoneshS
"""
#defining the function
def matrix(rows,columns):
    #creating a empty list and assingning into matrix1
    matrix1=[]
    #using looping conditions till rows
    for i in range(rows):
        #creating a empty list and assigning to a 
        a=[]
        #using looping conditions till columns
        for j in range(columns):
            #getting the values and appending to list a
            a.append(int(input()))
            #appending the a  values into matrix1
            matrix1.append(a)

    #printing the rows and columns values like a matrix
    for i in range(rows):
        for j in range(columns):
            print(matrix1[i][j], end=" ")
        print()



