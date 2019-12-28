"""
Created on Sat Dec 28 6:17:24 2019

@author: Moneshs
"""
from utility import regex
string="""Hello <<name>>, We have your full name as <<full name>> in our system.
your contact number is 91-xxxxxxxxxx.Please,let us know in case of any clarification
Thank you BridgeLabz 01/01/2016."""

#geting name,full name,number and date
name=input("enter the name:")
fullname=input("enter the fullname:")
mobilenumber=input("enter the mobile number:")
date=input("enter the date:")
#calling a function
print(regex(string,name,fullname,mobilenumber,date))