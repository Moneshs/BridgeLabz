def prime(n):
    for i in range(2,n+1):
        if i>1:
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                #return i
                palindrome(i)
                
l=[]             
print("The palindrome numbers are:")
def palindrome(i):
    temp=i
    l.append(i)
    rev=0
    while(i>0):
        dig=i%10
        rev=rev*10+dig
        i=i//10
    if(temp==rev):
        print(temp)