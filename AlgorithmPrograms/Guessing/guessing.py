"""
Created on Sat Dec 28 6:17:24 2019

@author: Moneshs
"""
from utility import computer_guess

def main():
    #Getting the number from user
    num = int(input("Enter a number: "))
    #checking whether the number is in given range
    if num < 1 or num > 100:
        print("Must be in range [1, 100]")
    else:
        #calling the function
        computer_guess(num)

if __name__ == '__main__':
    main()