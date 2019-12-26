from utility import computer_guess
def main():
    num = int(input("Enter a number: "))
    if num < 1 or num > 100:
        print("Must be in range [1, 100]")
    else:
        computer_guess(num)

if __name__ == '__main__':
    main()