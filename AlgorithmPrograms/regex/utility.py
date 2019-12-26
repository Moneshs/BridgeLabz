import re
def regex(string,name,fullname,mobilenumber,date):
    x=re.sub("<<name>>",name,string)
    x=re.sub("<<full name>>",fullname,x)
    x=re.sub("xxxxxxxxxx",mobilenumber,x)
    x=re.sub("01/01/2016.",date,x)

    return x