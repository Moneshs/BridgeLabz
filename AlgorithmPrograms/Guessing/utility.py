"""
Created on Sat Dec 28 6:17:24 2019

@author: Moneshs
"""
#defining the function
def computer_guess(num):
    #assigning values to low,high and guess
    low = 1
    high = 100
    guess = 50

    #checking through loop where guess is not equal not num
    while guess != num:
        
        guess = (low+high)//2
        print("The computer takes a guess...", guess)
        #checking whether the guess is less than num or greater than num
        if guess > num:
            high = guess
        elif guess < num:
            low = guess + 1

    print("The computer guessed", guess, "and it was correct!")