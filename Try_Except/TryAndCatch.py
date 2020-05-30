#Try_Except_Block
try:
    Number = int(input("Enter Your Favorite Number: "))
    print(Number)
    Division = 10/0
    print(Division)
except ZeroDivisionError:
    print("You Can't Divide a Number by Zero!..")
except ValueError:
    print("Invalid Input!..Integers Only!...")