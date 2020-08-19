def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


num1 = float(input("Enter First Number: \n"))
num2 = float(input("Enter Second Number: \n"))
print("Select Operation to carry out!.. \n "
      "1. Addition \n"
      "2. Subtraction \n"
      "3. Multiplication \n"
      "4. Division \n")
choice = int(input("Enter Choice: (1/2/3/4): "))
if choice == 1:
    print(num1, "+", num2, "= ", add(num1, num2))
elif choice == 2:
    print(num1, "-", num2, "= ", subtract(num1, num2))
elif choice == 3:
    print(num1, "*", num2, "= ", multiply(num1, num2))
elif choice == 4:
    print(num1, "/", num2, "= ", divide(num1, num2))
else:
    print("Invalid Inputs!.. Please Try Again!..")
