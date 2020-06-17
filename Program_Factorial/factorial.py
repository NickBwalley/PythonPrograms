#function factorial
def factorialNumber(num):
    if (num == 1):
        return 1
    else:
        return num*factorialNumber(num-1)

num = int(input("Enter a Number: "))

print("The factorial of {0} is: ".format(num)+str(factorialNumber(num)))

