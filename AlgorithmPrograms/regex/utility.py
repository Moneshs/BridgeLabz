"""
Created on Sat Dec 28 6:17:24 2019

@author: Moneshs
"""
import re
#using sub function to replace the words  in the string
def regex(string,name,fullname,mobilenumber,date):
    x=re.sub("<<name>>",name,string)
    x=re.sub("<<full name>>",fullname,x)
    x=re.sub("xxxxxxxxxx",mobilenumber,x)
    x=re.sub("01/01/2016.",date,x)
    #returning the string
    return x