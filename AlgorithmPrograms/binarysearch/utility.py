def binarysearch(L,target):
    #print(L)
    first=0
    r=len(L)-1 
    while(first<=r):
        middle=(first+r)//2
        mid=L[middle]
        if (mid > target): 
            end= middle-1
            return end
        elif(mid < target): 
            first= middle + 1
        else:
            return mid
