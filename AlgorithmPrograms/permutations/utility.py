def tostring(list):
    return ''.join(list)

def permute(a,l,r):
    if(l==r):
        print(tostring(a))
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            # print("first",a[l],a[i])
            permute(a,l+1,r)
            a[l],a[i]=a[i],a[l]
            #print("second",a[l],a[i])