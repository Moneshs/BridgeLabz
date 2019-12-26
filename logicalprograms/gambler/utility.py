import random
def gambler(s,g,n):
    bets=0
    wins=0
    for i in range(n):
        cash=s
        while(cash>0 and cash<g):
            bets+=1
            if(random.randrange(0,2)==0):
                cash+=1
            else:
                cash-=1
        if cash==g:
            wins+=1
    print("no of wins",wins)
    win=100*wins//n
    print(str(win)+'%wins')
    print(str(100.0-win)+'%lose')