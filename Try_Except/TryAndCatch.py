#Try_Except_Block
try:
    Number = int(input("Enter Your Favorite Number: "))
    print(Number)
    Division = 10/0
    print(Division)
except ZeroDivisionError as err:
    print(err)#prints out a specific error (divided by zero )
except ValueError as value:
    print(value)#prints out the compiler error