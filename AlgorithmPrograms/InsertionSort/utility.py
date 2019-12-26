def insertionsort(words):
    for i in range(1,len(words)):
        tmp=words[i]
        j=i-1
        while j>=0 and words[j]>tmp:
            words[j+1]=words[j]
            j=j-1
        words[j+1]=tmp
    return words