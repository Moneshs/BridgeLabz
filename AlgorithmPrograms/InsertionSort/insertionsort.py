from utility import insertionsort
words=[]
with open('file1.txt','r') as f:
    for line in f:
        for word in line.split():
            words.append(word)

sort=insertionsort(words)
print("hello")
print(sort)