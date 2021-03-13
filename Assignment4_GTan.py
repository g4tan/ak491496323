#In this program, I define a function call checkprime(num) which takes any integer in a for-loop.
#The for-loop takes an input num % the iterations to catch non-prime number; otherwise, prime numbers.
#the second else statement in my function handles num<=1 values which are non-prime.
#The bottom codes are basically just my previous assignment codes.
def checkprime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num, "is a not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num,"is not a prime number")
try:
    while True:
        num = int(input("Please enter a number: "))
        checkprime(num)
        Another = input("Do you want to try again?(Y or N )")
        if Another == "y" or Another == "Y":
            continue
        elif Another == "n" or Another == "N":
            print("\n")
            print("Thank you for playing")
            break
        else:
            print("You need to enter y/n")
            continue
except:
    print("Please enter an integer")