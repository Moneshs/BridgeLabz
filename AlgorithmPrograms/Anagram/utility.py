def anagram(str1,str2):
    n1=len(str1)
    n2=len(str2)
    if(n1!=n2):
        return False
    else:
        str1=sorted(str1)
        str2=sorted(str2)
        for i in range (n1):
            if str1[i]!=str2[i]:
                return False
            else:
                return True